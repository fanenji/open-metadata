---
title: "Best Practices for Workflows: A Guide to Effective dbt Use"
source: https://medium.com/@turkelturk/best-practices-for-workflows-a-guide-to-effective-dbt-use-fa925127647c
author:
  - "[[Turkel]]"
published: 2024-01-14
created: 2026-04-07
description: "Best Practices for Workflows: A Guide to Effective dbt Use Introduction Analytics teams are constantly seeking ways to enhance their efficiency and output quality. This article compiles the best …"
tags:
  - clippings
  - dbt
  - best-practices
topic:
type: note
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*mdl95QFN_hh_m-0A.png)

## Introduction

Analytics teams are constantly seeking ways to enhance their efficiency and output quality. This article compiles the best practices from experienced dbt users, providing insights into effective workflow management in analytics projects. By adhering to these practices and implementing the suggested pro-tips, your dbt projects will not only be efficient but also polished and professional.

## Best Practice Workflows in dbt

### 1\. Version Control Your dbt Project

- **Git Branches:** Manage development of new features and bug fixes through Git branches.
- **Pull Requests:** Ensure all code changes undergo a review before merging into the master branch.

*Example*: Create a Git branch named `feature/new_customer_segmentation` for developing a new customer segmentation model. Use pull requests for code reviews before merging into the master branch.

> Refer to codified best practices from dbt in [Git guide](https://github.com/dbt-labs/corp/blob/main/git-guide.md) for more details.

### 2\. Separate Development and Production Environments

- Utilize targets within a profile in dbt for different environments.
- Use a `dev` target for command line runs and a `prod` target for production deployments.
- Learn more [about environment management here](https://docs.getdbt.com/docs/environments-in-dbt).

*Example*: Configure two targets in your `profiles.yml` - `dev` for local testing with mock data and `prod` for live data processing.

### 3\. Adopt a Style Guide

- Codify SQL styles, field naming conventions, and rules.
- This is crucial for projects with multiple dbt users.
- Check out [public style guide by dbt](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects) as a starting point for your own.

*Example*: Define a rule such as all timestamp fields should be suffixed with `<event>_at` (e.g., `created_at`, `updated_at`).

## Best Practices in dbt Projects

### 1\. Utilize the ref Function

- The [ref](https://docs.getdbt.com/reference/dbt-jinja-functions/ref) function is a cornerstone in dbt, enabling correct model build order and environment-specific table selection.
- Always use the `ref` function over direct relation references.

*Example*: Instead of querying `SELECT * FROM my_schema.my_table`, use `{{ ref('my_model') }}` in your dbt models.

### 2\. Limit References to Raw Data

- Reference raw data in one place to ease updates.
- Avoid direct relation references in models.

*Example*: Define a source for your raw data once, like `{{ source('raw_data', 'user_table') }}`, and use this reference across models.

> As of v0.13.0, dbt recommends defining your raw data as [sources](https://docs.getdbt.com/docs/build/sources), and selecting from the source rather than using the direct relation reference.

### 3\. Rename and Recast Fields Once

- Transformations should select from one source, rename fields and tables, and recast fields into the correct data type.
- Follow this approach for consistency and reduced code duplication.

*Example*: In your first transformation layer, change `usr_name` to `user_name` and convert timestamp fields to UTC.

### 4\. Break Complex Models into Smaller Pieces

- Separate CTEs into different models for clarity and reduced code duplication.
- This approach also aids in independent testing and understanding of the SQL code.

*Example*: If a model has multiple CTEs, separate them into individual models named `intermediate_event_processing` and `final_event_aggregation`.

### 5\. Group Models in Directories

- Use directories within the `models/` dirctory for organization.
- This helps in model configuration, running subsections of your DAG, and communicating modeling steps.

*Example*: Store all staging models under `models/staging/` and all analytical models under `models/analytics/`.

### 6\. Add Tests to Your Models

- dbt’s framework allows testing of model results and source data.
- Ensure every model has primary key tests for uniqueness and non-null values.

*Example*: For a model `dim_users`, add a test to ensure the `user_id` field is always unique and not null.

### 7\. Consider the Information Architecture of Your Data Warehouse

- Use [custom schemas](https://docs.getdbt.com/docs/build/custom-schemas) and prefixes in table names for clarity and organization.
- Choose materializations (views, tables, incremental models) wisely based on query performance and build time.

## Pro-tips for dbt Workflows

### 1\. Use Model Selection Syntax for Local Runs

- Optimize development by running only the model you’re working on and its downstream models. For syntax see dbt’s [model selection syntax](https://docs.getdbt.com/reference/node-selection/syntax).

*Example*: Run `dbt run -m +model_you_are_working_on` to execute your model and its dependencies.

### 2\. Run Only Modified Models (Slim CI)

- Use dbt’s capability to run and test only modified models in a sandboxed environment.
- This approach saves time and resources, particularly for small changes.

*Example*: Use `dbt run -m state:modified` to build only models that have changed since the last production run.

### 3\. Use Source Freshness for Smarter Reruns

- Compare sources.json artifacts to determine fresher sources and run downstream models based on them.
- Refer to the dbt documentation on state for more information.

## Pro-tips for dbt Projects

### 1\. Limit Data Processed in Development

- Speed up runs by limiting data based on the target name in development environments.

*Example*: Add a condition in your SQL like `{% if target.name == 'dev' %} LIMIT 1000 {% endif %}` to process fewer rows in development.

### 2\. Use Hooks for Managing Privileges

- Apply grant statements through hooks for consistent permission management on dbt-created objects.

*Example*: In your `dbt_project.yml`, add a post-hook like `grant select on {{ this }} to user_role` to manage access to the created models.

### 3\. Separate Source-Centric and Business-Centric Transformations

- Distinguish between transformations for source consistency and business-specific models.
- This clarity enhances understanding and management of data models.

*Example*: Create initial models like `stg_users` for source alignment, then build `dim_users` for business-focused transformations.

### 4\. Managing Whitespace in Jinja

- Control unwanted whitespace in compiled SQL when using Jinja and macros. Familiarize yourself with Jinja documentation to effectively manage this aspect.

*Example*: Use Jinja’s `{%-` and `-%}` to strip unnecessary whitespaces in your SQL code.

## Conclusion

These best practices and pro-tips for dbt workflows are designed to streamline analytics processes, enhance data model quality, and foster efficient team collaboration. By adopting these methods, analytics teams can maximize the power of dbt in their projects, leading to more reliable, readable, and maintainable data models. Remember, the key to successful analytics work lies not just in the tools used but in how they are implemented. Therefore, integrating these best practices into your dbt projects will not only improve your workflows but also elevate the overall quality of your analytics output. For more details see [dbt Developer Hub — dbt Docs](https://docs.getdbt.com/docs/collaborate/documentation)

[![Turkel](https://miro.medium.com/v2/resize:fill:96:96/1*UEnFr49qQvoydMkxACDyQg.jpeg)](https://medium.com/@turkelturk?source=post_page---post_author_info--fa925127647c---------------------------------------)

[![Turkel](https://miro.medium.com/v2/resize:fill:128:128/1*UEnFr49qQvoydMkxACDyQg.jpeg)](https://medium.com/@turkelturk?source=post_page---post_author_info--fa925127647c---------------------------------------)

[47 following](https://medium.com/@turkelturk/following?source=post_page---post_author_info--fa925127647c---------------------------------------)