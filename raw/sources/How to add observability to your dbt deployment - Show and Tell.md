---
title: How to add observability to your dbt deployment - Show and Tell
source: https://discourse.getdbt.com/t/how-to-add-observability-to-your-dbt-deployment/3451
author:
  - "[[dbt Community Forum]]"
published: 2021-12-06
created: 2026-04-07
description: "April 2023 update: For an up-to-date overview of our observability stack for dbt, please refer to this blog post This post describes the system we (@kevinc and @jt_st) built at Snapcommerce to get more observability out…"
tags:
  - clippings
  - dbt
topic:
type: note
---
**April 2023 update:** For an up-to-date overview of our observability stack for dbt, please refer to this [blog post](https://medium.com/super/dbt-at-super-part-3-observability-c8755109901f)

This post describes the system we (@kevinc and [@jt\_st](https://discourse.getdbt.com/u/jt_st)) built at Snapcommerce to get more observability out of our dbt deployment. It serves as a companion piece to the Coalesce 2021 talk “ [Observability Within dbt](https://coalesce-2021.heysummit.com/talks/observability-within-dbt/) ”.

tl;dr: Use tools in your existing stack (MDS), dbt artifacts, and your query log to build reporting and alerts on dbt model/job runs and performance

## Introduction

We undertook this project to answer questions analytics engineers have about their dbt models, tests, and pipelines. The questions we often heard were:

- Why isn’t my model up to date?
- How long did my model take to run?
- When is the last time my model ran?
- Is my data accurate? Did my tests pass?
- Why are my models taking so long to build?

There wasn’t an easy way to answer these questions without going into several services or SaaS tools, or painstakingly debugging logs.

We decided to build a system that would help answer these questions in an automated and proactive manner. Applying the “ [jobs to be done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) ” framework, with analytics engineers were our customers, we set out to create a system that would perform the following jobs:

- Send alerts to individual model owners based on custom criteria (e.g. run or test failures)
- Surface key information about model and job-level executions, like model runtimes and freshness
- Identify models in need of optimization and bottlenecks in dbt pipelines
- Reliably collect metadata for *all* production pipelines in quasi-realtime, including after failures

Our guiding principles for this project were making the system:

1. **Lightweight** — deploy the system easily using tools in the modern data stack
2. **Flexible** — explore, report, and alert on metadata using SQL
3. **Exhaustive** — support all dbt resources, artifacts, and command types (e.g. run, test, build)

## Architecture

Our system comprises four distinct parts:

1. **Orchestration**
	- dbt pipelines are orchestrated using Airflow and KubernetesPodOperator tasks
		1. Example: `dbt run -s tag:hourly`
2. **Metadata**
	- Artifacts are loaded into Snowflake at the end of every pipeline, even if the dbt pipeline resulted in a failure
		- Example: `dbt run -s tag:hourly; dbt run-operation upload_artifacts —args run_results`
3. **Modelling**
	- Artifacts are modelled and joined to the manifest using dbt
		- Example: `stg_dbt_run_results`
4. **Reporting and Alerting**
	- dbt artifacts are brought into Looker and displayed in dashboards. Alerts are set up to fire directly to specific people based on Slack user groups.
		- Example: Alert @finance-domain on all model run and test failures with `tag:finance` in the last 15 minutes

### Orchestration

Our dbt deployment consists of three types of models: Hourly, nightly, and external. Each model in our project can only have one of these **deployment tags**. Hourly and nightly models are managed in their respective pipelines, which look like this:

![image](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/20bbd3248f6766a712326fdff41204746135c298_2_690x62.png)  
![image](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/be2fd7a3542c672734e0062dc2bb636b042dde56_2_690x42.png)

External dbt models refer to models managed outside of the hourly and nightly jobs. An external pipeline might be structured like this:  
`copy_myreport_to_s3 >> load_myreport_to_snowflake >> run_myreport_dbt_models`

We ensure that there is no duplication across hourly/nightly and external pipelines by using intersection selectors. For example, an “external” dbt job runs models at the intersection between the source’s downstream models and `tag:external`, e.g.:

`dbt run -s source.myreport+, tag:external`

In Airflow, we use the KubernetesPodOperator to execute these dbt commands in a single task, rather than splitting up into separate tasks as [some teams do](https://www.astronomer.io/blog/airflow-dbt-1).

```bash
dbt_nightly_run = KubernetesPodOperator(
  **snaptravel_defaults,
  **dbt_defaults,
  task_id='dbt_nightly_run_task',
  name="dbt-nightly-run-task",
  arguments=dbt_run_commands,
  dag=dag
  )
```

### Metadata

We created a macro to upload dbt artifacts directly to Snowflake from the Airflow worker node’s local disk. We first load data to a Snowflake stage using a `PUT` command:

```sql
{% set put_query %}
    PUT file://target/run_results.json @RAW.DBT.DBT_LOAD auto_compress=true;
{% endset %}
{% do run_query(put_query) %}
```

Then, we copy the file from the stage the respective dbt artifacts table using `COPY`:

```sql
{% set copy_query %}
    BEGIN;
    COPY INTO RAW.DBT.RUN_RESULTS FROM
        @RAW.DBT.DBT_LOAD
        file_format=(type='JSON')
        on_error='skip_file';
    COMMIT;
{% endset %}
{% do run_query(copy_query) %}
```

Then we remove data from the stage:

```bash
{% set remove_query %}
    REMOVE @{{ database }}.DBT.DBT_LOAD pattern='.*.json.gz';
{% endset %}
```

We run this macro after every dbt job in Airflow, using a command structure like the following:

```bash
dbt run -m tag:hourly; ret=$?;
dbt run-operation upload_dbt_artifacts --args 'run_results'; exit $ret
```

This ensures that artifacts are uploaded even if the first command returns a failure, as a result of a failing test, for example.

### Modelling

Once the artifacts land in Snowflake, they’re modelled using dbt so they can be used for reporting, analysis, and alerting on our dbt pipelines and model performance.

Much of this can be done automatically now using the [Tails.com](http://tails.com/) [dbt\_artifacts](https://github.com/tailsdotcom/dbt_artifacts) package, which didn’t exist when we began this project. We did use the Gitlab data team’s [open source analytics repo](https://gitlab.com/gitlab-data/analytics/-/tree/master/transform/snowflake-dbt/models/workspaces/workspace_data/dbt) for a lot of our initial code, and we are very grateful to them!

The full dbt DAG for artifacts looks like this:  

**[![|938px;x269px;](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/41540288a2b884050df549a02ba50dcf8dc30064_2_690x198.png)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/41540288a2b884050df549a02ba50dcf8dc30064.png "|938px;x269px;")**

The most relevant model joins the `run_results` artifact, `manifest` artifact, and Snowflake query history. The query history allows us to calculated the estimated cost of every dbt model and pipeline run. It also gives us key query performance metrics like **byte spillage** and **partitions scanned** at the model level, which helps us identify poorly performing models.

We join artifacts to the query log using a query comment:

```bash
query-comment:
  comment: "{{ query_comment(node) }}"
  append: true
```

The query comment macro is taken directly from the [dbt documentation](https://docs.getdbt.com/reference/project-configs/query-comment#advanced-use-a-macro-to-generate-a-comment), with small modifications. The fields `node_id` and `invocation_id ` allow us to join artifact instances to the underlying queries.

```bash
{% macro query_comment(node) %}
    {%- set comment_dict = {} -%}
    {%- do comment_dict.update(
        app='dbt',
        dbt_version=dbt_version,
        profile_name=target.get('profile_name'),
        target_name=target.get('target_name'),
        invocation_id=invocation_id
    ) -%}
    {%- if node is not none -%}
      {%- do comment_dict.update(
        file=node.original_file_path,
        node_id=node.unique_id,
        node_name=node.name,
        resource_type=node.resource_type,
        package_name=node.package_name,
        relation={
            "database": node.database,
            "schema": node.schema,
            "identifier": node.identifier,
            "materialized": node.config.get('materialized')
        }
      ) -%}
    {% else %}
      {%- do comment_dict.update(node_id='internal') -%}
    {%- endif -%}
    {% do return(tojson(comment_dict)) %}
{% endmacro %}
```

We use four types of models in our dbt project. Views and tables are single CREATE statements and can be mapped 1:1 with a query in the query history. Insert by period and incremental models have multiple queries associated with them, so for these we aggregate relevant metrics in the query history (e.g. `bytes_spilled` becomes `total_bytes_spilled` across all model queries).

We use our snowflake contract rate and the estimated credits used per query to calculate our estimated cost per query:

```bash
CASE
  WHEN group_queries.warehouse_size = 'XSMALL'
    THEN 1
  WHEN group_queries.warehouse_size = 'SMALL'
    THEN 2
  WHEN group_queries.warehouse_size = 'MEDIUM'
    THEN 4
  WHEN group_queries.warehouse_size = 'LARGE'
    THEN 8
  WHEN group_queries.warehouse_size = 'XLARGE'
    THEN 16
  WHEN group_queries.warehouse_size = 'XXLARGE'
    THEN 32
  WHEN group_queries.warehouse_size = 'XXXLARGE'
    THEN 64
  WHEN group_queries.warehouse_size = 'XXXXLARGE'
    THEN 128
END                                                        AS warehouse_credits_hourly,
total_elapsed_time_mins * warehouse_credits_hourly / 60    AS est_credits_used,
{{ var('snowflake_contract_rate') }} * est_credits_used    AS est_cost
```

### Reporting and Alerting

dbt artifacts are brought into Looker and displayed in dashboards. The first use case is alerting on model run and test failures.

#### Failures

One of our main objectives was sending alerts directly to individual model owners. To accomplish this, we require every model to be tagged with a single domain tag — finance, growth, product, etc. We construct charts for each domain’s model runs like the one below, which shows the most recent runs of every model tagged `finance`  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/a239d590962c2d8e19a70bded13db3c687d6cc5a.png)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/a239d590962c2d8e19a70bded13db3c687d6cc5a.png "Untitled")

A Looker alert on this chart runs every 15 minutes, and if there’s a failed run, a notification is sent to our #data-alerts slack channel tagging the slack user group @finance-domain. Once an alert fires, a domain member goes to the dashboard, fetches the compiled SQL, and starts debugging. The same occurs for tests, snapshots, source freshness failures, etc.:  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/f9f2a1d81a67111b602f4652c6a8db4de7ed0cb5_2_690x214.png)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/f9f2a1d81a67111b602f4652c6a8db4de7ed0cb5.png "Untitled")

#### Model Performance

We also show data relevant to model performance. We can easily see the models which take the longest along with their key query performance metrics. These metrics help us determine when a model’s materialization should be updated, or when the warehouse size should be increased. For example, let’s look at a subset of our models:  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/eafba5dbd83fc5a7157846b0b8c4bb36479d0717_2_690x186.jpeg)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/eafba5dbd83fc5a7157846b0b8c4bb36479d0717.jpeg "Untitled")

There are three main action items one can take from this view, beyond simple optimization and SQL refactoring:

1. **Materialization:** If the model is taking a long time to build, it may be worth exploring a new materialization strategy, like an incremental or insert\_by\_period
2. **Clustering**: If the model is taking a long time to build and a high percentage of total partitions are being scanned, it may be worthwhile to explore new cluster keys
3. **Warehouse**: If the model tends to have a lot of spillage and bytes sent over the network, it may be worthwhile to simply increase the size of the warehouse, once other opportunities for optimization have been exhausted.

Analytics engineers can also view models individually across time:  
![dbt_supply_bucketed_lmp](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/06c3ab2ce61f536b0d0e4473d879332fcb0c96da.gif)  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/7cfb244b1e0b469fec3d6216d06fa39a215685b3_2_690x321.png)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/7cfb244b1e0b469fec3d6216d06fa39a215685b3.png "Untitled")

  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/98903f6747a98a38bd8b678905faa92c20257447_2_690x346.jpeg)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/98903f6747a98a38bd8b678905faa92c20257447.jpeg "Untitled")

#### Job Performance

Finally, we can evaluate job-level performance and identify pipeline bottlenecks using Gantt charts, inspired by [@claire](https://discourse.getdbt.com/u/claire) ’s [post](https://discourse.getdbt.com/t/analyzing-fishtowns-dbt-project-performance-with-artifacts/2214) about the dbt project at dbt labs.

When the hourly or nightly jobs begin to take longer than expected, this view can help identify areas for optimization to keep them within SLA. Here are examples of our core hourly and nightly jobs:  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/17e47b235c88d3339ccefbf1cb64ea4924a535a4_2_690x242.jpeg)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/17e47b235c88d3339ccefbf1cb64ea4924a535a4.jpeg "Untitled")

  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/62e1a235dffd6db4e55d549402420bea7d9d8d5b_2_690x205.jpeg)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/62e1a235dffd6db4e55d549402420bea7d9d8d5b.jpeg "Untitled")

  

[![Untitled](https://us1.discourse-cdn.com/flex020/uploads/getdbt/optimized/1X/d06aacc248ab66fa462c2858d6a683782a85cedd_2_690x447.jpeg)](https://us1.discourse-cdn.com/flex020/uploads/getdbt/original/1X/d06aacc248ab66fa462c2858d6a683782a85cedd.jpeg "Untitled")

### Conclusion

Setting this up on your stack should be doable even if you have to swap out pieces, like a different orchestration tool or BI platform. Community projects like the dbt\_artifacts package and Gitlab’s open source analytics project help a lot. We are happy to share our code too – just reach out to either of us on the dbt slack.