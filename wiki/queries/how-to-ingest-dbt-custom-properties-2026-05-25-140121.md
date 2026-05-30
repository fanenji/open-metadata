---
type: query
title: "<think>We need to answer: \"how can i ingest custom propertie"
created: 2026-05-25
tags: []
---
To ingest custom properties from dbt, you declare them in your dbt model’s `schema.yml` file, run `dbt` to generate the `manifest.json` artifact, and let OpenMetadata’s dbt workflow read them into the platform. Here’s how to do it.

## 1. Pre‑define the Custom Properties in OpenMetadata

The custom properties **must already exist** on the **Table** entity in OpenMetadata before ingestion. You cannot create custom properties from dbt — only assign values to those that have been set up in Settings → Custom Properties → Tables [2]. If a property is not defined, the ingestion logs a warning and skips it.

## 2. Declare the Custom Properties in dbt

In your `schema.yml` file, use the `meta.openmetadata.customProperties` key to assign values to your pre‑defined properties. This works at both the model (table) level and the column level [1][2].

**Table‑level example:**

```yaml
models:
  - name: customers
    description: "Customer master data table"
    meta:
      openmetadata:
        customProperties:
          sla_hours: 24          # integer type
          data_steward: "John Doe"   # string type
          refresh_frequency: "daily" # enum type
```

**Column‑level example** (can be combined with table‑level):

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        customProperties:
          data_classification: "Confidential"
    columns:
      - name: customer_id
        meta:
          openmetadata:
            customProperties:
              pii_level: "High"
```

## 3. Supported Custom Property Types

OpenMetadata supports **14 custom property types** for dbt ingestion [2]:

| Type | Example Value |
|------|---------------|
| string | `"value"` |
| integer | `42` |
| number | `3.14` |
| markdown | `"# Title"` |
| sqlQuery | `"SELECT ..."` |
| email | `"user@example.com"` |
| date‑cp | `"2024-01-15"` |
| dateTime‑cp | `"2024-01-15T10:30:00"` |
| time‑cp | `"10:30:00"` |
| timestamp | Unix ms (e.g. `1705315200000`) |
| duration | ISO 8601 (e.g. `"P23DT23H"`) |
| enum | `"High"` or `["High","Critical"]` |
| entityReference | `{type: "user", fqn: "john.doe"}` |
| entityReferenceList | list of `{type:, fqn:}` |
| timeInterval | `{start: 1705..., end: 1705...}` |
| table‑cp | list of row objects |

Complex types like entity references and tables are documented in [2].

## 4. Generate the dbt Artifacts

After configuring `schema.yml`, run your dbt commands — `dbt run` (and optionally `dbt compile` / `dbt docs generate`). The custom properties are embedded into `manifest.json` under the model node’s `config.meta.openmetadata.customProperties` [2].

## 5. Ingest the Artifacts into OpenMetadata

Use either the **auto‑ingest** or **traditional YAML recipe** method to feed the artifacts to OpenMetadata (see the previous answer about dbt Core ingestion recipes). The ingestion process reads the `customProperties` block and assigns the values to the corresponding tables/columns in OpenMetadata [2].

## 6. View the Results

Once ingested, the custom properties appear on the table’s details page in the **Custom Properties** section of the OpenMetadata UI [2].

## Validation & Graceful Degradation

The ingestion validates each value against its defined type [2]:
- Invalid values are skipped with a warning.
- Values for undefined properties are ignored.
- For enum types, invalid selections cause a warning; multi‑select enum invalid entries are filtered out.

## Relationship to Other dbt Features

Custom property ingestion extends the standard [[dbt-integration]] by adding another metadata category that can be sourced from dbt artifacts, alongside descriptions, tags, ownership, and lineage [2].

<!-- cited: 2, 1 -->