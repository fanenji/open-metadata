---
type: query
title: "Ingestione metadati da dbt: tags, glossary, owner, tier"
created: 2026-06-08
origin: chat
query: "procedura per effettuare ingestion di vari tipi di metadati da dbt: tags, glossary, owner, tier. Per ogni tipo di metadato fornisci esempi concreti"
tags: [dbt, ingestion, tags, glossary, owner, tier, metadata]
---

# Ingestion metadati da dbt: tags, glossary, owner, tier

Tutti e quattro i tipi di metadato vengono ingestiti da [[dbt]] tramite il workflow di [[dbt-integration]], che legge gli artifact JSON (principalmente `manifest.json`) generati da `dbt run` / `dbt docs generate`. La configurazione avviene nei file `schema.yml` del progetto dbt, usando il blocco `meta.openmetadata.*` o i meccanismi nativi dbt.

---

## 1. Tags

I tag dbt vengono ingestiti **automaticamente**: se un tag non esiste già in OpenMetadata, viene creato sotto la categoria `DBTTags`. Non ci sono prerequisiti lato OpenMetadata.

### Configurazione in dbt

I tag si definiscono in `schema.yml`:

```yaml
models:
  - name: customers
    config:
      tags: ["model_tag_one", "model_tag_two"]  # table-level
    columns:
      - name: first_order
        description: "Date (UTC) of a customer's first order"
        tags:
          - tags_column_one                       # column-level
```

Dopo `dbt run`, il `manifest.json` conterrà:

```json
// Table-level: node_name -> tags
{
  "model.jaffle_shop.customers": {
    "tags": ["model_tag_one", "model_tag_two"]
  }
}

// Column-level: node_name -> columns -> column_name -> tags
"model.jaffle_shop.customers": {
  "columns": {
    "first_order": {
      "tags": ["tags_column_one"]
    }
  }
}
```

### Flag di configurazione workflow

Nella YAML di ingestion OpenMetadata:

```yaml
includeTags: true                 # default: true
dbtClassificationName: dbtTags   # nome custom classification (default: dbtTags)
```

**Fonti**: [[ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514]], [[dbt-integration]], [[run-dbt-workflow-externally]]

---

## 2. Glossary

L'ingestion dei termini di glossario richiede che i termini **esistano già in OpenMetadata** prima dell'ingestion. Non vengono creati automaticamente.

### Prerequisito: recuperare il FQN

Il FQN (Fully Qualified Name) si trova nell'URL della pagina del termine in OpenMetadata:
`https://localhost:8585/glossary/Test_Glossary.term_two.nested_term.more_nested_term`

Formato: `Glossary_Name.term_name` (o `Glossary_Name.parent.child` per termini annidati). Vedi [[glossary-term-fqn]].

### Configurazione in dbt (`schema.yml`)

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        glossary: [
          'Test_Glossary.term_one',
          'Test_Glossary.term_two.nested_term.more_nested_term',
        ]
    columns:
      - name: customer_id
        meta:
          openmetadata:
            glossary: [
              'Test_Glossary.term_two.nested_term'
            ]
```

Dopo `dbt run`, il `manifest.json` includerà:

```json
// Table-level: node_name -> meta -> openmetadata -> glossary
"model.jaffle_shop.customers": {
  "config": {
    "meta": {
      "openmetadata": {
        "glossary": [
          "Test_Glossary.term_one",
          "Test_Glossary.term_two.nested_term.more_nested_term"
        ]
      }
    }
  }
}

// Column-level: node_name -> columns -> column_name -> meta -> openmetadata -> glossary
"columns": {
  "customer_id": {
    "meta": {
      "openmetadata": {
        "glossary": [
          "Test_Glossary.term_two.nested_term"
        ]
      }
    }
  }
}
```

**Fonti**: [[dbt-glossary-ingestion]], [[dbt-meta-configuration]], [[glossary-term-fqn]]

---

## 3. Owner

L'owner può essere un **utente** o un **team**. Entrambi devono esistere in OpenMetadata prima dell'ingestion. OpenMetadata cerca prima un utente con quel nome; se non lo trova, cerca un team.

### Due modalità di configurazione

**A) Singolo owner (via `manifest.json` o `catalog.json`):**

```json
// manifest.json: node_name -> metadata -> owner
"model.jaffle_shop.orders": {
  "metadata": {
    "owner": "openmetadata_team"
  }
}
```

**B) Multi-owner (via `schema.yml` con `meta.openmetadata.owner`):**

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        owner: ['John Doe', 'jane@gmail.com']
```

### Flag di configurazione workflow

```yaml
dbtUpdateOwners: true   # true = sovrascrive owner esistenti
                         # false = assegna solo a tabelle senza owner
```

### Linee guida per nomi owner

- Se il nome in `manifest.json` è `openmetadata`, l'utente deve avere email `openmetadata@youremail.com` o il team deve chiamarsi `openmetadata`.
- I nomi devono corrispondere esattamente a nomi utente/email o nomi team in OpenMetadata.

**Fonti**: [[ingest-owner-from-dbt-official-documentation---ope-20260514]], [[dbt-integration]], [[run-dbt-workflow-externally]]

---

## 4. Tier

I tier devono **esistere già in OpenMetadata** prima dell'ingestion. Si applicano solo a livello tabella (non colonna).

### Configurazione in dbt (`schema.yml`)

```yaml
models:
  - name: customers
    meta:
      openmetadata:
        tier: 'Tier.Tier2'
```

Il FQN del tier segue il formato `Tier.NomeTier` (es. `Tier.Tier1`, `Tier.Tier2`, … `Tier.Tier5`).

Dopo `dbt run`, il `manifest.json` includerà:

```json
// node_name -> config -> meta -> openmetadata -> tier
"model.jaffle_shop.customers": {
  "config": {
    "meta": {
      "openmetadata": {
        "tier": "Tier.Tier2"
      }
    }
  }
}
```

### Prerequisito: creare i tier in OpenMetadata

I tier vanno creati nella sezione **Govern → Classification → Tiers** di OpenMetadata prima di eseguire l'ingestion. Il workflow dbt non crea tier automaticamente.

**Fonti**: [[ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514]], [[dbt-integration]], [[tiers]]

---

## Tabella riassuntiva

| Metadato    | Meccanismo in dbt (`schema.yml`)                       | Auto-creato in OM? | Prerequisito OM                | Livello supportato |
|-------------|-------------------------------------------------------|---------------------|--------------------------------|---------------------|
| **Tags**    | `config.tags` / `columns[].tags` (nativo dbt)         | ✅ Sì (`DBTTags`)   | Nessuno                        | Table + Column      |
| **Glossary**| `meta.openmetadata.glossary: [FQN, ...]`              | ❌ No               | Termini devono esistere        | Table + Column      |
| **Owner**   | `meta.openmetadata.owner: [...]` o `metadata.owner`   | ❌ No               | User/Team devono esistere      | Table               |
| **Tier**    | `meta.openmetadata.tier: 'Tier.Nome'`                 | ❌ No               | Tier devono esistere           | Solo Table          |

## Flusso operativo completo

1. **Preparazione prerequisiti in OpenMetadata**: creare utenti/team (per owner), termini glossario, tier.
2. **Configurare `schema.yml`** nel progetto dbt con i blocchi `meta.openmetadata.*` e `tags:` nativi.
3. **Eseguire il workflow dbt**: `dbt run && dbt docs generate` (più `dbt test` opzionale).
4. **Eseguire l'ingestion OpenMetadata**: via UI (Add Ingestion → dbt) o CLI esterna (`metadata ingest -c config.yaml`). Vedi [[run-dbt-workflow-externally]].
5. **Verificare i risultati** nell'interfaccia OpenMetadata sui nodi tabelle/colonne.

**Fonti consultate**:
- `wiki/entities/dbt.md`
- `wiki/concepts/dbt-integration.md`
- `wiki/concepts/dbt-glossary-ingestion.md`
- `wiki/concepts/dbt-meta-configuration.md`
- `wiki/concepts/glossary-term-fqn.md`
- `wiki/concepts/run-dbt-workflow-externally.md`
- `wiki/sources/ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514.md`
- `wiki/sources/ingest-owner-from-dbt-official-documentation---ope-20260514.md`
- `wiki/sources/ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514.md`
- `raw/sources/ingest-tags-from-dbt-openmetadata-metadata-tagging-20260514.md`
- `raw/sources/ingest-owner-from-dbt-official-documentation---ope-20260514.md`
- `raw/sources/ingest-tiers-from-dbt-openmetadata-data-tiering-gu-20260514.md`
- `raw/sources/ingest-glossary-from-dbt-official-documentation----20260514.md`
