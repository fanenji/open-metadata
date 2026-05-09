---
type: concept
title: Unified LLM Service
created: 2026-04-08
updated: 2026-04-08
tags: [llm, architecture, orchestration, openmetadata]
related: [local-llm-openmetadata-extension, ollama, openmetadata, privacy-by-design]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Unified LLM Service

An orchestration layer that abstracts across multiple LLM providers (OpenAI, [[ollama]], and custom OpenAI-compatible endpoints) to provide a unified interface for all LLM operations. Implemented in the [[local-llm-openmetadata-extension]] as `UnifiedLLMService.ts`.

## Purpose

The Unified LLM Service enables provider switching without code changes. It handles:
- Provider selection and initialization
- API communication format normalization
- Response parsing across different provider formats
- Fallback mechanisms for legacy formats

## Provider Support

| Provider | Service File | Characteristics |
|----------|-------------|-----------------|
| OpenAI | `OpenAIService.ts` | Cloud-based, fast, pay-per-use |
| Ollama | `LocalLLMService.ts` | Local, free, offline-capable |
| Custom | `LocalLLMService.ts` | Any OpenAI-compatible endpoint |

## Relevance to Wiki

This pattern enables [[privacy-by-design]] data discovery by allowing teams to use local LLMs for sensitive metadata exploration while maintaining the ability to switch to cloud providers when privacy is not a concern. It demonstrates a flexible architecture for [[data-discovery-tools]] that adapts to different security and performance requirements.