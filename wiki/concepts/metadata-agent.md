---
type: concept
title: Metadata Agent
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, agent, pipeline, scheduling, filtering]
related: [ingestion-framework, metadata-ingestion-workflow, service-connection, filter-patterns, ingestion-scheduling, soft-deletion, omjob-operator, pipeline-service-client]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Metadata Agent

A configurable, schedulable pipeline that extracts metadata from a connected external source and ingests it into OpenMetadata. The Metadata Agent is the user-facing abstraction over the [[ingestion-framework|Ingestion Framework]], deployed and managed through the OpenMetadata UI.

## Configuration Options

### Filter Patterns
Control the scope of ingestion by including or excluding specific assets:

- **Database Filter Pattern**: Include or exclude databases within a service connection. A single service may contain multiple databases — use this to limit ingestion to relevant ones.
- **Schema Filter Pattern**: Include or exclude schemas within selected databases.
- **Table Filter Pattern**: Include or exclude tables within selected schemas.

Patterns can use simple names or Fully Qualified Names (FQN) when the **Use FQN For Filtering** toggle is enabled.

### Ingestion Toggles

| Toggle | Purpose |
|--------|---------|
| **Use FQN For Filtering** | Apply filter patterns against fully qualified names instead of simple names |
| **Include Views** | Control whether database views are ingested alongside tables |
| **Include Tags** | Include [[glossary-tags|tags and classifications]] as part of metadata ingestion |
| **Enable Debug Log** | Enable verbose logging for troubleshooting ingestion issues |
| **Mark Deleted Tables** | Enable [[soft-deletion|soft deletion]]: tables absent from the source are marked as deleted rather than permanently removed, preserving lineage and history |

### Query Parsing Timeout Limit
Specifies the timeout (in seconds) for parsing view definition SQL queries during lineage analysis. Defaults to **300 seconds**. Increase this value for complex views with long-running query parsing.

## Scheduling

Metadata Agents run on a recurring schedule defined during deployment:

- **Preset intervals**: Hourly, Daily, Weekly, Monthly
- **Custom cron expressions**: For fine-grained scheduling control
- **Retries**: Configurable number of automatic retries on pipeline failure

The underlying execution is handled by the configured orchestration backend — either Apache Airflow or the [[kubernetes-native-orchestrator|Kubernetes-native orchestrator]] via the [[omjob-operator|OMJob Operator]].

## Agent Lifecycle Management

From the Agents tab, administrators can:

- **Run**: Trigger an immediate ingestion run
- **Kill**: Stop all currently running instances of the pipeline
- **Re Deploy**: Redeploy after configuration, schedule, or credential changes (e.g., updated source connection credentials)
- **Edit**: Modify agent configuration
- **Delete**: Remove the agent permanently

## Agent Types

Beyond the Metadata Agent, additional agent types can be added to a service for specialized ingestion:
- **Usage Agent**: Ingests query usage statistics
- **Lineage Agent**: Ingests data lineage information
- **dbt Agent**: Ingests dbt model metadata
- **Profiler Agent**: Runs data profiling and quality tests