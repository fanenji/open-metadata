---
type: concept
title: dbt Column-Level Custom Properties
created: 2026-06-08
updated: 2026-06-08
tags: [dbt, custom-properties, ingestion, column-level, metadata]
related: [dbt-custom-property-ingestion, dbt-integration, custom-properties, dbt-artifacts, dbt]
sources: [research-ingestion-di-custom-properties-a-livello-di-colonn-2026-06-08.md]
---

# dbt Column-Level Custom Properties — NON Supportato

> **⚠️ VERIFICATO EMPIRICAMENTE (giugno 2026): OpenMetadata NON supporta l'ingestion di custom properties a livello colonna da dbt.**

## Risultato della Verifica

L'ingestion di custom properties da dbt a OpenMetadata funziona **esclusivamente a livello tabella (model)**. Qualsiasi custom property dichiarata sotto `columns → name → meta → openmetadata → customProperties` in `schema.yml` viene **completamente ignorata** durante l'ingestion, senza warning né errori.

## Perché NON Funziona

Il motivo è radicato nel modello dati di OpenMetadata:

1. **Le custom properties in OpenMetadata sono definite per tipo di entità** (Table, Dashboard, Pipeline, ecc.). Non esiste un'entità "Column" indipendente per le custom properties.
2. **Anche se il `meta` field di dbt supporta nativamente dichiarazioni a livello colonna**, e queste vengono serializzate correttamente nel `manifest.json` (`nodes → <model> → columns → <column_name> → meta`), il processo di ingestion di OpenMetadata **legge solo il path `model → config → meta → openmetadata → customProperties`**, ignorando i nodi colonna.
3. **Il precedente dei tag NON si applica**: i tag hanno un meccanismo di ingestion dedicato che attraversa i nodi colonna del manifest, ma le custom properties non hanno un'implementazione analoga.

## Sintassi NON Supportata (Non Usare)

La seguente sintassi in `schema.yml` **NON PRODUCE ALCUN EFFETTO** in OpenMetadata:

```yaml
# ❌ NON SUPPORTATO - Ignorato silenziosamente da OpenMetadata
models:
  - name: customers
    columns:
      - name: customer_id
        meta:
          openmetadata:
            customProperties:
              pii_level: "High"
      - name: email
        meta:
          openmetadata:
            customProperties:
              pii_level: "Medium"
```

## Cosa Fare Invece

Se hai bisogno di metadati custom a livello colonna, le alternative sono:

1. **Tag di classificazione**: usa i [[classification-tags]] a livello colonna, che sono pienamente supportati nell'ingestion dbt (vedi [[dbt-integration]])
2. **Glossary terms**: assegna [[glossary-terms]] alle colonne
3. **Custom properties a livello tabella**: definisci le custom properties sulla Table entity e usale per attributi che si applicano all'intera tabella
4. **Descrizioni**: usa le descrizioni colonna in dbt, che vengono regolarmente ingerite

## Cronologia dell'Analisi

| Data | Fase | Conclusione |
|------|------|-------------|
| 2026-06-08 | Deep research iniziale | La documentazione ufficiale non menziona il livello colonna; la wiki afferma che funziona ma senza conferma ufficiale |
| 2026-06-08 | Verifica empirica | **NON funziona**. Le custom properties a livello colonna vengono ignorate. |

## Relazione con Altri Concetti

- [[dbt-custom-property-ingestion]] — Meccanismo di ingestion (solo table-level)
- [[custom-properties]] — Il sistema di custom properties di OpenMetadata
- [[dbt-integration]] — Panoramica delle 10 categorie di metadati dbt
- [[classification-tags]] — Alternativa per metadati a livello colonna
