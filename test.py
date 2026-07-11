#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import quote, unquote, urljoin, urlsplit
from zipfile import ZipFile

import requests
import rpmfile


MAPPING_TYPE: Dict[str, Optional[str]] = {
    "pip": "pypi",
    "python": "pypi",
    "pypi": "pypi",

    "npm": "npm",
    "yarn": "npm",

    "conan": "conan",

    "gomod": "go",
    "go": "go",
    "golang": "go",

    "cargo": "cargo",

    "composer": "composer",

    "pom": "maven",
    "maven": "maven",
    "gradle": "maven",

    "nuget": "nuget",

    "gem": "gem",
    "rubygems": "gem",
    "bundler": "gem",
}

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "gost-sbom-convert/3.4"})


def log(msg: str, args=None) -> None:
    if args is None:
        print(msg)
        return
    if getattr(args, "verbose", False):
        print(msg)


def add_error(
    errors: List[dict],
    stage: str,
    message: str,
    component: str = "",
    extra: Optional[dict] = None,
) -> None:
    rec = {
        "stage": stage,
        "component": component,
        "message": message,
    }
    if extra:
        rec.update(extra)
    errors.append(rec)


def debug_sbom_summary(sbom: dict, args) -> None:
    if not getattr(args, "debug", False):
        return

    comps = sbom.get("components")
    deps = sbom.get("dependencies")

    print("DEBUG: top-level keys:", sorted(list(sbom.keys())))

    if isinstance(comps, list):
        print("DEBUG: components count:", len(comps))
        type_counts: Dict[str, int] = {}
        for c in comps:
            if isinstance(c, dict):
                t = str(c.get("type") or "").strip().lower()
                type_counts[t] = type_counts.get(t, 0) + 1
        top_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)[:12]
        print("DEBUG: top component types:", top_types)
    else:
        print("DEBUG: components is not a list. value type:", type(comps).__name__)

    if isinstance(deps, list):
        print("DEBUG: dependencies count:", len(deps))
        root_ref = (((sbom.get("metadata") or {}).get("component") or {}).get("bom-ref"))
        print("DEBUG: metadata.component.bom-ref:", root_ref)
    else:
        print("DEBUG: dependencies is not a list. value type:", type(deps).__name__)


# ============================================================
# CycloneDX dependency graph helpers
# ============================================================
def build_dep_map(sbom: dict) -> Dict[str, Set[str]]:
    dep_map: Dict[str, Set[str]] = {}
    for d in sbom.get("dependencies", []) or []:
        if not isinstance(d, dict):
            continue
        ref = d.get("ref")
        if not isinstance(ref, str) or not ref:
            continue
        depends = d.get("dependsOn") or []
        s: Set[str] = set()
        if isinstance(depends, list):
            for x in depends:
                if isinstance(x, str) and x:
                    s.add(x)
        dep_map[ref] = s
    return dep_map


def build_component_map(sbom: dict) -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    for c in sbom.get("components", []) or []:
        if not isinstance(c, dict):
            continue
        br = c.get("bom-ref")
        if isinstance(br, str) and br:
            out[br] = c
    return out


def build_ref_to_bomref_map(sbom: dict) -> Dict[str, str]:
    m: Dict[str, str] = {}
    comps = sbom.get("components")
    if not isinstance(comps, list):
        return m

    for c in comps:
        if not isinstance(c, dict):
            continue
        bom = c.get("bom-ref")
        if not isinstance(bom, str) or not bom:
            continue

        m[bom] = bom

        purl = c.get("purl")
        if isinstance(purl, str) and purl:
            m[purl] = bom

        props = c.get("properties") or []
        if isinstance(props, list):
            for prop in props:
                if not isinstance(prop, dict):
                    continue
                if prop.get("name") == "aquasecurity:trivy:PkgID":
                    val = prop.get("value")
                    if isinstance(val, str) and val:
                        m[val] = bom

        name = (c.get("name") or "").strip()
        ver = (c.get("version") or "").strip()
        if name and ver:
            m[f"{name}@{ver}"] = bom

    return m


def component_is_library_like(c: Optional[dict]) -> bool:
    if not c or not isinstance(c, dict):
        return False
    t = (c.get("type") or "").strip().lower()
    return t in ("library", "framework")


def normalize_ref_to_bom(ref: str, ref2bom: Dict[str, str]) -> str:
    if not isinstance(ref, str) or not ref:
        return ""
    return ref2bom.get(ref, ref)


def compute_direct_library_bomrefs(sbom: dict, args=None) -> Optional[Set[str]]:
    root = (((sbom.get("metadata") or {}).get("component") or {}).get("bom-ref"))
    if not isinstance(root, str) or not root:
        return None

    dep_map = build_dep_map(sbom)
    comp_map = build_component_map(sbom)
    ref2bom = build_ref_to_bomref_map(sbom)

    direct_refs_raw = dep_map.get(root, set())
    if not direct_refs_raw:
        return set()

    direct_nodes = {normalize_ref_to_bom(r, ref2bom) for r in direct_refs_raw}
    direct_nodes.discard("")

    out: Set[str] = set()
    visited: Set[str] = set()

    def walk(node: str, depth_left: int) -> None:
        if not node or node in visited:
            return
        visited.add(node)

        c = comp_map.get(node)
        if component_is_library_like(c):
            out.add(node)
            return

        if depth_left <= 0:
            return

        kids_raw = dep_map.get(node, set())
        kids = {normalize_ref_to_bom(k, ref2bom) for k in kids_raw}
        kids.discard("")

        for k in kids:
            ck = comp_map.get(k)
            if component_is_library_like(ck):
                out.add(k)
            else:
                walk(k, depth_left - 1)

    for n in direct_nodes:
        walk(n, depth_left=2)

    if getattr(args, "debug", False) and args is not None:
        print("DEBUG: resolved direct libraries count:", len(out))

    return out


# ============================================================
# OS packages (rpm/deb)
# ============================================================
RPM_SRC_RE = re.compile(r"^(?P<name>.+)-(?P<ver>[^-]+-[^-]+)\.src\.rpm$", re.IGNORECASE)
RPM_RE = re.compile(r"^(?P<name>.+)-(?P<ver>[^-]+-[^-]+)\.[^.]+\.rpm$", re.IGNORECASE)
DEB_RE = re.compile(r"^(?P<name>[^_]+)_(?P<ver>[^_]+)_.+\.deb$", re.IGNORECASE)


def get_rpm_buildhost(path: Path, errors: Optional[List[dict]] = None) -> str:
    try:
        with rpmfile.open(str(path)) as rpm:
            v = rpm.headers.get("buildhost")
            if isinstance(v, bytes):
                return v.decode("utf-8", errors="ignore").strip()
            return str(v or "").strip()
    except Exception as e:
        if errors is not None:
            add_error(errors, "rpm_buildhost", str(e), component=str(path))
        return ""


def collect_os_pkgs(
    dir_path: str,
    ok_components: List[dict],
    error_components: List[dict],
    errors: Optional[List[dict]] = None,
) -> None:
    if not dir_path:
        return
    p = Path(dir_path)
    if not p.exists():
        return

    for fp in sorted(p.rglob("*")):
        if not fp.is_file():
            continue

        base_raw = fp.name
        low = base_raw.lower()
        if not (low.endswith(".rpm") or low.endswith(".deb")):
            continue

        base = unquote(base_raw)

        name = ""
        ver = ""
        kind = ""

        if base.lower().endswith(".rpm"):
            b = base[:-4]
            if "_" in b:
                name = b.split("_", 1)[0].strip()
                ver = b.split("_", 1)[1].strip()
                kind = "rpm"

        if not name:
            m = RPM_SRC_RE.match(base)
            if m:
                name = m.group("name")
                ver = m.group("ver")
                kind = "rpm"
            else:
                m = RPM_RE.match(base)
                if m:
                    name = m.group("name")
                    ver = m.group("ver")
                    kind = "rpm"
                else:
                    m = DEB_RE.match(base)
                    if m:
                        name = m.group("name")
                        ver = m.group("ver")
                        kind = "deb"

        if not name:
            if errors is not None:
                add_error(
                    errors,
                    stage="os_pkg_parse",
                    component=str(fp),
                    message="failed to parse package name/version from filename",
                )
            error_components.append(
                {
                    "type": "library",
                    "name": base_raw,
                    "version": "",
                    "properties": [
                        {"name": "GOST:attack_surface", "value": "no"},
                        {"name": "GOST:security_function", "value": "no"},
                    ],
                }
            )
            continue

        comp: Dict[str, Any] = {
            "type": "library",
            "name": name,
            "version": ver,
            "properties": [
                {"name": "GOST:attack_surface", "value": "no"},
                {"name": "GOST:security_function", "value": "no"},
            ],
        }

        if kind == "rpm":
            buildhost = get_rpm_buildhost(fp, errors=errors)

            if buildhost.lower().endswith("altlinux.org"):
                comp["properties"] += [
                    {"name": "GOST:provided_by", "value": "Alt Linux"},
                    {"name": "rpm", "value": base_raw},
                ]
                ok_components.append(comp)
            else:
                comp["properties"] += [
                    {"name": "rpm", "value": base_raw},
                ]
                comp["externalReferences"] = [{"type": "vcs", "url": buildhost or ""}]
                error_components.append(comp)

                if errors is not None:
                    add_error(
                        errors,
                        stage="rpm_buildhost_not_altlinux",
                        component=f"{name}@{ver}",
                        message="rpm buildhost does not end with altlinux.org",
                        extra={"rpm_file": base_raw, "buildhost": buildhost},
                    )
        else:
            comp["properties"] += [
                {"name": "GOST:provided_by", "value": "Astra Linux"},
                {"name": "deb", "value": base_raw},
            ]
            ok_components.append(comp)


# ============================================================
# PURL parsing
# ============================================================
def parse_purl(purl: str) -> Optional[Tuple[str, str, str]]:
    if not purl or not purl.startswith("pkg:"):
        return None
    try:
        s = purl[4:]
        s = s.split("?", 1)[0].split("#", 1)[0]
        eco, tail = s.split("/", 1)
        name, ver = tail.rsplit("@", 1)
        name = unquote(name)
        return eco.lower().strip(), name, ver
    except Exception:
        return None


# ============================================================
# Dist URL resolvers
# ============================================================
def pypi_sdist_url(name: str, version: str) -> str:
    r = SESSION.get(f"https://pypi.org/pypi/{name}/{version}/json", timeout=30)
    r.raise_for_status()
    data = r.json()
    for u in data.get("urls", []) or []:
        if u.get("packagetype") == "sdist" and u.get("url"):
            return str(u["url"])
    for u in data.get("urls", []) or []:
        if u.get("url"):
            return str(u["url"])
    return ""


def npm_dist_url(name: str, version: str) -> str:
    if not name or not version:
        return ""
    enc_name = quote(name, safe="@/")
    url = f"https://registry.npmjs.org/{enc_name}/{quote(version, safe='')}"
    r = SESSION.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    dist = data.get("dist") or {}
    tar = dist.get("tarball") or ""
    return str(tar) if isinstance(tar, str) else ""


def cargo_sdist_url(name: str, version: str) -> str:
    if not name or not version:
        return ""
    return f"https://crates.io/api/v1/crates/{quote(name, safe='')}/{quote(version, safe='')}/download"


def go_sdist_url(module: str, version: str) -> str:
    if not module or not version:
        return ""
    mod = quote(module, safe="/")
    ver = quote(version, safe="")
    return f"https://proxy.golang.org/{mod}/@v/{ver}.zip"


def composer_packagist_metadata(name: str) -> Optional[dict]:
    encoded = quote(name, safe="/")
    r = SESSION.get(f"https://repo.packagist.org/p2/{encoded}.json", timeout=30)
    r.raise_for_status()
    return r.json()


def composer_dist_url(name: str, version: str) -> str:
    data = composer_packagist_metadata(name)
    packages = data.get("packages") or {}
    vers = packages.get(name) or []
    for v in vers:
        if (
            (v.get("version") or "").strip() == version
            or (v.get("version_normalized") or "").strip() == version
        ):
            dist = v.get("dist") or {}
            url = dist.get("url") or ""
            if isinstance(url, str) and url.strip():
                return url.strip()
    return ""


def parse_maven_name(name: str) -> Optional[Tuple[str, str]]:
    if not name:
        return None

    if ":" in name:
        group, artifact = name.split(":", 1)
    elif "/" in name:
        group, artifact = name.split("/", 1)
    else:
        return None

    group = group.strip()
    artifact = artifact.strip()
    if not group or not artifact:
        return None
    return group, artifact


def url_exists(url: str) -> bool:
    try:
        r = SESSION.head(url, timeout=20, allow_redirects=True)
        if r.status_code == 200:
            return True
        if r.status_code in (403, 405):
            r2 = SESSION.get(url, stream=True, timeout=20, allow_redirects=True)
            return r2.status_code == 200
        return False
    except Exception:
        return False


def maven_dist_url(group: str, artifact: str, version: str, args=None) -> str:
    gpath = "/".join(group.split("."))
    base = f"https://repo1.maven.org/maven2/{gpath}/{quote(artifact, safe='')}/{quote(version, safe='')}"
    a = quote(artifact, safe="")
    v = quote(version, safe="")

    candidates = [
        f"{base}/{a}-{v}-sources.jar",
        f"{base}/{a}-{v}-source.jar",
        f"{base}/{a}-{v}.jar",
    ]

    for u in candidates:
        if url_exists(u):
            log(f"maven picked: {u}", args)
            return u

    return ""


def rubygems_dist_url(name: str, version: str) -> str:
    if not name or not version:
        return ""
    safe_name = quote(name, safe=".+-_")
    safe_ver = quote(version, safe=".+-_")
    return f"https://rubygems.org/downloads/{safe_name}-{safe_ver}.gem"


def conan_sdist_url(name: str, version: str) -> str:
    return ""


def resolve_dist_url(ecosystem: str, pkg_name: str, pkg_ver: str, args=None) -> str:
    if ecosystem == "pypi":
        return pypi_sdist_url(pkg_name, pkg_ver)
    if ecosystem == "npm":
        return npm_dist_url(pkg_name, pkg_ver)
    if ecosystem == "cargo":
        return cargo_sdist_url(pkg_name, pkg_ver)
    if ecosystem == "go":
        return go_sdist_url(pkg_name, pkg_ver)
    if ecosystem == "composer":
        return composer_dist_url(pkg_name, pkg_ver)
    if ecosystem == "maven":
        parsed = parse_maven_name(pkg_name)
        if not parsed:
            return ""
        g, a = parsed
        return maven_dist_url(g, a, pkg_ver, args=args)
    if ecosystem == "gem":
        return rubygems_dist_url(pkg_name, pkg_ver)
    if ecosystem == "conan":
        return conan_sdist_url(pkg_name, pkg_ver)
    return ""


# ============================================================
# NuGet helpers
# ============================================================
NUGET_SOURCE_REPO_HREF_RE = re.compile(
    r'<a[^>]+href="(?P<href>[^"]+)"[^>]*>\s*Source repository\s*</a>',
    re.IGNORECASE,
)
SEMVER_RE = re.compile(r"^v?(?P<maj>\d+)\.(?P<min>\d+)(?:\.(?P<pat>\d+))?(?:[-+].*)?$")
NUGET_INFO_REPO_RE = re.compile(
    r'Url:\s*<a[^>]+href="(?P<url>[^"]+)"',
    re.IGNORECASE,
)
NUGET_INFO_COMMIT_RE = re.compile(
    r'Commit:\s*(?P<commit>[0-9a-fA-F]{7,40})',
    re.IGNORECASE,
)
NUSPEC_REPOSITORY_RE = re.compile(
    r'<repository\b[^>]*\burl="(?P<url>[^"]+)"[^>]*\bcommit="(?P<commit>[0-9a-fA-F]{7,40})"[^>]*/?>',
    re.IGNORECASE,
)
NUSPEC_REPOSITORY_RE_ALT = re.compile(
    r'<repository\b[^>]*\bcommit="(?P<commit>[0-9a-fA-F]{7,40})"[^>]*\burl="(?P<url>[^"]+)"[^>]*/?>',
    re.IGNORECASE,
)


def _fetch_json_safe(url: str) -> Optional[dict]:
    if not isinstance(url, str):
        return None
    url = url.strip()
    if not url:
        return None
    try:
        r = SESSION.get(url, timeout=30)
        if r.status_code != 200:
            return None
        data = r.json()
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _merge_dicts_shallow(base: dict, extra: dict) -> dict:
    if not isinstance(base, dict):
        base = {}
    if not isinstance(extra, dict):
        return dict(base)
    merged = dict(extra)
    merged.update(base)
    return merged


def _extract_catalog_entry(data: dict) -> dict:
    if not isinstance(data, dict):
        return {}

    if "id" in data and "version" in data and (
        "repository" in data or "projectUrl" in data or "packageContent" in data
    ):
        return data

    def resolve_catalog_entry(entry) -> dict:
        if isinstance(entry, dict):
            entry_url = entry.get("@id")
            if isinstance(entry_url, str):
                sub = _fetch_json_safe(entry_url)
                if isinstance(sub, dict):
                    return _merge_dicts_shallow(entry, sub)
            return entry
        if isinstance(entry, str):
            sub = _fetch_json_safe(entry)
            if isinstance(sub, dict):
                return sub
        return {}

    catalog_entry = data.get("catalogEntry")
    if catalog_entry is not None:
        resolved = resolve_catalog_entry(catalog_entry)
        if resolved:
            return resolved

    items = data.get("items") or []
    if isinstance(items, list):
        for outer in items:
            if not isinstance(outer, dict):
                continue
            inner_items = outer.get("items") or []
            if not isinstance(inner_items, list):
                continue
            for inner in inner_items:
                if not isinstance(inner, dict):
                    continue
                inner_catalog_entry = inner.get("catalogEntry")
                if inner_catalog_entry is None:
                    continue
                resolved = resolve_catalog_entry(inner_catalog_entry)
                if resolved:
                    return resolved

    return {}


def get_nuget_registration_base_url() -> str:
    service_index_url = "https://api.nuget.org/v3/index.json"
    r = SESSION.get(service_index_url, timeout=30)
    r.raise_for_status()
    data = r.json()

    resources = data.get("resources") or []
    if not isinstance(resources, list):
        raise ValueError("NuGet service index has no resources array")

    preferred_types = [
        "RegistrationsBaseUrl/Versioned",
        "RegistrationsBaseUrl/3.6.0",
        "RegistrationsBaseUrl/3.4.0",
        "RegistrationsBaseUrl/3.0.0-rc",
        "RegistrationsBaseUrl/3.0.0-beta",
    ]

    for wanted in preferred_types:
        for resource in resources:
            if not isinstance(resource, dict):
                continue
            if resource.get("@type") == wanted:
                rid = resource.get("@id")
                if isinstance(rid, str) and rid.strip():
                    return rid.rstrip("/")

    for resource in resources:
        if not isinstance(resource, dict):
            continue
        rtype = resource.get("@type")
        rid = resource.get("@id")
        if (
            isinstance(rtype, str)
            and "RegistrationsBaseUrl" in rtype
            and isinstance(rid, str)
            and rid.strip()
        ):
            return rid.rstrip("/")

    raise ValueError("NuGet RegistrationsBaseUrl not found in service index")


def looks_like_git_repo(url: str) -> bool:
    if not isinstance(url, str):
        return False
    normalized = url.strip().lower()
    if not normalized:
        return False
    if normalized.startswith("git@"):
        return True
    if normalized.endswith(".git"):
        return True
    if any(host in normalized for host in ("github.com/", "gitlab.com/", "bitbucket.org/", "dev.azure.com/", "visualstudio.com/")):
        return True
    return False


def _http_ok(url: str, args=None) -> bool:
    try:
        r = SESSION.head(url, timeout=15, allow_redirects=True)
        if r.status_code == 200:
            return True
        if r.status_code in (403, 405):
            r2 = SESSION.get(url, timeout=15, allow_redirects=True)
            return r2.status_code == 200
        return False
    except Exception as e:
        log(f"http check failed {url}: {e}", args)
        return False


def build_version_candidates(version: str) -> List[str]:
    version = (version or "").strip()
    if not version:
        return []

    m = SEMVER_RE.match(version)
    if not m:
        vals = [version, f"v{version}"]
        out: List[str] = []
        seen: Set[str] = set()
        for v in vals:
            if v and v not in seen:
                out.append(v)
                seen.add(v)
        return out

    maj = m.group("maj")
    mi = m.group("min")
    pat = m.group("pat") or ""

    candidates: List[str] = []

    if pat:
        candidates += [
            version,
            f"v{version}",
            f"release-{version}",
            f"Release-{version}",
            f"release/{version}",
            f"releases/{version}",
            f"release-v{version}",
            f"release/v{version}",
            f"{maj}.{mi}.{pat}.0",
            f"v{maj}.{mi}.{pat}.0",
            f"{maj}_{mi}_{pat}",
            f"v{maj}_{mi}_{pat}",
            f"{maj}-{mi}-{pat}",
            f"v{maj}-{mi}-{pat}",
        ]

    candidates += [
        f"{maj}.{mi}",
        f"v{maj}.{mi}",
        f"release-{maj}.{mi}",
        f"Release-{maj}.{mi}",
    ]

    seen: Set[str] = set()
    out: List[str] = []
    for x in candidates:
        if x and x not in seen:
            out.append(x)
            seen.add(x)
    return out


def normalize_repo_url(repo_url: str) -> str:
    repo_url = (repo_url or "").strip()
    if repo_url.endswith(".git"):
        repo_url = repo_url[:-4]
    return repo_url.rstrip("/")


def github_find_tag_url(repo_url: str, version: str, args=None) -> str:
    repo_url = normalize_repo_url(repo_url)
    if not repo_url or "github.com" not in repo_url.lower():
        return ""

    for cand in build_version_candidates(version):
        candidates = [
            f"{repo_url}/tree/{quote(cand, safe='/:@._-')}",
            f"{repo_url}/releases/tag/{quote(cand, safe='/:@._-')}",
        ]
        for u in candidates:
            if _http_ok(u, args=args):
                log(f"github version tag found: {u}", args)
                return u
    return ""


def vcs_find_version_ref(repo_url: str, version: str, args=None) -> str:
    repo_url = (repo_url or "").strip()
    if not repo_url or not version:
        return ""

    if "github.com" in repo_url.lower():
        return github_find_tag_url(repo_url, version, args=args)

    return ""


def nuget_gallery_source_repo_url(package_id: str, version: str, args=None) -> str:
    package_id = (package_id or "").strip()
    version = (version or "").strip()
    if not package_id:
        return ""

    candidates = [
        f"https://www.nuget.org/packages/{quote(package_id, safe='')}/{quote(version, safe='')}" if version else "",
        f"https://www.nuget.org/packages/{quote(package_id, safe='')}",
    ]

    for page_url in candidates:
        if not page_url:
            continue
        try:
            r = SESSION.get(page_url, timeout=30)
            if r.status_code != 200:
                continue

            html = r.text or ""
            m = NUGET_SOURCE_REPO_HREF_RE.search(html)
            if not m:
                continue

            href = (m.group("href") or "").strip()
            if not href:
                continue

            href = urljoin(page_url, href)
            log(f"nuget gallery source repo found: {href}", args)
            return href
        except Exception as e:
            log(f"nuget gallery parse error {page_url}: {e}", args)

    return ""


def nuget_repo_url(package_id: str, version: str, args=None) -> str:
    package_id = (package_id or "").strip()
    version = (version or "").strip()
    if not package_id or not version:
        return ""

    gallery_repo = nuget_gallery_source_repo_url(package_id, version, args=args)
    if gallery_repo:
        return gallery_repo

    try:
        reg_base = get_nuget_registration_base_url()
    except Exception as e:
        log(f"nuget registration base error: {e}", args)
        return ""

    reg_index_url = f"{reg_base}/{quote(package_id.lower(), safe='')}/index.json"
    try:
        r = SESSION.get(reg_index_url, timeout=30)
        if r.status_code == 200:
            data = r.json()
        else:
            data = {}
    except Exception as e:
        log(f"nuget registration read error {package_id}@{version}: {e}", args)
        return ""

    catalog = {}
    items = data.get("items") or []

    if isinstance(items, list):
        version_lower = version.lower()
        for page in items:
            if not isinstance(page, dict):
                continue

            page_items = page.get("items")
            if not isinstance(page_items, list):
                page_url = page.get("@id")
                if isinstance(page_url, str):
                    page_data = _fetch_json_safe(page_url)
                    if isinstance(page_data, dict):
                        page_items = page_data.get("items")

            if not isinstance(page_items, list):
                continue

            for leaf in page_items:
                if not isinstance(leaf, dict):
                    continue

                catalog_entry = leaf.get("catalogEntry")
                leaf_version = None

                if isinstance(catalog_entry, dict):
                    leaf_version = catalog_entry.get("version")
                elif isinstance(catalog_entry, str):
                    leaf_data = _fetch_json_safe(catalog_entry)
                    if isinstance(leaf_data, dict):
                        catalog_entry = leaf_data
                        leaf_version = leaf_data.get("version")

                if isinstance(leaf_version, str) and leaf_version.lower() == version_lower:
                    if isinstance(catalog_entry, dict):
                        catalog = _extract_catalog_entry(catalog_entry)
                        if catalog:
                            break
            if catalog:
                break

    if not isinstance(catalog, dict) or not catalog:
        catalog = _extract_catalog_entry(data if isinstance(data, dict) else {})

    if not isinstance(catalog, dict) or not catalog:
        return ""

    repo_url = ""
    repo_info = catalog.get("repository")
    if isinstance(repo_info, dict):
        val = repo_info.get("url")
        if isinstance(val, str) and val.strip():
            repo_url = val.strip()
    elif isinstance(repo_info, str) and repo_info.strip():
        repo_url = repo_info.strip()

    if repo_url.startswith(("http://", "https://", "git@")):
        return repo_url

    project_url = catalog.get("projectUrl")
    if isinstance(project_url, str) and project_url.strip().startswith(("http://", "https://", "git@")):
        return project_url.strip()

    return ""


def github_commit_url(repo_url: str, commit: str) -> str:
    repo_url = normalize_repo_url(repo_url)
    commit = (commit or "").strip()
    if not repo_url or not commit:
        return ""
    return f"{repo_url}/commit/{quote(commit, safe='')}"


def nuget_info_repo_and_commit(package_id: str, version: str, args=None) -> Tuple[str, str]:
    package_id = (package_id or "").strip()
    version = (version or "").strip()
    if not package_id or not version:
        return "", ""

    page_url = f"https://nuget.info/packages/{quote(package_id, safe='')}/{quote(version, safe='')}"
    try:
        r = SESSION.get(page_url, timeout=30)
        if r.status_code != 200:
            log(f"nuget.info not available: {page_url} status={r.status_code}", args)
            return "", ""

        html = r.text or ""
        repo = ""
        commit = ""

        m_repo = NUGET_INFO_REPO_RE.search(html)
        if m_repo:
            repo = (m_repo.group("url") or "").strip()

        m_commit = NUGET_INFO_COMMIT_RE.search(html)
        if m_commit:
            commit = (m_commit.group("commit") or "").strip()

        if repo or commit:
            log(f"nuget.info fallback found repo={repo} commit={commit}", args)

        return repo, commit

    except Exception as e:
        log(f"nuget.info parse error {package_id}@{version}: {e}", args)
        return "", ""


def nuget_nupkg_url(package_id: str, version: str) -> str:
    package_id = (package_id or "").strip()
    version = (version or "").strip()
    if not package_id or not version:
        return ""
    lower_id = package_id.lower()
    lower_ver = version.lower()
    return (
        f"https://api.nuget.org/v3-flatcontainer/"
        f"{quote(lower_id, safe='')}/{quote(lower_ver, safe='')}/"
        f"{quote(lower_id, safe='')}.{quote(lower_ver, safe='')}.nupkg"
    )


def download_bytes_soft(url: str, args=None) -> Tuple[bytes, str]:
    if not url:
        return b"", "empty_url"
    try:
        with SESSION.get(url, timeout=60, allow_redirects=True) as r:
            if r.status_code != 200:
                msg = f"download_failed_status_{r.status_code}"
                log(f"{msg} url={url}", args)
                return b"", msg
            return r.content or b"", ""
    except Exception as e:
        log(f"download bytes error url={url} error={e}", args)
        return b"", str(e)


def nuget_nuspec_repo_and_commit(package_id: str, version: str, args=None) -> Tuple[str, str]:
    nupkg_url = nuget_nupkg_url(package_id, version)
    if not nupkg_url:
        return "", ""

    raw, err = download_bytes_soft(nupkg_url, args=args)
    if not raw:
        log(f"nupkg download failed {package_id}@{version}: {err}", args)
        return "", ""

    try:
        import io
        with ZipFile(io.BytesIO(raw)) as zf:
            nuspec_names = [n for n in zf.namelist() if n.lower().endswith(".nuspec")]
            if not nuspec_names:
                return "", ""

            nuspec_name = nuspec_names[0]
            text = zf.read(nuspec_name).decode("utf-8", errors="ignore")

            m = NUSPEC_REPOSITORY_RE.search(text)
            if not m:
                m = NUSPEC_REPOSITORY_RE_ALT.search(text)
            if not m:
                return "", ""

            repo = (m.group("url") or "").strip()
            commit = (m.group("commit") or "").strip()
            if repo or commit:
                log(f"nuspec repo+commit found repo={repo} commit={commit}", args)
            return repo, commit
    except Exception as e:
        log(f"nupkg nuspec parse error {package_id}@{version}: {e}", args)
        return "", ""


def nuget_fallback_version_ref(package_id: str, version: str, repo_url: str, args=None) -> str:
    info_repo, info_commit = nuget_info_repo_and_commit(package_id, version, args=args)

    final_repo = info_repo or repo_url
    if final_repo and info_commit and "github.com" in final_repo.lower():
        return github_commit_url(final_repo, info_commit)

    nuspec_repo, nuspec_commit = nuget_nuspec_repo_and_commit(package_id, version, args=args)
    final_repo = nuspec_repo or final_repo or repo_url
    if final_repo and nuspec_commit and "github.com" in final_repo.lower():
        return github_commit_url(final_repo, nuspec_commit)

    return ""


# ============================================================
# Download + hash via cpverify.exe
# ============================================================
HEX64_RE = re.compile(r"\b[0-9A-Fa-f]{64}\b")


def safe_filename_from_url(url: str) -> str:
    try:
        path = urlsplit(url).path
        base = os.path.basename(path).strip()
        return base or "download.bin"
    except Exception:
        return "download.bin"


def download_archive_soft(url: str, download_dir: str, args=None) -> Tuple[Optional[str], str]:
    if not url:
        return None, "empty_url"

    os.makedirs(download_dir, exist_ok=True)

    url_id = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    base = safe_filename_from_url(url)
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base)
    out_path = os.path.join(download_dir, f"{base}.{url_id}")

    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        log(f"download cache hit: {out_path}", args)
        return out_path, ""

    tmp = out_path + ".part"
    try:
        log(f"download GET {url}", args)
        with SESSION.get(url, stream=True, timeout=120, allow_redirects=True) as r:
            if r.status_code != 200:
                msg = f"download_failed_status_{r.status_code}"
                log(f"{msg} url={url}", args)
                return None, msg

            with open(tmp, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

        os.replace(tmp, out_path)

        if os.path.getsize(out_path) <= 0:
            msg = "download_failed_empty_file"
            log(f"{msg} url={url}", args)
            return None, msg

        log(f"download OK -> {out_path}", args)
        return out_path, ""

    except Exception as e:
        log(f"download error url={url} error={e}", args)
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
        return None, str(e)


def cpverify_streebog256_soft(cpverify_path: str, file_path: str, args=None) -> Tuple[str, str]:
    try:
        result = subprocess.run(
            [cpverify_path, "-mk", "-alg", "GR3411_2012_256", "-f", file_path],
            capture_output=True,
            text=True,
            check=False,
        )
        out = ((result.stdout or "") + "\n" + (result.stderr or "")).strip()

        if result.returncode != 0:
            log(f"cpverify failed file={file_path} out={out[:4000]}", args)
            return "", out[:4000] or f"cpverify_exit_code_{result.returncode}"

        m = HEX64_RE.search(out)
        if m:
            return m.group(0).upper(), ""

        log(f"cpverify output not parsed file={file_path} out={out[:4000]}", args)
        return "", "cpverify_output_not_parsed"

    except Exception as e:
        log(f"cpverify exception file={file_path} error={e}", args)
        return "", str(e)


def download_and_hash_soft(
    dist_url: str,
    download_dir: str,
    cpverify_path: str,
    args=None,
) -> Tuple[str, str, str]:
    local, err = download_archive_soft(dist_url, download_dir, args=args)
    if not local:
        return "", "", err

    h, hash_err = cpverify_streebog256_soft(cpverify_path, local, args=args)
    if not h:
        return local, "", hash_err

    return local, h, ""


# ============================================================
# GOST helpers
# ============================================================
def gost_props_for_type(cdx_type: str) -> List[dict]:
    t = (cdx_type or "").lower().strip()
    if t == "framework":
        return [
            {"name": "GOST:attack_surface", "value": "yes"},
            {"name": "GOST:security_function", "value": "yes"},
        ]
    return [
        {"name": "GOST:attack_surface", "value": "no"},
        {"name": "GOST:security_function", "value": "no"},
    ]


def should_skip_component(c: dict) -> bool:
    t = (c.get("type") or "").lower().strip()
    if t not in ("library", "framework"):
        return True
    name = (c.get("name") or "").strip()
    purl = (c.get("purl") or "").strip()
    if not name and not purl:
        return True
    return False


def component_dedupe_key(c: dict) -> str:
    ctype = (c.get("type") or "").strip().lower()
    purl = (c.get("purl") or "").strip()
    name = (c.get("name") or "").strip()
    ver = (c.get("version") or "").strip()
    if purl:
        return f"{ctype}|purl:{purl}"
    return f"{ctype}|name:{name}|ver:{ver}"


def unique_input_components(sbom: dict, allowed_bomrefs: Optional[Set[str]], args) -> List[dict]:
    out: List[dict] = []
    seen: Set[str] = set()

    comps = sbom.get("components")
    if not isinstance(comps, list):
        if getattr(args, "debug", False):
            print("DEBUG: sbom['components'] missing or not list")
        return out

    for c in comps:
        if not isinstance(c, dict):
            continue

        bom_ref = c.get("bom-ref")
        if allowed_bomrefs is not None:
            if not isinstance(bom_ref, str) or bom_ref not in allowed_bomrefs:
                continue

        if should_skip_component(c):
            continue

        key = component_dedupe_key(c)
        if key in seen:
            continue
        seen.add(key)
        out.append(c)

    return out


def make_source_distribution_ref(url: str, hash_hex: str) -> dict:
    return {
        "type": "source-distribution",
        "url": url,
        "hashes": [{"alg": "STREEBOG-256", "content": (hash_hex or "")}],
    }


def get_app_metadata_from_input(sbom: dict) -> Tuple[str, str, str]:
    md = sbom.get("metadata") or {}
    comp = (md.get("component") or {}) if isinstance(md, dict) else {}
    name = str(comp.get("name") or "application")
    version = str(comp.get("version") or "0")

    manufacturer = ""
    man = comp.get("manufacturer")
    if isinstance(man, dict):
        manufacturer = str(man.get("name") or "").strip()
    if not manufacturer:
        manufacturer = "unknown"

    return name, version, manufacturer


def build_output_sbom_template(app_name: str, app_version: str, app_manufacturer: str) -> dict:
    return {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "component": {
                "type": "application",
                "name": app_name,
                "version": app_version,
                "manufacturer": {"name": app_manufacturer},
            }
        },
        "components": [],
    }


# ============================================================
# Convert
# ============================================================
def convert(input_sbom: str, target_dir: str, args, download_dir: str, cpverify_path: str) -> Tuple[str, str, str]:
    with open(input_sbom, encoding="utf-8") as f:
        sbom = json.load(f)

    errors: List[dict] = []

    debug_sbom_summary(sbom, args)

    allowed_bomrefs: Optional[Set[str]] = None
    if args.only_direct:
        allowed_bomrefs = compute_direct_library_bomrefs(sbom, args=args)
        if getattr(args, "debug", False) and allowed_bomrefs is not None:
            print("DEBUG: allowed_bomrefs (direct libraries) size:", len(allowed_bomrefs))

    in_components = unique_input_components(sbom, allowed_bomrefs, args)

    if getattr(args, "debug", False):
        total_in = len(sbom.get("components") or []) if isinstance(sbom.get("components"), list) else 0
        print("DEBUG: total input components:", total_in)
        print("DEBUG: after filtering + dedupe:", len(in_components))

    app_name, app_version, app_manufacturer = get_app_metadata_from_input(sbom)

    out_ok = build_output_sbom_template(app_name, app_version, app_manufacturer)
    out_err = build_output_sbom_template(app_name, app_version, app_manufacturer)

    for c in in_components:
        name = (c.get("name") or "").strip()
        ver = (c.get("version") or "").strip()
        purl = (c.get("purl") or "").strip()
        cdx_type = (c.get("type") or "library").strip()
        component_id = purl or f"{name}@{ver}"

        comp: Dict[str, Any] = {
            "type": cdx_type if cdx_type in ("library", "framework") else "library",
            "name": name,
            "version": ver,
            "properties": gost_props_for_type(cdx_type),
        }
        if purl:
            comp["purl"] = purl

        eco_raw = ""
        pkg_name = ""
        pkg_ver = ""
        if purl:
            pp = parse_purl(purl)
            if pp:
                eco_raw, pkg_name, pkg_ver = pp

        eco = MAPPING_TYPE.get((eco_raw or "").lower().strip(), (eco_raw or "").lower().strip())
        if getattr(args, "verbose", False):
            log(f"component: {name} {ver} purl={purl} eco={eco}", args)

        if eco == "nuget":
            use_name = pkg_name or name
            use_ver = pkg_ver or ver

            repo = nuget_repo_url(use_name, use_ver, args=args) or ""

            if not repo:
                info_repo, info_commit = nuget_info_repo_and_commit(use_name, use_ver, args=args)
                repo = info_repo or ""

                if info_repo and info_commit and "github.com" in info_repo.lower():
                    commit_url = github_commit_url(info_repo, info_commit)
                    comp["externalReferences"] = [{"type": "vcs", "url": commit_url}]
                    out_ok["components"].append(comp)
                    continue

                nuspec_repo, nuspec_commit = nuget_nuspec_repo_and_commit(use_name, use_ver, args=args)
                repo = nuspec_repo or repo
                if nuspec_repo and nuspec_commit and "github.com" in nuspec_repo.lower():
                    commit_url = github_commit_url(nuspec_repo, nuspec_commit)
                    comp["externalReferences"] = [{"type": "vcs", "url": commit_url}]
                    out_ok["components"].append(comp)
                    continue

            if not repo:
                comp["externalReferences"] = [{"type": "vcs", "url": ""}]
                add_error(
                    errors,
                    stage="nuget_repo_url_not_found",
                    component=component_id,
                    message="NuGet repository URL was not resolved",
                    extra={"ecosystem": eco, "name": use_name, "version": use_ver},
                )
                out_err["components"].append(comp)
                continue

            version_ref_url = vcs_find_version_ref(repo, use_ver, args=args)

            if version_ref_url:
                comp["externalReferences"] = [{"type": "vcs", "url": version_ref_url}]
                out_ok["components"].append(comp)
                continue

            commit_ref_url = nuget_fallback_version_ref(use_name, use_ver, repo, args=args)
            if commit_ref_url:
                comp["externalReferences"] = [{"type": "vcs", "url": commit_ref_url}]
                out_ok["components"].append(comp)
                continue

            comp["externalReferences"] = [{"type": "vcs", "url": repo}]
            add_error(
                errors,
                stage="nuget_version_ref_not_found",
                component=component_id,
                message="Repository was found, but neither version tag nor commit reference was found",
                extra={
                    "ecosystem": eco,
                    "name": use_name,
                    "version": use_ver,
                    "repo_url": repo,
                },
            )
            out_err["components"].append(comp)
            continue

        use_name = pkg_name or name
        use_ver = pkg_ver or ver

        dist_url = ""
        try:
            dist_url = resolve_dist_url(eco, use_name, use_ver, args=args)
        except Exception as e:
            add_error(
                errors,
                stage="resolve_dist_url",
                component=component_id,
                message=str(e),
                extra={"ecosystem": eco, "name": use_name, "version": use_ver},
            )
            comp["externalReferences"] = [make_source_distribution_ref("", "")]
            out_err["components"].append(comp)
            continue

        if not dist_url:
            add_error(
                errors,
                stage="dist_url_not_found",
                component=component_id,
                message="source URL was not resolved",
                extra={"ecosystem": eco, "name": use_name, "version": use_ver},
            )
            comp["externalReferences"] = [make_source_distribution_ref("", "")]
            out_err["components"].append(comp)
            continue

        _, h, err = download_and_hash_soft(dist_url, download_dir, cpverify_path, args=args)
        if not h:
            add_error(
                errors,
                stage="download_or_hash",
                component=component_id,
                message=err or "unknown download/hash error",
                extra={"url": dist_url, "ecosystem": eco, "name": use_name, "version": use_ver},
            )
            comp["externalReferences"] = [make_source_distribution_ref("", "")]
            out_err["components"].append(comp)
        else:
            comp["externalReferences"] = [make_source_distribution_ref(dist_url, h)]
            out_ok["components"].append(comp)

    if args.os_pkgs_dir:
        collect_os_pkgs(
            args.os_pkgs_dir,
            ok_components=out_ok["components"],
            error_components=out_err["components"],
            errors=errors,
        )

    gost_ok_path = os.path.join(target_dir, "gost.sbom.json")
    with open(gost_ok_path, "w", encoding="utf-8") as f:
        json.dump(out_ok, f, indent=2, ensure_ascii=False)

    gost_err_sbom_path = os.path.join(target_dir, "gost.errors.sbom.json")
    with open(gost_err_sbom_path, "w", encoding="utf-8") as f:
        json.dump(out_err, f, indent=2, ensure_ascii=False)

    errors_path = os.path.join(target_dir, "gost.errors.json")
    with open(errors_path, "w", encoding="utf-8") as f:
        json.dump(errors, f, indent=2, ensure_ascii=False)

    print("written:", gost_ok_path)
    print("written:", gost_err_sbom_path)
    print("errors:", errors_path)

    return gost_ok_path, gost_err_sbom_path, errors_path


# ============================================================
# Main
# ============================================================
def resolve_cpverify_path(positional: str) -> str:
    cand = (positional or "").strip()
    if not cand:
        cand = (os.environ.get("CPVERIFY_PATH") or "").strip()
    if not cand:
        cand = "cpverify.exe"

    if os.path.isfile(cand):
        return os.path.abspath(cand)

    found = shutil.which(cand)
    if found:
        return os.path.abspath(found)

    return cand


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Path to CycloneDX SBOM JSON")
    ap.add_argument(
        "cpverify",
        nargs="?",
        default="",
        help="Path to cpverify.exe (optional). If omitted, uses CPVERIFY_PATH env or searches PATH.",
    )

    ap.add_argument("--os-pkgs-dir", default="", help="Folder with .rpm/.deb archives")
    ap.add_argument(
        "--download-dir",
        default="",
        help="Where to store downloaded archives (default: <sbom_dir>/downloads)",
    )

    ap.add_argument("--only-direct", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--debug", action="store_true")

    args = ap.parse_args()

    input_sbom = os.path.abspath(args.input)
    if not os.path.isfile(input_sbom):
        raise SystemExit(f"input is not a file: {input_sbom}")

    cpverify_path = resolve_cpverify_path(args.cpverify)
    if not os.path.isfile(cpverify_path):
        raise SystemExit(
            "cpverify.exe not found. Provide it as 2nd positional arg, or set CPVERIFY_PATH, or put cpverify.exe into PATH.\n"
            f"Resolved cpverify path: {cpverify_path}"
        )

    target_dir = os.path.dirname(input_sbom)
    download_dir = args.download_dir or os.path.join(target_dir, "downloads")

    convert(input_sbom, target_dir, args, download_dir=download_dir, cpverify_path=cpverify_path)


if __name__ == "__main__":
    main()
