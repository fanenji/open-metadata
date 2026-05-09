---
type: entity
title: Proj4j
tags: [proj4j, library, geospatial, crs, projection, coordinate-system]
related: [apache-sedona, projs-library]
sources: ["Apache Sedona Coordinate Transform.md", "Apache Sedona Coordinate Transform-20260506.md"]
created: 2026-02-13
updated: 2026-05-06
---
# Proj4j

**Proj4j** is a lightweight Java port of the PROJ.4 library. It is used as a core dependency in [[apache-sedona]] to handle Coordinate Reference System (CRS) transformations via the `ST_Transform` function.

## Characteristics and Constraints
- **Lightweight**: Designed for ease of integration within Java/Scala environments like Spark.
- **Limitations**: It does not implement the full feature set of the standard **PROJ** library. Most notably, it lacks support for advanced transformation methods such as the use of **.gsb** grid files for high-precision datum shifts.

## Impact on GIS Workflows
Because Proj4j is the engine behind Sedona's `ST_Transform` function, the lack of grid file support directly impacts the precision of spatial transformations possible within a native Sedona environment. Any transformation requiring specialized grid files must be handled outside of the Sedona environment via a [[spatial-pre-processing-pattern]].