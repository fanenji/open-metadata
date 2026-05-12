---
type: source
title: "Permission Control · open-metadata/OpenMetadata · Discussion #17119"
created: 2026-05-10
updated: 2026-05-10
tags: [openmetadata, permission-control, rbac, governance]
related: [openmetadata, openmetadata-permission-limitations, data-catalog-tool-comparison, data-domain-governance]
sources: ["permission-control-open-metadata-openmetadata-disc-20260510.md"]
authors: [luckyliush, Prajwal214]
year: 2024
url: "https://github.com/open-metadata/OpenMetadata/discussions/17119"
venue: "GitHub Discussions"
---
# Permission Control · open-metadata/OpenMetadata · Discussion #17119

This GitHub discussion documents a critical limitation in OpenMetadata's permission system (as of v1.4.x): the platform can restrict *access* to data assets but cannot hide them from the Explore tab UI. Users can see tables they are not authorized to access.

## Summary

User **luckyliush** asked whether OpenMetadata could restrict users to seeing only specified databases or tables. After several rounds of troubleshooting, OpenMetadata collaborator **Prajwal214** confirmed that tag-based policies could not hide assets from the Explore tab. The planned solution, Search-based RBAC, was scheduled for OpenMetadata v1.6.

## Key Findings

- **Current Limitation (pre-v1.6):** OpenMetadata cannot hide data assets from the Explore tab. Users can see all assets but cannot access restricted ones.
- **Tag-Based Policy Workaround:** Initially suggested but ultimately ineffective for hiding assets. Policies can block operations (View, Edit) but not visibility in the Explore tab.
- **Planned Solution:** Search-based RBAC, which would hide assets from search results and the Explore tab, was planned for OpenMetadata v1.6 release.
- **Governance Gap:** The inability to hide assets undermines a core governance requirement — users should not even know about data they are not authorized to see.

## Implications

This limitation is a critical evaluation criterion for any data catalog deployment requiring strict data confidentiality. Organizations needing to hide sensitive assets from unauthorized users should verify whether OpenMetadata v1.6+ fully implements Search-based RBAC, or consider alternative tools like [[datahub]] or [[amundsen]].