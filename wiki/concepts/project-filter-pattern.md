---
type: concept
title: Project Filter Pattern
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, filter, metadata-ingestion]
related: [powerbi-connector, filter-patterns]
sources: ["powerbi-connector-openmetadata-integration-documen-20260514.md"]
---

# Project Filter Pattern

The Project Filter Pattern is a filtering mechanism specific to the [[powerbi-connector|PowerBI Connector]] that controls which projects (workspaces) are included or excluded during metadata ingestion.

## Format

Projects are filtered using the **full project hierarchy expressed in dot notation**. For example:

- `Project1.NestedProjectA.OtherProject`
- `My Project`
- `.*Project`

## Usage

The filter supports regex-based include and exclude patterns, similar to other [[filter-patterns]] in OpenMetadata. The pattern is applied to the fully-qualified project path, so regex patterns must account for the dot notation format.

## Example

To include only projects under "Sales" and exclude "Sales.Archive":
- Include: `Sales.*`
- Exclude: `Sales.Archive.*`