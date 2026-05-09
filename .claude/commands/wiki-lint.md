---
description: Run a full health check on the Data Platform wiki
---

Run a full health check on the Data Platform wiki at `/Users/S.Parodi/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/dp-llm-wiki/wiki/`.

Read `SCHEMA.md` first if you haven't already in this session.

Optional flags in $ARGUMENTS:
- `--fix` — automatically fix issues where safe (create stub pages for missing wikilink targets, fix broken frontmatter)
- `--report-only` — print findings to console only, do not write wiki/lint-report.md
- `--section <name>` — run only a specific check: orphans | missing | frontmatter | contradictions | glossary | sources

---

## Lint Workflow

Run all checks below (or only the one specified via --section). After all checks, write the results.

### Check 1 — Missing pages (wikilinks with no target)

1. Use Glob to list all `.md` files under `wiki/` (excluding `wiki/sources/`). Collect the set of page slugs (filename without `.md`).
2. Use Grep with pattern `\[\[([^\]|#]+)` across all `wiki/*.md` files (recursive) to extract all wikilink targets. Normalize: lowercase, strip display text after `|`, strip anchors after `#`.
3. Compute the difference: wikilinks that have no matching page slug.
4. Exclude known-acceptable missing links: `gold-layer`, `secrets`, `decisions/`, `geospatial-data-lakehouse`, `geospatial-format-comparison`, `report-dettagliato-dbt-software`, `dbt-workbench`.
5. Report each missing target with: the wikilink, which pages reference it (up to 3), suggested action (create stub / acceptable gap).

If `--fix` is set: for each missing target that appears in ≥2 pages and is clearly a technology/concept/component, create a minimal stub page using the appropriate template from SCHEMA.md. Place in the correct subdirectory based on what the link refers to.

### Check 2 — Orphan pages (no inbound links)

1. Use Glob to list all wiki pages (exclude `index.md`, `log.md`, `overview.md`, `glossary.md`, `lint-report.md`, `meetings-index.md`, `_classification.md`, and all `sources/` pages).
2. For each page, use Grep to count how many other wiki pages reference `[[page-slug]]` or `[[page-slug|`.
3. Report pages with 0 inbound links as orphans.

### Check 3 — Frontmatter completeness

Sample 20 wiki pages across entity types (not sources). For each:
- Check required fields: `type`, `title`, `tags`, `created`, `updated`
- Check that `type` matches the subdirectory (e.g., files in `technologies/` should have `type: technology`)
- Check that `status` is present for: technology, component, decision, process pages
- Report pages with missing or mismatched fields.

### Check 4 — Source integrity

1. Use Glob to list all `wiki/sources/*.md` files.
2. For each source page, grep for `raw_path:` field and verify the referenced raw file exists under `raw/`.
3. Report broken raw_path references.
4. Count total source summaries and compare against expected (~305).

### Check 5 — Contradictions (spot check)

Check these known tension points — read the relevant pages and flag if the stated status conflicts:
- `kestra.md` vs meeting notes: is Kestra status "active" or still "evaluated"?
- `windmill.md`: confirm it is marked `status: not-selected` or `evaluated`
- `ci-cd-git-flow-v2.1.md`: verify it is `status: current`, v2.0 and v1 are `status: superseded`
- Any technology page where `status: active` but the page content describes rejection

### Check 6 — Glossary gaps

1. Read `wiki/glossary.md`.
2. Collect all technology and concept page titles from `wiki/index.md`.
3. Report technologies/concepts that appear in the wiki but have no glossary entry. Flag the top 10 most-linked missing terms.

### Check 7 — Index completeness

1. Read `wiki/index.md`.
2. Use Glob to count actual pages per entity type subdirectory.
3. Compare counts in the index headers (e.g., "Technologies (31)") against actual file counts.
4. Report any discrepancy.

---

## Output

Unless `--report-only` is set:

1. **Overwrite** `wiki/lint-report.md` with the new findings. Use this structure:

```markdown
---
type: lint-report
title: "Lint Report"
tags: [lint]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Lint Report — <Pass number> Pass

Date: YYYY-MM-DD
Wiki pages: N | Unique wikilinks: N | Source summaries: N

## Missing Pages
...

## Orphan Pages
...

## Frontmatter Issues
...

## Source Integrity
...

## Contradictions
...

## Glossary Gaps
...

## Index vs Actual Counts
...

## Recommendations
### High Priority
### Medium Priority
### Low Priority
```

2. Append to `wiki/log.md`:
```
## [YYYY-MM-DD] lint | <Pass number> lint pass
Summary: N missing pages, N orphans, N frontmatter issues, N source gaps, N contradictions, N glossary gaps.
<brief description of most important findings>
```

3. Print a concise summary table to the console:

| Check | Issues Found | Severity |
|-------|-------------|----------|
| Missing pages | N | medium |
| Orphans | N | low |
| Frontmatter | N | low |
| Source integrity | N | medium |
| Contradictions | N | high |
| Glossary gaps | N | low |
| Index counts | N | low |

---

## Context

- Wiki root: `wiki/`
- Raw sources: `raw/` (read-only, never modify)
- Schema: `SCHEMA.md`
- Previous lint report: `wiki/lint-report.md` (first pass: 2026-04-13, all items resolved)
- Today's date: available from system context
