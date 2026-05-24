#!/usr/bin/env python3
"""
queue.py — coda leggera di ingest persistente in JSON.

Versione semplificata di src/lib/ingest-queue.ts: niente concorrenza,
niente lock, niente abort signal — l'agente processa sequenzialmente.

Stato in `.llm-wiki/queue/items.json`:
    [{ "id": ..., "source_path": ..., "status": "pending"|"running"|"done"|"failed",
       "added_at": ..., "error": null, "retry_count": 0 }, ...]

Uso:
    python queue.py add <source_path> [<source_path>...]
    python queue.py next                # stampa il prossimo task pending in JSON
    python queue.py mark <id> running|done|failed [--error MSG]
    python queue.py list [--status STATUS]
    python queue.py clear-done
    python queue.py reset-failed        # ri-imposta failed → pending (retry)
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import uuid
from pathlib import Path


def find_vault_root(start: Path) -> Path:
    cur = start.resolve()
    while True:
        if (cur / "wiki").is_dir() and (cur / ".llm-wiki").exists():
            return cur
        if cur.parent == cur:
            raise SystemExit(f"Non trovo una vault llm-wiki risalendo da {start}")
        cur = cur.parent


def queue_file(vault_root: Path) -> Path:
    return vault_root / ".llm-wiki" / "queue" / "items.json"


def load_queue(vault_root: Path) -> list[dict]:
    p = queue_file(vault_root)
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []


def save_queue(vault_root: Path, items: list[dict]) -> None:
    p = queue_file(vault_root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")


def cmd_add(vault_root: Path, source_paths: list[Path]) -> list[str]:
    items = load_queue(vault_root)
    existing_paths = {it["source_path"] for it in items if it["status"] in ("pending", "running")}
    new_ids: list[str] = []

    for sp in source_paths:
        sp_str = str(sp.resolve())
        if sp_str in existing_paths:
            continue
        item = {
            "id": f"ingest-{int(time.time())}-{uuid.uuid4().hex[:6]}",
            "source_path": sp_str,
            "status": "pending",
            "added_at": time.time(),
            "error": None,
            "retry_count": 0,
        }
        items.append(item)
        new_ids.append(item["id"])

    save_queue(vault_root, items)
    return new_ids


def cmd_next(vault_root: Path) -> dict | None:
    items = load_queue(vault_root)
    for item in items:
        if item["status"] == "pending":
            return item
    return None


def cmd_mark(vault_root: Path, task_id: str, status: str, error: str | None = None) -> bool:
    items = load_queue(vault_root)
    found = False
    for item in items:
        if item["id"] == task_id:
            item["status"] = status
            if status == "failed":
                item["error"] = error
                item["retry_count"] = item.get("retry_count", 0) + 1
            elif status == "running":
                item["error"] = None
            elif status == "done":
                item["error"] = None
            found = True
            break
    save_queue(vault_root, items)
    return found


def cmd_list(vault_root: Path, status_filter: str | None = None) -> list[dict]:
    items = load_queue(vault_root)
    if status_filter:
        items = [it for it in items if it["status"] == status_filter]
    return items


def cmd_clear_done(vault_root: Path) -> int:
    items = load_queue(vault_root)
    before = len(items)
    items = [it for it in items if it["status"] != "done"]
    save_queue(vault_root, items)
    return before - len(items)


def cmd_reset_failed(vault_root: Path) -> int:
    items = load_queue(vault_root)
    count = 0
    for it in items:
        if it["status"] == "failed":
            it["status"] = "pending"
            it["error"] = None
            count += 1
    save_queue(vault_root, items)
    return count


def main() -> int:
    ap = argparse.ArgumentParser(description="Ingest queue management")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_add = sub.add_parser("add", help="Aggiungi file alla coda")
    ap_add.add_argument("source_paths", nargs="+", type=Path)

    sub.add_parser("next", help="Stampa il prossimo task pending in JSON")

    ap_mark = sub.add_parser("mark", help="Aggiorna lo stato di un task")
    ap_mark.add_argument("task_id")
    ap_mark.add_argument("status", choices=["pending", "running", "done", "failed"])
    ap_mark.add_argument("--error", help="Messaggio errore (per status=failed)")

    ap_list = sub.add_parser("list", help="Elenca task")
    ap_list.add_argument("--status", choices=["pending", "running", "done", "failed"])

    sub.add_parser("clear-done", help="Rimuovi task done dalla coda")
    sub.add_parser("reset-failed", help="Ri-imposta failed → pending")

    args = ap.parse_args()
    vault_root = find_vault_root(Path.cwd())

    if args.cmd == "add":
        ids = cmd_add(vault_root, args.source_paths)
        print(json.dumps(ids))
        return 0

    if args.cmd == "next":
        item = cmd_next(vault_root)
        if item is None:
            return 1
        print(json.dumps(item))
        return 0

    if args.cmd == "mark":
        ok = cmd_mark(vault_root, args.task_id, args.status, args.error)
        return 0 if ok else 1

    if args.cmd == "list":
        items = cmd_list(vault_root, args.status)
        print(json.dumps(items, indent=2, ensure_ascii=False))
        return 0

    if args.cmd == "clear-done":
        n = cmd_clear_done(vault_root)
        print(f"✓ Rimossi {n} task done", file=sys.stderr)
        return 0

    if args.cmd == "reset-failed":
        n = cmd_reset_failed(vault_root)
        print(f"✓ Reset {n} task failed → pending", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
