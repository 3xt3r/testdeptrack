23:16:43 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/2bf50ae9b75c4ceebc442c3dafcbea68/appsec/external_downloads
23:16:43 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/2bf50ae9b75c4ceebc442c3dafcbea68/debug/sources
23:16:43 [INFO] ============================================================
23:16:43 [INFO] STAGE START: cleanup_root
23:16:43 [INFO] ============================================================
23:16:43 [INFO] cleanup_root: disabled (delete_non_main_code skipped) — filtering moves to SBOM-level post-processing; see docstring
23:16:43 [INFO] STAGE DONE:  cleanup_root
23:16:43 [INFO] ============================================================
23:16:43 [INFO] STAGE START: ecosystem (lock-files scan + apply)
23:16:43 [INFO] ============================================================
23:16:53 [INFO] ecosystem report: /home/kali/Desktop/jobs/opensearch/jobs/2bf50ae9b75c4ceebc442c3dafcbea68/appsec/ecosystems/lock_summary.json
23:16:53 [INFO] lock suggestions: 231
Traceback (most recent call last):
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1385, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1383, in main
    return _main_normal(args)
           ^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1332, in _main_normal
    return pipeline_flow(
           ^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 1059, in pipeline_flow
    stages.append(run_ecosystem_pipeline(
                  ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/oss_checks/scanner.py", line 736, in run_ecosystem_pipeline
    lock_result = run_lock_generation(
                  ^^^^^^^^^^^^^^^^^^^^
TypeError: run_lock_generation() got an unexpected keyword argument 'root'
2026-07-03 23:16:53 | ERROR   |     [FAIL] scanner.py: exited with code 1
2026-07-03 23:16:53 | INFO    |   moving results: /home/kali/Desktop/jobs/opensearch/jobs/2bf50ae9b75c4ceebc442c3dafcbea68 -> /home/kali/Desktop/results/2026-07-03/opensearch__3.6.0
2026-07-03 23:16:53 | ERROR   |   [FAIL] opensearch / 3.6.0: exited with code 1
2026-07-03 23:16:53 | INFO    | run log written: /home/kali/Desktop/results/2026-07-03/run.log
2026-07-03 23:16:53 | ERROR   | 1/1 scan(s) failed
