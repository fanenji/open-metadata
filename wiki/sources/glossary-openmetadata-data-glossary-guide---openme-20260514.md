---
type: source
title: "Glossary | OpenMetadata Data Glossary Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, data-governance, controlled-vocabulary]
related: [glossary-overview, glossary-terms, glossary-fqn, glossary-apis, classification-tags, openmetadata]
sources: ["glossary-openmetadata-data-glossary-guide---openme-20260514.md"]
---
# Glossary | OpenMetadata Data Glossary Guide

This source is the official OpenMetadata documentation page for the Glossary feature (v1.12.x). It provides a high-level overview of glossaries as a controlled vocabulary for defining business terminologies, explains the Thesauri model used by OpenMetadata, and introduces the Glossary API entities (Glossary and Glossary Term) with their Fully Qualified Name (FQN) pattern. The page serves as a navigation hub linking to sub-pages on setup, term creation, bulk import, export, approval workflows, styling, and best practices.

Key points:
- A glossary is a controlled vocabulary that adds semantics/meaning to data by defining business terminologies.
- OpenMetadata models glossaries as a Thesauri with hierarchical, equivalent, and associative relationships.
- Glossaries are accessed via Govern >> Glossary in the UI.
- Glossary terms have a fully qualified name in the form `glossary.parentTerm.childTerm`.
- The main API entities are Glossary and Glossary Term, identified by a Unique ID.
- Glossaries facilitate Data Governance, data discovery, retrieval, and exploration.