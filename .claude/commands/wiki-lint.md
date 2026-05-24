---
description: Audit the wiki for broken links, orphans, frontmatter issues, and semantic problems
---

Invoca la skill `wiki-lint` per fare un audit di salute della wiki.

Opzioni passate dall'utente: $ARGUMENTS

Flag riconosciuti:
- `--fix` → applica fix automatici dove sicuro (stub pages, frontmatter)
- `--report-only` → stampa il report ma non scrive `wiki/lint-report.md`
- `--no-semantic` → salta il check semantico LLM (solo deterministici)
- `--no-qmd` → salta il check missing-page via QMD

Segui la procedura completa di `.claude/skills/wiki-lint/SKILL.md`: Step 1 deterministici via `lint.py`, Step 2 semantico via LLM, Step 3 report unificato. Aggiorna `wiki/log.md` al termine.
