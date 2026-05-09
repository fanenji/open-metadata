#!/usr/bin/env python3
"""Transcribe video/audio files using mlx_whisper.

Usage:
    python3 _system/scripts/transcript.py <file_path> [--lang LANG]
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi"}
AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".ogg", ".aac", ".flac"}


def check_requirements():
    errors = []
    if not shutil.which("ffmpeg"):
        errors.append(
            "ffmpeg not found. Install it:\n"
            "  brew install ffmpeg"
        )
    try:
        import mlx_whisper  # noqa: F401
    except ImportError:
        errors.append(
            "mlx_whisper not found. Install it:\n"
            "  pip install mlx-whisper"
        )
    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        sys.exit(1)


def detect_type(path):
    ext = Path(path).suffix.lower()
    if ext in VIDEO_EXTS:
        return "video"
    if ext in AUDIO_EXTS:
        return "audio"
    return None


def extract_audio(input_path, wav_path, media_type):
    if media_type == "video":
        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            wav_path,
            "-y",
        ]
    else:
        cmd = [
            "ffmpeg",
            "-i", input_path,
            wav_path,
            "-y",
        ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)


def transcribe(wav_path, lang=None):
    import mlx_whisper

    kwargs = {"path_or_hf_repo": "mlx-community/whisper-large-v3-turbo"}
    if lang:
        kwargs["language"] = lang

    result = mlx_whisper.transcribe(wav_path, **kwargs)
    return result["text"]


def main():
    parser = argparse.ArgumentParser(description="Transcribe video/audio files.")
    parser.add_argument("file_path", help="Path to the video or audio file")
    parser.add_argument(
        "--lang",
        help="Language code for whisper (auto-detect if not set)",
        default=None,
    )
    args = parser.parse_args()

    input_path = os.path.abspath(args.file_path)
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    media_type = detect_type(input_path)
    if media_type is None:
        ext = Path(input_path).suffix.lower()
        supported = sorted(VIDEO_EXTS | AUDIO_EXTS)
        print(
            f"Unsupported file type: {ext}\n"
            f"Supported extensions: {', '.join(supported)}",
            file=sys.stderr,
        )
        sys.exit(1)

    check_requirements()

    input_dir = os.path.dirname(input_path)
    stem = Path(input_path).stem
    wav_path = os.path.join("/tmp", f"{stem}_transcript.wav")
    output_path = os.path.join(input_dir, f"{stem}_TRANSCRIPS.txt")

    extract_audio(input_path, wav_path, media_type)
    text = transcribe(wav_path, lang=args.lang)

    with open(output_path, "w") as f:
        f.write(text)

    os.remove(wav_path)
    print(f"Transcript saved: {output_path}")


if __name__ == "__main__":
    main()
