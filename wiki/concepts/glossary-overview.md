---
type: concept
title: Glossary Overview
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, data-governance, controlled-vocabulary, thesauri]
related: [glossary-terms, glossary-fqn, glossary-apis, classification-tags, openmetadata]
sources: ["glossary-openmetadata-data-glossary-guide---openme-20260514.md"]
---
# Glossary Overview

A **Glossary** in OpenMetadata is a **Controlled Vocabulary** — an organized arrangement of words and phrases used to define terminology for organizing and retrieving information. It adds semantics or meaning to data by defining business terminologies, fostering a common and consistent understanding of data across the organization.

## Thesauri Model

OpenMetadata models a glossary as a **Thesauri**, which organizes terms with three types of relationships within a domain:

- **Hierarchical**: Parent-child relationships between terms (e.g., `Customer` > `VIP Customer`)
- **Equivalent**: Synonyms or alternative terms that mean the same thing
- **Associative**: Related terms that are not hierarchical or equivalent but are conceptually linked

This distinguishes OpenMetadata's glossary from a simple flat list of tags.

## Purpose and Benefits

- **Data Governance**: Provides a framework for managing business terminology
- **Data Discovery**: Enables finding data assets through conceptual business terms
- **Collaboration**: Fosters team collaboration with standard, well-defined terms
- **Onboarding**: A well-defined glossary helps new team members get familiar with organizational terminology
- **Consistency**: Ensures consistent understanding of data across departments

## Relationship to Classification Tags

While both glossaries and [[classification-tags]] are used to label data assets, they serve different purposes:

- **Glossary**: Defines business semantics and terminology; organized as a Thesauri with rich relationships
- **Classification Tags**: Governance labels for access control, sensitivity, and data management

Glossary terms can be applied to data assets as additional metadata for describing and categorizing things.

## Access

Glossaries are accessed in the OpenMetadata UI via **Govern >> Glossary**. All glossaries are displayed in the left navigation bar. Clicking a specific glossary shows an expanded view of the entire hierarchy of glossary terms (parent-child terms).