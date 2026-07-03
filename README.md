python scheduler.py --config config.yml
2026-07-03 23:35:07 | INFO    | GITLAB_TOKEN not set — will try anonymous clone first
2026-07-03 23:35:07 | INFO    | timeouts: scanner=3600s, distrib_scan=7200s, deptrack=3600s
2026-07-03 23:35:07 | INFO    | === product: opensearch ===
2026-07-03 23:35:07 | INFO    | --- version: 3.6.0 ---
2026-07-03 23:35:07 | INFO    |     cloning: https://github.com/opensearch-project/opensearch
2026-07-03 23:35:07 | INFO    |     running: git -c credential.helper= clone --no-checkout https://github.com/opensearch-project/opensearch /home/kali/Desktop/jobs/opensearch/_repos/opensearch
2026-07-03 23:36:25 | INFO    |     checkout opensearch @ 3.6.0
2026-07-03 23:36:25 | INFO    |     running: git -c credential.helper= checkout -- .
2026-07-03 23:36:25 | ERROR   |     [FAIL] git checkout -- . (reset local changes): error: pathspec '.' did not match any file(s) known to git
2026-07-03 23:36:25 | INFO    |     running: git -c credential.helper= clean -fd
2026-07-03 23:36:25 | INFO    |     running: git -c credential.helper= checkout 3.6.0
2026-07-03 23:36:25 | INFO    |     3.6.0 is a tag — skipping reset to origin/
2026-07-03 23:36:25 | INFO    |     running: git -c credential.helper= submodule update --init --recursive
2026-07-03 23:36:26 | INFO    |   running scanner on /home/kali/Desktop/jobs/opensearch/_repos/opensearch (DT project: opensearch__3.6.0, timeout=3600s)
2026-07-03 23:36:26 | INFO    |   job_dir: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954
2026-07-03 23:36:26 | INFO    |     running: /home/kali/Desktop/venv/bin/python /home/kali/Desktop/oss_checks/scanner.py /home/kali/Desktop/jobs/opensearch/_repos/opensearch --apply --deptrack --dt-project-name opensearch__3.6.0 --env-file /home/kali/Desktop/oss_checks/env --job-dir /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954 --only-cve --skip-cplus-scan
23:36:26 [INFO] loaded .env: /home/kali/Desktop/oss_checks/env
23:36:26 [INFO] [dt] auto-ensuring orig project 'opensearch__3.6.0-orig'...
23:36:26 [INFO] [dt] reusing existing project 'opensearch__3.6.0-orig' -> 90c437ed-7167-4ef8-aca6-e809468372b8
23:36:26 [INFO] [dt] server version: 5.0.0 — parentUUID support: yes
23:36:26 [INFO] [dt] auto-ensuring safe project 'opensearch__3.6.0 [safe]' (parent: 90c437ed-7167-4ef8-aca6-e809468372b8)...
23:36:26 [INFO] [dt] reusing existing project 'opensearch__3.6.0 [safe]' -> 7a914d32-05e2-4335-bbc2-d8ef5eb6dd63
23:36:26 [INFO] scan root: /home/kali/Desktop/jobs/opensearch/_repos/opensearch
23:36:26 [INFO] working copy:              /home/kali/Desktop/jobs/opensearch/_repos/opensearch
23:36:26 [INFO] job directory:             /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954
23:36:26 [INFO] dependency-track: enabled url=http://localhost:8080 safe_project=7a914d32-05e2-4335-bbc2-d8ef5eb6dd63 orig_project=90c437ed-7167-4ef8-aca6-e809468372b8 insecure=True
23:36:26 [INFO] mode: only-cve — skipping ASM, binary, license, downloads, toxic
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/_repos/jobs
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/reports
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec/asm
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec/ecosystems
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec/external_downloads
23:36:26 [INFO] created directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/sources
23:36:26 [INFO] ============================================================
23:36:26 [INFO] STAGE START: cleanup_root
23:36:26 [INFO] ============================================================
23:36:26 [INFO] cleanup_root: disabled (delete_non_main_code skipped) — filtering moves to SBOM-level post-processing; see docstring
23:36:26 [INFO] STAGE DONE:  cleanup_root
23:36:26 [INFO] ============================================================
23:36:26 [INFO] STAGE START: ecosystem (lock-files scan + apply)
23:36:26 [INFO] ============================================================
23:36:32 [INFO] ecosystem report: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec/ecosystems/lock_summary.json
23:36:32 [INFO] lock suggestions: 231
23:36:32 [INFO] [lock] [1/231] start: build.gradle
23:36:32 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/opensearch/_repos/opensearch" && set -e
cat > init-trivy-locks.gradle <<'TRIVY_GRADLE_INIT_EOF'
allprojects {
    dependencyLocking { lockAllConfigurations() }
    tasks.register("resolveTrivyLockDeps") {
        doLast {
            configurations.findAll { conf ->
                conf.canBeResolved &&
                !conf.name.toLowerCase().contains("test") &&
                !conf.name.toLowerCase().contains("integ") &&
                !conf.name.toLowerCase().contains("qa") &&
                !conf.name.toLowerCase().contains("fixture")
            }.each { conf ->
                try {
                    println("Resolving ${project.path}:${conf.name}")
                    conf.resolve()
                } catch (Exception e) {
                    println("SKIP ${project.path}:${conf.name} -> ${e.class.simpleName}: ${e.message}")
                }
            }
        }
    }
}
TRIVY_GRADLE_INIT_EOF
python3 - <<'TRIVY_SETTINGS_PATCH_EOF'

import re
from pathlib import Path

settings_path = Path("settings.gradle")
if settings_path.exists():
    backup_path = settings_path.with_name("settings.gradle.trivylock.bak")
    if not backup_path.exists():
        text = settings_path.read_text(encoding="utf-8")
        pattern = re.compile(r"^([ \t]*)project\('(:[^']+)'\)\.projectDir\s*=.*$")
        lines = text.splitlines()
        out = []
        changed = False
        for i, line in enumerate(lines):
            m = pattern.match(line)
            already_guarded = i > 0 and "findProject" in lines[i - 1]
            if m and not already_guarded:
                indent, name = m.group(1), m.group(2)
                out.append(f"{indent}if (findProject('{name}') != null) {{")
                out.append(f"{indent}    {line.strip()}")
                out.append(f"{indent}}}")
                changed = True
            else:
                out.append(line)
        if changed:
            backup_path.write_text(text, encoding="utf-8")
            settings_path.write_text("\n".join(out) + "\n", encoding="utf-8")
            print(f"[trivy-lock-prep] patched settings.gradle (backup: {backup_path.name})")
TRIVY_SETTINGS_PATCH_EOF
./gradlew resolveTrivyLockDeps --init-script init-trivy-locks.gradle --write-locks --warning-mode none --no-daemon
23:36:32 [INFO] [lock] PID=163899 PGID=163436: cd "/home/kali/Desktop/jobs/opensearch/_repos/opensearch" && set -e
cat > init-trivy-locks.gradle <<'TRIVY_GRADLE_INIT_EOF'
allprojects {
    dependencyLocking { lockAllConfigurations() }
    tasks.register("resolveTrivyLockDeps") {
        doLast {
            configurations.findAll { conf ->
                conf.canBeResolved &&
                !conf.name.toLowerCase().contains("test") &&
                !conf.name.toLowerCase().contains("integ") &&
                !conf.name.toLowerCase().contains("qa") &&
                !conf.name.toLowerCase().contains("fixture")
            }.each { conf ->
                try {
                    println("Resolving ${project.path}:${conf.name}")
                    conf.resolve()
                } catch (Exception e) {
                    println("SKIP ${project.path}:${conf.name} -> ${e.class.simpleName}: ${e.message}")
                }
            }
        }
    }
}
TRIVY_GRADLE_INIT_EOF
python3 - <<'TRIVY_SETTINGS_PATCH_EOF'

import re
from pathlib import Path

settings_path = Path("settings.gradle")
if settings_path.exists():
    backup_path = settings_path.with_name("settings.gradle.trivylock.bak")
    if not backup_path.exists():
        text = settings_path.read_text(encoding="utf-8")
        pattern = re.compile(r"^([ \t]*)project\('(:[^']+)'\)\.projectDir\s*=.*$")
        lines = text.splitlines()
        out = []
        changed = False
        for i, line in enumerate(lines):
            m = pattern.match(line)
            already_guarded = i > 0 and "findProject" in lines[i - 1]
            if m and not already_guarded:
                indent, name = m.group(1), m.group(2)
                out.append(f"{indent}if (findProject('{name}') != null) {{")
                out.append(f"{indent}    {line.strip()}")
                out.append(f"{indent}}}")
                changed = True
            else:
                out.append(line)
        if changed:
            backup_path.write_text(text, encoding="utf-8")
            settings_path.write_text("\n".join(out) + "\n", encoding="utf-8")
            print(f"[trivy-lock-prep] patched settings.gradle (backup: {backup_path.name})")
TRIVY_SETTINGS_PATCH_EOF
./gradlew resolveTrivyLockDeps --init-script init-trivy-locks.gradle --write-locks --warning-mode none --no-daemon
23:36:32 [INFO] [lock][stdout] [trivy-lock-prep] patched settings.gradle (backup: settings.gradle.trivylock.bak)
23:36:33 [INFO] [lock][stdout] To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
23:36:34 [INFO] [lock][stdout] Daemon will be stopped at the end of the build 
23:36:41 [INFO] [lock][stderr] 
23:36:41 [INFO] [lock][stderr] FAILURE: Build failed with an exception.
23:36:41 [INFO] [lock][stderr] 
23:36:41 [INFO] [lock][stderr] * Where:
23:36:41 [INFO] [lock][stderr] Build file '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/buildSrc/build.gradle' line: 78
23:36:41 [INFO] [lock][stderr] 
23:36:41 [INFO] [lock][stderr] * What went wrong:
23:36:41 [INFO] [lock][stderr] A problem occurred evaluating project ':buildSrc'.
23:36:41 [INFO] [lock][stderr] > At least Java 21 is required to build opensearch gradle tools
23:36:41 [INFO] [lock][stderr] 
23:36:41 [INFO] [lock][stderr] * Try:
23:36:41 [INFO] [lock][stderr] > Run with --stacktrace option to get the stack trace.
23:36:41 [INFO] [lock][stderr] > Run with --info or --debug option to get more log output.
23:36:41 [INFO] [lock][stderr] > Run with --scan to get full insights from a Build Scan (powered by Develocity).
23:36:41 [INFO] [lock][stderr] > Get more help at https://help.gradle.org.
23:36:41 [INFO] [lock][stderr] 
23:36:41 [INFO] [lock][stderr] BUILD FAILED in 8s
23:36:41 [INFO] [lock] [1/231] failed (rc=1, 9.0s): build.gradle
23:36:41 [WARNING] [lock]         stderr: FAILURE: Build failed with an exception.

* Where:
Build file '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/buildSrc/build.gradle' line: 78

* What went wrong:
A problem occurred evaluating project ':buildSrc'.
> At least Java 21 is required to build opensearch gradle tools

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 8s
23:36:41 [WARNING] [lock]         stdout: [trivy-lock-prep] patched settings.gradle (backup: settings.gradle.trivylock.bak)
To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
Daemon will be stopped at the end of the build
23:36:41 [INFO] [lock] [2/231] skipped (no command): benchmarks/build.gradle
23:36:41 [INFO] [lock] [3/231] skipped (no command): libs/build.gradle
23:36:41 [INFO] [lock] [4/231] skipped (no command): libs/common/build.gradle
23:36:41 [INFO] [lock] [5/231] skipped (no command): libs/telemetry/build.gradle
23:36:41 [INFO] [lock] [6/231] skipped (no command): libs/core/build.gradle
23:36:41 [INFO] [lock] [7/231] skipped (no command): libs/dissect/build.gradle
23:36:41 [INFO] [lock] [8/231] skipped (no command): libs/netty4/build.gradle
23:36:41 [INFO] [lock] [9/231] skipped (no command): libs/ssl-config/build.gradle
23:36:41 [INFO] [lock] [10/231] skipped (no command): libs/compress/build.gradle
23:36:41 [INFO] [lock] [11/231] skipped (no command): libs/nio/build.gradle
23:36:41 [INFO] [lock] [12/231] skipped (no command): libs/plugin-classloader/build.gradle
23:36:41 [INFO] [lock] [13/231] skipped (no command): libs/grok/build.gradle
23:36:41 [INFO] [lock] [14/231] skipped (no command): libs/secure-sm/build.gradle
23:36:41 [INFO] [lock] [15/231] skipped (no command): libs/cli/build.gradle
23:36:41 [INFO] [lock] [16/231] skipped (no command): libs/agent-sm/build.gradle
23:36:41 [INFO] [lock] [17/231] skipped (no command): libs/agent-sm/agent/build.gradle
23:36:41 [INFO] [lock] [18/231] skipped (no command): libs/agent-sm/bootstrap/build.gradle
23:36:41 [INFO] [lock] [19/231] skipped (no command): libs/agent-sm/agent-policy/build.gradle
23:36:41 [INFO] [lock] [20/231] skipped (no command): libs/task-commons/build.gradle
23:36:41 [INFO] [lock] [21/231] skipped (no command): libs/geo/build.gradle
23:36:41 [INFO] [lock] [22/231] skipped (no command): libs/x-content/build.gradle
23:36:41 [INFO] [lock] [23/231] skipped (no command): buildSrc/build.gradle
23:36:41 [INFO] [lock] [24/231] skipped (no command): buildSrc/src/testKit/symbolic-link-preserving-tar/build.gradle
23:36:41 [INFO] [lock] [25/231] skipped (no command): buildSrc/src/testKit/testingConventions/build.gradle
23:36:41 [INFO] [lock] [26/231] skipped (no command): buildSrc/src/testKit/opensearch.build/build.gradle
23:36:41 [INFO] [lock] [27/231] skipped (no command): buildSrc/src/testKit/opensearch-build-resources/build.gradle
23:36:41 [INFO] [lock] [28/231] skipped (no command): buildSrc/src/testKit/reaper/build.gradle
23:36:41 [INFO] [lock] [29/231] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/build.gradle
23:36:41 [INFO] [lock] [30/231] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/sample_jars/build.gradle
23:36:41 [INFO] [lock] [31/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/build.gradle
23:36:41 [INFO] [lock] [32/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/minor/build.gradle
23:36:41 [INFO] [lock] [33/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/bugfix/build.gradle
23:36:41 [INFO] [lock] [34/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/build.gradle
23:36:41 [INFO] [lock] [35/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/oss-darwin-tar/build.gradle
23:36:41 [INFO] [lock] [36/231] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/darwin-tar/build.gradle
23:36:41 [INFO] [lock] [37/231] skipped (no command): buildSrc/reaper/build.gradle
23:36:41 [INFO] [lock] [38/231] skipped (no command): sandbox/build.gradle
23:36:41 [INFO] [lock] [39/231] skipped (no command): sandbox/libs/build.gradle
23:36:41 [INFO] [lock] [40/231] skipped (no command): sandbox/libs/analytics-framework/build.gradle
23:36:41 [INFO] [lock] [41/231] skipped (no command): sandbox/modules/build.gradle
23:36:41 [INFO] [lock] [42/231] skipped (no command): sandbox/plugins/build.gradle
23:36:41 [INFO] [lock] [43/231] skipped (no command): sandbox/plugins/analytics-backend-datafusion/build.gradle
23:36:41 [INFO] [lock] [44/231] skipped (no command): sandbox/plugins/analytics-backend-lucene/build.gradle
23:36:41 [INFO] [lock] [45/231] skipped (no command): sandbox/plugins/analytics-engine/build.gradle
23:36:41 [INFO] [lock] [46/231] skipped (no command): client/benchmark/build.gradle
23:36:41 [INFO] [lock] [47/231] skipped (no command): client/rest/build.gradle
23:36:41 [INFO] [lock] [48/231] skipped (no command): client/rest-high-level/build.gradle
23:36:41 [INFO] [lock] [49/231] skipped (no command): client/client-benchmark-noop-api-plugin/build.gradle
23:36:41 [INFO] [lock] [50/231] skipped (no command): client/test/build.gradle
23:36:41 [INFO] [lock] [51/231] skipped (no command): client/sniffer/build.gradle
23:36:41 [INFO] [lock] [52/231] skipped (no command): server/build.gradle
23:36:41 [INFO] [lock] [53/231] skipped (no command): server/cli/build.gradle
23:36:41 [INFO] [lock] [54/231] skipped (no command): rest-api-spec/build.gradle
23:36:41 [INFO] [lock] [55/231] skipped (no command): modules/build.gradle
23:36:41 [INFO] [lock] [56/231] skipped (no command): modules/systemd/build.gradle
23:36:41 [INFO] [lock] [57/231] skipped (no command): modules/ingest-geoip/build.gradle
23:36:41 [INFO] [lock] [58/231] skipped (no command): modules/analysis-common/build.gradle
23:36:41 [INFO] [lock] [59/231] skipped (no command): modules/lang-painless/build.gradle
23:36:41 [INFO] [lock] [60/231] skipped (no command): modules/lang-painless/spi/build.gradle
23:36:41 [INFO] [lock] [61/231] skipped (no command): modules/opensearch-dashboards/build.gradle
23:36:41 [INFO] [lock] [62/231] skipped (no command): modules/ingest-common/build.gradle
23:36:41 [INFO] [lock] [63/231] skipped (no command): modules/autotagging-commons/build.gradle
23:36:41 [INFO] [lock] [64/231] skipped (no command): modules/autotagging-commons/common/build.gradle
23:36:41 [INFO] [lock] [65/231] skipped (no command): modules/autotagging-commons/spi/build.gradle
23:36:41 [INFO] [lock] [66/231] skipped (no command): modules/reindex/build.gradle
23:36:41 [INFO] [lock] [67/231] skipped (no command): modules/repository-url/build.gradle
23:36:41 [INFO] [lock] [68/231] skipped (no command): modules/transport-netty4/build.gradle
23:36:41 [INFO] [lock] [69/231] skipped (no command): modules/parent-join/build.gradle
23:36:41 [INFO] [lock] [70/231] skipped (no command): modules/search-pipeline-common/build.gradle
23:36:41 [INFO] [lock] [71/231] skipped (no command): modules/mapper-extras/build.gradle
23:36:41 [INFO] [lock] [72/231] skipped (no command): modules/lang-mustache/build.gradle
23:36:41 [INFO] [lock] [73/231] skipped (no command): modules/rank-eval/build.gradle
23:36:41 [INFO] [lock] [74/231] skipped (no command): modules/lang-expression/build.gradle
23:36:41 [INFO] [lock] [75/231] skipped (no command): modules/aggs-matrix-stats/build.gradle
23:36:41 [INFO] [lock] [76/231] skipped (no command): modules/geo/build.gradle
23:36:41 [INFO] [lock] [77/231] skipped (no command): modules/percolator/build.gradle
23:36:41 [INFO] [lock] [78/231] skipped (no command): modules/ingest-user-agent/build.gradle
23:36:41 [INFO] [lock] [79/231] skipped (no command): modules/cache-common/build.gradle
23:36:41 [INFO] [lock] [80/231] skipped (no command): modules/transport-grpc/build.gradle
23:36:41 [INFO] [lock] [81/231] skipped (no command): modules/transport-grpc/spi/build.gradle
23:36:41 [INFO] [lock] [82/231] skipped (no command): modules/store-subdirectory/build.gradle
23:36:41 [INFO] [lock] [83/231] skipped (no command): plugins/build.gradle
23:36:41 [INFO] [lock] [84/231] skipped (no command): plugins/examples/build.gradle
23:36:41 [INFO] [lock] [85/231] skipped (no command): plugins/examples/rescore/build.gradle
23:36:41 [INFO] [lock] [86/231] skipped (no command): plugins/examples/custom-settings/build.gradle
23:36:41 [INFO] [lock] [87/231] skipped (no command): plugins/examples/custom-significance-heuristic/build.gradle
23:36:41 [INFO] [lock] [88/231] skipped (no command): plugins/examples/rest-handler/build.gradle
23:36:41 [INFO] [lock] [89/231] skipped (no command): plugins/examples/stream-transport-example/build.gradle
23:36:41 [INFO] [lock] [90/231] skipped (no command): plugins/examples/system-search-processor/build.gradle
23:36:41 [INFO] [lock] [91/231] skipped (no command): plugins/examples/custom-suggester/build.gradle
23:36:41 [INFO] [lock] [92/231] skipped (no command): plugins/examples/system-ingest-processor/build.gradle
23:36:41 [INFO] [lock] [93/231] skipped (no command): plugins/examples/painless-allowlist/build.gradle
23:36:41 [INFO] [lock] [94/231] skipped (no command): plugins/examples/script-expert-scoring/build.gradle
23:36:41 [INFO] [lock] [95/231] skipped (no command): plugins/examples/mapping-transformer/build.gradle
23:36:41 [INFO] [lock] [96/231] skipped (no command): plugins/ingestion-fs/build.gradle
23:36:41 [INFO] [lock] [97/231] skipped (no command): plugins/cache-ehcache/build.gradle
23:36:41 [INFO] [lock] [98/231] skipped (no command): plugins/analysis-ukrainian/build.gradle
23:36:41 [INFO] [lock] [99/231] skipped (no command): plugins/analysis-icu/build.gradle
23:36:41 [INFO] [lock] [100/231] skipped (no command): plugins/repository-hdfs/build.gradle
23:36:41 [INFO] [lock] [101/231] skipped (no command): plugins/repository-azure/build.gradle
23:36:41 [INFO] [lock] [102/231] skipped (no command): plugins/analysis-kuromoji/build.gradle
23:36:41 [INFO] [lock] [103/231] skipped (no command): plugins/analysis-phonetic/build.gradle
23:36:41 [INFO] [lock] [104/231] skipped (no command): plugins/repository-gcs/build.gradle
23:36:41 [INFO] [lock] [105/231] skipped (no command): plugins/transport-reactor-netty4/build.gradle
23:36:41 [INFO] [lock] [106/231] skipped (no command): plugins/mapper-murmur3/build.gradle
23:36:41 [INFO] [lock] [107/231] skipped (no command): plugins/discovery-azure-classic/build.gradle
23:36:41 [INFO] [lock] [108/231] skipped (no command): plugins/crypto-kms/build.gradle
23:36:41 [INFO] [lock] [109/231] skipped (no command): plugins/telemetry-otel/build.gradle
23:36:41 [INFO] [lock] [110/231] skipped (no command): plugins/analysis-phonenumber/build.gradle
23:36:41 [INFO] [lock] [111/231] skipped (no command): plugins/store-smb/build.gradle
23:36:41 [INFO] [lock] [112/231] skipped (no command): plugins/analysis-nori/build.gradle
23:36:41 [INFO] [lock] [113/231] skipped (no command): plugins/analysis-stempel/build.gradle
23:36:41 [INFO] [lock] [114/231] skipped (no command): plugins/ingestion-kinesis/build.gradle
23:36:41 [INFO] [lock] [115/231] skipped (no command): plugins/mapper-annotated-text/build.gradle
23:36:41 [INFO] [lock] [116/231] skipped (no command): plugins/analysis-smartcn/build.gradle
23:36:41 [INFO] [lock] [117/231] skipped (no command): plugins/repository-s3/build.gradle
23:36:41 [INFO] [lock] [118/231] skipped (no command): plugins/discovery-ec2/build.gradle
23:36:41 [INFO] [lock] [119/231] skipped (no command): plugins/discovery-ec2/qa/build.gradle
23:36:41 [INFO] [lock] [120/231] skipped (no command): plugins/discovery-ec2/qa/amazon-ec2/build.gradle
23:36:41 [INFO] [lock] [121/231] skipped (no command): plugins/discovery-gce/build.gradle
23:36:41 [INFO] [lock] [122/231] skipped (no command): plugins/discovery-gce/qa/build.gradle
23:36:41 [INFO] [lock] [123/231] skipped (no command): plugins/discovery-gce/qa/gce/build.gradle
23:36:41 [INFO] [lock] [124/231] skipped (no command): plugins/ingestion-kafka/build.gradle
23:36:41 [INFO] [lock] [125/231] skipped (no command): plugins/arrow-flight-rpc/build.gradle
23:36:41 [INFO] [lock] [126/231] skipped (no command): plugins/workload-management/build.gradle
23:36:41 [INFO] [lock] [127/231] skipped (no command): plugins/workload-management/wlm-spi/build.gradle
23:36:41 [INFO] [lock] [128/231] skipped (no command): plugins/mapper-size/build.gradle
23:36:41 [INFO] [lock] [129/231] skipped (no command): plugins/ingest-attachment/build.gradle
23:36:41 [INFO] [lock] [130/231] skipped (no command): doc-tools/build.gradle
23:36:41 [INFO] [lock] [131/231] skipped (no command): doc-tools/missing-doclet/build.gradle
23:36:41 [INFO] [lock] [132/231] skipped (no command): qa/build.gradle
23:36:41 [INFO] [lock] [133/231] skipped (no command): qa/fips-compliance/build.gradle
23:36:41 [INFO] [lock] [134/231] skipped (no command): qa/evil-tests/build.gradle
23:36:41 [INFO] [lock] [135/231] skipped (no command): qa/full-cluster-restart/build.gradle
23:36:41 [INFO] [lock] [136/231] skipped (no command): qa/wildfly/build.gradle
23:36:41 [INFO] [lock] [137/231] skipped (no command): qa/systemd-test/build.gradle
23:36:41 [INFO] [lock] [138/231] skipped (no command): qa/mixed-cluster/build.gradle
23:36:41 [INFO] [lock] [139/231] skipped (no command): qa/smoke-test-multinode/build.gradle
23:36:41 [INFO] [lock] [140/231] skipped (no command): qa/verify-version-constants/build.gradle
23:36:41 [INFO] [lock] [141/231] skipped (no command): qa/smoke-test-ingest-disabled/build.gradle
23:36:41 [INFO] [lock] [142/231] skipped (no command): qa/rolling-upgrade/build.gradle
23:36:41 [INFO] [lock] [143/231] skipped (no command): qa/no-bootstrap-tests/build.gradle
23:36:41 [INFO] [lock] [144/231] skipped (no command): qa/repository-multi-version/build.gradle
23:36:41 [INFO] [lock] [145/231] skipped (no command): qa/smoke-test-http/build.gradle
23:36:41 [INFO] [lock] [146/231] skipped (no command): qa/logging-config/build.gradle
23:36:41 [INFO] [lock] [147/231] skipped (no command): qa/smoke-test-plugins/build.gradle
23:36:41 [INFO] [lock] [148/231] skipped (no command): qa/ccs-unavailable-clusters/build.gradle
23:36:41 [INFO] [lock] [149/231] skipped (no command): qa/unconfigured-node-name/build.gradle
23:36:41 [INFO] [lock] [150/231] skipped (no command): qa/os/build.gradle
23:36:41 [INFO] [lock] [151/231] skipped (no command): qa/os/windows-2016/build.gradle
23:36:41 [INFO] [lock] [152/231] skipped (no command): qa/os/debian-9/build.gradle
23:36:41 [INFO] [lock] [153/231] skipped (no command): qa/os/oel-6/build.gradle
23:36:41 [INFO] [lock] [154/231] skipped (no command): qa/os/ubuntu-1804/build.gradle
23:36:41 [INFO] [lock] [155/231] skipped (no command): qa/os/oel-7/build.gradle
23:36:41 [INFO] [lock] [156/231] skipped (no command): qa/os/fedora-28/build.gradle
23:36:41 [INFO] [lock] [157/231] skipped (no command): qa/os/sles-12/build.gradle
23:36:41 [INFO] [lock] [158/231] skipped (no command): qa/os/centos-6/build.gradle
23:36:41 [INFO] [lock] [159/231] skipped (no command): qa/os/debian-8/build.gradle
23:36:41 [INFO] [lock] [160/231] skipped (no command): qa/os/fedora-29/build.gradle
23:36:41 [INFO] [lock] [161/231] skipped (no command): qa/os/windows-2012r2/build.gradle
23:36:41 [INFO] [lock] [162/231] skipped (no command): qa/os/centos-7/build.gradle
23:36:41 [INFO] [lock] [163/231] skipped (no command): qa/os/ubuntu-1604/build.gradle
23:36:41 [INFO] [lock] [164/231] skipped (no command): qa/remote-clusters/build.gradle
23:36:41 [INFO] [lock] [165/231] skipped (no command): qa/smoke-test-ingest-with-all-dependencies/build.gradle
23:36:41 [INFO] [lock] [166/231] skipped (no command): qa/die-with-dignity/build.gradle
23:36:41 [INFO] [lock] [167/231] skipped (no command): qa/multi-cluster-search/build.gradle
23:36:41 [INFO] [lock] [168/231] skipped (no command): distribution/build.gradle
23:36:41 [INFO] [lock] [169/231] skipped (no command): distribution/packages/build.gradle
23:36:41 [INFO] [lock] [170/231] skipped (no command): distribution/packages/no-jdk-deb/build.gradle
23:36:41 [INFO] [lock] [171/231] skipped (no command): distribution/packages/no-jdk-arm64-deb/build.gradle
23:36:41 [INFO] [lock] [172/231] skipped (no command): distribution/packages/arm64-rpm/build.gradle
23:36:41 [INFO] [lock] [173/231] skipped (no command): distribution/packages/rpm/build.gradle
23:36:41 [INFO] [lock] [174/231] skipped (no command): distribution/packages/deb/build.gradle
23:36:41 [INFO] [lock] [175/231] skipped (no command): distribution/packages/arm64-no-jdk-deb/build.gradle
23:36:41 [INFO] [lock] [176/231] skipped (no command): distribution/packages/arm64-no-jdk-rpm/build.gradle
23:36:41 [INFO] [lock] [177/231] skipped (no command): distribution/packages/no-jdk-rpm/build.gradle
23:36:41 [INFO] [lock] [178/231] skipped (no command): distribution/packages/arm64-deb/build.gradle
23:36:41 [INFO] [lock] [179/231] skipped (no command): distribution/packages/no-jdk-arm64-rpm/build.gradle
23:36:41 [INFO] [lock] [180/231] skipped (no command): distribution/tools/fips-demo-installer-cli/build.gradle
23:36:41 [INFO] [lock] [181/231] skipped (no command): distribution/tools/launchers/build.gradle
23:36:41 [INFO] [lock] [182/231] skipped (no command): distribution/tools/plugin-cli/build.gradle
23:36:41 [INFO] [lock] [183/231] skipped (no command): distribution/tools/keystore-cli/build.gradle
23:36:41 [INFO] [lock] [184/231] skipped (no command): distribution/tools/java-version-checker/build.gradle
23:36:41 [INFO] [lock] [185/231] skipped (no command): distribution/bwc/build.gradle
23:36:41 [INFO] [lock] [186/231] skipped (no command): distribution/bwc/maintenance/build.gradle
23:36:41 [INFO] [lock] [187/231] skipped (no command): distribution/bwc/minor/build.gradle
23:36:41 [INFO] [lock] [188/231] skipped (no command): distribution/bwc/bugfix/build.gradle
23:36:41 [INFO] [lock] [189/231] skipped (no command): distribution/bwc/staged/build.gradle
23:36:41 [INFO] [lock] [190/231] skipped (no command): distribution/archives/build.gradle
23:36:41 [INFO] [lock] [191/231] skipped (no command): distribution/archives/no-jdk-darwin-tar/build.gradle
23:36:41 [INFO] [lock] [192/231] skipped (no command): distribution/archives/no-jdk-windows-zip/build.gradle
23:36:41 [INFO] [lock] [193/231] skipped (no command): distribution/archives/no-jdk-linux-riscv64-tar/build.gradle
23:36:41 [INFO] [lock] [194/231] skipped (no command): distribution/archives/no-jdk-darwin-arm64-tar/build.gradle
23:36:41 [INFO] [lock] [195/231] skipped (no command): distribution/archives/integ-test-zip/build.gradle
23:36:41 [INFO] [lock] [196/231] skipped (no command): distribution/archives/linux-s390x-tar/build.gradle
23:36:41 [INFO] [lock] [197/231] skipped (no command): distribution/archives/jre-linux-tar/build.gradle
23:36:41 [INFO] [lock] [198/231] skipped (no command): distribution/archives/linux-arm64-tar/build.gradle
23:36:41 [INFO] [lock] [199/231] skipped (no command): distribution/archives/darwin-tar/build.gradle
23:36:41 [INFO] [lock] [200/231] skipped (no command): distribution/archives/windows-zip/build.gradle
23:36:41 [INFO] [lock] [201/231] skipped (no command): distribution/archives/freebsd-tar/build.gradle
23:36:41 [INFO] [lock] [202/231] skipped (no command): distribution/archives/linux-riscv64-tar/build.gradle
23:36:41 [INFO] [lock] [203/231] skipped (no command): distribution/archives/linux-ppc64le-tar/build.gradle
23:36:41 [INFO] [lock] [204/231] skipped (no command): distribution/archives/no-jdk-freebsd-tar/build.gradle
23:36:41 [INFO] [lock] [205/231] skipped (no command): distribution/archives/no-jdk-linux-ppc64le-tar/build.gradle
23:36:41 [INFO] [lock] [206/231] skipped (no command): distribution/archives/no-jdk-linux-arm64-tar/build.gradle
23:36:41 [INFO] [lock] [207/231] skipped (no command): distribution/archives/no-jdk-linux-tar/build.gradle
23:36:41 [INFO] [lock] [208/231] skipped (no command): distribution/archives/darwin-arm64-tar/build.gradle
23:36:41 [INFO] [lock] [209/231] skipped (no command): distribution/archives/linux-tar/build.gradle
23:36:41 [INFO] [lock] [210/231] skipped (no command): distribution/docker/build.gradle
23:36:41 [INFO] [lock] [211/231] skipped (no command): distribution/docker/docker-riscv64-export/build.gradle
23:36:41 [INFO] [lock] [212/231] skipped (no command): distribution/docker/docker-arm64-export/build.gradle
23:36:41 [INFO] [lock] [213/231] skipped (no command): distribution/docker/docker-s390x-export/build.gradle
23:36:41 [INFO] [lock] [214/231] skipped (no command): distribution/docker/docker-build-context/build.gradle
23:36:41 [INFO] [lock] [215/231] skipped (no command): distribution/docker/docker-ppc64le-export/build.gradle
23:36:41 [INFO] [lock] [216/231] skipped (no command): distribution/docker/docker-arm64-build-context/build.gradle
23:36:41 [INFO] [lock] [217/231] skipped (no command): distribution/docker/docker-export/build.gradle
23:36:41 [INFO] [lock] [218/231] skipped (no command): docs/build.gradle
23:36:41 [INFO] [lock] [219/231] skipped (no command): test/build.gradle
23:36:41 [INFO] [lock] [220/231] skipped (no command): test/telemetry/build.gradle
23:36:41 [INFO] [lock] [221/231] skipped (no command): test/fixtures/build.gradle
23:36:41 [INFO] [lock] [222/231] skipped (no command): test/fixtures/krb5kdc-fixture/build.gradle
23:36:41 [INFO] [lock] [223/231] skipped (no command): test/fixtures/minio-fixture/build.gradle
23:36:41 [INFO] [lock] [224/231] skipped (no command): test/fixtures/azure-fixture/build.gradle
23:36:41 [INFO] [lock] [225/231] skipped (no command): test/fixtures/s3-fixture/build.gradle
23:36:41 [INFO] [lock] [226/231] skipped (no command): test/fixtures/hdfs-fixture/build.gradle
23:36:41 [INFO] [lock] [227/231] skipped (no command): test/fixtures/gcs-fixture/build.gradle
23:36:41 [INFO] [lock] [228/231] skipped (no command): test/framework/build.gradle
23:36:41 [INFO] [lock] [229/231] skipped (no command): test/external-modules/build.gradle
23:36:41 [INFO] [lock] [230/231] skipped (no command): test/external-modules/delayed-aggs/build.gradle
23:36:41 [INFO] [lock] [231/231] skipped (no command): test/logger-usage/build.gradle
23:36:41 [INFO] lock generation: ok=0, failed=1, skipped=230
23:36:41 [INFO] STAGE DONE:  ecosystem
23:36:41 [INFO] ============================================================
23:36:41 [INFO] STAGE START: cplus_scan
23:36:41 [INFO] ============================================================
23:36:41 [INFO] cplus_scan skipped (--skip-cplus-scan)
23:36:41 [INFO] STAGE DONE:  cplus_scan
23:36:41 [INFO] ============================================================
23:36:41 [INFO] STAGE START: trivy
23:36:41 [INFO] ============================================================
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
23:36:42 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/opensearch/_repos/opensearch)
[INFO] restored template pom.xml files: 0
23:36:44 [WARNING] [cplus] no cplus sbom files to merge — skipping
23:36:44 [INFO] STAGE DONE:  trivy
23:36:44 [INFO] ============================================================
23:36:44 [INFO] STAGE START: vuln_management
23:36:44 [INFO] ============================================================
23:36:44 [INFO] [normalize] processing: origsbom.json
23:36:44 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
23:36:44 [INFO] [normalize] saved: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/sources/origsbom/origsbom_normalized.json
23:36:44 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/sources/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/sources/origsbom/origsbom_normalized.json (token=019f29b2-b07f-7c75-a6a9-98904d06941a)
[dt] origsbom uploaded to orig project: 90c437ed-7167-4ef8-aca6-e809468372b8
[dt] ===== enrich origsbom =====
[trivy] scanning: origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/sources/origsbom/origsbom_normalized.json (token=019f29b2-b0ae-714d-b6ec-327dcd2424ac)
[dt] bom/token poll 1: processing=True
[trivy] done: origsbom_normalized.json components=0 vulnerabilities=0
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dual] +0 vulnerability record(s) added from trivy (not seen by DT yet)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 7a914d32-05e2-4335-bbc2-d8ef5eb6dd63
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/sbom-clean.json (token=019f29b2-ebf4-75a4-8a17-07c35576c832)
[dt] empty sbom-clean uploaded to safe project: 7a914d32-05e2-4335-bbc2-d8ef5eb6dd63
[OK] report.xlsx           : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] dt_vs_trivy_safe_scan.xlsx : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/debug/dt_vs_trivy_safe_scan.xlsx
[OK]   comparison rows          : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/debug/failed_safe_versions_debug.txt
23:36:59 [WARNING] [vuln] cplus_sbom NOT found at /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/cplus_sbom.json — C/C++ scan may have been skipped or failed
23:36:59 [INFO] STAGE DONE:  vuln_management
23:36:59 [INFO] pipeline summary:
23:36:59 [INFO] stage ecosystem: done
23:36:59 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/appsec/ecosystems/lock_summary.json
23:36:59 [WARNING] stage ecosystem: lock generation had failures: ok=0, failed=1, skipped=230
23:36:59 [INFO] stage cplus_scan: skipped
23:36:59 [WARNING] stage cplus_scan: --skip-cplus-scan set: C/C++ vendored-library scan skipped
23:36:59 [INFO] stage trivy_sbom: done
23:36:59 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/origsbom.json
23:36:59 [INFO] stage vuln_management: done
23:36:59 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/reports/report.xlsx
23:36:59 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954/sbom/sbom-clean.json
23:36:59 [INFO] pipeline finished successfully
23:36:59 [INFO] artifacts directory: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954
2026-07-03 23:36:59 | INFO    |   moving results: /home/kali/Desktop/jobs/opensearch/jobs/b8737b2b88c742ee9a6884eb11077954 -> /home/kali/Desktop/results/2026-07-03/opensearch__3.6.0
2026-07-03 23:36:59 | INFO    |   [OK] opensearch / 3.6.0 -> /home/kali/Desktop/results/2026-07-03/opensearch__3.6.0
2026-07-03 23:36:59 | INFO    | run log written: /home/kali/Desktop/results/2026-07-03/run.log
2026-07-03 23:36:59 | INFO    | all 1 scan(s) completed successfully
