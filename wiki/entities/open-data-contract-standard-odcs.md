---
type: entity
title: Open Data Contract Standard (ODCS)
created: 2026-05-06
updated: 2026-05-06
tags: [data-contracts, standards, governance]
related: [data-contracts, openmetadata]
sources: ["Announcing OpenMetadata 1.12-20260506.md"]
---
# Open Data Contract Standard (ODCS)

The **Open Data Contract Standard (ODCS)** is a standard for defining and exchanging data contracts. OpenMetadata 1.12 introduced support for **ODCS 3.1**, allowing for the import and export of contracts to ensure interoperability across the data ecosystem.

### Integration with OpenMetadata
- **Import/Export**: Supports importing contracts in ODCS 3.1 format and exporting OpenMetadata contracts to ODCS.
- **Enhanced Semantics**: While supporting the standard, OpenMetadata extends the contract specification with additional capabilities such as terms of service, ownership, and quality definitions.
- **Data Product Level**: Supports defining contracts at the data product level with automatic inheritance to all underlying assets.