"""
_parse_file_blocks.py — parser robusto di FILE/REVIEW blocks.

Porting fedele di parseFileBlocks da src/lib/ingest.ts, replica i fix per:
  H1. CRLF → LF normalization
  H2. Stream truncation → surface warning (non silenzioso)
  H3. Marker whitespace/case variants (`--- END FILE ---`, `---end file---`)
  H5. ```END FILE``` dentro fenced code block (non triggera close)
  H6. Empty path → warning

Include anche `is_safe_ingest_path` (guard path traversal).
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Line-level openers/closers, case-insensitive, tollerante a spazi interni
_OPENER_LINE = re.compile(r"^---\s*FILE:\s*(.+?)\s*---\s*$", re.IGNORECASE)
_CLOSER_LINE = re.compile(r"^---\s*END\s+FILE\s*---\s*$", re.IGNORECASE)
# REVIEW block separato
_REVIEW_BLOCK_RE = re.compile(
    r"---REVIEW:\s*(\w[\w-]*)\s*\|\s*(.+?)\s*---\n(.*?)---END REVIEW---",
    re.DOTALL,
)

# CommonMark code fence: triple+ backticks o tildes, leading <=3 spazi
_FENCE_LINE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")

# Windows-invalid filename chars / reserved names
_WIN_INVALID_CHARS = re.compile(r'[<>:"|?*]')
_WIN_TRAILING_SPACE_OR_DOT = re.compile(r"[ .]$")
_WIN_RESERVED_RE = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$", re.IGNORECASE)


@dataclass
class ParsedFileBlock:
    path: str
    content: str


@dataclass
class ParsedReviewBlock:
    type: str          # contradiction | duplicate | missing-page | suggestion | confirm
    title: str
    body: str
    options: list[str]
    pages: list[str]
    search: list[str]


@dataclass
class ParseResult:
    blocks: list[ParsedFileBlock]
    reviews: list[ParsedReviewBlock]
    warnings: list[str]


def is_safe_ingest_path(p: str) -> bool:
    """
    Rifiuta path che tentano di uscire da `wiki/`.

    Allow:  paths sotto `wiki/` (es. `wiki/concepts/foo.md`).
    Reject:
      - paths non sotto `wiki/`
      - absolute paths (`/etc/passwd`, `C:/Windows/...`)
      - `..` segments
      - chars Windows-invalid / reserved device names
      - segment che termina in spazio o `.`
      - NUL / control chars
      - vuoto / solo whitespace
    """
    if not isinstance(p, str) or not p.strip():
        return False
    # No control / NUL bytes
    if any(0 <= ord(c) < 0x20 for c in p):
        return False
    # Reject absolute POSIX e Windows drive
    if p.startswith("/") or p.startswith("\\"):
        return False
    if re.match(r"^[a-zA-Z]:", p):
        return False
    normalized = p.replace("\\", "/")
    segments = normalized.split("/")
    if any(seg == ".." for seg in segments):
        return False
    if not all(_is_windows_safe_segment(seg) for seg in segments):
        return False
    if not normalized.startswith("wiki/"):
        return False
    return True


def _is_windows_safe_segment(segment: str) -> bool:
    if not segment:
        return False
    if _WIN_INVALID_CHARS.search(segment):
        return False
    if _WIN_TRAILING_SPACE_OR_DOT.search(segment):
        return False
    stem = segment.split(".")[0]
    if not stem:
        return False
    if _WIN_RESERVED_RE.match(stem):
        return False
    return True


def parse_blocks(text: str) -> ParseResult:
    """
    Parsa FILE blocks e REVIEW blocks.

    Fix replicati da TS:
      - normalizza CRLF → LF
      - line-based parsing (no regex multi-line greedy)
      - tracking code fence state per non chiudere dentro fence
      - warning su stream truncation (block non chiuso)
      - warning su empty path / unsafe path
    """
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")

    blocks: list[ParsedFileBlock] = []
    warnings: list[str] = []

    i = 0
    while i < len(lines):
        opener = _OPENER_LINE.match(lines[i])
        if not opener:
            i += 1
            continue
        path = opener.group(1).strip()
        i += 1  # consume opener

        content_lines: list[str] = []
        fence_marker: str | None = None
        fence_len = 0
        closed = False

        while i < len(lines):
            line = lines[i]

            # Update fence state PRIMA di checkare closer (H5)
            fence_m = _FENCE_LINE.match(line)
            if fence_m:
                run = fence_m.group(1)
                char = run[0]
                length = len(run)
                if fence_marker is None:
                    fence_marker = char
                    fence_len = length
                elif char == fence_marker and length >= fence_len:
                    fence_marker = None
                    fence_len = 0
                content_lines.append(line)
                i += 1
                continue

            # Closer valido SOLO se fuori da un fence
            if fence_marker is None and _CLOSER_LINE.match(line):
                closed = True
                i += 1
                break

            content_lines.append(line)
            i += 1

        if not closed:
            label = path or "(unnamed)"
            warnings.append(
                f'FILE block "{label}" was not closed before end of stream — '
                f"likely truncation (model hit max_tokens, timeout, or connection dropped). "
                f"Block dropped."
            )
            continue

        if not path:
            warnings.append(
                "FILE block with empty path skipped (LLM omitted path after `---FILE:`)."
            )
            continue

        if not is_safe_ingest_path(path):
            warnings.append(
                f'FILE block with unsafe path "{path}" rejected '
                f"(must be under wiki/, no .., no absolute paths, Windows-safe names)."
            )
            continue

        blocks.append(ParsedFileBlock(path=path, content="\n".join(content_lines)))

    reviews = _parse_reviews(normalized)

    return ParseResult(blocks=blocks, reviews=reviews, warnings=warnings)


def _parse_reviews(text: str) -> list[ParsedReviewBlock]:
    """Parsa REVIEW blocks dal testo. Whole-text regex (è più semplice qui)."""
    reviews: list[ParsedReviewBlock] = []
    valid_types = {"contradiction", "duplicate", "missing-page", "suggestion"}

    for m in _REVIEW_BLOCK_RE.finditer(text):
        raw_type = m.group(1).strip().lower()
        title = m.group(2).strip()
        body_raw = m.group(3).strip()

        review_type = raw_type if raw_type in valid_types else "confirm"

        # Parse OPTIONS / PAGES / SEARCH lines
        options: list[str] = []
        pages: list[str] = []
        search: list[str] = []
        body_lines = []
        for line in body_raw.split("\n"):
            stripped = line.strip()
            if stripped.startswith("OPTIONS:"):
                options = [o.strip() for o in stripped[len("OPTIONS:"):].split("|") if o.strip()]
            elif stripped.startswith("PAGES:"):
                pages = [p.strip() for p in stripped[len("PAGES:"):].split(",") if p.strip()]
            elif stripped.startswith("SEARCH:"):
                search = [s.strip() for s in stripped[len("SEARCH:"):].split("|") if s.strip()]
            else:
                body_lines.append(line)

        reviews.append(ParsedReviewBlock(
            type=review_type,
            title=title,
            body="\n".join(body_lines).strip(),
            options=options,
            pages=pages,
            search=search,
        ))

    return reviews
