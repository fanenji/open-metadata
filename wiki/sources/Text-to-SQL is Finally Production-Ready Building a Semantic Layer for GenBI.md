---
type: source
title: "Text-to-SQL is Finally Production-Ready: Building a Semantic Layer for GenBI"
created: 2026-05-07
updated: 2026-05-07
tags: [text2sql, genbi, rag, semantic-layer, llm]
related: [kapil-khatik, genbi-architecture, semantic-layer-for-text2sql, rag-for-database-schema, golden-queries-few-shot, text2sql-patterns, context-store, llm-sql-generation-evaluation]
sources: ["Text-to-SQL is Finally Production-Ready Building a Semantic Layer for GenBI.md"]
authors: [Kapil Khatik]
year: 2026
url: "https://medium.com/@kapildevkhatik2/text-to-sql-is-finally-production-ready-building-a-semantic-layer-for-genbi-0127c1127574"
venue: Medium
---
# Text-to-SQL is Finally Production-Ready: Building a Semantic Layer for GenBI

This article by [[Kapil Khatik]] argues that zero-shot Text-to-SQL fails on enterprise databases due to context management problems — LLMs hallucinate when given hundreds of tables with obscure column names. The proposed solution is a RAG-based architecture where schema metadata is enriched with plain-English descriptions, only the most relevant tables/columns are retrieved per query, and the LLM generates SQL from a focused, narrow context.

The author provides a working code example (LangChain + ChromaDB + GPT-4) that correctly generates a join query for "revenue from premium members in the US" by semantically mapping "revenue" → `order_total_usd` and "premium members" → `is_active_member`. The article acknowledges production complexity including few-shot prompting with [[golden-queries-few-shot]], human-in-the-loop UI, and feedback loops for continuous improvement.

The article introduces the [[genbi-architecture]] pattern, the [[semantic-layer-for-text2sql]] concept, and the [[rag-for-database-schema]] technique. It positions GenBI as a data engineering challenge rather than just prompt engineering, emphasizing the need for enriched metadata beyond raw DDL.

**Key Claims:**
- Zero-shot Text-to-SQL fails on enterprise schemas with hundreds of tables
- RAG over schema metadata solves the context management problem
- The semantic layer must be designed for embedding models, not just humans
- Production GenBI requires golden queries, human-in-the-loop, and feedback loops

**Limitations Acknowledged:**
- The example is illustrative, not benchmarked
- No empirical results or comparison against baselines
- Golden queries are needed for complex analytical questions (window functions, date math)