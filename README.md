1:45 | INFO    |   running scanner on /home/kali/Desktop/jobs/commons-lang/_repos/commons-lang (DT project: commons-lang__rel/commons-lang-3.17.0, timeout=3600s)
2026-07-03 13:01:45 | INFO    |   job_dir: /home/kali/Desktop/jobs/commons-lang/jobs/c88d384f19094affb30f18ec762d7322
2026-07-03 13:01:45 | INFO    |     running: /home/kali/Desktop/venv/bin/python /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/commons-lang/_repos/commons-lang --apply --deptrack --dt-project-name commons-lang__rel/commons-lang-3.17.0 --env-file /home/kali/Desktop/oss_checks/env --job-dir /home/kali/Desktop/jobs/commons-lang/jobs/c88d384f19094affb30f18ec762d7322
13:01:45 [INFO] loaded .env: /home/kali/Desktop/oss_checks/env
13:01:45 [INFO] [dt] auto-ensuring orig project 'commons-lang__rel/commons-lang-3.17.0-orig'...
13:01:45 [WARNING] [dt] could not search for project 'commons-lang__rel/commons-lang-3.17.0-orig': Expecting value: line 1 column 1 (char 0)
13:01:45 [ERROR] [dt] failed to create project 'commons-lang__rel/commons-lang-3.17.0-orig': HTTP 405 — <html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.31.1</center>
</body>
</html>

Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1356, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1354, in main
    return _main_normal(args)
           ^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1302, in _main_normal
    dt_config = build_dependency_track_config(args, root, dt_base) if dt_base is not None else None
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 253, in build_dependency_track_config
    orig_uuid = dt_ensure_project(dt_base, name=orig_name, version=project_version)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/ecosystem_management/vulnerability/dependency_track/dt_projects.py", line 223, in dt_ensure_project
    return dt_create_project(dt_base, name, version, parent_uuid=parent_uuid)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/ecosystem_management/vulnerability/dependency_track/dt_projects.py", line 180, in dt_create_project
    resp.raise_for_status()
  File "/home/kali/Desktop/venv/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 405 Client Error: Not Allowed for url: http://localhost:8081/api/v1/project
2026-07-03 13:01:45 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-07-03 13:01:45 | INFO    |   moving results: /home/kali/Desktop/jobs/commons-lang/jobs/c88d384f19094affb30f18ec762d7322 -> /home/kali/Desktop/results/2026-07-03/commons-lang__rel/commons-lang-3.17.0
2026-07-03 13:01:45 | ERROR   |   [FAIL] commons-lang / rel/commons-lang-3.17.0: exited with code 1
2026-07-03 13:01:45 | INFO    | === product: gin ===
2026-07-03 13:01:45 | INFO    | --- version: v1.12.0 ---
2026-07-03 13:01:45 | INFO    |     cloning: https://github.com/gin-gonic/gin.git
2026-07-03 13:01:45 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/gin-gonic/gin.git /home/kali/Desktop/jobs/gin/_repos/gin
2026-07-03 13:01:47 | INFO    |     checkout gin @ v1.12.0
2026-07-03 13:01:47 | INFO    |     running: git -c credential.helper= checkout -- .
2026-07-03 13:01:47 | ERROR   |     [FAIL] git checkout -- . (reset local changes): error: pathspec '.' did not match any file(s) known to git
2026-07-03 13:01:47 | INFO    |     running: git -c credential.helper= clean -fd
2026-07-03 13:01:47 | INFO    |     running: git -c credential.helper= checkout v1.12.0
2026-07-03 13:01:47 | INFO    |     v1.12.0 is a tag — skipping reset to origin/
2026-07-03 13:01:47 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-07-03 13:01:47 | INFO    |   running scanner on /home/kali/Desktop/jobs/gin/_repos/gin (DT project: gin__v1.12.0, timeout=3600s)
2026-07-03 13:01:47 | INFO    |   job_dir: /home/kali/Desktop/jobs/gin/jobs/6af2e57f2c614cf8877ec4fff0bbc884
2026-07-03 13:01:47 | INFO    |     running: /home/kali/Desktop/venv/bin/python /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/gin/_repos/gin --apply --deptrack --dt-project-name gin__v1.12.0 --env-file /home/kali/Desktop/oss_checks/env --job-dir /home/kali/Desktop/jobs/gin/jobs/6af2e57f2c614cf8877ec4fff0bbc884
13:01:48 [INFO] loaded .env: /home/kali/Desktop/oss_checks/env
13:01:48 [INFO] [dt] auto-ensuring orig project 'gin__v1.12.0-orig'...
13:01:48 [WARNING] [dt] could not search for project 'gin__v1.12.0-orig': Expecting value: line 1 column 1 (char 0)
13:01:48 [ERROR] [dt] failed to create project 'gin__v1.12.0-orig': HTTP 405 — <html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.31.1</center>
</body>
</html>

Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1356, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1354, in main
    return _main_normal(args)
           ^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1302, in _main_normal
    dt_config = build_dependency_track_config(args, root, dt_base) if dt_base is not None else None
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 253, in build_dependency_track_config
    orig_uuid = dt_ensure_project(dt_base, name=orig_name, version=project_version)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/ecosystem_management/vulnerability/dependency_track/dt_projects.py", line 223, in dt_ensure_project
    return dt_create_project(dt_base, name, version, parent_uuid=parent_uuid)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/ecosystem_management/vulnerability/dependency_track/dt_projects.py", line 180, in dt_create_project
    resp.raise_for_status()
  File "/home/kali/Desktop/venv/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 405 Client Error: Not Allowed for url: http://localhost:8081/api/v1/project
2026-07-03 13:01:48 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-07-03 13:01:48 | INFO    |   moving results: /home/kali/Desktop/jobs/gin/jobs/6af2e57f2c614cf8877ec4fff0bbc884 -> /home/kali/Desktop/results/2026-07-03/gin__v1.12.0
2026-07-03 13:01:48 | ERROR   |   [FAIL] gin / v1.12.0: exited with code 1
2026-07-03 13:01:48 | INFO    | === product: sinatra ===
2026-07-03 13:01:48 | INFO    | --- version: v4.2.1 ---
2026-07-03 13:01:48 | INFO    |     cloning: https://github.com/sinatra/sinatra.git
2026-07-03 13:01:48 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/sinatra/sinatra.git /home/kali/Desktop/jobs/sinatra/_repos/sinatra
2026-07-03 13:01:51 | INFO    |     checkout sinatra @ v4.2.1
2026-07-03 13:01:51 | INFO    |     running: git -c credential.helper= checkout -- .
2026-07-03 13:01:51 | ERROR   |     [FAIL] git checkout -- . (reset local changes): error: pathspec '.' did not match any file(s) known to git
2026-07-03 13:01:51 | INFO    |     running: git -c credential.helper= clean -fd
2026-07-03 13:01:51 | INFO    |     running: git -c credential.helper= checkout v4.2.1
2026-07-03 13:01:51 | INFO    |     v4.2.1 is a tag — skipping reset to origin/
2026-07-03 13:01:51 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-07-03 13:01:51 | INFO    |   running scanner on /home/kali/Desktop/jobs/sinatra/_repos/sinatra (DT project: sinatra__v4.2.1, timeout=3600s)
2026-07-03 13:01:51 | INFO    |   job_dir: /home/kali/Desktop/jobs/sinatra/jobs/280e4966c0914308aec94c971b3e5dfa
2026-07-03 13:01:51 | INFO    |     running: /home/kali/Desktop/venv/bin/python /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/sinatra/_repos/sinatra --apply --deptrack --dt-project-name sinatra__v4.2.1 --env-file /home/kali/Desktop/oss_checks/env --job-dir /home/kali/Desktop/jobs/sinatra/jobs/280e4966c0914308aec94c971b3e5dfa
13:01:51 [INFO] loaded .env: /home/kali/Desktop/oss_checks/env
13:01:51 [INFO] [dt] auto-ensuring orig project 'sinatra__v4.2.1-orig'...
13:01:51 [WARNING] [dt] could not search for project 'sinatra__v4.2.1-orig': Expecting value: line 1 column 1 (char 0)
13:01:51 [ERROR] [dt] failed to create project 'sinatra__v4.2.1-orig': HTTP 405 — <html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.31.1</center>
</body>


DEPENDENCY_TRACK_URL=http://localhost:8081
DEPENDENCY_TRACK_API_KEY=

# Trivy (локальный vulnerability-бэкстоп рядом с Dependency-Track)
TRIVY_ENABLED=true
TRIVY_BINARY=/usr/bin/trivy
# Кэш БД — та же директория, что использует update_trivy_db_daily.py по крону,
# и та же, что видят контейнеры/раннеры, которые реально сканируют (shared volume).
TRIVY_CACHE_DIR=/var/cache/trivy
TRIVY_SKIP_DB_UPDATE=true
TRIVY_OFFLINE_SCAN=true
TRIVY_SCAN_TIMEOUT=10m
# TRIVY_DB_REPOSITORY=ghcr.io/aquasecurity/trivy-db   # переопределить при использовании зеркала/прокси
