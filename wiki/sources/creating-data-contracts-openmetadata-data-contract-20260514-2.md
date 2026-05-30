---
type: source
title: "Source: creating-data-contracts-openmetadata-data-contract-20260514-2.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["creating-data-contracts-openmetadata-data-contract-20260514-2.md"]
tags: []
related: []
---

# Source: creating-data-contracts-openmetadata-data-contract-20260514-2.md

## Analysis of: creating-data-contracts-openmetadata-data-contract-20260514-2.md

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| Data Contract | Entity/Concept | Central — the core subject of the document | **No** |
| OpenMetadata | Platform | Central — the system implementing data contracts | Yes |
| Table | Asset Type | Central — the only asset type currently supported for contracts | Yes (implied) |
| JSON Schema | Schema Definition | Central — defines the contract entity structure | Yes (jsonschemas) |
| Data Quality | Feature | Central — contracts built on top of native DQ features | Yes (data-quality) |
| Glossary | Feature | Peripheral — referenced for approval workflow analogy | Yes (glossary-terms) |
| PII.Sensitive | Tag | Peripheral — example security classification | Yes (pii-sample-data-masking) |
| General.Person | Tag | Peripheral — example semantic tag | Yes (classification-tags) |

### Key Concepts

| Concept | Definition | Importance | In Wiki? |
|---------|------------|------------|----------|
| Data Contract | Formal, machine-readable agreement between data producers and consumers about schema, semantics, quality, SLAs, and security | **Core innovation** — brings API-contract-like standardization to data assets | **No** |
| Contract Status | Tri-state lifecycle: DRAFT → ACTIVE → VIOLATED | Central to contract enforcement and observability | **No** |
| Schema Section | Expected structural schema (fields, data types) — subset of available fields | Captures agreed-upon column structure | **No** |
| Semantics Section | Business meaning requirements (description, owner, domain) | Ensures contracts carry business context beyond technical schema | **No** |
| Security Section | Access policy references and required classification labels | Links contracts to RBAC/ABAC and tag-based governance | **No** |
| Quality (Assertions) Section | Data quality tests that must pass for compliance | Bridges contracts to existing Data Quality framework | **No** |
| SLA Section | Refresh frequency, max latency, availability time, retention | Codifies timeliness and lifecycle expectations | **No** |
| Terms of Use Section | Allowed/disallowed uses, compliance requirements (GDPR, HIPAA) | Captures legal/regulatory constraints | **No** |
| Approval Workflow | Review process for contract changes (analogous to Glossaries) | Ensures governance over contract modifications | **No** |

### Main Arguments & Findings

- **Core claim**: Data contracts formalize producer-consumer agreements in a machine-readable, enforceable format, bringing standardization and reliability to data ecosystems.
- **Evidence**: The document provides a complete JSON Schema design, YAML example, and explicit mapping to existing OpenMetadata features (Data Quality, Classification, RBAC).
- **Strength**: Strong — this is official documentation from OpenMetadata v1.12.x, providing a concrete specification with implementation details.

### Connectio
