---
type: query
title: "Best Practices for Glossary Definition"
created: 2026-06-17
origin: chat
query: "best practices for glossary definition"
tags: [glossary, best-practices, data-governance]
---

# Best Practices for Glossary Definition

La wiki documenta otto pratiche per la gestione dei glossari in OpenMetadata, definite nella guida ufficiale v1.12.x [[glossary-best-practices]].

## Pratiche principali

**1. Usare relazioni gerarchiche (max 3 livelli)**
Strutturare i termini in parent-child invece di una lista piatta. Una gerarchia dà contesto per classification e policy enforcement. Esempio: `Contact Info → Phone Number → User Phone Number` distingue dati PII da dati non sensibili [[glossary-hierarchy]].

**2. Associare classification tag ai glossary term**
Attaccare [[classification-tags]] (es. `PII.Sensitive`) ai termini. Quando il termine viene applicato a un data asset, i tag vengono auto-assegnati — governance scalabile in un passo solo [[glossary-best-practices]].

**3. Usare i Tier (Tier 1–5)**
I [[tiers]] definiscono l'importanza dei dati. Focus su Tier 1 per massimo impatto, identificare Tier 5 per decluttering.

**4. Semplificare le policy con i tag**
Raggruppare asset con tag (`sensitive`, `restrictive`, `public`, `internal`) e creare una policy unica a livello tag invece di policy per-risorsa. Vedi [[tag-based-policy-design]].

**5. Usare Display Name per migliorare i nomi**
Quando i termini sono ereditati da sistemi sorgente, rinominarli con nomi user-friendly: `dep-prod` → `Product Department`, `c_id` → `Customer ID` [[glossary-best-practices]].

**6. Import/Export per modifiche bulk**
Esportare il glossario in CSV, editare descrizioni/ownership/reviewer/status, reimportare. Utile per aggiornamenti massivi [[glossary-best-practices]].

**7. Rinominare, non cancellare**
Cancellare un termine rimuove tutto il tagging sugli asset. Rinominare per correggere typo o aggiornare nomi — operazione nativa in OpenMetadata [[glossary-best-practices]].

**8. Raggruppare concetti simili**
Creare relazioni semantiche tra termini correlati per aiutare gli utenti a capire i dati attraverso i concetti.

## Modello Thesauri

OpenMetadata modella il glossario come **Thesauri** (non semplice lista flat), con tre tipi di relazioni: gerarchica (parent-child), equivalente (sinonimi), associativa (concetti collegati) [[glossary-overview]].

## Setup e Ciclo di Vita

Alla creazione, il glossario richiede: **Name*** (obbligatorio), **Description*** (obbligatorio), più Display Name, Tags, flag Mutually Exclusive, Owner e Reviewers opzionali [[glossary-setup]]. I termini hanno un lifecycle con stati **Draft** e **Approved**, governati dai Reviewer [[glossary-term-lifecycle]].

L'FQN segue il formato `Glossary_Name.term_name` (o dot-notation per termini annidati) ed è usato come ponte tra modelli dbt e glossario OpenMetadata [[glossary-term-fqn]].

## Principi chiave

- **Scalabilità:** Combinare significato semantico (glossary term) + definizione del tipo dato (classification tag)
- **Preservazione:** Rinominare > cancellare
- **Policy:** Tag-level policies per ridurre overhead amministrativo
- **Ricercabilità:** Display name ottimizzati per i pattern di ricerca utente

## Fonti consultate

- `wiki/concepts/glossary-best-practices.md`
- `wiki/concepts/glossary-hierarchy.md`
- `wiki/concepts/glossary-overview.md`
- `wiki/concepts/glossary-setup.md`
- `wiki/concepts/glossary-term-lifecycle.md`
- `wiki/concepts/glossary-term-fqn.md`
- `wiki/sources/best-practices-for-glossary-official-documentation-20260514.md`
