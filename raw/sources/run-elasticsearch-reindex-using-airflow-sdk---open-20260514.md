---
type: clip
title: "Run Elasticsearch Reindex using Airflow SDK - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/elasticsearch-reindex"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Run Elasticsearch Reindex using Airflow SDK - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/elasticsearch-reindex

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData InsightsRun Elasticsearch Reindex using Airflow SDKHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData InsightsOverviewWhat is TieringSet Up Data Insights IngestionKey Performance Indicators (KPI)Elasticsearch reindexData Insights ReportConfigure the Data Insights ReportHow to Transform the Data Culture of Your CompanyService InsightsOn this pageRun Elasticsearch Reindex using Airflow SDK1. Define the YAML Config2. Prepare the Ingestion DAGDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Run Elasticsearch Reindex using Airflow SDK

​1. Define the YAML Config

This is a sample config for Elasticsearch Reindex:

source:

source:

type: metadata_elasticsearch

serviceName: OpenMetadata

serviceConnection:

config:

type: MetadataES

sourceConfig:

config: {}

sink:

type: elasticsearch

config:

es_host: localhost

es_port: 9200

recreate_indexes: true

workflowConfig:

OpenMetadataServerConfig:

hostPort: http://localhost:8585/api

authProvider: OpenMetadata

securityConfig:

jwtToken: "eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImlzQm90IjpmYWxzZSwiaXNzIjoib3Blbi1tZXRhZGF0YS5vcmciLCJpYXQiOjE2NjM5Mzg0NjIsImVtYWlsIjoiYWRtaW5Ab3Blbm1ldGFkYXRhLm9yZyJ9.tS8um_5DKu7HgzGBzS1VTA5uUjKWOCU0B_j08WXBiEC0mr0zNREkqVfwFDD-d24HlNEbrqioLsBuFRiwIWKc1m_ZlVQbG7P36RUxhuv2vbSp80FKyNM-Tj93FDzq91jsyNmsQhyNv_fNr3TXfzzSPjHt8Go0FMMP66weoKMgW2PbXlhVKwEuXUHyakLLzewm9UMeQaEiRzhiTMU3UkLXcKbYEJJvfNFcLwSl9W8JCO_l0Yj3ud-qt_nQYEZwqW6u5nfdQllN133iikV4fM5QZsMCnm8Rq1mvLR0y9bmJiD7fwM1tmJ791TUWqmKaTnP49U493VanKpUAfzIiOiIbhg"

​2. Prepare the Ingestion DAG

Create a Python file in your Airflow DAGs directory with the following contents:

import pathlib

import yaml

from datetime import timedelta

from airflow import DAG

try:

from airflow.operators.python import PythonOperator

except ModuleNotFoundError:

from airflow.operators.python_operator import PythonOperator

from metadata.config.common import load_config_file

from metadata.workflow.metadata import MetadataWorkflow

from metadata.workflow.workflow_output_handler import print_status

from airflow.utils.dates import days_ago

default_args = {

"owner": "user_name",

"email": ["username@org.com"],

"email_on_failure": False,

"retries": 3,

"retry_delay": timedelta(minutes=5),

"execution_timeout": timedelta(minutes=60)

}

config = """

<your YAML configuration>

"""

def metadata_ingestion_workflow():

workflow_config = yaml.safe_load(config)

workflow = MetadataWorkflow.create(workflow_config)

workflow.execute()

workflow.raise_from_status()

print_status(workflow)

workflow.stop()

with DAG(

"sample_data",

default_args=default_args,

description="An example DAG which runs a OpenMetadata ingestion workflow",

start_date=days_ago(1),

is_paused_upon_creation=False,

schedule_interval='*/5 * * * *',

catchup=False,

) as dag:

ingest_task = PythonOperator(

task_id="ingest_using_recipe",

python_callable=metadata_ingestion_workflow,

)

Was this page helpful?YesNoSuggest editsRaise issueKey Performance Indicators (KPI) | Official DocumentationPreviousData Insights Report | OpenMetadata Reporting GuideNext⌘I
