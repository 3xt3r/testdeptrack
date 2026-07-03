[cleanup] done in 0.0s — removed 2 dirs, 42 files
16:33:21 [INFO] STAGE DONE:  cleanup_root
16:33:21 [INFO] ============================================================
16:33:21 [INFO] STAGE START: ecosystem (lock-files scan + apply)
16:33:21 [INFO] ============================================================
16:33:21 [INFO] ecosystem report: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/appsec/ecosystems/lock_summary.json
16:33:21 [INFO] lock suggestions: 1
16:33:21 [INFO] [lock] [1/1] start: go.mod
16:33:21 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
16:33:21 [INFO] [lock] PID=89929 PGID=89840: cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
16:33:22 [INFO] [lock] [1/1] ok (rc=0, 0.1s): go.mod
16:33:22 [INFO] lock generation: ok=1, failed=0, skipped=0
16:33:22 [INFO] STAGE DONE:  ecosystem
16:33:22 [INFO] ============================================================
16:33:22 [INFO] STAGE START: cplus_scan
16:33:22 [INFO] ============================================================
16:33:22 [INFO] cplus_scan skipped (--skip-cplus-scan)
16:33:22 [INFO] STAGE DONE:  cplus_scan
16:33:22 [INFO] ============================================================
16:33:22 [INFO] STAGE START: trivy
16:33:22 [INFO] ============================================================
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
16:33:22 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/gin/_repos/gin)
[INFO] restored template pom.xml files: 0
16:33:22 [WARNING] [cplus] no cplus sbom files to merge — skipping
16:33:22 [INFO] STAGE DONE:  trivy
16:33:22 [INFO] ============================================================
16:33:22 [INFO] STAGE START: vuln_management
16:33:22 [INFO] ============================================================
16:33:22 [INFO] [normalize] processing: origsbom.json
16:33:22 [INFO] [normalize] origsbom.json: components 32→32, vulnerabilities 0→0, filtered=0
16:33:22 [INFO] [normalize] saved: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/debug/sources/origsbom/origsbom_normalized.json
16:33:22 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/debug/sources/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/debug/sources/origsbom/origsbom_normalized.json (token=019f282f-1858-7017-9f69-2fd497fa5a87)
[dt] origsbom uploaded to orig project: 46a2afc2-4430-4649-8415-2a9e9bf173bf
[dt] ===== enrich origsbom =====
[trivy] scanning: origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/debug/sources/origsbom/origsbom_normalized.json (token=019f282f-1881-72af-81a7-a96256f2cd7e)
[dt] bom/token poll 1: processing=True
[trivy] done: origsbom_normalized.json components=32 vulnerabilities=22
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=64, stable=0
[dt] findings poll 2: count=64, stable=0
[dt] findings poll 3: count=64, stable=1
[dt] findings poll 4: count=64, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.dt-tmp-enrich.json
[dt] enriched: components=32, vulnerabilities=64 (OSV filtered: 0)
[dual] +22 vulnerability record(s) added from trivy (not seen by DT yet)
[dt] starting DT cleanup: orig_vulns=86  candidate_components=19
16:34:25 [INFO] [dt] created project 'safe-staging-sbom-1a823a92' -> a08652c1-1879-467e-a832-869cc23e4548
[dt] created staging project for this run: safe-staging-sbom-1a823a92 -> a08652c1-1879-467e-a832-869cc23e4548
[dual] ===== round: round1 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json (token=019f2830-0b71-7f01-938f-7aadd0ed0363)
[dt] bom/token poll 1: processing=True
[trivy] done: sbom-clean.json components=19 vulnerabilities=27
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.dt-tmp-round1.json
[dual/dt] round=round1 components=19 vulnerabilities=290 (OSV filtered: 0)
[dt] remove_vulnerable: vulns=27  affects=72  matched_by_ref=72  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=10  bad_name_ver=10
[merge] source=trivy: 19 -> 9 component(s) (removed 10)
[dt] remove_vulnerable: vulns=290  affects=290  matched_by_ref=290  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=17  bad_name_ver=17
[merge] source=dt: 9 -> 2 component(s) (removed 7)
[dual] round1: vulns_dt=290  vulns_trivy=27  components_remaining=2  removed=17
[dual] ===== round: round2 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json (token=019f2830-f905-7e1c-a2a0-9e40d6c5a0fa)
[dt] bom/token poll 1: processing=True
[trivy] done: sbom-clean.json components=2 vulnerabilities=0
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.dt-tmp-round2.json
[dual/dt] round=round2 components=2 vulnerabilities=0 (OSV filtered: 0)
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=trivy: 2 -> 2 component(s) (removed 0)
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=dt: 2 -> 2 component(s) (removed 0)
[dual] round2: vulns_dt=0  vulns_trivy=0  components_remaining=2  removed=0
[dual] clean after round2: 2 safe component(s), 0 vulnerabilities (DT + Trivy)
16:35:41 [INFO] [safe_versions] fallback: golang/golang.org/x/crypto @ 0.48.0 — 20 older candidate(s) collected
16:35:41 [INFO] [safe_versions] fallback: golang/golang.org/x/net @ 0.51.0 — 20 older candidate(s) collected
16:35:42 [INFO] [safe_versions] fallback: golang/golang.org/x/sys @ 0.41.0 — 20 older candidate(s) collected
16:35:42 [INFO] [fallback] probing 60 older-version candidates for 3 package(s) via DT
[dual] ===== round: fallback =====
[trivy] scanning: .fallback-probe.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.fallback-probe.json (token=019f2831-38bf-7110-88db-1229194633b2)
[dt] bom/token poll 1: processing=True
[trivy] done: .fallback-probe.json components=60 vulnerabilities=32
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.dt-tmp-fallback.json
[dual/dt] round=fallback components=60 vulnerabilities=1418 (OSV filtered: 0)
[dt] remove_vulnerable: vulns=32  affects=522  matched_by_ref=522  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=60  bad_name_ver=60
[merge] source=trivy: 60 -> 0 component(s) (removed 60)
[dt] remove_vulnerable: vulns=1418  affects=1418  matched_by_ref=1418  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=60  bad_name_ver=60
[merge] source=dt: 0 -> 0 component(s) (removed 0)
16:36:44 [WARNING] [fallback] golang/golang.org/x/crypto @ 0.48.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
16:36:44 [WARNING] [fallback] golang/golang.org/x/net @ 0.51.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
16:36:44 [WARNING] [fallback] golang/golang.org/x/sys @ 0.41.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
[dt] fallback: no additional components found
[dt] SUMMARY: orig_vulns=86  candidates_sent=19  final_safe_components=2  missed_packages=3
[generic] C/C++ components found in enriched SBOM: 0
[dual] ===== round: final =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json (token=019f2832-2b3b-7815-be89-af0bf62a7812)
[dt] bom/token poll 1: processing=True
[trivy] done: sbom-clean.json components=2 vulnerabilities=0
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/.dt-tmp-final.json
[dual/dt] round=final components=2 vulnerabilities=0 (OSV filtered: 0)
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=trivy: 2 -> 2 component(s) (removed 0)
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=dt: 2 -> 2 component(s) (removed 0)
[dual] final staging verification: vulns_dt=0  vulns_trivy=0  components_after_cleanup=2
[dt] uploading final verified SBOM to safe project: 0bfa801c-9d23-447d-b547-2a86e92a0850
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json (token=019f2832-6661-704d-8a3a-1a03b32d85bf)
[dt] no token received, skipping BOM processing wait
[dt] findings poll 1: count=64, stable=0
[dt] findings poll 2: count=0, stable=0
[dt] findings poll 3: count=0, stable=0
[dt] findings poll 4: count=0, stable=1
[dt] findings poll 5: count=0, stable=2
[dt] findings stabilized
[dt] final verified SBOM uploaded to safe project: 0bfa801c-9d23-447d-b547-2a86e92a0850
16:37:59 [INFO] [dt] deleted staging project a08652c1-1879-467e-a832-869cc23e4548
[OK] report.xlsx           : /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/reports/report.xlsx
[OK]   Vulnerabilities rows: 86
[OK]   SafeVersions rows   : 2
[OK] dt_vs_trivy_safe_scan.xlsx : /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/debug/dt_vs_trivy_safe_scan.xlsx
[OK]   comparison rows          : 2302
[OK] sbom-clean.json : /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/debug/failed_safe_versions_debug.txt
16:37:59 [WARNING] [vuln] cplus_sbom NOT found at /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/cplus_sbom.json — C/C++ scan may have been skipped or failed
16:37:59 [INFO] STAGE DONE:  vuln_management
16:37:59 [INFO] pipeline summary:
16:37:59 [INFO] stage ecosystem: done
16:37:59 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/appsec/ecosystems/lock_summary.json
16:37:59 [INFO] stage cplus_scan: skipped
16:37:59 [WARNING] stage cplus_scan: --skip-cplus-scan set: C/C++ vendored-library scan skipped
16:37:59 [INFO] stage trivy_sbom: done
16:37:59 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/origsbom.json
16:37:59 [INFO] stage vuln_management: done
16:37:59 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/reports/report.xlsx
16:37:59 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d/sbom/sbom-clean.json
16:37:59 [INFO] pipeline finished successfully
16:37:59 [INFO] artifacts directory: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d
2026-07-03 16:38:00 | INFO    |   moving results: /home/kali/Desktop/jobs/gin/jobs/662730b2a0c441109a0be2bef3dfcb8d -> /home/kali/Desktop/results/2026-07-03/gin__v1.12.0
2026-07-03 16:38:00 | INFO    |   [OK] gin / v1.12.0 -> /home/kali/Desktop/results/2026-07-03/gin__v1.12.0
2026-07-03 16:38:00 | INFO    | run log written: /home/kali/Desktop/results/2026-07-03/run.log
2026-07-03 16:38:00 | INFO    | all 1 scan(s) completed successfully
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 
