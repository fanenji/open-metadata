---
type: concept
title: Data Quality as Code
created: 2026-05-14
updated: 2026-05-15
tags:
  - data-quality
  - sdk
  - python
  - testing
  - etl
  - automation
  - ci-cd
  - openmetadata
related:
  - testrunner-api
  - test-runner
  - dataframe-validation
  - test-definition-sources
  - data-quality
  - ingestion-framework
  - openmetadata-collaboration
  - personal-access-token
  - openmetadata-python-sdk
  - metadata-cli
  - sdk-configuration
  - test-definitions-reference
  - metadata-ingestion-workflow
  - data-quality-sdk
  - data-profiling
  - publishing-quality-results
  - dynamic-test-generation
  - multi-table-validation
  - dataframe-validator
  - dbt-integration
sources:
  - data-quality-as-code---openmetadata-documentation-20260514.md
  - getting-started-with-data-quality-as-code---openme-20260514.md
  - testrunner---running-table-level-tests---openmetad-20260514.md
  - dataframe-validation---openmetadata-documentation-20260514.md
  - publishing-results-best-practices---openmetadata-d-20260514.md
---
# Data Quality as Code

Data Quality as Code is a programmatic paradigm in OpenMetadata where data quality tests and validation workflows are defined, managed, and executed using the OpenMetadata Python SDK, rather than solely through the UI or static YAML configuration files. This approach enables automated, pipeline‑integrated quality validation that can be version‑controlled, reviewed, and deployed as part of standard software engineering practices. By integrating data quality validation directly into data pipelines, it ensures data quality is verified at every stage of the data lifecycle. It also promotes a separation of concerns: data stewards can define quality criteria in the UI while engineers execute those tests in code, and test criteria can be dynamically updated without code deployments. Key capabilities include dynamic test generation, multi‑table validation, publishing results back to OpenMetadata for tracking and alerting, and robust error handling with retries.

## Key Concepts

- **Programmatic test definition** – Tests are defined in Python using built‑in test definition classes (e.g., `TableRowCountToBeBetween`, `ColumnValuesToBeNotNull`). Supports inline definition, loading from the OpenMetadata UI, or importing from YAML files.
- **Fluent API** – The [[test-runner|TestRunner]] and [[dataframe-validation|DataFrameValidator]] classes provide builder‑pattern APIs for creating, configuring, and running tests.
- **Collaborative workflow** – Data stewards define test criteria in the UI while engineers execute those same tests in automated pipelines, enabling a shared responsibility model.
- **ETL integration** – Tests can be run as a validation step after data loading, with short‑circuit and rollback capability on failure.
- **Short‑circuit ETL** – Validation results decide whether data is loaded; pipelines fail fast when quality checks fail.
- **Separation of concerns** – Stewards define criteria, engineers execute; test criteria changes do not require code deployments.
- **Version control** – Test definitions can be stored in Git repositories alongside application code, enabling review, versioning, and audit.
- **Automation & reproducibility** – Tests run automatically and consistently across environments.
- **Test loading from OpenMetadata** – Tests configured in the UI can be loaded at runtime via `add_openmetadata_table_tests()` on a DataFrameValidator or similar mechanisms in TestRunner.
- **Dynamic test generation** – Tests can be generated programmatically based on table metadata (column constraints, data types), reducing manual effort and ensuring coverage matches schema changes. (See [[dynamic-test-generation]].)
- **Multi‑table validation** – Multiple tables can be validated in a single workflow with aggregated summary reporting, enabling pipeline‑level quality gates. (See [[multi-table-validation]].)
- **Publishing results** – Validation outcomes can be published back to OpenMetadata for historical tracking, alerting, dashboards, collaboration, and compliance. (See [[publishing-quality-results]].)
- **Error handling with retries** – Production‑grade error handling with exponential backoff retry for transient failures (e.g., `ConnectionError`) and immediate failure for configuration errors (e.g., `ValueError`).
- **Consistency** – The same test definitions can be used for table‑level validation and DataFrame validation, ensuring uniform quality criteria.

## Benefits

- Integration with ETL workflows – Run data quality tests directly within existing Python‑based ETL pipelines.
- CI/CD integration – Tests can be run as part of automated pipelines, enabling data quality gates in deployment workflows.
- Version control – Manage test definitions alongside code in version control systems (e.g., Git).
- Developer‑friendly – Use familiar Python syntax and IDE features for test development.
- Programmatic control – Dynamically generate tests based on data discovery or metadata.
- Immediate feedback – Validate data transformations before loading to destinations.
- Shared responsibility / Collaboration – Data stewards define tests in the OpenMetadata UI, engineers execute them in code.
- Automation & consistency – Tests run automatically and consistently across environments.
- Traceability – Test definitions are version‑controlled and auditable.
- Scalability – Programmatic execution enables testing across hundreds of tables with consistent patterns.
- Separation of concerns – Quality criteria are managed by domain experts, execution by engineers.
- Dynamic updates – Test criteria changes in the UI are reflected in code pipelines without redeployment.
- Consistency – Same test definitions can be reused for table‑level and DataFrame validation.
- Dynamic test generation – Reduces manual effort and ensures test coverage adapts as schemas evolve.
- Multi‑table validation – Enables pipeline‑level quality gates by validating multiple tables in one workflow.
- Publishing results – Provides full traceability, alerting, and compliance through publication of outcomes.

## Key Components

- **[[test-runner|TestRunner]]** – The core execution engine for running tests against a table Fully Qualified Name (FQN). It allows adding predefined or custom tests and executing them programmatically using a fluent API. Results can be published back to OpenMetadata.
- **[[dataframe-validation|DataFrameValidator]]** – A class for validating in‑memory pandas DataFrames against OpenMetadata table test definitions, bridging data processing with metadata‑driven quality checks. Supports chunk‑based validation for large datasets.
- **[[testrunner-api]]** – Execute tests against tables cataloged in OpenMetadata and publish results.
- **[[data-quality-sdk]]** – Reference for the `metadata.sdk.data_quality` module.
- **[[test-definition-sources]]** – Define tests inline, load from OpenMetadata UI, or import from YAML files.
- **[[sdk-configuration]]** – Required SDK setup for programmatic access.
- **[[test-definitions-reference]]** – Catalog of available test classes.
- **[[data-profiling]]** – Complements validation by observing data characteristics.

## Prerequisites

- Python 3.10+
- `openmetadata-ingestion` package v1.11.0.0 or later (v1.12.0.0+ recommended for the full feature set, including DataFrame validation extras)
- OpenMetadata instance v1.11.0+
- Valid JWT token for authentication (see [[personal-access-token]])

## Getting Started

### Installation

```bash
pip install "openmetadata-ingestion>=1.12.0.0"
```

Optional extras are available for database connectors and DataFrame support.

### Authentication

Use the `configure()` function from `metadata.sdk` with a JWT token. Tokens can be obtained from pre‑configured bots (like the `ingestion-bot`) or custom bots created in **Settings > Bots**. For production, pass the token via environment variables (`OPENMETADATA_HOST`, `OPENMETADATA_JWT_TOKEN`) instead of hardcoding it.

```python
from metadata.sdk import configure

configure(host="your_openmetadata_host", jwt_token="your_jwt_token")
```

### Table-Level Tests with TestRunner

The [[test-runner|TestRunner]] class provides a fluent API for table‑level tests.

```python
from metadata.sdk import TestRunner
from metadata.sdk.tests import TableRowCountToBeBetween

runner = TestRunner.for_table("service.database.schema.table")
runner.add_test(TableRowCountToBeBetween(min=100, max=1000))
results = runner.run()
```

### DataFrame Validation with DataFrameValidator

The [[dataframe-validation|DataFrameValidator]] class enables validating pandas DataFrames.

```python
from metadata.sdk.data_quality import ColumnValuesToBeNotNull, ColumnValuesToBeUnique
from metadata.sdk import DataFrameValidator

validator = DataFrameValidator()
validator.add_tests(
    ColumnValuesToBeNotNull(column="customer_id"),
    ColumnValuesToBeUnique(column="customer_id")
)
result = validator.validate(df)
print(result.success, result.failures)
```

#### Loading Tests from OpenMetadata

Tests defined in the UI can be loaded at runtime:

```python
validator.add_openmetadata_table_tests("BigQuery.analytics.staging.customers")
```

### Short-Circuit ETL Pattern

Integrate validation directly into a pipeline:

```python
result = validator.validate(df)
if result.success:
    load_to_warehouse(df)
else:
    raise Exception("Data quality validation failed")
```

The same pattern can be applied with `TestRunner.run()`.

## Advanced Capabilities

### Publishing Results

Validation outcomes can be published back to OpenMetadata, enabling historical tracking, alerting, dashboards, and compliance. The SDK supports result publication through parameters such as `publish_results=True` in `run()` calls. This is essential for governance and observability. See [[publishing-quality-results]] for detailed configuration.

### Dynamic Test Generation

Instead of manually writing tests, you can programmatically generate test definitions based on table metadata (e.g., column constraints, data types). This reduces manual effort and ensures test coverage adapts as schemas evolve. See [[dynamic-test-generation]] for implementation patterns.

### Multi-Table Validation

For pipelines that process multiple tables, the SDK allows you to validate several tables in a single workflow and aggregate the results into a summary report. This enables pipeline‑level quality gates. See [[multi-table-validation]].

### Error Handling with Retries

Production deployments should implement retry logic for transient failures (e.g., network issues). A common pattern uses exponential backoff via `tenacity` or custom decorators. Configuration errors (e.g., invalid table FQN) should fail immediately. The SDK is designed to integrate with such patterns.

### Chunk-Based Validation

For very large DataFrames, the [[dataframe-validation|DataFrameValidator]] can process data in chunks with success/failure callbacks, enabling efficient validation without loading entire datasets into memory.

## Architecture

Data Quality as Code integrates with OpenMetadata’s existing data quality infrastructure:

- **Test Definitions** – Can be defined in code, loaded from OpenMetadata, or imported from YAML files.
- **Execution Engine** – Leverages OpenMetadata’s proven test execution engine.
- **Result Publishing** – Test results can be published back to OpenMetadata for visualization and alerting.
- **Service Connections** – Automatically uses service connections configured in OpenMetadata.

Both `TestRunner` and `DataFrameValidator` use the same underlying test execution infrastructure, ensuring consistent behavior.

## Use Cases

### ETL Data Validation
Validate data after extraction and transformation, before loading to the destination. If validation fails, the pipeline can alert the team or let OpenMetadata handle notifications through [[data-observability-alerts]]. The SDK also supports rollback on failure, enabling safer pipeline execution. The short‑circuit pattern provides immediate failure on quality violations.

### Collaborative Quality Management
Data stewards define tests in the OpenMetadata UI, and engineers execute those tests in their code pipelines. This enables a shared responsibility model where domain experts define quality rules and engineers integrate them into automated workflows. Test criteria changes in the UI are immediately picked up by running the same tests without code changes.

### Chunk-Based Validation
Validate large datasets processed in chunks with success/failure callbacks, enabling efficient processing of data that does not fit in memory. This is available via the [[dataframe-validation]] component.

### Dynamic Test Updates
Because tests can be loaded from OpenMetadata at runtime, quality criteria can be updated in the UI and automatically applied in pipelines without redeployment. This enables a responsive quality management workflow.

### Dynamic Test Generation
Automatically generate test definitions from table metadata (column constraints, types, profiling data) to keep test coverage aligned with evolving schemas. See [[dynamic-test-generation]].

### Multi-Table Validation
Validate multiple tables in a single pipeline run and aggregate results to create pipeline-level quality gates. See [[multi-table-validation]].

### Publishing Results for Compliance and Observability
Publish validation results to OpenMetadata for audit trails, dashboards, and alerting. See [[publishing-quality-results]].

## Best Practices

- Version control test configurations (store YAML or Python files in Git).
- Use environment variables for credentials (host, JWT token).
- Implement retries for transient failures (e.g., connection timeouts) with exponential backoff.
- Publish results to enable tracking, alerting, and governance.
- Monitor execution metrics (e.g., test pass/fail rates, run times).
- Handle errors explicitly – fail fast on configuration errors, retry on transient issues.
- Use descriptive test names and descriptions for clarity in reports.
- Validate incrementally (test early and often at each pipeline stage).
- Separate concerns: data stewards define tests, engineers execute them.
- Test your test definitions by running them against sample data.
- Use the short‑circuit pattern to fail fast on quality violations.
- Integrate tests into CI/CD pipelines to enforce data quality gates at deployment.

## Relationship to Other Test Definition Methods

### UI-Based Quality

Data Quality as Code complements the UI‑based data quality configuration in [[data-quality]]. While the UI provides a visual interface for ad‑hoc test setup, the SDK approach is better suited for automated, repeatable, and version‑controlled workflows. The [[test-runner]] and [[dataframe-validation]] can also execute tests defined in the OpenMetadata UI without redefining them in code, enabling a hybrid approach where:

- Business‑critical thresholds are maintained by data stewards in the UI.
- Pipeline‑integrated validation is managed by engineers in code.
- Both approaches use the same underlying test infrastructure.
- Test criteria can be updated in the UI and dynamically loaded by SDK‑based pipelines.

### YAML-Based Configuration

Data Quality as Code also complements the YAML‑based test configuration approach. YAML configs are version‑controlled and audit‑friendly, while programmatic generation is schema‑responsive and automated. The choice between them depends on the use case: static, well‑understood schemas benefit from YAML; dynamic or rapidly evolving schemas benefit from programmatic generation. Both approaches can be combined in a single workflow.

## Open Questions

- How are UI‑defined tests version‑controlled? The documentation promotes version control as a benefit, but the collaborative workflow stores test definitions in the UI.
- What happens when tests defined in code conflict with tests defined in the UI for the same table?
- Is there a mechanism to export UI‑defined tests to YAML for version control?
- The full list of supported test types in the SDK (beyond `TableRowCountToBeBetween` and `ColumnValuesToBeNotNull`) is not yet fully documented.
- Are column‑level tests supported via the SDK, or only table‑level tests?
- How are SDK‑based test results persisted and integrated with the alerting system compared to UI‑configured tests?

## Connections

Data Quality as Code extends the following OpenMetadata concepts:
- [[data-quality]] – with a programmatic, code‑driven dimension beyond UI‑based testing.
- [[ingestion-framework]] – by showing how the SDK can be used for quality testing beyond metadata ingestion.
- [[openmetadata-collaboration]] – through the collaborative workflow where stewards define tests and engineers execute them.
- [[dbt-integration]] – in that both involve external validation/transformation results published back to OpenMetadata.
- [[data-profiling]] – dynamic test generation leverages profiling metadata.

Related concepts:
- [[personal-access-token]] for JWT‑based authentication.
- [[data-observability-alerts]] for notification on test failures.
- [[openmetadata-python-sdk]] and [[metadata-cli]] for broader SDK capabilities.
- [[dynamic-test-generation]]
- [[multi-table-validation]]
- [[publishing-quality-results]]