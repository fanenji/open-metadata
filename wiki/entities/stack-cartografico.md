---
type: entity
title: Stack Cartografico
created: 2026-05-07
updated: 2026-05-07
tags: [geospatial, gis, spatial-analysis, visualization]
related: [duckdb-spatial-extension, postgis, geoarrow, jupyter, dremio, apache-superset, bronze-silver-gold-architecture]
sources: ["Sintesi Architettura (Claude).md"]
---
# Stack Cartografico

The Stack Cartografico is the collection of geospatial libraries and components integrated into the Regione Liguria Data Platform for spatial data analysis and visualization. It operates alongside the core data lakehouse architecture.

## Components

| Component | Role |
|---|---|
| **GDAL** | Raster/vector format conversion (COG, GeoParquet) |
| **DuckDB Spatial** | In-process geospatial analytical queries (PostGIS-like functions) |
| **GeoPandas** | Python spatial analysis (buffer, intersection, union) |
| **Leafmap** | Interactive cartographic visualization in Jupyter |
| **deck.gl** | WebGL2 rendering of large geographic datasets |
| **PBI-Carto** | Custom component for thematic maps in Power BI + WMS |

## Integration Points

- **Jupyter**: GeoPandas and Leafmap provide interactive geospatial analysis in [[jupyter]] notebooks
- **DuckDB Spatial**: In-process query engine for geospatial analytics on data from the [[bronze-silver-gold-architecture|Data Lake]]
- **Power BI**: PBI-Carto enables thematic map visualizations
- **Dremio**: Geospatial data can be queried through [[dremio]]'s SQL interface
- **Apache Superset**: Alternative BI visualization for geospatial dashboards