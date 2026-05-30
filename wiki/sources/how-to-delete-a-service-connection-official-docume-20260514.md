---
type: source
title: "How to Delete a Service Connection | Official Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [administration, service-connection, deletion, ui]
related: [service-connection, delete-service-connection, openmetadata-administration]
sources: ["how-to-delete-a-service-connection-official-docume-20260514.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/delete-service-connection"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# How to Delete a Service Connection | Official Documentation

Official documentation page describing the UI procedure for deleting a service connection in OpenMetadata v1.12.x. The source provides a brief two-step workflow: navigate to the service page, click the vertical ellipsis (⋮) menu, select Delete, then type `DELETE` to confirm permanent removal.

This source is part of the Admin Guide section, positioned between "How to Ingest Metadata" and "Manage Teams and Users" in the documentation navigation hierarchy.

## Key Points

- Deletion is performed through the OpenMetadata UI on the service page.
- A two-step confirmation safeguard requires typing the word `DELETE` to prevent accidental removal.
- The source does not address downstream consequences: impact on ingested metadata, associated ingestion pipelines, lineage, or data quality tests.
- The confirmation prompt wording conflates "delete the database" with "delete the service connection," which are distinct concepts.