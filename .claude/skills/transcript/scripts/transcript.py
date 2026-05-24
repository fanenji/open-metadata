#!/usr/bin/env python3
"""
transcript.py — trascrizione audio/video locale via mlx_whisper.

Porting dello script originale `_system/scripts/transcript.py` con
migliorie minime:
  - Fix typo output suffix: `_TRANSCRIPS.txt` → `_TRANSCRIPTS.txt`
  - Accetta directory come argomento → processa tutti i file supportati
  - Skip file con `_TRANSCRIPTS.txt` esistente (no double work)
  - Exit code: 0 ok, 1 errore irreversibile, 2 prerequisiti mancanti

Uso:
    python transcript.py <file_or_dir> [--lang it|en] [--force]
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi"}
AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".ogg", ".aac", ".flac"}
SUPPORTED = VIDEO_EXTS | AUDIO_EXTS
OUTPUT_SUFFIX = "_TRANSCRIPTS.txt"


def check_requirements() -> None:
    errors: list[str] = []
    if not shutil.which("ffmpeg"):
        errors.append(
            "ffmpeg not found. Install it:\n  brew install ffmpeg"
        )
    try:
        import mlx_whisper  # noqa: F401
    except ImportError:
        errors.append(
            "mlx_whisper not found. Install it:\n  pip install mlx-whisper"
        )
    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        sys.exit(2)


def detect_type(path: Path) -> str | None:
    ext = path.suffix.lower()
    if ext in VIDEO_EXTS:
        return "video"
    if ext in AUDIO_EXTS:
        return "audio"
    return None


def extract_audio(input_path: Path, wav_path: Path, media_type: str) -> None:
    if media_type == "video":
        cmd = [
            "ffmpeg", "-i", str(input_path),
            "-vn", "-acodec", "pcm_s16le",
            "-ar", "16000", "-ac", "1",
            str(wav_path), "-y",
        ]
    else:
        cmd = ["ffmpeg", "-i", str(input_path), str(wav_path), "-y"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("ffmpeg conversion failed")


def transcribe_one(wav_path: Path, lang: str | None = None) -> str:
    import mlx_whisper

    kwargs: dict = {"path_or_hf_repo": "mlx-community/whisper-large-v3-turbo"}
    if lang:
        kwargs["language"] = lang

    result = mlx_whisper.transcribe(str(wav_path), **kwargs)
    return result["text"]


def output_path_for(input_path: Path) -> Path:
    return input_path.parent / f"{input_path.stem}{OUTPUT_SUFFIX}"


def process_file(input_path: Path, lang: str | None, force: bool) -> int:
    """Ritorna 0 ok, 1 errore, 2 skip."""
    out = output_path_for(input_path)
    if out.exists() and not force:
        print(f"  ⏭  {input_path.name} → existing {out.name} (use --force to redo)")
        return 2

    media_type = detect_type(input_path)
    if media_type is None:
        print(f"  ✗ Unsupported: {input_path.name}", file=sys.stderr)
        return 1

    wav = Path("/tmp") / f"{input_path.stem}_transcript.wav"
    try:
        extract_audio(input_path, wav, media_type)
        text = transcribe_one(wav, lang=lang)
    except Exception as e:
        print(f"  ✗ {input_path.name}: {e}", file=sys.stderr)
        return 1
    finally:
        if wav.exists():
            try:
                wav.unlink()
            except OSError:
                pass

    out.write_text(text, encoding="utf-8")
    print(f"  ✓ {input_path.name} → {out.name}")
    return 0


def collect_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() in SUPPORTED else []
    files: list[Path] = []
    for p in sorted(path.iterdir()):
        if p.is_file() and p.suffix.lower() in SUPPORTED:
            files.append(p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description="Transcribe audio/video with mlx_whisper.")
    ap.add_argument("path", type=Path, help="File or directory")
    ap.add_argument("--lang", default=None, help="Language code (it, en, …); auto-detect if omitted")
    ap.add_argument("--force", action="store_true", help="Re-transcribe even if output exists")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"Not found: {args.path}", file=sys.stderr)
        return 1

    check_requirements()

    files = collect_files(args.path.resolve())
    if not files:
        print("No supported audio/video files.", file=sys.stderr)
        return 1

    print(f"→ Transcribing {len(files)} file(s)...")
    ok = err = skipped = 0
    for f in files:
        rc = process_file(f, args.lang, args.force)
        if rc == 0:
            ok += 1
        elif rc == 1:
            err += 1
        else:
            skipped += 1

    print(f"\nDone — ok={ok}, errors={err}, skipped={skipped}")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
