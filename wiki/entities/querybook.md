---
type: entity
title: Querybook
created: 2026-04-29
updated: 2026-04-29
tags: [tool, open-source, sql, pinterest]
related: [pinterest-engineering, pinterest-text-to-sql-architecture, text2sql-patterns]
sources: ["How we built Text-to-SQL at Pinterest.md"]
---
# Querybook

Querybook is Pinterest's in-house open-source big data SQL query tool. It serves as the primary interface for data analysis at Pinterest and was the natural deployment platform for the Text-to-SQL feature.

The Text-to-SQL feature was integrated directly into Querybook's interface, allowing users to ask analytical questions in natural language and receive generated SQL queries. The system uses WebSocket for streaming responses and integrates with [[Langchain]] for JSON parsing.

Querybook also incorporates the NLP-based table search functionality, enabling users to discover relevant tables through semantic similarity search in addition to the Text-to-SQL feature.