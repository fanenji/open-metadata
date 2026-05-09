---
type: concept
title: Privacy-by-Design
created: 2026-04-08
updated: 2026-04-08
tags: [privacy, data-governance, security, llm]
related: [ollama, local-llm-openmetadata-extension, data-masking-techniques, data-pseudonymization]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Privacy-by-Design

A design principle ensuring that data processing systems are built with privacy as a core requirement from the ground up. In the context of the [[local-llm-openmetadata-extension]], this means the extension operates entirely locally unless explicitly configured to use a remote API endpoint.

## Implementation in the Extension

- **Local LLM Support**: Using [[ollama]], all metadata queries and LLM processing happen on the user's machine.
- **No Data Leakage**: No metadata or query data is sent to external servers unless the user explicitly configures a remote provider.
- **User Control**: The user chooses which LLM provider to use, with full awareness of the privacy implications.

## Relevance to Wiki

Privacy-by-Design aligns with the wiki's coverage of [[data-masking-techniques]] and [[data-pseudonymization]] for sensitive data handling. It provides an architectural approach to privacy that complements technical de-identification methods, particularly relevant for organizations exploring [[openmetadata]] with sensitive metadata.