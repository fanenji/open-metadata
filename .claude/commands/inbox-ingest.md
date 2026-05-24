---
description: Bulk-ingest tutti i file da _inbox/ nella wiki
---

Invoca la skill `wiki-ingest` su tutti i file presenti in `_inbox/` e sue sotto-cartelle (eccetto `_inbox/transcription/` che è gestito da `/transcript`).

Flag riconosciuti in $ARGUMENTS:
- `--dry-run` → mostra il piano senza eseguire
- `--type clippings|docs|media` → filtra per tipo
- `--no-process` → copia in `raw/sources/` ma salta il pipeline LLM

Procedura:
1. `ls _inbox/` e sottocartelle → lista file processabili
2. Per ciascuno: aggiungi alla coda con `python .claude/skills/wiki-ingest/scripts/queue.py add <path>`
3. Loop: `queue.py next` → invoca wiki-ingest → `queue.py mark <id> done` / `failed`
4. Al termine: sposta i file processati con successo da `_inbox/` a `raw/sources/` (oppure cancellali se l'utente preferisce, su conferma esplicita)
5. Report finale: N successi / M fallimenti / dettagli warnings

Default: ingerisce tutto tranne audio/video (`.mp4`, `.mov`, `.mp3`, ...) che richiedono `/transcript` separato.
