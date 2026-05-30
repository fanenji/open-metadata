---
type: concept
title: Glossary Term Lifecycle
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, lifecycle, data-governance]
related: [glossary-terms, glossary-term-version-history]
sources: ["what-is-a-glossary-term-official-documentation---o-20260514.md"]
---
# Glossary Term Lifecycle

Each glossary term in OpenMetadata has a **life cycle status** that indicates its current state in the governance workflow. The documentation mentions statuses such as **Draft** and **Approved**, but the exact workflow for transitioning between statuses is not fully detailed in the source.

## Known Statuses

- **Draft** — The term is in an initial or work-in-progress state.
- **Approved** — The term has been reviewed and accepted by the designated reviewers.

## Reviewers

A glossary term has a set of **Reviewers** — users who review and accept changes to the glossary for governance. Multiple reviewers can be added to a single term. The reviewers are likely responsible for approving status transitions (e.g., from Draft to Approved).

## Open Questions

- What is the exact workflow for transitioning between statuses (Draft → Approved)?
- Can status transitions be automated or are they always manual?
- How does the lifecycle status interact with the [[glossary-term-version-history]]?
- Is there a rejection or retirement status?

## Related Pages

- [[glossary-terms]] — Core entity that has a life cycle status.
- [[glossary-term-version-history]] — Version tracking that may record lifecycle transitions.