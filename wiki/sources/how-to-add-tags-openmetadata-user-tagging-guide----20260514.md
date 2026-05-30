---
type: source
title: "How to Add Tags | OpenMetadata User Tagging Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, tagging, classification, pii, auto-classification, data-profiling]
related: [classification-tags, auto-classification, data-profiling, pii-sample-data-masking, tiers, system-classification, how-to-classify-data-assets-official-documentation-20260514]
sources: ["how-to-add-tags-openmetadata-user-tagging-guide----20260514.md"]
---

# How to Add Tags | OpenMetadata User Tagging Guide

**Source:** [OpenMetadata Documentation v1.12.x](https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/tags)

## Summary

This is a simplified user-facing guide for adding classification tags to data assets in OpenMetadata. It covers the 3-step manual tagging workflow, the discovery of tagged assets from the Classification page, and the auto-classification feature that uses NLP during profiling to automatically tag PII-sensitive data.

## Key Content

### Manual Tagging Workflow (3 Steps)

1. From the Explore page, select a data asset and click the edit icon or "+ Add" for Tags.
2. Search for the relevant tags by typing or scrolling through the options.
3. Click the checkmark to save the changes.

### Tag Discovery

Tagged data assets can be discovered from the Classification page (Govern >> Classification), which displays a list of tags along with their usage count across data assets. Clicking the usage number reveals the specific tagged assets.

### Auto-Classification via NLP

OpenMetadata identifies PII data and auto-tags or suggests tags using the data profiler during ingestion. The profiler analyzes both column names and column content (sample data) using NLP. Two examples are provided:

- **Name-based detection:** Columns named `user_name` and `social security number` are auto-tagged as PII-Sensitive.
- **Content-based detection:** A column named `dwh_x10` (which gives no clue from its name) is also auto-tagged as PII-Sensitive because the sample data values reveal PII content.

### Related Topics

The guide also references [[tiers]], [[system-classification]], and the tag request workflow.

## Significance

This document provides the critical detail that auto-classification analyzes column *content* (sample data values), not just column names. This is a key distinction from simpler name-based classification systems. The document is a simplified user guide; for more detailed administrative guidance, see [[how-to-classify-data-assets-official-documentation-20260514]].