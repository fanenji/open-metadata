---
type: concept
title: Tag Rename vs. Delete
created: 2026-05-14
updated: 2026-05-14
tags: [classification, data-governance, operations, best-practices]
related: [classification-tags, classification-best-practices]
sources: ["best-practices-for-classification-official-documen-20260514.md"]
---
# Tag Rename vs. Delete

Tag Rename vs. Delete is an operational best practice in [[OpenMetadata]] that advises renaming [[classification-tags|classification tags]] with typos or poor names rather than deleting them. Deleting a classification tag removes all the tagging effort that has been invested in applying that tag to data assets across the organization.

## The Problem

When classification tags contain typos or are poorly named, users may be tempted to delete the tag and create a corrected version. However, deleting a tag permanently removes all associations between that tag and the data assets it was applied to. This results in lost governance metadata and requires re-tagging all affected assets.

## The Solution

OpenMetadata supports renaming classification tags. Instead of deleting a tag with a typo, simply rename it to the correct name. All existing tag assignments on data assets are preserved and automatically reflect the new name.

## Best Practice

- Always rename tags to fix typos or improve names.
- Only delete tags when the tag itself is no longer needed conceptually (e.g., a deprecated classification category).
- Before deleting any tag, audit its usage to understand the impact on existing data asset classifications.

## Open Questions

- Does renaming a classification tag retroactively update all existing tag assignments on data assets? (The documentation implies yes, but this should be verified.)
- Are there any performance implications for renaming a heavily-used tag across a large data estate?