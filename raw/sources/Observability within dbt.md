---
title: Observability within dbt
source: https://www.getdbt.com/blog/observability-within-dbt
author:
  - "[[Daniel Poppy]]"
published: 2021-10-29
created: 2026-04-07
description: This session showcases one of the projects that were associated with using the dbt run artifacts.
tags:
  - clippings
  - dbt
topic:
type: note
---


[Daniel Poppy](https://www.getdbt.com/authors/daniel-poppy)

last updated on Oct 21, 2024

This session showcases one of the projects that were associated with using the dbt run artifacts. We wanted better visibility into the status of our dbt runs and tests, and the artifacts contained the information we wanted.

Thus using the artifacts we were able to create a central monitoring and alerting system that notified people if a specific dbt model failed. More data is available, that can also help improve our dbt model runtime such as the execution time, the resources that were used etc.

![](https://www.youtube.com/watch?v=LNY0K6mSEEI)

[Follow along in the slides here](https://docs.google.com/presentation/d/13Q7B2MpA9MCszMJV8HEaf-WFfXsR1xZ4NlMeXCnB9oU/view "Follow along in the slides here").

## Full transcript

**Amada Echeverria:** \[00:00:00\] Welcome everyone. And thank you for joining us at Coalesce 2021. My name is Amada Echeverria. I use she her pronouns and I’m a developer relations advocate on the community team at dbt labs, I’m thrilled to be hosting today’s session Observability Within dbt presented by Kevin Chan and JonathanTalmi. Kevin is a data engineer at Snapcommerce and helped scale the data platform from infancy.

He’s also one of the original developers of the dbt Snowflake run operation. Fun fact about Kevin. He happens to have a tooth within his front tooth, and when he was very young, the baby version fell out and the adult version grew, quite the hero’s journey for Kevin’s tooth. Jonathan Talmi is a data platform lead also a Snapcommerce.

He is a researcher turned analyst, turned data engineer, and finally turned analytics engineer. \[00:01:00\] An avid outdoors person. Jonathan has hiked across two whole countries. Using the dbt run artifacts, Jonathan and Kevin were able to create a central monitoring and alerting system that notified people if a specific dbt model failed.

And this is what our speakers will explore over the next 30 minutes we have together. Before we jump into things, some recommendations for making the best out of this session. All chat conversation is taking place in the #coalesce-dbt-observability channel of dbt Slack. If you are not yet a part of dbt Slack community, you have time to join now.

Seriously, go do it. Visit getdbt.com/community and search for #coalesce-dbt-observability. We encourage you to set up Slack and your browser side-by-side in Slack. I think you’ll have a great experience. If you ask other attendees questions, make comments, share memes, or react in the channel at any point during Kevin and Jonathan session \[00:02:00\].To kick us off our chat champion, Ashley Marie, a software engineer at dbt labs started a thread to have you introduced yourself. Let us know where you’re calling in from and tell us how you currently use dbt artifacts if at all. After the session, Kevin and Jonathan will be available in Slack to answer questions. Let’s get started over to you, Kevin and Jonathan.

**Jonathan Talmi:** Okay. Everyone. Yeah, it’s great to be here.

Today we’re going to talk about Observability Within dbt. My name is Jonathan. I’m the data platform manager at Snapcommerce.

**Kevin Chan:** My name’s Kevin. I’m a data engineer at Snapcommerce.

**Jonathan Talmi:** Awesome. So let’s get started just first, a little bit about the company. So the mission statement of the company is to provide access for everyone to experience more of what life has to offer regardless of income or circumstance.

Now, what that actually means is we built a new way to shop that maximize the savings, benefits of rewards on mobile, and this roughly \[00:03:00\] translates into started with hotel bookings in the consumer goods, but with plans for much more. And so far, we’ve driven nearly a billion dollars in sales using our platform.

So about myself, I’m a data platform leader or manager here, and I got my start doing research academic research before migrating to the tech industry and had a winding path to find myself really thriving in that analytics engineering space. Yeah, Kevin, you can introduce yourself.

**Kevin Chan:** I have experience within engineering as well as some machine learning, engineering and deployments.

Recent graduates from Waterloo as well from computer science and statistics. Previously I worked at Hootsuite in Splunk before I found my way back here at Snapcommerce.

## \[00:03:42\] Data observability

**Jonathan Talmi:** Cool. Data observability is obviously a really large topic that. The number of use cases for data within individual companies is probably everybody here knows, has grown exponentially over the last few years.

Data platforms serve not only classical BI use cases, but power data science, real-time analytics, \[00:04:00\] experimentation, and more, and the modern data stack while we love it and cherish, it has made data platforms even more fragmented than before. So the surface area of data systems has increased the need for observability into the system.

Now there’s even a lot of companies focused specifically on observability and reliability like meta-plain or Monte-Carlo. And there’s the data observability space is growing really fast and tender. It’s pretty multifaceted as a whole. So this talk specifically is going to focus on how to get more observability out of dbt, specifically using the tools that you already have in your stack.

## \[00:04:39\] Why observability matters

**Jonathan Talmi:** Now why does observability matter? The need for observability within dbt becomes apparent when you start getting questions that you can’t answer within a reasonable timeframe, these questions might be something like why isn’t my model up to date? Is my data accurate? Why is my model taking so long to run?

How do I speed up my dbt \[00:05:00\] pipeline? How should I materialize and provision my model? So as you can see, observability is particularly critical during periods of data downtime, where your data’s partial or erroneous or missing or inaccurate. Now, when we couldn’t answer these questions, we realized that we had limited the observability into our own dbt deployment.

And we had to do something about that. So this gave us a mandate to build a system that would help us perform a few jobs that would give analytics, engineers, their desired observability into dbt. First, we wanted to send alerts to dbt model owners and stakeholders based on custom criteria. So model owners should know when their specific models or test fails or when their sources are not from.

Second, we wanted to surface data that would help analytics, engineers optimize their models and identify pipeline bottlenecks. And third, we wanted to reliably collect \[00:06:00\] all of this metadata and action it in close to real time, regardless of the success or failure of the dbt pipeline. Our guiding principles for this project as engineers was we’re, keeping the system lightweight so that it could be easily deployed on our stack, which is a modern data stack.

We wanted to surface all the relevant artifacts and metadata to enable SQL based, alerting and exploration. And finally, we want it to support all dbt, resources and artifacts and all job types like run, test build, etc.

## \[00:06:39\] Data Sources

**Jonathan Talmi:** So we thought that dbt artifacts might serve as a good foundation for the systems as they continue pretty granular information about dbt. For one dbt tests are an interface between or an interface for defining data quality metrics, and are often the first line of defense when you’re identifying disruptions and artifacts themselves \[00:07:00\] store the results of model and test failures, dbt artifacts, also store information about when models get built and how long they take.

Which can help you identify bottlenecks and underperforming models. So we came up with three data sources to build our system. Now, the first is the project manifest, which it gives you the full configuration of the dbt project, the second, or the run results, artifacts that get triggered after you do a dbt run or test or other commands.

These give you a detailed note and pipeline level execution, data for models, tests, and other resources. Finally, we looked at the Snowflake query history of Snowflake users, which gives you rich query performance metrics that you can tie to individual models. We ultimately found that joining the artifacts and the query history together actually gave us deeper insights about model, level performance than we would have had.

## \[00:07:53\] Solution overview

**Jonathan Talmi:** If we just use the artifacts alone. Now I’ll hand it over to Kevin. Who’s going to discuss the \[00:08:00\] architecture of the solution.

**Kevin Chan:** So on a high level, the solution that we built can be really divided into five components. And that’s actually what we built on is a very lightweight [ELT](https://docs.getdbt.com/terms/elt "ELT") system that adjusts the artifact data into our data storage.

So the first component is the orchestration. We use airflow as our workflow orchestrator and with an air flow, your workflow is represented each task and your workflow is represented as an operator and effects. When you use the Kubernetes pod operators spin up a competitive spot to execute our dbt tasks.

At every dbt commands such as dbt run dbt tests, there are artifacts generated associated that I started in local disk or on, in our case, the community’s pot operator needed a way to load the data from this pod into our data storage, which in our case was Snowflake at the end of every dbt pipeline.

So once we have the pure ride data in our data storage, that’s something we can begin to use dbt to parse out the nest of [JSON](https://docs.getdbt.com/terms/json "JSON") parse out the structure or parts of the metadata that we need associated for dashboard’s downstream and effectively merged and run assaults with a query history and a \[00:09:00\] Snowflake to generate even more metadata and more information regarding our pipelines.

The fourth component is reporting. So once we have the specs, we transform the data and create a structure that we can work with. That’s when we can start to build dashboards upon and take a look at how our model, how our pipelines of doing, how, what models have failed, what tests are failing, how long have these models and executed, and then merging it with the query history and stuff like that.

## \[00:09:23\] Orchestration

**Kevin Chan:** We can take a look at how many bites of data spill on to disk, why does the credit usage and stuff like, and finally, within these dashboards in Looker we’re actually able to create alerts on them to say, okay, if our status has changed within the last 15 minutes and the model has failed, let’s send the alert to Slack and we’ve effectively done so by creating Slack user groups to alert individual model owners, if they’re dbt tests for model has failed. So let’s go into your deeper dive about each of the current. All of our dbt pipelines are centralized in Airflow with the exception of course, some of the ad hoc jobs, we still have dbt Cloud and a use case for this would be save it once you’d refresh an \[00:10:00\] incremental model at X point in time.

The code piece snippet below is an example of how you stand shift. The Kubernetes pod operate in airflow. We do have some default configurations, which are more so just the CPU usage the resource allocation for each pod, as well as where the image lives. Within every model within our deployment has one deployment tag.

These are hourly and nightly and external. So image just showcases below. Our hourly maybe violence note that every widget or note in this graph is effectively one indication of dbt. So for example the two tasks at the very beginning, our dbt run commands the following our snapshot, I’m finally at the test.

And for external for models that are tagged external, that just means that interrupt and not part of our hourly or negative lines. Instead, what we do is for pipelines, where we want to run the transformations, as soon as the data lands, that’s when we sorry. But once the data is loaded into our data storage, that’s when we, if we want to begin to run our dbt transformations and that’s the perfect use case for our external tag, we use intro that sections lectures to of what race conditions, so that we’re not \[00:11:00\] effectively building a model that is existing in our.

So once, once we had, now we have orchestration and we have a place at which we can execute our dbt commands. The next step is let’s load this data into our data storage. In fact,. we will be well-taught a dbt macro in order for us to do so. The first step of this is to put query what that does it loads the file from your local disk onto an external stage and Snowflake.

Think of this as an external cloud storage where Snowflake can effectively carry that file. The next command is the copy command. What that does is it loads the data from pickup. It quite literally copies the other contents of that file that you uploaded to the stage into destination [table](https://docs.getdbt.com/terms/table "table"). We’ve created destination tables for the major artifacts such as the one results, the dbt test run results as well as the manifests.

And the final command is the new query that just removes the file that she uploaded into the external stage from, and all of this can be executed using the dbt run operation. So the first command that we’ve shown is the dbt run \[00:12:00\] that runs all of our models, height hourly. And then following command is the one operation that runs the macro that we’ve built out to upload the artifacts into Snowflake.

The beauty of this is that this also executes even after a dbt job failure, because we also want to load the artifacts. I hope if the run has failed.

## \[00:12:17\] Modelling

**Kevin Chan:** The next component is the modelling. Once we have the raw data of let’s begin to use dbt to transform this data set into structured into different models that can really power our dashboards downstream. So not that all the green notes are sources. We do have run results test run results as well as in manifests.

One keynote is that one of our sources is also a query history table that Snowflake, we effectively emerged that, but then run results to generate a table. that contains credit usage per query bite spillage ought to disk, as well as the warehouse sizing per model.

Also taking sorry, I’ll take note that, this all of these transformations are heavily based on the repo by git lab.

Their repo is open source. You can take a look, all of our staging models on power, the downstream dashboards, and the fact as well as the fact table, that we created.\[00:13:00\]

So cluster the transformations. Now we have onto the reporting that we’ve requested. We’ve created a, this is an example of a dashboard that we’ve created and Looker. And if you go from that’s your right of the columns, the model name is what we’ve parsed out from the artifact. Metadata is that as the course is that the model has failed to compile or knots.

January timestamp is when the the artifacts should be generated. And that’s what we can focus our learning on. The next one is the malaria. So with every model failure, there’s also the error associated with that. So we can have it in a table that we can view and send to stakeholders or to help us debug our data pipelines.

The tags are the text associated with the model. And finally, the fresh field one is what we actually use to set up the alerting associated. If that value changes in a 15 minute time span, that’s when we were able to send an alert to Slack.

The next component are, these are the test results. Is the dashboard specifically for our risk test results. Similar structure to our finance runs. The only key, not the key difference with this is that \[00:14:00\] we have the compiled SQL as the very right most column that contains SQL that you can execute on the [data warehouse](https://docs.getdbt.com/terms/data-warehouse "data warehouse").

## \[00:14:05\] Alerting

**Kevin Chan:** Two sets run the same test that was run during the dbt tests. The test name also has the type of test embedded within the name such as not an allergy test and finally the alerting component. So that fresh failed run component that we’ve set up is what we use to send Slack alerts. You’ll notice that we have these domain specific tags. Every model within our dbt deployment has one specific one deployed when one domain tag and these can be growth pod or finance or catalogs.

These tags are what we effectively use to filter up, to create these dashboards. For example, in the previous slide, we have the latest test betas restaurant results. So again, you just filter out for the peg risk and within Slack, we’re able to create these user groups. So within these user groups, we can add people to them.

So when we send the stock alert, tagging everyone from growth. Everyone who is part of that domain will receive this alert and we became in Slack. Whenever \[00:15:00\] their model feels that they own they’ll be able to debug accordingly instead of notifying everyone in the company or anyone on the data team who has a model dbt.

## \[00:15:10\] Performance management

**Jonathan Talmi:** Cool. So Kevin just demonstrated how we use this system to power our our success and failure, alerting and dashboards which is extremely useful. I’m going to talk a bit about how we use this data for performance management. So we surfaced. We, this chart shows that the performance data for some long running models taken from the artifacts and joined to the query history in that combined [view](https://docs.getdbt.com/terms/view "view") you can see that there’s several actionable pieces of information here.

First, if a model is taking a really long time to build and at the end, an engineer can consider adopting a new [materialization](https://docs.getdbt.com/terms/materialization "materialization") strategy. Like maybe it’s time to make that model incremental or insert. Second, if the model has a high percentage of total partition scan, which is a Snowflake metadata field then they might want to explore updating or adding clustering because for certain \[00:16:00\] models, it’s not a good, it’s not a good sign if they’re scanning the entire table when we’ve been building.

Finally if the model tends to have a lot of spillage and bytes sent over the network that might be a sign that it’s time to increase the size of the warehouse. Once other opportunities for optimization like refactoring the SQL or anything else have been exhausted. So overall this type of view can be very useful for people to get a sort of a bird’s eye view of their models and their domain and how well their are performing.

You can also take that, look at that previous view and look at an individual model over time. I’ll show you a couple of views that you might find interesting. This animation here shows you a single model and the execution time and all the other metrics in a time series view.

So you can see that this model start has kinda growing and growing in terms of overall execution over the course of the last couple of months. And similarly, you can look at other views for model executions over time. So the top one is probably an hourly model. You can \[00:17:00\] see that it’s triggered quite a lot, but the execution time is relatively

Over the last, a little while and at the bottom, it’s most likely a model that gets run once a day and it’s, you can see that it started to trend up over time and eventually it might be worth taking a closer look at this model.

## \[00:17:16\] Pipeline Bottlenecks

**Jonathan Talmi:** Finally the last set of visualizations I’ll show you are visualizations that allow people to look at dbt pipeline as a whole.

So this slide shows to get charts one each for the hourly and the nightly dbt model run pipelines. On the Y axis you have thread number. On the X axis you have time. Definitely got a shout out Claire and Drew for inspiring this visualization with their artifacts, discourse posts So these views can help us identify bottlenecks and candidates for optimization when the pipeline start to get out of SLA.

So for example, if your hourly jobs starts to take longer than an hour, or your nightly job is taking several hours and starting to affect other downstream pipelines, \[00:18:00\] then you might want to take a look at this and identify the bottlenecks that and work on specifically on those models and optimizing them.

For example, in the nightly run here, you can see there’s one model. That’s really holding up a lot of other ones and pushing the entire pipeline, execution time farther out. And this last visualization is the same view as before, but for tests and I pretty much included it because I thought it looked really cool.

## \[00:18:24\] Implementation

**Jonathan Talmi:** How can you implement this yourself? While everything that we’ve showed you is highly interchangeable. You can deploy this easily on the modern data stack using any BI tool, any alerting tool, any orchestration tool really every piece of it is interchangeable. Specifically for alerting, you can alert through BI or you can look at there was a dbt community member who published this library here called Snowflake the Slack, which would allow you to trigger these alerts directly.

For example, airflow or any other orchestration tool. And then when it comes to modeling the dbt artifacts you don’t have to build it ourselves like we did, or the get lab folks did right now, because now \[00:19:00\] there’s a package called from the tail’s team called dbt artifacts. That does pretty much a lot of this for you.

So this didn’t exist at the time that we sent. And finally definitely we encouraged everyone to use dbt cloud. Now they have a robust metadata API they’re even building visualizations and other features directly into the tool like the bottleneck diagram shown below. So it’s for, in terms of, from a metadata perspective, it’s they’re doing a lot of great work.

And yeah, that about wraps it up. We really appreciate everybody coming in and listening to our talk and just wanna remind everyone that if you thought that any of what you saw here today was cool and you would want to work on similar and even different projects. Definitely give me or Kevin, a shout we’re hiring across data and where we love to chat about this. Email us dbt Slack, LinkedIn, anything.

And yeah, thanks a lot to everybody attending things a lot to actually Amada and Barr specifically for helping us with our presentation and yeah, it’s great \[00:20:00\] to be here.

The dbt Community

## Join the largest community shaping data

The dbt Community is your gateway to best practices, innovation, and direct collaboration with thousands of data leaders and AI practitioners worldwide. Ask questions, share insights, and build better with the experts.

100,000+active members

50k+teams using dbt weekly

50+Community meetups