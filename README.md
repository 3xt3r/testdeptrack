(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ trivy image --download-db-only --cache-dir /var/cache/trivy
2026-07-03T14:43:03+03:00	INFO	[vulndb] Need to update DB
2026-07-03T14:43:03+03:00	INFO	[vulndb] Downloading vulnerability DB...
2026-07-03T14:43:03+03:00	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
98.90 MiB / 98.90 MiB [-------------------------------------------------------------------------------------------------------------------------------------] 100.00% 12.16 MiB p/s 8.3s
2026-07-03T14:43:13+03:00	FATAL	Fatal error	run error: init error: DB error: failed to download vulnerability DB: OCI artifact error: failed to download vulnerability DB: failed to download artifact from mirror.gcr.io/aquasec/trivy-db:2: oci download error: download error: failed to download /tmp/trivy-55399/oci-download-2088400477/db.tar.gz: mkdir /var/cache/trivy: permission denied
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ trivy fs --download-db-only --cache-dir /var/cache/trivy
2026-07-03T14:43:30+03:00	INFO	[vulndb] Need to update DB
2026-07-03T14:43:30+03:00	INFO	[vulndb] Downloading vulnerability DB...
2026-07-03T14:43:30+03:00	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
98.90 MiB / 98.90 MiB [-------------------------------------------------------------------------------------------------------------------------------------] 100.00% 12.57 MiB p/s 8.1s
2026-07-03T14:43:39+03:00	FATAL	Fatal error	run error: init error: DB error: failed to download vulnerability DB: OCI artifact error: failed to download vulnerability DB: failed to download artifact from mirror.gcr.io/aquasec/trivy-db:2: oci download error: download error: failed to download /tmp/trivy-55534/oci-download-475285735/db.tar.gz: mkdir /var/cache/trivy: permission denied
(venv) kali@kali-RedmiBook-16:~/Desktop/oss_checks$ 
