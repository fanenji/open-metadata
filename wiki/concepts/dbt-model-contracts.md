---
type: concept
title: dbt Model Contracts
created: 2026-07-07
updated: 2026-07-07
tags: [dbt, model-contracts, data-quality, governance, ingestion, schema]
related: [dbt, dbt-integration, data-contracts, dbt-artifacts, manifest-json, dbt-lineage-ingestion, dbt-troubleshooting]
sources: ["research-how-to-ingest-dbt-data-contracts-to-open-metadata-2026-07-07.md"]
---

# dbt Model Contracts

I **dbt Model Contracts** sono una feature nativa di [[dbt]] (introdotta in dbt Core 1.5) che permette di definire garanzie formali sulla struttura di un modello: nomi colonne, data types e constraints.

## Funzionamento

Quando un modello ha `contract: {enforced: true}` nel suo YAML di configurazione, dbt esegue un **preflight check** a build-time: se l'output SQL non corrisponde esattamente allo schema dichiarato, la build fallisce e il modello non viene materializzato.

```yaml
models:
  - name: dim_customers
    config:
      contract:
        enforced: true
    columns:
      - name: customer_id
        data_type: int
        constraints:
          - type: not_null
      - name: customer_name
        data_type: string
```

Il contract impone che **tutte** le colonne del modello siano dichiarate esplicitamente con `name` e `data_type`.

## Constraints supportate

Le constraints variano per piattaforma e si dividono in tre categorie:
- **Definibili e enforced** — la build fallisce se violate (es. `not_null` su Snowflake, Postgres)
- **Definibili ma non enforced** — metadata-only (comune nei cloud data warehouse)
- **Non supportate** — la piattaforma non le riconosce

## Differenza dai test dbt

I model contracts definiscono la **forma** del dataset e operano a build-time (prevengono la materializzazione). I [[dbt-artifacts|test dbt]] validano il **contenuto** dopo la build e sono più flessibili. In alcuni casi un constraint può sostituire un test equivalente (es. `not_null`), con il vantaggio di essere enforceato a build-time e consumare meno compute.

## Ingestione in OpenMetadata

Quando il workflow dbt di [[openmetadata|OpenMetadata]] processa i file `manifest.json`, `catalog.json` e `run_results.json`, **ingerisce automaticamente**:

- **Nomi e data type delle colonne** — definiti nel contract, visibili nello schema della tabella
- **Constraints** (`not_null`, `primary_key`, `foreign_key`, `unique`) — mappate come table constraints
- **Test results** — i test associati al modello appaiono nei risultati di [[data-quality]]

Non esiste un'ingestione diretta "dbt model contract → OpenMetadata Data Contract". I due sistemi sono indipendenti. Vedi [[data-contracts]] per gli OpenMetadata Data Contracts.

## Bug noto

In OpenMetadata < 1.12.4, i modelli dbt con column-level constraints causano falsi version bump a ogni ciclo di ingestione, corrompendo le descrizioni delle colonne (issue [#27161](https://github.com/open-metadata/OpenMetadata/issues/27161)). **Raccomandazione**: usare OpenMetadata ≥ 1.12.4.

## Related

- [[dbt]] — Il tool di data transformation
- [[dbt-integration]] — Overview dell'integrazione dbt-OpenMetadata
- [[data-contracts]] — OpenMetadata Data Contracts (entità separata)
- [[dbt-artifacts]] — I file JSON ingeriti da OpenMetadata
- [[manifest-json]] — L'artifact principale che trasporta i metadati del contract
- [[dbt-troubleshooting]] — Troubleshooting dell'integrazione