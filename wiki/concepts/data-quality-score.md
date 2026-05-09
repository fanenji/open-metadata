---
type: concept
title: Data Quality Score
created: 2026-04-29
updated: 2026-04-29
tags: [data-quality, measurement, metric, governance]
related: [data-quality-dimensions, shift-left-data-quality, engineering-led-data-quality, data-quality-certification-vs-usability-certification, data-observability-definition, data-contract-observability]
sources: ["Defining Data Quality The Foundation of Modern Data Architecture.md"]
---
# Data Quality Score

A quantifiable metric for measuring Data Quality (DQ) across datasets. The DQ Score transforms DQ from a subjective discussion into an objective, engineering-grade metric that can be automated, monitored, and improved continuously.

## Calculation

The DQ Score is calculated as the percentage of passed DQ rules:

> **DQ Score = (Number of Passed Rules / Total Number of Rules) × 100**

## Process

1. **Define Validation Rules**: For each dataset, establish a set of DQ rules or checks covering key dimensions such as accuracy, completeness, consistency, and validity.
2. **Evaluate Rule Outcomes**: Each rule produces a binary result — pass or fail — based on whether the dataset meets the expected standard.
3. **Calculate the DQ Score**: Apply the formula above to produce a clear, interpretable metric.
4. **Monitor Trends**: Track DQ scores periodically to identify degradation early, track improvements, and prioritize datasets needing remediation.

## Relationship to Other Concepts

The DQ Score is the measurement mechanism for [[data-quality-dimensions]]. It can be integrated into [[data-contract-observability]] dashboards as a key metric for contract compliance. The score supports the [[engineering-led-data-quality]] approach by providing a programmatic, automatable quality indicator.

## Open Questions

- How does the DQ Score integrate with existing observability tools like [[sifflet]] or [[openmetadata-data-quality]]?
- What is the relationship between DQ Score and [[data-contract-observability]] metrics?
- How should thresholds for "good enough" DQ Scores be defined across different data domains?