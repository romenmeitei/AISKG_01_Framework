#!/usr/bin/env python3
"""Verify every release file listed in PACKAGE_MANIFEST.csv."""
from __future__ import annotations
import csv
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "PACKAGE_MANIFEST.csv"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

if not MANIFEST.is_file():
    raise SystemExit("Missing PACKAGE_MANIFEST.csv")

failures = []
with MANIFEST.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        rel = row["path"]
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"MISSING: {rel}")
            continue
        actual_size = path.stat().st_size
        actual_hash = sha256(path)
        if actual_size != int(row["bytes"]):
            failures.append(f"SIZE: {rel} expected={row['bytes']} actual={actual_size}")
        if actual_hash != row["sha256"]:
            failures.append(f"SHA256: {rel} expected={row['sha256']} actual={actual_hash}")

if failures:
    print("Repository verification FAILED")
    print("\n".join(failures))
    sys.exit(1)
print("Repository verification PASSED")
