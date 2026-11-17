---
type: concept
title: dbt to ODCS Mapping
created: 2026-07-07
updated: 2026-07-07
tags: [dbt, odcs, data-contracts, mapping, interoperability, ingestion, automation]
related: [dbt-model-contracts, odcs-open-data-contract-standard, data-contracts, dbt-integration, dbt, openmetadata]
sources: ["research-openmetadata-112-odcs-31-bridge-per-dbt-data-contr-2026-07-07.md"]
---

# dbt to ODCS Mapping

Il mapping tra i campi di un [[dbt-model-contracts|dbt model contract]] e le sezioni dello standard [[odcs-open-data-contract-standard|ODCS 3.1]] è il fondamento per costruire un pipeline automatico di ingestione [[data-contracts|data contract]] in [[openmetadata|OpenMetadata]] via API REST.

## Tabella di mapping

| dbt Model Contract | ODCS 3.1 | Note |
|---|---|---|
| `columns[].name` | `schema[].name` | Mapping diretto |
| `columns[].data_type` | `schema[].logicalType` o `schema[].physicalType` | dbt data_type → ODCS logicalType |
| `columns[].constraints` (not_null) | `schema[].quality[]` (regola `nullCount` = 0) | Trasformazione constraint → quality rule |
| `columns[].constraints` (unique) | `schema[].quality[]` (regola `duplicateCount` = 0) | Idem |
| `columns[].constraints` (primary_key) | `schema[].primaryKey` (o custom property) | Dipende dalla piattaforma |
| `columns[].constraints` (foreign_key) | `customProperties` | Non ha equivalente nativo ODCS |
| `columns[].description` | `schema[].description` | Mapping diretto |
| `config.contract.enforced: true` | `status: active` | Interpretazione semantica |
| Modello dbt (nome) | `name` (nome contratto) | Mapping diretto |
| Test dbt associati | `quality[]` (custom, `engine: dbt`) | Via sezione quality custom |
| `meta` field dbt | `customProperties` | Per tags, owner, domain |
| — (non presente in dbt) | `sla` | Da arricchire manualmente |
| — (non presente in dbt) | `team`, `roles` | Da arricchire manualmente |
| — (non presente in dbt) | `servers` | Da arricchire manualmente |

## Workflow CI/CD in 3 fasi

### Fase 1: Estrazione dbt → ODCS

```
dbt manifest.json ──► [script di mapping] ──► contract.odcs.yaml
```

Script che legge `manifest.json` e `catalog.json` ed estrae:
- **Colonne**: da `nodes[].columns`
- **Constraints**: `not_null`, `primary_key`, `foreign_key`, `unique` → regole `quality` ODCS
- **Test**: da `nodes[].tests` → `quality[].custom` con `engine: dbt`
- **Metadati aggiuntivi**: `meta` field → `customProperties` ODCS

### Fase 2: Arricchimento

Il contratto ODCS viene arricchito con metadati semantici non presenti in dbt:
- SLA (refresh frequency, latency)
- Team e ruoli
- Classification tags, Domain, Data Product

### Fase 3: Import in OpenMetadata

```bash
curl -X PUT "https://{host}/api/v1/dataContracts/odcs/yaml?entityId={uuid}&entityType=table&mode=merge" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/yaml" \
  -d @contract.odcs.yaml
```

La modalità `merge` preserva gli arricchimenti manuali fatti in OpenMetadata, aggiornando solo i campi presenti nell'ODCS importato. Per un replace completo usare `mode=replace`.

## Strumenti utili

- **[[datavow|DataVow]]** — CLI open-source per ODCS 3.1 con validazione DuckDB, dbt test sync e GitHub Action
- **Data Contract CLI** — Linting, testing, import/export ODCS
- **FLUID Forge** — Python CLI per authoring data contract ODCS con round-trip lossless
- **[[openmetadata-dbt-action]]** — GitHub Action ufficiale per triggerare l'ingestione dbt in CI/CD

## Limitazioni

1. **entityType solo `table`**: l'import ODCS in OpenMetadata 1.12 supporta solo tabelle, non viste
2. **Nessun mapper nativo**: OpenMetadata non offre un convertitore built-in
3. **Metadati semantici assenti in dbt**: Domain, Tier, Tags vanno aggiunti a mano
4. **Flusso unidirezionale**: dbt → ODCS → OpenMetadata; l'inverso (OM → dbt) non ha senso perché dbt non consuma ODCS
5. **Versioning non allineato**: ODCS ha `version`, dbt ha il suo versioning interno — vanno sincronizzati manualmente

## Vedi anche

- [[dbt-model-contracts]] — Cosa sono i dbt model contracts
- [[odcs-open-data-contract-standard]] — Lo standard ODCS in dettaglio
- [[data-contracts]] — OpenMetadata Data Contracts
- [[dbt-integration]] — Panoramica integrazione dbt-OpenMetadata