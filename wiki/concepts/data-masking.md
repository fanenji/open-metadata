---
type: concept
title: Data Masking
created: 2026-04-08
updated: 2026-04-08
tags: [security, privacy, pii, etl]
related: [duckdb, ai-driven-data-query, data-governance]
sources: ["Beyond Storing Data How to Use DuckDB, MotherDuck and Kestra for ETL.md"]
---
# Data Masking

[[data-masking]] is a security technique used during the ETL (Extract, Transform, Load) process to protect sensitive information, such as Personally Identifiable Information (PII), by replacing it with unidentifiable or obfuscated data.

### Implementation in Modern Pipelines
In a modern, lightweight stack, masking can be performed "in-flight" using high-performance analytical engines like [[duckdb]].

**Common Techniques:**
- **Hashing**: Using functions like `md5()` or `hash()` to transform a sensitive string (e.g., an email address) into a unique, irreversible string.
- **Redaction**: Replacing parts of a string with a fixed character (e.g., `****`).
- **Substitution**: Replacing real values with realistic but fake data.

### Importance in ETL
Performing masking during the "Transform" step—specifically *before* the data is loaded into a permanent warehouse like [[motherduck]] or [[bigquery]]—is a critical component of a robust [[data-governance]] strategy. It ensures that sensitive data never reaches the persistent storage layer in its raw, identifiable form.
