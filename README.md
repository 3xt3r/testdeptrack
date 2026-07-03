15:45:01 [INFO] STAGE DONE:  cleanup_root
15:45:01 [INFO] ============================================================
15:45:01 [INFO] STAGE START: ecosystem (lock-files scan + apply)
15:45:01 [INFO] ============================================================
15:45:01 [INFO] ecosystem report: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/appsec/ecosystems/lock_summary.json
15:45:01 [INFO] lock suggestions: 1
15:45:01 [INFO] [lock] [1/1] start: go.mod
15:45:01 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
15:45:01 [INFO] [lock] PID=74176 PGID=74107: cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
15:45:01 [INFO] [lock] [1/1] ok (rc=0, 0.1s): go.mod
15:45:01 [INFO] lock generation: ok=1, failed=0, skipped=0
15:45:01 [INFO] STAGE DONE:  ecosystem
15:45:01 [INFO] ============================================================
15:45:01 [INFO] STAGE START: cplus_scan
15:45:01 [INFO] ============================================================
15:45:01 [INFO] cplus_scan skipped (--skip-cplus-scan)
15:45:01 [INFO] STAGE DONE:  cplus_scan
15:45:01 [INFO] ============================================================
15:45:01 [INFO] STAGE START: trivy
15:45:01 [INFO] ============================================================
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
15:45:01 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/gin/_repos/gin)
[INFO] restored template pom.xml files: 0
15:45:02 [WARNING] [cplus] no cplus sbom files to merge — skipping
15:45:02 [INFO] STAGE DONE:  trivy
15:45:02 [INFO] ============================================================
15:45:02 [INFO] STAGE START: vuln_management
15:45:02 [INFO] ============================================================
15:45:02 [INFO] [normalize] processing: origsbom.json
15:45:02 [INFO] [normalize] origsbom.json: components 32→32, vulnerabilities 0→0, filtered=0
15:45:02 [INFO] [normalize] saved: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/debug/sources/origsbom/origsbom_normalized.json
15:45:02 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/debug/sources/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/debug/sources/origsbom/origsbom_normalized.json (token=019f2802-d723-7a98-a7ec-0733a52c45c4)
[dt] origsbom uploaded to orig project: 46a2afc2-4430-4649-8415-2a9e9bf173bf
[dt] ===== enrich origsbom =====
[trivy] scanning: origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/debug/sources/origsbom/origsbom_normalized.json (token=019f2802-d744-799a-b306-37af0e737866)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=64, stable=0
[dt] findings poll 2: count=64, stable=0
[dt] findings poll 3: count=64, stable=1
[dt] findings poll 4: count=64, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.dt-tmp-enrich.json
[dt] enriched: components=32, vulnerabilities=64 (OSV filtered: 0)
[dual] WARNING: trivy enrichment of origsbom failed: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/debug/sources/origsbom/origsbom_normalized.json
stdout: 
stderr: 2026-07-03T15:45:02+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T15:45:02+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dt] starting DT cleanup: orig_vulns=64  candidate_components=19
15:46:06 [INFO] [dt] created project 'safe-staging-sbom-93a4ec1a' -> 69249c1c-94ba-4bda-9bb4-57e6d3fd5612
[dt] created staging project for this run: safe-staging-sbom-93a4ec1a -> 69249c1c-94ba-4bda-9bb4-57e6d3fd5612
[dual] ===== round: round1 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json (token=019f2803-cf40-7752-8ba3-a4aadfca4819)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.dt-tmp-round1.json
[dual/dt] round=round1 components=19 vulnerabilities=290 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=round1: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T15:46:06+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T15:46:06+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=290  affects=290  matched_by_ref=290  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=17  bad_name_ver=17
[merge] source=dt: 19 -> 2 component(s) (removed 17)
[dual] round1: vulns_dt=290  vulns_trivy=0  components_remaining=2  removed=17
[dual] ===== round: round2 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json (token=019f2804-bcdc-7389-a28e-66f9c60fbfcd)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.dt-tmp-round2.json
[dual/dt] round=round2 components=2 vulnerabilities=0 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=round2: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T15:47:07+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T15:47:07+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=dt: 2 -> 2 component(s) (removed 0)
[dual] round2: vulns_dt=0  vulns_trivy=0  components_remaining=2  removed=0
[dual] clean after round2: 2 safe component(s), 0 vulnerabilities (DT + Trivy)
15:47:22 [INFO] [safe_versions] fallback: golang/golang.org/x/crypto @ 0.48.0 — 20 older candidate(s) collected
15:47:22 [INFO] [safe_versions] fallback: golang/golang.org/x/net @ 0.51.0 — 20 older candidate(s) collected
15:47:23 [INFO] [safe_versions] fallback: golang/golang.org/x/sys @ 0.41.0 — 20 older candidate(s) collected
15:47:23 [INFO] [fallback] probing 60 older-version candidates for 3 package(s) via DT
[dual] ===== round: fallback =====
[trivy] scanning: .fallback-probe.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.fallback-probe.json (token=019f2804-fca8-7d62-8f10-90a99c752ae8)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.dt-tmp-fallback.json
[dual/dt] round=fallback components=60 vulnerabilities=1418 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=fallback: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.fallback-probe.json
stdout: 
stderr: 2026-07-03T15:47:23+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T15:47:23+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=1418  affects=1418  matched_by_ref=1418  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=60  bad_name_ver=60
[merge] source=dt: 60 -> 0 component(s) (removed 60)
15:48:25 [WARNING] [fallback] golang/golang.org/x/crypto @ 0.48.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
15:48:25 [WARNING] [fallback] golang/golang.org/x/net @ 0.51.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
15:48:25 [WARNING] [fallback] golang/golang.org/x/sys @ 0.41.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
[dt] fallback: no additional components found
[dt] SUMMARY: orig_vulns=64  candidates_sent=19  final_safe_components=2  missed_packages=3
[generic] C/C++ components found in enriched SBOM: 0
[dual] ===== round: final =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json (token=019f2805-efb0-7cfb-9b27-86bd8afafbb6)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/.dt-tmp-final.json
[dual/dt] round=final components=2 vulnerabilities=0 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=final: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T15:48:25+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T15:48:25+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=dt: 2 -> 2 component(s) (removed 0)
[dual] final staging verification: vulns_dt=0  vulns_trivy=0  components_after_cleanup=2
[dt] uploading final verified SBOM to safe project: 0bfa801c-9d23-447d-b547-2a86e92a0850
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json (token=019f2806-2ae8-7a39-9499-158caf996d1d)
[dt] no token received, skipping BOM processing wait
[dt] findings poll 1: count=64, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=0
[dt] findings poll 4: count=0, stable=1
[dt] findings poll 5: count=0, stable=2
[dt] findings stabilized
[dt] final verified SBOM uploaded to safe project: 0bfa801c-9d23-447d-b547-2a86e92a0850
15:49:40 [INFO] [dt] deleted staging project 69249c1c-94ba-4bda-9bb4-57e6d3fd5612
[OK] report.xlsx           : /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/reports/report.xlsx
[OK]   Vulnerabilities rows: 64
[OK]   SafeVersions rows   : 2
[OK] sbom-clean.json : /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/debug/failed_safe_versions_debug.txt
15:49:40 [WARNING] [vuln] cplus_sbom NOT found at /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/cplus_sbom.json — C/C++ scan may have been skipped or failed
15:49:40 [INFO] STAGE DONE:  vuln_management
15:49:40 [INFO] pipeline summary:
15:49:40 [INFO] stage ecosystem: done
15:49:40 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/appsec/ecosystems/lock_summary.json
15:49:40 [INFO] stage cplus_scan: skipped
15:49:40 [WARNING] stage cplus_scan: --skip-cplus-scan set: C/C++ vendored-library scan skipped
15:49:40 [INFO] stage trivy_sbom: done
15:49:40 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/origsbom.json
15:49:40 [INFO] stage vuln_management: done
15:49:40 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/reports/report.xlsx
15:49:40 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b/sbom/sbom-clean.json
15:49:40 [INFO] pipeline finished successfully
15:49:40 [INFO] artifacts directory: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b
2026-07-03 15:49:41 | INFO    |   moving results: /home/kali/Desktop/jobs/gin/jobs/d4ca3118abba4dbca8ff47267ac2ee4b -> /home/kali/Desktop/results/2026-07-03/gin__v1.12.0
2026-07-03 15:49:41 | INFO    |   [OK] gin / v1.12.0 -> /home/kali/Desktop/results/2026-07-03/gin__v1.12.0
2026-07-03 15:49:41 | INFO    | run log written: /home/kali/Desktop/results/2026-07-03/run.log
2026-07-03 15:49:41 | INFO    | all 1 scan(s) completed successfully
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ cd ..
(venv) kali@kali-RedmiBook-16:~/Desktop$ mkdir gin
(venv) kali@kali-RedmiBook-16:~/Desktop$ cdgin
cdgin: command not found
(venv) kali@kali-RedmiBook-16:~/Desktop$ cd gin
(venv) kali@kali-RedmiBook-16:~/Desktop/gin$ trivy fs .
2026-07-03T15:52:24+03:00	INFO	[vuln] Vulnerability scanning is enabled
2026-07-03T15:52:24+03:00	INFO	[secret] Secret scanning is enabled
2026-07-03T15:52:24+03:00	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2026-07-03T15:52:24+03:00	INFO	[secret] Please see https://trivy.dev/docs/v0.69/guide/scanner/secret#recommendation for faster secret detection
2026-07-03T15:52:25+03:00	INFO	Number of language-specific files	num=1
2026-07-03T15:52:25+03:00	INFO	[gomod] Detecting vulnerabilities...
2026-07-03T15:52:25+03:00	WARN	Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.69/guide/scanner/vulnerability#severity-selection for details.

Report Summary

┌────────┬───────┬─────────────────┬─────────┐
│ Target │ Type  │ Vulnerabilities │ Secrets │
├────────┼───────┼─────────────────┼─────────┤
│ go.mod │ gomod │       22        │    -    │
└────────┴───────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


go.mod (gomod)

Total: 22 (UNKNOWN: 1, LOW: 0, MEDIUM: 7, HIGH: 14, CRITICAL: 0)

┌────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│          Library           │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ github.com/quic-go/quic-go │ CVE-2026-40898 │ MEDIUM   │ fixed  │ v0.59.0           │ 0.59.1        │ quic-go is an implementation of the QUIC protocol in Go.     │
│                            │                │          │        │                   │               │ Prior to...                                                  │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-40898                   │
├────────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto        │ CVE-2026-39827 │ HIGH     │        │ v0.48.0           │ 0.52.0        │ An authenticated SSH client that repeatedly opened channels  │
│                            │                │          │        │                   │               │ which were ...                                               │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39827                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39828 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:            │
│                            │                │          │        │                   │               │ Unauthorized command execution via discarded SSH permissions │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39828                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39829 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                            │                │          │        │                   │               │ Service via crafted public key with excessive parameters...  │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39829                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39830 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                            │                │          │        │                   │               │ Service via resource leak from unsolicited SSH responses...  │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39830                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39832 │          │        │                   │               │ golang.org/x/crypto/ssh/agent:                               │
│                            │                │          │        │                   │               │ golang.org/x/crypto/ssh/agent: Security bypass due to        │
│                            │                │          │        │                   │               │ improper handling of key restrictions                        │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39832                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39835 │          │        │                   │               │ golang.org/x/crypto/ssh: golang: golang.org/x/crypto/ssh:    │
│                            │                │          │        │                   │               │ Denial of Service via crafted SSH certificate                │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39835                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-42508 │          │        │                   │               │ golang.org/x/crypto/ssh/knownhosts: golang:                  │
│                            │                │          │        │                   │               │ golang.org/x/crypto/ssh/knownhosts: Revocation bypass via    │
│                            │                │          │        │                   │               │ unchecked SignatureKey                                       │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-42508                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-46595 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:            │
│                            │                │          │        │                   │               │ Authorization bypass due to skipped source-address           │
│                            │                │          │        │                   │               │ validation                                                   │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46595                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-46597 │          │        │                   │               │ An incorrectly placed cast from bytes to int allowed for     │
│                            │                │          │        │                   │               │ server-side p...                                             │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46597                   │
│                            ├────────────────┼──────────┤        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39831 │ MEDIUM   │        │                   │               │ The Verify() method for FIDO/U2F security key types          │
│                            │                │          │        │                   │               │ (sk-ecdsa-sha2-nis ...                                       │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39831                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39833 │          │        │                   │               │ golang.org/x/crypto/ssh/agent:                               │
│                            │                │          │        │                   │               │ golang.org/x/crypto/ssh/agent: Security bypass due to        │
│                            │                │          │        │                   │               │ unenforced key confirmation                                  │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39833                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39834 │          │        │                   │               │ When writing data larger than 4GB in a single Write call     │
│                            │                │          │        │                   │               │ on...                                                        │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39834                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-46598 │          │        │                   │               │ golang.org/x/crypto/ssh/agent: golang:                       │
│                            │                │          │        │                   │               │ golang.org/x/crypto/ssh/agent: Denial of Service via         │
│                            │                │          │        │                   │               │ malformed input                                              │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46598                   │
├────────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net           │ CVE-2026-25681 │ HIGH     │        │ v0.51.0           │ 0.55.0        │ golang.org/x/net/html: golang.org/x/net/html: Arbitrary code │
│                            │                │          │        │                   │               │ execution via Cross-Site Scripting                           │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-25681                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-27136 │          │        │                   │               │ golang.org/x/net/html: golang: golang.org/x/net/html:        │
│                            │                │          │        │                   │               │ Cross-Site Scripting via HTML parsing bypass                 │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-27136                   │
│                            ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-33814 │          │        │                   │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                            │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                            │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                            ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                            │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-42502 │          │        │                   │               │ Parsing arbitrary HTML which is then rendered using Render   │
│                            │                │          │        │                   │               │ can result ...                                               │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-42502                   │
│                            ├────────────────┼──────────┤        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-25680 │ MEDIUM   │        │                   │               │ golang.org/x/net/html: golang.org/x/net/html: Denial of      │
│                            │                │          │        │                   │               │ Service due to excessive HTML parsing                        │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-25680                   │
│                            ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                            │ CVE-2026-42506 │          │        │                   │               │ golang.org/x/net/html: golang.org/x/net/html: Cross-Site     │
│                            │                │          │        │                   │               │ Scripting (XSS) via arbitrary HTML parsing                   │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-42506                   │
├────────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/sys           │ CVE-2026-39824 │ UNKNOWN  │        │ v0.41.0           │ 0.44.0        │ Invoking integer overflow in NewNTUnicodeString in           │
│                            │                │          │        │                   │               │ golang.org/x/sys/windows                                     │
│                            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39824                   │
└────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

📣 Notices:
  - Version 0.72.0 of Trivy is now available, current version is 0.69.3

To suppress version checks, run Trivy scans with the --skip-version-check flag
Stage	Package	VulnerabilityID	Severity	FoundByDT	FoundByTrivy
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-3vm4-22fp-5rfm	HIGH	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-8c26-wmh5-6g9v	HIGH	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-cjjc-xp8v-855w	HIGH	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-ffhg-7mh4-33c4	HIGH	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-gwc9-m7rh-j2ww	HIGH	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-xhjq-w7xm-p8qj	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-2wp2-chmh-r934	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-39qc-96h7-956f	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-4r78-hx75-jjj2	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-5p4h-3377-7w67	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-69cg-p879-7622	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-83g2-8m93-v3w7	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-fcf9-6fv2-fc5v	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-hgr8-6h9x-f7q9	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-mv93-wvcp-7m7r	HIGH	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-vfw5-hrgq-h5wf	HIGH	yes	no
origsbom (primary scan)	github.com/quic-go/quic-go@v0.59.0	GHSA-vvgj-x9jq-8cj9	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-45x7-px36-x8w8	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-r5c5-pr8j-pfp7	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GHSA-x3jr-pf6g-c48f	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-5cv4-jp36-h3mw	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GHSA-h86h-8ppg-mxmh	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/sys@v0.41.0	GHSA-p782-xgp4-8hr8	MEDIUM	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2020-0012	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2020-0013	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2021-0227	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2021-0356	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2022-0209	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2022-0229	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2022-0968	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2023-1992	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2024-2961	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5005	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5006	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5013	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5014	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5015	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5016	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5017	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5018	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5019	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5020	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5021	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5023	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/crypto@v0.48.0	GO-2026-5033	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2020-0014	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2021-0078	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2021-0238	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0192	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0193	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0197	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0236	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0288	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0536	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2022-0969	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-4918	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5025	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5026	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5027	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5028	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5029	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/net@v0.51.0	GO-2026-5030	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/sys@v0.41.0	GO-2022-0493	UNKNOWN	yes	no
origsbom (primary scan)	golang.org/x/sys@v0.41.0	GO-2026-5024	UNKNOWN	yes	no
<img width="866" height="1300" alt="image" src="https://github.com/user-attachments/assets/1239c83a-7c33-43e7-93bd-c7d3b2f5e79f" />
