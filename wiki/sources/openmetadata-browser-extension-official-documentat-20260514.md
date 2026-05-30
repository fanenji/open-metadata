---
type: source
title: "Source: openmetadata-browser-extension-official-documentat-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["openmetadata-browser-extension-official-documentat-20260514.md"]
tags: []
related: []
---

# Source: openmetadata-browser-extension-official-documentat-20260514.md

## Analysis of: OpenMetadata Browser Extension

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| OpenMetadata Browser Extension | Product/Feature | Central — the subject of the document | **No** |
| Chrome Webstore | Platform | Peripheral — distribution channel | No |
| SSO redirect URL (`ndjnpiadedlmgddlpeklbnobebkpkdgb.chromiumapp.org/auth0`) | Configuration value | Peripheral — technical requirement for SSO | No |

### Key Concepts

| Concept | Definition | Why It Matters | In Wiki? |
|---------|------------|----------------|----------|
| Browser Extension Metadata Bridge | Mechanism allowing users to view OpenMetadata metadata (ownership, description, tags, glossary terms, schema, lineage, custom properties) directly within third-party tools via a Chrome extension | Enables context-switch reduction — users stay in their active workspace while accessing metadata | **No** |
| SSO Redirect Registration | Requirement to add a specific Chrome extension callback URL to the SSO provider's allowed redirect list for authentication to work | Critical for SSO-enabled OpenMetadata instances; without it, authentication fails | **No** |

### Main Arguments & Findings

- **Core claim**: The browser extension eliminates context-switching by surfacing OpenMetadata metadata directly within third-party tools.
- **Evidence**: The document describes the feature's functionality (activity feeds, metadata details) and provides a video walkthrough reference. No quantitative evidence or user studies are cited.
- **Strength of evidence**: Low — purely descriptive documentation with no empirical support.

### Connections to Existing Wiki

- **Related pages**: [[activity-feed]], [[data-asset-ownership]], [[classification-tags]], [[glossary-terms]], [[custom-properties]], [[data-lineage]], [[openmetadata-collaboration]]
- **Relationship**: The extension is a **consumption-side interface** that surfaces existing wiki concepts (activity feeds, tags, lineage, etc.) in a new context (third-party tools). It does not introduce new metadata types or governance mechanisms.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension**: The document mentions "third party tool, which is integrated with OpenMetadata" but does not specify which tools are supported or how integration is established. This is a significant gap — the extension's value proposition depends on tool compatibility, which is undefined.
- **Caveat**: SSO configuration is required for self-hosted instances but the document provides only a single URL and a generic link for "more information" — no step-by-step SSO setup guidance.

### Recommendations

**Pages to create:**
1. **[[browser-extension]]** — New entity page covering installation, authentication, SSO configuration, supported tools, and known limitations.

**Pages to update:**
- **[[openmetadata-collaboration]]** — Add a note that the browser extension extends collaboration
