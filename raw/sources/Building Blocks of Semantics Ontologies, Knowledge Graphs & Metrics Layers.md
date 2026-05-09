---
title: "Building Blocks of Semantics: Ontologies, Knowledge Graphs & Metrics Layers"
source: "https://sriram-narasim.medium.com/building-blocks-of-semantics-ontologies-knowledge-graphs-metrics-layers-ef1808ea6e82"
author:
  - "[[Sriram Narasimhan]]"
published: 2026-01-06
created: 2026-04-07
description: "Building Blocks of Semantics: Ontologies, Knowledge Graphs & Metrics Layers The Semantic Layer: The Trust Fabric of the Agentic Enterprise (Part 2) Semantics Is Not a Single Thing In Part 1, we …"
tags:
  - "clippings"
topic:
type: "note"
---
[Sitemap](https://sriram-narasim.medium.com/sitemap/sitemap.xml)

**The Semantic Layer: The Trust Fabric of the Agentic Enterprise (Part 2)**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HiV0AzH8eh0O3HhKXiLpUA.png)

### Semantics Is Not a Single Thing

In [**Part 1**,](https://medium.com/@sriram-narasim/the-semantic-layer-the-trust-fabric-of-the-agentic-enterprise-part-1-c27d41ae3aec) we argued that the semantic layer is the *trust fabric* of the agentic enterprise. Without it, autonomous systems operate on brittle prompts, implicit assumptions, and inconsistent interpretations of “truth”. They fail plausibly — by acting on subtly different interpretations of the same business concept.

But that leads to the more important question:

> What is the semantic layer actually made of?

There is no one single magic set of tables, no universal YAML, no vendor abstraction that suddenly turns data into meaning.

Instead, **semantics emerges from a system of complementary building blocks,** each solving a different failure mode in enterprise AI.

In the agentic enterprise, four blocks matter most:

1. **Data Substrate** — governed analytical and operational foundations
2. **Ontologies** — shared, explicit meaning
3. **Knowledge Graphs** — contextual relationships
4. **Metrics Layers** — Executable business truth

> **Semantics is a system, not a schema**

### Data Substrate: The Execution Foundation

Semantics without substance is theory. The data substrate is where semantic decisions become executable reality.

### What a Data Substrate Actually is

A data substrate is the execution foundation that supplies agents and semantic services with reliable, scalable, queryable enterprise truth. It’s not just storage — it’s the analytical and operational infrastructure that makes semantic reasoning actionable at scale.

### What Belongs in the Data Substrate

A proper substrate includes:

1. **Analytical Stores (First-Class Citizens)**
- Lakehouse platforms (Delta / Iceberg /Hudi)
- Cloud data warehouses (BigQuery/ Snowflake)
- Columnar analytical engines
- Time-series and vector stores (when used analytically)

These provide the scale, performance, historical depth, and cost efficiency that agents need to operate on enterprise data. They aren’t semantic themselves, but semantic layers cannot execute without them.

2\. **Curated Data Products**

Raw bronze tables don’t constitute a substrate. A proper substrate is built from governed data products such as:

- Canonical Supplier master
- Contract coverage views
- Harmonized PO & Invoice facts
- Category and hierarchy mappings
- Policy and control registries
- External risk and ESG signals

Data-as-a-product principles ensure ownership, SLAs, quality signals, and lineage — making the substrate trustworthy enough for autonomous decision-making.

3\. **Governance and Access Plane**

The substrate must expose multiple interfaces for different consumption patterns:

- SQL (for metrics evaluation)
- APIs (for agent tools)
- Graph projections (for traversal)
- Event streams/ CDC (for reactive agents)
- Audit logs and access controls

**The Division of Labour**

> **The data substrate provides substance**
> 
> **The Semantic layer provides meaning**

One cannot function without the other. The substrate makes semantics executable; semantics make the substrate intelligible to agents.

### Ontologies: Agreeing on Meaning Before Reasoning

Once substance exists, meaning can be imposed.

That is the role of an ontology.

### What an Ontology Is — and Isn’t

An ontology is not:

- A physical data model
- A table layout
- A taxonomy spreadsheet
- A glossary PDF

An ontology is:

- A formal definition of business concepts
- Their attributes
- Their constraints
- Their semantic intent

It answers questions agents cannot infer safely:

- What is a Supplier?
- When does a Supplier become “high risk”?
- Is “Spend” the same as “Cost”?
- Can a Contract exist without a financial impact?

### Why Ontologies Are Non-Negotiable for Agentic AI

LLMs are linguistically fluent, not semantically precise.

Without ontologies:

- Prompts become bloated
- Meanings drift across use cases
- Agents hallucinate and make incompatible assumptions

With ontologies:

- Concepts are stable
- Ambiguity is explicit
- Drift is detectable
- Reasoning is bounded

Procurement is one of the most semantically fragile domains in the enterprise:

- Supplier ≠ Vendor ≠ Partner
- Spend ≠ Cost ≠ Commitment
- Risk ≠ Exposure ≠ Violation
- Savings ≠ Negotiated ≠ Realized

Humans resolve these ambiguities in meetings.  
Agents resolve them in execution.

> ***Where humans debate, agents decide — and get it wrong if semantics are implicit.***

### Knowledge Graphs: Where Context Actually Lives

Ontologies define *what things mean*.  
Knowledge graphs define *how things relate*.

This is where semantics becomes operational.

### Why Tables and Joins Are Not Enough

Relational models excel at storage and aggregation.

They fail at:

- Expressing causality
- Traversing context
- Explaining *why* something happened

A SQL join tells you *how* data connects — not *what that connection means*.

Knowledge graphs encode:

- Direction
- Cardinality
- Semantics
- Causality

They mirror how humans — and agents — reason.

Let's look at a procurement example on **Explainable Risk**

Question:

> Why did the agent flag Supplier A as high risk?

Graph traversal:

- Supplier → linked Contracts
- Contract → governing Policies
- Policy → violated Thresholds
- Threshold → Risk Classification
- Risk → allowed actions

The output is not just a result — it is an explanation trail.

### Knowledge Graphs vs Embeddings: Complementary, Not Competing

The distinction between knowledge graphs and embeddings often confuses practitioners. Both are essential, but they solve different problems in the agentic stack.

**What Each Does Best**

**Embeddings excel at discovery**

- Semantic similarity search
- Pattern recognition across unstructured content
- Retrieving relevant context from large corpora
- Fuzzy matching when exact relationships are unknown

**Knowledge graphs excel at explanation:**

- Traversing explicit relationships
- Encoding business rules and constraints
- Providing auditable reasoning paths
- Maintaining referential integrity

### Where the Confusion Comes From

Enterprise vector databases often market themselves as “semantic search” solutions, which conflates retrieval with reasoning. Retrieving similar content is not the same as understanding how concepts relate.

Consider the procurement risk example:

**Embedding-based retrieval** might surface documents about “high-risk suppliers” by semantic similarity — helpful for finding relevant policies or past incidents.

**Graph traversal** shows you *why* Supplier A is classified as high-risk right now — by walking the explicit chain: Supplier → Contract → Policy Violation → Risk Threshold → Classification.

One finds relevant information. The other explains a specific decision.

### The Hybrid Reality

Production agentic systems use both:

- Embeddings to discover what might be relevant
- Graphs to explain why something is relevant
- Embeddings to handle the long tail of unstructured knowledge
- Graphs to enforce governed relationships

The key insight: embeddings are probabilistic approximations; graphs are explicit commitments. Agents need both to balance flexibility with accountability.

> *Ontologies define meaning.*
> 
> *Knowledge graphs operationalize it.  
> Embeddings help discover it.*

### Metrics Layers: Turning Meaning into Executable Truth

If ontologies provide language and graphs provide context, metrics layers provide decisions.

This is where semantics meets execution.

**Metrics Are Not Aggregations**

Traditional metrics were built for dashboards:

- Context-free
- Retrospective
- Human-consumed

Agents need metrics that encode:

- Grain (what level of aggregation)
- Filters (what’s included/excluded)
- Valid contexts (when this metric applies)
- Business intent (what decision it informs)
- Policy constraints (what actions it permits)

**Why Procurement Metrics Collapse Without Semantics**

1. **Total Spend**
2. **Addressable Spend**
3. **Compliant Spend**
4. **Managed Spend**
5. **Realized Savings**

Without semantic precision, these metrics become dangerously ambiguous.

Example: **Addressable Spend**

Question: “ *What is our addressable spend in the APAC region?*”

**Without Semantics:** Three different teams might calculate this three different ways:

- **Procurement team:** All spend in APAC with suppliers we *could* renegotiate (excludes utilities, taxes, one-time capital expenditures)
- **Finance team:** All spend in APAC entities (includes everything in regional P&L)
- **Category team:** All spend on goods/services sourced in APAC (includes APAC-manufactured goods shipped globally)

An agent asked to “optimize addressable spend” will get radically different numbers and take incompatible actions depending on which definition it uses.

```c
Addressable Spend = 
  SUM(Invoice.Amount)
  WHERE:
    Supplier.Region = 'APAC'
    AND Supplier.Relationship_Type IN ['Strategic', 'Preferred', 'Transactional']
    AND Category.Negotiability = 'High'
    AND Spend.Type NOT IN ['Tax', 'Utility', 'Regulatory']
    AND Contract.Renewal_Window <= 12_months
  CONTEXT:
    Valid_For: ['Sourcing Strategy', 'Category Planning']
    Invalid_For: ['Financial Reporting', 'Tax Planning']
    Decision_Authority: ['Procurement_VP', 'Category_Manager']
```

This isn’t just a SQL query — it’s a semantic contract that defines:

- **Ontology:** What qualifies as “addressable”
- **Graph context:** Supplier relationships, contract states, category attributes
- **Data substrate:** Where the underlying facts live (invoices, contracts, suppliers)
- **Business rules:** What decisions this metric can inform

> *Agents don’t act on data.  
> They act on metrics.*

If your metrics are ambiguous, your agents are ungoverned.

### Canonical: Semantic + Data Substrate Stack

Individually, these components help.

Together, they enable governed autonomy

### Canonical Decision Pipeline

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*reX4gnMID_ZC1SJeMzS3TA.png)

This is not a data pipeline.

It is a **decision pipeline**.

### The Failure Modes Enterprises Must Avoid

Most failures are architectural, not technical.

- Treating the lakehouse as the semantic layer
- Treating semantics as documentation
- Encoding business logic in prompts
- Letting agents infer policy from text

The result:

- Inconsistent decisions
- Unexplainable outcomes
- Escalating human overrides
- Loss of trust

> If semantics lives in prompts, governance is already lost.  
> If semantics floats above the substrate, truth is unstable.

### Why This Stack Is Different in an Agentic World

The shift from BI to agentic systems isn’t incremental — it’s categorical.

**In BI systems:** Semantics explained the past. Humans made decisions

**In agentic systems:** Semantics governs the future. Agents makde decisions.

The shift is fundamental:

The question changes from “W **hat does this number mean?**” to “ **What am I allowed to do with it?**”

This is why CTOs must treat semantics as **core infrastructure**, not metadata.

> In agentic enterprises, **semantics is no longer descriptive — it is prescriptive.**

### The Architecture No One Wants to Build (But Everyone Will Need)

To recap the system:

- **Data Substrate** supplies governed analytical execution
- **Ontologies** define shared meaning
- **Knowledge Graphs** provide contextual reasoning
- **Metrics Layers** deliver executable business truth

Together, they form the trust fabric required for safe autonomy.

**Without this stack, you get:**

- Agents that hallucinate plausible-sounding decisions
- Metrics that mean different things to different systems
- Explanations that cannot be audited
- Governance that happens after the damage is done

**With this stack, you get:**

- Decisions that are explainable before they execute
- Metrics that are semantic contracts, not calculations
- Reasoning that can be traced from data to action
- Governance that accelerates autonomy instead of blocking it

The enterprises that build this foundation will deploy agents safely at scale.

The enterprises that skip it will spend the next decade debugging why their autonomous systems keep making “technically correct” decisions that violate business intent.

### The Question That Determines Success

You now understand *what* to build. But one critical question remains:

**Who owns this system?**

Not philosophically — operationally. Who maintains the ontologies? Who approves metric definitions? Who decides when a semantic change is breaking vs. non-breaking? How do you scale semantic governance without creating a bottleneck that kills agility?

This is the operating model problem, and it’s where most semantic initiatives collapse — not from technical failure, but from organizational paralysis.

**Part 3** will address:

- Centralized vs federated semantic ownership
- Semantic versioning and CI/CD
- How to govern semantics without becoming the team that says “no”
- Why the operating model determines whether agents accelerate or stall your enterprise

The stack enables autonomy.  
The operating model determines who benefits from it.

**If semantics lives in prompts, governance is already lost.**  
**If semantics floats above the substrate, truth is unstable.**  
**If semantics has no owner, agents have no accountability.**

The technical architecture is solved. The organizational one is not.

[![Sriram Narasimhan](https://miro.medium.com/v2/resize:fill:64:64/1*fulQO8je7MdoL7SxpQOsnQ.jpeg)](https://sriram-narasim.medium.com/?source=post_page---post_author_info--ef1808ea6e82---------------------------------------)

[![Sriram Narasimhan](https://miro.medium.com/v2/resize:fill:85:85/1*fulQO8je7MdoL7SxpQOsnQ.jpeg)](https://sriram-narasim.medium.com/?source=post_page---post_author_info--ef1808ea6e82---------------------------------------)

[13 following](https://sriram-narasim.medium.com/following?source=post_page---post_author_info--ef1808ea6e82---------------------------------------)

VP Engineering, Data & Analytics - SAP Procurement, Chief Architect, Basketball/sports nerd

## Responses (2)

S Parodi

What are your thoughts?  

```c
Dear Sriram,Thank you so much for putting this together. It resonates with me.In the last few months, as our team is trying to understand how to build a good semantic layer, I've been reading almost every article I can get my hands on about how a…more
```

1

```c
Happy New Year and thanks for this detailed and informative article. It is of interest to my company which is a stealth startup and uses AI and RDF and of course the Semantic Web
```

Impossibile connettersi al servizio reCAPTCHA. Controlla la connessione a Internet e ricarica la pagina per generare un test reCAPTCHA.