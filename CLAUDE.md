# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

An **Obsidian vault**, not a software project — there is no build, test, lint, or typecheck step. The vault documents the Data Platform's architecture, technologies, decisions, and research, and is maintained collaboratively by a human curator and an LLM. It extends the open-source pattern at https://github.com/nashsu/llm_wiki.

## Read these first

Before performing any wiki operation, read these in order — they are the source of truth and override any general assumptions:

1. **`AGENTS.md`** — directory invariants, slash command catalog, content conventions, contradiction workflow, fallback paths.
2. **`schema.md`** — page types, naming conventions, frontmatter requirements, index/log format, cross-referencing rules.
3. **`README.md`** — slash command flags and options.
4. **`purpose.md`** — project goals and key questions driving the wiki.

Do not duplicate or paraphrase the rules from those files into other notes; link to them.

## Three-layer architecture

The vault enforces a strict separation that future Claude instances must respect:

- **`raw/`** — original ingested source files. **Immutable. Read-only.** Never edit, rename, or delete.
- **`wiki/`** — LLM-generated Markdown (entities, concepts, sources, queries, comparisons, synthesis). The active workspace. The LLM owns this layer; the human reads and curates direction.
- **`AGENTS.md` / `schema.md`** — Schema layer: conventions, structure, workflow. Co-evolved by human and LLM.

Supporting directories:
- `_inbox/` — staging for files awaiting ingest. Files are deleted from here after being copied into `raw/`.
- `_notes/` — write target for `/graph-analyze` reports and ad-hoc analysis output.
- `_system/templates/` — Obsidian note templates. Reference only; do not move.
- `_system/scripts/` — Python scripts backing slash commands. Run from the vault root (e.g. `python3 _system/scripts/graph-analyze.py`).
- `.llm-wiki/` — internal tooling state (LanceDB, ingest queues, conversation history). Managed automatically; do not edit.

## Slash commands

Defined in `.claude/commands/` (Claude) and `.opencode/commands/` (OpenCode), backed by Python scripts in `_system/scripts/`.

| Command | Purpose |
|---------|---------|
| `/wiki-lint [--fix] [--report-only] [--section <name>]` | Seven-check health audit; writes `wiki/lint-report.md` |
| `/graph-analyze [--console-only]` | Directed-graph analysis of the wikilink structure; writes `_notes/graph-analysis-YYYY-MM-DD.md` |
| `/transcript [<file>] [--lang it\|en] [--summary]` | Transcribe `_inbox/transcription/` audio/video via mlx_whisper |
| `/inbox-ingest`, `/meeting-ingest <file>`, `/url-ingest <URL>`, `/yt-ingest <URL>` | Ingest pipelines (OpenCode-only — see `.opencode/commands/`) |

See `README.md` and `AGENTS.md` for full flag semantics.

## Content conventions (cheat sheet)

- File names: `kebab-case.md`. Sources: `author-year-slug.md`. Queries: question as slug.
- Required frontmatter: `type`, `title`, `tags`, `created`, `updated` (sources also need `authors`, `year`, `url`, `venue`).
- A page's `type` must match its subdirectory under `wiki/` (`wiki/entities/` → `type: entity`, etc.).
- Cross-link with `[[page-slug]]`. Every entity and concept must appear in `wiki/index.md`.
- Activity is appended to `wiki/log.md` in reverse chronological order.

## Contradiction workflow

When sources conflict: note in the relevant concept/entity page → create/update a query page → link both sources from the query → resolve in a synthesis page once evidence is sufficient. Full details in `AGENTS.md`.
