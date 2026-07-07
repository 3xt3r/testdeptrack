#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dedup_sboms.py — слияние нескольких CycloneDX SBOM в один с корректной
дедупликацией компонентов, БЕЗ потери цепочки зависимостей (dependencies).

Проблемы исходного варианта (_merge_sboms из sbom_tool.py), которые здесь
исправлены:

  1. Ключ дедупа был `purl or bom-ref or name`. Если у компонента нет purl
     (обычный случай для generic/OS-компонентов), дедуп скатывался на голое
     `name` — и два РАЗНЫХ компонента с одинаковым именем, но разными
     версиями, молча схлопывались в один (терялась версия).
     Здесь: ключ = purl, если есть; иначе (name, version); а если нет ни
     purl, ни version — считается уникальным и никогда не дедупится с
     другими такими же компонентами.

  2. Секция `dependencies` (граф "что от чего зависит") при слиянии вообще
     не переносилась — из нескольких входных SBOM бралось только
     `components`. Из-за этого после дедупа/слияния исчезала цепочка
     вызовов до уязвимого компонента.
     Здесь: dependencies собираются из всех входных файлов, а ссылки на
     удалённые дубликаты (bom-ref которых отличался от оставленного)
     перенаправляются («remap») на оставшийся компонент, чтобы граф
     остался целостным.

  3. Полная тишина — не было видно, что и почему задедуплено.
     Здесь: в stdout печатается, какой компонент отброшен и куда
     перенаправлена ссылка на него.

Использование:
    python3 dedup_sboms.py sbom1.json sbom2.json ... -o merged.json
    python3 dedup_sboms.py sbom1.json sbom2.json --name my-product -o merged.json
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _dedup_key(comp: dict) -> tuple:
    """
    Ключ дедупликации компонента.

    - Если есть purl — дедупим по нему (наиболее надёжный идентификатор
      конкретного пакета конкретной версии).
    - Иначе, если есть и name, и version — дедупим по паре (name, version).
    - Иначе (нет ни purl, ни version — например, голое имя без версии)
      считаем компонент уникальным: ключить по identity объекта, чтобы он
      НИКОГДА не считался дубликатом чего-либо ещё. Раньше именно этот
      случай ошибочно схлопывал разные компоненты по одному лишь `name`.
    """
    purl = comp.get("purl")
    if purl:
        return ("purl", purl)

    name, version = comp.get("name"), comp.get("version")
    if name and version:
        return ("name+version", name, version)

    return ("unique", id(comp))


def _resolve(ref: str, redirect: dict[str, str]) -> str:
    """Проходит по цепочке redirect (дубликат -> оставленный компонент)."""
    seen: set[str] = set()
    while ref in redirect and ref not in seen:
        seen.add(ref)
        ref = redirect[ref]
    return ref


def merge_sboms(sbom_files: list[Path], product_name: str) -> dict[str, Any]:
    merged_components: list[dict] = []
    seen_keys: dict[tuple, str] = {}      # dedup key -> bom-ref оставленного компонента
    ref_redirect: dict[str, str] = {}     # bom-ref дубликата -> bom-ref оставленного
    merged_dependencies: list[dict] = []
    n_dropped = 0
    n_deps_before = 0

    for f in sbom_files:
        if not f.exists():
            print(f"  [dedup] skip missing: {f}")
            continue
        try:
            sbom = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  [dedup] could not read {f}: {e}")
            continue

        for comp in sbom.get("components") or []:
            key = _dedup_key(comp)
            bom_ref = comp.get("bom-ref") or ""
            kept_ref = seen_keys.get(key)

            if kept_ref is not None:
                n_dropped += 1
                if bom_ref and bom_ref != kept_ref:
                    ref_redirect[bom_ref] = kept_ref
                print(
                    f"  [dedup] dropping duplicate: {comp.get('name')}@{comp.get('version')} "
                    f"(bom-ref {bom_ref!r} -> {kept_ref!r})"
                )
                continue

            if bom_ref:
                seen_keys[key] = bom_ref
            merged_components.append(comp)

        deps = sbom.get("dependencies") or []
        n_deps_before += len(deps)
        merged_dependencies.extend(deps)

    if n_dropped:
        print(f"  [dedup] dropped {n_dropped} duplicate component(s) total")
    else:
        print("  [dedup] no duplicates found")

    valid_refs = {c.get("bom-ref") for c in merged_components if c.get("bom-ref")}

    by_ref: dict[str, dict] = {}
    for entry in merged_dependencies:
        ref = _resolve(str(entry.get("ref") or ""), ref_redirect)
        if not ref or ref not in valid_refs:
            continue

        node = by_ref.setdefault(ref, {"ref": ref, "dependsOn": []})
        for dep in entry.get("dependsOn") or []:
            dep_ref = _resolve(str(dep or ""), ref_redirect)
            if dep_ref and dep_ref != ref and dep_ref in valid_refs \
                    and dep_ref not in node["dependsOn"]:
                node["dependsOn"].append(dep_ref)

    merged_dependencies = list(by_ref.values())

    print(f"  [dedup] dependency entries: {n_deps_before} in -> {len(merged_dependencies)} out (merged/remapped)")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    merged: dict[str, Any] = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": now,
            "tools": [{"vendor": "dedup_sboms", "name": "dedup_sboms.py"}],
            "component": {
                "type": "application",
                "name": product_name,
            },
        },
        "components": merged_components,
        "dependencies": merged_dependencies,
    }
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge multiple CycloneDX SBOMs into one, deduping components "
                     "without losing the dependency chain.",
    )
    parser.add_argument("sboms", nargs="+", type=Path, help="input CycloneDX SBOM json files")
    parser.add_argument("-o", "--output", type=Path, required=True, help="output merged SBOM path")
    parser.add_argument("--name", default="merged", help="metadata.component.name for the output SBOM")
    args = parser.parse_args()

    merged = merge_sboms(args.sboms, args.name)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"[dedup] wrote {len(merged['components'])} component(s), "
          f"{len(merged['dependencies'])} dependency node(s) -> {args.output}")


if __name__ == "__main__":
    main()
