---
type: concept
title: Glossary Term Version History
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, versioning, data-governance]
related: [glossary-terms, change-events-system, audit-logs]
sources: ["what-is-a-glossary-term-official-documentation---o-20260514.md"]
---
# Glossary Term Version History

Glossary terms in OpenMetadata maintain a version history that tracks all changes over time. The version number is displayed in the UI, and clicking on it reveals the details of each version.

## Versioning Rules

- **Backward compatible changes** result in a **Minor version change** (+0.1). Examples include changes to:
  - Description
  - Tags
  - Ownership
- **Backward incompatible changes** result in a **Major version change** (+1.0). An example is:
  - Term deletion

## Examples

- A change to the description of a term increases the version from 0.1 to 0.2 (minor).
- Deleting a term increases the version from 0.2 to 1.2 (major).

## Viewing Version History

The version history can be viewed from the top right of the glossary term detail page. Clicking on the version number displays the details of the version history, including what changed and when.

## Relationship to Change Events

The version history is likely powered by the [[change-events-system]], which captures all metadata changes. Each version corresponds to a change event that was recorded and stored.

## Related Pages

- [[glossary-terms]] — Core entity that maintains version history.
- [[change-events-system]] — Event capture mechanism that likely underpins version tracking.
- [[audit-logs]] — Compliance and security records that complement version history.