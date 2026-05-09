---
type: entity
title: Looker
created: 2026-04-05
updated: 2026-05-07
tags:
  - bi
  - dashboard
  - analytics
  - business-intelligence
  - tool
related:
  - semantic-context-layer
  - openmetadata
  - mcp-toolbox
  - tableau
  - mode
  - metabase
  - lookml
  - business-intelligence-tools
sources:
  - "Building a Semantic Intelligence Layer for the AI Data Stack.md"
  - "understanding-the-modern-data-stack.md"
---
# Looker

Looker is a business intelligence (BI) and data modeling platform used for data exploration, visualization, and ad-hoc analysis. It serves as a primary integration target in the modern AI data stack, and in the [[modern-data-stack-overview|Modern Data Stack]] it is one of the popular BI tools alongside [[tableau]], [[mode]], and [[metabase]]. Looker also offers [[lookml]], a transformation alternative to [[dbt]].

In the context of a **Semantic Intelligence Layer**, Looker serves as a "downstream" consumer of metadata. Through the **Model Context Protocol (MCP)**, metadata such as tags, descriptions, and lineage can be automatically synchronized from **OpenMetadata** to Looker's LookML models. This ensures that the semantic definitions used by human analysts in dashboards are consistent with the definitions used by AI agents.