---
title: "From Domain Expertise to Autonomous Agents: Introducing the Agentic Graph Framework"
source: "https://medium.com/graph-praxis/from-domain-expertise-to-autonomous-agents-introducing-the-agentic-graph-framework-0d97725c58b6"
author:
  - "[[Alexander Shereshevsky]]"
published: 2026-01-18
created: 2026-04-05
description: "From Domain Expertise to Autonomous Agents: Introducing the Agentic Graph Framework How we’re enabling domain experts to transform decades of knowledge into executable AI agents — without writing …"
tags:
  - "clippings"
topic:
type: "note"
---

Where knowledge graph theory meets production reality. Enterprise architectures for Graph RAG, dynamic ontologies, and AI agents that actually remember.

*How we’re enabling domain experts to transform decades of knowledge into executable AI agents — without writing a single line of code*

## The Trillion-Dollar Knowledge Gap

Here’s a paradox that keeps enterprise AI leaders awake at night: We have more powerful AI models than ever, yet **most domain expertise remains locked in human heads**, inaccessible to automated systems.

Consider Wayne, a 62-year-old retired supply chain consultant. Over 35 years, he developed sophisticated mental models for optimizing logistics across pharmaceuticals, electronics, and retail. He knows which questions to ask, what patterns signal problems, and how to adapt strategies for different contexts. This knowledge — his *domain ontology* — took decades to build.

Now consider a Fortune 500 company’s supply chain team, drowning in complexity, unable to hire experienced consultants at scale. They have data. They have computed. What they lack is Wayne’s structured understanding of how supply chain concepts relate to and interact with one another.

This gap isn’t just inconvenient — it’s existential for AI adoption. McKinsey’s 2025 State of AI report finds that while **88% of organizations use AI in at least one function**, nearly two-thirds remain stuck in experimentation. The bottleneck isn’t algorithms. It’s knowledge representation.

We built the Agentic Graph framework to bridge this gap.

## What Is an Agentic Graph?

An **Agentic Graph** is the fusion of three capabilities that have recently converged:

1. **Ontology-driven knowledge structures** that represent domain expertise as traversable graphs
2. **Planning agents** that reason over these graphs to solve novel problems
3. **Reflective improvement mechanisms** that learn from execution to enhance the graph over time

The key insight: domain experts don’t need to understand graph theory, ontology languages, or agent architectures. They need to describe their expertise in natural language. Our framework handles the transformation.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VQAr-DoCcETOgSEcEtu6mQ.png)

This isn’t speculative architecture. It builds on proven research from Google DeepMind, Microsoft Research, and leading academic institutions — adapted for practical enterprise deployment.

## The Research Foundation

## From Chain-of-Thought to Graph-of-Thought

The evolution of AI reasoning provides the theoretical foundation for our approach.

**Chain-of-Thought prompting** demonstrated that including intermediate reasoning steps unlocks LLM capabilities. **Tree-of-Thought** extended this by modeling reasoning as search over a tree, enabling backtracking and lookahead — achieving 74% success on complex reasoning tasks versus 4% for linear approaches.

**Graph-of-Thought** generalizes further by modeling thoughts as vertices with arbitrary edge dependencies. Unlike trees, graphs enable:

- **Cyclic reasoning**: Revisiting earlier conclusions with new information
- **Thought aggregation**: Combining multiple partial solutions
- **Feedback loops**: Incorporating execution results into reasoning

The framework achieved **62% improvement over Tree-of-Thought** for complex tasks while reducing computational costs by 31%.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ADtM2xJgO2UkQHLO1eHURA.png)

**Why this matters for domain expertise**: Real-world problem-solving isn’t linear. A supply chain expert doesn’t follow a script — they navigate a mental graph of concepts, constraints, and trade-offs. Graph-of-Thought provides the computational analog.

## Knowledge Graphs Meet Language Models

The integration of structured knowledge with LLMs has become a major research thrust. The landmark survey [“Unifying Large Language Models and Knowledge Graphs: A Roadmap”](https://arxiv.org/abs/2306.08302) identifies three paradigms:

```c
|      Paradigm      |                Description                 |                     Example                     |
|--------------------|--------------------------------------------|-------------------------------------------------|
| KG-enhanced LLM    | Knowledge graphs inform LLM reasoning      | Grounding responses in verified facts           |
| LLM-augmented KG   | LLMs help construct and complete graphs    | Extracting entities and relationships from text |
| Synergized Systems | Bidirectional reasoning between KG and LLM | Agents that both query and update knowledge     |
```

Our framework implements the third paradigm. Domain experts provide knowledge that becomes a graph; agents reason over that graph; execution results flow back to enhance it.

Microsoft’s **GraphRAG** framework validates this approach at scale, demonstrating substantial impr ovements over traditional retrieval by leveraging entity knowledge graphs and community summarization. Gartner placed GraphRAG on their Hype Cycle with 2–5 years to mainstream adoption — we’re building on this foundation.

## The AGI Levels Framework

Google DeepMind’s “Levels of AGI” paper (Morris et al., 2023) provides crucial framing. Modeled on SAE autonomous driving levels, it distinguishes:

- **Level 0**: No AI (rule-based automation)
- **Level 1**: Emerging AI (narrow task assistance)
- **Level 2**: Competent AI (skilled human-level on specific tasks)
- **Level 3**: Expert AI (90th percentile human performance)
- **Level 4–5**: Virtuoso to Superhuman

Critically, DeepMind separates **capability levels** from **autonomy levels**. A Level 2 system might operate as a Tool (human invokes), Consultant (human approves), or Collaborator (human can override) — or as an Agent (human sets goals, AI executes).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*X2YRHzR9UoiWggMAf_CHXQ.png)

**Our framework targets the transition from Level 1–2 (assisted) to Level 3 (autonomous) for domain-specific tasks.** The key enabler: rich ontological knowledge that constrains and guides agent reasoning.

## How the Framework Works

### Step 1: Natural Language to Ontology

Domain experts describe their knowledge in plain English. No formal languages, no schemas, no technical prerequisites.

Example input from Wayne:

```c
When optimizing cold chain logistics for pharmaceuticals, I first assess
the temperature sensitivity categories of the products. Class A products
require 2–8°C and have zero tolerance for excursions. Class B can handle
15–25°C with brief excursions up to 30°C.
The key relationships are:
- Product sensitivity determines carrier requirements
- Carrier capabilities constrain route options
- Route distance affects viable transport modes
- Transport modes have different cost/reliability trade-offs

For any new optimization request, I start by mapping product categories
to required capabilities, then filter carriers, then evaluate routes
by the client's priority: cost, speed, or reliability.
```

Our **Ontology Extraction Engine** uses LLM-powered parsing to identify:

- **Entities**: Product categories, carriers, routes, transport modes
- **Relationships**: “determines,” “constrains,” “affects”
- **Attributes**: Temperature ranges, tolerances, priorities
- **Procedures**: The sequence of evaluation steps

The output is an OWL-compatible ontology stored as a traversable knowledge graph.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_A0BAQC8_wDZjFlUSb6Ikg.png)

### Step 2: Ontology to Executable Agent

The extracted ontology becomes the “world model” for a planning agent. We leverage the **RAP (Reasoning via Planning)** framework (Hao et al., EMNLP 2023), which uses LLMs as both world model and reasoning agent.

When a new problem arrives — “Optimize cold chain for this shipment to Brazil” — the agent:

1. **Parses** the request to identify relevant ontology subgraphs
2. **Plans** by traversing the knowledge graph using Monte Carlo Tree Search
3. **Executes** each step, gathering real data from connected systems
4. **Reflects** on results, updating confidence, and identifying gaps

This mirrors how Wayne actually works: he doesn’t follow a rigid script; he navigates his mental model, adapting to what he discovers.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XNc9nDWMVON2uIcK-6RTGg.png)

### Step 3: Multi-Agent Orchestration

Complex problems require specialized capabilities. Our framework decomposes tasks across multiple agents coordinated through emerging standards:

- **Google’s A2A Protocol**: Enables agent-to-agent communication with 150+ enterprise partners, including SAP, Salesforce, and ServiceNow
- **Anthropic’s MCP**: Standardizes agent-to-tool connections with 97M+ monthly SDK downloads
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5M4tSdAqpIjy3daXBZbAvQ.png)

A supply chain optimization might involve:

- **Data Agent**: Queries inventory systems, carrier APIs, and weather services
- **Analysis Agent**: Evaluates options against ontology-defined criteria
- **Optimization Agent**: Runs route calculations with constraints
- **Orchestrator Agent**: Coordinates workflow, handles exceptions

Each agent operates with its own context but shares the domain ontology as common ground.

### Step 4: Reflective Improvement

The breakthrough insight from recent research: agents can learn from execution without retraining.

The **Reflexion** framework (Shinn et al., NeurIPS 2023) introduced verbal reinforcement learning — agents that analyze their failures in natural language and store lessons in episodic memory. This achieved 20%+ improvement on complex reasoning tasks.

We extend this with **CLIN-style causal abstractions** (Majumder et al., 2024): instead of storing specific experiences, agents derive generalizable rules that transfer across problems.

Example reflection:

```c
Execution: Route via Miami hub selected for Brazil shipment

Outcome: 18-hour delay due to customs processing backlog

Analysis: Miami hub has 3x average customs delay for pharma shipments

Learning: "When routing pharmaceutical shipments through US hubs to 

          South America, factor in 24-48 hour customs buffer for 

          Miami; consider Atlanta as alternative with 40% faster 

          pharma clearance."

→ Ontology updated: Miami hub node gains "pharma_customs_delay: high" 

  attribute; Atlanta gains "pharma_customs_priority: preferred"
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0wQNiBGUKpjoK9DUVbCiWw.png)

This is how institutional knowledge grows. Wayne’s 35 years of experience came from exactly this loop — executed manually, stored in his head. Our framework automates it.

## The Architecture in Full

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UlYb4G3fYEyT_68fu32s1w.png)

The complete Agentic Graph framework consists of:

**Ingestion Layer**

- Natural language processing for expertise capture
- Ontology extraction and validation
- Knowledge graph construction (OWL/RDF compatible)

**Reasoning Layer**

- Graph-of-Thought planning engine
- MCTS-based solution search
- Constraint satisfaction from ontology

**Orchestration Layer**

- Multi-agent coordination (A2A protocol)
- Tool integration (MCP protocol)
- State management and context preservation

**Improvement Layer**

- Execution monitoring and outcome tracking
- Reflexion-based analysis
- Ontology enhancement pipeline

**Governance Layer**

- Autonomy level controls per task type
- Human-in-the-loop checkpoints
- Audit trails and explainability

## Why This Matters Now

Three convergent trends make this framework timely:

## 1\. Protocol Standardization

Before 2024, every agent framework was an island. The emergence of A2A and MCP creates genuine interoperability. An agent built on our framework can collaborate with agents built by enterprise vendors — crucial for real-world deployment.

## 2\. Reasoning Maturity

Graph-of-Thought and LATS (Language Agent Tree Search) moved from research papers to production-ready implementations in 2024. The **92.7% pass@1** achieved by LATS on programming benchmarks demonstrates these aren’t toy systems.

## 3\. Enterprise Knowledge Graph Adoption

Domain ontologies exist. The **Industrial Ontologies Foundry** maintains OWL-based reference ontologies for manufacturing, supply chain, and logistics. The infrastructure for semantic interoperability is built — it’s waiting to be activated by agents.

## From Wayne to Scale

Remember Wayne? After describing his supply chain methodology in natural language, our framework:

1. **Extracted** 47 entities and 89 relationships into a cold chain logistics ontology
2. **Generated** a planning agent that reasons over this structure
3. **Connected** it to carrier APIs, weather services, and inventory systems via MCP
4. **Deployed** it to the marketplace, where enterprises license it

Within 48 hours, three companies were using Wayne’s expertise — automated, scalable, available 24/7. Wayne earns passive income. Enterprises get expert-level optimization. The knowledge that took 35 years to accumulate now compounds through every execution.

This is the promise of the Agentic Graph framework: **democratizing domain expertise by making it computable**.

*Questions or implementation war stories? Find me on* [*LinkedIn*](https://www.linkedin.com/in/alexander-shereshevsky/)*.*

## References

**Foundational Research**

- [Besta, M., et al. (2024). “Graph of Thoughts: Solving Elaborate Problems with Large Language Models.” AAAI 2024. \[arXiv:2308.09687\]](https://arxiv.org/abs/2308.09687)
- [Yao, S., et al. (2023). “Tree of Thoughts: Deliberate Problem Solving with Large Language Models.” NeurIPS 2023. \[arXiv:2305.10601\]](https://arxiv.org/abs/2305.10601)
- [Zhou, A., et al. (2024). “Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models.” ICML 2024. \[arXiv:2310.04406\]](https://arxiv.org/abs/2310.04406)
- [Hao, S., et al. (2023). “Reasoning with Language Model is Planning with World Model.” EMNLP 2023. \[arXiv:2305.14992\]](https://arxiv.org/abs/2305.14992)

**Knowledge Graph Integration**

- [Pan, S., et al. (2024). “Unifying Large Language Models and Knowledge Graphs: A Roadmap.” IEEE TKDE. \[arXiv:2306.08302\]](https://arxiv.org/abs/2306.08302)
- [Edge, D., et al. (2024). “From Local to Global: A Graph RAG Approach to Query-Focused Summarization.” Microsoft Research. \[arXiv:2404.16130\]](https://arxiv.org/abs/2404.16130)
- [DeLong, L., et al. (2024). “Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey.” \[arXiv:2302.07200\]](https://arxiv.org/abs/2302.07200)

**Agent Architectures**

- [Shinn, N., et al. (2023). “Reflexion: Language Agents with Verbal Reinforcement Learning.” NeurIPS 2023. \[arXiv:2303.11366\]](https://arxiv.org/abs/2303.11366)
- [Majumder, B., et al. (2024). “CLIN: A Continually Learning Language Agent for Rapid Task Adaptation.” \[arXiv:2310.10134\]](https://arxiv.org/abs/2310.10134)
- [Wang, G., et al. (2023). “Voyager: An Open-Ended Embodied Agent with Large Language Models.” \[arXiv:2305.16291\]](https://arxiv.org/abs/2305.16291)
- [Sumers, T., et al. (2024). “Cognitive Architectures for Language Agents.” \[arXiv:2309.02427\]](https://arxiv.org/abs/2309.02427)

**Industry Standards & Protocols**

- Google. (2025). “Agent-to-Agent (A2A) Protocol Specification.” Linux Foundation.
- Anthropic. (2024). “Model Context Protocol (MCP).” Agentic AI Foundation.
- Industrial Ontologies Foundry. “Supply Chain Reference Ontology (SCRO).” IOF.

**Capability Frameworks**

- [Morris, M., et al. (2023). “Levels of AGI: Operationalizing Progress on the Path to AGI.” Google DeepMind. \[arXiv:2311.02462\]](https://arxiv.org/abs/2311.02462)
- [McKinsey & Company. (2025). “The State of AI in 2025: Agents, Innovation, and Transformation.”](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Gartner. (2024). “AI Maturity Model.” Gartner Research.](https://www.gartner.com/en/documents/5937907)

[![Graph Praxis](https://miro.medium.com/v2/resize:fill:96:96/1*rUElHORNRlPmVu9QZUkR-A.png)](https://medium.com/graph-praxis?source=post_page---post_publication_info--0d97725c58b6---------------------------------------)

[![Graph Praxis](https://miro.medium.com/v2/resize:fill:128:128/1*rUElHORNRlPmVu9QZUkR-A.png)](https://medium.com/graph-praxis?source=post_page---post_publication_info--0d97725c58b6---------------------------------------)

[Last published Mar 24, 2026](https://medium.com/graph-praxis/multi-lora-for-knowledge-graphs-one-model-many-domains-b6c1f4c96953?source=post_page---post_publication_info--0d97725c58b6---------------------------------------)

Where knowledge graph theory meets production reality. Enterprise architectures for Graph RAG, dynamic ontologies, and AI agents that actually remember.

[![Alexander Shereshevsky](https://miro.medium.com/v2/resize:fill:96:96/1*Yam5uYmyyy1ZE3QqSBDekA.jpeg)](https://medium.com/@shereshevsky?source=post_page---post_author_info--0d97725c58b6---------------------------------------)

[![Alexander Shereshevsky](https://miro.medium.com/v2/resize:fill:128:128/1*Yam5uYmyyy1ZE3QqSBDekA.jpeg)](https://medium.com/@shereshevsky?source=post_page---post_author_info--0d97725c58b6---------------------------------------)

[35 following](https://medium.com/@shereshevsky/following?source=post_page---post_author_info--0d97725c58b6---------------------------------------)

## Responses (3)

S Parodi

What are your thoughts?  

```c
Great article! Nice to see progress towards automating domain expertise in entity-relationship models! Reminds of my information engineering days when I developed standards for entity-relationship modelling for industry-specific blue print of how an…more
```

1

```c
So complex an approach makes sense for large enterprises. Yet, a simple SKOS generated from texts by ChatGPT, along with simple agent implementations, makes sense for a much broader audience.
```

1

```c
Thank you, author. That’s an interesting graph-based concept. In some ways, it aligns with my own thoughts and the direction I’m taking in developing my own AI agent. What will be interesting…more
```