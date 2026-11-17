---
type: query
title: "Research: Ingestion di Custom Properties a Livello di Colonna da DBT a OpenMetadata"
created: 2026-06-08
updated: 2026-06-08
origin: deep-research
tags: [research]
sources: []
related: []
---

# Research: Ingestion di Custom Properties a Livello di Colonna da DBT a OpenMetadata

# Ingestion di Custom Properties a Livello di Colonna da DBT a OpenMetadata

## Risposta Sintetica

L'ingestion di custom properties da dbt a OpenMetadata è ufficialmente supportata **solo a livello tabella** (model). **Il supporto a livello colonna NON esiste** — verificato empiricamente (giugno 2026). La documentazione ufficiale è corretta nel documentare solo il livello tabella. Le precedenti affermazioni della wiki che indicavano il contrario erano errate e basate su un'estrapolazione non verificata del comportamento del `meta` field di dbt.

## Evidenza dalle Fonti

### Documentazione Ufficiale OpenMetadata v1.12.x

La guida [Ingest Custom Properties from dbt](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties) [2] documenta esplicitamente solo l'ingestion a livello tabella:

> "To set custom property values for a **table** in your dbt model, add them under `model->name->meta->openmetadata->customProperties`"

Tutti gli esempi ufficiali (Complete Example, Advanced Examples) mostrano `customProperties` sotto `meta.openmetadata` al livello del model, mai al livello della colonna. L'esempio "Complete Example" include una sezione `columns:` ma senza `meta.openmetadata.customProperties` al suo interno.

Il path in `manifest.json` è documentato come: `node_name->config->meta->openmetadata->customProperties` [2].

**Requisiti ufficiali** [2]:
1. Le custom properties devono essere **pre-definite** in OpenMetadata su Settings → Custom Properties → Tables
2. Se una property referenziata in dbt non esiste, viene loggato un warning e saltata
3. 15 tipi supportati: `string`, `integer`, `number`, `markdown`, `sqlQuery`, `email`, `date-cp`, `dateTime-cp`, `time-cp`, `timestamp`, `duration`, `enum`, `entityReference`, `entityReferenceList`, `timeInterval`, `table-cp`

### Wiki Esistente (cross-reference) — CORRETTA

La wiki conteneva precedentemente affermazioni errate sul supporto column-level. Il concept [[dbt-custom-property-ingestion]] affermava:

> "This works at both the model (table) level and the column level."

E forniva un esempio column-level. **Queste pagine sono state corrette (giugno 2026)** per riflettere che solo il table-level è supportato. La query [[dbt-custom-properties-livello-colonna-2026-06-08]] è stata aggiornata con la risposta corretta: NO, non è possibile.

### GitHub Issue #22747

L'[issue #22747](https://github.com/open-metadata/OpenMetadata/issues/22747) [1] è la feature request originale per l'ingestion di custom properties da dbt. Descrive il problema:

> "Currently, dbt metadata ingestion into OpenMetadata doesn't support custom properties from dbt model meta fields."

L'issue richiedeva l'estrazione da `meta.openmetadata.customProperties` e `meta.openmetadata.domain`. La feature è stata poi implementata (come dimostra la documentazione v1.12.x). L'issue originale menziona solo il livello tabella.

### DBT Tag Ingestion (confronto) — NON applicabile

La guida [Ingest Tags from dbt](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tags) [5] documenta **esplicitamente** sia table-level che column-level tags. Questo aveva portato a ipotizzare che lo stesso meccanismo si applicasse alle custom properties.

**Tuttavia, la verifica empirica ha dimostrato che NON è così.** I tag hanno un'implementazione dedicata che attraversa i nodi colonna del `manifest.json`, mentre le custom properties no. Il processore di custom properties legge esclusivamente `model → config → meta → openmetadata → customProperties`.

### DBT `meta` Field

Il [meta field di dbt](https://docs.getdbt.com/reference/resource-configs/meta) [2] è supportato a tutti i livelli: model, column, source, snapshot, seed, test. La struttura è gerarchica: qualsiasi cosa sotto `meta` a livello colonna viene serializzata nel `manifest.json` all'interno del nodo colonna.

## Meccanismo di Ingestion

1. **Definizione in schema.yml**: valori dichiarati sotto `meta → openmetadata → customProperties`
2. **Generazione artifacts**: `dbt run` / `dbt compile` / `dbt docs generate` producono `manifest.json`
3. **Serializzazione**: i valori finiscono in `manifest.json` sotto `nodes → <model_name> → config → meta → openmetadata → customProperties`
4. **Ingestion**: il workflow dbt di OpenMetadata (auto-ingest o recipe YAML) legge il `manifest.json` e assegna i valori
5. **Validazione**: ogni valore è validato contro il tipo definito in OpenMetadata; fallimenti generano warning senza bloccare la pipeline [2]

### Validazione e Graceful Degradation [2]

| Scenario | Comportamento |
|---|---|
| Custom property non definita su Table entity | Warning, property saltata |
| Valore invalido per il tipo | Warning con dettagli, property saltata |
| Enum value invalido (single-select) | Warning, property saltata |
| Enum value invalido (multi-select) | Valori invalidi filtrati, validi applicati con warning |
| Campi richiesti mancanti per tipi complessi | Warning, property saltata |

## Analisi Critica: Livello Colonna — RISOLTA

### Perché NON funziona

1. **Modello dati OpenMetadata**: le custom properties sono definite per tipo di entità (Table, Dashboard, Pipeline, ecc.). Non esiste un'entità "Column" separata. Le colonne in OpenMetadata non hanno una sezione "Custom Properties".
2. **Implementazione ingestion**: il processore di custom properties legge solo `model → config → meta → openmetadata → customProperties` dal `manifest.json`. Non esiste codice che attraversa i nodi `columns`.
3. **Documentazione ufficiale**: menziona solo "table" e solo `model->name->meta->openmetadata->customProperties`. Nessun riferimento a colonne. **La documentazione è corretta.**

### Perché si pensava funzionasse (ipotesi smentite)

1. ~~**DBT `meta` field**: supporta nativamente `meta` a livello colonna.~~ — Vero, ma irrilevante: OpenMetadata non lo legge.
2. ~~**Pattern Tag**: OpenMetadata processa tags a livello colonna.~~ — Vero per i tag, ma l'implementazione delle custom properties è diversa.
3. ~~**Wiki assertion**: esempi column-level funzionanti.~~ — Erano estrapolazioni non verificate.

## Risultato della Verifica Empirica (giugno 2026)

**L'ingestion di custom properties a livello colonna NON funziona.** Test end-to-end eseguito:
1. Custom property `pii_level` (tipo `enum`) definita sulla Table entity in OpenMetadata
2. Valore column-level dichiarato in `schema.yml` sotto `columns → name → meta → openmetadata → customProperties`
3. Ingestion eseguita con successo (nessun errore)
4. **Risultato: la custom property NON appare sulla colonna in OpenMetadata.** Il valore viene silenziosamente ignorato.

Il motivo è che OpenMetadata legge solo il path `model → config → meta → openmetadata → customProperties` dal `manifest.json` e non attraversa i nodi `columns`.

## Relazione con Altri Concetti

- [[custom-properties]] — Meccanismo generale per estendere i modelli dati con campi aggiuntivi
- [[dbt-integration]] — Panoramica dell'integrazione dbt-OpenMetadata (10 categorie di metadati)
- [[dbt-artifacts]] — `manifest.json`, `catalog.json`, `run_results.json`
- [[dbt-lineage-ingestion]] — Estrazione della lineage dalle dipendenze `ref()` e `source()`
- [[custom-property-naming-conventions]] — Convenzioni di naming
- [[dbt]] — Data Build Tool
- [[schema-first-approach]] — Approccio architetturale di OpenMetadata

## Domande Chiuse

1. **Column-level support verificato**: ~~La documentazione ufficiale non menziona il livello colonna. Test empirico necessario.~~ **VERIFICATO: NON funziona.** Vedi sopra.

## Domande Aperte

1. **Conflict resolution**: Cosa succede se un valore dbt confligge con un valore già impostato manualmente nella UI? La guida "Ingest Descriptions" [6] documenta un toggle `Update Descriptions` che controlla se sovrascrivere o preservare le descrizioni esistenti. Non è chiaro se esista un meccanismo analogo per le custom properties.

## Fonti

1. [Custom Properties ingestion via dbt agent support · Issue #22747](https://github.com/open-metadata/OpenMetadata/issues/22747) — GitHub, feature request originale
2. [Ingest Custom Properties from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties) — Documentazione ufficiale
3. [dbt Workflow — OpenMetadata v1.11.x](https://docs.open-metadata.org/v1.11.x/connectors/database/dbt) — Panoramica integrazione dbt
4. [OpenMetadata + dbt: All Your Data Assets in One Place](https://atlan.com/openmetadata-dbt) — Articolo Atlan (terze parti)
5. [Ingest Tags from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tags) — Documenta esplicitamente column-level tags
6. [Ingest Descriptions from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-descriptions) — Documenta toggle Update Descriptions per conflict resolution

## References

1. [Custom Properties ingestion via dbt agent support · Issue #22747](https://github.com/open-metadata/OpenMetadata/issues/22747) — github.com
2. [Ingest Custom Properties from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties) — docs.open-metadata.org
3. [dbt Workflow — OpenMetadata v1.11.x](https://docs.open-metadata.org/v1.11.x/connectors/database/dbt) — docs.open-metadata.org
4. [OpenMetadata + dbt: All Your Data Assets in One Place](https://atlan.com/openmetadata-dbt) — atlan.com
5. [Ingest Tags from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-tags) — docs.open-metadata.org
6. [Ingest Descriptions from dbt — OpenMetadata v1.12.x](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-descriptions) — docs.open-metadata.org
7. [Lineage — OpenMetadata Standards](https://openmetadatastandards.org/lineage/lineage) — openmetadatastandards.org
8. [Auto Ingest dbt-core — OpenMetadata v1.11.x](https://docs.open-metadata.org/v1.11.x/connectors/database/dbt/auto-ingest-dbt-core) — docs.open-metadata.org
