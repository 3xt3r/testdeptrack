:33:39 [INFO] STAGE DONE:  cleanup_root
14:33:39 [INFO] ============================================================
14:33:39 [INFO] STAGE START: ecosystem (lock-files scan + apply)
14:33:39 [INFO] ============================================================
14:33:39 [INFO] ecosystem report: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/appsec/ecosystems/lock_summary.json
14:33:39 [INFO] lock suggestions: 1
14:33:39 [INFO] [lock] [1/1] start: go.mod
14:33:39 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
14:33:39 [INFO] [lock] PID=50962 PGID=50890: cd "/home/kali/Desktop/jobs/gin/_repos/gin" && go mod tidy
14:33:39 [INFO] [lock] [1/1] ok (rc=0, 0.1s): go.mod
14:33:39 [INFO] lock generation: ok=1, failed=0, skipped=0
14:33:39 [INFO] STAGE DONE:  ecosystem
14:33:39 [INFO] ============================================================
14:33:39 [INFO] STAGE START: cplus_scan
14:33:39 [INFO] ============================================================
14:33:39 [INFO] cplus_scan skipped (--skip-cplus-scan)
14:33:39 [INFO] STAGE DONE:  cplus_scan
14:33:39 [INFO] ============================================================
14:33:39 [INFO] STAGE START: trivy
14:33:39 [INFO] ============================================================
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
14:33:39 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/gin/_repos/gin)
[INFO] restored template pom.xml files: 0
14:33:40 [WARNING] [cplus] no cplus sbom files to merge — skipping
14:33:40 [INFO] STAGE DONE:  trivy
14:33:40 [INFO] ============================================================
14:33:40 [INFO] STAGE START: vuln_management
14:33:40 [INFO] ============================================================
14:33:40 [INFO] [normalize] processing: origsbom.json
14:33:40 [INFO] [normalize] origsbom.json: components 32→32, vulnerabilities 0→0, filtered=0
14:33:40 [INFO] [normalize] saved: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/debug/sources/origsbom/origsbom_normalized.json
14:33:40 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/debug/sources/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/debug/sources/origsbom/origsbom_normalized.json (token=019f27c1-8064-77dc-b79f-6a462306d82d)
[dt] origsbom uploaded to orig project: 46a2afc2-4430-4649-8415-2a9e9bf173bf
[dt] ===== enrich origsbom =====
[trivy] scanning: origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/debug/sources/origsbom/origsbom_normalized.json (token=019f27c1-8082-7e98-85bc-dfd053399af6)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=64, stable=0
[dt] findings poll 2: count=64, stable=0
[dt] findings poll 3: count=64, stable=1
[dt] findings poll 4: count=64, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.dt-tmp-enrich.json
[dt] enriched: components=32, vulnerabilities=64 (OSV filtered: 0)
[dual] WARNING: trivy enrichment of origsbom failed: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/debug/sources/origsbom/origsbom_normalized.json
stdout: 
stderr: 2026-07-03T14:33:40+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T14:33:40+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dt] starting DT cleanup: orig_vulns=64  candidate_components=19
14:34:47 [INFO] [dt] created project 'safe-staging-sbom-754d80e3' -> 66334f19-7ff2-4032-bdf4-017bf8b48a38
[dt] created staging project for this run: safe-staging-sbom-754d80e3 -> 66334f19-7ff2-4032-bdf4-017bf8b48a38
[dual] ===== round: round1 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json (token=019f27c2-87c4-74b5-99a3-2333cc9fd5f9)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.dt-tmp-round1.json
[dual/dt] round=round1 components=19 vulnerabilities=290 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=round1: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T14:34:48+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T14:34:48+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=290  affects=290  matched_by_ref=290  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=17  bad_name_ver=17
[merge] source=dt: 19 -> 2 component(s) (removed 17)
[dual] round1: vulns_dt=290  vulns_trivy=0  components_remaining=2  removed=17
[dual] ===== round: round2 =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json (token=019f27c3-7562-740d-b058-2ef1a0ff6bcc)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.dt-tmp-round2.json
[dual/dt] round=round2 components=2 vulnerabilities=0 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=round2: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T14:35:48+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T14:35:48+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=0  affects=0  matched_by_ref=0  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=0  bad_name_ver=0
[merge] source=dt: 2 -> 2 component(s) (removed 0)
[dual] round2: vulns_dt=0  vulns_trivy=0  components_remaining=2  removed=0
[dual] clean after round2: 2 safe component(s), 0 vulnerabilities (DT + Trivy)
14:36:04 [INFO] [safe_versions] fallback: golang/golang.org/x/crypto @ 0.48.0 — 20 older candidate(s) collected
14:36:05 [INFO] [safe_versions] fallback: golang/golang.org/x/net @ 0.51.0 — 20 older candidate(s) collected
14:36:06 [INFO] [safe_versions] fallback: golang/golang.org/x/sys @ 0.41.0 — 20 older candidate(s) collected
14:36:06 [INFO] [fallback] probing 60 older-version candidates for 3 package(s) via DT
[dual] ===== round: fallback =====
[trivy] scanning: .fallback-probe.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.fallback-probe.json (token=019f27c3-b9b5-714d-a135-07deac85742d)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=100, stable=0
[dt] findings poll 2: count=100, stable=0
[dt] findings poll 3: count=100, stable=1
[dt] findings poll 4: count=100, stable=2
[dt] findings stabilized
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.dt-tmp-fallback.json
[dual/dt] round=fallback components=60 vulnerabilities=1418 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=fallback: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.fallback-probe.json
stdout: 
stderr: 2026-07-03T14:36:06+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T14:36:06+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

[dual] continuing with DT-only result for this round
[dt] remove_vulnerable: vulns=1418  affects=1418  matched_by_ref=1418  matched_by_purl=0  matched_as_purl_ref=0  bad_purls=60  bad_name_ver=60
[merge] source=dt: 60 -> 0 component(s) (removed 60)
14:37:08 [WARNING] [fallback] golang/golang.org/x/crypto @ 0.48.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
14:37:08 [WARNING] [fallback] golang/golang.org/x/net @ 0.51.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
14:37:08 [WARNING] [fallback] golang/golang.org/x/sys @ 0.41.0 — NO safe version found in older candidates. All versions appear vulnerable. Manual review required.
[dt] fallback: no additional components found
[dt] SUMMARY: orig_vulns=64  candidates_sent=19  final_safe_components=2  missed_packages=3
[generic] C/C++ components found in enriched SBOM: 0
[dual] ===== round: final =====
[trivy] scanning: sbom-clean.json
[dt] uploaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json (token=019f27c4-ac19-7044-8977-d2f229b91460)
[dt] bom/token poll 1: processing=True
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/.dt-tmp-final.json
[dual/dt] round=final components=2 vulnerabilities=0 (OSV filtered: 0)
[dual] WARNING: trivy scan failed for round=final: trivy sbom exited with code 1 for /home/kali/Desktop/jobs/gin/jobs/bbf15d21a54d4504bcae3e1131fc2bda/sbom/sbom-clean.json
stdout: 
stderr: 2026-07-03T14:37:08+03:00	ERROR	[vulndb] The first run cannot skip downloading DB
2026-07-03T14:37:08+03:00	FATAL	Fatal error	run error: init error: DB error: database error: --skip-db-update cannot be specified on the first run

