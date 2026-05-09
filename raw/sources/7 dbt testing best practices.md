---
title: 7 dbt testing best practices
source: https://www.datafold.com/blog/7-dbt-testing-best-practices/
author:
  - "[[Gleb Mezhanskiy]]"
published: 2024-05-07
created: 2026-04-07
description: Learn best practices for how to write and manage dbt tests in your organization.
tags:
  - clippings
  - dbt
  - best-practices
topic:
type: note
---
![](https://www.datafold.com/images/Hero-2_1.avif) ![7 dbt testing best practices](https://cdn.prod.website-files.com/66e408a2a1c53743a642f485/674754f3baef51bb9b76b11a_seven-dbt-testing-best-practices.png)

An effective testing strategy is key to shipping high-quality data products with confidence. It can help increase team velocity while minimizing thrash and firefighting related to data quality issues. However, given the complexity of data and the abundance of various testing techniques, the task can seem overwhelming. In this post, we cover the best practices for implementing an effective data testing strategy with dbt:

1. [Shift testing your dbt models](https://www.datafold.com/blog/shifting-data-quality-to-the-left-a-four-level-framework) to the left
2. Build a foundation with generic dbt tests
3. Leverage [unit testing](https://www.datafold.com/blog/dbt-unit-testing-definitions-best-practices-2024) for complex code logic
4. Use data diffing to test for unknown unknowns
5. Work smarter, not harder (aka, don’t write every test in the book)
6. Always, always test your data during CI
7. It sounds obvious, but don’t deploy failed PRs But before we dive in, let’s start by better understanding the different types of dbt tests that exist for your project.

## What is dbt testing

Data testing is the process of ensuring data quality by validating the code that processes data **before it is deployed to production**, and dbt testing aims to prevent data quality regressions when data-processing code (dbt SQL) is written or modified.

Data testing is all about proactively identifying issues before they even happen.

Data testing can help detect and prevent issues like:

1. A change in a SQL column definition causing a significant change in a critical business metric
2. Code refactoring causing an unexpected change in a KPI downstream
3. Column renaming breaking a downstream dashboard or reverse ETL sync to Salesforce

## dbt testing vs. data observability: Prevention vs. detection

You’ve probably also heard of data observability, but it’s not the same as data testing. Data observability is about continuously monitoring the state of data already in production (e.g., what tables are there and what kind of data is in them) and identifying anomalies.

Observability helps identify live data quality issues in real-time, like identifying if:

1. A column has an unusual % of NULL values since yesterday
2. An analytics event stopped sending
3. A rollup of a revenue column is half of the expected value While testing and observability are essential pillars of a data quality strategy, focusing on **preventing data quality issues with testing** allows us to eliminate most of the problems. It makes data monitoring in production more valuable by reducing the noise and thrash of dealing with production incidents.

## #1: Shift data quality to the left with dbt testing

Implementing testing allows data quality to be [shifted to the left](https://www.datafold.com/blog/the-day-you-stopped-breaking-your-data) in the development workflow.

With dbt testing, you can validate your data transformations as part of your development cycle, ensuring that any errors or discrepancies are identified before they propagate downstream. This preventative approach not only improves the reliability of your data pipelines but also streamlines the debugging process, saving time and resources in the long run.

As a bonus, by embedding testing into your development workflow, it encourages a culture of higher data quality standards within and beyond your data team.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/66e408a2a1c53743a642f485/66feb038a8e6d3a1da8e6bad_66fa177f9e2fc9c291313347_663a6a52c9aa5ffceecae3d8_image2.png)

## #2: Add essential dbt tests

It’s often tempting in data testing—just as in standard software development testing—to start with the most complex cases and tests. (After all, the more tests the better, right? Right?) Before long, analytics and data engineers get mired in the minute details of these scenarios, and their test writing gets stalled. Instead, it’s best to start simple.

Start with the most basic tests before moving to more advanced tests that deal with business logic. Begin by validating the structure and assumptions made of the data. If the basic assumptions of the data are wrong, this will affect the usefulness of any advanced tests built on top of these assumptions.

### Example - eCommerce

We’re going to use an ecommerce store selling widgets as an example to illustrate best practices. A sales manager comes to us asking which widgets were sold when and for how much to determine revenue by product per month. We have our transaction data in a fact table and our product information in a dimensional model, table but how do we know this data will stay reliable over time?

Let’s take a closer look at how a proper dbt testing strategy can help us prevent many common problems when delivering and querying such data.

#### Transactions Table

transaction\_idtransaction\_dateproduct\_idquantityamount34983282022-01-0155105.5598273462022-02-1723215.8912393832022-03-151256.99

#### Product Table

product\_idproduct\_nameproduct\_categorylaunch\_date55widget\_4AB1002021-01-0123widget\_2NB5002020-07-01

#### Analytical query: “Monthly Product Sales Report”

The following query illustrates a common analytical scenario for how this data is queries for analysis used.

`SELECT       p.product_name,       YEAR(f.transaction_date) as sales_year,       MONTH(f.transaction_date) as sales_month,       SUM(f.amount * f.quantity) as monthly_sales FROM       fact_transactions as f INNER JOIN       dim_products as p ON f.product_id = p.product_id GROUP BY       p.product_name,       YEAR(f.transaction_date),       MONTH(f.transaction_date) ORDER BY       sales_year,       sales_month DESC` The result of this Monthly Product Sales report SQL query would look like this:

product\_namesales\_yearsales\_monthmonthly\_salesWidget\_42022035,600.00widget\_220220410,500.00

### dbt generic tests

A good place to start is to implement [generic](https://docs.getdbt.com/docs/building-a-dbt-project/tests#generic-tests) dbt tests – modular, reusable tests for ensuring data reliability and integrity. dbt has four generic tests that come out of the box, and they can be deployed with minimal configuration:

1\. [not\_null](https://docs.getdbt.com/reference/resource-properties/tests#not_null): A null value in data indicates that a value in a column is missing or unknown. While sometimes null values are intentional and desired, they often suggest a data issue. This kind of test identifies where null values exist in a given column. Adding a not\_null test to the primary key for every model to ensure PKs are not null is a great way to avoid gnarly (and often easily preventable) data quality incidents.

For example, our imaginary Monthly Product Sales report would likely be affected by NULL values in the product\_id column. If the “product\_id” column contained NULL values, those sales would likely be omitted from an analytical query.

\` version: 2

models: - name: fact\_transactions columns: - name: product\_id tests: - not\_null \`2. [unique](https://docs.getdbt.com/reference/resource-properties/tests#unique): This test ensures that a dataset does not contain duplicate values or rows. This is important because duplicate primary keys can lead to massive issues, causing fanouts in joins and misleading data metrics.

The example dim\_products table is particularly susceptible to duplicate “product\_id” values, which would seriously impact our analytical query. If duplicate values existed, this would inflate the numbers reported in our Monthly Product Sales because each row in our fact\_transactions table would be duplicated during the table join.

\` version: 2

models: - name: fact\_transactions columns: - name: product\_id tests: - not\_null \`

Without this example unique test for our dim\_products table, we could end up with duplicate product\_id records. For example, we might have a scenario in which product\_id 55 is reused in the table.

product\_idproduct\_nameproduct\_categorylaunch\_date55widget\_4AB1002021-01-0123widget\_2NB5002020-07-0155widget\_5ZB9002021-05-01

When our analytics query runs to populate the Monthly Product Sales report, the join between the dim\_products and the fact\_transactions tables now inflates our sales numbers by duplicating all records in fact\_transactions that have a product\_id of 55.

3\. [accepted\_values](https://docs.getdbt.com/reference/resource-properties/tests#accepted_values): This test verifies that all column values across all rows are in the set of valid values. For example, our product\_category column might only have two valid values (AB100, NB500). If this test uncovers any values in the product\_category column that are not one of these two, it will fail.

\` version: 2

models: - name: dim\_products columns: - name: product\_category tests: - accepted\_values: values: \[‘AB100’, ‘NB500’\] \`4. [relationships](https://docs.getdbt.com/reference/resource-properties/tests#relationships): This test verifies referential integrity, ensuring all of the records in a table have a corresponding record in another upstream table that is expected to be joined to the former (or simply is considered the source of truth). We could use this test to check that all product\_id values in our fact\_transactions table exist in the dim\_products table.

\` version: 2

models: - name: fact\_transactions columns: - name: product\_id tests: - relationships: to: ref(‘dim\_products’) field: product\_id \`

For example, it would be a common data bug if new sales were recorded in our fact\_transactions table with a product\_id that did not exist in our dim\_products table.

transaction\_idtransaction\_dateproduct\_idquantityamount34983282022-01-0155105.5576958422022-02-020146.99

The above example shows that product\_id 01 does not exist in dim\_products. As a result, our Monthly Product Sales report will underreport our sales. This is why relational integrity checks are so important for catching hard-to-detect problems introduced into a dataset.

### Custom generic dbt tests

When more complex logic or validation criteria are needed, data practitioners can write their own custom generic tests. These tests are written with Jinja, a templating language combined with SQL, as part of your dbt project in either your / **tests** or / **macros** subdirectories.

When examining our table fact\_transactions and the Monthly Product Sales analytics, along with the basic dbt testing we already implemented, data issues and business rules might not fit well into these simple tests.

For example, let’s say the business requires we have no orders for over 500 units, as the company cannot fulfill such large orders with current inventory levels. This is the perfect use case for customer generic tests.

We could write the following custom test for verifying that none of the orders coming into our fact\_transactions table exceed the 500 unit order quantity:

\`

{% test order\_limit(model, column\_name) %}

with validation as ( select {{ column\_name }} as limit\_field from {{ model }} ),

validation\_errors as ( select limit\_field from validation where limit\_field > 500 )

select \* from validation\_errors

{% endtest %} \`This custom generic test can now be used in a model:

\` version: 2

models: - name: fact\_transactions columns: - name: quantity tests: - order\_limit \`

### Singular tests

One can write a [singular test](https://docs.getdbt.com/docs/building-a-dbt-project/tests#singular-tests) when a testing scenario is unique to a mode. Such a test is based on a specific SQL statement, which should return no records if successful and otherwise return failing records. For example, ensure that no order has a negative order quantity:

\` select transaction\_id, from {{ ref(‘fact\_transactions’ )}} where quantity

#### Tip: Use extensions for writing dbt data tests faster

As an open-source framework, dbt is easily extensible with packages that can be discovered through [dbt Package hub](https://hub.getdbt.com/). Two packages can be beneficial in simplifying the writing of data tests, including [dbt-expectations](https://www.datafold.com/blog/dbt-expectations) and [dbt-utils](https://www.datafold.com/blog/top-dbt-utils-and-how-to-use-them-in-your-project#generic-testing).

## #3 Add unit tests for complex SQL logic

[dbt unit tests](https://www.datafold.com/blog/dbt-unit-testing-definitions-best-practices-2024) are dbt tests that validate the model logic with predefined inputs and outputs.

Unlike a “classic” dbt data test, which runs an assertion against a model built with database data, unit tests require the developer to define “test cases” with input data and expected output. Thus, they allow more granular testing and isolate the validation of source data from the validation of the model code itself.

`unit_tests:   - name: test_employee_seniority_and_department     description: "Check if the seniority and department are correctly derived from the employee's title"     model: dim_employees     given:       - input: ref('stg_employees')         rows:           - {employee_id: 1, first_name: 'Buzz', last_name: 'Lightyear', title: 'Chief Financial Officer'}           - {employee_id: 2, first_name: 'Elsa', last_name: 'Arendelle', title: 'Marketing Manager'}           - {employee_id: 3, first_name: 'Woody', last_name: 'Pride', title: 'Senior Software Engineer'}           - {employee_id: 4, first_name: 'Mulan', last_name: 'Fa', title: 'HR Coordinator'}           - {employee_id: 5, first_name: 'Simba', last_name: 'Pride', title: 'Sales Representative'}     expect:       rows:         - {employee_id: 1, seniority: 'Executive', department: 'Finance'}         - {employee_id: 2, seniority: 'Manager', department: 'Marketing'}         - {employee_id: 3, seniority: 'Individual Contributor', department: 'Engineering'}         - {employee_id: 4, seniority: 'Individual Contributor', department: 'Human Resources'}         - {employee_id: 5, seniority: 'Individual Contributor', department: 'Sales'}`

## #4 Implement data diffing to achieve 100% test coverage

Data Diff is a value-level and statistical comparison of datasets. When developing and deploying your dbt models, data diff can be leveraged to compare the data in production (the ground truth) and development/staging, allowing the developer and the code reviewer to fully assess the nature and impact of changes to the business logic.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/66e408a2a1c53743a642f485/66feaffec0bae0325b205628_66fa177f9e2fc9c291313353_663936373f21e0cb040a672a_data_diff_new.png)

[Implemented in CI](https://www.datafold.com/data-deployment-testing/) and coupled with [column-level lineage](https://www.datafold.com/data-knowledge-graph/) that extends to BI integrations, data diff safeguards against unforeseen changes, reducing the time needed to review and test the code and accelerating the overall team velocity.

## \# 5 Apply each test type smartly (aka work smarter, not harder)

This post covered three testing types: dbt data tests, dbt unit tests, and data diffing. Knowing when each testing technique is appropriate and understanding its powers and limitations is essential to implementing an effective testing strategy that utilizes all three types of dbt testing to maximize each method’s impact and ROI.

For that, let’s compare each testing type in terms of implementation effort, coverage, specificity and ideal application:

**dbt data tests** **dbt unit tests** **Data Diff** **Effort to implement** Medium

Requires test cases to be written High

Requires test cases and input/output dataset curation Low

Requires no manual test set-up **Expected code coverage** Medium

Relatively easy to add generic tests that cover data quality fundamentals Low

Due to the lift required to build them, unit tests are often only applied to the most complex or business-critical logic logic High

Automatically catches all changes to your data **Specificity (how clear are test results)** Medium

Reacts to changes in code and data High

Focused on testing code given fixed input Medium

Requires the user to interpret acceptable-ness of data differences **Use Case** Testing general rules such as not-nullness, uniqueness, value ranges, and referrential integrity Testing complex business logic Understanding the potential impact from your code change on your data and downstream assets **Scalibility with data volume** Low

Can slow down your project if tested rows becomes too large Excellent

Independent of data volume since test rows are defined by the user Excellent

Scales well with filtering and sampling

Considering the relative advantages of each testing type, the following simple rules help create an effective data quality strategy:

1. Write unit tests for a small share of critical/complex business logic – they are harder to implement but are the most precise type of testing.
2. Write data tests for essential quality checks, such as checking for uniqueness, non-null, referential integrity and other basic expectations of your models. Data tests are easy to add for simple testing cases.
3. Use data diff for most “unknown unknowns” that make up data quality issues. By highlighting how the data changes when the code is modified, data diff helps you catch the long tail of unexpected data quality issues and regressions that wouldn’t be picked up by traditional data or unit tests.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/66e408a2a1c53743a642f485/66feafffc0bae0325b20563f_66fa177f9e2fc9c291313350_66393b5e2f194b1a517984e3_testing_hierarchy.png)

## #6 Run tests in CI to provide guardrails

CI stands for Continuous Integration, a software development practice where developers frequently merge code changes into a shared repository. Each proposed integration (pull/merge request) can then be verified by an **automated build and automated tests**. In data and analytics engineering, CI aims to improve data quality and team velocity and reduce the time it takes to validate and deploy dbt code updates.

In other words, CI is an automated process that runs all tests and validations for every proposed code change before it’s merged and deployed to production.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/66e408a2a1c53743a642f485/66feb038a8e6d3a1da8e6bb6_66fa89d52a834cd16f13685a_6620421ed9ed5098cc81e424_Screenshot%2525202024-04-17%252520at%2525202.41.33%252520PM.png)

#### I have dbt tests, why do I need CI?

Having dbt tests is like having a fire extinguisher at home. It’s useful for tackling fires when they occur, but it relies on your vigilance and immediate action to be effective. On the other hand, having CI is like having a comprehensive home security system. It not only detects fires but also takes proactive measures to suppress them, alerts emergency services, and operates round-the-clock, providing peace of mind and enhanced protection for your data environment.

While dbt data and unit tests are examples of validation techniques that can be applied to code changes, having those tests defined in the dbt project without CI means relying on each developer to execute all required tests manually, ensuring successful results and addressing issues before merging the code, which is a highly brittle process. As the complexity of dbt project grows beyond a few models and contributors, slips are inevitable and the negative impact can be significant.

Running your dbt build (which will run your dbt tests) and data diffs during [your CI process](https://www.datafold.com/blog/why-you-should-care-about-ci/#anatomy-of-an-effective-ci-pipeline) ensures every single PR undergoes the same standard of testing (and scrutiny), creating a more governable system for code changes.

## #7 Never deploy with failing tests

This advice stems from the Broken Window Theory, is a criminological concept proposed by James Q. Wilson and George L. Kelling in the early 1980s and that significantly influenced policing and urban policy in New York City, particularly during the 1990s. The name comes from a metaphor that a window left broken in a community shows an apparent lack of care and attention, thereby fostering an environment where people feel more inclined to break more windows or commit more serious crimes.

In the context of dbt testing, this means that the team should ensure that tests are always passing and never deploy with failing tests. It is easier said than done because in a large dbt project with hundreds/thousands of models, the probability of a particular test failing is quite high. Yet, if you once proceed with merging despite a failing test “we all know this one test is noisy, so we just been ignoring it”, you step (and set your team) on a slippery slope of allowing more and more tests to fail eventually leading to tests not being taken seriously and significant data quality issues slipping through.

### How to avoid broken tests

It’s quite simple. When a data or a unit test fails, you have following options:

1. **Investigate the test**
- If it’s a dbt data test, check if it’s failing because of a change in the underlying data
- If it’s a dbt unit test, that means you introduced a code change that breaks previous assumptions of how the code should work.
1. **Ask your team**
- Check the model and test owner, or do a git blame if the owner is unclear, to consult with whomever wrote the original code and test.
1. **Fix the code or the test**
- Change your code if you believe that the test condition is relevant.
- Change the test itself if the expected output is now different.
- Remove the tests; some tests are inherently noise, poorly-defined, or redundant. It’s ok to remove a test if you believe it’s not adding incremental value.

## Conclusion

Let’s take a step back for a second.

Optimizing for data quality has been (and likely will remain) an ongoing battle for data practitioners. We can list the best ways to safeguard your dbt project and analytics work from data quality issues, but we acknowledge that no data team or dbt project is perfect. Tests will fail. PRs may need to be reverted, and hotfixes added. And data quality issues will still exist.

What we can control, however, as data practitioners is adopting best practices over time that enforce scalable and standardized testing methods that grow with your team and data. So one day, those data quality issues might exist, but maybe they don’t happen as often or on nearly as large of a scale:).

So to summarize, for your dbt project, we recommend:

1. **Shifting data quality checks to the left**
2. **Adding dbt generic tests for your important columns**
3. **Adding unit testing to validate your more complex code logic**
4. **Implementing data diffing to safeguard against all unknown unknowns**
5. **Not overdoing it: Not every single column needs every single test; save your team’s time and your warehouse’s compute costs**
6. **Implementing CI; we cannot emphasize this enough, this is the singular best practice that will enable your team to find data quality issues before they enter your production space**
7. **Creating a solid foundation, and avoiding deploying failed PRs**