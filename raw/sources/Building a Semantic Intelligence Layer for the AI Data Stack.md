---
title: Building a Semantic Intelligence Layer for the AI Data Stack
source: https://medium.com/google-cloud/building-a-semantic-intelligence-layer-for-the-ai-data-stack-0c867fd23e6f
author:
  - "[[MCP Toolbox for Databases]]"
published: 2026-03-24
created: 2026-04-05
description: "Building a Semantic Intelligence Layer for the AI Data Stack Written by: Mike DeAngelo, Developer Relations Engineer @ Google (LinkedIn) Nick Acosta, Developer Advocate @ Collate (LinkedIn) Imagine a …"
tags:
  - clippings
  - openmetadata
  - ai
  - mcp
topic:
type: note
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)## [Google Cloud - Community](https://medium.com/google-cloud?source=post_page---publication_nav-e52cf94d98af-0c867fd23e6f---------------------------------------)

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:76:76/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_sidebar-e52cf94d98af-0c867fd23e6f---------------------------------------)

A collection of technical articles and blogs published or curated by Google Cloud Developer Advocates. The views expressed are those of the authors and don't necessarily reflect those of Google.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*kjdqSvEe403TJNwjHmyBwg.png)

Written by:

- Mike DeAngelo, Developer Relations Engineer @ Google ([LinkedIn](https://www.linkedin.com/in/mike-deangelo/))
- Nick Acosta, Developer Advocate @ Collate ([LinkedIn](https://www.linkedin.com/in/nickacosta/))

Imagine a dashboard filled with perfectly modeled and tested data, bringing it to your team for the next move, and everyone quickly aligning around an obvious decision. But a few weeks later, the results didn’t match expectations. Data teams are better than ever at collecting, cleaning, and visualizing data, but can still struggle with communicating assumptions, limitations, and conditions present in data’s semantics.

At [Kansai Airports,](https://open-metadata.org/case-study/kansai-airports) different departments had different definitions of “passengers.” For some teams, a “passenger” was only every paying customer, others included crew and infants. Aligning on a standard definition of this key metric helped make the airport’s data more people-ready, but the jump to AI-ready data is even steeper because an agent will not stop and deliberate when it sees two different “passenger” counts. While [OpenMetadata](https://open-metadata.org/) acts as a semantic library storing shared definitions, relationships, and context, [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) empowers AI agents to generate and run application code and tests with a deep understanding of your enterprise data. Together, these open-source tools use semantic intelligence to turn metadata into meaning and allow AI to take action that is trustworthy, explainable, and safe.

In this article, we provide a guide on configuring OpenMetadata alongside MCP Toolbox. We also highlight various use cases currently employed by the open-source community to effectively scale AI operations.

## Step-By-Step Guide

OpenMetadata can be set up quickly in a local environment using Docker. Each deployment has an embedded MCP Server already integrated into the OpenMetadata platform. The MCP server leverages the same authorization engine established for OpenMetadata APIs. This enables any MCP client to interface with existing OpenMetadata integrations for read or write operations, while adhering to established roles and policies. Consequently, agents are granted appropriate access to the specific data and functional logic required to automate data operations effectively.

### Step 1: Download OpenMetadata

[Download Docker](https://www.docker.com/products/docker-desktop/) and run the following command to get OpenMetadata’s Docker Compose file:

```c
curl -sL -o docker-compose-postgres.yml https://github.com/open-metadata/OpenMetadata/releases/download/1.12.3-release/docker-compose-postgres.yml
```

Once downloaded, start OpenMetadata and its dependencies by running:

```c
docker compose -f docker-compose-postgres.yml up --d
```

This will install a OpenMetadata standalone instance on your local machine. OpenMetadata’s embedded MCP Server architecture fully integrates an MCP Server into OpenMetadata by default, enabling AI Agents to act on assets stored in OpenMetadata without any setup and giving agents the proper access to the right data and functional logic to automate data operations.

## Step 2: Generate Looker Credentials

You will need an Looker API `client_id` and `client_secret`. You can find that information from [Looker API authentication](https://docs.cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk). If the “Manage” button is greyed out, contact your Looker administrator for help.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FjnZ-MUxBiSYKmKKXPjKmQ.gif)

Generate API credentials for a Looker user account.

## Step 3: Setup MCP Toolbox and OpenMetadata MCP in Gemini CLI

In this section, we will be installing MCP Toolbox with [Gemini CLI](https://github.com/google-gemini/gemini-cli). Instructions for installing MCP Toolbox with other agents can be found [here](https://googleapis.github.io/genai-toolbox/how-to/connect-ide/looker_mcp/).

To get started, install the Gemini CLI:

```c
npm install -g @google/gemini-cli
```

Next, add the MCP Toolbox server and OpenMetadata MCP Server:

```c
gemini mcp add -t stdio looker-toolbox \
  npx -y @toolbox-sdk/server --stdio --prebuilt looker \
  -e LOOKER_BASE_URL=https://looker.example.com \
  -e LOOKER_CLIENT_ID="<YOUR_LOOKER_CLIENT_ID>" \
  -e LOOKER_CLIENT_SECRET="<YOUR_LOOKER_CLIENT_SECRET>" \
  -e LOOKER_VERIFY_SSL=true

gemini mcp add -t stdio OpenMetadata \
  npx -y mcp-remote http://localhost:8585/mcp \
  --auth-server-url=http://localhost:8585/mcp --client-id=OpenMetadata \
  --verbose --clean "--header" "Authorization:${AUTH_HEADER}" \
  -e AUTH_HEADER="Bearer <YOUR_OPENMETADATA_JWT_TOKEN>"
```

Now, editing ~/.gemini/settings.json will allow you to add Looker and OpenMetadata MCP Servers to Gemini-CLI, your settings.json should contain the following:

```c
{
  "security": {
    "auth": {
      "selectedType": "oauth-personal"
    }
  },
  "ui": {
    "theme": "Default Light"
  },
  "mcpServers": {
    "looker-toolbox": {
      "command": "npx",
      "args": [
        "-y",
        "@toolbox-sdk/server",
        "--stdio",
        "--prebuilt",
        "looker"
      ],
      "env": {
        "LOOKER_BASE_URL": "https://looker.example.com",
        "LOOKER_CLIENT_ID": "<YOUR_LOOKER_CLIENT_ID>",
        "LOOKER_CLIENT_SECRET": "<YOUR_LOOKER_CLIENT_SECRET>",
        "LOOKER_VERIFY_SSL": "true"
      }
    },
    "OpenMetadata": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "http://localhost:8585/mcp",
        "--auth-server-url=http://localhost:8585/mcp",
        "--client-id=OpenMetadata",
        "--verbose",
        "--clean",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <YOUR_OPENMETADATA_JWT_TOKEN"
      }
    }
  }
}
```

To get LookML development tools in addition to the query and content tools, change the line

```c
"args": ["--stdio", "--prebuilt", "looker"],
# to
"args": ["--stdio", "--prebuilt", "looker,looker-dev"],
```

Note: this guide is running Gemini CLI from the home path (~) and [authenticated with a Google Account](https://geminicli.com/docs/get-started/authentication/).

You may have to restart Gemini-CLI for it to pick up these new MCP Servers. Once restarted, type `/mcp` and you should see a list of available tools like:

```c
Configured MCP servers:

   🟢 looker-toolbox - Ready (10 tools)
     - looker-toolbox__get_models
     - looker-toolbox__query
     - looker-toolbox__get_looks
     - looker-toolbox__get_measures
     - looker-toolbox__get_filters
     - looker-toolbox__get_parameters
     - looker-toolbox__get_explores
     - looker-toolbox__query_sql
     - looker-toolbox__get_dimensions
     - looker-toolbox__run_look
     - looker-toolbox__query_url

🟢 OpenMetadata - Ready (12 tools, 2 prompts)
  Tools:
  - mcp_OpenMetadata_create_glossary
  - mcp_OpenMetadata_create_glossary_term
  - mcp_OpenMetadata_create_lineage
  - mcp_OpenMetadata_create_metric
  - mcp_OpenMetadata_create_test_case
  - mcp_OpenMetadata_get_entity_details
  - mcp_OpenMetadata_get_entity_lineage
  - mcp_OpenMetadata_get_test_definitions
  - mcp_OpenMetadata_patch_entity
  - mcp_OpenMetadata_root_cause_analysis
  - mcp_OpenMetadata_search_metadata
  - mcp_OpenMetadata_semantic_search
  Prompts:
  - create-greeting
  - search_metadata
```

### Step 4: Ingest Looker metadata into OpenMetadata

OpenMetadata ingests metadata from over 120 cloud data services. Adding Looker to OpenMetadata helps to track and manage ownership and lineage of Looker Dashboards, Charts, and LookML Models across data sources and departments. To add Looker to OpenMetadata:

1. In OpenMetadata, click “Settings” at the bottom of the side navigation bar and then “Services”. Looker will be service type: “Dashboards”. After selecting “Dashboards”, select “Add New Service” and look for the Looker icon.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*7VAI2VKbbR1KYcc8bHs3Cg.png)

Selecting Looker as the new dashboard service type.

2\. After providing a `Service Name`, OpenMetadata needs the following to connect to Looker:

- **Client ID**: User’s Client ID to authenticate to the SDK. This user should have privileges to read all the metadata in Looker.
- **Client Secret**: User’s Client Secret for the same ID provided.
- **Host and Port**: URL to the Looker instance, e.g., [https://my-company.region.looker.com.](https://my-company.region.looker.com./)
- **Repository Owner**: The owner of a GitHub repository. For example, in [https://github.com/open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata), the owner is “open-metadata”.
- **Repository Name**: The name of a GitHub repository. For example, in [https://github.com/open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata), the name is “OpenMetadata”.
- **API Token**: Token to use the API. This is required for private repositories and to ensure we don’t hit API limits. Follow these [steps](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token) in order to create a fine-grained personal access token. When configuring, give repository access to “Only select repositories” and choose the one containing your LookML files. Then, we only need “Repository Permissions” as read-only for `Contents`.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*qtWlSdhU7jMQOMhhujd-ig.png)

Entering authentication and GitHub credentials for Looker integration.

With your Looker connector configured, OpenMetadata will start ingesting Looker metadata!

## Use Cases

Integrating OpenMetadata, Looker, and MCP Toolbox provides your AI agents with a comprehensive understanding of the semantics within your data stack and Looker environment. To help you scale your operations, we’ve highlighted two key strategies currently being adopted by the community:

### 1\. Automated Tag Synchronization

As different builders and agents produce new data assets across data services, [OpenMetadata’s MCP Server](https://open-metadata.org/mcp) and MCP Toolbox provide automated ways to synchronize tags, descriptions, and other metadata across the tools in your data stack. This ensures that as your data ecosystem expands, and more agents are added, the semantic context remains consistent across every tool in your stack. By automating these updates, your Looker environment can stay up-to-date regardless of the data sources that are being used to populate dashboards.

With both MCP Servers installed in [Gemini CLI](https://geminicli.com/), you can prompt the agent with:

> “ *Use OpenMetadata to trace the lineage for my* `*ecommerce.customers*` *LookML Data Model, apply all tags and field descriptions from its upstream data sources corresponding LookML fields*.”

### 2\. Generating Custom Metadata Insights

We are also seeing developers use [OpenMetadata’s MCP Server](https://open-metadata.org/mcp) to pull stats like asset and user counts from OpenMetadata to build Looker charts that track adoption of data services. By leveraging MCP Toolbox, agents can quickly turn prompts into insights that can provide a deeper understanding of the health of your data environments.

To implement this use case, the stats from OpenMetadata need to be written to a database before they can be consumed through Looker. Use MCP Toolbox to connect to a database, e.g. Postgres, AlloyDB, etc.. The Docker Compose file used to install OpenMetadata earlier ships with a Postgres instances the can be used in Gemini CLI via the MCP Toolbox by adding the following to`.gemini/settings.json`:

```c
{
    "mcpServers": {
        "postgres": {
            "command": "toolbox",
            "args": [
                "--prebuilt",
                "postgres",
                "--stdio"
            ],
            "env": {
                "POSTGRES_HOST": "localhost",
                "POSTGRES_PORT": "5432",
                "POSTGRES_DATABASE": "openmetadata_db",
                "POSTGRES_USER": "openmetadata_user",
                "POSTGRES_PASSWORD": "openmetadata_password"
            }
        }
    }
}
```

Then, prompt Gemini-CLI to:

> *“Calculate the total number of assets in OpenMetadata by asset type, create a table to hold these stats in Postgres, and write them to the newly created table.”*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5EByN2jqZJoa9556X1v5uw.gif)

From here, we could have Gemini CLI connect Postgres and Looker, create a new LookML project, and initial LookML model, before building dashboards and Looks based on our new data.

## Conclusion

Integrating OpenMetadata and MCP Toolbox can bring Semantic Intelligence to Looker and the rest of your data stack, providing powerful capabilities that give AI agents and other AI workflows a deep understanding of data assets, relationships and context. For more information on OpenMetadata, please check it out on [GitHub](https://github.com/open-metadata) and join the [OpenMetadata Slack Community](https://slack.open-metadata.org/). To explore the MCP Toolbox, check out the [GitHub repository](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fmcp-toolbox), read the [documentation](https://www.google.com/search?q=https%3A%2F%2Fmcp-toolbox.com%2Fdocs), and join our [Discord serve](https://www.google.com/search?q=https%3A%2F%2Fdiscord.gg%2Fmcptoolbox) r to connect with the community.

For more on OpenMetadata and MCP Toolbox, please be sure to attend the next OpenMetadata Community Meeting! Google developers, Wenxin Du and Mike DeAngelo, will be showcasing MCP Toolbox at this virtual meetup [this Wednesday, March 25th, 2026 at 9 AM PST](https://luma.com/s4kl1x9f)!

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:96:96/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_info--0c867fd23e6f---------------------------------------)

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:128:128/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---post_publication_info--0c867fd23e6f---------------------------------------)

[Last published 3 hours ago](https://medium.com/google-cloud/gemma-4-and-the-rise-of-agentic-commerce-34dc723ab736?source=post_page---post_publication_info--0c867fd23e6f---------------------------------------)

A collection of technical articles and blogs published or curated by Google Cloud Developer Advocates. The views expressed are those of the authors and don't necessarily reflect those of Google.

[![MCP Toolbox for Databases](https://miro.medium.com/v2/resize:fill:96:96/1*FprCEQmwO8Xy36qI2s2OMw.png)](https://medium.com/@mcp_toolbox?source=post_page---post_author_info--0c867fd23e6f---------------------------------------)

[![MCP Toolbox for Databases](https://miro.medium.com/v2/resize:fill:128:128/1*FprCEQmwO8Xy36qI2s2OMw.png)](https://medium.com/@mcp_toolbox?source=post_page---post_author_info--0c867fd23e6f---------------------------------------)

[4 following](https://medium.com/@mcp_toolbox/following?source=post_page---post_author_info--0c867fd23e6f---------------------------------------)

MCP Toolbox: Google Cloud's open source MCP server for databases. Develop tools easier, faster & securely. [https://googleapis.github.io/genai-toolbox](https://googleapis.github.io/genai-toolbox)

## Responses (4)

S Parodi

What are your thoughts?  

```c
The Kansai Airports example highlights a critical point – differing definitions aren’t just a people problem, they’re a fatal flaw for AI. Given that MCP Toolbox relies on OpenMetadata’s authorization, how robust is that system against evolving…more
```

```c
Interesting architecture. The Kansai Airports "passengers" problem is the exact scenario we've been solving -- different departments, same term, different definitions.The challenge with the OpenMetadata + MCP Toolbox approach is that the semantic…more
```

```c
Dear Authors. Thank you for this. 

As a BI engineer on BQ, with a shaky understanding of MCPs, I don't understand from your article which Metadata, or even which data, is gonna be seen by Open Metadata. I'm considering undertaking an exercise where…more
```