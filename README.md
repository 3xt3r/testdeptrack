sudo docker logs --tail=200 dependency-track-apiserver-1
2026-06-18 12:38:27,246 INFO [VulnAnalysisWorkflow] Vulnerability analysis completed [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-65fc-71bb-b939-1643677cc651, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:27,491 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2023]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:27,535 INFO [CelPolicyEngine] No applicable policies found [projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:27,802 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2022]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:27,947 INFO [AnalyzeProjectWorkflow] Project analysis completed [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-6452-7590-be1e-40c5fab8dd10, workflowRunId=019edabd-659c-75b1-b956-06e5b329e37b, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:28,005 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2021]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:28,414 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2020]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:28,724 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2019]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:29,131 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2018]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:29,443 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2017]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:29,793 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2016]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:30,009 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2015]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:30,365 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2014]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:30,769 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2013]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:30,974 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2012]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:31,284 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2011]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:31,691 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2010]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:31,896 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2009]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:32,209 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2008]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:32,612 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2007]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:32,925 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2006]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:33,329 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2005]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:33,534 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2004]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:33,738 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2003]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:33,944 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2002]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:38:34,257 INFO [NvdVulnDataSource] Downloading feed ModifiedDataFeed[] from https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-modified.json.gz [vulnDataSourceName=nvd]
2026-06-18 12:38:34,559 WARN [ActivityTaskWorker] Activity failed; Next retry due at 2026-06-18T12:39:19.080021847Z (attempt 6/6) [activityName=mirror-vuln-data-source, workflowRunId=019edaa4-3b3d-72f2-aa41-aaef5561830a, activityTaskAttempt=5]
java.lang.IllegalStateException: Unexpected response code: 404
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.downloadFeedFile(NvdVulnDataSource.java:368)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:203)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.hasNext(NvdVulnDataSource.java:109)
	at org.dependencytrack.vulndatasource.MirrorVulnDataSourceActivity.execute(MirrorVulnDataSourceActivity.java:119)
	at org.dependencytrack.vulndatasource.MirrorVulnDataSourceActivity.execute(MirrorVulnDataSourceActivity.java:65)
	at org.dependencytrack.dex.engine.ActivityTaskWorker.lambda$process$0(ActivityTaskWorker.java:117)
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
	at java.base/java.util.concurrent.ThreadPerTaskExecutor$ThreadBoundFuture.run(Unknown Source)
	at java.base/java.lang.VirtualThread.run(Unknown Source)
2026-06-18 12:38:40,781 INFO [BomResource] BOM upload accepted [principal=odt_wzWt2FAg********************************, requestId=1a090427-df1d-45db-9571-c0286798479e, requestMethod=PUT, bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, requestUri=/v1/bom, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=null]
2026-06-18 12:38:40,791 INFO [ImportBomWorkflow] Starting BOM import [bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-9f87-7c3d-8217-ac151a6a4935, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:40,853 INFO [BomResource] BOM upload accepted [principal=odt_wzWt2FAg********************************, requestId=fb8c11eb-60ea-4fbc-a119-50c2b7b7706e, requestMethod=PUT, bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, requestUri=/v1/bom, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=null]
2026-06-18 12:38:40,903 INFO [ImportBomActivity] Consumed 4 components (4 before de-duplication), 0 services (0 before de-duplication), and 0 dependency graph entries [bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:40,907 INFO [ImportBomActivity] Processing 4 components [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:40,917 INFO [ImportBomActivity] Processing 0 services [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:40,919 INFO [ImportBomActivity] Processing 0 dependency graph entries [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:40,924 INFO [ImportBomActivity] BOM processed successfully in 00:00:00.027 [bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:40,990 INFO [AnalyzeProjectWorkflow] Starting project analysis [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-9f84-77a7-8413-e258a325b37d, workflowRunId=019edabd-a01e-7d62-ad5b-9f3bb9dc616d, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:41,189 INFO [VulnAnalysisWorkflow] Starting vulnerability analysis [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-a05e-706b-bd69-d439604faa89, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:41,292 INFO [ResolvePackageMetadataWorkflow] No more packages due for metadata resolution [workflowInstanceId=resolve-package-metadata, workflowRunId=019edabd-a023-7c67-82da-b43a14a3bb46, workflowName=resolve-package-metadata]
2026-06-18 12:38:41,292 INFO [ImportBomWorkflow] BOM import completed [bomUploadToken=019edabd-9f84-77a7-8413-e258a325b37d, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-9f87-7c3d-8217-ac151a6a4935, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:41,490 INFO [ImportBomWorkflow] Starting BOM import [bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-9fd1-77a0-a738-0d0d82a65775, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:41,676 INFO [ImportBomActivity] Consumed 4 components (4 before de-duplication), 0 services (0 before de-duplication), and 0 dependency graph entries [bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:41,691 INFO [ImportBomActivity] Processing 4 components [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:41,703 INFO [ImportBomActivity] Processing 0 services [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:41,705 INFO [ImportBomActivity] Processing 0 dependency graph entries [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:41,710 INFO [ImportBomActivity] BOM processed successfully in 00:00:00.048 [bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:42,098 INFO [ResolvePackageMetadataWorkflow] No more packages due for metadata resolution [workflowInstanceId=resolve-package-metadata, workflowRunId=019edabd-a336-74ce-96a9-a76930310df6, workflowName=resolve-package-metadata]
2026-06-18 12:38:42,194 INFO [ImportBomWorkflow] BOM import completed [bomUploadToken=019edabd-9fcf-7182-a12c-4d6c05f18182, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-9fd1-77a0-a738-0d0d82a65775, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:42,394 INFO [VulnAnalysisWorkflow] Vulnerability analysis completed [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-a05e-706b-bd69-d439604faa89, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:42,668 INFO [CelPolicyEngine] No applicable policies found [projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:43,293 INFO [AnalyzeProjectWorkflow] Project analysis completed [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-9f84-77a7-8413-e258a325b37d, workflowRunId=019edabd-a01e-7d62-ad5b-9f3bb9dc616d, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:43,492 INFO [AnalyzeProjectWorkflow] Starting project analysis [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-9fcf-7182-a12c-4d6c05f18182, workflowRunId=019edabd-a330-7a76-b902-096c670f7c18, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:43,693 INFO [VulnAnalysisWorkflow] Starting vulnerability analysis [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-aa24-75f6-b4f2-374c8e6126c9, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:44,995 INFO [VulnAnalysisWorkflow] Vulnerability analysis completed [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-aa24-75f6-b4f2-374c8e6126c9, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:45,380 INFO [CelPolicyEngine] No applicable policies found [projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:45,996 INFO [AnalyzeProjectWorkflow] Project analysis completed [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-9fcf-7182-a12c-4d6c05f18182, workflowRunId=019edabd-a330-7a76-b902-096c670f7c18, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:55,991 INFO [BomResource] BOM upload accepted [principal=odt_wzWt2FAg********************************, requestId=a359002a-4337-45dc-86ad-9f66ba93cfde, requestMethod=PUT, bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, requestUri=/v1/bom, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=null]
2026-06-18 12:38:56,004 INFO [ImportBomWorkflow] Starting BOM import [bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-daf0-7153-b7a1-db9de0180e75, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:56,094 INFO [ImportBomActivity] Consumed 4 components (4 before de-duplication), 0 services (0 before de-duplication), and 0 dependency graph entries [bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:56,099 INFO [ImportBomActivity] Processing 4 components [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:56,106 INFO [ImportBomActivity] Processing 0 services [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:56,107 INFO [ImportBomActivity] Processing 0 dependency graph entries [bomSerialNumber=null, bomFormat=CycloneDX, bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, projectName=newtonsoft-json__13.0.4 [safe], bomSpecVersion=1.6, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=, bomVersion=1]
2026-06-18 12:38:56,112 INFO [ImportBomActivity] BOM processed successfully in 00:00:00.029 [bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, projectName=newtonsoft-json__13.0.4 [safe], projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:56,201 INFO [AnalyzeProjectWorkflow] Starting project analysis [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-daed-7cdd-a370-78a6f4cdb092, workflowRunId=019edabd-db72-7f43-8127-e9fb8de52089, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:56,302 INFO [VulnAnalysisWorkflow] Starting vulnerability analysis [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-dbc9-7f76-9bd8-6785436c3c87, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:56,503 INFO [ImportBomWorkflow] BOM import completed [bomUploadToken=019edabd-daed-7cdd-a370-78a6f4cdb092, workflowName=import-bom, projectName=newtonsoft-json__13.0.4 [safe], workflowInstanceId=null, workflowRunId=019edabd-daf0-7153-b7a1-db9de0180e75, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3, projectVersion=]
2026-06-18 12:38:56,603 INFO [ResolvePackageMetadataWorkflow] No more packages due for metadata resolution [workflowInstanceId=resolve-package-metadata, workflowRunId=019edabd-db76-7c95-96fc-19d0a3f7f14b, workflowName=resolve-package-metadata]
2026-06-18 12:38:57,306 INFO [VulnAnalysisWorkflow] Vulnerability analysis completed [workflowName=vuln-analysis, workflowInstanceId=null, workflowRunId=019edabd-dbc9-7f76-9bd8-6785436c3c87, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:57,500 INFO [CelPolicyEngine] No applicable policies found [projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:38:57,807 INFO [AnalyzeProjectWorkflow] Project analysis completed [workflowName=analyze-project, workflowInstanceId=analyze-project:bom-upload:019edabd-daed-7cdd-a370-78a6f4cdb092, workflowRunId=019edabd-db72-7f43-8127-e9fb8de52089, projectUuid=95c2a6df-c375-4a87-abe0-c8962a5049a3]
2026-06-18 12:39:19,149 INFO [MirrorVulnDataSourceActivity] Starting mirror [vulnDataSourceName=nvd]
2026-06-18 12:39:19,613 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2026]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:19,787 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2025]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:19,957 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2024]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,131 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2023]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,301 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2022]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,474 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2021]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,652 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2020]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,822 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2019]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:20,996 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2018]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:21,166 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2017]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:21,339 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2016]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:21,506 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2015]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:21,678 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2014]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:21,853 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2013]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,088 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2012]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,260 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2011]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,433 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2010]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,609 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2009]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,780 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2008]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:22,953 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2007]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,126 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2006]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,300 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2005]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,472 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2004]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,640 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2003]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,810 INFO [NvdVulnDataSource] Skipping YearDataFeed[year=2002]: Digest unchanged [vulnDataSourceName=nvd]
2026-06-18 12:39:23,995 INFO [NvdVulnDataSource] Downloading feed ModifiedDataFeed[] from https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-modified.json.gz [vulnDataSourceName=nvd]
2026-06-18 12:39:24,169 WARN [ActivityTaskWorker] Activity failed terminally after 6 attempt(s) [activityName=mirror-vuln-data-source, workflowRunId=019edaa4-3b3d-72f2-aa41-aaef5561830a, activityTaskAttempt=6]
java.lang.IllegalStateException: Unexpected response code: 404
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.downloadFeedFile(NvdVulnDataSource.java:368)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:203)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.openNextFeed(NvdVulnDataSource.java:190)
	at org.dependencytrack.vulndatasource.nvd.NvdVulnDataSource.hasNext(NvdVulnDataSource.java:109)
	at org.dependencytrack.vulndatasource.MirrorVulnDataSourceActivity.execute(MirrorVulnDataSourceActivity.java:119)
	at org.dependencytrack.vulndatasource.MirrorVulnDataSourceActivity.execute(MirrorVulnDataSourceActivity.java:65)
	at org.dependencytrack.dex.engine.ActivityTaskWorker.lambda$process$0(ActivityTaskWorker.java:117)
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
	at java.base/java.util.concurrent.ThreadPerTaskExecutor$ThreadBoundFuture.run(Unknown Source)
	at java.base/java.lang.VirtualThread.run(Unknown Source)
2026-07-03 09:25:18,475 INFO [Application] Starting Dependency-Track 5.0.0 (built 2026-06-07T15:28:31Z)
2026-07-03 09:25:18,581 INFO [DataSourceRegistry] Creating data source default
Exception in thread "main" com.zaxxer.hikari.pool.HikariPool$PoolInitializationException: Failed to initialize pool: The connection attempt failed.
	at com.zaxxer.hikari.pool.HikariPool.throwPoolInitializationException(HikariPool.java:610)
	at com.zaxxer.hikari.pool.HikariPool.checkFailFast(HikariPool.java:597)
	at com.zaxxer.hikari.pool.HikariPool.<init>(HikariPool.java:97)
	at com.zaxxer.hikari.HikariDataSource.<init>(HikariDataSource.java:80)
	at org.dependencytrack.common.datasource.DataSourceFactory.createDataSource(DataSourceFactory.java:56)
	at org.dependencytrack.common.datasource.DataSourceRegistry.lambda$get$0(DataSourceRegistry.java:66)
	at java.base/java.util.concurrent.ConcurrentHashMap.computeIfAbsent(Unknown Source)
	at org.dependencytrack.common.datasource.DataSourceRegistry.get(DataSourceRegistry.java:64)
	at org.dependencytrack.Application.main(Application.java:166)
Caused by: org.postgresql.util.PSQLException: The connection attempt failed.
	at org.postgresql.core.v3.ConnectionFactoryImpl.openConnectionImpl(ConnectionFactoryImpl.java:437)
	at org.postgresql.core.ConnectionFactory.openConnection(ConnectionFactory.java:52)
	at org.postgresql.jdbc.PgConnection.<init>(PgConnection.java:290)
	at org.postgresql.Driver.makeConnection(Driver.java:448)
	at org.postgresql.Driver.connect(Driver.java:298)
	at com.zaxxer.hikari.util.DriverDataSource.getConnection(DriverDataSource.java:144)
	at com.zaxxer.hikari.pool.PoolBase.newConnection(PoolBase.java:373)
	at com.zaxxer.hikari.pool.PoolBase.newPoolEntry(PoolBase.java:210)
	at com.zaxxer.hikari.pool.HikariPool.createPoolEntry(HikariPool.java:488)
	at com.zaxxer.hikari.pool.HikariPool.checkFailFast(HikariPool.java:576)
	... 7 more
Caused by: java.net.UnknownHostException: postgres
	at java.base/sun.nio.ch.NioSocketImpl.connect(Unknown Source)
	at java.base/java.net.SocksSocketImpl.connect(Unknown Source)
	at java.base/java.net.Socket.connect(Unknown Source)
	at org.postgresql.core.PGStream.createSocket(PGStream.java:271)
	at org.postgresql.core.PGStream.<init>(PGStream.java:132)
	at org.postgresql.core.v3.ConnectionFactoryImpl.tryConnect(ConnectionFactoryImpl.java:219)
	at org.postgresql.core.v3.ConnectionFactoryImpl.openConnectionImpl(ConnectionFactoryImpl.java:365)
	... 16 more
kali@kali-RedmiBook-16:~/Desktop/dependency-track-local$ 
