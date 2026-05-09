---
type: concept
title: API Regression Test Suite
created: 2026-02-13
updated: 2026-02-13
tags: [testing, api, regression, migration, quality-assurance]
related: [migration-strategy-two-phase, fastapi, container-separation-principle]
sources: ["Migrazione API REST Java:Groovy a Python:FastAPI.md"]
---
# API Regression Test Suite

A testing methodology for verifying behavioral equivalence between an original API implementation and its migrated version. This is the critical success factor for technology migrations — without it, migration correctness cannot be verified.

## Golden Set / Baseline Approach

The recommended methodology uses a "golden set" of recorded API responses from the original system:

1. **Record baseline**: For each API endpoint, send requests to the original system and record responses (status code, headers, body)
2. **Define test cases**: Cover happy path, validation errors, error handling, and edge cases
3. **Automate comparison**: Send identical requests to the new system and compare responses

## Comparison Criteria

- **HTTP Status Code**: Must be identical
- **Headers**: Compare relevant headers (Content-Type, Cache-Control, custom headers); ignore environment-specific headers (Server)
- **Response Body**: For JSON responses, compare structure and values using structural comparison libraries (e.g., DeepDiff) that ignore key ordering

## Test Categories

1. **Functional / Happy Path**: Verify core operations with valid inputs
2. **Input Validation**: Send invalid inputs (wrong types, missing fields, out-of-range values) and verify equivalent error responses
3. **Error Handling**: Test scenarios that should generate server errors and verify consistent error status codes and bodies
4. **Performance (Optional)**: Light load testing to ensure the new API is not significantly slower

## Recommended Tools

- **pytest**: Test framework
- **pytest-asyncio**: For testing async FastAPI code
- **requests** or **httpx**: HTTP clients for sending test requests
- **DeepDiff**: JSON structural comparison ignoring key ordering

## CI/CD Integration

The test suite should be integrated into the CI/CD pipeline for the new Python/FastAPI application. Every code change should trigger automatic execution to prevent regressions against the original API behavior.

## Related

- [[migration-strategy-two-phase]] — The migration strategy that requires this test suite
- [[fastapi]] — Target framework being verified
- [[container-separation-principle]] — Enables running both systems side-by-side for comparison