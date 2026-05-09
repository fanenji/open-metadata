---
type: concept
title: GDAL as Technology Gatekeeper
created: 2026-04-29
updated: 2026-04-29
tags: [heuristic, technology-selection, geospatial, GDAL]
related: [cloud-optimized-geotiff-cog, flatgeobuf-fgb, legacy-geospatial-etl-pipeline]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# GDAL as Technology Gatekeeper

A heuristic for technology selection in geospatial systems: if GDAL recognizes a format or supports a concept, it indicates the technology has reached critical mass and is likely to be around tomorrow. If GDAL does not support it, the format or concept may never achieve widespread adoption.

## Origin

[[scott-parks]] describes this as his first stop when evaluating new spatial formats or concepts. He explicitly avoids being the first to introduce new or "next big thing" technologies into production, preferring proven and tested technologies.

## Implications

- **Positive signal**: GDAL support for [[cloud-optimized-geotiff-cog]] and [[flatgeobuf-fgb]] confirmed their maturity for production use.
- **Negative signal**: A format without GDAL support is unlikely to be adopted by [[scott-parks]].
- **Risk management**: This heuristic reduces the risk of investing in technologies that may not be supported in the future.