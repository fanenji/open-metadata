---
type: concept
title: Incident Status Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, incident-manager, workflow, lifecycle]
related: [incident-manager, incident-dashboard, data-quality]
sources: ["how-to-work-with-the-incident-manager-official-doc-20260514.md"]
---

# Incident Status Workflow

The **Incident Status Workflow** defines the lifecycle of a data quality incident in OpenMetadata. Incidents progress through a series of statuses from creation to resolution.

## Statuses

- **New** — The incident has been created and is awaiting acknowledgment.
- **ACK** — The incident has been acknowledged by a team member.
- **Assigned** — The incident has been assigned to a specific team member for resolution.
- **Resolved** — The incident has been resolved and closed, with Root Cause Analysis (RCA) documented.

## Status Transitions

The documented workflow suggests a linear progression: New → ACK → Assigned → Resolved. However, the exact transition rules and whether re-opening or escalation is supported are not documented in the source material.

## Root Cause Analysis (RCA)

When an incident is resolved, a Root Cause Analysis (RCA) must be documented in the resolution comments. This provides context and understanding of the resolution process for future reference.

## Open Questions

- Can an incident go from "Resolved" back to "New" or "Assigned"?
- What happens if an incident is not acknowledged (ACK)?
- Are there any time-based escalations for unassigned incidents?