---
type: entity
title: Glossary API
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, api, glossary, data-governance]
related: [glossary-overview, glossary-terms, glossary-fqn, openmetadata]
sources: ["glossary-openmetadata-data-glossary-guide---openme-20260514.md"]
---
# Glossary API

OpenMetadata provides extensive Glossary APIs for programmatic management of glossaries and glossary terms. The main entities are **Glossary** and **Glossary Term**, each identified by a Unique ID.

## Key Characteristics

- **Entities**: Glossary and Glossary Term
- **Identification**: Unique ID per entity
- **Fully Qualified Name (FQN)**: `glossary.parentTerm.childTerm`
- **Operations**: Create, Read, Update, Delete (CRUD)

## Usage

The Glossary API enables automation of glossary management tasks such as:
- Creating and managing glossaries
- Adding, updating, and deleting glossary terms
- Retrieving terms by FQN or Unique ID
- Integrating glossary operations into CI/CD pipelines

For detailed API documentation, refer to the official OpenMetadata Glossary API documentation.