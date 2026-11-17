---
type: query
title: "Ingestione Domains da dbt a OpenMetadata"
created: 2026-06-17
origin: chat
query: "come effettuare ingestion di Domains da dbt a openmetadata"
tags: [dbt, domains, ingestion, metadata]
---

# Ingestione Domains da dbt a OpenMetadata

I [[domains|Domains]] vengono ingestiti da [[dbt]] a [[OpenMetadata]] tramite il workflow di [[dbt-integration]], leggendo il `manifest.json`. L'assegnazione è **a livello tabella** (non colonna). Il dominio deve **esistere già in OpenMetadata** prima dell'ingestion — non viene creato automaticamente [[dbt-integration]].

## Configurazione in `schema.yml`

Si usa il blocco `meta.openmetadata.domain`:

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        domain: "Sales"
    description: "..."
    columns:
      - name: customer_id
        description: "..."
        tests:
          - unique
          - not_null
```

Il valore (`"Sales"`) deve corrispondere al **nome esatto** del dominio già creato in OpenMetadata.

## Cosa succede nel `manifest.json`

Dopo `dbt run`, il manifest conterrà:

```json
"model.jaffle_shop.customers": {
  "config": {
    "meta": {
      "openmetadata": {
        "domain": "Sales"
      }
    }
  }
}
```

La chiave è `node_name → config → meta → openmetadata → domain`.

## Prerequisiti

1. **Creare il dominio in OpenMetadata** — UI: Govern → Domains. I tre tipi sono Source-aligned, Aggregate, Consumer-aligned [[domains]].
2. **Configurare `schema.yml`** con `meta.openmetadata.domain`.
3. **Eseguire `dbt run`** per generare/aggiornare `manifest.json`.
4. **Eseguire l'ingestion OpenMetadata** — via UI (Add Ingestion → dbt) o CLI esterna (`metadata ingest -c config.yaml`). Vedi [[run-dbt-workflow-externally]].

## Comportamento in caso di errori

| Scenario | Comportamento |
|---|---|
| Dominio non trovato in OM | Warning, ingestion continua senza assegnare |
| Valore vuoto | Assegnazione saltata |
| Formato nome invalido | Warning, assegnazione saltata |

## Riepilogo

| Metadato | Meccanismo dbt | Auto-creato in OM? | Prerequisito OM | Livello |
|---|---|---|---|---|
| **Domain** | `meta.openmetadata.domain: "NomeDominio"` | No | Dominio deve esistere | Solo Table |

Il pattern è analogo a tier e glossary: si configura in `schema.yml` sotto `meta.openmetadata.*`, il dominio deve pre-esistere in OM, e l'ingestion legge il valore dal `manifest.json`.

## Fonti consultate

- `wiki/concepts/dbt-integration.md`
- `wiki/concepts/dbt-artifacts.md`
- `wiki/concepts/domains.md`
- `wiki/queries/ingestione-metadati-dbt-tags-glossary-owner-tier-2026-06-08.md`
- Documentazione ufficiale: https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/ingest-dbt-domain
