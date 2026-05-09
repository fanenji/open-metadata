---
type: source
title: "Complex geospatial analytics with dbt - Video Transcript"
created: 2026-05-06
updated: 2026-05-06
tags: ["mapping", "dbt", "geospatial", "h3", "snowflake", "openstreetmap", "nexar"]
related: ["dbt-best-practices", "geospatial-data-stack", "spatial-pre-processing-pattern", "h3-spatial-indexing", "spatial-to-integer-conversion"]
sources: ["Complex geospatial analytics with dbt - Summary.md", "Complex geospatial analytics with dbt - Video Transcript.md"]
authors: [Assaf Lavi]
year: 2022
url: "https://www.youtube.com/watch?v=UCEFHXUBqr0"
venue: "Big Things"
---
# Complex geospatial analytics with dbt - Video Transcript

A technical presentation by Assaf Lavi (Principal Engineer at Nexar) detailing how to handle massive-scale geospatial datasets using dbt, Snowflake, and the H3 hexagonal hierarchical spatial index.

## Key Takeaways

### 1. The Problem: Scale and Complexity
* **Raw GPS Data is Messy**: GPS traces are imprecise and require map-matching to road networks.
* **Computational Expense**: Traditional geospatial operations like `point-in-polygon` are too expensive for billions of GPS samples.
* **Semantic Ambiguity**: Names like "Detroit" or "Jerusalem" can be ambiguous without stable, hierarchical identifiers.

### 2. The Solution: Integer-Based Geospatialism
* **H3 Spatial Indexing**: By converting complex geometries into H3 hexagonal cells (represented as integers), expensive geometric computations are replaced by high-performance integer equality checks and joins.
* **Pre-processing**: Use Apache Spark to enrich OpenStreetMap (OSM) and Who's on First (WOF) data with H3 indices *before* loading into the data warehouse.
* **Hex-Road Segment Join**: A pattern that combines H3 hexagons with OSM road segments to provide both spatial granularity and road topology (directionality, road type).

### 3. dbt Engineering Patterns
* **Development Workflow**: Using Snowflake's **Zero-Copy Cloning** to create isolated, full-scale development environments from production schemas.
* **Materialization Strategies**:
    * **Incremental**: Standard approach for processing new data.
    * **Insert by Period**: An advanced strategy for partitioned data, processing data in chunks (periods) to handle massive backfills efficiently, provided there is no late-arriving data.
* **Optimization**: Using **Manual Clustering** in Snowflake (e.g., by date or OS version) to enable partition pruning and accelerate incremental runs.
* **UDF Management**: Using dbt to manage and deploy SQL-based UDFs for bitwise H3 operations (e.g., traversing between H3 resolutions).

### 4. Data Enrichment Sources
* **OpenStreetMap (OSM)**: Provides the road network topology (nodes, ways, relations).
* **Who's on First (WOF)**: Provides stable, hierarchical geographic identifiers (countries, regions, cities) and population metadata.
