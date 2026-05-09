---
type: synthesis
title: HEX_EGG Table
created: 2026-05-08
updated: 2026-05-08
tags: [geospatial, dbt, h3, data-model, nexar, spatial-aggregation, synthesis]
related: [h3-geospatial-indexing, geospatial-analytics-with-dbt, nexar, elt-pattern, data-lakehouse, dbt, iceberg-table-versioning, dremio-geospatial-limitations, dbt-osmosis, data-contract-implementation, dbt-insert-by-period, dbt-expectations, dbt-observability-implementation, count-co]
sources: ["research-hexegg-table-2026-05-08.md", "Complex geospatial analytics with dbt - Summary-20260507.md", "dbt-osmosis Automation for Schema and Documentation Management in dbt.md"]
---
# HEX_EGG Table

The **HEX_EGG Table** is a spatial data model pattern for aggregating large-scale, streaming geospatial event data into a consistent, analysis-ready format using the [[h3-geospatial-indexing]] system. It serves as a critical intermediate or fact table bridging raw point-level events and analytical aggregates.

## Etymology and Acronym

- **HEX**: Directly references Uber's **H3** hierarchical hexagonal spatial indexing system.
- **EGG**: No formal expansion found in available literature. Most plausibly interpreted as **E**vent **G**eometry **G**rid** or **E**ntity **G**eographic **G**rid**. This naming follows the pattern of converting individual telemetry events into standardized hexagonal cells.

> **Note**: The lack of a canonical definition for "EGG" represents a knowledge gap. It may be a local naming convention from a specific organization (e.g., Nexar) or a project-internal abbreviation.

## Architecture and Data Flow

The HEX_EGG table operates within a modern [[data-lakehouse]] employing the [[elt-pattern]] with [[dbt]] as the primary transformation engine.

1. **Ingestion**: Raw geospatial data streams (GPS coordinates, video metadata, incident events) are ingested into the lakehouse.
2. **H3 Conversion**: Raw latitude/longitude points are mapped to H3 cell IDs using standard library functions. Multiple resolutions can be materialized simultaneously (e.g., Resolution 8 for city districts, Resolution 12 for building blocks).
3. **Materialization**: Data is materialized as the HEX_EGG table in the lakehouse (e.g., [[iceberg-table-versioning]]), serving as the bridge between raw point-level data and analytical aggregates.
4. **Transformation and Aggregation**: Downstream dbt models query the HEX_EGG table to produce domain-specific aggregates: trip counts per zone, average speed per cell, incident frequency, or supply-demand density maps.
5. **Metadata and Observability**: Metadata descriptions from the dbt project are pushed to the warehouse and surfaced in analytics tools like [[count-co]]'s Hex platform. [[dbt-observability-implementation]] patterns track run metadata and test results.

## Schema and Structure

| Column | Type | Description |
|---|---|---|
| `event_id` | STRING / UUID | Unique identifier for the source event |
| `h3_cell_index` | BIGINT | H3 cell index in canonical integer form |
| `h3_cell_string` | TEXT | Hex string representation of the H3 cell |
| `resolution` | INTEGER | H3 resolution level (0–15) |
| `event_timestamp` | TIMESTAMP | Time the event was generated |
| `geometry` | GEOGRAPHY | WKT/WKB representation of the hexagon boundary |
| `source_entity_id` | STRING | Identifier for the generating device or source |

## Use Cases

- **Large-Scale Telematics**: Nexar processes ~500K dashcam devices; H3 hexagons enable efficient joining without complex geometric comparisons.
- **Urban Mobility Analysis**: Aggregate trip volumes, congestion patterns, or safety incidents at neighborhood or city scale.
- **Supply & Demand Mapping**: Ride-hailing and logistics use cases benefiting from H3's consistent global tessellation.

## Integration with dbt and Data Quality

- **Testing**: The table is a natural target for [[data-quality-dimensions]] enforcement via dbt. Packages like [[dbt-expectations]] provide statistical anomaly detection on cell occupancy.
- **Incremental Models**: Frequently modeled as a dbt incremental model using timestamp-based or [[dbt-insert-by-period]] strategies.
- **Observability**: [[dbt-observability-implementation]] patterns (e.g., `on-run-end` hooks) track run metadata; dbt Cloud's integration with Hex surfaces test failures and freshness.

## Limitations and Considerations

- **Acronym Ambiguity**: The specific expansion of "EGG" is not documented — a formal knowledge gap.
- **Grid System Arbitrariness**: H3 cells do not align with natural geographic or political boundaries, which can misrepresent data.
- **Storage and Performance**: High-resolution H3 cells at scale require careful partitioning and clustering within the lakehouse.
- **Dremio Limitations**: In stacks using [[dremio]], geospatial functions may be limited, requiring UDF workarounds like [[dremio-udf-gis]] or transitioning to DuckDB/Iceberg-native queries (see [[dremio-geospatial-limitations]]).

## Cross-Referencing

- [[h3-geospatial-indexing]] — The core indexing system powering the HEX dimension
- [[geospatial-analytics-with-dbt]] — The architectural pattern this table supports
- [[nexar]] — Primary case study organization using this pattern at scale
- [[data-lakehouse]] — The storage and compute infrastructure context
- [[dbt]] — The transformation layer
- [[iceberg-table-versioning]] — The table format enabling safe data versioning
- [[dremio-geospatial-limitations]] — Known limitations of the query engine in this stack
- [[dbt-osmosis]] — Tool for automated YAML and documentation synchronization
- [[data-contract-implementation]] — How contracts govern the schema of this table