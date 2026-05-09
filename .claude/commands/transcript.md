---
description: Transcribe audio/video files from _inbox/transcription/ using mlx_whisper
---

Transcribe audio/video files in `_inbox/transcription/` using the `transcript.py` script. Each `.txt` output is saved alongside its source file with a `_TRANSCRIPTS` suffix.

**Input:** `$ARGUMENTS` contains an optional filename and flags:

```
/transcript [<filename>] [--lang it|en] [--summary]
```

- If `<filename>` is provided, transcribe only that file.
- If no filename is given, transcribe **all** audio/video files in `_inbox/transcription/`.
- `--lang`: language code for whisper (auto-detect if not set).
- `--summary`: after transcription, generate a structured summary saved as `_SUMMARY` alongside the transcript.

---

## Step 1 — Verify prerequisites

Check that the source directory and script exist:

```bash
ls "_inbox/transcription/"
python3 -c "import mlx_whisper" 2>/dev/null && echo "mlx ok"
command -v ffmpeg && echo "ffmpeg ok"
```

If `mlx_whisper` or `ffmpeg` is missing, print install instructions and stop:
- `pip install mlx-whisper`
- `brew install ffmpeg`

---

## Step 2 — Collect files

If a filename is given, use only that file (resolve relative to `_inbox/transcription/`).

If no filename, list all supported files:

**Supported extensions:** `.mp4`, `.mov`, `.mkv`, `.webm`, `.avi` (video) and `.mp3`, `.m4a`, `.wav`, `.ogg`, `.aac`, `.flac` (audio).

Skip files that already have a matching `_TRANSCRIPTS.txt`.

Print a manifest table:

```
FILE                          STATUS
meeting-recording.m4a         → transcribing
already-done.wav              → skip (existing _TRANSCRIPTS.txt)
```

If all files are already transcribed or no supported files found, print a summary and stop.

---

## Step 3 — Transcribe

For each file, run:

```bash
python3 _system/scripts/transcript.py "_inbox/transcription/<filename>" [--lang <lang>]
```

Run files **sequentially** (one at a time) to avoid GPU contention with mlx_whisper.

After each transcription, print: `✓ <filename> → <output.txt>`

---

## Step 3.5 — Generate summary (if `--summary` is set)

If `--summary` was passed, after each successful transcription generate a summary of the transcript.

**Detect content type:** If the filename contains "meeting" (case-insensitive) or the transcript content refers to attendees, decisions, action items, or a structured discussion, treat it as a **meeting**. Otherwise treat it as **general content**.

**Meeting structure** (language matches `--lang`, default Italian):

```markdown
## Riepilogo
3-5 sentence summary of what was discussed

## Punti chiave
- 5-8 most important topics covered

## Decisioni prese
- Explicit decisions made during the meeting (if none, state "Nessuna decisione esplicita presa.")

## Azioni da svolgere
- [ ] Azione — *Assignee* (if no assignee, omit)

## Temi aperti
- Unresolved questions or topics deferred
```

**General content structure** (always in English):

```markdown
## Abstract
3-5 sentence summary of what the video covers

## Key points
- 5-8 most important takeaways

## Entities
- Technologies, concepts, tools, people mentioned

## Notable quotes
- "Verbatim quote" (approx. timestamp if inferable)
```

Save the summary to `_inbox/transcription/<filename>_SUMMARY.txt` (same name as the input file, with `_SUMMARY` suffix).

After generating, print: `✓ Summary: <filename> → <summary.txt>`

---

## Step 4 — Report

Print final summary:

```
transcript complete — YYYY-MM-DD

  Transcribed : N
  Skipped     : N (already had _TRANSCRIPTS.txt)
  Errors      : N
```
