---
title: Testing Dbt Macros
source: https://blog.dataengineerthings.org/testing-dbt-macros-a80e76243ae4
author:
  - "[[Leo Godin]]"
published: 2024-01-12
created: 2026-04-07
description: Testing Dbt Macros You do test, right? Not a Medium member? No problem. Read free here. Sure, dbt has data-quality tests built in, but that isn’t enough to create reliable data pipelines. We need …
tags:
  - clippings
  - dbt
topic:
type: note
---
[Sitemap](https://blog.dataengineerthings.org/sitemap/sitemap.xml)## [Data Engineer Things](https://blog.dataengineerthings.org/?source=post_page---publication_nav-f2ba5b8f6eb3-a80e76243ae4---------------------------------------)

[![Data Engineer Things](https://miro.medium.com/v2/resize:fill:76:76/1*HtZXPy85bDrTZm9tMXi6aQ.png)](https://blog.dataengineerthings.org/?source=post_page---post_publication_sidebar-f2ba5b8f6eb3-a80e76243ae4---------------------------------------)

Things learned in our data engineering journey and ideas on data and engineering.

## You do test, right?

*Not a Medium member? No problem. Read free* [*here*](https://blog.det.life/testing-dbt-macros-a80e76243ae4?sk=c48259c2258d7d8a97787b2fb3e4e897)*.*

Sure, dbt has data-quality tests built in, but that isn’t enough to create reliable data pipelines. We need to validate our code. Let me repeat. We need to validate our code. Fortunately for us, there are simple patterns for ensuring the macros we write do exactly what we expect them to do. Let’s dive in with a scenario.

### The Scenario

Here at Moon Walks, the premier online shoe retailer for men who only walk outside during full moons, we process mounds of data every night. To ensure idempotency and efficiency, we need to specify specific date ranges in our models and tests. Our macros appear to work, but sometimes logic errors are found. How can we ensure our macros provide the intended results?

Seems reasonable, right? Of course there would be a niche market for men who only walk outside during full moons. It’s 2024 after all. The macro below looks pretty good to me. It takes a Python date object and a date logic as arguments and returns a string representing a date in SQL. Look at the code and tell me if it is correct. Here’s a hint. There is one flaw.

*/macros/get\_model\_start\_date.sql*

```c
{% macro get_model_start_date(run_at_date, date_logic='run_at_day') %}

    {# This is like a Python import statement. Makes calling these functions shorter. #}
    {% set date = modules.datetime.date %}
    {% set timedelta = modules.datetime.timedelta %}

    {# Define any date logics used by your company  #}

    {% if date_logic == 'run_at_day' %}
        {% set start_date = run_at_date %}

    {% elif date_logic == 'run_at_week' %}
        {# Get the beginning of the week, which is always Sunday #}
        {% set start_date = run_at_date - timedelta(days = run_at_date.weekday() ) %}

    {% elif date_logic == 'run_at_month' %}
         {# Build a date using year and month from execution date  #}
        {% set start_date = date(run_at_date.year, run_at_date.month, 1) %}

    {% else %}
        {{ exceptions.raise_compiler_error('get_start_dates: Invalid date logic: ' + date_logic) }}
    {% endif %}

    {% set model_start_date  = "'" + start_date.strftime('%Y-%m-%d') + "'" %}
    {% do return(model_start_date) %}
{% endmacro %}
```

### Why Test Macros

Macros are code blocks that will often be reused in multiple contexts. When we utilize a macro in our project, we need to be confident the macro works. Otherwise, we may introduce bugs. The whole point of macros is to make development easier and conform to standards. Without validating our code, we introduce more complexity and degrade the confidence our co-workers and consumers have in us.

Sure, we could use dbt run-operation a bunch of times with a bunch of inputs. That is one way to test a macro. Not only is that method tedious, but it is also prone to mistakes and requires duplication of effort if we ever modify the macro. Instead, we should have an automated test suite. something we can run before releases to ensure our logic is valid.

To learn more about testing data pipelines, see [this excellent article](https://medium.com/@samzamany/unit-testing-in-data-engineering-a-practical-guide-91196afdf32a) from Sam Zamany

### What To Test

Testing is a bit of an art form. We can go overboard and write tons of tests that provide diminishing returns. Going that route wastes time and often creates a false sense of security. We need to test the core functionality, any paths through the code, and any boundaries. Simple, right? I get it, you’re like, “What the hell does that even mean?” Let’s start from the beginning by looking at the spec for the macro.

> **get\_model\_start\_date:** Used to find the start date to use for loading data into a model. Supports models that load daily, weekly and monthly and should be used with get\_model\_end\_date to get the full date range to load data from. Custom tests can use this macro to only test data that was loaded in the current job.
> 
> **Arguments:**
> 
> run\_at\_date: Python date object representing the day our DAG is running for. This can be the current date or a date in the past.
> 
> date\_logic: String representing the load strategy for the model. (run\_at\_day, run\_at\_week, run\_at\_month). These determine if we should return the run\_at\_day, beginning of the week, or beginning of the month.
> 
> **Returns:** String representing a single SQL date.

From the spec, we see the core functionality is to provide the start date used to load data into a model. Our tests should compare the date returned by the macro to an expected date. There are three paths through the code determined by date logic. We can get a start date using run\_at\_day, run\_at\_week, and run\_at\_month. What about the boundaries?

Boundaries represent the beginning and end of possible ranges. For instance, a macro that takes an integer between 0 and 100 would have 0 and 100 as boundaries. Let’s look at the boundaries for our macro.

- run\_at\_date: There is only one option here. So the boundary is the date provided as an argument to the macro.
- run\_at\_week: The first of the week and the end of the week represent the boundaries.
- run\_at\_month: The first of the month and the end of the month represent the boundaries.

It is generally a good idea to test something in the middle of a boundary, just in case we have hard-coded logic for the boundaries that create more paths through the code. That leaves us with testing the beginning, middle, and end. A test spec might look like this.

![A table showing all the paths through our macro.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_CBY2zWSJEejp27c9p4pcg.png)

A table showing all the paths through our macro.

We have seven test cases representing the beginning, middle, and end dates for each path through our code. We probably could improve this a bit by using different months and years, but this looks good enough. Let’s write some validation tests.

### Finally, Time To Write Code!

The basic pattern I use for testing macros is simple. Create a new model that runs the macro once for every test case, then use dbt tests to ensure the returned value matches the expected value. In this example, we simply union a bunch of SQL. We could use a seed to get arguments and expected returned values, then create a model on top of that. That is a great method for validating custom tests, but seems like overkill for this particular use case.

Here’s the model. Can you see how it sets us up to validate the macro? What dbt tests would you write to ensure expected\_date matches actual\_date?

*/models/validation/validate\_get\_model\_start\_date.sql*

```c
{# Acts like an import statement #}
{% set python_date = modules.datetime.date.fromisoformat %}

-- run_at_day: Simply returns the python date as a string
select 
    'run_at_day' as test_case,
    '2023-12-05' as run_at_date,
    '2023-12-05' as expected_date,
    {{ get_model_start_date(python_date('2023-12-05'), date_logic='run_at_day') }} as actual_date 

union all 

-- run_at_week: Get the Sunday that begins the week 
select 
    'run_at_week_start' as test_case,
    '2023-12-17' as run_at_date,
    '2023-12-17' as expected_date,
    {{ get_model_start_date(python_date('2023-12-17'), date_logic='run_at_week') }} as actual_date 

union all 

select 
    'run_at_week_middle' as test_case,
    '2023-12-21' as run_at_date,
    '2023-12-17' as expected_date,
    {{ get_model_start_date(python_date('2023-12-21'), date_logic='run_at_week') }} as actual_date 

union all 

select 
    'run_at_week_end' as test_case,
    '2023-12-23' as run_at_date,
    '2023-12-17' as expected_date,
    {{ get_model_start_date(python_date('2023-12-23'), date_logic='run_at_week') }} as actual_date 

union all 
-- run_at_month: Should always return the first day of the month
 select 
    'run_at_month_start' as test_case,
    '2023-12-01' as run_at_date,
    '2023-12-01' as expected_date,
    {{ get_model_start_date(python_date('2023-12-01'), date_logic='run_at_month') }} as actual_date 

union all 

select 
    'run_at_month_middle' as test_case,
    '2023-12-15' as run_at_date,
    '2023-12-01' as expected_date,
    {{ get_model_start_date(python_date('2023-12-15'), date_logic='run_at_month') }} as actual_date 

union all 

select 
    'run_at_month_end' as test_case,
    '2023-12-31' as run_at_date,
    '2023-12-01' as expected_date,
    {{ get_model_start_date(python_date('2023-12-31'), date_logic='run_at_month') }} as actual_date
```

### Let’s Add Some Tests

With this pattern, we will generally use expression\_is\_true from dbt\_utils. Unfortunately, the compiled code doesn’t give us any useful information to troubleshoot. Instead, We’ll use a custom [expression\_is\_true](https://github.com/leogodin217/dbt_demos/blob/main/elementary_demo/macros/custom_tests/expression_is_true.sql) test that selects all defined uniqueness columns in the compiled query. We’ll cover how this works in an upcoming post. For now, feel free to use dbt\_utils, copy my test, or write your own.

*/models/validation/validate\_get\_model\_start\_date.yml*

```c
version: 2

models:
  - name: validate_get_model_start_date
    description: Validates the get_model_start_date macro 
    config:
      meta:
        # Used in the custom expression_is_true test I use.
        model_meta:
          uniqueness:
            - test_case
            - run_at_date
            - expected_date
            - actual_date
    tests:
      - expression_is_true:
          # Captures all test cases in case we miss one here
          name: Validate get_model_start_date all test cases 
          expression: expected_date = actual_date
      - expression_is_true:
          name: Validate get_model_start_date run_at_day 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_day' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_week start
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_week_start' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_week middle 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_week_middle' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_week end 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_week_end' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_month start 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_month_start' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_month middle 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_month_middle' 
      - expression_is_true:
          name: Validate get_model_start_date run_at_month end 
          expression: expected_date = actual_date 
          where_clause: test_case = 'run_at_month_end'
```

Notice, we have a catch-all test at the top? While not absolutely necessary, it provides a simple way to catch any test cases we missed in the YAML. It is very easy to miss a test or misconfigure one. The catch all gives us full coverage and the individual tests tell us exactly which one is failing. A few things to note.

- The meta config at the top of the model works with my custom test to ensure we select enough columns to identify which row in our model is failing a test.
- We give the tests a unique name property. This helps with readability and ensures we do not create two tests with the same unique ID. That would cause an error.
- Since these are validation tests, we don’t want to run them in our production runs. We disable the related models and tests in dbt\_project.yml. To run our validation tests, we need to use — vars ‘{run\_validation: true}’
![Snippet from dbt_project.yml disabling the validation folder unless we run dbt with — var ‘{run_validation: True}’](https://miro.medium.com/v2/resize:fit:1272/format:webp/1*N8OZG51FZAPLP2rs7VuTqQ.png)

Snippet from dbt\_project.yml disabling the validation folder unless we run dbt with — var ‘{run\_validation: True}’

### The Results Are In and They Are Awesome!

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vi6AGbLRiqq9Nv1Qzh3NJA.png)

Failed tests? Awesome! We might not have caught this with manual testing. The work we just did caught a bug in our code and will prevent bugs in production. As we say in New Hampshire, that’s wicked awesome!

Console output shows us which tests failed, but it doesn’t show us the values returned from our macro. This is where the custom expression\_is\_true test helps a lot. Let’s look at the compiled query for our catch-all test.

*/target/compiled/validation/validate\_get\_model\_start\_date.yml/Validate get\_model\_start\_date all test cases.sql*

```c
select 
    test_case, run_at_date, expected_date, actual_date 

from (
    select * from \`somedb\`.\`enterprise_sales\`.\`validate_get_model_start_date\`
    
) as subquery
where not (expected_date = actual_date)
```

Let’s compare the results with a calendar. Our weekly tests seem to be returning Monday as the start date when it should give us Sunday. This is why we test boundaries! *I know we shouldn’t use so many exclamation marks, but I’m excited. Testing is wicked awesome!*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0hi7CuyjwHFqxOMIvi3_SA.png)

Let’s go back to the macro. I see the problem. Python uses ISO standards for dates and ISO work weeks start on Monday. Our work week goes from Sunday to Saturday. We can fix this by adding one more day in the timedelta.

```c
{% elif date_logic == 'run_at_week' %}
{# Get the beginning of the week, which is always Sunday #}
{# ISO weeks start on Monday, so we need to go back one more day #} 
{# set start_date = run_at_date - timedelta(days = run_at_date.weekday() ) #}
{% set start_date = run_at_date - timedelta(days = run_at_date.weekday() + 1) %}
```

This is the result we’re looking for. Green is good.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XzgQtv7afMf6Lv4RhCjLHg.png)

### Still Here? Let’s Wrap It Up

We’ve covered a simple way to validate our macros. Using the macro in a model, then adding dbt tests allows us to be confident in our code. Do you have macros? Then you should go back to add validation tests even for simple code. It may take some time to get used to doing it, but fear not. Soon, you will know that testing is wicked awesome!

All code in this project can be viewed here [https://github.com/leogodin217/dbt\_demos/tree/main/elementary\_demo](https://github.com/leogodin217/dbt_demos/tree/main/elementary_demo)

[![Data Engineer Things](https://miro.medium.com/v2/resize:fill:96:96/1*HtZXPy85bDrTZm9tMXi6aQ.png)](https://blog.dataengineerthings.org/?source=post_page---post_publication_info--a80e76243ae4---------------------------------------)

[![Data Engineer Things](https://miro.medium.com/v2/resize:fill:128:128/1*HtZXPy85bDrTZm9tMXi6aQ.png)](https://blog.dataengineerthings.org/?source=post_page---post_publication_info--a80e76243ae4---------------------------------------)

[Last published 15 hours ago](https://blog.dataengineerthings.org/building-an-on-call-partner-with-snowflake-cortex-11560b9d5819?source=post_page---post_publication_info--a80e76243ae4---------------------------------------)

Things learned in our data engineering journey and ideas on data and engineering.

[![Leo Godin](https://miro.medium.com/v2/resize:fill:96:96/0*kkwZ8D_UzFGPeDg_.png)](https://leo-godin.medium.com/?source=post_page---post_author_info--a80e76243ae4---------------------------------------)

[![Leo Godin](https://miro.medium.com/v2/resize:fill:128:128/0*kkwZ8D_UzFGPeDg_.png)](https://leo-godin.medium.com/?source=post_page---post_author_info--a80e76243ae4---------------------------------------)

[184 following](https://medium.com/@leo-godin/following?source=post_page---post_author_info--a80e76243ae4---------------------------------------)

I’m Leo and I love data! Recovering mansplainer, currently working as a senior data engineer at Shopify. BS in computer science and a MS in data science.