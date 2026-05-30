---
type: entity
title: Incident Manager
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, incident-manager, data-quality, observability]
related: [incident-dashboard, incident-status-workflow, data-quality, data-observability-alerts, test-cases]
sources: ["how-to-work-with-the-incident-manager-official-doc-20260514.md"]
---

# Incident Manager

The **Incident Manager** is a feature/module in OpenMetadata that provides a structured workflow for managing data quality incidents from detection to resolution. It bridges the gap between data quality test case failures and their formal resolution, enabling teams to track, assign, and close incidents with proper documentation.

## Workflow

The Incident Manager follows a four-step workflow:

1. **Incident Dashboard** — Central hub for viewing and filtering all incidents.
2. **Incident Status Change** — Updating the status of an incident through its lifecycle.
3. **Incident Resolution** — Closing an incident after verifying resolution and documenting Root Cause Analysis (RCA).
4. **Incident Activities** — Viewing the chronological timeline of all events, RCA, and closure updates.

## Integration with Data Quality

The Incident Manager is a downstream component of the [[data-quality]] and [[data-observability-alerts]] system. It consumes test case failures and provides a resolution workflow. Incidents are associated with specific [[test-cases]] and can be filtered by test case.

## Open Questions

- How are incidents created? Automatically from test case failures? Manually?
- What are the exact status transition rules? Can an incident be re-opened after resolution?
- How does the Incident Manager integrate with the existing alerting system ([[data-observability-alerts]])?
- Is there any notification mechanism when an incident is assigned or resolved?