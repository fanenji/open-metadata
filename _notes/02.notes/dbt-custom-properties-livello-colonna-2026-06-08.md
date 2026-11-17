---
type: query
title: "dbt custom properties ingestion a livello di colonna in OpenMetadata"
created: 2026-06-08
origin: chat
query: "E' possibile fare ingestion di custom properties dbt in OpenMetadata a LIVELLO DI COLONNA?"
tags: [dbt, custom-properties, ingestion, openmetadata, column-level]
related: [dbt-custom-property-ingestion, dbt-custom-properties-ingestion, custom-properties, dbt-integration]
---

# dbt Custom Properties Ingestion a Livello di Colonna in OpenMetadata

**Risposta: NO, non è possibile.** L'ingestion di custom properties da dbt in OpenMetadata supporta **solo il livello tabella (model)**. Il livello colonna **non è supportato** — verificato empiricamente (giugno 2026).

## Correzione (giugno 2026)

Precedenti versioni della wiki affermavano erroneamente che l'ingestion column-level funzionasse, basandosi su:
- Il supporto nativo del `meta` field di dbt a livello colonna
- Il precedente dei tag (che supportano column-level ingestion)

**La verifica empirica ha dimostrato che NON funziona.** La sintassi qui sotto, precedentemente mostrata come esempio funzionante, **è ignorata da OpenMetadata**:

```yaml
# ❌ NON SUPPORTATO - Ignorato da OpenMetadata
models:
  - name: customers
    columns:
      - name: customer_id
        meta:
          openmetadata:
            customProperties:
              pii_level: "High"
```

## Fonti

1. **[[dbt-custom-property-ingestion]]** — Documenta l'ingestion table-level (unico livello supportato)
2. **[[dbt-column-level-custom-properties]]** — Analisi dettagliata e verifica empirica del non-supporto column-level
3. **Documentazione ufficiale OpenMetadata v1.12.x** — [Ingest Custom Properties from dbt](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-custom-properties): documenta esclusivamente il livello tabella

## Prerequisiti

- Le custom properties **devono essere pre-definite in OpenMetadata** su Settings → Custom Properties → Tables **prima** dell'ingestion
- dbt non può creare nuove definizioni di custom property, solo assegnare valori a quelle già esistenti
- Se una property referenziata in dbt non esiste in OpenMetadata, viene loggato un warning e viene saltata

## Meccanismo (Table-Level Only)

I valori dichiarati in `schema.yml` a livello model vengono incorporati in `manifest.json` sotto `config.meta.openmetadata.customProperties` e il workflow standard di ingestion dbt li legge e li assegna alle **tabelle** corrispondenti in OpenMetadata. I valori a livello colonna vengono ignorati.

## Alternative per Metadati a Livello Colonna

- [[classification-tags]] — Tag di classificazione, pienamente supportati a livello colonna nell'ingestion dbt
- [[glossary-terms]] — Glossary terms assegnabili alle colonne
- Descrizioni colonna — Ingerite regolarmente da dbt
