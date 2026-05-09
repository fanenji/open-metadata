---
type: entity
title: OpenMetadata Governance
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, governance, rbac, business-glossary, pii, classification]
related: [openmetadata, openmetadata-data-quality, automated-data-discovery-and-classification, data-domain-governance, data-product-definition]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# OpenMetadata Governance

Governance in OpenMetadata is woven into every part of the platform, covering business glossary, tags, auto-classification, RBAC, ownership, and domains.

## Business Glossary

Define the official meaning of terms across the organization. Structure: **Glossary** (e.g., "Finance Terms") → **Term** (e.g., "Net Revenue") → Definition, synonyms, related terms, linked assets, owners.

## Tags and Classification

Organize assets by any criteria:
- Business domain: `Finance`, `Marketing`, `Product`
- Sensitivity: `PII.Email`, `PII.Phone`, `Confidential`
- Status: `Deprecated`, `Draft`, `Certified`

## Auto-Classification and PII Detection

Automatically scans column names and data samples to detect and tag PII:
- Columns named `email`, `ssn`, `phone_number` → auto-tagged `PII.Sensitive`
- Columns containing patterns matching credit card numbers → auto-tagged `PII.CreditCard`

## Roles and Policies (RBAC)

**Built-in Roles:** Admin, Data Steward, Data Consumer, Data Engineer.

**Custom Roles Example:**
```json
{
  "name": "FinanceDataOwner",
  "policies": [
    {
      "name": "FinanceDataPolicy",
      "rules": [
        {
          "effect": "allow",
          "resources": ["table"],
          "operations": ["ViewAll", "EditDescription", "EditTags"],
          "condition": "inDomain('Finance')"
        }
      ]
    }
  ]
}
```

**Restricting PII Access:**
```json
{
  "name": "SensitiveDataPolicy",
  "rules": [
    {
      "effect": "deny",
      "resources": ["table"],
      "operations": ["ViewAll"],
      "condition": "hasTag('PII.Sensitive') AND !hasRole('DataSteward')"
    }
  ]
}
```

## Ownership

Every asset can be assigned an owner (user or team). Ownership is visible on every asset page, searchable, filterable, enforced in policies, and used in impact alerts.

## Domains and Data Products

- **Domains** map to business functions (Finance, Marketing, Product) with owners, asset collections, and scoped governance policies.
- **Data Products** are curated, named, governed collections of assets representing a business capability (e.g., `Customer 360`, `Revenue Analytics`).