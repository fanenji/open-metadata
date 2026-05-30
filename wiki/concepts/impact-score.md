---
type: concept
title: "Impact Score"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Impact Score
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, dimensional-validation, ranking, metric]
related: [dimensional-validation, data-quality]
sources: ["dimensional-validation-data-quality-testing-by-dim-20260514.md"]
---
# Impact Score

The impact score is a ranking metric (0.0 to 1.0) used in [[dimensional-validation]] to prioritize data quality issues across dimension groups. It balances two factors:

- **Failure rate:** The percentage of rows that failed the test in a given dimension group
- **Absolute failure volume:** The total number of rows that failed in that dimension group

This balanced approach ensures that both high-failure-rate dimensions (even with small data volumes) and high-volume dimensions (even with moderate failure rates) are surfaced as critical.

## How It Works

The impact score algorithm is designed to surface the most actionable issues first. For example:

- **Region A:** 1,000 rows, 500 failures (50% failure rate) → impact score ~0.95
- **Region B:** 100,000 rows, 20,000 failures (20% failure rate) → impact score ~0.87

Region A ranks higher due to its extreme failure rate, but Region B still ranks high due to the large absolute number of failures.

## Usage

- Dimensional validation results are automatically sorted by impact score in descending order
- The top 10 dimension groups by impact score are displayed as "Top Dimensions"
- The impact score determines which dimensions appear in the top 10 vs. being relegated to the "Others" group

## Notes

The exact formula for the impact score is not publicly documented. The algorithm is described conceptually as balancing failure rate and absolute volume. The score is computed automatically by OpenMetadata and displayed in the dimensional validation results UI.