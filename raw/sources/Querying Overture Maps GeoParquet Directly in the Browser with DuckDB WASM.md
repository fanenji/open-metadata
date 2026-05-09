---
title: Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM
source: https://dev.to/camptocamp-geo/querying-overture-maps-geoparquet-directly-in-the-browser-with-duckdb-wasm-4jn4
author:
  - "[[Florent Gravin]]"
published: 2025-05-16
created: 2026-04-08
description: Overture Maps provides a rich, open and collaborative dataset of geospatial features that’s designed... Tagged with geoparquet, duckdb, cloudnative, overturemaps.
tags:
  - clippings
  - mapping
  - duckdb
  - geoparquet
topic:
type: note
---
[Overture Maps](https://overturemaps.org/) provides a rich, open and collaborative dataset of geospatial features that’s designed to power everything from routing to visualization. These datasets are distributed in [GeoParquet](https://geoparquet.org/) format: **cloud-native**, efficient, columnar, and increasingly becoming a standard for geospatial data at scale.

But what if you could explore and query these massive datasets directly in your browser - **without any server-side processing or backend setup**? Thanks to [DuckDB-WASM](https://duckdb.org/docs/stable/clients/wasm/overview.html), you can.

- [Demo](https://fgravin.github.io/overture-duckdb-wasm/)
- [Code](https://github.com/fgravin/overture-duckdb-wasm)

In this post, we’ll walk through how to:

- Load an Overture Maps GeoParquet file into the browser
- Query it using SQL, right from the front-end
- Visualize features on a map

Let’s dive in. 🦆

---

## Tools and Technologies

- **DuckDB-WASM**: A full DuckDB engine compiled to WebAssembly, enabling in-browser analytics.
- **GeoParquet**: Parquet format with additional metadata to support geometry and spatial operations.
- **Overture Maps**: A collaborative open map dataset from companies like Meta, Microsoft, Amazon, and TomTom.
- **MapLibre GL JS**: For rendering geospatial features.

---

## Step 1: Load DuckDB WASM

Include DuckDB-WASM in your HTML or install it via npm:  

```
npm install @duckdb/duckdb-wasm
```

And initialize it:  

```
import * as duckdb from '@duckdb/duckdb-wasm'
import duckdb_wasm from '@duckdb/duckdb-wasm/dist/duckdb-mvp.wasm?url'
import mvp_worker from '@duckdb/duckdb-wasm/dist/duckdb-browser-mvp.worker.js?url'
import duckdb_wasm_next from '@duckdb/duckdb-wasm/dist/duckdb-eh.wasm?url'
import eh_worker from '@duckdb/duckdb-wasm/dist/duckdb-browser-eh.worker.js?url'

const MANUAL_BUNDLES = {
  mvp: {
    mainModule: duckdb_wasm,
    mainWorker: mvp_worker,
  },
  eh: {
    mainModule: duckdb_wasm_next,
    mainWorker: eh_worker,
  },
}

const bundle = await duckdb.selectBundle(MANUAL_BUNDLES)
const worker = new Worker(bundle.mainWorker)
const db = new duckdb.AsyncDuckDB(logger, worker)
await db.instantiate(bundle.mainModule, bundle.pthreadWorker)
```

---

## Step 2: Fetch and Load the GeoParquet File

**Disclaimer**: As DuckDB WASM [does not support HTTPFS extension](https://duckdb.org/docs/stable/clients/wasm/extensions.html#httpfs) you can't directly hint the official Overture Maps GeoParquet releases, which provide root level S3 file system entry.  
You should extract a subset of the datasets and host them in your web application, you could use the [Python CLI](https://docs.overturemaps.org/getting-data/overturemaps-py/) for that.

Then, load the spatial extension to process the GeoParquet, and init your DuckDB connection.  

```
conn.query('INSTALL spatial;LOAD spatial;')
conn.query('INSTALL h3 FROM community;LOAD h3;')
const conn = await db.connect()
```

---

## Step 3: Query Your Data

Run SQL queries directly in the browser:  

```
const res = await conn.query(\`
WITH areas AS (
  SELECT names.primary as name,
         geometry as area_geom
  FROM read_parquet('https://your.parquet.path/division_area.parquet', filename=true, hive_partitioning=1) 
  WHERE subtype = 'locality'
    AND region = 'US-UT'
),
schools AS (SELECT geometry as place_geom
  FROM read_parquet('https://your.parquet.path/places.parquet', filename=true, hive_partitioning=1) 
  WHERE categories.main = 'hotel'
)
SELECT name, ST_AsGeoJSON(area_geom) as geometry,
       CAST(count(place_geom) as INT) as count
FROM areas
       LEFT JOIN schools ON ST_Contains(area_geom, place_geom)
GROUP BY area_geom, name
\`)
```

This query fetches Overture division areas of Utah, and performs a spatial aggregation, it counts every hotel within each locality.

---

## Step 4: Visualize on a Map

Convert geometries to GeoJSON and render them:  

```
const data = {
  type: 'FeatureCollection',
  features: res.toArray().map((d: DuckResponseObject) => {
    const { geometry, ...properties } = d
    return {
      type: 'Feature',
      geometry: JSON.parse(geometry) as Polygon,
      properties,
    }
  }),
}

map.addSource('places-area-sources', {
  type: 'geojson',
  data,
})

map.addLayer({
  id: 'places-area',
  type: 'fill',
  source: 'places-area-sources',
  paint: {
    'fill-color': ['interpolate', ['linear'], ['get', 'count'], ...colorGradient],
    'fill-outline-color': 'grey',
    'fill-opacity': 0.8,
  },
})
```

Where `colorGradient` is a computed classification depending on count distribution.

Et voila! You have a beautiful choropleth map, from Overture Maps datasets, with no backend implied 👏

[![Hotel distribution per county in Utah, from Overture Maps division areas and places datasets](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvlcezwowkym3ddzukqni.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvlcezwowkym3ddzukqni.png)[MongoDB](https://dev.to/mongodb)Promoted

[![Build seamlessly, securely, and flexibly with MongoDB Atlas. Try free.](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FVYTIlUE.png)](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_devto-broad_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=devto&utm_medium=display&utm_content=runappsanywhere-v1&bb=241235)

## Build seamlessly, securely, and flexibly with MongoDB Atlas. Try free.

MongoDB Atlas lets you build and run modern apps in 125+ regions across AWS, Azure, and Google Cloud. Multi-cloud clusters distribute data seamlessly and auto-failover between providers for high availability and flexibility. Start free!