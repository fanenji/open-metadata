---
type: source
title: "How to Assign or Change Data Ownership - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-ownership, governance, teams]
related: [data-asset-ownership, owner-propagation, teams-and-users, team-types, data-steward-role]
sources: ["how-to-assign-or-change-data-ownership---openmetad-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/data-ownership"
venue: "OpenMetadata Documentation"
---

# How to Assign or Change Data Ownership - OpenMetadata Documentation

Official OpenMetadata v1.12.x documentation covering the assignment and change of data asset ownership. The source defines the concept of data asset ownership, the assignment and change procedures (Admin-only), the top-down owner propagation mechanism (Database → Schema → Table), and the recommendation that team ownership (specifically Groups) is preferred over individual user ownership.

Key points:
- Only Admin users can assign or change data ownership.
- Ownership can be assigned to a Team (preferred) or a User.
- Only teams of type 'Groups' can own data assets.
- Owner propagation follows a top-down hierarchy: Database → Database Schema → Table.
- Propagation does not override existing owners; it only fills unowned assets.
- If an owner is deleted from a child asset, the owner is auto-assigned from the top hierarchy.
- Team ownership is recommended for broader context and collaboration.
