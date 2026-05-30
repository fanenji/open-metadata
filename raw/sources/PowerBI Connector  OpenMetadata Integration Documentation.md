---
title: "PowerBI Connector | OpenMetadata Integration Documentation"
source: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi"
author:
published:
created: 2026-05-14
description: "Connect Power BI to OpenMetadata with our comprehensive dashboard connector guide. Setup instructions, configuration tips, and metadata extraction made simple."
tags:
  - "clippings"
topic:
type: "note"
---
## PowerBI

PROD

In this section, we provide guides and references to use the PowerBI connector.

**Supported Authentication Types:**

- **OAuth 2.0 Service Principal** — Azure AD application authentication using Client ID, Client Secret, and Tenant ID

Configure and schedule PowerBI metadata and profiler workflows from the OpenMetadata UI:

- [Requirements](#requirements)
- [Metadata Ingestion](#metadata-ingestion)
- [Lineage](#lineage)
- [Troubleshooting](https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi/troubleshooting)

## Requirements

To access the PowerBI APIs and import dashboards, charts, and datasets from PowerBI into OpenMetadata, a `PowerBI Pro` license is necessary.

PowerBI dataflows are not yet supported.

OpenMetadata does not support Power BI usage ingestion because the Power BI Usage API does not support Service Principal authentication.

When configuring Azure Authentication, ensure that “Allow public client flows” is enabled. This setting is required to support authentication for public client applications.

### PowerBI Admin and Non-Admin APIs:

While configuring the PowerBI ingestion you can choose whether to use the PowerBI Admin APIs to retrieve the metadata or use the PowerBI Non-Admin APIs. Please check below for the the difference in their functionality:

- Enabled (Use PowerBI Admin APIs) Using the admin APIs will fetch the dashboard and chart metadata from all the workspaces available in the PowerBI instance.

When using the PowerBI Admin APIs, the table and dataset information used to generate lineage is gathered using the PowerBI [Scan Result](https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result) API. This API has no limitations and hence does not restrict getting the necessary data for generating lineage.

- Disabled (Use Non-Admin PowerBI APIs) Using the non-admin APIs will only fetch the dashboard and chart metadata from the workspaces that have the security group of the service principal assigned to them.

When using the PowerBI Non-Admin APIs, the table and dataset information used to generate lineage is gathered using the PowerBI [Get Dataset Tables](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables) API. This API only retrieves the table information if the dataset is a [Push Dataset](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets). Hence the lineage can only be created for push datasets in this case. For more information please visit the PowerBI official documentation [here](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables#limitations).

### PowerBI Account Setup

Follow the steps below to configure the account setup for PowerBI connector:

### Step 1: Enable API permissions from the PowerBI Admin console

We extract the information from PowerBI using APIs, this is a manual step a PowerBI Admin needs to do to ensure we can get the right information. Login to the [Power BI](https://app.powerbi.com/) as Admin and from `Tenant` settings allow below permissions.

- Allow service principles to use Power BI APIs
- Allow service principals to use read-only Power BI admin APIs
- Enhance admin APIs responses with detailed metadata

### Step 2: Create the App in Azure AD

Please follow the steps mentioned [here](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal) for setting up the Azure AD application service principle.

### Step 3: Provide necessary API permissions to the Azure AD app

Go to the `Azure Ad app registrations` page, select your app and add the dashboard permissions to the app for PowerBI service and grant admin consent for the same: The required permissions are:

- `Dashboard.Read.All` Optional Permissions: (Without granting these permissions, the dataset information cannot be retrieved and the datamodel and lineage processing will be skipped)
- `Dataset.Read.All`

Make sure that in the API permissions section **Tenant** related permissions are not being given to the app Please refer [here](https://stackoverflow.com/questions/71001110/power-bi-rest-api-requests-not-authorizing-as-expected) for detailed explanation

### Step 4: PowerBI Workspaces

The service principal does not take into account the default user workspaces e.g `My Workspace`. Create new workspaces in PowerBI by following the document [here](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-the-new-workspaces) For reference here is a [thread](https://community.powerbi.com/t5/Service/Error-while-executing-Get-dataset-call-quot-API-is-not/m-p/912360#M85711) referring to the same

## Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.  
  
To create a service connection and ingest your metadata, follow the steps below:

## Connection Details

## Lineage

To establish lineage from your **database tables to dashboards**, you must add the corresponding **database service name**.

![lineage in dashboard](https://mintcdn.com/openmetadata/9SXjaLbGROaofLQU/public/images/connectors/dashboard-lineage.png?w=2500&fit=max&auto=format&n=9SXjaLbGROaofLQU&q=85&s=b2d2afcf3b0d32c40971e7f6b3a95297)

lineage in dashboard