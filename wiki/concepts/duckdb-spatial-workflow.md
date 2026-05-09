---
type: concept
title: DuckDB Spatial Workflow
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, geospatial, workflow, spatial]
related: [duckdb, duckdb-spatial-extension, duckdb-execution-model, duckdb-python-integration, cloud-native-geospatial-workflow, geospatial-analytics-with-dbt]
sources: ["DuckDB Spatial Supercharged Geospatial SQL - Summary.md"]
---
# DuckDB Spatial Workflow

An end-to-end pattern for geospatial analysis using [[duckdb-spatial-extension]], demonstrated with the NYC taxi dataset (1 million rides).

## Step 1 — Load and Inspect

```python
import duckdb

duckdb.sql("INSTALL spatial; LOAD spatial;")

# Scan parquet file as a relation (lazy)
rides = duckdb.read_parquet("nyc_taxi.parquet")

# Inspect schema
duckdb.sql("SUMMARIZE rides").show()
```

## Step 2 — Create Geometry Columns

Convert raw lat/lon columns to geometry using `ST_Point`, then reproject from WGS84 (EPSG:4326) to a local NYC CRS (EPSG:102718, in feet) using `ST_Transform`.

Uses the [[duckdb-python-integration]] Relational API expression builder for programmatic composition.

## Step 3 — Spatial Data Cleaning

Use `ST_Distance` to detect impossible rides (aerial distance > reported trip distance):

```python
dist_expr = FunctionExpression("ST_Distance",
    ColumnExpression("pickup_geom"),
    ColumnExpression("dropoff_geom")
) / 5280

rides = rides.select("*", dist_expr.alias("aerial_distance_mi"))

# Count suspicious rides
rides.filter("trip_distance < aerial_distance_mi").count().show()
# → 65,000 out of 1,000,000 rides (6.5% — very dirty dataset)

# Filter them out
clean_rides = rides.filter("trip_distance >= aerial_distance_mi")
```

## Step 4 — Read Shapefiles and Spatial Join

```python
# List GDAL drivers
duckdb.sql("SELECT * FROM ST_Drivers()").show()

# Read shapefile (calls GDAL internally)
zones = duckdb.sql("SELECT * FROM ST_Read('taxi_zones.shp')")

# Spatial join: assign each ride to its dropoff zone
result = clean_rides.join(
    zones,
    "ST_Within(dropoff_geom, zones.geometry)"
).aggregate(
    "zone_name, COUNT(*) AS trip_count, zones.geometry",
    "zone_name, zones.geometry"
).order("trip_count DESC")
```

## Step 5 — Visualize with GeoPandas

```python
# Convert geometry to WKT for GeoPandas compatibility
result_wkt = result.select(
    "zone_name",
    "trip_count",
    "ST_AsText(geometry).alias('geometry_wkt')"
)

# To GeoPandas
import geopandas as gpd
from shapely import wkt

df = result_wkt.to_df()
df["geometry"] = df["geometry_wkt"].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry="geometry")
gdf.plot(column="trip_count", legend=True)
```

## Performance Considerations

- For datasets fitting in RAM (e.g., 1M rows), GeoPandas alone is comparably fast
- DuckDB Spatial's advantage grows with larger datasets, complex multi-join queries, or when data doesn't fit in memory
- The sweet spot is large datasets that don't fit in memory, complex multi-table spatial queries, and local analytics without infrastructure

## Comparison with Cloud-Native Workflow

This in-process workflow complements the [[cloud-native-geospatial-workflow]] pattern. DuckDB Spatial is ideal for local, interactive analysis without infrastructure, while the cloud-native approach (remote GeoParquet with DuckDB) is better for distributed or shared datasets.
