---
type: concept
title: Data Quality Certification vs Data Usability Certification
created: 2026-04-29
updated: 2026-05-07
tags: [data-quality, certification, governance, medallion-architecture]
related: [data-quality-dimensions, data-quality-score, engineering-led-data-quality, data-lakehouse, data-product-definition, medallion-architecture]
sources: ["Defining Data Quality The Foundation of Modern Data Architecture.md", "if-you-understand-these-5-data-engineering-terms-youre-ahead-of-90-of-the.md"]
---
# Data Quality Certification vs Data Usability Certification

A distinction between two types of data certifications that help consumers understand dataset readiness across the data lifecycle, particularly in the context of the [[medallion-architecture|Medallion Architecture]] (Bronze/Silver/Gold layers).

## Data Quality Certification

- **Focus**: “How good is the data?”
- **Measures**: Accuracy, completeness, reliability of the data.
- **Purpose**: Indicates whether the data is trustworthy and free from errors.

## Data Usability Certification

- **Focus**: “How ready is the data for use?”
- **Measures**: How modeled, standardized, and analysis‑ready the data is.
- **Purpose**: Indicates whether the data has been transformed and structured for consumption.

## Medallion Architecture Mapping

The Bronze/Silver/Gold tiers of the Medallion Architecture map naturally to certification levels, providing a clear, auditable path from raw source to business‑ready data product.

| Layer  | Certification                        | Description                                                                                                                                               |
|--------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bronze | No formal certification              | Raw data, preserved for audit and replay. May have high inherent quality from the source but is unmodeled and not standardized – low usability.           |
| Silver | **Data Quality** certified           | Cleaned, typed, deduplicated, and validated against [[data-quality-dimensions]]. Data is trustworthy and accurate, but may still need further transformation for specific use cases. |
| Gold   | **Data Usability** certified         | Aggregated, pre‑joined, and fully modeled for business consumption. Achieves both high quality and high usability – the dataset is analysis‑ready.         |

These certifications help data consumers understand what they are getting and whether a dataset is appropriate for their needs, without having to inspect the data itself.