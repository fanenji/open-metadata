---
title: "Modern Data Modeling: Start with the End?"
source: https://www.adventofdata.com/modern-data-modeling-start-with-the-end/
author:
  - "[[Brice Luu]]"
published: 2022-12-03
created: 2026-04-07
description: "Ok, you wanna use dbt. But how?Introducing: dbtSo what's this dbt everyone's fussing about??At its core, dbt (data build tool) is a \"modern\" data modeling framework using (Jinja) templated SQL. It comes with a CLI tool that allows to easily materialize your models as tables or views"
tags:
  - clippings
  - dbt
topic:
type: note
---
> Ok, you wanna use dbt. But how?

## Introducing: dbt

So what's this dbt everyone's fussing about??

At its core, [dbt (data build tool)](https://docs.getdbt.com/docs/introduction?ref=adventofdata.com) is a "modern" data modeling framework using ([Jinja](https://jinja.palletsprojects.com/en/3.1.x/?ref=adventofdata.com)) templated SQL. It comes with a [CLI](https://en.wikipedia.org/wiki/Command-line_interface?ref=adventofdata.com) tool that allows to easily materialize your models as tables or views in your data warehouse.

The company behind it: [dbt Labs](https://www.getdbt.com/?ref=adventofdata.com) (formerly known as Fishtown Analytics) also produces a cloud-managed service revolving around the core dbt. They call it, quite simply, "dbt Cloud". Now, we won't get into that part here, just a thing to note: they've been central to the current "modern data stack" movement, for example coining new job titles like "analytics engineer" and, doing so, they've [coalesced](https://coalesce.getdbt.com/?ref=adventofdata.com) 😉 quite a [following](https://www.getdbt.com/community/?ref=adventofdata.com).

What I mean (and think most people mean) by "modern data stack" is any service (open-sourced or not) that is native to cloud data warehouses (things like Snowflake, BigQuery and co...) and specifically targeting data teams.

What dbt allows is quite useful for data teams. Simply put, we're now easily able to adopt best practices software engineers take for granted (things like code versioning and reviewing, sandbox environments, testing, documentation, etc.) throughout our data warehouses and data modeling processes.

That makes things like unreproducible queries or inextricably weird numbers things of the past! Because instead of having a collection of interdependent views and/or dynamically generated bits of queries that do stuff all over our warehouse, it gives us (pretty) plain SQL `select` statements, cleanly versioned in a [git](https://git-scm.com/about?ref=adventofdata.com) code repository.

Along with a simple CLI to run these models, which will "materialize" (create or update) them in our data warehouse. It also has a bunch of nice additions that help us structure, test and document all those data models.

> Disclaimer: We'll cover how to gradually structure a dbt project. Not how to run it. When you're developing you can [install the dbt CLI](https://docs.getdbt.com/docs/get-started/installation?ref=adventofdata.com) to easily use it in your development environment. For deployment to production there are [different options](https://docs.getdbt.com/docs/deploy/deployments?ref=adventofdata.com). If you're already using a data orchestrator like Airflow, Prefect or Dagster, running dbt is as simple as adding a task/step that runs `dbt build` in a shell environment containing the [dbt pip package](https://pypi.org/search/?q=dbt&ref=adventofdata.com) you're using.

## With great power comes great responsibility

The problem with frameworks that are so flexible is that they can be used in way too many ways. Some are good, some less so...

Anyway, we know we want to use dbt, but how should we go about it?

In terms of data modeling, there are multiple theories out there. Take one of the most prevalent still widely used today, [dimensional modeling](https://en.wikipedia.org/wiki/Dimensional_modeling?ref=adventofdata.com): it was initially formulated back in the 90s’!

Now don't get me wrong, it has plenty of still very relevant and useful principles. The problem though, is that it takes too much conception time to pay up front. That's because it's mainly top-down design, at least for the initial fleshing out of the business entities and relationships.

In contrast, the approach I want to outline here is primarily bottom-up, in order to:

- deliver value and insights as quickly as possible
- not pile up too much [(data modeling) technical debt](https://martinfowler.com/bliki/TechnicalDebt.html?ref=adventofdata.com) along the way.

So, we'll start naively, and gradually factorize common patterns as they emerge.

## Quick and dirty... or let's say: humble beginnings

The quickest way to extract any insight from our data is to:

1. have all our data sources readily available under the same roof: in our data warehouse (I’ve mentioned a couple options to help with that in [a previous post](https://bluu.dev/modern-data-stack-for-cto-99552102a5f9?ref=adventofdata.com))
2. directly write each query that will join all the useful sources into a single table that we’ll then expose to our stakeholders (either in their own tools via [reverse-ETL](https://medium.com/memory-leak/reverse-etl-a-primer-4e6694dcc7fb?ref=adventofdata.com) or through a dashboard we'll create for them in our BI tool of choice)

Of course, this isn’t sustainable! Because as soon as we have piled up a few such *usecases*, we'll surely need to copy/paste some parts from one query to the next... And this is always a slippery slope to get on!

Still! Go ahead and hack together your first couple of usecases in precisely this manner. The quicker we prove the value of data, the quicker we’ll start building support for “data” as a function/team within our organization. And that’ll be our basis for hiring more, spending more, etc. So raw speed is definitely something we want to aim for... in the beginning.

First off, `dbt init` your git repository. dbt will create a folder for you (named with the project name you’ll enter at prompt), which will contain the whole dbt project: meaning the `.sql` queries/files we’ll add, and a few `.yml` configurations to go with 'em.

That first command will have created a bunch of folders, most of which we won’t get into right now, but the main ones we can start working with are `analysis` and `models`.

- `analysis` can hold all our ad-hoc queries that we'll want to manually run,
- `models` will contain all the queries that we actually want to `dbt run`, which will then materialize (as tables or views) in the data warehouse.

Also, it loaded a couple of useless examples in the `models` folder. You can safely delete these. They only sparsely illustrate dbt’s main Jinja "macro" when you’re starting out: `{{ref(<parent_model_of_current_query>)}}` but we’ll get into that later 😉

You can simply start creating `.sql` files with your select queries for your first few usecases. These can go in the `models` folder if you want them to be materialized on your data warehouse when you execute `dbt run` from your CLI.

When running `dbt` commands, it isn’t really doing anything more than just executing our SQL files (just wrapped up in the correct [DDL](https://en.wikipedia.org/wiki/Data_definition_language?ref=adventofdata.com) [boilerplate](https://en.wikipedia.org/wiki/Boilerplate_code?ref=adventofdata.com)) against our warehouse at this stage. We’ll get to the Jinja templating superpowers later!

If in doubt, please check out dbt’s documentation to get you up and running: [Configuring your profile](https://www.adventofdata.com/modern-data-modeling-start-with-the-end/[Modern%20Data%20Modeling%20Start%20with%20the%20End%20-%20Advent%20of%20data]\(https://advent-of-data-2022.ghost.io/ghost/#/editor/post/6384c0761e2223003d6b7eba\)).

The only useful piece of advice at this stage: do start splitting out the logic within your query/ies in smaller bite-sized [CTEs](https://learnsql.com/blog/cte-with-examples/?ref=adventofdata.com). This will be a huge time saver down the line.

But even with somewhat readable queries, just be aware that you’ll soon hit that slippery slope we mentioned earlier.

## Start specifying your sources

So the next step we should take is to add a first *base* layer in our dbt project. I like calling it "base" as it’ll be the layer in which we simply select the data we need from our raw data sources.

So let’s create that `base` folder under `models/`. Then add a general `_sources.yml` inside. That configuration file will hold all the (input) references to our raw data. Effectively [declaring the origin of your data sources](https://docs.getdbt.com/docs/building-a-dbt-project/using-sources?ref=adventofdata.com) (read the dbt documentation linked to get the details of what that means and looks like).

You can now start creating simple `select` statements for the data sources that are actually used in the usecases you’ve previously fleshed out. The idea here is to be explicit with the columns you’re selecting. Try not to be tempted with just using `select *` because the main responsibility of this layer will be to explicitly declare the data your using at the column level.

Our `_<source_name>_sources.yml` declares *where* our raw data is, our `base` models declare *what* raw data we want to use.

Here’s a quick example (in Snowflake syntax):

```sql
with parsed as (
    select *
        , parse_json(merge_fields) as parsed_fields
    from {{ source('mailchimp', 'members') }}
)
select id as member_id
    , status
    , parsed_fields:'FNAME' || ' ' || parsed_fields:'LNAME' as full_name
    , parsed_fields:'REGISTERAT' as registered_at
from parsed
```

base/mailchimp/base\_mailchimp\_\_members.sql

We can then use this with `select * from {{ ref('base_mailchimp__members') }}` in a downstream model/query...

Just don’t forget to point your usecases to the new base models created here with that `ref()` macro.

Now, under this new `base` folder, we can also separate each data source into it’s own subfolder (as shown above). This allows to cleanly organize our base layer by source. That being said, we do *not* want to nest too many levels of folders. For the simple reason that dbt lives in a single namespace!

This means all our models (`models/**/*.sql` files) all need to have a **unique** name. A good idea is to prefix the filenames with the source’s name (as shown above). This will prevent most duplicate name clashes. Bonus: let's start writing down a style guide where we'll, ultimately, specify our preferences in terms writing SQL, but for now simply document this naming convention.

> i.e "base models filepath should be in the form: `base/<source_name>/base_<source_name>__<model_name>.sql` "

Apart from explicitly detailing what data we want to use from our sources, any simple row-wise transformations can also go here in our base layer. Things like renaming columns to align names across models, type casting or even "case-when-ing" 😉 Here, we just want to avoid changing the grain of our raw data (no group bys nor joins) or filter anything out.

Last but not least, take the time to add a `_<source_name>_models.yml` file to each of the base subfolders. There, we’ll start specifying [descriptions](https://docs.getdbt.com/reference/model-properties?ref=adventofdata.com) and [schema tests](https://docs.getdbt.com/reference/resource-properties/tests?ref=adventofdata.com) for the most used models and their main columns. You don’t need to be exhaustive for the time being. Just describe and test the most important ones to start off with!

Now that we've got our bases covered, where to?

## First refactorings

Now it’s time to add a middle layer (still under the `models/` folder). You can call it `core`, `staging`, `transform` or anything in between: this is ultimately where most of the magic will happen. The layer that our data team will keep full ownership of till the end of times! (no pressure 😆)

But for now, let’s start simple: is there any logic that you’ve already had to copy/paste in the different usecase queries you already have? Or CTEs you keep on re-writing in each new usecase?

If so, just isolate the repeated parts in their own `.sql` file in this folder and `ref()` it in the usecase models that use it.

For the time being, the main point is to start reducing the complexity and length of the usecase models by simply extracting the parts that are repeating. A good rule of thumb is the [rule of three](https://en.wikipedia.org/wiki/Rule_of_three_\(computer_programming\)?ref=adventofdata.com): if you have a logic that’s repeated 3 (or more) times in your project, then it should be isolated in it’s own model and can then be referenced by all the models that use it.

This way, if that logic needs to change down the line, it can be changed in a single place, instead of having to patch it systematically in all the places where it’s used. The risk being that it's easy to miss one of these places and therefor have differing logic when it should really be the same.

If your main *usecase* queries are still directly under the `models` folder. You can move them to `models/usecases/`. And, if you’re starting to have more than a few usecases, a nice addition to that folder is a further level of subfolders per stakeholder type. E.g one for `usecases/product`, another for `usecases/sales` or `usecases/marketing`, yet another for `usecases/finance` or `usescases/board`,... You get the idea.

The ownership over each of these can ultimately be split out if and when data competency is spread in each department of our organization. But that’ll be the topic for another blog...😉

Nice: our project is getting a bit more structured!

So we can now start getting into the Jinja templating goodness of dbt. But let's use it wisely 😆

Good candidates for such templating are if you have long and predictable column lists that you want to systematically add. You can do so with a simple Jinja `for` loop. You can also check out the `dbt_utils` [package](https://github.com/dbt-labs/dbt-utils?ref=adventofdata.com) for other ideas on what you can do more concisely with Jinja.

Any custom Jinja macros should go in the `macros` main level folder of your dbt project (same level as the `models` folder). I generally like separating out the macros that simply override dbt core ones in a `macros/overrides` subfolder. The first example of such, is generally the `generate_schema_name.sql` macro to [specify different schema names](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/using-custom-schemas?ref=adventofdata.com#how-does-dbt-generate-a-models-schema-name) between locally/manually triggered runs and non-dev (prod/preprod) environments for example.

Here’s how I often end up doing that:

```
{% macro generate_schema_name(schema_name, node='Unknown node') -%}
    {%- if var('ENV') == 'dev' and target.schema -%}
        {# -- use the target schema provided in profiles.yml for manually-triggered (dev) runs #}
        {{ target.schema | trim }}
    {%- elif var('ENV') in ('prod', 'preprod') -%}
        {# -- or use the schemas provided in configuration (in dbt_project.yml or individual models' config) #}
        {{ schema_name | trim }}
    {%- else -%}
        {# -- fail fast in case of unexpected configurations #}
        {{ exceptions.raise_compiler_error("Local run but environment variable \`DBT_DEFAULT_SCHEMA\` is not set. Or environment is not known.") }}
    {%- endif -%}
{%- endmacro %}
```

macros/overrides/generate\_schema\_name.sql

  
Which requires adding to the end of your `dbt_project.yml`:

```yaml
#...
vars:
  ENV: "{{ env_var('DBT_ENV', 'dev') }}"
```

And passing a `DBT_ENV` environment variable with the corresponding environment name.

Next up: shoot for the stars!

## Endgame: core objects

Now that we’re getting the hang of it, it’s time to shuffle things around a bit more 😆

That middle layer we’ve introduced is actually the place where we’ll want to have our central logic manipulating the data.

The goal will be to aim towards [either](https://www.fivetran.com/blog/star-schema-vs-obt?ref=adventofdata.com):

- a [dimensional model](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/?ref=adventofdata.com) / [star schema](https://en.wikipedia.org/wiki/Star_schema?ref=adventofdata.com)
- or a limited collection of " [One Big Tables](https://hightouch.com/blog/data-warehouse-modelling-part-2?ref=adventofdata.com) "
- (or any other top-down theory you’re most comfortable with...)

where we’ll progressively define all our main business objects: users on the one hand, orders on the other, inventory in a third, etc

Each being at the grain of that object and having all the attributes useful to that particular object (via shared dimensions in the case of dimensional modeling).

These core objects will be the output of that layer, but will probably each need to be based on shared "preparation" models (the repeating CTEs we first factorized above...) Which can go in a `core/staging` subfolder when things become unwieldy.

As previously mentioned, we’ll generally want to keep central ownership on that layer.

And from these core objects, the `usecases` that are exposed (then outsourced) to our different stakeholders can simply select a limited number of columns/informations, relevant to each particular usecase.

So from `sources -> base -> core`, we're integrating data: the idea being to end up with fewer but wider (more columns) models.

And from `core -> usecases`, we're doing a [fan-out](https://en.wikipedia.org/wiki/Fan-out_\(software\)?ref=adventofdata.com), producing multiple variations from the core objects that only specify the data needed for each different type of stakeholder.

## Conclusion: don't over design up-front

> "Be like water my friend"

1. Start small but start fast
2. Progressively regroup repetitions
3. Only formalize once you have a good grasp of what's what
4. Rinse and repeat...

Agile analytics engineering.

### Addendum: Naming is important

Why do I like these 3 folders for the first level under \`models\`?

1. `base`
2. `core` this folder we’ll always be our common thread as data modelers, our perpetual “work in progress”
3. `usecases` these models are our end goals and we want the insights to actually be “useable”! (detail: I like the plural to insist on the transverse role of our data team: we strive to serve **all** the other teams!!)

Ok, these names can seem a bit arbitrary, because they kind of are. But another thing I really like is that they’ll appear in that logical, sequential, alphabetical order anywhere you’ll list them: your cloud data warehouse UI (cf config in snippet below), your file explorer, your IDE of choice, you name it!

It just flows in the natural order: starting from our `base` models, passing through our `core` and finishing with the actual `usecases` we want to deliver.

Of course, I encourage you to align that first level of folder structure with your warehouse schemas. Here’s how in your `dbt_project.yml`:

```yaml
models:
  <your_dbt_project_name>:
    base:
      +schema: "base"
    core:
      +schema: "core"
    usecases:
      +schema: "usecases"
```

Note: this will only be the case in prod/preprod envs if your using `generate_schema_name` macro covered previously, when triggering locally (dev) everything will end up in a single schema (defined in your personal `~/.dbt/profiles.yml`)