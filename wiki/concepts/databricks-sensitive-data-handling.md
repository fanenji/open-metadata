---
type: concept
title: Databricks Sensitive Data Handling
created: 2026-04-29
updated: 2026-04-29
tags: [databricks, data-governance, pii, masking, encryption]
related: [databricks, unity-catalog, sensitive-data-handling-strategies, data-masking-techniques, data-classification-automation]
sources: ["Handling Sensitive Data in Your Data Platform.md"]
---
# Databricks Sensitive Data Handling

A collection of Databricks-specific techniques for handling sensitive data, including built-in functions and Unity Catalog features.

## Masking Functions

Databricks provides built-in SQL functions for masking values during ingestion and ETL:

- `regexp_replace` — for partial masking of emails, phone numbers, etc.
- `replace` — for replacing specific values with generic placeholders.
- `mask` — for custom masking with configurable characters.

## Encryption

Databricks supports `aes_encrypt` and `aes_decrypt` functions for field-level encryption, with keys stored in a Key Vault.

## Hashing

Databricks provides `sha2`, `md5`, and `hash` functions for generating irreversible hash values.

## Data Classification

Unity Catalog's Data Classification feature can automatically scan for sensitive categories like names, emails, and credit card numbers.

## Attribute-Based Access Control (ABAC)

Unity Catalog supports tagging sensitive columns and creating policies that apply masking or restrict access for specific groups.