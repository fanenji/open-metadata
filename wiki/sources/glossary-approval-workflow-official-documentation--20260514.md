---
type: source
title: "Source: glossary-approval-workflow-official-documentation--20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["glossary-approval-workflow-official-documentation--20260514.md"]
tags: []
related: []
---

# Source: glossary-approval-workflow-official-documentation--20260514.md

## Analysis of "Glossary Approval Workflow | Official Documentation - OpenMetadata Documentation"

### Key Entities

- **Glossary** — Central entity; a business glossary that standardizes terminology. Already exists in the wiki ([[glossary-terms]], [[glossary-tags]]).
- **Reviewers** — Assigned users who approve or reject new glossary terms. Peripheral in this source; not yet a dedicated wiki page.
- **Glossary Term** — Individual term within a glossary; can be in Draft, Approved, or Rejected status. Already exists in the wiki ([[glossary-terms]]).
- **Task** — Assigned to reviewers for approval/rejection; supports discussion and @mentions. Already exists in the wiki ([[tag-request-workflow]] mentions tasks).

### Key Concepts

- **Glossary Approval Workflow** — Automated review process triggered when a new term is added to a glossary that has assigned reviewers. Terms appear as Draft until approved or rejected. If no reviewers are assigned, terms are Approved by default.
- **Draft Status** — Initial state of a new glossary term when reviewers are assigned; visible in the glossary but not yet approved.
- **Approved/Rejected Labels** — Visual indicators on glossary terms after reviewer action.

### Main Arguments & Findings

- **Core claim:** The Glossary Approval Workflow provides governance control by requiring reviewer approval for all new glossary terms.
- **Evidence:** Official documentation; no empirical data or user studies.
- **Strength:** Low — this is a procedural description, not a research finding.

### Connections to Existing Wiki

- **Strengthens:** [[glossary-terms]] — adds the approval workflow dimension to glossary term management.
- **Extends:** [[tag-request-workflow]] — parallels the task-based request/review pattern for classification tags.
- **Related:** [[data-steward-role]] — reviewers are likely data stewards or similar governance roles.

### Contradictions & Tensions

- **Internal tension:** The source does not specify how reviewers are assigned or managed, nor how conflicts between multiple reviewers are resolved (e.g., one approves, another rejects).
- **No contradiction** with existing wiki content found.

### Recommendations

- **Create new page:** `glossary-approval-workflow` — dedicated page covering the workflow, reviewer assignment, status transitions, and task management.
- **Update existing page:** [[glossary-terms]] — add a section on approval workflow and status labels (Draft, Approved, Rejected).
- **Emphasize:** The conditional nature (reviewers required for workflow to trigger) and the default approval behavior when no reviewers exist.
- **De-emphasize:** The video reference (not actionable in text form).
- **Open questions:**
  - How are reviewers assigned to a glossary? (Not covered in this source.)
  - What happens when multiple reviewers disagree?
  - Can reviewers be changed after the workflow is triggered?
  - Is there a notification mechanism for reviewers when a new term is added?
