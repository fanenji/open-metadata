---
type: concept
title: Integration Testing without Mocking
created: 2024-05-22
updated: 2024-05-22
tags: [testing, reliability, spatial-data]
related: [pytest, docker, ogr2ogr]
sources: ["CONCONVERSIONI GROOVY -> PYTHON.md"]
---
# Integration Testing without Mocking

A strategy for testing complex ETL pipelines by using real, containerized database instances (PostgreSQL and Oracle) instead of software mocks. This approach is essential for capturing "peculiar cases" in spatial workflows, such as:
- OGR2OGR failures.
- Database timeouts.
- Invalid spatial geometries.

While more resource-intensive and slower than unit testing with mocks, it provides much higher confidence in the reliability of the spatial transformation process.