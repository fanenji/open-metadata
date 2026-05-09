---
type: concept
title: Data Warehouse as Public Institution
created: 2026-05-07
updated: 2026-05-07
tags: [data-warehouse, governance, participation, data-mesh]
related: [data-engineering-definition, data-engineer-as-librarian, data-engineer-as-center-of-excellence, data-mesh, monolithic-data-lake, data-quality-certification-vs-usability-certification, maxime-beauchemin]
sources: ["The Rise of the Data Engineer.md"]
---
# Data Warehouse as Public Institution

A concept from Maxime Beauchemin's 2017 manifesto describing the modern data warehouse as a "more public institution" that welcomes data scientists, analysts, and software engineers to participate in its construction and operation. This contrasts with the historical model where only BI engineers managed the warehouse.

## Characteristics

- **Open participation:** Multiple roles contribute to the warehouse's construction and operation.
- **Chaotic and imperfect:** The open model results in a more chaotic, shape-shifting, imperfect piece of infrastructure.
- **Certified core areas:** The data engineering team owns pockets of certified, high-quality areas with defined SLAs, naming conventions, and best practices.
- **Governance challenges:** The tension between openness and quality requires active governance.

## Implications

- Data is too central to the company's activity to restrict who can manage its flow.
- The model allows scaling to match the organization's data needs.
- It requires data engineers to act as librarians, certifiers, and educators.
- It creates a tension between openness and governance control that must be managed.

## Relationship to Data Mesh

This concept is a precursor to [[data-mesh]] principles, particularly domain ownership and federated governance. The "public institution" warehouse anticipates the decentralized, participatory model of data mesh, though without the formal domain boundaries and self-serve platform that data mesh prescribes.

## Connections

- [[data-engineering-definition]] — Context for the role
- [[data-engineer-as-librarian]] — Managing the public institution
- [[data-engineer-as-center-of-excellence]] — Setting standards for the public institution
- [[data-mesh]] — Later evolution of the participatory model
- [[monolithic-data-lake]] — Contrasting centralized model
- [[data-quality-certification-vs-usability-certification]] — Related to certified core schemas
- [[maxime-beauchemin]] — Author of the concept