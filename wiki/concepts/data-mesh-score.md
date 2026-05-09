---
type: concept
title: Data Mesh Score
created: 2026-05-08
updated: 2026-05-08
tags: [data-mesh, assessment, scoring, monte-carlo]
related: [data-mesh, data-mesh-maturity-assessment, data-mesh-challenges, monolithic-data-lake]
sources: ["research-data-mesh-organizational-maturity-assessment-2026-05-08.md"]
---
# Data Mesh Score

The **Data Mesh Score** is a lightweight self-assessment tool proposed by Monte Carlo for evaluating an organization's readiness for [[data-mesh]] adoption.

## Scoring Ranges

- **1–15:** A centralized warehouse or data lake is likely sufficient. Data mesh may add unnecessary complexity.
- **15–30:** The organization is beginning to feel the pain of centralized bottlenecks. A pilot mesh implementation may be appropriate.
- **30+:** The organization is experiencing significant friction from centralized data management. Formal mesh adoption is likely warranted.

## Critique

- **Oversimplification:** A single score may obscure complex organizational dynamics, such as [[jagged-maturity-profiles]]
- **Lack of Dimension-Specific Insight:** Does not identify which specific dimensions (domain ownership, platform, governance, culture) need improvement
- **Vendor Perspective:** Monte Carlo is a data observability vendor; the score may be biased toward tooling solutions

## Relationship to Other Frameworks

The Data Mesh Score is at one end of a spectrum from lightweight to comprehensive assessment. More detailed frameworks like the Everforth ECS Four-Category Model or the synthesized [[data-mesh-maturity-assessment]] provide multidimensional evaluation but require more effort to administer.
