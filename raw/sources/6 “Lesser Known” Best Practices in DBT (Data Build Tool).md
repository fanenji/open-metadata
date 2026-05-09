---
title: 6 “Lesser Known” Best Practices in DBT (Data Build Tool)
source: https://medium.com/dkatalis/6-lesser-known-best-practices-in-dbt-data-build-tool-f94687abf89d
author:
  - "[[Rizal Ardiyanto]]"
published: 2023-10-21
created: 2026-04-07
description: 6 “Lesser Known” Best Practices in DBT (Data Build Tool) Step up your DBT game with these tips! Data Build Tool (DBT) has emerged as a go-to framework for data engineers, analysts, and data …
tags:
  - clippings
  - dbt
  - best-practices
topic:
type: note
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)## [DKatalis](https://medium.com/dkatalis?source=post_page---publication_nav-a639e354dffe-f94687abf89d---------------------------------------)

[![DKatalis](https://miro.medium.com/v2/resize:fill:76:76/1*CWXOTJHAxS3M5o5iUPqiJg.png)](https://medium.com/dkatalis?source=post_page---post_publication_sidebar-a639e354dffe-f94687abf89d---------------------------------------)

DKatalis is a highly adaptive tech company, driven to solve problems through tech and data.

## Step up your DBT game with these tips!

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gIYy-dgmBbC12aCVhyQXcA.png)

Data Build Tool (DBT) has emerged as a go-to framework for data engineers, analysts, and data scientists alike. Its open-source nature, flexibility, and support for source control have made it a strong addition in the modern data stacks.

If you are a serial user of DBT (Data Build Tool), you probably have already heard about these DBT practices. But, there are 6 lesser known practices when using DBT that I’m going to share:

### 1\. Adopt “Incremental” models for faster builds

DBT's default mode of operation is to build all the models from scratch every time you execute a dbt run command.

This can be resource-intensive and time-consuming, especially as your project grows. To optimize it, consider adopting “incremental” models. With this DBT only processes the data that has changed since the last run.

To do this you can simply do the following:

```c
{{  config( materialized='incremental') }}

< insert your dbt sql query here>
```

This will significantly reduce build times and save valuable computing resources.

### 2\. Use macros for code reusability

DBT macros are reusable code snippets that can simplify your ETL pipelines.

By creating macros for common tasks, you can reduce redundancy in your project and make it more maintainable. For example, hypothetically if you frequently need to count rows of a certain table for a specific date, you can create a macro that encapsulates this logic (see below).

```c
{% macro get_table_row_count(table_name, selected_date) %}

SELECT row_count
FROM {{ table_name }}
WHERE business_date = '{{ selected_date }}'

{% endmacro %}
```

Macros not only improve code quality but also save you time and effort.

### 3\. Explore custom materializations

DBT supports various materialization types, including tables, views, and ephemeral models.

Custom materializations allow you to define how DBT should store and query your data models. While the default materialization type may suffice for most use cases, there are situations where custom materializations can offer significant advantages (e.g. you want to update ONLY the target table without inserting new data). Below is an example of a modified “incremental” materialization template, just to give you an idea.

```c
{% materialization modified_incremental, adapter='bigquery' %}

{%- set existing_relation = load_relation(this) %}
{%- set tmp_relation = make_temp_relation(this) %}
{%- set raw_partition_by = config.get('partition_by', none) -%}
{%- set partition_by = adapter.parse_partition_by(raw_partition_by) -%}
{%- set cluster_by = config.get('cluster_by', none) -%}

{{- run_hooks(pre_hooks) -}}

{%- call statement('main') -%}
  {{ template_query }}
{% endcall %}

{{ run_hooks(post_hooks) }}

{% set target_relation = this.incorporate(type='table') %}
{% do persist_docs(target_relation, model) %}
{{ return({'relations': [target_relation]}) }}

{% endmaterialization %}
```

With custom materializations, you can fine-tune DBT to meet your project's unique requirements.

### 4\. Leverage custom DBT tests for data quality validation

Anyone working with Data must have experienced some sort of trivial (or critical) data issues.

DBT provides a powerful testing framework that allows you to define and run tests on your data models. This feature is sometimes overlooked but can be a game-changer for ensuring the integrity of your data.

By writing custom tests, you can check for data consistency, accuracy, and completeness beyond the conventional NULL or accepted values checks.

```c
## Example of not null test for partitioned table with row_condition

tests:
- partitioned_not_null:
  partitioned_column: column1
  row_condition: ‘status NOT IN(‘ACTIVE’)’

## More complex custom test using dbt_expectations package

tests:
- dbt_expectations.expect_table_row_count_to_equal_other_table:
  compare_model: source(“main_table”, “column1”)
  row_condition: business_date = ‘{{ vars(‘this_date’) }}’
  compare_row_condition: >
    business_date = ‘{{ this_date }}’
    AND column2 IN(
      select DISTINCT column2
      from {{ secondary_table }} a
      LEFT JOIN
        {{ third_table }} b
      ON a.column2 = b.column2
      where status = ‘ACTIVE’
    )
```

By incorporating testing into your DBT workflow, you can catch data issues early in the development process, saving you time and headaches down the line.

### 5\. Document your project thoroughly

Documentation is often underestimated in the world of data analytics, but it plays a crucial role in maintaining a healthy and growing DBT project.

Comprehensive documentation helps both current and new team members to understand the project’s structure, logic, and purpose. DBT provides tools for documenting your project, including the “dbt Docs” feature, which generates interactive documentation from your code and metadata.

Take your time to write clear descriptions for your models, columns, and tests.

### 6\. Implement Git best practices for version control

This may not be entirely DBT, still a good one to hear out.

DBT projects are typically managed using Git, a distributed version control system. While Git is a powerful tool, it can become unwieldy without proper organization. To maintain a clean and efficient version control system, adhere to Git best practices, e.g. create branches for each new feature or bug fix, and use meaningful commit messages, establish a branching strategy that suits your team’s needs (i.e. Gitflow).

By following these Git best practices, you’ll ensure that your DBT project remains well-structured and easy to manage.

### Conclusion

In conclusion, DBT is a powerful tool for managing data workflows.

By embracing incremental models, using macros, exploring custom materializations, testing for data quality, documenting your project thoroughly and following Git best practices, you can elevate your DBT skills and create more robust and efficient data pipelines.

Hopefully these lesser-known best practices will help you further in your DBT journey and unlock the true potential of your data. May you find these tips insightful!

*Want more lesser known yet insightful tips right from the brilliant minds of our Katalis?* [**Follow us!**](https://medium.com/dkatalis)

[![DKatalis](https://miro.medium.com/v2/resize:fill:96:96/1*CWXOTJHAxS3M5o5iUPqiJg.png)](https://medium.com/dkatalis?source=post_page---post_publication_info--f94687abf89d---------------------------------------)

[![DKatalis](https://miro.medium.com/v2/resize:fill:128:128/1*CWXOTJHAxS3M5o5iUPqiJg.png)](https://medium.com/dkatalis?source=post_page---post_publication_info--f94687abf89d---------------------------------------)

[Last published Dec 11, 2025](https://medium.com/dkatalis/the-3-year-routing-mistake-that-festered-under-the-rug-a5a8bfc07ada?source=post_page---post_publication_info--f94687abf89d---------------------------------------)

DKatalis is a highly adaptive tech company, driven to solve problems through tech and data.

[![Rizal Ardiyanto](https://miro.medium.com/v2/resize:fill:96:96/0*uF_x2LU405gNOodB)](https://medium.com/@rizal.ardiyanto?source=post_page---post_author_info--f94687abf89d---------------------------------------)

[![Rizal Ardiyanto](https://miro.medium.com/v2/resize:fill:128:128/0*uF_x2LU405gNOodB)](https://medium.com/@rizal.ardiyanto?source=post_page---post_author_info--f94687abf89d---------------------------------------)

[1 following](https://medium.com/@rizal.ardiyanto/following?source=post_page---post_author_info--f94687abf89d---------------------------------------)