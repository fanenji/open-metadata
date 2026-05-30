---
type: concept
title: Keyword Search
created: 2026-05-14
updated: 2026-05-14
tags: [search, data-discovery, openmetadata]
related: [data-discovery, faceted-search, advanced-search]
sources: ["data-discovery-openmetadata-how-to-guide---openmet-20260514.md"]
---

# Keyword Search

Keyword search is the most basic [[data-discovery]] strategy in OpenMetadata. It allows users to search for data assets by entering text terms, which are matched against asset names, descriptions, and other text fields.

## How It Works

Users type one or more keywords into the search bar. OpenMetadata returns matching results across all supported asset types: tables, topics, dashboards, pipelines, ML models, containers, glossaries, and tags.

## Relationship to Other Search Modes

- **[[faceted-search]]** — After a keyword search, users can apply facet filters to narrow results
- **[[advanced-search]]** — For more precise queries, users can switch to advanced search syntax

## Limitations

Keyword search alone is insufficient for large data estates with thousands of assets. It relies on users knowing the right terms to search for, and it may return too many results without the ability to filter by attributes. This is why OpenMetadata also provides [[faceted-search]] and [[advanced-search]] as complementary strategies.

## See Also

- [[data-discovery]] — The overall data discovery framework
- [[faceted-search]] — Filter-based refinement of search results
- [[advanced-search]] — Complex query syntax for precise searches