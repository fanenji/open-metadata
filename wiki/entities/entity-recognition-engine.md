---
type: entity
title: Entity Recognition Engine
created: 2026-05-14
updated: 2026-05-14
tags: [nlp, spacy, auto-classification, pii, entity-recognition]
related: [auto-pii-tagging, column-name-scanner, sample-data-storage-toggle, ssl-certificate-troubleshooting, auto-classification]
sources: ["auto-pii-tagging-guide-official-documentation---op-20260514.md"]
---
# Entity Recognition Engine

The Entity Recognition Engine is the NLP-based component of the [[auto-pii-tagging]] workflow that scans sample data rows to identify sensitive information. It operates alongside the [[column-name-scanner]] as one of two detection methods for automatic PII classification.

## Model Dependency

The engine relies on the **spaCy `en_core_web_md`** model (version 3.5.0), a medium-sized English language model trained for named entity recognition tasks. This model is downloaded at runtime from the explosion/spaCy-models GitHub repository.

## Activation Condition

Entity recognition is **only active when sample data ingestion is enabled** in the Auto Classification Agent configuration (see [[sample-data-storage-toggle]]). If sample data storage is disabled, the workflow falls back to the Column Name Scanner alone for PII detection.

## Supported Entities

The engine detects a list of supported sensitive entity types within sample data rows. The full enumerated list of supported entities is not documented in the official guide, but the engine is designed to identify common PII categories such as personal names, addresses, and other sensitive identifiers.

## Confidence Threshold

The engine's tagging decisions are governed by the `confidence` parameter, which sets the minimum score required to classify a column as `PII.Sensitive`. This allows operators to balance precision and recall based on organizational risk tolerance.

## Known Issues

### SSL Certificate Verification Failure
On some corporate Windows laptops, the engine's model download fails with a `CERTIFICATE_VERIFY_FAILED` error when attempting to fetch the spaCy model compatibility manifest from `raw.githubusercontent.com`. The documented workaround is to manually install the model using `pip` with the `--trusted-host` flag. See [[ssl-certificate-troubleshooting]] for full details.

### Enterprise vs. Open-Source
The General Classification capability (tags like `Address`, `Name`) that would leverage this engine more broadly is not available in open-source OpenMetadata. It is expected from version 1.7.1.