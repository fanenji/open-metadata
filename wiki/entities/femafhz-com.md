---
type: entity
title: femaFHZ.com
created: 2026-04-29
updated: 2026-04-29
tags: [product, geospatial, hazard, mapping]
related: [scott-parks, cloud-optimized-geotiff-cog, flatgeobuf-fgb, serverless-geospatial-architecture]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# femaFHZ.com

A hazard mapping site created by [[scott-parks]] that displays various peril/hazard layers using a hybrid [[cloud-optimized-geotiff-cog]] and [[flatgeobuf-fgb]] approach. The site demonstrates a practical pattern where low-resolution rasters are used for low zoom levels and high-resolution vectors for high zoom levels. It also uses a server-side virtual raster (VRT) for efficient multi-layer point queries, illustrating that cloud-native is not always the optimal solution.