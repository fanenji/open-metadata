---
title: DBT Tests That Catch Real Bugs and How to Wire CI
source: https://blog.stackademic.com/dbt-tests-that-catch-real-bugs-and-how-to-wire-ci-9e96508b8c73
author:
  - "[[Sai Kumar Devulapelli]]"
published: 2025-09-08
created: 2026-04-07
description: Build a dbt test suite that finds real defects—dupes, orphan facts, drift, SCD bugs—and wire CI so every PR runs the right tests fast.
tags:
  - clippings
  - dbt
  - best-practices
topic:
type: note
---
[Sitemap](https://blog.stackademic.com/sitemap/sitemap.xml)## [Stackademic](https://blog.stackademic.com/?source=post_page---publication_nav-d1baaa8417a4-9e96508b8c73---------------------------------------)

[![Stackademic](https://miro.medium.com/v2/resize:fill:76:76/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---post_publication_sidebar-d1baaa8417a4-9e96508b8c73---------------------------------------)

Stackademic is a learning hub for programmers, devs, coders, and engineers. Our goal is to democratize free coding education for the world.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RyqCPMEIFEgvVuBbaNnLmw.png)

DBT tests image from dbt.docs

Most [dbt](https://www.getdbt.com/) projects ship with the defaults — `unique` and `not_null` —then wonder why bugs still slip into production. Real incidents rarely come from a single null. They come from ***duplicate business keys after a join****,* ***orphan facts*** when a dimension lags, ***future timestamps*** from a source glitch,***SCD2 overlaps*** after a merge, or a silent ***row-count explosion*** that doubles your dashboard overnight. If your tests don’t target those failure modes, you’re not testing what actually breaks in the real world.

What you’ll build:

- Ship a [***targeted test suite***](https://docs.getdbt.com/docs/build/data-tests) (not just `unique` / `not_null`): add referential integrity, composite uniqueness, time sanity, ranges, SCD2 invariants, and drift guards.
- ***Make tests deterministic*** and small; use seeds/fixtures where helpful.
- [***Wire CI***](https://docs.getdbt.com/docs/deploy/about-ci) to run only what changed with `state:modified+`, publish artifacts, and block merges on failures.
- Add ***freshness checks*** for sources and surface test results in pull requests.

### What “real-bug-catching” means in dbt:

Most incidents aren’t “the column was null” — they’re ***logic and contract breaks****:*

- Duplicate business keys after a new source joins
- ***Orphan facts*** (missing dimension keys)
- ***Time sanity*** errors (future timestamps, late/out-of-order CDC)
- ***Range/enum*** violations (negative money, weird statuses)
- ***SCD2 gaps/overlaps*** after a merge
- ***Distribution drift*** (row counts double; cardinalities explode)

Your test suite should target these.

### The Essential Test Suite (with copy-paste examples)

Create a `schema.yml` next to your model. Start with the basics, then layer in ***generic*** custom tests.

> **1) Keys & integrity**

```c
version: 2

models:
  - name: fct_orders
    columns:
      - name: order_id
        tests:
          - not_null
          - unique

      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customer')
              field: customer_id    # catches orphan facts

      # Composite uniqueness: order_id + line_number
      - name: line_number
        tests:
          - not_null
    tests:
      - unique_combination_of_columns:
          combination_of_columns: [order_id, line_number]
```

> **2) Enums & ranges**

```c
- name: dim_customer
    columns:
      - name: status
        tests:
          - accepted_values:
              values: ['active', 'inactive', 'prospect']

      - name: lifetime_value
        tests:
          - dbt_utils.expression_is_true:
              expression: "lifetime_value >= 0"
```

> **3) Time sanity & freshness**

```c
- name: fct_orders
    columns:
      - name: order_ts
        tests:
          - dbt_utils.expression_is_true:        # no future dates
              expression: "order_ts <= current_timestamp"
          - recent_enough:
              within: '7 days'                   # custom generic test (below)

sources:
  - name: app
    schema: raw
    tables:
      - name: orders_src
        freshness:                                # source freshness check
          warn_after: {count: 2, period: hour}
          error_after: {count: 6, period: hour}
```

> **4) SCD2 invariants**

```c
- name: dim_customer_scd2
    tests:
      - scd2_no_overlaps:        # custom test asserts no overlapping validity ranges
          pk: customer_id
          valid_from: valid_from
          valid_to: valid_to
          is_current: is_current
```

### Handy custom generic tests (drop into macros/tests/)

> **A) Composite uniqueness (if you don’t use dbt-utils’ version)**

```c
-- macros/tests/unique_combination_of_columns.sql

{% test unique_combination_of_columns(model, combination_of_columns) %}
select {{ combination_of_columns | join(', ') }}
from {{ model }}
group by {{ combination_of_columns | join(', ') }}
having count(*) > 1
{% endtest %}
```

> **B) Recent enough (freshness at the row level)**

```c
-- macros/tests/recent_enough.sql

{% test recent_enough(model, within, column='order_ts') %}
select *
from {{ model }}
where {{ column }} < current_timestamp - interval '{{ within }}'
{% endtest %}
```

> **C) SCD2: no gaps/overlaps**

```c
-- macros/tests/scd2_no_overlaps.sql

{% test scd2_no_overlaps(model, pk, valid_from, valid_to, is_current) %}
with ordered as (
  select
    {{ pk }},
    {{ valid_from }} as start_at,
    {{ valid_to   }} as end_at,
    {{ is_current }} as is_current,
    lead({{ valid_from }}) over (partition by {{ pk }} order by {{ valid_from }}) as next_start
  from {{ model }}
),
problems as (
  select *
  from ordered
  where
    -- overlap
    (end_at is not null and next_start is not null and end_at > next_start)
    -- gap (optional): next period starts after current ended
    or (end_at is not null and next_start is not null and end_at < next_start)
)
select * from problems
{% endtest %}
```

(Tune the “gap” rule to your policy. Some shops allow small gaps; others require perfect stitching.)

### Drift guards that save you in prod

Numbers drift before they explode. Add ***guardrail tests*** that fail on abnormal change.

> **Row-count deltas (daily or PR)**

```c
- name: fct_orders
    tests:
      - volume_didnt_jump:
          period: '1 day'
          max_pct_increase: 100     # fail if rows >2x day-over-day
```
```c
-- macros/tests/volume_didnt_jump.sql (simplified)

{% test volume_didnt_jump(model, period, max_pct_increase) %}
with curr as (select count(*) as c from {{ model }} where date(updated_at) = current_date),
prev as (select count(*) as c from {{ model }} where date(updated_at) = current_date - interval '{{ period }}')
select *
from curr, prev
where prev.c > 0 and ( (curr.c - prev.c) / prev.c::decimal ) * 100 > {{ max_pct_increase }}
{% endtest %}
```

> **Cardinality drift (keys exploding)**

```c
- name: fct_orders
    tests:
      - key_cardinality_guard:
          key: customer_id
          max_pct_increase: 50
```

Implement similar to the volume test but counting distinct keys.

### Deterministic tests, not flaky ones

- ***Bound the time window*** in tests (e.g., last 7 days), so results don’t change mid-run.
- Avoid functions like `random()` or non-deterministic UDFs inside tests.
- If your model reads streaming/append-only tables, ***snapshot*** a small fixture or use a filtered view for tests.
- Quarantine intermittent upstream issues with ***warn*** thresholds, but **error** on true data contract breaks.

### Make the warehouse help (constraints where useful)

- On warehouses that **enforce** constraints (e.g., Postgres, some modes in others), add `**not null**` and `**unique**` constraints to critical tables.
- For engines that ***don’t enforce*** constraints, keep them in dbt tests and consider ***materialized views*** or ***merge logic*** that self-heals (e.g., dedup on write).

### Wire CI so tests run fast (and on every PR)

> **Goals**

- Run ***only impacted models/tests*** on a pull request.
- Fail the PR if **any** test fails, publish artifacts for debugging.
- Keep a ***“freshness job”*** on schedule (hourly/daily) for source SLAs.

### Pattern 1: dbt Core + GitHub Actions

```c
# .github/workflows/dbt-ci.yml
name: dbt CI

on:
  pull_request:
    branches: [ main ]

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Install dbt
        run: |
          pip install dbt-core dbt-bigquery # or dbt-snowflake/dbt-redshift/etc.
          dbt --version

      - name: Restore state (manifest from main for Slim CI)
        uses: actions/download-artifact@v4
        with:
          name: dbt-state
          path: .state
        continue-on-error: true

      - name: Prepare profiles
        run: |
          mkdir -p ~/.dbt
          cat > ~/.dbt/profiles.yml << 'EOF'
          your_profile:
            target: ci
            outputs:
              ci:
                type: bigquery      # adjust for your adapter
                method: service-account
                project: ${{ secrets.BQ_PROJECT }}
                dataset: ci_dbt
                keyfile_json: ${{ secrets.BQ_KEY_JSON }}
          EOF

      - name: deps + compile
        run: |
          dbt deps
          dbt compile

      - name: Build only what changed (Slim CI)
        run: |
          dbt build --select state:modified+ --state .state --fail-fast

      - name: Upload artifacts (manifest/run_results)
        uses: actions/upload-artifact@v4
        with:
          name: dbt-state
          path: |
            target/manifest.json
            target/run_results.json
```

> **How it works**

- The previous pipeline’s `manifest.json` is downloaded into `.state`.
- `dbt build --select state:modified+` runs only changed models and those downstream.
- Artifacts from this run are uploaded to become ***next time’s*** state — keeping CI fast.

### Pattern 2: dbt Cloud (simple)

- Use a **PR Job** with ***Defer to Production*** (executes models as if built on top of prod).
- Configure ***Run on Pull Requests*** and **Fail PR on Test Failures**.
- Pair with a scheduled ***Freshness Job*** (`dbt source freshness`) and a nightly ***Full Build****.*

### Add freshness & exposures to your guardrails

> **Source freshness (scheduled job)**

```c
dbt source freshness --select source:app.orders_src --output json
# Gate on error status; alert Slack if freshness fails.
```

> **Exposures** (tie models to dashboards/apps; great for impact analysis)

```c
exposures:
  - name: rev_dashboard
    type: dashboard
    url: https://bi.yourco.com/revenue
    depends_on:
      - ref('gold_revenue_daily')
    owner:
      name: Finance
      email: finance-data@yourco.com
```

### Put it together: a small but mighty test plan

> **For every fact table**

- `unique` + `not_null` on the natural/business key
- `relationships` to all dimension keys (no orphans)
- composite uniqueness for grain (`unique_combination_of_columns`)
- ranges: non-negative amounts, sensible limits
- time sanity: not future; recent enough; optional monotonic sequence for CDC
- drift guards: row-count delta and key cardinality

> **For every dimension**

- `unique` + `not_null` on surrogate key & business key
- enums on statuses; valid email/phone patterns as needed
- **SCD2** invariants (no overlaps; single current row per key)

> **For sources**

- `source freshness` warnings & errors
- input-field sanity (lengths, regex for IDs) using custom tests

### Conclusion

A dbt project is only as trustworthy as its tests — and your CI is only as fast as the scope you select. Combine ***contract-level*** [***tests***](https://docs.getdbt.com/docs/build/unit-tests) (keys, enums, ranges) with ***behavioral tests*** (SCD2, freshness, drift). Then wire **Slim CI** (`state:modified+`) so every pull request executes the ***right*** tests quickly and fails loud on real defects.

Thank you for reading this article. If you enjoyed this post, do you mind [***buying me a coffee***](http://buymeacoffee.com/devulapellisaikumar).

*Before you go:*

*👉 Be sure to* ***clap*** *and* ***follow*** *the* [*writer*](https://medium.com/@devulapellisaikumar)*! 👏*

*👉 Follow me on* [***LinkedIn***](https://www.linkedin.com/in/saikumard/)***.***

***Explore my related articles:***## [A Comprehensive Guide to Modern Data Transformation with DBT and BigQuery.](https://blog.stackademic.com/a-comprehensive-guide-to-modern-data-transformation-with-dbt-and-bigquery-43a5562ff4ae?source=post_page-----9e96508b8c73---------------------------------------)

### [In today’s data-driven world, having the right tools to manage, analyze, and transform vast amounts of information is…](https://blog.stackademic.com/a-comprehensive-guide-to-modern-data-transformation-with-dbt-and-bigquery-43a5562ff4ae?source=post_page-----9e96508b8c73---------------------------------------)

[

blog.stackademic.com

](https://blog.stackademic.com/a-comprehensive-guide-to-modern-data-transformation-with-dbt-and-bigquery-43a5562ff4ae?source=post_page-----9e96508b8c73---------------------------------------)

## A message from our Founder

**Hey,** [**Sunil**](https://linkedin.com/in/sunilsandhu) **here.** I wanted to take a moment to thank you for reading until the end and for being a part of this community.

Did you know that our team run these publications as a volunteer effort to over 3.5m monthly readers? **We don’t receive any funding, we do this to support the community. ❤️**

If you want to show some love, please take a moment to **follow me on** [**LinkedIn**](https://linkedin.com/in/sunilsandhu)**,** [**TikTok**](https://tiktok.com/@messyfounder), [**Instagram**](https://instagram.com/sunilsandhu). You can also subscribe to our [**weekly newsletter**](https://newsletter.plainenglish.io/).

And before you go, don’t forget to **clap** and **follow** the writer️!

[![Stackademic](https://miro.medium.com/v2/resize:fill:96:96/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---post_publication_info--9e96508b8c73---------------------------------------)

[![Stackademic](https://miro.medium.com/v2/resize:fill:128:128/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---post_publication_info--9e96508b8c73---------------------------------------)

[Last published 2 hours ago](https://blog.stackademic.com/build-a-tiny-ai-bot-with-a-simple-ui-using-python-and-streamlit-75e3ba5ea80f?source=post_page---post_publication_info--9e96508b8c73---------------------------------------)

Stackademic is a learning hub for programmers, devs, coders, and engineers. Our goal is to democratize free coding education for the world.

[![Sai Kumar Devulapelli](https://miro.medium.com/v2/resize:fill:96:96/1*guV-R5y3dwFTIn1feznJdg.png)](https://medium.com/@devulapellisaikumar?source=post_page---post_author_info--9e96508b8c73---------------------------------------)

[![Sai Kumar Devulapelli](https://miro.medium.com/v2/resize:fill:128:128/1*guV-R5y3dwFTIn1feznJdg.png)](https://medium.com/@devulapellisaikumar?source=post_page---post_author_info--9e96508b8c73---------------------------------------)

[56 following](https://medium.com/@devulapellisaikumar/following?source=post_page---post_author_info--9e96508b8c73---------------------------------------)

Senior Data Engineer | Turning Data into Business Value | Generative AI Enthusiast