---
type: entity
title: georaster-layer-for-leaflet
created: 2026-04-29
updated: 2026-04-29
tags: [tool, javascript, leaflet, COG, geospatial]
related: [cloud-optimized-geotiff-cog, leaflet, serverless-geospatial-architecture, daniel-dufour]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# georaster-layer-for-leaflet

A JavaScript API created by [[daniel-dufour]] for displaying Cloud Optimized GeoTIFFs (COGs) in Leaflet maps. This library is the critical client-side component that enables [[postholer]]'s serverless geospatial architecture, allowing COG data to be fetched directly from S3 and rendered in the browser without any intermediate tile server.

## Usage

The library leverages HTTP range requests to stream only the necessary portions of a COG file, enabling efficient display of large raster datasets in the browser. It is the primary tool used by [[scott-parks]] for raster layer display in his Leaflet maps.