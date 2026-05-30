---
type: concept
title: Glossary Fully Qualified Name (FQN)
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, fqn, naming-convention]
related: [glossary-overview, glossary-terms, glossary-apis]
sources: ["glossary-openmetadata-data-glossary-guide---openme-20260514.md"]
---
# Glossary Fully Qualified Name (FQN)

The **Fully Qualified Name (FQN)** for glossary terms in OpenMetadata follows a hierarchical naming convention that reflects the term's position within the glossary structure.

## Format

```
glossary.parentTerm.childTerm
```

Where:
- `glossary` — the name of the glossary
- `parentTerm` — the immediate parent term (optional for top-level terms)
- `childTerm` — the specific term being referenced

## Examples

- `BankGlossary.Customer` — a top-level term in the Bank Glossary
- `BankGlossary.Customer.VIPCustomer` — a child term of Customer
- `BusinessGlossary.Revenue.MonthlyRecurringRevenue` — a deeply nested term

## Usage

The FQN is used for:
- **API calls**: Identifying glossary terms in CRUD operations via the [[glossary-apis]]
- **References**: Linking to glossary terms from other parts of the system
- **Uniqueness**: Ensuring each term has a unique, unambiguous identifier within the metadata graph