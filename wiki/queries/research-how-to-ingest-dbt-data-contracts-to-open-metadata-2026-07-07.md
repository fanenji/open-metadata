---
type: query
title: "Research: how to ingest dbt data contracts to open-metadata"
created: 2026-07-07
updated: 2026-07-07
origin: deep-research
tags: [research]
sources: []
related: []
---

# Research: how to ingest dbt data contracts to open-metadata

# How to Ingest dbt Data Contracts into OpenMetadata

## Overview

Il termine "data contracts" ha due significati distinti ma correlati nel contesto dbt → OpenMetadata:

1. **dbt Model Contracts** — una feature nativa di dbt (introdotta in dbt Core 1.5) che permette di definire garanzie formali sulla struttura di un modello (nomi colonne, data types, constraints) usando `contract: {enforced: true}` [1]. dbt esegue un "preflight check" a build-time: se l'output SQL non corrisponde esattamente allo schema YAML dichiarato, la build fallisce [1][5].

2. **OpenMetadata Data Contracts** — un'entità nativa di OpenMetadata (introdotta in v1.12) che formalizza un accordo tra producer e consumer su schema, semantica, qualità, SLA e termini d'uso di un data asset [2][3]. Attualmente supportati solo per Table.

**La relazione**: Non esiste un'ingestione diretta "dbt model contracts → OpenMetadata Data Contracts". I due sistemi convivono: dbt model contracts vengono ingeriti come metadati di modello (colonne, constraint, test) tramite il normale workflow dbt, mentre gli OpenMetadata Data Contracts sono creati e gestiti nativamente in OpenMetadata (via UI o API).

## Come i dbt Model Contracts arrivano in OpenMetadata

### Cosa viene ingerito automaticamente

Quando il workflow dbt di OpenMetadata processa i file `manifest.json`, `catalog.json` e `run_results.json`, ingerisce automaticamente [1][4]:

- **Nomi e data type delle colonne** — definiti nel contract dbt, visibili come schema della tabella in OpenMetadata
- **Constraints** (`not_null`, `primary_key`, `foreign_key`, `unique`) — definite nel model contract, mappate come table constraints in OpenMetadata
- **Test results** — i test dbt associati al modello (inclusi quelli ridondanti con i constraints) appaiono nei risultati di qualità

### Bug noti (risolti in v1.12.4+)

Versioni di OpenMetadata precedenti alla 1.12.4 avevano un bug (#27161) che causava falsi version bump durante l'ingestione di modelli dbt con column-level constraints. In questi casi, le descrizioni delle colonne venivano corrotte a ogni ciclo di ingestione [7][8]. **Raccomandazione**: usare OpenMetadata ≥ 1.12.4.

## Configurazione del workflow dbt per l'ingestione

### dbt Core — Auto-ingest

1. Aggiungere le variabili OpenMetadata al `dbt_project.yml` [6]:

```yaml
vars:
  openmetadata_host_port: "https://your-openmetadata-server/api"
  openmetadata_jwt_token: "${OPENMETADATA_JWT_TOKEN}"
  openmetadata_service_name: "your-database-service-name"
```

2. Generare gli artifact:
```bash
dbt compile && dbt docs generate && dbt test
```

3. Eseguire l'ingestione:
```bash
metadata ingest-dbt
```

### dbt Core — External Workflow (YAML)

Configurare uno YAML di workflow con storage (S3, GCS, Azure, Local, HTTP) e puntare ai file artifact [4][10].

### dbt Cloud

Integrazione diretta via API. Richiede Account ID, Project ID, Job ID e API token (minimo permesso: `Account Viewer`) [9].

## OpenMetadata Data Contracts: workflow separato

Gli OpenMetadata Data Contracts sono un workflow UI-driven a 6 step [2]:

1. **Contract Details** — nome, owners, descrizione
2. **Schema** — selezione colonne dalla tabella
3. **Semantics** — regole di business (Owners, Tags, Domain, Tier, Description)
4. **Quality** — data quality tests
5. **Security** (nei contratti avanzati) — policy di accesso, tag di classificazione
6. **SLA** — refresh frequency, max latency, retention

I contratti supportano approval workflow e hanno stati: `DRAFT` → `ACTIVE` → `VIOLATED` [3].

## Gap: da dbt Model Contract a OpenMetadata Data Contract

Attualmente **non esiste un percorso automatizzato** che trasformi un dbt model contract in un OpenMetadata Data Contract. Le ragioni:

- **Diversa granularità**: il contract dbt opera a livello di build (previene la materializzazione), il contract OpenMetadata opera a livello di governance (monitora la conformità).
- **Diversi metadati**: dbt non ha concetti come SLA, Terms of Use, o Security policy che OpenMetadata richiede.
- **API-only per OpenMetadata Contracts**: la creazione programmatica è possibile via API REST (`POST /v1/dataContracts`) ma richiede di costruire l'intero payload JSON.

### Workaround possibili

1. **Creazione manuale nella UI**: dopo l'ingestione dbt, creare il Data Contract in OpenMetadata selezionando le colonne già popolate.
2. **Automazione via API**: scrivere uno script che legge il `manifest.json` dbt, estrae colonne e constraint, e chiama l'API OpenMetadata per creare un Data Contract corrispondente.
3. **GitHub Action**: usare [openmetadata-dbt-action](https://github.com/open-metadata/openmetadata-dbt-action) nella CI/CD per triggerare l'ingestione dopo ogni run dbt [8].

## Raccomandazioni

| Scenario                           | Approccio                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------- |
| dbt model contract come governance | Ingerire dbt metadata normalmente. Usare il "dbt tab" sulla Table Entity per visibilità. |
| OpenMetadata Data Contract formale | Creare via UI dopo l'ingestione dbt, selezionando le colonne dal modello già popolato.   |
| Automazione CI/CD                  | GitHub Action `openmetadata-dbt-action` + script API per creazione contract.             |
| Versione OpenMetadata              | ≥ 1.12.4 per evitare il bug #27161 dei falsi version bump.                               |

## Riferimenti

1. dbt Model Contracts — https://docs.getdbt.com/docs/mesh/govern/model-contracts
2. OpenMetadata Data Contracts Spec — https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/spec
3. Creating Data Contracts in OpenMetadata — https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/spec
4. Configure dbt Workflow — https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/configure-dbt-workflow
5. dbt contract reference — https://docs.getdbt.com/reference/resource-configs/contract
6. Auto Ingest dbt-core — https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/auto-ingest-dbt-core
7. GitHub Issue #27161: False version bumps during dbt ingestion — https://github.com/open-metadata/OpenMetadata/issues/27161
8. openmetadata-dbt-action — https://github.com/open-metadata/openmetadata-dbt-action
9. dbt Cloud API Guide — https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/dbt-cloud-api-guide
10. Run dbt Workflow Externally — https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/run-dbt-workflow-externally

## References

1. [dbt Model Contracts](https://docs.getdbt.com/docs/mesh/govern/model-contracts) — dbt Developer Hub
2. [OpenMetadata Data Contracts Spec](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/spec) — OpenMetadata Documentation
3. [Configure dbt Workflow](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/configure-dbt-workflow) — OpenMetadata Documentation
4. [dbt contract reference](https://docs.getdbt.com/reference/resource-configs/contract) — dbt Developer Hub
5. [Auto Ingest dbt-core](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/auto-ingest-dbt-core) — OpenMetadata Documentation
6. [GitHub Issue #27161: False version bumps during dbt ingestion](https://github.com/open-metadata/OpenMetadata/issues/27161) — GitHub
7. [openmetadata-dbt-action](https://github.com/open-metadata/openmetadata-dbt-action) — GitHub
8. [dbt Cloud API Guide](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/dbt-cloud-api-guide) — OpenMetadata Documentation
9. [Run dbt Workflow Externally](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/run-dbt-workflow-externally) — OpenMetadata Documentation
10. [dbt Model Contract Mechanics](https://adriennevermorel.com/notes/dbt-model-contract-mechanics/) — Blog
11. [Model Governance: access, contracts and namespaces](https://andrealeonel.substack.com/p/model-governance-access-contracts) — Substack
