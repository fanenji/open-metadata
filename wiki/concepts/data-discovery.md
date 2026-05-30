---
type: concept
title: Data Discovery
created: 2026-05-14
updated: 2026-05-14
tags: ["data-discovery", "search", "openmetadata", "governance"]
related: ["faceted-search", "advanced-search", "metadata-versioning", "openmetadata-features", "unified-metadata-graph", "data-lineage", "classification-tags", "glossary-terms", "usage-metrics", "elasticsearch-7x", "tiers", "data-profiling", "soft-deletion"]
sources: ["data-discovery-openmetadata-how-to-guide---openmet-20260514.md", "how-to-discover-assets-of-interest---openmetadata--20260514.md"]
---

# Data Discovery

Data Discovery in OpenMetadata is the process of finding relevant data assets within the organization's data estate. The platform provides five complementary discovery strategies that work together to help users locate the data they need.

## The Five Discovery Strategies

1. **Keyword Search**: Simple name/description matching across all asset types, backed by [[elasticsearch-7x|Elasticsearch]]. Matches names, column names, chart names, and descriptions.

2. **Quick Filters**: Pre-defined filter categories (Owner, Tag, Tier, Service, Service Type, Database, Schema, Columns) that narrow search results. Includes a toggle for [[soft-deletion|soft-deleted assets]].

3. **Filter by Importance**: Two mechanisms — [[tiers]] (manual importance classification) and [[usage-metrics]] (automated activity-based metrics like Last Updated, Weekly Usage, and Relevance).

4. **Discover through Association**: Two sub-strategies:
   - **Frequently Joined Tables/Columns**: Measured by the [[data-profiling|data profiler]].
   - **Relationships via Lineage**: Upstream and downstream nodes from [[data-lineage]].

5. **Advanced Search**: Boolean operators, faceted queries, and a syntax editor with and/or conditions for strict multi-parameter criteria. Separate interfaces per asset type.

6. **Discover Data Evolution**: Viewing [[data-lineage]] and [[metadata-versioning]] to track how assets have changed over time.

## Key Differentiator

The multi-strategy approach — from simple keyword search to advanced Boolean queries to serendipitous discovery through association — is a key differentiator of OpenMetadata's data discovery capabilities. Users can start with broad searches and progressively narrow down using filters, importance metrics, and relationships.

## Open Questions

- How do "frequently joined tables" (profiler) and lineage-based relationships relate? Are they complementary or overlapping?
- Does Advanced Search support saved searches or search history?
- What is the "Relevance" sorting algorithm based on?