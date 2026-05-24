---
description: Ingest a document into the wiki (PDF/DOCX/PPTX/XLSX/HTML/MD) with 2-step pipeline
---

Invoca la skill `wiki-ingest` per ingerire uno o più file nella wiki.

Argomenti dall'utente: $ARGUMENTS

Pattern:
- `$ARGUMENTS` può contenere uno o più path a file da ingerire.
- Se vuoto, chiedi all'utente quale file processare oppure offri di processare la coda corrente (`queue.py list --status pending`).
- Se è una directory, processa tutti i file supportati al suo interno (uno per volta).

Segui la procedura completa di `.claude/skills/wiki-ingest/SKILL.md`: cache check → preprocessing → step-1 analisi → step-2 generation → finalize → page merge LLM se necessario → report.
