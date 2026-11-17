---
type: query
title: "Research: OpenMetadata 1.12 ODCS 3.1 bridge per dbt data contracts"
created: 2026-07-07
updated: 2026-07-07
origin: deep-research
tags: [research]
sources: []
related: []
---

# Research: OpenMetadata 1.12 ODCS 3.1 bridge per dbt data contracts

# OpenMetadata 1.12 + ODCS 3.1: un ponte per i dbt Data Contracts?

## Overview

OpenMetadata 1.12 ha introdotto il supporto nativo per lo standard **ODCS (Open Data Contract Standard) 3.1**, sia in import che in export [1][2]. Questa novità apre potenzialità interessanti per l'integrazione con strumenti esterni — incluso [[dbt]] — ma la domanda "può ODCS fare da ponte per l'ingestione automatica dei dbt model contracts in OpenMetadata?" richiede un'analisi a più livelli.

La risposta breve: **sì, ODCS 3.1 può essere il formato intermedio per convertire dbt model contracts in [[data-contracts|OpenMetadata Data Contracts]], ma non esiste un percorso automatico nativo**. Servono script di trasformazione.

## Cosa è cambiato in OpenMetadata 1.12

### Supporto ODCS 3.1 nativo

OpenMetadata 1.12 espone API REST complete per l'import/export in formato ODCS 3.1 [2]:

| Operazione | Endpoint | Metodo |
|---|---|---|
| Import da ODCS JSON | `/v1/dataContracts/odcs` | POST |
| Import da ODCS YAML | `/v1/dataContracts/odcs/yaml` | POST |
| Create-or-Update da ODCS JSON | `/v1/dataContracts/odcs` | PUT |
| Create-or-Update da ODCS YAML | `/v1/dataContracts/odcs/yaml` | PUT |
| Export in ODCS JSON | `/v1/dataContracts/{id}/odcs` | GET |
| Export in ODCS YAML | `/v1/dataContracts/{id}/odcs/yaml` | GET |

Le API PUT supportano due modalità: `merge` (preserva campi esistenti non inclusi nell'import) e `replace` (sovrascrive completamente il contratto) [2]. Questo permette un'integrazione CI/CD in cui un contratto ODCS generato esternamente viene sincronizzato a ogni build.

### Cosa contengono gli OpenMetadata Data Contracts

I contratti in OpenMetadata coprono sei dimensioni [3]:
1. **Contract Details** — nome, owners, descrizione
2. **Schema** — selezione colonne dalla tabella
3. **Semantics** — regole di business (Owners, Tags, Domain, Tier, Description)
4. **Quality** — data quality tests
5. **Security** — policy di accesso, tag di classificazione
6. **SLA** — refresh frequency, max latency, retention

È una specifica più ricca di ODCS (che copre schema, quality, SLA, pricing, team, servers) e **decisamente più ricca** dei dbt model contracts (che coprono solo colonne, data types e constraints).

## ODCS 3.1: cosa contiene lo standard

ODCS (Open Data Contract Standard) è nato in PayPal per supportare iniziative Data Mesh ed è oggi parte del progetto Bitol della Linux Foundation, con licenza Apache 2.0 [4][5].

Le sezioni dello standard ODCS 3.1 [6][7]:

| Sezione | Contenuto |
|---|---|
| **Fundamentals** | ID, name, version, status, domain, owner, description |
| **Schema** | Array di oggetti con nome, logicalType, physicalType, description, classification, quality, customProperties |
| **Data Quality** | Regole testuali, SQL, libreria (`rowCount`, `unique`, `freshness`), o custom (Soda, Great Expectations, dbt tests) |
| **SLA** | Service-level agreement |
| **Pricing** | Costo del dataset |
| **Team** | Team e ruoli |
| **Roles** | Ruoli con permessi di accesso |
| **Servers** | Server, environment, tipo (BigQuery, Snowflake, ecc.) |
| **Support** | Canali di comunicazione |
| **customProperties** | Estensioni vendor-specific |

Un aspetto chiave di ODCS 3.1 è la **strict JSON Schema validation**: campi non definiti nello schema vengono flaggati come errori, garantendo interoperabilità tra tool [5].

### ODCS e dbt

ODCS supporta nativamente riferimenti a regole di qualità esterne, incluse quelle dbt. Nella sezione `quality` è possibile usare il tipo `custom` per riferirsi a dbt tests, Soda, Great Expectations o Monte Carlo [6]:

```yaml
quality:
  - type: custom
    description: dbt test checks
    engine: dbt
```

Inoltre, tool come **DataVow** (open-source CLI per ODCS 3.1) offrono sync bidirezionale con dbt tests e validazione DuckDB [8]. Anche **FLUID Forge** supporta import/export bidirezionale ODCS 3.1 con lossless round-trip [8].

## Il gap: da dbt Model Contract a ODCS

[[dbt-model-contracts|I dbt model contracts]] definiscono una garanzia build-time sulla struttura di un modello: nomi colonne, data types, e constraints (`not_null`, `primary_key`, `foreign_key`, `unique`). Se l'output SQL non corrisponde allo YAML dichiarato, la build fallisce [9].

Il mapping concettuale tra dbt model contract e ODCS è parziale ma realizzabile:

| dbt Model Contract | ODCS 3.1 |
|---|---|
| `columns[].name` | `schema[].name` |
| `columns[].data_type` | `schema[].logicalType` o `schema[].physicalType` |
| `columns[].constraints` (not_null) | `schema[].quality[]` (regola `nullCount` = 0) |
| `columns[].constraints` (unique) | `schema[].quality[]` (regola `duplicateCount` = 0) |
| `columns[].constraints` (primary_key) | `schema[].primaryKey` (o custom property) |
| `columns[].description` | `schema[].description` |
| `config.contract.enforced: true` | `status: active` |
| Modello dbt | `name` (nome contratto) |
| Test dbt associati | `quality[]` (custom, engine: dbt) |
| — (non presente in dbt) | `sla`, `pricing`, `team`, `roles`, `servers`, `support` |

**Quello che manca in dbt**: SLA, pricing, team, ruoli, servers, classification, e i metadati semantici avanzati (Domain, Tier, Tags) che OpenMetadata richiede.

## Workflow di integrazione proposto

Ecco un pipeline in 3 fasi per usare ODCS 3.1 come ponte:

### Fase 1: Estrazione da dbt → ODCS

Script che legge `manifest.json` e `catalog.json` dbt e produce un file ODCS 3.1:

```
dbt manifest.json ──► [script di mapping] ──► contract.odcs.yaml
```

Cosa mappare:
- **Colonne**: da `nodes[].columns` nel manifest
- **Constraints**: da `nodes[].constraints` (not_null, primary_key, foreign_key, unique) → regole `quality` ODCS
- **Test**: da `nodes[].tests` → sezione `quality[].custom` con `engine: dbt`
- **Metadati aggiuntivi**: `meta` field dbt può contenere tags, owner, domain (se configurato) → `customProperties` ODCS

### Fase 2: Arricchimento (opzionale)

Il contratto ODCS generato può essere arricchito manualmente o via script con:
- SLA (refresh frequency, latency)
- Team e ruoli
- Classification tags
- Domain e Data Product reference

### Fase 3: Import in OpenMetadata

```bash
# Import del contratto ODCS in OpenMetadata
curl -X PUT "https://{openmetadata-host}/api/v1/dataContracts/odcs/yaml?entityId={table-uuid}&entityType=table&mode=merge" \
  -H "Authorization: Bearer {jwt-token}" \
  -H "Content-Type: application/yaml" \
  -d @contract.odcs.yaml
```

Il `mode=merge` è cruciale perché preserva eventuali arricchimenti manuali fatti in OpenMetadata, aggiornando solo i campi presenti nell'ODCS importato.

## Tool e risorse utili

- **[Data Contract CLI](https://github.com/datacontract/datacontract-cli)** — Open-source, supporta linting, testing, import/export ODCS [8]
- **[DataVow](https://github.com/data-vow/data-vow)** — CLI open-source per ODCS 3.1 con validazione DuckDB, dbt test sync, GitHub Action [8]
- **[FLUID Forge](https://github.com/sherifabdulaziz/fluid-forge)** — Python CLI per authoring, planning e apply di data contracts ODCS 3.1 con round-trip lossless [8]
- **[ODCS Python Package](https://pypi.org/project/open-data-contract-standard/)** — Lettura/scrittura YAML/JSON ODCS [8]
- **[OpenMetadata dbt Action](https://github.com/open-metadata/openmetadata-dbt-action)** — GitHub Action per triggerare l'ingestione dbt in CI/CD [10]

## Limitazioni attuali

1. **Nessun mapper nativo**: OpenMetadata non offre un convertitore "dbt model contract → ODCS → Data Contract". Serve sviluppo custom.
2. **Entità limitate**: l'import ODCS in OpenMetadata 1.12 supporta solo `entityType=table`. I model contract dbt che generano viste non sono coperti.
3. **Metadati semantici assenti in dbt**: Domain, Tier, Tags, Data Product sono concetti OpenMetadata-specifici che dbt non ha nativamente. Vanno aggiunti a mano o via `meta` field.
4. **Versioning**: ODCS 3.1 ha un campo `version` per il versioning del contratto, ma non è automaticamente allineato con i version bump di dbt.
5. **Bidirectionalità incompleta**: l'export ODCS da OpenMetadata → dbt non ha senso (dbt non consuma ODCS). Il flusso è unidirezionale: dbt → ODCS → OpenMetadata.

## Raccomandazioni

| Scenario | Approccio |
|---|---|
| Ingestione esistente dbt | Continuare con il workflow dbt standard. I model contract vengono già ingeriti come metadati di colonna e constraint |
| Data contract formali | Creare manualmente in OpenMetadata (UI wizard) o importare via ODCS se generati da tool esterni |
| Automazione CI/CD | Script custom che: `dbt docs generate` → estrai metadati → produci ODCS YAML → `POST` API OpenMetadata |
| Tool esterno | Valutare Data Contract CLI o DataVow per generare ODCS da sorgenti eterogenee, poi importare in OpenMetadata |
| OpenMetadata ≥ 1.12.4 | Necessario per evitare il bug #27161 dei falsi version bump |

## Conclusione

ODCS 3.1 è esattamente il tassello che mancava per rendere OpenMetadata interoperabile con tool esterni di data contract. **Tecnicamente, è possibile costruire un pipeline che trasforma i dbt model contracts in ODCS 3.1 e li importa in OpenMetadata**, ma richiede:

1. Uno script di mapping dbt → ODCS (community-driven o custom)
2. Arricchimento con metadati semantici (Domain, Tier, Tags) non presenti in dbt
3. Integrazione CI/CD per mantenere il contratto sincronizzato a ogni build dbt

Il valore reale di ODCS in OpenMetadata non è tanto il bridge dbt-specifico, quanto la **portabilità**: un contratto ODCS generato oggi da dbt potrà essere consumato domani da qualsiasi tool compatibile con lo standard — prevenendo il vendor lock-in [4][5].

## References

1. [Announcing OpenMetadata 1.12](https://blog.open-metadata.org/announcing-openmetadata-1-12-9e15b66e7748) — blog.open-metadata.org
2. [OpenMetadata Data Contracts API — Import & Export ODCS](https://docs.open-metadata.org/v1.12.x/api-reference/data-contracts/odcs) — docs.open-metadata.org
3. [OpenMetadata Data Contracts Documentation](https://docs.open-metadata.org/v1.12.x/api-reference/data-contracts) — docs.open-metadata.org
4. [ODCS: The Open Data Contract Standard — Foundational](https://www.foundational.io/blog/introduction-data-contracts) — foundational.io
5. [Bitol Announces ODCS v3.1.0](https://bitol.io/bitol-announces-odcs-v3-1-0-stronger-smarter-and-stricter) — bitol.io
6. [ODCS v3.1.0 Specification](https://bitol-io.github.io/open-data-contract-standard/v3.1.0) — bitol-io.github.io
7. [ODCS JSON Schema v3.1.0](https://github.com/bitol-io/open-data-contract-standard/blob/main/schema/odcs-json-schema-v3.1.0.json) — github.com
8. [ODCS Vendors & Tools](https://github.com/bitol-io/open-data-contract-standard/blob/main/vendors.md) — github.com
9. [dbt Model Contracts](https://docs.getdbt.com/docs/mesh/govern/model-contracts) — docs.getdbt.com
10. [Data Contracts Guide — Soda](https://soda.io/blog/guide-to-data-contracts) — soda.io
11. [Open Data Product Specification 3.1](https://opendataproducts.org/v3.1) — opendataproducts.org
12. [ODCS — Entropy Data](https://www.entropy-data.com/learn/open-data-contract-standard) — entropy-data.com
