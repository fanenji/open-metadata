---
type: concept
title: dbt Custom Property Ingestion
created: 2026-05-25
updated: 2026-06-08
tags: [dbt, custom-properties, ingestion, metadata]
related: [dbt-integration, dbt-artifacts, custom-properties, dbt-lineage-ingestion, manifest-json, dbt-column-level-custom-properties]
sources: ["thinkwe-need-to-answer-how-can-i-ingest-custom-pro-2026-05-25-140121.md", research-ingestion-di-custom-properties-a-livello-di-colonn-2026-06-08.md]
---
# dbt Custom Property Ingestion

dbt Custom Property Ingestion is a mechanism that populates pre-defined [[custom-properties|Custom Properties]] in OpenMetadata with values declared in dbt model YAML files. It is a one-way flow: dbt → OpenMetadata. Properties must already exist in OpenMetadata before ingestion; dbt cannot create new property definitions.

> **⚠️ IMPORTANTE:** L'ingestion di custom properties da dbt è supportata **solo a livello tabella (model)**. L'ingestion a **livello colonna NON è supportata** da OpenMetadata (verificato empiricamente, giugno 2026). Qualsiasi custom property dichiarata sotto `columns → name → meta → openmetadata → customProperties` in `schema.yml` viene **ignorata** durante l'ingestion. Vedi [[dbt-column-level-custom-properties]] per i dettagli della verifica.

## Prerequisites

Custom properties **must be pre-defined** on the Table entity in OpenMetadata via **Settings → Custom Properties → Tables**. If a property referenced in dbt does not exist in OpenMetadata, the ingestion logs a warning and skips it.

## Declaring Custom Properties in dbt

Values are declared under the `meta.openmetadata.customProperties` key in `schema.yml` at the **model (table) level only**.

**Table-level example:**

```yaml
models:
  - name: customers
    description: "Customer master data table"
    meta:
      openmetadata:
        customProperties:
          sla_hours: 24
          data_steward: "John Doe"
          refresh_frequency: "daily"
```

> **⚠️ L'esempio column-level qui sotto NON FUNZIONA.** Viene mostrato solo per illustrare cosa **non** fare. OpenMetadata attualmente ignora le custom properties dichiarate a livello colonna.
>
> ```yaml
> # ❌ NON SUPPORTATO - Questo viene ignorato da OpenMetadata:
> models:
>   - name: customers
>     meta:
>       openmetadata:
>         customProperties:
>           data_classification: "Confidential"
>     columns:
>       - name: customer_id
>         meta:
>           openmetadata:
>             customProperties:
>               pii_level: "High"
> ```

## Supported Custom Property Types

OpenMetadata supports **14 custom property types** for dbt ingestion:

| Type | Example Value |
|------|---------------|
| `string` | `"value"` |
| `integer` | `42` |
| `number` | `3.14` |
| `markdown` | `"# Title"` |
| `sqlQuery` | `"SELECT ..."` |
| `email` | `"user@example.com"` |
| `date-cp` | `"2024-01-15"` |
| `dateTime-cp` | `"2024-01-15T10:30:00"` |
| `time-cp` | `"10:30:00"` |
| `timestamp` | Unix ms (e.g., `1705315200000`) |
| `duration` | ISO 8601 (e.g., `"P23DT23H"`) |
| `enum` | `"High"` or `["High","Critical"]` |
| `entityReference` | `{type: "user", fqn: "john.doe"}` |
| `entityReferenceList` | list of `{type:, fqn:}` |
| `timeInterval` | `{start: 1705..., end: 1705...}` |
| `table-cp` | list of row objects |

## Artifact Generation and Ingestion

After configuring `schema.yml`, run dbt commands (`dbt run`, `dbt compile`, `dbt docs generate`). The custom properties are embedded into [[dbt-artifacts|manifest.json]] under the model node's `config.meta.openmetadata.customProperties`. The standard dbt ingestion workflow (auto-ingest or YAML recipe) reads this block and assigns the values to the corresponding **tables only** in OpenMetadata. Column-level custom properties are **not ingested**.

## Validation and Graceful Degradation

The ingestion process validates each value against its defined type:

- **Invalid values** are skipped with a warning.
- **Values for undefined properties** are ignored.
- **Enum types**: invalid selections cause a warning; multi-select enum invalid entries are filtered out.

This graceful degradation ensures that a single misconfigured property does not fail the entire pipeline.

## Column-Level Support: NOT Available

**Confermato empiricamente (giugno 2026): l'ingestion di custom properties a livello colonna NON è supportata da OpenMetadata.**

L'analisi iniziale (2026-06-08) aveva ipotizzato che potesse funzionare basandosi su:
1. Il supporto nativo del field `meta` di dbt a livello colonna
2. Il precedente dei tag (che supportano l'ingestion column-level)
3. Assertion della community

Tuttavia, **la verifica empirica ha dimostrato il contrario**: OpenMetadata ignora completamente le custom properties dichiarate sotto `columns → name → meta → openmetadata → customProperties` nel `manifest.json`. Questo è coerente con il modello dati di OpenMetadata, dove le custom properties sono definite solo a livello di entità Table, non a livello di colonna.

Per i dettagli completi della verifica, vedi [[dbt-column-level-custom-properties]].

## Relationship to Other dbt Features

Custom property ingestion extends the standard [[dbt-integration]] by adding another metadata category that can be sourced from dbt artifacts, alongside descriptions, tags, ownership, and lineage.

## Open Questions

1. **Conflict Resolution**: What happens when a dbt-declared custom property value conflicts with a value already set manually in the OpenMetadata UI? The [[dbt-integration|dbt descriptions ingestion]] has an `Update Descriptions` toggle that controls overwrite behavior — but no analogous mechanism is documented for custom properties.

## References

1. [Ingest Custom Properties from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties)