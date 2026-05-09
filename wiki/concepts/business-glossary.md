---
type: concept
title: Business Glossary
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, governance, glossary, business-terms]
related: [openmetadata, openmetadata-governance, data-domain-governance]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# Business Glossary

A Business Glossary in [[OpenMetadata]] lets organizations define the official meaning of terms across the enterprise. Instead of every team having a different definition of "active user" or "revenue," it is defined once in the glossary, and every data asset can be linked to those official terms.

## Structure

**Glossary** (e.g., "Finance Terms") → **Term** (e.g., "Net Revenue") → Definition, synonyms, related terms, linked assets, owners

When a table column is tagged with a glossary term, anyone viewing that column sees the authoritative definition instantly. This is a core component of [[openmetadata-governance]].