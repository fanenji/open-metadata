---
type: clip
title: "dbt Artifact Storage - Local Filesystem Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-local-guide"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# dbt Artifact Storage - Local Filesystem Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-local-guide

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...Navigationdbt Coredbt Artifact Storage - Local Filesystem Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreOverviewS3 ConfigurationGCS ConfigurationAzure ConfigurationHTTP ConfigurationLocal ConfigurationConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pagedbt Artifact Storage: Local/Shared FilesystemPrerequisites ChecklistConfiguration OptionsOption A: Same Machine (Development)Option B: Docker Compose with Shared VolumeOption C: Kubernetes with PersistentVolumeClaimOption D: NFS Mounted Shared StorageStep 2: Configure OpenMetadataConfigurationVerificationBest Practices1. Use Absolute Paths2. Ensure Read Permissions3. Automate Artifact Copying4. Use ReadWriteMany for KubernetesTroubleshootingNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​dbt Artifact Storage: Local/Shared Filesystem

This guide walks you through configuring a local or shared filesystem as the artifact storage layer for dbt Core + OpenMetadata integration. Ideal for development, single-server deployments, or Kubernetes with shared volumes.

Not recommended for production distributed systems. dbt and OpenMetadata must access the same filesystem. Use cloud storage (S3/GCS/Azure) for production multi-server deployments.

​Prerequisites Checklist

RequirementDetailsHow to VerifyShared Filesystemdbt on same machine or shared volumeCan access same directorydbt ProjectExisting dbt projectdbt debugDatabase ServiceData warehouse already ingestedCheck Settings → Services

​Configuration Options

​Option A: Same Machine (Development)

If dbt and OpenMetadata run on the same machine:

1. Run dbt and generate artifacts:

cd /path/to/dbt/project

dbt run

dbt test

dbt docs generate

2. Note the target directory path:

# Artifacts are in target/ directory

ls -la target/

# Output: manifest.json, catalog.json, run_results.json

3. Configure OpenMetadata with absolute path:

Manifest: /path/to/dbt/project/target/manifest.json

Catalog: /path/to/dbt/project/target/catalog.json

Run Results: /path/to/dbt/project/target/run_results.json

​Option B: Docker Compose with Shared Volume

Perfect for local development stacks.

docker-compose.yml:

version: '3.8'

services:

# dbt service (runs dbt commands)

dbt:

image: ghcr.io/dbt-labs/dbt-postgres:latest

volumes:

- ./dbt:/usr/app/dbt          # dbt project

- dbt-artifacts:/dbt-artifacts # Shared volume for artifacts

command: >

bash -c "

dbt run --project-dir /usr/app/dbt &&

dbt test --project-dir /usr/app/dbt &&

dbt docs generate --project-dir /usr/app/dbt &&

cp /usr/app/dbt/target/*.json /dbt-artifacts/

"

environment:

DBT_PROFILES_DIR: /usr/app/dbt

# OpenMetadata service

collate:

image: openmetadata/server:latest

ports:

- "8585:8585"

volumes:

- dbt-artifacts:/dbt-artifacts  # Same shared volume

environment:

# OpenMetadata will read from /dbt-artifacts/

DBT_ARTIFACTS_PATH: /dbt-artifacts

volumes:

dbt-artifacts:  # Named volume shared between services

Configure OpenMetadata:

Manifest: /dbt-artifacts/manifest.json

Catalog: /dbt-artifacts/catalog.json

Run Results: /dbt-artifacts/run_results.json

​Option C: Kubernetes with PersistentVolumeClaim

For Kubernetes deployments where dbt and OpenMetadata run in the same cluster.

1. Create PersistentVolumeClaim:

# dbt-artifacts-pvc.yaml

apiVersion: v1

kind: PersistentVolumeClaim

metadata:

name: dbt-artifacts

namespace: data-platform

spec:

accessModes:

- ReadWriteMany  # Critical: Allows multiple pods to read

storageClassName: nfs-client  # Use NFS, EFS, or similar

resources:

requests:

storage: 1Gi

kubectl apply -f dbt-artifacts-pvc.yaml

2. dbt CronJob (uploads artifacts):

# dbt-cronjob.yaml

apiVersion: batch/v1

kind: CronJob

metadata:

name: dbt-runner

namespace: data-platform

spec:

schedule: "0 6 * * *"  # Daily at 6 AM

jobTemplate:

spec:

template:

spec:

containers:

- name: dbt

image: ghcr.io/dbt-labs/dbt-postgres:latest

command:

- /bin/bash

- -c

- |

dbt run &&

dbt test &&

dbt docs generate &&

cp target/*.json /dbt-artifacts/

volumeMounts:

- name: dbt-project

mountPath: /usr/app/dbt

- name: dbt-artifacts

mountPath: /dbt-artifacts

volumes:

- name: dbt-project

configMap:

name: dbt-project-config

- name: dbt-artifacts

persistentVolumeClaim:

claimName: dbt-artifacts

restartPolicy: OnFailure

3. Mount volume in OpenMetadata deployment:

# collate-deployment.yaml

apiVersion: apps/v1

kind: Deployment

metadata:

name: collate

namespace: data-platform

spec:

replicas: 1

selector:

matchLabels:

app: collate

template:

metadata:

labels:

app: collate

spec:

containers:

- name: collate

image: openmetadata/server:latest

ports:

- containerPort: 8585

volumeMounts:

- name: dbt-artifacts

mountPath: /dbt-artifacts

readOnly: true  # OpenMetadata only reads

volumes:

- name: dbt-artifacts

persistentVolumeClaim:

claimName: dbt-artifacts

Configure OpenMetadata:

Manifest: /dbt-artifacts/manifest.json

Catalog: /dbt-artifacts/catalog.json

Run Results: /dbt-artifacts/run_results.json

​Option D: NFS Mounted Shared Storage

For VMs or bare-metal servers with shared NFS storage.

1. Set up NFS share:

On NFS server:

# Install NFS server

sudo apt install -y nfs-kernel-server

# Create shared directory

sudo mkdir -p /export/dbt-artifacts

sudo chmod 777 /export/dbt-artifacts

# Configure exports

echo "/export/dbt-artifacts *(rw,sync,no_subtree_check,no_root_squash)" | \

sudo tee -a /etc/exports

# Restart NFS

sudo systemctl restart nfs-kernel-server

2. Mount on client machines:

On dbt server:

sudo apt install -y nfs-common

sudo mkdir -p /mnt/dbt-artifacts

sudo mount nfs-server:/export/dbt-artifacts /mnt/dbt-artifacts

# Make permanent

echo "nfs-server:/export/dbt-artifacts /mnt/dbt-artifacts nfs defaults 0 0" | \

sudo tee -a /etc/fstab

On OpenMetadata server:

sudo apt install -y nfs-common

sudo mkdir -p /mnt/dbt-artifacts

sudo mount nfs-server:/export/dbt-artifacts /mnt/dbt-artifacts

# Make permanent

echo "nfs-server:/export/dbt-artifacts /mnt/dbt-artifacts nfs defaults 0 0" | \

sudo tee -a /etc/fstab

3. Configure dbt to write to NFS:

cd /path/to/dbt/project

dbt run && dbt test && dbt docs generate

cp target/*.json /mnt/dbt-artifacts/

Configure OpenMetadata:

Manifest: /mnt/dbt-artifacts/manifest.json

Catalog: /mnt/dbt-artifacts/catalog.json

Run Results: /mnt/dbt-artifacts/run_results.json

​Step 2: Configure OpenMetadata

​Configuration

Go to Settings → Services → Database Services

Click on your database service

Go to the Ingestion tab

Click Add Ingestion

Select dbt from the dropdown

Configure dbt Source (Local):

FieldValueNotesdbt Configuration SourceLocalSelect from dropdowndbt Catalog File Path/dbt-artifacts/catalog.jsonAbsolute path accessible by OpenMetadatadbt Manifest File Path/dbt-artifacts/manifest.jsonAbsolute path accessible by OpenMetadatadbt Run Results File Path/dbt-artifacts/run_results.jsonOptional - absolute path

Configure dbt Options:

FieldRecommended ValueUpdate DescriptionsEnabledUpdate OwnersEnabledInclude TagsEnabledClassification NamedbtTags

​Verification

# Verify artifacts exist and are readable

ls -la /dbt-artifacts/

cat /dbt-artifacts/manifest.json | jq '.metadata.dbt_version'

# Check from OpenMetadata's perspective (if in Docker)

docker exec collate-container ls -la /dbt-artifacts/

docker exec collate-container cat /dbt-artifacts/manifest.json | jq '.'

​Best Practices

​1. Use Absolute Paths

Always use absolute paths, not relative:

✓ /dbt-artifacts/manifest.json

✗ ../dbt/target/manifest.json

​2. Ensure Read Permissions

# Set correct permissions

chmod 644 /dbt-artifacts/*.json

chown collate-user:collate-group /dbt-artifacts/*.json

​3. Automate Artifact Copying

# Add to dbt wrapper script

dbt run && dbt test && dbt docs generate

cp target/*.json /dbt-artifacts/

​4. Use ReadWriteMany for Kubernetes

For Kubernetes PVC, ensure accessMode: ReadWriteMany:

Works: NFS, EFS, Azure Files, GlusterFS

Doesn’t work: EBS (ReadWriteOnce only)

​Troubleshooting

IssueSymptomSolutionFile not found”No such file or directory”Verify absolute path is correct and accessible from OpenMetadataPermission denied”Permission denied”Run chmod 644 /dbt-artifacts/*.jsonStale dataOld metadata showingEnsure dbt writes artifacts before OpenMetadata readsMount issue”Transport endpoint not connected”Check NFS mount: `mountgrep dbt-artifacts`Volume not sharedWorks for dbt, not OpenMetadataVerify both containers/pods mount the same volume

No built-in versioning or backup

File locking issues possible with concurrent access

Requires shared filesystem infrastructure

For production, consider:

S3 Storage for AWS

GCS Storage for GCP

Azure Blob Storage for Azure

​Next Steps

Configure dbt Workflow

dbt Troubleshooting

See other storage options: S3 | GCS | Azure | HTTP | dbt CloudWas this page helpful?YesNoSuggest editsRaise issuedbt Artifact Storage - HTTP Server Configuration | OpenMetadataPreviousConfigure dbt workflowNext⌘I
