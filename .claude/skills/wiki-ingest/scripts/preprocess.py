#!/usr/bin/env python3
"""
preprocess.py — converte un file sorgente (PDF/DOCX/PPTX/XLSX/HTML/MD/TXT)
in markdown plain via MarkItDown.

Sostituisce il preprocessing Rust del backend originale (pdfium / calamine /
docx-rs / pptx). Output: markdown su stdout.

Uso:
    python preprocess.py <path> [--max-chars 50000]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def preprocess(path: Path, max_chars: int | None = None) -> str:
    """Converti `path` in markdown.

    - Per .md/.txt: legge direttamente.
    - Per altri formati: usa MarkItDown.
    - Tronca a `max_chars` se specificato (replica del cap a 50_000 dell'originale).
    """
    suffix = path.suffix.lower()

    if suffix in (".md", ".markdown", ".txt"):
        content = path.read_text(encoding="utf-8", errors="replace")
    else:
        try:
            from markitdown import MarkItDown
        except ImportError:
            print(
                "Errore: markitdown non installato. Esegui:\n"
                "    pip install 'markitdown[all]'",
                file=sys.stderr,
            )
            sys.exit(2)

        md = MarkItDown()
        try:
            result = md.convert(str(path))
            content = result.text_content
        except Exception as e:
            print(f"Errore conversione {path}: {e}", file=sys.stderr)
            sys.exit(3)

    if max_chars and len(content) > max_chars:
        content = content[:max_chars] + "\n\n[...truncated...]"

    return content


def main() -> int:
    ap = argparse.ArgumentParser(description="Preprocess a document → markdown")
    ap.add_argument("path", type=Path, help="Source file path")
    ap.add_argument("--max-chars", type=int, default=50_000,
                    help="Tronca a N caratteri (default 50000, come backend originale)")
    args = ap.parse_args()

    if not args.path.is_file():
        print(f"Errore: file non trovato: {args.path}", file=sys.stderr)
        return 1

    print(preprocess(args.path, args.max_chars))
    return 0


if __name__ == "__main__":
    sys.exit(main())
