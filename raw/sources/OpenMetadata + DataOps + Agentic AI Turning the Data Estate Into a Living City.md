---
title: "OpenMetadata + DataOps + Agentic AI: Turning the Data Estate Into a Living City"
source: "https://www.linkedin.com/pulse/openmetadata-dataops-agentic-ai-turning-data-estate-rodriguez-via%C3%B1a-jlzzc/"
author:
  - "[[Jeffrey Rodriguez Viaña]]"
published: 2026-05-17
created: 2026-06-02
description: "Most companies do not have a data problem. They have a lost-and-found problem."
tags:
  - "clippings"
topic:
type: "note"
---
The data exists. The tables exist. The dashboards exist. The pipelines exist. The jobs run every night. The problem is that nobody can answer simple questions quickly:

Who owns this table? Can I trust this dashboard? Where did this number come from? What breaks if I change this column? Why did yesterday’s report look different? Which system is the real source of truth?

That is where OpenMetadata, DataOps, and Agentic AI become powerful together. Not as three separate trends, but as three parts of the same operating model.

OpenMetadata is the map. DataOps is the traffic system. Agentic AI is the dispatcher that reads the map, watches the traffic, and helps people take action.

OpenMetadata describes itself as an open and unified metadata platform for discovery, observability, and governance, with a unified metadata graph, APIs, schema-first design, and many connectors across the data estate.

### The grocery store analogy

Imagine walking into a grocery store where nothing has labels.

The milk is not labeled. The expiration dates are missing. Nobody knows which supplier delivered the apples. The cashier does not know which aisle contains rice. The manager does not know which products are recalled. The chef in the deli is using ingredients without knowing whether they are fresh.

That is how many enterprise data platforms feel.

A table called xref\_customer\_final\_v3 might be important, abandoned, duplicated, or dangerous. A dashboard might be executive-facing, but nobody knows whether it uses certified data. A pipeline might produce revenue numbers, but the person who wrote it left two years ago.

OpenMetadata is the label system for the grocery store.

It tells you what each item is, where it came from, who owns it, how it is used, whether it is trusted, and what depends on it. OpenMetadata’s own repository describes this broader context as technical metadata, data quality signals, lineage, ownership, usage, policies, conversations, glossaries, classifications, metrics, domains, and data products connected into a unified metadata knowledge graph.

But labels alone are not enough. A grocery store also needs routines: stocking, cleaning, checking expiration dates, handling recalls, fixing broken refrigerators, and making sure customers find what they need.

That is DataOps.

### DataOps is not just pipelines. It is operational discipline.

DataOps is the habit of treating data systems like production systems.

Not “we loaded the table.” But “we know whether the table is fresh, correct, owned, documented, used, and safe to change.”

A good DataOps practice asks:

Is the data discoverable? Is it observable? Is lineage visible? Are quality checks running? Are incidents triaged? Are owners accountable? Are changes reviewed before they break downstream users?

OpenMetadata supports this operating model through ingestion workflows for metadata, usage, lineage, dbt, profiling, and data quality.

Think of DataOps like running a hospital.

The patient is your data product. OpenMetadata is the medical chart. Pipelines are the nurses moving blood samples, medicine, and lab results. Data quality checks are the vital signs. Lineage is the patient history. Governance is the consent form. The DataOps dashboard is the nurse station.

Without the chart, every doctor asks the same questions again. Without the nurse station, nobody sees the alarms. Without the patient history, nobody knows whether today’s symptom is new or recurring.

### Lineage is the family tree of data

Lineage answers one of the most human questions in data:

Where did this come from?

In daily life, we use lineage all the time.

A recipe tells you which ingredients produced the cake. A package tracking number tells you where the box traveled. A family tree tells you who is related to whom. A bank transaction history tells you how money moved.

Data lineage does the same thing for tables, columns, dashboards, metrics, jobs, and pipelines.

OpenMetadata can build lineage by parsing query logs, view definitions, stored procedures, and SQL transformations to understand source-to-target data movement, including column-level lineage where available.

For some systems, lineage comes from query history. OpenMetadata documents query-log lineage support for systems such as BigQuery, Snowflake, MSSQL, Redshift, ClickHouse, Databricks, and PostgreSQL, and it also supports using query log files for other connectors where native logs are not available.

That distinction matters.

Some systems naturally remember the roads that data traveled. Others only show the warehouse, not the trucks. For those systems, a DataOps platform may need to enrich lineage from APIs, logs, OpenLineage events, stored procedures, job metadata, or custom adapters.

This is where your DataOps dashboard becomes more than a UI over OpenMetadata. It becomes the city planning office for the data estate.

### OpenLineage is the travel receipt

OpenMetadata is strong as a metadata hub. OpenLineage is strong as a standard way to capture lineage events from jobs, datasets, and runs. OpenLineage describes itself as an open framework for lineage collection and analysis, with a standard API that pipeline components can use to send information about runs, jobs, and datasets to compatible backends.

A simple analogy:

OpenMetadata is the library catalog. OpenLineage is the travel receipt. Marquez is the filing cabinet for those receipts. Your DataOps dashboard is the front desk where people ask, “What happened?”

A job runs. It reads table A. It writes table B. It emits an OpenLineage event. That event becomes evidence. Later, when a dashboard looks wrong, an agent can inspect the evidence and say:

“This dashboard changed because table B was rebuilt by job X, which read table A, whose upstream source had a freshness delay.”

That is not magic. That is good metadata becoming operational memory.

### Agentic AI is not the brain. It is the field operator.

The mistake is to think Agentic AI replaces metadata.

It does not.

An AI agent without metadata is like a new employee on their first day with no badge, no map, no Slack history, and no idea which systems are production. It may sound confident, but it is guessing.

An AI agent with OpenMetadata is different. It can ask grounded questions:

## Consigliati da LinkedIn

Find the owner of this table. Show the lineage for this dashboard. List downstream dependencies before a schema change. Check whether this dataset has failed quality tests. Explain why this metric changed. Create a Jira ticket with the affected assets. Draft a Slack update for the owning team.

OpenMetadata now documents an MCP Server that allows technical and non-technical users to interact with organizational metadata through natural language conversations using tools such as ChatGPT or Claude. It also documents MCP tools for searching metadata, managing glossaries, and working with lineage data.

That changes the role of the agent.

The agent is no longer just a chatbot. It becomes a metadata-aware operator.

### The restaurant kitchen analogy

A modern data platform is like a restaurant kitchen during dinner rush.

Databricks is one cooking station. HANA is another. MongoDB is the cold prep table. Kafka is the conveyor belt. Power BI is the dining room. OpenMetadata is the recipe book, ingredient list, supplier record, kitchen map, and inspection log.

Now add Agentic AI.

The agent is not the chef. The chef is still the engineering team, the data owner, the analyst, the platform team. The agent is the experienced expediter standing between the kitchen and dining room:

“Table 12 is waiting on revenue metrics.” “The sauce depends on the inventory feed.” “The fish shipment was late.” “If we change this recipe, three menu items are affected.” “This dish is safe to serve; this one is not.”

That is the practical value of Agentic DataOps: not replacing humans, but reducing the time it takes humans to understand what is happening.

### The DataOps dashboard as mission control

A DataOps dashboard built on OpenMetadata should not simply copy OpenMetadata screens.

OpenMetadata is the system of record for metadata. Your dashboard should be the operational cockpit.

That means the dashboard should answer action-oriented questions:

What changed overnight? Which data products are unhealthy? Which high-value tables have no owner? Which dashboards depend on failing pipelines? Which lineage paths cross from HANA to Databricks to Power BI? Which schemas does this service principal actually see? Which secrets, scopes, and access paths are required to onboard this provider?

The dashboard should not only show metadata. It should show operational readiness.

A useful architecture could look like this:

Data sources feed OpenMetadata through metadata, usage, quality, and lineage ingestion. Systems that support native lineage contribute directly. Systems with weaker lineage support are enriched through query logs, APIs, OpenLineage events, or custom emulators. OpenMetadata becomes the context graph. The DataOps dashboard reads that graph, adds operational workflows, and exposes agentic actions such as impact analysis, onboarding guidance, incident explanation, and change-risk review.

For Databricks specifically, Unity Catalog lineage system tables can be queried programmatically, although Databricks notes that lineage events are emitted only when lineage can be inferred and that system tables retain a rolling one-year window.

That is exactly the type of limitation a DataOps dashboard should make visible. Not hidden. Visible.

### The best agent is boring in the right places

Agentic AI should be creative in reasoning but boring in execution.

A good DataOps agent should not randomly invent lineage. It should say:

“I found lineage from OpenMetadata.” “I found additional lineage from Databricks system tables.” “I could not find lineage for this HANA stored procedure.” “I found a likely relationship based on naming and job configuration, but it needs human confirmation.” “This downstream Power BI dashboard may be affected.”

That is the difference between an impressive demo and a production-ready system.

The agent should behave like a careful accountant, not a street magician.

For high-trust DataOps, the agent needs guardrails:

Read metadata before acting. Cite the source of its conclusion. Separate confirmed lineage from inferred lineage. Respect RBAC and data access boundaries. Create drafts before sending broad notifications. Escalate when confidence is low. Never pretend missing metadata exists.

### The inventive part: metadata as a nervous system

The future of DataOps is not a bigger catalog.

It is a nervous system.

In the human body, the nervous system does not only store information. It senses pain, detects temperature, coordinates movement, and triggers reflexes.

OpenMetadata can become the memory. Data quality can become the vital signs. Lineage can become the nerve pathways. Usage can become muscle memory. Governance can become the immune system. Agentic AI can become the reflex layer.

When something breaks, the system should not wait for a person to manually inspect ten tools. It should sense the issue, trace the blast radius, identify owners, explain likely causes, and recommend the next best action.

That is the real promise of OpenMetadata + DataOps + Agentic AI.

Not “ask AI anything.”

More like:

“Ask the data estate what it knows about itself — and let an agent help you operate it responsibly.”

### Final thought

OpenMetadata gives the enterprise a shared language for data. DataOps turns that language into daily discipline. Agentic AI turns that discipline into guided action.

The winning pattern is not to let AI wander through databases blindly. The winning pattern is to give AI a governed map, a reliable memory, and a clear operating procedure.

In common life terms:

OpenMetadata is the label on the medicine bottle. DataOps is the pharmacist’s process. Agentic AI is the assistant who checks the prescription, warns about interactions, and calls the doctor when something looks wrong.

That is how data becomes trustworthy.

Not because someone bought a catalog. Not because someone added a chatbot. But because the organization finally taught its data estate to explain itself.