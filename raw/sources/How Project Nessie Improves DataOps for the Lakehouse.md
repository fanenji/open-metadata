---
title: "How Project Nessie Improves DataOps for the Lakehouse"
source: "https://www.dremio.com/blog/how-project-nessie-improves-dataops-for-the-lakehouse/"
author:
  - "[[Dremio]]"
published: 2022-03-15
created: 2026-05-07
description: "The open-source Project Nessie enables enterprises to improve DataOps by controlling consistent versions of data in the lakehouse."
tags:
  - "clippings"
topic:
type: "note"
---
***This article was originally published on*** [***eckerson.com***](http://eckerson.com/)***.***

To avoid drowning in data, enterprises must simplify and manage it in a consistent way.

The data lakehouse, also called a cloud data platform, simplifies data delivery by combining the best of the data warehouse with the best of the data lake. The lakehouse runs SQL queries directly on a consolidated object store, removing the need for duplicative data extracts. But it still needs help automating data management and controlling multiple versions of data within the object store.

The open-source [Project Nessie](https://projectnessie.org/) provides a new level of control and consistency. Nessie takes a page from [GitHub](https://github.com/), the popular platform on which developers build, test, release, and update versions of software. By applying similar development processes and concepts to data, Nessie enables data engineers and analysts to update, reorganize, and fix datasets while maintaining a consistent version of truth. This strengthens the methodology of data operations (DataOps), which seeks to ensure the delivery of timely, accurate data to the business.

## Project Nessie strengthens DataOps by helping control versions of data in a consistent way

At its [Winter 2022 Subsurface](https://www.dremio.com/subsurface/live/winter2022/) event, [Dremio unveiled](https://www.dremio.com/press-releases/dremio-announces-open-and-forever-free-lakehouse-platform-dremio-cloud-on-aws/) a new version of its lakehouse platform that introduces [Arctic](https://www.dremio.com/platform/lakehouse-management/), an intelligent metastore service that includes DataOps capabilities based on Nessie.

## Try Dremio’s Interactive Demo

Explore this interactive demo and see how Dremio's Intelligent Lakehouse enables Agentic AI

### DataOps

To understand how this works, let’s first review what we mean by DataOps.

DataOps is a methodology for developing, deploying, and maintaining data solutions using practices derived from DevOps and agile approaches to software development. As my colleagues Wayne Eckerson, Joe Hilleary, and Dave Wells write in their [extensive research](https://www.eckerson.com/topics/dataops), DataOps has four pillars: continuous integration and deployment (CI/CD), orchestration, testing, and monitoring. They perform the following tasks.

- **CI/CD**: Continuously improve both data pipeline code and data itself by branching, updating, and then merging pipeline versions back into the “single source of truth.”
- **Testing**. Check pipeline functionality and data quality to reduce errors while developing, deploying, and operating pipelines.
- **Orchestration**. Automate the tasks within a pipeline, and the interactions of multiple pipelines and tools, to reduce the effort of data delivery.
- **Monitoring**. Observe the performance of pipelines and their supporting infrastructure to spot, predict, and prevent issues.

### Enter Project Nessie

Nessie uses CI/CD to control data versions in a consistent way. Data engineers and analysts can branch a data set into a virtual copy, update that virtual copy, then merge it back into the core data set. This means they can ingest, transform, and experiment with data in isolation, across many users and multiple processing engines, with no fear of corrupting the core data that represents the single version of truth. They don’t change the core data set until they have a new version they trust.

![](https://www.dremio.com/wp-content/uploads/2022/03/Project-Nessie-Helps-Control-Data-Versions-2048x767.png)

## Project Nessie Helps Control Data Versions with CI/CD

Let’s illustrate this with two examples, one for business intelligence and one for data science.

**Business intelligence.** Suppose the data analyst with an ecommerce company needs to start tracking customer satisfaction (CSAT) in an executive dashboard for sales and marketing leadership. The data analyst collaborates with a data engineer to branch their core dataset for the dashboard by creating a virtual copy. They combine metadata for two tables with the virtual copy. These tables are (1) scores from the CSAT surveys they email to customers each quarter, and (2) customers’ voluntary responses to a touchtone survey after support calls.

The data analyst and data engineer transform these two tables by joining them, reformatting them, and creating a weighted model that derives a single CSAT score. These refined tables yield accurate CSAT scores within their virtual copy of the dashboard dataset. Once they trust the virtual copy, they merge it back into the core data, effectively creating a new source of truth. They continue to update this source of truth with fresh survey results each week.

**Data science**. Now suppose the sales and marketing executives go one step further. They ask the data team to refine their CSAT scores based on social media postings about their products. To meet this new requirement, the data analyst and data engineer branch their core data set by creating another virtual copy. They combine it with metadata for recent Facebook postings about their top three products.

A data scientist then transforms the Facebook text files and uses [natural language processing](https://www.eckerson.com/articles/how-covid-19-will-drive-adoption-of-natural-language-processing) to summarize their content and create an aggregate score of customer sentiment. The data scientist collaborates with the data engineer and data analyst to feed this sentiment score into the existing model for measuring CSAT. Once they have an accurate updated model within the virtual copy, they merge that virtual copy back into the core data. This creates a new source of truth that, as before, receives fresh inputs each week.

## Just Scratching the Surface

Project Nessie is part of a rich ecosystem of DataOps tools, some of which have taken a similar “git-hub” approach to controlling data versions. [DataOps.live](https://www.dataops.live/), for example, helps branch and merge datasets—even full databases—as they put large-scale data changes into production.

I explore this and other aspects of the lakehouse with Deepa Sankar, VP of Portfolio Marketing at Dremio, for our [webinar](https://hello.dremio.com/designing-an-effective-sql-data-lakehouse-reg.html?_ga=2.259684105.209164946.1646138243-148862902.1644539327) “Designing an Effective Data Lakehouse for SQL,” which is now available to watch on demand. Join the discussion to learn more and tell us what you think!