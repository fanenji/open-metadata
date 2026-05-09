---
type: concept
title: Data Drift
created: 2026-05-06
updated: 2026-05-06
tags: [machine-learning, data-quality]
related: [ai-driven-data-quality, data-observability-framework]
sources: ["Automate Data Quality Checks with AI Agents-20260506.md"]
---
# Data Drift

**Data Drift** refers to the phenomenon where the statistical properties of input data change over time, potentially degrading the performance of machine learning models and AI agents.

## Impact on AI Systems
As AI agents learn patterns from historical data, shifts in the underlying distribution (e.g., changes in user behavior, seasonal trends, or sensor degradation) can lead to "model decay."

## Mitigation Strategies
*   **Automated Cleaning and Normalization**: Ensuring data is standardized to prevent superficial shifts.
*   **Continuous Monitoring**: Implementing [[data-observability-framework]] to detect shifts in feature distributions.
*   **Retraining Loops**: Using feedback loops to update agents when significant drift is detected.
