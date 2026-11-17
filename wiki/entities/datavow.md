---
type: entity
title: DataVow
created: 2026-07-07
updated: 2026-07-07
tags: [odcs, data-contracts, dbt, validation, cli, open-source]
related: [dbt-to-odcs-mapping, odcs-open-data-contract-standard, data-contracts, dbt-model-contracts]
sources: ["research-openmetadata-112-odcs-31-bridge-per-dbt-data-contr-2026-07-07.md"]
---

# DataVow

**DataVow** è una CLI open-source per lo standard [[odcs-open-data-contract-standard|ODCS 3.1]] che offre validazione dati via DuckDB, sincronizzazione bidirezionale con [[dbt-model-contracts|dbt tests]], e integrazione GitHub Action per CI/CD.

## Funzionalità principali

- **Validazione DuckDB**: esegue i controlli di qualità definiti in un contratto ODCS 3.1 su dati reali usando DuckDB come engine embedded
- **dbt test sync**: sincronizza i test dbt con le regole `quality` di un contratto ODCS, mantenendo allineate le definizioni
- **GitHub Action**: integrazione nativa per eseguire validazioni a ogni push/PR
- **Vow Score**: metrica aggregata di conformità del contratto

## Rilevanza per OpenMetadata

DataVow può essere usato nel workflow di [[dbt-to-odcs-mapping|mapping dbt-to-ODCS]] come step intermedio: genera o valida il file ODCS prima dell'import in [[openmetadata|OpenMetadata]] via API REST.

## Collegamenti

- Repository: [github.com/data-vow/data-vow](https://github.com/data-vow/data-vow)
- Elencato nella [vendors list ufficiale ODCS](https://github.com/bitol-io/open-data-contract-standard/blob/main/vendors.md)