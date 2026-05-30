---
type: entity
title: "Rsync"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: rsync
created: 2026-05-14
updated: 2026-05-14
tags: [file-transfer, upload, dbt, openmetadata]
related: [http-artifact-storage, dbt-artifact-storage, dbt-integration]
sources: ["dbt-artifact-storage---http-server-configuration-o-20260514.md"]
---

# rsync

rsync is a fast, versatile file copying tool for Unix-like systems. In the context of OpenMetadata's [[dbt-integration]], rsync is used as a manual upload method for transferring dbt JSON artifacts (manifest.json, catalog.json, run_results.json) to the [[http-artifact-storage]] server.

## Usage

```bash
rsync -avz target/*.json user@server:/var/www/dbt-artifacts/
```

rsync is also used in the automated Airflow DAG example for uploading artifacts after a dbt run completes.