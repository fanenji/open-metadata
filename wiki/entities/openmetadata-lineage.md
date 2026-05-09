---
type: entity
title: OpenMetadata Lineage
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, lineage, data-lineage, column-level-lineage]
related: [openmetadata, openmetadata-ingestion-framework, openmetadata-python-sdk, dbt, data-observability-three-pillars, data-root-cause-analysis]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Lineage

OpenMetadata captures table-level and column-level lineage across platforms, enabling impact analysis and root cause tracing.

## What It Captures

- **Table-level lineage** — which tables feed which tables
- **Column-level lineage** — which column feeds which column, through SQL transformations
- **Cross-platform lineage** — from S3 → Spark → Snowflake → dbt → Tableau, in one graph

## How Lineage Gets Built

1. **Automated** — Connectors parse query logs, dbt manifests, and pipeline metadata.
2. **Manual** — Draw lineage directly in the UI when automated capture isn't possible.
3. **API** — Push lineage programmatically via the Python SDK.

## dbt Lineage Integration

Ingest `manifest.json` to automatically build the full model-to-model lineage graph:

```yaml
source:
  type: dbt
  serviceName: analytics-dbt
  serviceConnection:
    config:
      type: dbt
      dbtConfigSource:
        dbtManifestFilePath: /path/to/manifest.json
        dbtCatalogFilePath: /path/to/catalog.json
        dbtRunResultsFilePath: /path/to/run_results.json
  sourceConfig:
    config:
      type: DBTMetadata
      dbtUpdateDescriptions: true
      includeTags: true
```

## Pushing Lineage via Python SDK

```python
from metadata.generated.schema.type.entityLineage import EntitiesEdge
from metadata.generated.schema.api.lineage.addLineage import AddLineageRequest

source_table = metadata.get_by_name(entity=Table, fqn="snowflake_service.analytics_db.public.raw_orders")
target_table = metadata.get_by_name(entity=Table, fqn="snowflake_service.analytics_db.public.fct_orders")

lineage_request = AddLineageRequest(
    edge=EntitiesEdge(
        fromEntity=EntityReference(id=source_table.id, type="table"),
        toEntity=EntityReference(id=target_table.id, type="table"),
    )
)
metadata.add_lineage(lineage_request)
```

## UI Features

- Interactive graph showing upstream and downstream dependencies
- Expand nodes to see multi-hop lineage
- Lineage layers (data, governance, observability)
- Impact analysis — click any node to see what would break
- Root cause tracing — from dashboard back to broken source table