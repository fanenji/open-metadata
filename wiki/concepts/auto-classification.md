---
type: concept
title: Auto-Classification
created: 2026-05-14
updated: 2026-05-15
tags: [data-governance, classification, auto-classification, pii, nlp, profiling, automation, agent, openmetadata, data-profiling, governance]
related: [auto-pii-tagging, tag-mapping, classification-tags, data-profiling, pii-sample-data-masking, system-classification, ingestion-framework, nlp-based-profiler-classification, tag-request-workflow, metadata-agent, metadata-ingestion-workflow, sample-data-storage-toggle, agent-based-ingestion, how-to-classify-data-assets-official-documentation-20260514]
sources: ["auto-classification-in-openmetadata---openmetadata-20260514.md", "adding-auto-classification-workflow-through-ui---o-20260514.md", "how-to-add-tags-openmetadata-user-tagging-guide----20260514.md"]
---

# Auto-Classification

Auto-classification is an automated data governance feature in OpenMetadata that detects personally identifiable information (PII) and other sensitive data. Using Natural Language Processing (NLP), it analyzes column names and sample data content to identify sensitive fields and automatically assign relevant [[classification-tags]], such as `PII.Sensitive`. The feature can be triggered either as part of the [[data-profiling|profiling phase]] during [[ingestion-framework|metadata ingestion]] or through a dedicated scheduled agent, enabling both one-time and recurring classification runs without manual intervention.

Auto-classification extends the [[classification-tags]] system with agent-based automation, providing a flexible governance workflow.

## How Auto-Classification Detects Sensitive Data

When auto-classification runs, the NLP engine examines two dimensions:

1. **Column names** — Recognizes patterns like `last_name`, `email`, `social_security_number` that indicate PII.
2. **Sample data content** — Analyzes the actual data values in the column using NLP to detect PII even when the column name provides no clues.

This dual approach ensures that sensitive data is identified both through explicit naming conventions and through content-based inference.

### Content-Based Detection Example

A column named `dwh_x10` gives no indication of its contents from its name alone. However, when the profiler examines the sample data values, it detects PII content and auto-tags the column as `PII.Sensitive`. This demonstrates that auto-classification is not merely name-based — it performs deep content analysis.

## Triggering Auto-Classification

Auto-classification can be initiated through two different mechanisms:

### Profiling-Triggered Auto-Classification

As part of the [[data-profiling|profiler]] during [[ingestion-framework|metadata ingestion]], auto-classification runs automatically when profiling is enabled for a data source. It leverages the NLP detection described above to analyze data and apply tags. This approach requires:

- The profiler to be enabled during ingestion for the target data source.
- The ingestion pipeline to have access to sample data from the source tables.
- [[system-classification|System classification tags]] (such as `PII.Sensitive`) to be available in the environment.

This method is well-suited for environments where profiling is already part of the regular metadata ingestion workflow.

### Agent-Triggered Auto-Classification (Scheduled)

A newer, more flexible approach uses a scheduled agent to perform auto-classification independently of the ingestion pipeline. The Auto Classification Agent follows the [[agent-based-ingestion|agent-based pattern]] and can be configured per-database service:

1. Navigate to **Settings > Services > Databases**.
2. Select the target database service.
3. Access the **Agents** tab.
4. Click **Add Auto Classification Agent**.
5. Configure details, including:
   - **Name** for the agent.
   - **Sample data storage toggle** (enabled by default) — controls whether sample data is ingested during scheduled runs for content analysis (see [[sample-data-storage-toggle]]). Disabling this toggle skips sample data ingestion, which may be desirable for performance or privacy reasons.
6. Set the schedule time interval.
7. Click **Add Auto Classification Agent** to activate.

The agent runs on the configured schedule, detecting and tagging sensitive data using the same NLP engine, without requiring a full metadata ingestion. Once configured, the agent operates without further human involvement, enabling ongoing, at-scale classification.

## Tag Application Behavior

The source documentation uses both "auto-tags" and "suggests the tags" language, creating some ambiguity about the exact behavior. In practice, the feature may either:

- **Automatically apply** the detected tag without user intervention, or
- **Suggest** the tag for review, requiring a governance user to approve before it becomes active.

The exact behavior may depend on configuration settings or the confidence level of the NLP detection. This distinction is important for governance workflows — if tags are only suggested, a review step is required before enforcement via [[roles-and-policies|ABAC policies]].

## Comparison with Manual Classification

The table below contrasts the automated auto-classification approaches with manual methods:

| Method                                     | Trigger                      | Human Involvement                                   | Use Case                                                         |
|--------------------------------------------|------------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| Manual [[classification-tags|Classification]] | User applies tags via UI     | Direct                                              | Ad-hoc tagging of known columns                                  |
| [[tag-request-workflow|Tag Request Workflow]] | User submits a request       | Review-based                                        | Collaborative governance with approval                           |
| **Auto-Classification (Profiling)**        | Ingestion profiling phase    | Requires profiling config; runs automatically       | Integrated with regular ingestion; good for new or updated data  |
| **Auto-Classification (Agent)**            | Scheduled agent run          | None after configuration                            | Dedicated recurring runs; independent of full ingestion          |

## Relationship to Other Features

Once applied, auto-classification tags trigger downstream behaviors:

- **[[pii-sample-data-masking]]**: Auto-classification is the prerequisite for PII masking. When a column is auto-tagged as `PII.Sensitive`, the UI automatically masks the sample data displayed for that column, replacing values with `******`. Masking also inherits from table-level tags to all columns.
- **[[tag-request-workflow]]**: Auto-classification provides an automated alternative to the manual, collaborative tag request workflow. While tag requests involve human review and discussion, auto-classification operates programmatically.
- **[[tag-mapping]]**: Auto-classification can be extended through tag mapping, where applying one tag automatically cascades to associated tags (e.g., `Personal Data.Personal` → `Data Classification.Confidential`).
- **[[classification-tags]]**: Auto-classification is a complementary mechanism to the manual 3-step tagging workflow, providing an automated path for initial tag assignment.

Additionally, the OpenMetadata documentation navigation lists "Auto PII Tagging" as a sibling page to the Auto Classification workflow. The exact relationship between these two features is an open question—they may be the same feature described from different angles, or distinct capabilities with different detection scopes.

## Limitations and Open Questions

- **Tag application**: Does auto-classification apply tags automatically or only suggest them? The documentation uses both terms, and the exact behavior may depend on configuration.
- **NLP sensitivity and configurability**: What configuration options exist for controlling NLP sensitivity, tag application behavior, or selecting specific PII categories? Currently unclear.
- **Scoping**: Can auto-classification be disabled or limited to specific schemas/tables? Not documented.
- **Relationship with Auto PII Tagging**: What is the exact relationship between Auto Classification and Auto PII Tagging? They may be the same feature or distinct.
- **Interaction of triggering methods**: How do the profiling-triggered and agent-triggered auto-classification methods interact if both are configured for the same service? Unknown.
- **Language support**: Does the NLP-based detection handle non-English data? Not specified.
- **Accuracy**: No metrics are provided for the precision or recall of content-based PII detection.

## See Also

- [[classification-tags]] — The broader tagging system that auto-classification feeds into.
- [[how-to-classify-data-assets-official-documentation-20260514]] — The detailed admin guide for classification.
- [[agent-based-ingestion]] — The architectural pattern underlying the Auto Classification Agent.
- [[pii-sample-data-masking]] — The downstream effect of auto-classification on sample data display.