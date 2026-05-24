---
description: Transcribe audio/video files from _inbox/transcription/ using mlx_whisper
---

Invoca la skill `transcript` per trascrivere file audio/video.

Argomenti dall'utente: $ARGUMENTS

Pattern:
- Se $ARGUMENTS è vuoto → trascrivi tutti i file supportati in `_inbox/transcription/`
- Se $ARGUMENTS contiene un filename → resolvi relativo a `_inbox/transcription/` e trascrivi solo quello
- Flag riconosciuti: `--lang it|en|...`, `--summary`, `--force`

Segui la procedura completa di `.claude/skills/transcript/SKILL.md`: Step 1 trascrizione via `scripts/transcript.py`, Step 2 (se `--summary`) generazione summary strutturato via LLM, Step 3 report finale.
