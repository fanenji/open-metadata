---
type: entity
title: Data Steward Role
created: 2026-05-14
updated: 2026-05-14
tags: [roles, policies, governance, glossary, data-steward]
related: [roles-and-policies, building-blocks-of-authorization---rules-policies--20260514, spel-conditions, glossary-tags, policy-use-cases, persona]
sources: ["use-cases---creating-roles-policies-in-openmetadat-20260514.md"]
---
# Data Steward Role

A Data Steward in OpenMetadata is a governance-focused role responsible for managing business metadata and ensuring data assets are properly described and classified. The role is typically associated with a [[persona|Persona]] that reflects stewardship responsibilities.

## Recommended Policy Configuration

The official documentation prescribes a two-rule policy for Data Stewards:

### Rule 1: Allow Glossary Operations
Grants permission to perform all operations on Glossary and Glossary Term resources. This enables the Data Steward to create, update, and manage the business glossary that underpins data classification.

### Rule 2: Edit Rule
Grants permission to edit descriptions and tags on **all entities** across the platform. This enables the Data Steward to manage metadata for governance purposes — ensuring data assets are accurately described, tagged, and classified.

> **Note:** The Edit Rule can be fine-tuned to suit organizational needs. The broad "all entities" scope may be narrowed to specific resource types if a more constrained governance model is required.

## Relationship to Other Roles

- **Distinct from Admin** — Data Stewards do not need full administrative privileges; their permissions are scoped to metadata management and glossary curation.
- **Complementary to ServiceOwner** — While a [[serviceowner-role|ServiceOwner]] focuses on service creation and ingestion, a Data Steward focuses on the quality and governance of the metadata itself.
- **Works with Organization Policy** — The default [[default-organization-policy|Organization Policy]] enables basic viewing and ownership claims; the Data Steward role adds governance capabilities on top.

## SpEL Conditions

The Data Steward policy typically uses simple Allow rules without complex SpEL conditions, as the role requires broad access for governance. However, conditions can be added to scope permissions to specific domains or teams if needed. See [[spel-conditions]] for available functions.