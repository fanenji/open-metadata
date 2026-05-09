---
type: concept
title: Data Quality for AI
created: 2026-04-04
updated: 2026-04-04
tags: [data-quality, ai, embeddings, rag, training]
related: [data-quality-dimensions, shift-left-data-quality, context-engineering, vector-database-operations, ai-data-governance]
sources: ["The 2026 Data Engineering Roadmap Building Data Systems for the Agentic AI Era.md"]
---
# Data Quality for AI

AI systems are particularly sensitive to data quality issues. A small amount of bad data can lead to incorrect embeddings, poor retrieval, and misleading outputs. Traditional data quality approaches need to be strengthened and extended for AI workloads.

## AI-Specific Quality Concerns

- **Quality for embeddings**: Poor data quality produces embeddings that don't cluster properly and don't retrieve well. Noisy, inconsistent, or erroneous data degrades embedding quality.
- **Quality for training**: If data is used to fine-tune models, quality issues can be amplified. A model trained on bad data will confidently produce bad outputs.
- **Quality for RAG**: RAG systems retrieve and present data to LLMs. If retrieved data is wrong, the LLM will confidently present wrong information to users.

## Modern Data Quality Practices for AI

- **Semantic validation**: Beyond checking that data is well-formed, semantic validation checks whether data makes sense in context — plausible values, consistent relationships.
- **Drift detection**: Data distributions change over time. Detecting unexpected changes and distinguishing between real change and quality issues is increasingly important.
- **Cross-source consistency**: Checking consistency across multiple sources reveals issues not apparent from any single source.
- **Quality scoring**: Quality scores capturing multiple dimensions help AI agents make appropriate decisions about how much to trust different data sources.

## Quality Feedback Loops

- **Usage-based quality signals**: When AI agents struggle to use data effectively, that is a quality signal. Systems should capture and learn from these signals.
- **Human feedback integration**: When humans correct AI outputs, that feedback often reflects underlying data quality issues.
- **Automated remediation**: When quality issues are detected, automated systems can fill in missing values, correct obvious errors, or flag suspicious records.

## Relationship to Existing Wiki

This concept extends [[data-quality-dimensions]] with AI-specific dimensions (embedding quality, training quality, RAG quality). It also connects to [[shift-left-data-quality]] through the emphasis on early detection and to [[context-engineering]] through semantic validation.
