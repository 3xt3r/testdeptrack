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
23:05:55 [INFO] [lock] PID=154330 PGID=154140: cd "/home/kali/Desktop/jobs/opensearch/_repos/opensearch" && set -e
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
23:05:55 [INFO] [lock][stdout] [trivy-lock-prep] patched settings.gradle (backup: settings.gradle.trivylock.bak)
23:05:56 [INFO] [lock][stdout] To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
23:05:57 [INFO] [lock][stdout] Daemon will be stopped at the end of the build 
23:06:00 [INFO] [lock][stderr] 
23:06:00 [INFO] [lock][stderr] FAILURE: Build failed with an exception.
23:06:00 [INFO] [lock][stderr] 
23:06:00 [INFO] [lock][stderr] * Where:
23:06:00 [INFO] [lock][stderr] Settings file '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/settings.gradle' line: 150
23:06:00 [INFO] [lock][stderr] 
23:06:00 [INFO] [lock][stderr] * What went wrong:
23:06:00 [INFO] [lock][stderr] A problem occurred evaluating settings 'OpenSearch'.
23:06:00 [INFO] [lock][stderr] > Project with path ':test:external-modules' could not be found.
23:06:00 [INFO] [lock][stderr] 
23:06:00 [INFO] [lock][stderr] * Try:
23:06:00 [INFO] [lock][stderr] > Run with --stacktrace option to get the stack trace.
23:06:00 [INFO] [lock][stderr] > Run with --info or --debug option to get more log output.
23:06:00 [INFO] [lock][stderr] > Run with --scan to get full insights from a Build Scan (powered by Develocity).
23:06:00 [INFO] [lock][stderr] > Get more help at https://help.gradle.org.
23:06:00 [INFO] [lock][stderr] 
23:06:00 [INFO] [lock][stderr] BUILD FAILED in 4s
23:06:00 [INFO] [lock] [1/204] failed (rc=1, 4.8s): build.gradle
23:06:00 [WARNING] [lock]         stderr: FAILURE: Build failed with an exception.

* Where:
Settings file '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/settings.gradle' line: 150

* What went wrong:
A problem occurred evaluating settings 'OpenSearch'.
> Project with path ':test:external-modules' could not be found.

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 4s
23:06:00 [WARNING] [lock]         stdout: [trivy-lock-prep] patched settings.gradle (backup: settings.gradle.trivylock.bak)
To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
Daemon will be stopped at the end of the build
23:06:00 [INFO] [lock] [2/204] skipped (no command): benchmarks/build.gradle
23:06:00 [INFO] [lock] [3/204] skipped (no command): libs/build.gradle
23:06:00 [INFO] [lock] [4/204] skipped (no command): libs/common/build.gradle
23:06:00 [INFO] [lock] [5/204] skipped (no command): libs/telemetry/build.gradle
23:06:00 [INFO] [lock] [6/204] skipped (no command): libs/core/build.gradle
23:06:00 [INFO] [lock] [7/204] skipped (no command): libs/dissect/build.gradle
23:06:00 [INFO] [lock] [8/204] skipped (no command): libs/netty4/build.gradle
23:06:00 [INFO] [lock] [9/204] skipped (no command): libs/ssl-config/build.gradle
23:06:00 [INFO] [lock] [10/204] skipped (no command): libs/compress/build.gradle
23:06:00 [INFO] [lock] [11/204] skipped (no command): libs/nio/build.gradle
23:06:00 [INFO] [lock] [12/204] skipped (no command): libs/plugin-classloader/build.gradle
23:06:00 [INFO] [lock] [13/204] skipped (no command): libs/grok/build.gradle
23:06:00 [INFO] [lock] [14/204] skipped (no command): libs/secure-sm/build.gradle
23:06:00 [INFO] [lock] [15/204] skipped (no command): libs/cli/build.gradle
23:06:00 [INFO] [lock] [16/204] skipped (no command): libs/agent-sm/build.gradle
23:06:00 [INFO] [lock] [17/204] skipped (no command): libs/agent-sm/agent/build.gradle
23:06:00 [INFO] [lock] [18/204] skipped (no command): libs/agent-sm/bootstrap/build.gradle
23:06:00 [INFO] [lock] [19/204] skipped (no command): libs/agent-sm/agent-policy/build.gradle
23:06:00 [INFO] [lock] [20/204] skipped (no command): libs/task-commons/build.gradle
23:06:00 [INFO] [lock] [21/204] skipped (no command): libs/geo/build.gradle
23:06:00 [INFO] [lock] [22/204] skipped (no command): libs/x-content/build.gradle
23:06:00 [INFO] [lock] [23/204] skipped (no command): buildSrc/build.gradle
23:06:00 [INFO] [lock] [24/204] skipped (no command): buildSrc/src/testKit/symbolic-link-preserving-tar/build.gradle
23:06:00 [INFO] [lock] [25/204] skipped (no command): buildSrc/src/testKit/testingConventions/build.gradle
23:06:00 [INFO] [lock] [26/204] skipped (no command): buildSrc/src/testKit/opensearch.build/build.gradle
23:06:00 [INFO] [lock] [27/204] skipped (no command): buildSrc/src/testKit/opensearch-build-resources/build.gradle
23:06:00 [INFO] [lock] [28/204] skipped (no command): buildSrc/src/testKit/reaper/build.gradle
23:06:00 [INFO] [lock] [29/204] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/build.gradle
23:06:00 [INFO] [lock] [30/204] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/sample_jars/build.gradle
23:06:00 [INFO] [lock] [31/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/build.gradle
23:06:00 [INFO] [lock] [32/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/minor/build.gradle
23:06:00 [INFO] [lock] [33/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/bugfix/build.gradle
23:06:00 [INFO] [lock] [34/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/build.gradle
23:06:00 [INFO] [lock] [35/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/oss-darwin-tar/build.gradle
23:06:00 [INFO] [lock] [36/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/darwin-tar/build.gradle
23:06:00 [INFO] [lock] [37/204] skipped (no command): buildSrc/reaper/build.gradle
23:06:00 [INFO] [lock] [38/204] skipped (no command): sandbox/build.gradle
23:06:00 [INFO] [lock] [39/204] skipped (no command): sandbox/libs/build.gradle
23:06:00 [INFO] [lock] [40/204] skipped (no command): sandbox/libs/analytics-framework/build.gradle
23:06:00 [INFO] [lock] [41/204] skipped (no command): sandbox/modules/build.gradle
23:06:00 [INFO] [lock] [42/204] skipped (no command): sandbox/plugins/build.gradle
23:06:00 [INFO] [lock] [43/204] skipped (no command): sandbox/plugins/analytics-backend-datafusion/build.gradle
23:06:00 [INFO] [lock] [44/204] skipped (no command): sandbox/plugins/analytics-backend-lucene/build.gradle
23:06:00 [INFO] [lock] [45/204] skipped (no command): sandbox/plugins/analytics-engine/build.gradle
23:06:00 [INFO] [lock] [46/204] skipped (no command): client/benchmark/build.gradle
23:06:00 [INFO] [lock] [47/204] skipped (no command): client/rest/build.gradle
23:06:00 [INFO] [lock] [48/204] skipped (no command): client/rest-high-level/build.gradle
23:06:00 [INFO] [lock] [49/204] skipped (no command): client/client-benchmark-noop-api-plugin/build.gradle
23:06:00 [INFO] [lock] [50/204] skipped (no command): client/sniffer/build.gradle
23:06:00 [INFO] [lock] [51/204] skipped (no command): server/build.gradle
23:06:00 [INFO] [lock] [52/204] skipped (no command): server/cli/build.gradle
23:06:00 [INFO] [lock] [53/204] skipped (no command): rest-api-spec/build.gradle
23:06:00 [INFO] [lock] [54/204] skipped (no command): modules/build.gradle
23:06:00 [INFO] [lock] [55/204] skipped (no command): modules/systemd/build.gradle
23:06:00 [INFO] [lock] [56/204] skipped (no command): modules/ingest-geoip/build.gradle
23:06:00 [INFO] [lock] [57/204] skipped (no command): modules/analysis-common/build.gradle
23:06:00 [INFO] [lock] [58/204] skipped (no command): modules/lang-painless/build.gradle
23:06:00 [INFO] [lock] [59/204] skipped (no command): modules/lang-painless/spi/build.gradle
23:06:00 [INFO] [lock] [60/204] skipped (no command): modules/opensearch-dashboards/build.gradle
23:06:00 [INFO] [lock] [61/204] skipped (no command): modules/ingest-common/build.gradle
23:06:00 [INFO] [lock] [62/204] skipped (no command): modules/autotagging-commons/build.gradle
23:06:00 [INFO] [lock] [63/204] skipped (no command): modules/autotagging-commons/common/build.gradle
23:06:00 [INFO] [lock] [64/204] skipped (no command): modules/autotagging-commons/spi/build.gradle
23:06:00 [INFO] [lock] [65/204] skipped (no command): modules/reindex/build.gradle
23:06:00 [INFO] [lock] [66/204] skipped (no command): modules/repository-url/build.gradle
23:06:00 [INFO] [lock] [67/204] skipped (no command): modules/transport-netty4/build.gradle
23:06:00 [INFO] [lock] [68/204] skipped (no command): modules/parent-join/build.gradle
23:06:00 [INFO] [lock] [69/204] skipped (no command): modules/search-pipeline-common/build.gradle
23:06:00 [INFO] [lock] [70/204] skipped (no command): modules/mapper-extras/build.gradle
23:06:00 [INFO] [lock] [71/204] skipped (no command): modules/lang-mustache/build.gradle
23:06:00 [INFO] [lock] [72/204] skipped (no command): modules/rank-eval/build.gradle
23:06:00 [INFO] [lock] [73/204] skipped (no command): modules/lang-expression/build.gradle
23:06:00 [INFO] [lock] [74/204] skipped (no command): modules/aggs-matrix-stats/build.gradle
23:06:00 [INFO] [lock] [75/204] skipped (no command): modules/geo/build.gradle
23:06:00 [INFO] [lock] [76/204] skipped (no command): modules/percolator/build.gradle
23:06:00 [INFO] [lock] [77/204] skipped (no command): modules/ingest-user-agent/build.gradle
23:06:00 [INFO] [lock] [78/204] skipped (no command): modules/cache-common/build.gradle
23:06:00 [INFO] [lock] [79/204] skipped (no command): modules/transport-grpc/build.gradle
23:06:00 [INFO] [lock] [80/204] skipped (no command): modules/transport-grpc/spi/build.gradle
23:06:00 [INFO] [lock] [81/204] skipped (no command): modules/store-subdirectory/build.gradle
23:06:00 [INFO] [lock] [82/204] skipped (no command): plugins/build.gradle
23:06:00 [INFO] [lock] [83/204] skipped (no command): plugins/ingestion-fs/build.gradle
23:06:00 [INFO] [lock] [84/204] skipped (no command): plugins/cache-ehcache/build.gradle
23:06:00 [INFO] [lock] [85/204] skipped (no command): plugins/analysis-ukrainian/build.gradle
23:06:00 [INFO] [lock] [86/204] skipped (no command): plugins/analysis-icu/build.gradle
