---
type: entity
title: Chrome Extension
created: 2026-05-14
updated: 2026-05-14
tags: [tool, browser-extension, ui]
related: [openmetadata, persona]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Chrome Extension

The OpenMetadata Chrome Extension is a browser tool that provides inline metadata display and platform access directly from the browser. Updated in the 1.2.0 release to reflect the new UI design and support all entity types.

## Features

- **Inline metadata display**: When browsing data sources (e.g., Snowflake), clicking the extension shows owner, tier, domain, tags, glossary terms, descriptions, and lineage information for the current asset.
- **Activity feed**: View platform activity, mentions, and pending tasks directly from the extension.
- **Universal entity support**: Previously limited to pipelines and dashboards; now supports all entity types including stored procedures, search indexes, and data products.
- **Task notifications**: Displays pending tasks assigned to the user.

## Use Case

A data engineer exploring data directly in Snowflake can use the extension to instantly see OpenMetadata context — who owns the data, what it means, how it's classified, and its lineage — without switching to the OpenMetadata UI.