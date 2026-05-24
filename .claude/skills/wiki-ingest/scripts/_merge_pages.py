"""
_merge_pages.py — merge soft di una pagina esistente con una nuova generata.

Porting parziale di src/lib/page-merge.ts. Replica:
  - Array fields union (sources, tags, related) — sempre
  - Locked fields (type, title, created) — sempre preservati dall'esistente
  - Updated stamp = oggi

Il merge LLM-based del body (terzo layer del backend originale) è DELEGATO
all'agente: questo modulo emette un flag `merge_body_needed` quando i bodies
differiscono. L'agente legge il flag, esegue il merge nel suo contesto LLM,
e ri-invoca lo script con il body risultante.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date

UNION_FIELDS = ("sources", "tags", "related")
LOCKED_FIELDS = ("type", "title", "created")
BODY_SHRINK_THRESHOLD = 0.7  # come backend originale

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class MergeOutcome:
    """Esito del merge."""
    content: str                       # Contenuto finale (potrebbe necessitare LLM body merge)
    merge_body_needed: bool            # True se i bodies differiscono e serve LLM merge
    existing_body: str = ""            # Body esistente (se merge_body_needed)
    incoming_body: str = ""            # Body incoming (array-merged, se merge_body_needed)
    fallback_used: bool = False        # True se il merge è stato un fallback semplice


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse frontmatter best-effort. Ritorna (dict, body)."""
    m = _FM_RE.match(content)
    if not m:
        return {}, content
    raw = m.group(1)
    body = content[m.end():]

    fm: dict = {}
    for line in raw.split("\n"):
        line = line.rstrip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
            fm[key] = items
        elif value == "":
            fm[key] = None
        else:
            fm[key] = value
    return fm, body


def merge_array_field(existing: list | None, incoming: list | None) -> list:
    """Union deterministico, mantiene ordine: prima existing, poi incoming nuovi."""
    seen: set[str] = set()
    out: list = []
    for v in (existing or []) + (incoming or []):
        key = str(v).strip()
        if key and key not in seen:
            seen.add(key)
            out.append(v)
    return out


def merge_pages(
    new_content: str,
    existing_content: str | None,
    source_filename: str = "",
    today: str | None = None,
) -> MergeOutcome:
    """
    Merge soft. Casistica:
      1. existing == None → ritorna new_content as-is.
      2. byte-identical → ritorna existing.
      3. solo array fields differiscono → array union, ritorna risultato.
      4. bodies differiscono → ritorna stato che richiede LLM merge.
    """
    if existing_content is None:
        return MergeOutcome(content=new_content, merge_body_needed=False)

    if new_content == existing_content:
        return MergeOutcome(content=existing_content, merge_body_needed=False)

    today_str = today or date.today().isoformat()

    old_fm, old_body = parse_frontmatter(existing_content)
    new_fm, new_body = parse_frontmatter(new_content)

    # Array fields union
    merged_fm = dict(new_fm)
    for field in UNION_FIELDS:
        merged_fm[field] = merge_array_field(old_fm.get(field), new_fm.get(field))

    # Locked fields: preserva esistente se presente
    for field in LOCKED_FIELDS:
        existing_val = old_fm.get(field)
        if existing_val:
            merged_fm[field] = existing_val

    # Updated = oggi
    merged_fm["updated"] = today_str

    # Body merge: se i bodies sono uguali (modulo whitespace), no LLM needed
    if old_body.strip() == new_body.strip():
        return MergeOutcome(
            content=_render(merged_fm, new_body),
            merge_body_needed=False,
        )

    # Bodies differiscono → segnala bisogno LLM merge
    return MergeOutcome(
        content=_render(merged_fm, new_body),  # fallback: usa new body con fm merged
        merge_body_needed=True,
        existing_body=old_body,
        incoming_body=new_body,
        fallback_used=True,
    )


def apply_llm_merge_result(
    llm_output: str,
    existing_content: str,
    incoming_content: str,
    today: str | None = None,
) -> str:
    """
    Applica deterministicamente le regole post-LLM:
      - Sanity check body length (≥70% del max)
      - Lock back type/title/created
      - Re-union sources/tags/related
      - Updated = oggi

    Se sanity check fallisce, ritorna fallback (incoming + array union).
    """
    today_str = today or date.today().isoformat()

    llm_fm, llm_body = parse_frontmatter(llm_output)
    if not llm_fm:
        # Output LLM senza frontmatter → reject, fallback
        old_fm, old_body = parse_frontmatter(existing_content)
        new_fm, new_body = parse_frontmatter(incoming_content)
        for f in UNION_FIELDS:
            new_fm[f] = merge_array_field(old_fm.get(f), new_fm.get(f))
        for f in LOCKED_FIELDS:
            if old_fm.get(f):
                new_fm[f] = old_fm[f]
        new_fm["updated"] = today_str
        return _render(new_fm, new_body)

    old_fm, old_body = parse_frontmatter(existing_content)
    new_fm, new_body = parse_frontmatter(incoming_content)

    # Sanity check body length
    threshold = max(len(old_body), len(new_body)) * BODY_SHRINK_THRESHOLD
    if len(llm_body) < threshold:
        # LLM ha probabilmente troncato. Fallback.
        for f in UNION_FIELDS:
            new_fm[f] = merge_array_field(old_fm.get(f), new_fm.get(f))
        for f in LOCKED_FIELDS:
            if old_fm.get(f):
                new_fm[f] = old_fm[f]
        new_fm["updated"] = today_str
        return _render(new_fm, new_body)

    # OK: apply post-processing all'output LLM
    for f in LOCKED_FIELDS:
        if old_fm.get(f):
            llm_fm[f] = old_fm[f]
    for f in UNION_FIELDS:
        llm_fm[f] = merge_array_field(
            old_fm.get(f),
            merge_array_field(new_fm.get(f), llm_fm.get(f)),
        )
    llm_fm["updated"] = today_str

    return _render(llm_fm, llm_body)


def _render(fm: dict, body: str) -> str:
    """Render frontmatter + body in markdown standard."""
    lines = ["---"]
    for k, v in fm.items():
        if v is None:
            lines.append(f"{k}:")
        elif isinstance(v, list):
            items = ", ".join(
                f'"{x}"' if isinstance(x, str) and (":" in x or "[" in x) else str(x)
                for x in v
            )
            lines.append(f"{k}: [{items}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, str) and ":" in v:
            lines.append(f'{k}: "{v}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n" + body.lstrip("\n")
