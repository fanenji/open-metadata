---
type: entity
title: Column Name Scanner
created: 2026-05-14
updated: 2026-05-14
tags: [regex, auto-classification, pii, classification-tags]
related: [auto-pii-tagging, entity-recognition-engine, auto-classification, classification-tags]
sources: ["auto-pii-tagging-guide-official-documentation---op-20260514.md"]
---
# Column Name Scanner

The Column Name Scanner is the regex-based detection component of the [[auto-pii-tagging]] workflow. It validates column names against a set of regular expression rules to identify columns likely to contain Personally Identifiable Information (PII).

## Detection Method

The scanner operates on **schema metadata only** — it examines column names without accessing the underlying data. This makes it:
- **Always active**: Does not depend on sample data ingestion being enabled
- **Fast**: Operates on schema information already available in the metadata graph
- **Language-specific**: The documented rule set targets common English patterns

## Pattern Coverage

The regex rule set is designed to identify column names matching common English patterns for:
- Email addresses (e.g., columns named `email`, `email_address`, `user_email`)
- Social Security Numbers (e.g., `ssn`, `social_security_number`)
- Bank account numbers (e.g., `bank_account`, `account_number`, `iban`)
- Other common PII-bearing column name patterns

The exact regex patterns are not enumerated in the official documentation.

## Relationship to Entity Recognition

The Column Name Scanner works alongside the [[entity-recognition-engine]] as a complementary detection method. While the scanner catches columns whose **names** suggest PII content, the entity recognition engine catches columns whose **data** contains PII regardless of column naming. Together they provide broader coverage than either method alone.

## Limitations

- **Naming convention dependent**: Columns with non-standard or non-English names may be missed
- **No data validation**: A column named `email` that contains non-PII data would still be flagged
- **Pattern scope**: The documented patterns cover common English conventions; organizations with non-English schemas may need additional customization