---
type: source
title: Definizione Metadati
created: 2026-02-20
updated: 2026-04-29
tags: [data-platform, metadata, governance]
related: [metadata-fields-definition, data-domain-governance, kestra, data-observability-definition, federated-computational-governance]
sources: ["DEFINIZIONE METADATI.md"]
---
# Definizione Metadati

A minimal, prescriptive definition of metadata fields required to govern the Data Platform. This source defines a core set of metadata attributes that should be tracked for every dataset or project within the platform.

## Metadata Fields

- **Project Managers (responsabili progetto dp)** — One or more people responsible for the data platform project.
- **Data Stewards (referenti per dati)** — One or more people responsible for specific datasets.
- **Update Frequency (frequenza di aggiornamento)** — Cron pattern (Kestra) for data refresh schedules.
- **Last Update Date (data ultimo aggiornamento)** — Timestamp of the most recent data update.
- **Last Update Status (stato ultima aggiornamento)** — Whether the last data refresh succeeded or failed.
- **Project Development Status (stato sviluppo progetto)** — Lifecycle stage of the project (e.g., development, production, deprecated).
- **Data Accessibility Level (livello accessibilità del dato)** — Classification of data access permissions.

## Context

This source is a brief internal note that prescribes a minimal metadata schema. It does not provide justification, examples, or implementation details. The fields mix technical metadata (update frequency, last update status) with business metadata (project managers, data stewards, accessibility level).

## Connections

- Strengthens [[data-domain-governance]] by adding concrete metadata fields for governance tracking.
- Extends [[data-catalog-critique]] by providing a minimal catalog schema that could be embedded in the platform.
- Related to [[kestra]] as the orchestration tool for scheduling and monitoring data updates.
- The **update frequency** and **last update status** fields enable [[data-observability-definition]] freshness monitoring.
- The **data accessibility level** field supports [[federated-computational-governance]].