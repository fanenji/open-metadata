---
type: source
title: "Source: 6 “Lesser Known” Best Practices in DBT (Data Build Tool).md"
created: 2026-05-06
updated: 2026-05-06
sources: ["6 “Lesser Known” Best Practices in DBT (Data Build Tool).md"]
tags: []
related: []
---

# Source: 6 “Lesser Known” Best Practices in DBT (Data Build Tool).md

## Key Entities

**People & Organizations**
* **Rizal Ardiyanto (Person):** Author of the article; peripheral role.
* **DKatalis (Organization):** The tech company that published the article; peripheral role.

**Products & Tools**
* **dbt / Data Build Tool (Tool):** The central subject of the article; the primary framework for data transformation. (Already in Wiki)
* **Git (Tool):** A version control system recommended for managing dbt projects. (Peripheral)
* **BigQuery (Product):** A data warehouse mentioned in a code example for custom materialization. (Peripheral)
* **dbt_expectations (Package/Tool):** A dbt package used for advanced data testing. (Peripheral)

## Key Concepts

**Techniques & Methods**
* **Incremental Models:** A method of processing only new or changed data since the last run to optimize performance and resource usage. (Central)
* **Macros:** Reusable SQL snippets used to implement the DRY (Don't Repeat Yourself) principle in ETL pipelines. (Central)
* **Custom Materializations:** Advanced configurations that define unique ways for dbt to store and query data models beyond standard tables or views. (Central)
* **Custom dbt Tests:** Advanced data validation logic that goes beyond simple null or uniqueness checks to ensure complex data integrity. (Central)
* **dbt Docs:** An automated feature that generates interactive documentation from dbt code and metadata. (Central)
* **Gitflow (Branching Strategy):** A specific Git workflow/strategy recommended for maintaining organized and scalable dbt projects. (Central)

**Data Management Principles**
* **Data Quality/Integrity:** The overarching goal of using custom tests to catch errors early. (Central)
* **Code Reusability:** The principle of using macros to reduce redundancy. (Central)

## Main Arguments & Findings

The core argument is that while basic dbt usage is common, mastering "lesser-known" advanced features is essential for scaling data engineering workflows.

**Core Claims:**
1. **Performance Optimization:** Using **incremental models** is critical for reducing build times and computing costs as datasets grow.
2. **Maintainability:** Implementing **macros** and **Git best practices** (like Gitflow) reduces code redundancy and project complexity.
3. **Data Reliability:** Moving beyond standard tests to **custom tests** (and using packages like `dbt_expectations`) is a "game-changer" for catching critical data issues.
4. **Project Sustainability:** Thorough **documentation** via dbt Docs is vital for long-term maintenance and team onboarding.

**Evidence Strength:**
The evidence is **moderate**. The author provides concrete code snippets (SQL/Jinja) for incremental models, macros, custom materialization, and testing, which demonstrates the practical application of the claims. However, the claims are based on professional experience/best practices rather than empirical large-scale studies.

## Connections to Existing Wiki

* **[[dbt]]:** This source serves as a direct extens
