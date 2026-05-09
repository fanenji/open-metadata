---
type: concept
title: Dremio Row/Column Security
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, security, governance, access-control]
related: [dremio, dremio-vds-pds, openmetadata, data-masking-techniques]
sources: ["Sintesi Architettura (Claude).md"]
---
# Dremio Row/Column Security

Dremio provides fine-grained access control at the row and column level, enabling data governance directly within the virtualization layer. This is a key capability for the Regione Liguria Data Platform's governance requirements.

## Row-Level Security

- **Mechanism**: SQL-based filters applied to datasets based on user/group identity
- **Use cases**: Restricting data access by geographic region, department, or data sensitivity
- **Implementation**: Defined on [[dremio-vds-pds|VDS]] using Dremio's built-in functions and user context variables

## Column-Level Security

- **Mechanism**: Hiding or masking specific columns based on user/group identity
- **Use cases**: PII/PHI protection, financial data restriction, role-based column visibility
- **Implementation**: Column masking policies defined on VDS

## Integration with OpenMetadata

Row/Column security policies defined in Dremio can be documented and governed through [[openmetadata]], providing a unified view of data access controls alongside data lineage and quality information.

## Related Concepts

- [[data-masking-techniques]]: Broader data masking patterns for compliance
- [[data-pseudonymization]]: Reversible de-identification techniques