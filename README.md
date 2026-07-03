leanup] removing file: /home/kali/Desktop/jobs/opensearch/_repos/opensearch/buildSrc/src/main/resources/META-INF/gradle-plugins/opensearch.test.fixtures.properties
[cleanup] done in 2.9s — removed 164 dirs, 1 files
22:58:22 [INFO] STAGE DONE:  cleanup_root
22:58:22 [INFO] ============================================================
22:58:22 [INFO] STAGE START: ecosystem (lock-files scan + apply)
22:58:22 [INFO] ============================================================
22:58:28 [INFO] ecosystem report: /home/kali/Desktop/jobs/opensearch/jobs/95eae439ca934b8682632e387845e366/appsec/ecosystems/lock_summary.json
22:58:28 [INFO] lock suggestions: 204
22:58:28 [INFO] [lock] [1/204] start: build.gradle
22:58:28 [INFO] [lock]         cmd:  cd "/home/kali/Desktop/jobs/opensearch/_repos/opensearch" && ./gradlew resolveTrivyLockDeps --init-script init-trivy-locks.gradle --write-locks --warning-mode none --no-daemon
22:58:28 [INFO] [lock] PID=151793 PGID=151624: cd "/home/kali/Desktop/jobs/opensearch/_repos/opensearch" && ./gradlew resolveTrivyLockDeps --init-script init-trivy-locks.gradle --write-locks --warning-mode none --no-daemon
22:58:29 [INFO] [lock][stdout] To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
22:58:30 [INFO] [lock][stdout] Daemon will be stopped at the end of the build 
22:58:30 [INFO] [lock][stderr] 
22:58:30 [INFO] [lock][stderr] FAILURE: Build failed with an exception.
22:58:30 [INFO] [lock][stderr] 
22:58:30 [INFO] [lock][stderr] * What went wrong:
22:58:30 [INFO] [lock][stderr] The specified initialization script '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/init-trivy-locks.gradle' does not exist.
22:58:30 [INFO] [lock][stderr] 
22:58:30 [INFO] [lock][stderr] * Try:
22:58:30 [INFO] [lock][stderr] > Run with --stacktrace option to get the stack trace.
22:58:30 [INFO] [lock][stderr] > Run with --info or --debug option to get more log output.
22:58:30 [INFO] [lock][stderr] > Run with --scan to get full insights from a Build Scan (powered by Develocity).
22:58:30 [INFO] [lock][stderr] > Get more help at https://help.gradle.org.
22:58:30 [INFO] [lock][stderr] 
22:58:30 [INFO] [lock][stderr] BUILD FAILED in 1s
22:58:30 [INFO] [lock] [1/204] failed (rc=1, 1.6s): build.gradle
22:58:30 [WARNING] [lock]         stderr: FAILURE: Build failed with an exception.

* What went wrong:
The specified initialization script '/home/kali/Desktop/jobs/opensearch/_repos/opensearch/init-trivy-locks.gradle' does not exist.

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights from a Build Scan (powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 1s
22:58:30 [WARNING] [lock]         stdout: To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.4.0/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
Daemon will be stopped at the end of the build
22:58:30 [INFO] [lock] [2/204] skipped (no command): benchmarks/build.gradle
22:58:30 [INFO] [lock] [3/204] skipped (no command): libs/build.gradle
22:58:30 [INFO] [lock] [4/204] skipped (no command): libs/common/build.gradle
