---
type: query
title: "Data Product in OpenMetadata: definizione e gestione"
created: 2026-06-29
origin: chat
query: "what is a Data Product in openmetadata and how are they managed?"
tags: [data-products, openmetadata, data-mesh, domains, governance]
---

# Data Product in OpenMetadata: definizione e gestione

Un **Data Product** è un'entità logica che raggruppa uno o più data asset (tabelle, dashboard, pipeline, ecc.) in un'unità consumabile, organizzata per uno scopo di business specifico [[data-products]]. Implementa il principio "data as a product" del [[data-mesh]], dove dataset curati, dashboard e API sono trattati come prodotti con consumatori, SLA e miglioramento continuo [[data-products]].

## Caratteristiche chiave

- **Composizione**: un Data Product aggrega più asset. Es. un prodotto "Customer Churn" può raggruppare dashboard mensili, annuali, per regione [[data-products]].
- **Multi-membership**: un asset può appartenere a più Data Product — a differenza dei [[domains]], dove l'appartenenza è esclusiva [[data-products]].
- **Ownership**: ogni Data Product ha Owner ed Expert assegnati in creazione, secondo il modello [[data-asset-ownership]] [[data-products]].
- **Discoverability**: i Data Product sono visibili e filtrabili sulla [[explore-page]], anche con domain-only view attivo [[data-products]].
- **Governance**: forniscono un modo strutturato per organizzare asset intorno ai domini di business [[data-products]].

## Relazione con i Domains

La gerarchia è **Domain → Data Product → Asset** [[data-products]]. I Data Product sono l'output curato di un dominio. Nella release iniziale (1.2.0) devono essere creati **dentro** un dominio; release future prevedono Data Product indipendenti [[data-products]].

## Come vengono gestiti

Il workflow di creazione è **solo via UI** (supporto API non documentato). Cinque passi [[data-products]] [[how-to-use-data-products-official-documentation----20260514]]:

1. **Name & Display Name**: identificatore univoco + nome user-friendly
2. **Description**: descrizione dettagliata di scopo e contenuti
3. **Owner/Experts**: assegnazione utenti/team per manutenzione e governance
4. **Group Data Assets**: aggiunta asset (tabelle, dashboard, pipeline) dal dominio
5. **View on Explore**: filtro e discovery tramite Explore page

## Data Product Layer (Lineage)

Nella vista di lineage, il **Data Product Layer** è uno dei 5 [[lineage-layers]] ed evidenzia i prodotti curati pronti al consumo (es. "Customer Registry"), collegando la lineage tecnica al valore di business [[data-product-layer]].

## Questioni aperte

La wiki documenta esplicitamente queste lacune [[data-products]]:

- I Data Product possono essere creati/aggiornati via API o solo UI? _(non documentato)_
- Qual è il JSON Schema nel metadata graph? _(non documentato)_
- Un Data Product può coprire più Domini? _(non documentato)_
- Come interagiscono con le policy [[hybrid-rbac-abac-model|RBAC/ABAC]]? _(non documentato)_
- Esiste un catalogo/marketplace dei Data Product? _(non documentato)_

## Fonti consultate

- [[data-products]]
- [[domains]]
- [[data-mesh]]
- [[data-product-layer]]
- [[how-to-use-data-products-official-documentation----20260514]]
- [[domains-data-products-official-documentation---ope-20260514]]
