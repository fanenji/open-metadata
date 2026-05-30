---
type: concept
title: "Custom Connector Deployment"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Custom Connector Deployment
created: 2026-05-14
updated: 2026-05-14
tags: [custom-connectors, deployment, docker, ingestion]
related: [custom-connectors, either-stacktrace-error, ingestion-framework, metadata-ingestion-workflow]
sources: ["custom-connectors-build-extend-openmetadata-easily-20260514.md"]
---

# Custom Connector Deployment

The 6-step workflow for deploying a custom connector from development to production.

## Step 1 — Prepare the Connector

Create a Python class that extends `Source` from `metadata.ingestion.api.steps` and implements the `_iter` generator method. See [[custom-connectors]] for the architecture details.

## Step 2 — Yield the Data

The `_iter` method must yield `CreateEntityRequest` objects wrapped in `Either` instances. Use the [[either-stacktrace-error]] pattern for structured error handling.

## Step 3 — Prepare the Package Installation

Package the connector code using a `setup.py` file so it can be installed in the ingestion environment.

## Step 4 — Prepare the Ingestion Image

Build a custom Docker image based on `openmetadata/ingestion` that includes the custom connector package:

```dockerfile
FROM openmetadata/ingestion:1.4.4
WORKDIR ingestion
USER airflow
COPY connector connector
COPY setup.py .
RUN pip install --no-deps .
```

## Step 5 — Run OpenMetadata with the Custom Ingestion Image

Use Docker Compose (or Kubernetes) with the custom ingestion image. The OpenMetadata Demos repository provides a Makefile for convenience.

## Step 6 — Configure the Connector in the UI

1. Go to the appropriate service type (e.g., Database Services > Add New Service > Custom)
2. Set the **Source Python Class Name** to the full module name, e.g., `connector.my_awesome_connector.MyAwesomeConnector`
3. The Ingestion Framework imports the class using this full module path

## Important Notes

- The full module name is critical — it must match the Python import path exactly
- For production, consider using a private package index instead of copying files
- The guide references version 1.4.4; verify compatibility with your OpenMetadata version
- See the OpenMetadata Demos repository for a working example