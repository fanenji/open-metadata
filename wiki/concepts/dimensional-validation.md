---
type: concept
title: "Dimensional Validation"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Dimensional Validation
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, dimensional-validation, openmetadata]
related: [impact-score, data-quality, data-profiling, profiler-partitioning, data-observability-alerts]
sources: ["dimensional-validation-data-quality-testing-by-dim-20260514.md"]
---
# Dimensional Validation

Dimensional validation is a data quality testing feature in [[OpenMetadata]] that groups test results by a categorical **dimension column**, producing per-segment metrics instead of a single pass/fail result. This enables granular analysis of data quality across business dimensions such as region, product category, customer segment, or time period.

## Key Concepts

- **Dimension Column:** A categorical column used to group test results (e.g., `region`, `product_category`). Must have low-to-medium cardinality (5-25 unique values recommended).
- **Dimension Group:** One unique value in the dimension column (e.g., "North America"). Each group gets its own metrics.
- **Top Dimensions:** The default top 10 dimension groups ranked by [[impact-score]], showing the most critical issues first.
- **"Others" Group:** If the dimension column has more than 10 unique values, all dimensions outside the top 10 are combined into an "Others" group. Metrics are accurately calculated but individual issues in dimensions 11+ may be hidden.
- **Cardinality:** The number of unique values in the dimension column. Critical for performance — high cardinality (>100) causes significant slowdowns (5-10x longer execution).
- **Impact Score:** A 0.0-1.0 score balancing failure rate and absolute failure volume to rank dimension groups by severity.

## When to Use

- Multi-region or multi-location data analysis
- Product or category quality analysis
- Customer segment quality monitoring
- Any scenario where understanding *where* quality issues occur is more valuable than knowing *whether* they exist

## When NOT to Use

- When only a yes/no pass/fail answer is needed
- With high-cardinality columns (>100 unique values)
- On very large tables (>500GB) without sampling or partitioning
- When the dimension does not provide actionable business insights

## Configuration

Dimensional validation is configured via the OpenMetadata UI:

1. Navigate to the target table → Data Observability tab → Add Test → Dimension Level
2. Select the target column and dimension column
3. Choose a column-level test type and configure parameters
4. Set up the pipeline and schedule as with standard tests

## Results Interpretation

Results display per dimension group:
- **Dimension Value:** The specific value (e.g., "North America")
- **Total Count:** Rows in this group
- **Failed Count:** Rows failing the test
- **Impact Score:** Severity ranking (0.0-1.0)
- **Test-Specific Metrics:** Vary by test type (null counts, mean values, duplicate counts, etc.)

Results are sorted by impact score descending. Click any dimension group to view its historical trend.

## Best Practices

- Choose meaningful, low-cardinality dimensions (region, product_type, customer_segment)
- Group high-cardinality values into derived columns (e.g., cities → regions)
- Start with 1-2 critical tests, validate performance, then scale
- Combine with Profile Sample and partitioning for large tables
- Monitor test execution time in the Pipeline tab
- Use descriptive test names (e.g., "Email Completeness by Region")
- Document business context in the test description

## Limitations

- **High Cardinality Performance Impact:** Tests may take 5-10x longer; use sampling or derived columns as workarounds
- **"Others" Group Limitations:** Issues in dimensions ranked 11+ are hidden; reduce cardinality so all important values fit in top 10
- Only works with column-level tests (not table-level tests)

## Troubleshooting

- **"No results":** Test hasn't run yet, partitioning filtered all data, or sampling excluded all groups
- **"NULL" as dimension value:** Null values in the dimension column are grouped together; clean up nulls if unexpected
- **Test execution too long:** Enable sampling, enable partitioning, or choose a lower-cardinality dimension

## Real-World Examples

1. **E-Commerce Product Descriptions:** A company discovers clothing product descriptions are only 72% complete (vs. 98% for electronics), enabling targeted content improvement.
2. **Multi-Region Email Validation:** A SaaS company finds Asia Pacific email validation is 96.2% valid (vs. 99.8% for North America), revealing a regional portal bug.
3. **Financial Transaction Monitoring:** A financial services company identifies business accounts have 94.3% valid transaction amounts (vs. 99.9% for checking), prompting limit updates.