---
type: concept
title: Mutually Exclusive Tags
created: 2026-05-14
updated: 2026-05-14
tags: [classification, tags, configuration, openmetadata]
related: [classification-tags, classification-vs-categorization-tags, system-classification]
sources: ["overview-of-classification-official-documentation--20260514.md"]
---
# Mutually Exclusive Tags

The **Mutually Exclusive Tags** configuration is a setting on a [[classification-tags|Classification]] that prevents assigning multiple tags from the same Classification to a single data asset.

## Use Case

When a Classification groups tags that represent mutually exclusive states, this configuration ensures data integrity. For example:

- A **PII** Classification with tags `PII.Sensitive` and `PII.NonSensitive` — an asset cannot be both.
- A **PersonalData** Classification with tags `Personal` and `NonPersonal` — an asset cannot be both.

## Behavior

- If enabled, the UI and APIs will reject attempts to assign a second tag from the same Classification to an asset that already has one.
- If disabled (default), multiple tags from the same Classification can be applied.

## Configuration

The Mutually Exclusive option is set when creating or editing a Classification in the OpenMetadata UI (Govern > Classification). It can also be configured via the [[classification-apis]].

## Relationship to Categorization

This configuration is what formally distinguishes [[classification-vs-categorization-tags|Classification tags from Categorization tags]]. Classification tags are designed to be mutually exclusive; Categorization tags are not.