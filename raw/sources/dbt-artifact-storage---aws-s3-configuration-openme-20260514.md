---
type: clip
title: "dbt Artifact Storage - AWS S3 Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-s3-guide"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# dbt Artifact Storage - AWS S3 Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-s3-guide

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...Navigationdbt Coredbt Artifact Storage - AWS S3 Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreOverviewS3 ConfigurationGCS ConfigurationAzure ConfigurationHTTP ConfigurationLocal ConfigurationConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pagedbt Artifact Storage: AWS S3 ConfigurationPrerequisites ChecklistStep 1: AWS S3 Setup1.1 Create S3 Bucket1.2 Create IAM Policy for dbt (Write Access)1.3 Create IAM Policy for OpenMetadata (Read Access)1.4 Verify S3 AccessStep 2: Upload Artifacts from dbt2.1 Understanding dbt Artifacts2.2 Complete Airflow DAG Example2.3 Verify DAG DeploymentStep 3: Configure OpenMetadataConfigurationVerificationTroubleshootingNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​dbt Artifact Storage: AWS S3 Configuration

This guide walks you through configuring AWS S3 as the artifact storage layer for dbt Core + OpenMetadata integration. After completing this guide, your dbt artifacts will automatically sync to OpenMetadata for metadata extraction and lineage tracking.

​Prerequisites Checklist

RequirementDetailsHow to VerifyAWS AccountWith permissions to create S3 buckets and IAM policiesaws sts get-caller-identityAWS CLIInstalled and configuredaws --versiondbt ProjectExisting dbt projectdbt debugOrchestrationAirflow or similar schedulerAccess to DAG configurationDatabase ServiceData warehouse already ingestedCheck Settings → Services

​Step 1: AWS S3 Setup

​1.1 Create S3 Bucket

# Set your variables

export AWS_REGION="us-east-1"

export BUCKET_NAME="your-company-dbt-artifacts"

# Create the bucket

aws s3 mb s3://${BUCKET_NAME} --region ${AWS_REGION}

# Verify bucket creation

aws s3 ls | grep ${BUCKET_NAME}

Expected output:

2026-02-10 10:30:00 your-company-dbt-artifacts

​1.2 Create IAM Policy for dbt (Write Access)

Your Airflow/dbt environment needs permission to write to S3.

Save this as dbt-s3-write-policy.json:

{

"Version": "2012-10-17",

"Statement": [

{

"Sid": "AllowDBTArtifactUpload",

"Effect": "Allow",

"Action": [

"s3:PutObject",

"s3:PutObjectAcl"

],

"Resource": "arn:aws:s3:::your-company-dbt-artifacts/dbt-artifacts/*"

},

{

"Sid": "AllowBucketListing",

"Effect": "Allow",

"Action": [

"s3:ListBucket"

],

"Resource": "arn:aws:s3:::your-company-dbt-artifacts"

}

]

}

Create and attach the policy:

# Create the IAM policy

aws iam create-policy \

--policy-name dbt-s3-write-policy \

--policy-document file://dbt-s3-write-policy.json

# Attach to your Airflow/ECS role

export AIRFLOW_ROLE_NAME="your-airflow-task-role"

aws iam attach-role-policy \

--role-name ${AIRFLOW_ROLE_NAME} \

--policy-arn arn:aws:iam::YOUR_ACCOUNT_ID:policy/dbt-s3-write-policy

​1.3 Create IAM Policy for OpenMetadata (Read Access)

OpenMetadata needs permission to read from S3.

Save this as collate-s3-read-policy.json:

{

"Version": "2012-10-17",

"Statement": [

{

"Sid": "AllowOpenMetadataRead",

"Effect": "Allow",

"Action": [

"s3:GetObject",

"s3:ListBucket"

],

"Resource": [

"arn:aws:s3:::your-company-dbt-artifacts",

"arn:aws:s3:::your-company-dbt-artifacts/dbt-artifacts/*"

]

}

]

}

Create the policy:

# Create the policy

aws iam create-policy \

--policy-name collate-s3-read-policy \

--policy-document file://collate-s3-read-policy.json

# Attach to OpenMetadata's role or create access keys for OpenMetadata user

​1.4 Verify S3 Access

# Create test file

echo "test" > /tmp/test.txt

# Upload it

aws s3 cp /tmp/test.txt s3://${BUCKET_NAME}/dbt-artifacts/test.txt

# Verify it exists

aws s3 ls s3://${BUCKET_NAME}/dbt-artifacts/

# Clean up

aws s3 rm s3://${BUCKET_NAME}/dbt-artifacts/test.txt

rm /tmp/test.txt

​Step 2: Upload Artifacts from dbt

​2.1 Understanding dbt Artifacts

OpenMetadata requires these dbt-generated files:

FileGenerated ByRequired?What It Containsmanifest.jsondbt run, dbt compile, dbt buildYESModels, sources, lineage, descriptions, testscatalog.jsondbt docs generateRecommendedColumn names, types, descriptionsrun_results.jsondbt run, dbt test, dbt buildOptionalTest pass/fail results, timing

Generate all artifacts:

dbt run          # Generates manifest.json

dbt test         # Updates run_results.json

dbt docs generate # Generates catalog.json

​2.2 Complete Airflow DAG Example

This is a complete, working DAG for uploading dbt artifacts to S3.

Save as dbt_with_collate.py in your Airflow DAGs folder:

"""

dbt + OpenMetadata Integration DAG (S3 Method)

This DAG:

1. Runs dbt models

2. Runs dbt tests

3. Generates dbt documentation (catalog.json)

4. Uploads all artifacts to S3

No OpenMetadata packages are installed in this Airflow environment.

OpenMetadata pulls the artifacts from S3 independently.

"""

import os

from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator

from airflow.operators.python import PythonOperator

from airflow.utils.task_group import TaskGroup

# =============================================================================

# CONFIGURATION

# =============================================================================

# dbt Configuration

DBT_PROJECT_DIR = os.getenv("DBT_PROJECT_DIR", "/opt/airflow/dbt/my_project")

DBT_PROFILES_DIR = os.getenv("DBT_PROFILES_DIR", "/opt/airflow/dbt")

# S3 Configuration

S3_BUCKET = os.getenv("S3_BUCKET", "your-company-dbt-artifacts")

S3_PREFIX = os.getenv("S3_PREFIX", "dbt-artifacts")

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# =============================================================================

# DAG DEFAULT ARGUMENTS

# =============================================================================

default_args = {

"owner": "data-engineering",

"depends_on_past": False,

"email": ["data-team@yourcompany.com"],

"email_on_failure": True,

"email_on_retry": False,

"retries": 2,

"retry_delay": timedelta(minutes=5),

"execution_timeout": timedelta(hours=2),

}

# =============================================================================

# PYTHON FUNCTIONS

# =============================================================================

def upload_artifacts_to_s3(**context):

"""

Upload dbt artifacts to S3.

Uses boto3 (AWS SDK) which is typically available in Airflow.

If not: pip install boto3

"""

import boto3

from botocore.exceptions import ClientError

s3_client = boto3.client("s3", region_name=AWS_REGION)

target_dir = os.path.join(DBT_PROJECT_DIR, "target")

# Files to upload

artifacts = [

("manifest.json", True),      # Required

("catalog.json", False),      # Optional but recommended

("run_results.json", False),  # Optional

("sources.json", False),      # Optional

]

uploaded = []

failed = []

for filename, required in artifacts:

local_path = os.path.join(target_dir, filename)

s3_key = f"{S3_PREFIX}/{filename}"

if os.path.exists(local_path):

try:

s3_client.upload_file(local_path, S3_BUCKET, s3_key)

uploaded.append(filename)

print(f"✓ Uploaded {filename} to s3://{S3_BUCKET}/{s3_key}")

except ClientError as e:

error_msg = f"✗ Failed to upload {filename}: {e}"

print(error_msg)

if required:

raise Exception(error_msg)

failed.append(filename)

else:

if required:

raise FileNotFoundError(

f"Required artifact not found: {local_path}\n"

f"Make sure 'dbt run' completed successfully."

)

else:

print(f"⊘ Skipping {filename} (not found - optional)")

# Log summary

print(f"\n{'='*50}")

print(f"Upload Summary:")

print(f"  Uploaded: {', '.join(uploaded) or 'None'}")

print(f"  Skipped:  {', '.join(failed) or 'None'}")

print(f"  S3 Location: s3://{S3_BUCKET}/{S3_PREFIX}/")

print(f"{'='*50}")

return {"uploaded": uploaded, "bucket": S3_BUCKET, "prefix": S3_PREFIX}

# =============================================================================

# DAG DEFINITION

# =============================================================================

with DAG(

dag_id="dbt_with_collate",

default_args=default_args,

description="Run dbt models and sync metadata to OpenMetadata via S3",

schedule_interval="0 6 * * *",  # Daily at 6 AM UTC

start_date=datetime(2024, 1, 1),

catchup=False,

max_active_runs=1,

tags=["dbt", "collate", "data-pipeline"],

) as dag:

# Task Group: dbt Execution

with TaskGroup(group_id="dbt_execution") as dbt_tasks:

dbt_run = BashOperator(

task_id="dbt_run",

bash_command=f"""

cd {DBT_PROJECT_DIR} && \

dbt run --profiles-dir {DBT_PROFILES_DIR}

""",

)

dbt_test = BashOperator(

task_id="dbt_test",

bash_command=f"""

cd {DBT_PROJECT_DIR} && \

dbt test --profiles-dir {DBT_PROFILES_DIR}

""",

trigger_rule="all_done",  # Run even if dbt_run fails

)

dbt_docs = BashOperator(

task_id="dbt_docs_generate",

bash_command=f"""

cd {DBT_PROJECT_DIR} && \

dbt docs generate --profiles-dir {DBT_PROFILES_DIR}

""",

)

dbt_run >> dbt_test >> dbt_docs

# Upload to S3

upload_to_s3 = PythonOperator(

task_id="upload_artifacts_to_s3",

python_callable=upload_artifacts_to_s3,

provide_context=True,

)

# DAG Dependencies

dbt_tasks >> upload_to_s3

​2.3 Verify DAG Deployment

# Check DAG is visible in Airflow

airflow dags list | grep dbt

# Trigger manual run

airflow dags trigger dbt_with_collate

# Check S3 after DAG completes

aws s3 ls s3://your-company-dbt-artifacts/dbt-artifacts/

Expected S3 output:

2026-02-10 10:30:00   5242880 manifest.json

2026-02-10 10:30:01   1048576 catalog.json

2026-02-10 10:30:01    102400 run_results.json

​Step 3: Configure OpenMetadata

​Configuration

Go to Settings → Services → Database Services

Click on your database service (e.g., “production-snowflake”)

Go to the Ingestion tab

Click Add Ingestion

Select dbt from the dropdown

Configure dbt Source (S3):

FieldValueNotesdbt Configuration SourceS3Select from dropdownS3 Bucket Nameyour-company-dbt-artifactsYour bucket nameS3 Object Prefixdbt-artifactsFolder path (no leading /)AWS Regionus-east-1Your region

AWS Credentials (choose one):

Option A: Using Access Keys

FieldValueAWS Access Key IDAKIA...AWS Secret Access KeywJalrXUtn...

Option B: Using IAM Role (if OpenMetadata runs on AWS)

FieldValueAWS Access Key IDLeave emptyAWS Secret Access KeyLeave empty

Configure dbt Options:

FieldRecommended ValueUpdate DescriptionsEnabledUpdate OwnersEnabledInclude TagsEnabledClassification NamedbtTags

Test & Deploy:

Click Test Connection

If successful, click Deploy

Click Run to trigger immediately

​Verification

After running the full pipeline, verify:

CheckHow to VerifyExpected ResultS3 artifacts existaws s3 ls s3://bucket/dbt-artifacts/manifest.json, catalog.json listedIngestion completedOpenMetadata UI → Service → Ingestion tabGreen status, no errorsLineage appearsClick on a dbt model → Lineage tabUpstream/downstream connectionsDescriptions syncedClick on a table → Schema tabColumn descriptions visibleTags appearClick on a table → Tags sectiondbt tags shown

​Troubleshooting

IssueSymptomCauseSolutionAccess Denied”403 Forbidden” errorIAM permissions insufficientVerify IAM policy has s3:GetObject and s3:ListBucketManifest not found”dbtManifestFilePath not found”S3 path incorrectCheck dbtObjectPrefix matches your S3 structureNo lineageTables exist but no lineageDatabase metadata not ingested firstRun database metadata ingestion before dbt ingestionStale dataOld lineage/descriptionsOld artifacts in S3Verify dbt DAG uploads fresh artifactsMissing columnsNo column descriptionsMissing catalog.jsonEnsure dbt docs generate runs and uploads

​Next Steps

Configure dbt Workflow

Auto Ingest dbt Core

dbt Troubleshooting

See other storage options: GCS | Azure | HTTP | Local | dbt CloudWas this page helpful?YesNoSuggest editsRaise issuedbt Artifact Configuration Guide | OpenMetadataPreviousdbt Artifact Storage - Google Cloud Storage Configuration | OpenMetadataNext⌘I
