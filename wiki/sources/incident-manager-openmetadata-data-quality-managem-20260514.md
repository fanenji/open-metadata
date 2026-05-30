---
type: source
title: "Source: incident-manager-openmetadata-data-quality-managem-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["incident-manager-openmetadata-data-quality-managem-20260514.md"]
tags: []
related: []
---

# Source: incident-manager-openmetadata-data-quality-managem-20260514.md

## Analysis of Incident Manager Source Document

### Key Entities

- **Incident Manager** — Central feature/module in OpenMetadata for managing data quality test failures. **Central.** Likely does not exist in the wiki as a dedicated page.
- **Data Quality Test** — The test case whose failure triggers an incident. **Central.** Related to [[data-quality]] concept page.
- **OpenMetadata Platform** — The overall system. **Peripheral context.**
- **Test Resolution Flow** — The workflow process for resolving incidents (notification → acknowledge → assign → status updates → sharing updates). **Central.** Likely does not exist in the wiki.
- **Troubleshooting Handbook** — The accumulated historical record of past incidents used for future reference. **Central concept.** Likely does not exist in the wiki.

### Key Concepts

- **Incident Lifecycle** — The progression from failure detection → automatic incident creation → triage (acknowledge, assign, log root cause) → resolution with reason/comment. **Why it matters:** Defines the core workflow for data quality incident management.
- **Automatic Incident Creation** — When a test case fails, the system automatically opens a new incident and marks it as "new." Severity is auto-assigned but overridable. **Why it matters:** Zero-touch failure capture.
- **Incident Triaging Actions** — Three distinct actions: Acknowledge (awareness), Assign (responsibility via task), Log Root Cause (documentation). **Why it matters:** Structured resolution process.
- **Incident Context & History** — Open incidents show timeline + comments; closed incidents add resolution reason. **Why it matters:** Provides audit trail and learning resource.
- **Troubleshooting Handbook** — Historical incident data used to explore similar scenarios, access contextual information, and drive continuous improvement. **Why it matters:** Transforms incident data into a reusable knowledge base.

### Main Arguments & Findings

- **Core claim:** The Incident Manager centralizes and streamlines data quality issue resolution by automating incident creation, providing structured triage, and preserving historical context.
- **Evidence:** The document describes the feature's functionality (auto-creation, triage actions, resolution flow, history) but provides no empirical data, user studies, or comparative analysis.
- **Evidence strength:** Weak. This is a feature overview/guide, not a research paper. No metrics, benchmarks, or validation.

### Connections to Existing Wiki

- **Directly related to:** [[data-quality]] (the domain), [[data-observability-alerts]] (failure notifications), [[activity-feed]] (timeline/comments display), [[announcements]] (time-bound notifications), [[conversation-threads]] (comments/collaboration on incidents).
- **Extends:** [[data-quality]] by adding the incident management lifecycle as a downstream process after test failures.
- **Strengthens:** The data observability narrative by connecting test failures to actionable workflow
