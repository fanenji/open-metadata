---
type: concept
title: Confidence Parameter (Auto Classification)
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, pii, data-governance, tuning]
related: [auto-classification, auto-classification-external-workflow, pii-processor]
sources: ["external-auto-classification-workflow---openmetada-20260514.md"]
---
# Confidence Parameter (Auto Classification)

The `confidence` parameter is a numeric threshold (0–100) in the Auto Classification workflow configuration that controls the sensitivity-specificity trade-off for PII detection. It determines how certain the detection algorithm must be before tagging a column as containing sensitive information.

## Behavior

- **Higher values (e.g., 90–100)**: The algorithm requires high certainty before tagging. This reduces false positives (columns incorrectly tagged as sensitive) but may miss genuinely sensitive columns (false negatives). Use when precision is critical — for example, when false positives would trigger unnecessary compliance reviews.

- **Lower values (e.g., 50–70)**: The algorithm tags columns more aggressively. This catches more sensitive data but increases the risk of false positives. Use when recall is critical — for example, during initial data discovery scans where missing sensitive data is more costly than reviewing false positives.

- **Default (80)**: A balanced threshold suitable for most use cases.

## Configuration

In the YAML configuration:

```yaml
sourceConfig:
  config:
    type: AutoClassification
    enableAutoClassification: true
    confidence: 85
```

## Tuning Guidance

1. Start with the default value (80).
2. Review the classification results in the OpenMetadata UI.
3. If too many false positives: increase confidence by 5–10 points.
4. If sensitive columns are being missed: decrease confidence by 5–10 points.
5. Iterate until the desired balance is achieved for your data and compliance requirements.