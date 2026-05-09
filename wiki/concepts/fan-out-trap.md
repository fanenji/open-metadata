---
type: concept
title: "1:N Fan-Out Trap"
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, sql, performance, cost-optimization]
related: [data-quality-dimensions, network-shuffle, idempotency, medallion-architecture]
sources: ["if-you-understand-these-5-data-engineering-terms-youre-ahead-of-90-of-the.md"]
---
# 1:N Fan-Out Trap

The **1:N Fan-Out Trap** is an unintended row multiplication that occurs when joining two tables where one side has duplicate keys, causing a Cartesian explosion. It is a silent killer of cloud compute budgets.

## How It Happens

When you join Table A (1,000 rows) to Table B using a `LEFT JOIN`, you expect the result to still be 1,000 rows. But if Table B has multiple rows matching the join key (e.g., one user with 5 purchases), each row in Table A duplicates once per match in Table B. A 1,000-row table joined to a table with 5 duplicates per key becomes 5,000 rows.

## The Danger

- A 100-million-row table joined to a billion-row log table can explode into 50+ billion rows in seconds.
- The Spark cluster runs out of RAM, spills to disk, and crashes — burning hundreds of dollars in cloud compute.
- The explosion is silent: no error is thrown, just a slow, expensive death.

## Prevention

- **Verify granularity:** Always check the uniqueness of join keys before writing a `JOIN`.
- **Use `DISTINCT` or aggregation** on the many-side table before joining.
- **Test with small samples** before running at full scale.
- **Monitor row count ratios** in query plans.

## Connection to Existing Wiki

- [[data-quality-dimensions]] — The fan-out trap violates the **Uniqueness** and **Consistency** dimensions of data quality.
- [[network-shuffle]] — A fan-out trap amplifies shuffle costs by moving exploded data across the network.
- [[idempotency]] — Non-idempotent pipelines that trigger fan-out traps compound the problem on reruns.
