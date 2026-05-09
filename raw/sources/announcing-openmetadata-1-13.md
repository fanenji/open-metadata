---
source_url: "https://blog.open-metadata.org/announcing-openmetadata-1-13-123d66609468"
fetched: "2026-05-05"
title: "Announcing OpenMetadata 1.13"
author: "Shawn Gordon"
published: "2026-04-30"
original_tags: [clippings]
clipped_from: obsidian-web-clipper
---
*Open source semantic context layer for AI-ready data teams*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RnqyJJZL1OT4GX-92cV2EA.png)

We're excited to announce OpenMetadata 1.13, with new semantic context capabilities that data teams need to build AI that understands their business. Make sure your AI and data teams have a shared understanding of your data landscape. Highlights include:

- **Knowledge Graph**: Semantic context visualizations unifying technical and business metadata in an interactive graph
- **Ontology Explorer**: Visual map for navigating how business glossary terms relate to each other and to the data assets that implement them
- **Glossary Terms & Relations**: Define how business terms relate, with typed relationships that AI agents can reason over
- **Columns as Assets**: Columns surface as first-class discoverable assets throughout the platform

We started by standardizing metadata. Now we are standardizing meaning. This semantic context powers AI agents with the necessary context to deliver trusted results.

## Knowledge Graph

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TaHm6V1Ucrj2O9fKq5jBjw.png)

OpenMetadata 1.13 ships the Knowledge Graph, unifying technical metadata (e.g. schemas, lineage, ownership) with semantic metadata (e.g. glossary terms, classifications) into an interactive graph. Now you can navigate your entire data landscape, from business terms to data assets, in one unified view.

- **Semantic context graph**: Every AI agent, including LLMs connected via MCP, has a deep understanding of what data means and how it interconnects.
- **W3C-compatible**: OpenMetadata's semantic context graph supports open W3C standards, including RDF, OWL, DCAT, DPROD, SKOS, PROV-O, and Schema.org, to ensure portability and interoperability.
- **Auto-inferred relationships:** Knowledge Graph derives ownership chains, reverse relationships, and pipeline associations to surface connections your team never explicitly declared.
- **Bidirectional queries:** Start from any asset to see everything connected to it, or start from a team, domain, or glossary term to see what it owns or governs.

**Why this matters**: AI agents and data teams need semantic context to understand your data — schemas alone don't tell you how business terms connect. The Knowledge Graph gives teams visibility into this semantic context, ensuring that the same graph that powers AI reasoning is navigable by every data steward. Read our [Knowledge Graph product blog post](https://medium.com/openmetadata/00ab12b3488a) for more details.

## Ontology Explorer

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oruqyeZMnMJ9WmHfj70m8A.png)

Understand how your business glossary terms connect to each other and to the data that implements them. Ontology Explorer is an interactive map where data teams can build, navigate, and govern their business ontology visually, without writing a single query.

- **View modes**: Switch between Overview, Hierarchy, Related, and Cross Glossary perspectives to see how terms relate within a single glossary or across the whole organization.
- **Trace terms to data**: In Data Mode, see which tables, dashboards, and pipelines implement each business term, along with their quality scores, lineage, and ownership.
- **Build as you go**: Create new term relationships directly on the map, without clicking into individual term pages.
- **Share saved views**: Save curated graph perspectives for compliance teams, domain leads, or any stakeholder who needs the same picture you're looking at.

**Why this matters**: When a CDO asks which Revenue definition is authoritative, a flat glossary list doesn't show what's important. Ontology Explorer makes the relationships between business terms visual and navigable, so governance teams understand what matters, and AI agents downstream have the relationship structure they need to produce trustworthy answers. [Read our Ontology Explorer product blog post](https://medium.com/openmetadata/524f87c1a5c3) for more details.

## Glossary Terms & Relations

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9Iz5WWQM6xXdbKoJOAWB3g.png)

Define how your business terms actually relate to each other, not just that they're related. You can say ARR is *calculated* from Revenue, or that Customer Tier *has a part* called Behavioral Segment, or that Churn in Finance *is equivalent* to Attrition in Product. Glossary Terms & Relations gives admins a configurable schema layer for typed, RDF-compatible relationships between glossary terms.

- **Pick the right relationship type:** Define Hierarchical (broader, narrower), Associative (part of, has part, see also), Equivalence (calculated from, synonym, antonym), or other relationship types to match how your organization actually uses terms.
- **Set the rules per type:** Configure cardinality, transitivity, inverse relations, cross-glossary flags, and RDF predicates for every relationship type.
- **Track usage counts:** Understand which relationship types your teams rely on most to see where semantic coverage is strongest.

**Why this matters**: AI agents built on schema alone will always guess at the relationships between business terms. Glossary Terms & Relations lets you teach the platform that ARR is calculated from Revenue and that Churn means one thing in Finance and another in Product, so downstream AI reasons from governed context instead of making its own guesses.

## Columns as Assets

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*g9O1kyCRXfnPVAoiv3xv1g.png)

Columns are now first-class assets throughout OpenMetadata. Searching for a column name returns it directly in Explore results. Columns also appear in Glossary term pages and Classification asset lists, making column-level governance visible from every entry point.

- **Explore visibility**: Column searches return results at the column level, making fields directly discoverable.
- **Glossary & Classification visibility**: Columns surface as assets wherever governance context is shown, not buried inside table schemas.

**Why this matters**: Governance often happens at the column level, including classifications, glossary assignments, and quality rules. Discovery limited to tables makes column-level work harder to find or report on. Columns as Assets make that work visible from anywhere in the platform.

## New Connectors

OpenMetadata 1.13 adds support for multiple new connectors, expanding coverage across databases, reporting, messaging, orchestration, and AI integration sources:

- **BurstIQ**: Catalog metadata from the BurstIQ blockchain platform for healthcare and life sciences data.
- **SSRS**: Ingest metadata and lineage from SQL Server Reporting Services, including reports, data sources, and datasets.
- **Google Pub/Sub:** Catalog topics, subscriptions, and schemas from Google Cloud's messaging service.
- **Airflow REST API:** Ingest DAG metadata, pipeline schedules, and run history through Airflow's REST API.
- **Matillion Data Cloud:** Ingest pipeline metadata and lineage from Matillion's cloud-native ETL platform.
- **Model Context Protocol (Expansion)**: Our existing MCP support has been expanded to a full service category.

Now in Open Source:

- **Google Drive:** Catalog files and metadata from Google Drive shared drives and folders.
- **Microsoft Fabric Database:** Connect to Microsoft Fabric Data Warehouse for metadata and lineage.
- **Microsoft Fabric Pipeline:** Ingest pipeline metadata from Microsoft Fabric Data Factory.

## Collate 1.13 Features

The Collate-managed OpenMetadata service extends 1.13 with additional enterprise capabilities. Read the [Collate 1.13 release blog](https://www.getcollate.io/blog/announcing-collate-1-13) for full details.

- **Collate AI Analytics**: Native AI data analyst built for business users and analysts to get trusted answers faster. Go from natural language to a governed chart, to a shareable dashboard, grounded in your existing business context. Read the [AI Analytics product blog](https://www.getcollate.io/blog/introducing-collate-ai-analytics-your-ai-data-analyst) for more details.
- **Governance Workflow Improvements**: Workflows now trigger on state transitions, not just creation events. If an asset moves from Tier 2 to Tier 1, this reclassification can be routed through human review and approval before it takes effect.
- **Metadata Exporter — Trino Support**: Trino joins Snowflake, Databricks, BigQuery, and Redshift as a supported destination for scheduled governance analytics exports.
- **Hybrid Search**: Keyword and semantic search are now unified into a single query box to improve relevance and speed up data discovery across your data landscape.
- **New Collate Connectors** include Informix and Microsoft Access.

## Conclusion

OpenMetadata 1.13 ships the semantic context layer data teams need to build AI that understands their business. Knowledge Graph, Ontology Explorer, and Glossary Terms & Relations make business and technical semantic context explicit, navigable, and usable — for people and AI alike. The more your team invests in defining these relationships, the more trustworthy the AI agents and data assets built on top become.

Ready to get started? You can [install OpenMetadata 1.13](https://docs.open-metadata.org/), try it out with demo data in the [live sandbox](https://sandbox.open-metadata.org/), or sign up for [Collate's free tier of managed OpenMetadata service](https://www.getcollate.io/welcome). If you have questions about setting up OpenMetadata, read our [documentation](https://docs.open-metadata.org/) to get started, [join the Slack community](https://slack.open-metadata.org/), and provide feedback on [GitHub](https://github.com/open-metadata/OpenMetadata).

[Please star the OpenMetadata GitHub repo](https://github.com/open-metadata/OpenMetadata) to support the project and help more teams discover it!
