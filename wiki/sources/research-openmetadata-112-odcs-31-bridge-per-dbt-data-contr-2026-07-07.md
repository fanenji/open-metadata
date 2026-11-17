---
source_path: "[[raw/sources/research-openmetadata-112-odcs-31-bridge-per-dbt-data-contr-2026-07-07]]"
sources: [research-openmetadata-112-odcs-31-bridge-per-dbt-data-contr-2026-07-07.md]
tags: [research, data-contracts, odcs, dbt, openmetadata, interoperability]
related: [odcs-open-data-contract-standard, dbt-model-contracts, data-contracts, dbt-integration, openlineage-integration, dbt-to-odcs-mapping]
type: source
title: "Research: OpenMetadata 1.12 ODCS 3.1 bridge per dbt data contracts"
created: 2026-07-07
updated: 2026-07-07
---
# Research: OpenMetadata 1.12 ODCS 3.1 bridge per dbt data contracts

Ricerca web multi-query che esplora se il supporto ODCS 3.1 introdotto in [[openmetadata|OpenMetadata]] 1.12 può fungere da ponte per l'ingestione automatica dei [[dbt-model-contracts|dbt model contracts]] come [[data-contracts|OpenMetadata Data Contracts]].

## Risultati principali

1. **ODCS 3.1 è il formato ponte, ma manca automazione nativa**: OpenMetadata 1.12 espone API REST complete (`POST/PUT /v1/dataContracts/odcs`) per importare contratti in formato ODCS. Un dbt model contract può essere trasformato in ODCS 3.1 e importato, ma serve uno script di mapping custom.

2. **Mapping parziale ma sufficiente**: colonne, data types e constraints dbt mappano direttamente su campi ODCS. Manca la parte semantica (Domain, Tier, Tags, SLA) che dbt non ha nativamente e va arricchita.

3. **Esistono tool community**: [[datavow|DataVow]] (sync dbt test), Data Contract CLI, FLUID Forge — tool che possono accelerare l'adozione.

4. **Il valore reale è la portabilità**: ODCS previene vendor lock-in. Un contratto generato oggi può essere consumato da qualsiasi tool compatibile domani.

## Vedi anche

- [[dbt-to-odcs-mapping]] — Tabella di mapping e workflow CI/CD
- [[odcs-open-data-contract-standard]] — Lo standard ODCS
- [[dbt-model-contracts]] — I model contract di dbt
- [[data-contracts]] — OpenMetadata Data Contracts