---
type: concept
title: Static vs. Dynamic Content Tradeoff in Cloud-Native Geospatial
created: 2026-04-29
updated: 2026-04-29
tags: [pattern, architecture, geospatial, cloud-native]
related: [serverless-geospatial-architecture, cloud-optimized-geotiff-cog, femafhz-com]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Static vs. Dynamic Content Tradeoff in Cloud-Native Geospatial

A key architectural consideration for cloud-native geospatial systems: purely cloud-native data pushes dynamic spatial analysis onto the web client, which is ideal in theory but not always practical.

## The Tradeoff

- **Static content**: Cloud-native formats (COG, FGB) are excellent for serving pre-processed data directly to clients.
- **Dynamic content**: Complex spatial analysis (e.g., querying 14 different perils for a single lat/lon) is more efficiently handled server-side.

## Example from Postholer

On femaFHZ.com, users can double-click on the map to retrieve 14 different perils for that location. Using purely cloud-native data, the web app would make 14 separate COG requests and process the results client-side. Instead, [[scott-parks]] uses a server-side virtual raster (VRT) containing all 14 COGs. The user's lat/lon is sent via a simple web service, the VRT is queried, and all 14 results are returned in a single fast response.

## Implication

A purely serverless architecture is not always the best choice. The decision depends on the complexity of the spatial analysis required and the number of data layers involved.