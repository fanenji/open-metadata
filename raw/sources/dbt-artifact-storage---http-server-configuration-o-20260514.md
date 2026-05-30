---
type: clip
title: "dbt Artifact Storage - HTTP Server Configuration | OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-http-guide"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# dbt Artifact Storage - HTTP Server Configuration | OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/storage-http-guide

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...Navigationdbt Coredbt Artifact Storage - HTTP Server Configuration | OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsConnectorsConnectorsConnectorAPIDatabaseOverviewADLS DatalakeAthenaAzureSQLBigQueryBigTableBurstIQCassandraClickhouseCockroachCouchbaseDatabricksDB2dbtOverviewdbt Cloud APIdbt CoreOverviewS3 ConfigurationGCS ConfigurationAzure ConfigurationHTTP ConfigurationLocal ConfigurationConfigure dbt workflowRun ExternallyAuto Ingest dbt Core ArtifactsIngest dbt OwnerIngest dbt DescriptionsIngest dbt TagsIngest dbt TiersIngest dbt GlossaryIngest dbt DomainIngest dbt Custom PropertiesIngest dbt LineageSetup Multiple dbt Projectsdbt troubleshootingDeltaLakeDomo DatabaseDorisDruidDynamoDBEpicExasolGCS DatalakeGlueGreenplumHiveImpalaMariaDBMongoDBMSSQLMySQLOraclePinotDBPostgreSQLPrestoRedshiftS3 DatalakeSalesforceSAP ERPSAP HANASASSingleStoreSnowflakeSQLiteTeradataTimescaleDBTrinoUnity CatalogVerticaGrafanaHexDashboardMessagingPipelineML ModelStorageSearchMetadataDriveCustom ConnectorsConnector IngestionIngestionOn this pagedbt Artifact Storage: HTTP Server ConfigurationPrerequisites ChecklistHTTP Server OptionsOption 1: S3 + CloudFront (Recommended)Option 2: Nginx Static File ServerOption 3: Apache Static File ServerStep 2: Upload Artifacts from dbt2.1 Manual Upload with rsync2.2 Automated Upload in Airflow DAG2.3 Upload with curl (Simple HTTP POST)Step 3: Configure OpenMetadataConfigurationVerificationSecurity ConsiderationsEnable HTTPSAdd Basic AuthenticationIP WhitelistingTroubleshootingNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​dbt Artifact Storage: HTTP Server Configuration

This guide walks you through configuring an HTTP/HTTPS server as the artifact storage layer for dbt Core + OpenMetadata integration. Ideal for multi-cloud or on-premises deployments.

​Prerequisites Checklist

RequirementDetailsHow to VerifyWeb ServerNginx, Apache, or cloud CDNcurl http://your-server/dbt ProjectExisting dbt projectdbt debugServer AccessSSH or deployment accessCan upload files to serverDatabase ServiceData warehouse already ingestedCheck Settings → Services

​HTTP Server Options

​Option 1: S3 + CloudFront (Recommended)

Combine S3 storage with CloudFront CDN for HTTPS and global access.

Setup:

Follow S3 guide to create bucket and upload artifacts

Create CloudFront distribution:

# Create CloudFront distribution (AWS Console or CLI)

aws cloudfront create-distribution \

--origin-domain-name your-bucket.s3.amazonaws.com \

--default-root-object index.html

Configure OpenMetadata with CloudFront URL:

URL: https://d123abc.cloudfront.net/dbt/

​Option 2: Nginx Static File Server

Install Nginx:

# Ubuntu/Debian

sudo apt update && sudo apt install -y nginx

# CentOS/RHEL

sudo yum install -y nginx

# macOS

brew install nginx

Configure Nginx:

Create /etc/nginx/sites-available/dbt-artifacts:

server {

listen 80;

server_name artifacts.yourcompany.com;

# Root directory for dbt artifacts

root /var/www/dbt-artifacts;

# Enable directory listing (optional)

autoindex on;

# CORS headers for OpenMetadata access

add_header 'Access-Control-Allow-Origin' '*';

add_header 'Access-Control-Allow-Methods' 'GET, OPTIONS';

location /dbt/ {

alias /var/www/dbt-artifacts/;

try_files $uri $uri/ =404;

}

# Optional: Basic authentication

# auth_basic "Restricted Access";

# auth_basic_user_file /etc/nginx/.htpasswd;

}

Enable the site:

sudo ln -s /etc/nginx/sites-available/dbt-artifacts /etc/nginx/sites-enabled/

sudo mkdir -p /var/www/dbt-artifacts

sudo chmod 755 /var/www/dbt-artifacts

sudo nginx -t

sudo systemctl reload nginx

​Option 3: Apache Static File Server

Install Apache:

# Ubuntu/Debian

sudo apt install -y apache2

# CentOS/RHEL

sudo yum install -y httpd

Configure Apache:

Create /etc/apache2/sites-available/dbt-artifacts.conf:

<VirtualHost *:80>

ServerName artifacts.yourcompany.com

DocumentRoot /var/www/dbt-artifacts

<Directory /var/www/dbt-artifacts>

Options Indexes FollowSymLinks

AllowOverride None

Require all granted

# Enable CORS

Header set Access-Control-Allow-Origin "*"

</Directory>

ErrorLog ${APACHE_LOG_DIR}/dbt-artifacts-error.log

CustomLog ${APACHE_LOG_DIR}/dbt-artifacts-access.log combined

</VirtualHost>

Enable the site:

sudo a2ensite dbt-artifacts

sudo mkdir -p /var/www/dbt-artifacts

sudo chmod 755 /var/www/dbt-artifacts

sudo systemctl reload apache2

​Step 2: Upload Artifacts from dbt

​2.1 Manual Upload with rsync

# Upload artifacts to server

rsync -avz target/*.json user@server:/var/www/dbt-artifacts/

# Or via SCP

scp target/*.json user@server:/var/www/dbt-artifacts/

​2.2 Automated Upload in Airflow DAG

"""

dbt + HTTP Upload DAG

"""

from airflow import DAG

from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {

"owner": "data-engineering",

"retries": 2,

"retry_delay": timedelta(minutes=5),

}

with DAG(

dag_id="dbt_with_http",

default_args=default_args,

schedule_interval="0 6 * * *",

start_date=datetime(2024, 1, 1),

catchup=False,

) as dag:

dbt_run = BashOperator(

task_id="dbt_run",

bash_command="cd /opt/airflow/dbt && dbt run && dbt test && dbt docs generate"

)

upload_artifacts = BashOperator(

task_id="upload_to_http_server",

bash_command="""

rsync -avz /opt/airflow/dbt/target/*.json \

user@artifacts.yourcompany.com:/var/www/dbt-artifacts/

"""

)

dbt_run >> upload_artifacts

​2.3 Upload with curl (Simple HTTP POST)

If your server accepts POST requests:

cd target

curl -X POST -F "file=@manifest.json" http://artifacts.yourcompany.com/upload

curl -X POST -F "file=@catalog.json" http://artifacts.yourcompany.com/upload

curl -X POST -F "file=@run_results.json" http://artifacts.yourcompany.com/upload

​Step 3: Configure OpenMetadata

​Configuration

Go to Settings → Services → Database Services

Click on your database service

Go to the Ingestion tab

Click Add Ingestion

Select dbt from the dropdown

Configure dbt Source (HTTP):

FieldValueNotesdbt Configuration SourceHTTPSelect from dropdowndbt Catalog HTTP Pathhttp://artifacts.yourcompany.com/dbt/catalog.jsonFull URL to catalog.jsondbt Manifest HTTP Pathhttp://artifacts.yourcompany.com/dbt/manifest.jsonFull URL to manifest.jsondbt Run Results HTTP Pathhttp://artifacts.yourcompany.com/dbt/run_results.jsonFull URL to run_results.json (optional)

If using Basic Auth:

FieldValueUsernameyour-usernamePasswordyour-password

Configure dbt Options:

FieldRecommended ValueUpdate DescriptionsEnabledUpdate OwnersEnabledInclude TagsEnabledClassification NamedbtTags

​Verification

# Verify artifacts are accessible

curl http://artifacts.yourcompany.com/dbt/manifest.json | jq '.metadata.dbt_version'

curl http://artifacts.yourcompany.com/dbt/catalog.json | jq '.metadata.dbt_version'

# Check from OpenMetadata's network

# (Run this from OpenMetadata's server/container)

curl -I http://artifacts.yourcompany.com/dbt/manifest.json

​Security Considerations

​Enable HTTPS

Use Let’s Encrypt for free SSL certificates:

# Install certbot

sudo apt install -y certbot python3-certbot-nginx

# Get certificate

sudo certbot --nginx -d artifacts.yourcompany.com

# Auto-renew

sudo certbot renew --dry-run

​Add Basic Authentication

For Nginx:

# Create password file

sudo apt install -y apache2-utils

sudo htpasswd -c /etc/nginx/.htpasswd collate

# Update Nginx config (already shown above)

For Apache:

# Create password file

sudo htpasswd -c /etc/apache2/.htpasswd collate

# Add to Apache config

<Directory /var/www/dbt-artifacts>

AuthType Basic

AuthName "Restricted Access"

AuthUserFile /etc/apache2/.htpasswd

Require valid-user

</Directory>

​IP Whitelisting

For Nginx:

location /dbt/ {

allow 10.0.0.0/8;        # Internal network

allow 203.0.113.0/24;    # OpenMetadata servers

deny all;

alias /var/www/dbt-artifacts/;

}

​Troubleshooting

IssueSymptomSolution403 ForbiddenAccess deniedCheck file permissions: chmod 644 /var/www/dbt-artifacts/*.json404 Not FoundFiles not foundVerify file paths and Nginx/Apache configConnection TimeoutCan’t reach serverCheck firewall rules, ensure port 80/443 openCORS ErrorBrowser blocks requestAdd CORS headers to web server configStale DataOld metadataVerify upload happens after dbt completes

​Next Steps

Configure dbt Workflow

dbt Troubleshooting

See other storage options: S3 | GCS | Azure | Local | dbt CloudWas this page helpful?YesNoSuggest editsRaise issuedbt Artifact Storage - Azure Blob Storage Configuration | OpenMetadataPreviousdbt Artifact Storage - Local Filesystem Configuration | OpenMetadataNext⌘I
