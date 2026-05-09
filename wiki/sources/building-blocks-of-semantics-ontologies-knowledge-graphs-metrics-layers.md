---
type: source
title: "Building Blocks of Semantics: Ontologies, Knowledge Graphs & Metrics Layers"
authors: [Sriram Narasimhan]
year: 2026
url: "https://sriram-narasim.medium.com/building-blocks-of-semantics-ontologies-knowledge-graphs-metrics-layers-ef1808ea6e82"
venue: "Medium"
created: 2026-04-07
updated: 2026-04-07
tags: [semantics, knowledge-graph, ontology, metrics-layer, agentic-enterprise]
related: [the-agentic-enterprise-architecture, semantic-context-layer, knowledge-graph, embeddings-vs-knowledge-graphs, semantic-contracts]
sources: ["Building Blocks of Semantics Ontologies, Knowledge Graphs & Metrics Layers.md"]
---
# Building Blocks of Semantics: Ontologies, Knowledge Graphs & Metrics Layers

The semantic layer is the **trust fabric** of the agentic enterprise. Without it, autonomous systems operate on brittle prompts, implicit assumptions, and inconsistent interpretations of "truth."

Semantics is not a single tool or schema, but a system of four interdependent building blocks:

1.  **Data Substrate**: The physical and analytical foundation (Lakehouses, Warehouses, Data Products) that provides the "substance" or executable reality.
2.  **Ontologies**: The formal definition of business concepts, attributes, and constraints. They provide "meaning" and prevent semantic drift.
3.  **Knowledge Graphs**: The layer that encodes relationships, causality, and context. They provide the "explanation" for why certain data points are connected.
4.  **Metrics Layers**: The "executable business truth." These are **Semantic Contracts** that define the grain, filters, and business intent for agentic decision-making.

## The Four Building Blocks

### 1. Data Substrate: The Execution Foundation
Semantics without substance is theory. The substrate provides the scale, performance, and historical depth required for agents to operate. It includes analytical stores (Delta, Iceberg, Snowflake) and curated data products (e.g., Supplier masters, Contract coverage).

### 2. Ontologies: Agreeing on Meaning
An ontology is a formal definition of business concepts, attributes, and constraints. It prevents the "semantic drift" that occurs when LLMs are left to infer meaning from text alone. In domains like procurement, ontologies clarify that `Supplier ≠ Vendor ≠ Partner`.

### /3. Knowledge Graphs: Where Context Lives
While ontologies define *what* things mean, knowledge graphs define *how* things relate. They excel at expressing causality and providing auditable reasoning paths (e.g., tracing a risk flag from a Supplier through a Contract to a Policy Violation).

**Key Distinction:**
*   **Embeddings (Discovery):** Probabilistic; excellent at finding similar content and unstructured patterns.
*   **Knowledge Graphs (Explanation):** Deterministic; excellent at providing auditable, explicit reasoning paths and enforcing business rules.

### 4. Metrics Layers: Turning Meaning into Executable Truth
Metrics in an agentic world are **Semantic Contracts**. They are not just aggregations for dashboards; they encode grain, filters, business intent, and policy constraints. They define what an agent is *allowed* to do with a specific metric (e.g., "Addressable Spend").

## The Shift: From Data Pipeline to Decision Pipeline
The transition from traditional BI to agentic systems represents a categorical shift:
*   **In BI systems:** Semantics is **descriptive** (explaining what happened).
*   **In agentic systems:** Semantics is **prescriptive** (defining what an agent is allowed to do).

The goal is to move from a **Data Pipeline** (moving data from A to B) to a **Decision Pipeline** (moving from data to actionable, governed business outcomes).
