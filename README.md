[cleanup] removing directory: /home/kali/Desktop/jobs/opensearch/_repos/opensearch/distribution/docker/src/test
[cleanup] removing file: /home/kali/Desktop/jobs/opensearch/_repos/opensearch/buildSrc/src/main/resources/META-INF/gradle-plugins/opensearch.test.fixtures.properties
[cleanup] done in 1.8s — removed 164 dirs, 1 files
18:59:26 [INFO] STAGE DONE:  cleanup_root
18:59:26 [INFO] ============================================================
18:59:26 [INFO] STAGE START: ecosystem (lock-files scan + apply)
18:59:26 [INFO] ============================================================
18:59:30 [INFO] ecosystem report: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/appsec/ecosystems/lock_summary.json
18:59:30 [INFO] lock suggestions: 204
18:59:30 [INFO] [lock] [1/204] skipped (no command): build.gradle
18:59:30 [INFO] [lock] [2/204] skipped (no command): benchmarks/build.gradle
18:59:30 [INFO] [lock] [3/204] skipped (no command): libs/build.gradle
18:59:30 [INFO] [lock] [4/204] skipped (no command): libs/common/build.gradle
18:59:30 [INFO] [lock] [5/204] skipped (no command): libs/telemetry/build.gradle
18:59:30 [INFO] [lock] [6/204] skipped (no command): libs/core/build.gradle
18:59:30 [INFO] [lock] [7/204] skipped (no command): libs/dissect/build.gradle
18:59:30 [INFO] [lock] [8/204] skipped (no command): libs/netty4/build.gradle
18:59:30 [INFO] [lock] [9/204] skipped (no command): libs/ssl-config/build.gradle
18:59:30 [INFO] [lock] [10/204] skipped (no command): libs/compress/build.gradle
18:59:30 [INFO] [lock] [11/204] skipped (no command): libs/nio/build.gradle
18:59:30 [INFO] [lock] [12/204] skipped (no command): libs/plugin-classloader/build.gradle
18:59:30 [INFO] [lock] [13/204] skipped (no command): libs/grok/build.gradle
18:59:30 [INFO] [lock] [14/204] skipped (no command): libs/secure-sm/build.gradle
18:59:30 [INFO] [lock] [15/204] skipped (no command): libs/cli/build.gradle
18:59:30 [INFO] [lock] [16/204] skipped (no command): libs/agent-sm/build.gradle
18:59:30 [INFO] [lock] [17/204] skipped (no command): libs/agent-sm/agent/build.gradle
18:59:30 [INFO] [lock] [18/204] skipped (no command): libs/agent-sm/bootstrap/build.gradle
18:59:30 [INFO] [lock] [19/204] skipped (no command): libs/agent-sm/agent-policy/build.gradle
18:59:30 [INFO] [lock] [20/204] skipped (no command): libs/task-commons/build.gradle
18:59:30 [INFO] [lock] [21/204] skipped (no command): libs/geo/build.gradle
18:59:30 [INFO] [lock] [22/204] skipped (no command): libs/x-content/build.gradle
18:59:30 [INFO] [lock] [23/204] skipped (no command): buildSrc/build.gradle
18:59:30 [INFO] [lock] [24/204] skipped (no command): buildSrc/src/testKit/symbolic-link-preserving-tar/build.gradle
18:59:30 [INFO] [lock] [25/204] skipped (no command): buildSrc/src/testKit/testingConventions/build.gradle
18:59:30 [INFO] [lock] [26/204] skipped (no command): buildSrc/src/testKit/opensearch.build/build.gradle
18:59:30 [INFO] [lock] [27/204] skipped (no command): buildSrc/src/testKit/opensearch-build-resources/build.gradle
18:59:30 [INFO] [lock] [28/204] skipped (no command): buildSrc/src/testKit/reaper/build.gradle
18:59:30 [INFO] [lock] [29/204] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/build.gradle
18:59:30 [INFO] [lock] [30/204] skipped (no command): buildSrc/src/testKit/thirdPartyAudit/sample_jars/build.gradle
18:59:30 [INFO] [lock] [31/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/build.gradle
18:59:30 [INFO] [lock] [32/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/minor/build.gradle
18:59:30 [INFO] [lock] [33/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/bwc/bugfix/build.gradle
18:59:30 [INFO] [lock] [34/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/build.gradle
18:59:30 [INFO] [lock] [35/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/oss-darwin-tar/build.gradle
18:59:30 [INFO] [lock] [36/204] skipped (no command): buildSrc/src/integTest/resources/org/opensearch/gradle/internal/fake_git/remote/distribution/archives/darwin-tar/build.gradle
18:59:30 [INFO] [lock] [37/204] skipped (no command): buildSrc/reaper/build.gradle
18:59:30 [INFO] [lock] [38/204] skipped (no command): sandbox/build.gradle
18:59:30 [INFO] [lock] [39/204] skipped (no command): sandbox/libs/build.gradle
18:59:30 [INFO] [lock] [40/204] skipped (no command): sandbox/libs/analytics-framework/build.gradle
18:59:30 [INFO] [lock] [41/204] skipped (no command): sandbox/modules/build.gradle
18:59:30 [INFO] [lock] [42/204] skipped (no command): sandbox/plugins/build.gradle
18:59:30 [INFO] [lock] [43/204] skipped (no command): sandbox/plugins/analytics-backend-datafusion/build.gradle
18:59:30 [INFO] [lock] [44/204] skipped (no command): sandbox/plugins/analytics-backend-lucene/build.gradle
18:59:30 [INFO] [lock] [45/204] skipped (no command): sandbox/plugins/analytics-engine/build.gradle
18:59:30 [INFO] [lock] [46/204] skipped (no command): client/benchmark/build.gradle
18:59:30 [INFO] [lock] [47/204] skipped (no command): client/rest/build.gradle
18:59:30 [INFO] [lock] [48/204] skipped (no command): client/rest-high-level/build.gradle
18:59:30 [INFO] [lock] [49/204] skipped (no command): client/client-benchmark-noop-api-plugin/build.gradle
18:59:30 [INFO] [lock] [50/204] skipped (no command): client/sniffer/build.gradle
18:59:30 [INFO] [lock] [51/204] skipped (no command): server/build.gradle
18:59:30 [INFO] [lock] [52/204] skipped (no command): server/cli/build.gradle
18:59:30 [INFO] [lock] [53/204] skipped (no command): rest-api-spec/build.gradle
18:59:30 [INFO] [lock] [54/204] skipped (no command): modules/build.gradle
18:59:30 [INFO] [lock] [55/204] skipped (no command): modules/systemd/build.gradle
18:59:30 [INFO] [lock] [56/204] skipped (no command): modules/ingest-geoip/build.gradle
18:59:30 [INFO] [lock] [57/204] skipped (no command): modules/analysis-common/build.gradle
18:59:30 [INFO] [lock] [58/204] skipped (no command): modules/lang-painless/build.gradle
18:59:30 [INFO] [lock] [59/204] skipped (no command): modules/lang-painless/spi/build.gradle
18:59:30 [INFO] [lock] [60/204] skipped (no command): modules/opensearch-dashboards/build.gradle
18:59:30 [INFO] [lock] [61/204] skipped (no command): modules/ingest-common/build.gradle
18:59:30 [INFO] [lock] [62/204] skipped (no command): modules/autotagging-commons/build.gradle
18:59:30 [INFO] [lock] [63/204] skipped (no command): modules/autotagging-commons/common/build.gradle
18:59:30 [INFO] [lock] [64/204] skipped (no command): modules/autotagging-commons/spi/build.gradle
18:59:30 [INFO] [lock] [65/204] skipped (no command): modules/reindex/build.gradle
18:59:30 [INFO] [lock] [66/204] skipped (no command): modules/repository-url/build.gradle
18:59:30 [INFO] [lock] [67/204] skipped (no command): modules/transport-netty4/build.gradle
18:59:30 [INFO] [lock] [68/204] skipped (no command): modules/parent-join/build.gradle
18:59:30 [INFO] [lock] [69/204] skipped (no command): modules/search-pipeline-common/build.gradle
18:59:30 [INFO] [lock] [70/204] skipped (no command): modules/mapper-extras/build.gradle
18:59:30 [INFO] [lock] [71/204] skipped (no command): modules/lang-mustache/build.gradle
18:59:30 [INFO] [lock] [72/204] skipped (no command): modules/rank-eval/build.gradle
18:59:30 [INFO] [lock] [73/204] skipped (no command): modules/lang-expression/build.gradle
18:59:30 [INFO] [lock] [74/204] skipped (no command): modules/aggs-matrix-stats/build.gradle
18:59:30 [INFO] [lock] [75/204] skipped (no command): modules/geo/build.gradle
18:59:30 [INFO] [lock] [76/204] skipped (no command): modules/percolator/build.gradle
18:59:30 [INFO] [lock] [77/204] skipped (no command): modules/ingest-user-agent/build.gradle
18:59:30 [INFO] [lock] [78/204] skipped (no command): modules/cache-common/build.gradle
18:59:30 [INFO] [lock] [79/204] skipped (no command): modules/transport-grpc/build.gradle
18:59:30 [INFO] [lock] [80/204] skipped (no command): modules/transport-grpc/spi/build.gradle
18:59:30 [INFO] [lock] [81/204] skipped (no command): modules/store-subdirectory/build.gradle
18:59:30 [INFO] [lock] [82/204] skipped (no command): plugins/build.gradle
18:59:30 [INFO] [lock] [83/204] skipped (no command): plugins/ingestion-fs/build.gradle
18:59:30 [INFO] [lock] [84/204] skipped (no command): plugins/cache-ehcache/build.gradle
18:59:30 [INFO] [lock] [85/204] skipped (no command): plugins/analysis-ukrainian/build.gradle
18:59:30 [INFO] [lock] [86/204] skipped (no command): plugins/analysis-icu/build.gradle
18:59:30 [INFO] [lock] [87/204] skipped (no command): plugins/repository-hdfs/build.gradle
18:59:30 [INFO] [lock] [88/204] skipped (no command): plugins/repository-azure/build.gradle
18:59:30 [INFO] [lock] [89/204] skipped (no command): plugins/analysis-kuromoji/build.gradle
18:59:30 [INFO] [lock] [90/204] skipped (no command): plugins/analysis-phonetic/build.gradle
18:59:30 [INFO] [lock] [91/204] skipped (no command): plugins/repository-gcs/build.gradle
18:59:30 [INFO] [lock] [92/204] skipped (no command): plugins/transport-reactor-netty4/build.gradle
18:59:30 [INFO] [lock] [93/204] skipped (no command): plugins/mapper-murmur3/build.gradle
18:59:30 [INFO] [lock] [94/204] skipped (no command): plugins/discovery-azure-classic/build.gradle
18:59:30 [INFO] [lock] [95/204] skipped (no command): plugins/crypto-kms/build.gradle
18:59:30 [INFO] [lock] [96/204] skipped (no command): plugins/telemetry-otel/build.gradle
18:59:30 [INFO] [lock] [97/204] skipped (no command): plugins/analysis-phonenumber/build.gradle
18:59:30 [INFO] [lock] [98/204] skipped (no command): plugins/store-smb/build.gradle
18:59:30 [INFO] [lock] [99/204] skipped (no command): plugins/analysis-nori/build.gradle
18:59:30 [INFO] [lock] [100/204] skipped (no command): plugins/analysis-stempel/build.gradle
18:59:30 [INFO] [lock] [101/204] skipped (no command): plugins/ingestion-kinesis/build.gradle
18:59:30 [INFO] [lock] [102/204] skipped (no command): plugins/mapper-annotated-text/build.gradle
18:59:30 [INFO] [lock] [103/204] skipped (no command): plugins/analysis-smartcn/build.gradle
18:59:30 [INFO] [lock] [104/204] skipped (no command): plugins/repository-s3/build.gradle
18:59:30 [INFO] [lock] [105/204] skipped (no command): plugins/discovery-ec2/build.gradle
18:59:30 [INFO] [lock] [106/204] skipped (no command): plugins/discovery-ec2/qa/build.gradle
18:59:30 [INFO] [lock] [107/204] skipped (no command): plugins/discovery-ec2/qa/amazon-ec2/build.gradle
18:59:30 [INFO] [lock] [108/204] skipped (no command): plugins/discovery-gce/build.gradle
18:59:30 [INFO] [lock] [109/204] skipped (no command): plugins/discovery-gce/qa/build.gradle
18:59:30 [INFO] [lock] [110/204] skipped (no command): plugins/discovery-gce/qa/gce/build.gradle
18:59:30 [INFO] [lock] [111/204] skipped (no command): plugins/ingestion-kafka/build.gradle
18:59:30 [INFO] [lock] [112/204] skipped (no command): plugins/arrow-flight-rpc/build.gradle
18:59:30 [INFO] [lock] [113/204] skipped (no command): plugins/workload-management/build.gradle
18:59:30 [INFO] [lock] [114/204] skipped (no command): plugins/workload-management/wlm-spi/build.gradle
18:59:30 [INFO] [lock] [115/204] skipped (no command): plugins/mapper-size/build.gradle
18:59:30 [INFO] [lock] [116/204] skipped (no command): plugins/ingest-attachment/build.gradle
18:59:30 [INFO] [lock] [117/204] skipped (no command): doc-tools/build.gradle
18:59:30 [INFO] [lock] [118/204] skipped (no command): doc-tools/missing-doclet/build.gradle
18:59:30 [INFO] [lock] [119/204] skipped (no command): qa/build.gradle
18:59:30 [INFO] [lock] [120/204] skipped (no command): qa/fips-compliance/build.gradle
18:59:30 [INFO] [lock] [121/204] skipped (no command): qa/evil-tests/build.gradle
18:59:30 [INFO] [lock] [122/204] skipped (no command): qa/full-cluster-restart/build.gradle
18:59:30 [INFO] [lock] [123/204] skipped (no command): qa/wildfly/build.gradle
18:59:30 [INFO] [lock] [124/204] skipped (no command): qa/systemd-test/build.gradle
18:59:30 [INFO] [lock] [125/204] skipped (no command): qa/mixed-cluster/build.gradle
18:59:30 [INFO] [lock] [126/204] skipped (no command): qa/smoke-test-multinode/build.gradle
18:59:30 [INFO] [lock] [127/204] skipped (no command): qa/verify-version-constants/build.gradle
18:59:30 [INFO] [lock] [128/204] skipped (no command): qa/smoke-test-ingest-disabled/build.gradle
18:59:30 [INFO] [lock] [129/204] skipped (no command): qa/rolling-upgrade/build.gradle
18:59:30 [INFO] [lock] [130/204] skipped (no command): qa/no-bootstrap-tests/build.gradle
18:59:30 [INFO] [lock] [131/204] skipped (no command): qa/repository-multi-version/build.gradle
18:59:30 [INFO] [lock] [132/204] skipped (no command): qa/smoke-test-http/build.gradle
18:59:30 [INFO] [lock] [133/204] skipped (no command): qa/logging-config/build.gradle
18:59:30 [INFO] [lock] [134/204] skipped (no command): qa/smoke-test-plugins/build.gradle
18:59:30 [INFO] [lock] [135/204] skipped (no command): qa/ccs-unavailable-clusters/build.gradle
18:59:30 [INFO] [lock] [136/204] skipped (no command): qa/unconfigured-node-name/build.gradle
18:59:30 [INFO] [lock] [137/204] skipped (no command): qa/os/build.gradle
18:59:30 [INFO] [lock] [138/204] skipped (no command): qa/os/windows-2016/build.gradle
18:59:30 [INFO] [lock] [139/204] skipped (no command): qa/os/debian-9/build.gradle
18:59:30 [INFO] [lock] [140/204] skipped (no command): qa/os/oel-6/build.gradle
18:59:30 [INFO] [lock] [141/204] skipped (no command): qa/os/ubuntu-1804/build.gradle
18:59:30 [INFO] [lock] [142/204] skipped (no command): qa/os/oel-7/build.gradle
18:59:30 [INFO] [lock] [143/204] skipped (no command): qa/os/fedora-28/build.gradle
18:59:30 [INFO] [lock] [144/204] skipped (no command): qa/os/sles-12/build.gradle
18:59:30 [INFO] [lock] [145/204] skipped (no command): qa/os/centos-6/build.gradle
18:59:30 [INFO] [lock] [146/204] skipped (no command): qa/os/debian-8/build.gradle
18:59:30 [INFO] [lock] [147/204] skipped (no command): qa/os/fedora-29/build.gradle
18:59:30 [INFO] [lock] [148/204] skipped (no command): qa/os/windows-2012r2/build.gradle
18:59:30 [INFO] [lock] [149/204] skipped (no command): qa/os/centos-7/build.gradle
18:59:30 [INFO] [lock] [150/204] skipped (no command): qa/os/ubuntu-1604/build.gradle
18:59:30 [INFO] [lock] [151/204] skipped (no command): qa/remote-clusters/build.gradle
18:59:30 [INFO] [lock] [152/204] skipped (no command): qa/smoke-test-ingest-with-all-dependencies/build.gradle
18:59:30 [INFO] [lock] [153/204] skipped (no command): qa/die-with-dignity/build.gradle
18:59:30 [INFO] [lock] [154/204] skipped (no command): qa/multi-cluster-search/build.gradle
18:59:30 [INFO] [lock] [155/204] skipped (no command): distribution/build.gradle
18:59:30 [INFO] [lock] [156/204] skipped (no command): distribution/packages/build.gradle
18:59:30 [INFO] [lock] [157/204] skipped (no command): distribution/packages/no-jdk-deb/build.gradle
18:59:30 [INFO] [lock] [158/204] skipped (no command): distribution/packages/no-jdk-arm64-deb/build.gradle
18:59:30 [INFO] [lock] [159/204] skipped (no command): distribution/packages/arm64-rpm/build.gradle
18:59:30 [INFO] [lock] [160/204] skipped (no command): distribution/packages/rpm/build.gradle
18:59:30 [INFO] [lock] [161/204] skipped (no command): distribution/packages/deb/build.gradle
18:59:30 [INFO] [lock] [162/204] skipped (no command): distribution/packages/arm64-no-jdk-deb/build.gradle
18:59:30 [INFO] [lock] [163/204] skipped (no command): distribution/packages/arm64-no-jdk-rpm/build.gradle
18:59:30 [INFO] [lock] [164/204] skipped (no command): distribution/packages/no-jdk-rpm/build.gradle
18:59:30 [INFO] [lock] [165/204] skipped (no command): distribution/packages/arm64-deb/build.gradle
18:59:30 [INFO] [lock] [166/204] skipped (no command): distribution/packages/no-jdk-arm64-rpm/build.gradle
18:59:30 [INFO] [lock] [167/204] skipped (no command): distribution/tools/fips-demo-installer-cli/build.gradle
18:59:30 [INFO] [lock] [168/204] skipped (no command): distribution/tools/launchers/build.gradle
18:59:30 [INFO] [lock] [169/204] skipped (no command): distribution/tools/plugin-cli/build.gradle
18:59:30 [INFO] [lock] [170/204] skipped (no command): distribution/tools/keystore-cli/build.gradle
18:59:30 [INFO] [lock] [171/204] skipped (no command): distribution/tools/java-version-checker/build.gradle
18:59:30 [INFO] [lock] [172/204] skipped (no command): distribution/bwc/build.gradle
18:59:30 [INFO] [lock] [173/204] skipped (no command): distribution/bwc/maintenance/build.gradle
18:59:30 [INFO] [lock] [174/204] skipped (no command): distribution/bwc/minor/build.gradle
18:59:30 [INFO] [lock] [175/204] skipped (no command): distribution/bwc/bugfix/build.gradle
18:59:30 [INFO] [lock] [176/204] skipped (no command): distribution/bwc/staged/build.gradle
18:59:30 [INFO] [lock] [177/204] skipped (no command): distribution/archives/build.gradle
18:59:30 [INFO] [lock] [178/204] skipped (no command): distribution/archives/no-jdk-darwin-tar/build.gradle
18:59:30 [INFO] [lock] [179/204] skipped (no command): distribution/archives/no-jdk-windows-zip/build.gradle
18:59:30 [INFO] [lock] [180/204] skipped (no command): distribution/archives/no-jdk-linux-riscv64-tar/build.gradle
18:59:30 [INFO] [lock] [181/204] skipped (no command): distribution/archives/no-jdk-darwin-arm64-tar/build.gradle
18:59:30 [INFO] [lock] [182/204] skipped (no command): distribution/archives/integ-test-zip/build.gradle
18:59:30 [INFO] [lock] [183/204] skipped (no command): distribution/archives/linux-s390x-tar/build.gradle
18:59:30 [INFO] [lock] [184/204] skipped (no command): distribution/archives/jre-linux-tar/build.gradle
18:59:30 [INFO] [lock] [185/204] skipped (no command): distribution/archives/linux-arm64-tar/build.gradle
18:59:30 [INFO] [lock] [186/204] skipped (no command): distribution/archives/darwin-tar/build.gradle
18:59:30 [INFO] [lock] [187/204] skipped (no command): distribution/archives/windows-zip/build.gradle
18:59:30 [INFO] [lock] [188/204] skipped (no command): distribution/archives/freebsd-tar/build.gradle
18:59:30 [INFO] [lock] [189/204] skipped (no command): distribution/archives/linux-riscv64-tar/build.gradle
18:59:30 [INFO] [lock] [190/204] skipped (no command): distribution/archives/linux-ppc64le-tar/build.gradle
18:59:30 [INFO] [lock] [191/204] skipped (no command): distribution/archives/no-jdk-freebsd-tar/build.gradle
18:59:30 [INFO] [lock] [192/204] skipped (no command): distribution/archives/no-jdk-linux-ppc64le-tar/build.gradle
18:59:30 [INFO] [lock] [193/204] skipped (no command): distribution/archives/no-jdk-linux-arm64-tar/build.gradle
18:59:30 [INFO] [lock] [194/204] skipped (no command): distribution/archives/no-jdk-linux-tar/build.gradle
18:59:30 [INFO] [lock] [195/204] skipped (no command): distribution/archives/darwin-arm64-tar/build.gradle
18:59:30 [INFO] [lock] [196/204] skipped (no command): distribution/archives/linux-tar/build.gradle
18:59:30 [INFO] [lock] [197/204] skipped (no command): distribution/docker/build.gradle
18:59:30 [INFO] [lock] [198/204] skipped (no command): distribution/docker/docker-riscv64-export/build.gradle
18:59:30 [INFO] [lock] [199/204] skipped (no command): distribution/docker/docker-arm64-export/build.gradle
18:59:30 [INFO] [lock] [200/204] skipped (no command): distribution/docker/docker-s390x-export/build.gradle
18:59:30 [INFO] [lock] [201/204] skipped (no command): distribution/docker/docker-build-context/build.gradle
18:59:30 [INFO] [lock] [202/204] skipped (no command): distribution/docker/docker-ppc64le-export/build.gradle
18:59:30 [INFO] [lock] [203/204] skipped (no command): distribution/docker/docker-arm64-build-context/build.gradle
18:59:30 [INFO] [lock] [204/204] skipped (no command): distribution/docker/docker-export/build.gradle
18:59:30 [INFO] lock generation: ok=0, failed=0, skipped=204
18:59:30 [INFO] STAGE DONE:  ecosystem
18:59:30 [INFO] ============================================================
18:59:30 [INFO] STAGE START: cplus_scan
18:59:30 [INFO] ============================================================
18:59:30 [INFO] cplus_scan skipped (--skip-cplus-scan)
18:59:30 [INFO] STAGE DONE:  cplus_scan
18:59:30 [INFO] ============================================================
18:59:30 [INFO] STAGE START: trivy
18:59:30 [INFO] ============================================================
[INFO] removed rust vendor dirs: 0
[INFO] renamed Cargo.lock.in files: 0
[INFO] hidden template pom.xml files: 0
18:59:30 [INFO] RUN trivy fs . --scanners license --offline-scan --skip-db-update --format cyclonedx --output /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/origsbom.json --timeout 30m  (cwd=/home/kali/Desktop/jobs/opensearch/_repos/opensearch)
[INFO] restored template pom.xml files: 0
18:59:32 [WARNING] [cplus] no cplus sbom files to merge — skipping
18:59:32 [INFO] STAGE DONE:  trivy
18:59:32 [INFO] ============================================================
18:59:32 [INFO] STAGE START: vuln_management
18:59:32 [INFO] ============================================================
18:59:32 [INFO] [normalize] processing: origsbom.json
18:59:32 [INFO] [normalize] origsbom.json: components 0→0, vulnerabilities 0→0, filtered=0
18:59:32 [INFO] [normalize] saved: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/debug/sources/origsbom/origsbom_normalized.json
18:59:32 [INFO] [normalize] using normalized SBOM: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/debug/sources/origsbom/origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/debug/sources/origsbom/origsbom_normalized.json (token=019f28b4-e7cd-740b-8b91-288bcae4802c)
[dt] origsbom uploaded to orig project: 90c437ed-7167-4ef8-aca6-e809468372b8
[dt] ===== enrich origsbom =====
[trivy] scanning: origsbom_normalized.json
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/debug/sources/origsbom/origsbom_normalized.json (token=019f28b4-e7f8-72ed-9bbb-431f170beb2b)
[dt] bom/token poll 1: processing=True
[trivy] done: origsbom_normalized.json components=0 vulnerabilities=0
[dt] bom/token poll 2: processing=False
[dt] BOM processing complete
[dt] findings poll 1: count=0, stable=0
[dt] findings stabilized (empty)
[dt] downloaded: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/.dt-tmp-enrich.json
[dt] enriched: components=0, vulnerabilities=0 (OSV filtered: 0)
[dual] +0 vulnerability record(s) added from trivy (not seen by DT yet)
[dt] starting DT cleanup: orig_vulns=0  candidate_components=0
[dt] SBOM is empty (0 components, 0 vulnerabilities) — skipping DT cleanup rounds
[dt] uploading empty sbom-clean to safe project: 7a914d32-05e2-4335-bbc2-d8ef5eb6dd63
[dt] uploaded: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/sbom-clean.json (token=019f28b5-234b-73eb-a432-7f6b30fb4bf8)
[dt] empty sbom-clean uploaded to safe project: 7a914d32-05e2-4335-bbc2-d8ef5eb6dd63
[OK] report.xlsx           : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/reports/report.xlsx
[OK]   Vulnerabilities rows: 0
[OK]   SafeVersions rows   : 0
[OK] dt_vs_trivy_safe_scan.xlsx : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/debug/dt_vs_trivy_safe_scan.xlsx
[OK]   comparison rows          : 0
[OK] report.xlsx           : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/reports/report.xlsx
[OK] sbom-clean.json : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/sbom-clean.json
[OK] missing versions txt          : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/debug/missing_versions.txt
[OK] failed debug txt              : /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/debug/failed_safe_versions_debug.txt
18:59:47 [WARNING] [vuln] cplus_sbom NOT found at /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/cplus_sbom.json — C/C++ scan may have been skipped or failed
18:59:47 [INFO] STAGE DONE:  vuln_management
18:59:47 [INFO] pipeline summary:
18:59:47 [INFO] stage ecosystem: done
18:59:47 [INFO] stage ecosystem artifact: report -> /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/appsec/ecosystems/lock_summary.json
18:59:47 [INFO] stage cplus_scan: skipped
18:59:47 [WARNING] stage cplus_scan: --skip-cplus-scan set: C/C++ vendored-library scan skipped
18:59:47 [INFO] stage trivy_sbom: done
18:59:47 [INFO] stage trivy_sbom artifact: sbom -> /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/origsbom.json
18:59:47 [INFO] stage vuln_management: done
18:59:47 [INFO] stage vuln_management artifact: report_xlsx -> /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/reports/report.xlsx
18:59:47 [INFO] stage vuln_management artifact: sbom_clean -> /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf/sbom/sbom-clean.json
18:59:47 [INFO] pipeline finished successfully
18:59:47 [INFO] artifacts directory: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf
2026-07-03 18:59:47 | INFO    |   moving results: /home/kali/Desktop/jobs/opensearch/jobs/fe0976484dff4c3392bda06b9523c1cf -> /home/kali/Desktop/results/2026-07-03/opensearch__3.6.0
2026-07-03 18:59:47 | INFO    |   [OK] opensearch / 3.6.0 -> /home/kali/Desktop/results/2026-07-03/opensearch__3.6.0
2026-07-03 18:59:47 | INFO    | run log written: /home/kali/Desktop/results/2026-07-03/run.log
2026-07-03 18:59:47 | INFO    | all 1 scan(s) completed successfully
