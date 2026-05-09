---
type: source
title: "Data Contracts: Implementation Guide"
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, data-quality, data-governance, CI-CD]
related: [data-contract-platform, data-contract-versioning-strategy, data-contract-observability, data-product-definition, data-domain-governance, data-discovery-tools, YAML-data-contract-format, CI-CD-for-data-pipelines, jatin-solanki]
sources: ["Data Contracts Implementation Guide.md"]
authors: [Jatin Solanki]
year: 2024
url: "https://aicontext.substack.com/p/data-contracts-implementation-guide"
venue: "Substack"
---
# Data Contracts: Implementation Guide

This guide by [[Jatin Solanki]], founder of [[decube]], presents a practical, process-oriented approach to implementing [[data-contract]]s at scale. The core argument is that data contracts are primarily a cultural and process challenge, not a technical one. The guide provides an 8-step implementation process, a real-life scenario involving a fictional marketing analytics manager named Ryan, and a detailed CI/CD enforcement pattern using Git and YAML.

The guide credits [[Andrew Jones]] as the creator of the data contracts concept, referencing his implementation at [[GoCardless]]. It emphasizes that the biggest barrier to adoption is collaboration and organizational culture, not platform capability.

## Key Concepts

- **[[data-contract]]**: An agreement between data producers and consumers on expected data values, structure, and quality. Violations should break the flow and notify stakeholders.
- **[[data-product]]**: Curated datasets or analytical models designed to meet specific business requirements (e.g., recommender systems, P&L dashboards, marketing dashboards).
- **[[data-domain]]**: Organizational grouping of data assets with assigned ownership.
- **[[data-discovery]]**: The process of identifying and cataloging data assets.
- **[[CI-CD-for-data]]**: Applying software engineering CI/CD practices to data pipelines for enforcement.
- **[[YAML-data-contract]]**: Machine-readable contract definition using YAML format.

## 8-Step Implementation Process

1. Deploy Data Discovery
2. Create Domains & Assign Ownership
3. Add Assets to Domains
4. Create Data Products
5. Filter Assets to Meet Data Product Requirements
6. Apply Validation, Schema, and Metadata Rules
7. Generate YAML File
8. Enforce via GitHub CI/CD

## Enforcement Pattern

The guide describes a Git-based enforcement workflow: feature branching, pull requests with code reviews, CI pipeline checks (YAML linting, schema validation with `yamale` or `jsonschema`, unit tests), documentation and changelog updates, restricted merge access, and deployment to data systems.

## Ownership Model

Data engineers own the data contract, but business stakeholders (data consumers) define the expectations. The contract is written based on business requirements.

## Distinction from Data Catalogs

Data contracts are preventive measures that notify users during code push about downstream impact, whereas data catalogs are discovery tools.

## Platforms Mentioned

- [[decube]] (author's company)
- [[datakitchen]]
- [[dremio]]
- [[datacontract.com]] (open source)