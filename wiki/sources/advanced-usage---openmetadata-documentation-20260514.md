---
type: source
title: "Source: advanced-usage---openmetadata-documentation-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["advanced-usage---openmetadata-documentation-20260514.md"]
tags: []
related: []
---

# Source: advanced-usage---openmetadata-documentation-20260514.md

# Analysis: Advanced Usage - OpenMetadata Documentation (Data Quality as Code)

## Key Entities

| Entity | Type | Role | In Wiki? |
|--------|------|------|----------|
| **TestRunner** | Python SDK class | Central — primary API for programmatic data quality testing | **No** |
| **TestRunner.from_yaml()** | Method | Central — loads test configurations from YAML files/strings | **No** |
| **TestRunner.for_table()** | Method | Central — creates runner for a specific table | **No** |
| **TestRunner.setup()** | Method | Central — configures workflow behavior (force update, log level, success threshold) | **No** |
| **TestRunner.run()** | Method | Central — executes configured tests | **No** |
| **TestRunner.test_definitions** | Property | Peripheral — access configured test definitions before execution | **No** |
| **TableRowCountToBeBetween** | Test definition class | Peripheral — table-level row count validation | **No** |
| **ColumnValuesToBeNotNull** | Test definition class | Peripheral — column-level null check | **No** |
| **ColumnValuesToBeUnique** | Test definition class | Peripheral — column-level uniqueness check | **No** |
| **ColumnValuesToMatchRegex** | Test definition class | Peripheral — column-level regex validation | **No** |
| **LogLevels** | Enum | Peripheral — log level configuration | **No** |
| **openmetadataServerConfig** | Configuration block | Peripheral — server connection settings in YAML | **No** |
| **OPENMETADATA_JWT_TOKEN** | Environment variable | Peripheral — recommended token injection method | **No** |

## Key Concepts

| Concept | Definition | Why It Matters | In Wiki? |
|---------|-----------|----------------|----------|
| **Data Quality as Code** | Managing data quality test definitions as version-controlled code (YAML + Python SDK) | Enables CI/CD integration, reproducibility, and automation of quality testing | **No** |
| **YAML-based test loading** | Loading test definitions from YAML workflow files via `TestRunner.from_yaml()` | Allows version-controlled, declarative test configuration | **No** |
| **Programmatic test configuration** | Using Python SDK (`TestRunner.for_table()`, `.add_test()`, `.setup()`) to configure tests | Enables dynamic test generation and integration with existing Python workflows | **No** |
| **forceUpdate** | Configuration flag to update existing test definitions | Controls whether tests are re-created or updated | **No** |
| **success_threshold** | Percentage threshold for overall test success | Enables quality gates with configurable pass/fail criteria | **No** |
| **enable_streamable_logs** | Real-time log streaming during test execution | Improves debugging and observability | **No** |
| **TestSuite entity** | OpenMetadata entity type representing a collection of tests | Core organizational unit for data quality testing | **No** |
| **entityFullyQualifiedName** | Fully qualified name of the target table/entity | Identifies which data asset tests apply to | **No** |

## Main Argume
