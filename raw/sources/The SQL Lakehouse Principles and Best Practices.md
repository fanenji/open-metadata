---
title: "The SQL Lakehouse: Principles and Best Practices"
source: "https://www.dremio.com/blog/the-sql-lakehouse-principles-and-best-practices/"
author:
  - "[[Dremio]]"
published: 2021-10-26
created: 2026-05-06
description: "Discover SQL Lakehouse principles and best practices in this blog post. Learn how it transforms BI and analytics in modern data environments."
tags:
  - "clippings"
topic:
type: "note"
---
As enterprises move to the cloud, they are embracing cloud data platforms that merge elements of the data warehouse and data lake.

These new platforms layer familiar SQL querying and transformation capabilities—heritage of the data warehouse—onto the object stores that now underpin most data lakes. These platforms consume elastic cloud compute and storage resources, enabling enterprises to scale workloads up and down on demand.

The SQL lakehouse is a subset of cloud data platforms that simplifies how you support high-performance BI workloads.

What does this look like? The SQL lakehouse sweeps aside the ETL copies that accumulate on top of the traditional data warehouse, and instead applies SQL queries directly to the object store or other storage platforms. It transforms, updates, and queries data objects, then presents the results to BI tools through a common semantic layer. It offers an open architecture via open APIs and data formats, and assists governance with elements such as role-based access controls and data masking. The SQL lakehouse assists governance by consolidating data views into a single semantic layer, and minimizing the need for multiple ETL copies that can diminish [data quality](https://www.dremio.com/wiki/data-quality/). It accelerates queries with capabilities such as columnar processing, parallel processing, and query pre-computations.

## The SQL Lakehouse

![](https://lh3.googleusercontent.com/e7XuYPXmDT4epxC00EMNVfm3BBqmBmXRBUolJ5Btq8BpzMIgwJyNWbhoNCExDSgWmIlBo77uI7fRWWrOaIsFukbeiwbfb_mSWlUksBCaGyRpaUgA__DtNotxQKEjmhJtiizIT94)

## Try Dremio’s Interactive Demo

Explore this interactive demo and see how Dremio's Intelligent Lakehouse enables Agentic AI

## Making It Work

So, what best practices help enterprise data teams succeed with the SQL lakehouse? A range of data leaders offered their insights at the Subsurface industry event that SQL lakehouse vendor Dremio recently hosted. Their best practices include starting with [DataOps](https://www.dremio.com/wiki/dataops-vs-devops/), assembling the right team, integrating a variety of data, and opening your architecture.

**Start with DataOps**. Data Operations, or DataOps, is a discipline comprised of tools and processes that build, implement, and manage data pipelines. DataOps uses practices derived from [DevOps](https://www.dremio.com/wiki/devops/) and agile software development to ingest, transform, and deliver data to various users. With DataOps, you can make your SQL lakehouse efficient and effective by continuously deploying, orchestrating, testing, and monitoring its key components. These key components might include new data sources, processors, transformation scripts, or BI queries, each of which contributes to data pipelines within the SQL lakehouse. They need vigilant oversight and steady improvements to ensure the SQL lakehouse meets business requirements.

**Assemble the right team**. Staff represents a bigger wild card than technology. To succeed, your executive sponsor, technical leads, and functional contributors need to execute coordinated plays. This means your SQL lakehouse initiative must align with team members’ skills and charters, and they must contribute their expertise at each stage. Klemen Strojan, lead data engineer at Knauf Insulation, explained how data engineers, data scientists, software developers, and other team members each play a distinct role in supporting use cases such as predictive maintenance for their manufacturing operations. HyreCar, meanwhile, overcame early resistance to its new SQL lakehouse by enlisting the sponsorship of the CEO. Their technical leads then identified gaps in the team’s domain expertise and filled those gaps with targeted hiring—as well custom training and “a culture of continuous learning,” according to CTO Ken Grimes.

**Integrate a variety of data**. The SQL lakehouse should encompass all the available and relevant datasets for the use cases your business requires. This might include database records, telemetry feeds, clickstream data, or other types of [structured](https://www.dremio.com/wiki/structured-vs-unstructured-data/) and semi-structured data. The federated approach of the SQL lakehouse enables your data team to access this data within cloud object stores, on-premises databases, internet of things (IoT) sensors, or heritage Hadoop file systems (HDFS). Such platforms can ingest all this data via periodic ETL batches or via streaming pipelines. By casting a wide net with your data, you can support both current and potential future use cases. Raiffeisenbank’s SQL lakehouse, for example, integrates various datasets from HDFS, Hive, and Oracle, and soon will phase in a Greenplum database, according to Mikhail Setkin, their data lake platform owner.

**Open your architecture**. Data environments start complex and become more complex over time. To meet modern business requirements, the SQL lakehouse must maintain data portability between users, tools, scripts, and applications. This means supporting all the popular BI tools, cloud platforms, data formats, APIs, and programming languages. Examples such as the following featured in customer presentations at Subsurface.

- Data formats such as comma-separated values (CSV), optimized row columnar (ORC) (for Apache Hive data), Apache Parquet, and JavaScript object notation (JSON)
- APIs such as open database connectivity (ODBC), Java database connectivity (JDBC), and Representational State Transfer (REST)
- Programming languages such as Python, R, Scala, and Java
- The Apache Iceberg open table format
- The Project [Nessie](https://www.dremio.com/open-source/nessie/) platform for version control of data

As the data warehouse and data lake merge on the cloud, enterprises need to give careful thought to their options. Designed and implemented well, the SQL lakehouse can help you support your analytics use cases—starting with BI—with less effort and cost. Check out the Subsurface sessions on demand to learn how early adopters have tackled the opportunity.