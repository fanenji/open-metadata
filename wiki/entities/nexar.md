---
type: entity
title: Nexar
created: 2026-05-06
updated: 2026-05-07
tags: [dashcam, mapping, gps, organization, geospatial, data-engineering]
related: [assaf-lavi-2022-complex-geospatial-analytics-with-dbt, assaf-lavi, geospatial-data-stack, h3-geospatial-indexing, geospatial-analytics-with-dbt, openstreetmap-data-model]
sources: ["Complex geospatial analytics with dbt - Summary.md", "Complex geospatial analytics with and dbt - Video Transcript.md", "Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# Nexar

Nexar is a dashcam company that uses massive GPS and vision datasets to create a "digital twin" of the physical world. With approximately 500,000 dashcams deployed on US roads and 4 trillion images collected, they produce large volumes of GPS and vision data used for road intelligence, AI training data for autonomous vehicles, and services for fleets, OEMs, insurance companies, and public sector entities. By indexing road data similarly to how search engines index the web, Nexar provides road intelligence APIs, detecting road blockages, traffic slowdowns, and parking availability.

## Data Engineering Challenge

A core engineering challenge is quantifying supply: given a specific geographic area, does Nexar have enough data to provide a service to a customer? This requires enriching noisy, raw GPS coordinates with semantic geographic dimensions (e.g., road types, city boundaries, county, state) to answer complex business questions.

## Technology Stack

- **Storage:** Amazon S3 (Parquet/ORC)
- **Warehouse:** Snowflake
- **Transformation:** dbt
- **BI:** Looker
- **Preprocessing:** PySpark (for H3 enrichment, OSM parsing, map matching)