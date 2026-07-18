#!/usr/bin/env python

from __future__ import annotations

import os
import signal
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build_pdf.py"
IGNORED_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "_build",
    "exports",
    "node_modules",
}
WATCHED_SUFFIXES = {
    ".css",
    ".gif",
    ".ipynb",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".png",
    ".py",
    ".svg",
    ".tex",
    ".webp",
    ".yml",
    ".yaml",
}
POLL_INTERVAL_SECONDS = 1.0
SETTLE_SECONDS = 1.0


def iter_watched_files() -> list[Path]:
    watched: list[Path] = []
    for current_root, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in IGNORED_DIRS]
        root_path = Path(current_root)
        for filename in filenames:
            path = root_path / filename
            if path.suffix.lower() not in WATCHED_SUFFIXES:
                continue
            watched.append(path)
    return watched


def snapshot() -> dict[str, int]:
    state: dict[str, int] = {}
    for path in iter_watched_files():
        try:
            state[str(path.relative_to(ROOT))] = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
    return state


def rebuild_pdf() -> int:
    print("[pdf] rebuilding export")
    result = subprocess.run([sys.executable, str(BUILD_SCRIPT)], cwd=ROOT, text=True, check=False)
    if result.returncode == 0:
        print("[pdf] export updated")
    else:
        print(f"[pdf] export failed with exit code {result.returncode}")
    return result.returncode


def shutdown(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def main() -> int:
    myst_args = sys.argv[1:]
    if any(arg in {"-h", "--help"} for arg in myst_args):
        return subprocess.run(["npx", "myst", "start", *myst_args], cwd=ROOT, text=True).returncode

    server = subprocess.Popen(["npx", "myst", "start", *myst_args], cwd=ROOT, text=True)

    def handle_signal(signum: int, _frame: object) -> None:
        shutdown(server)
        raise KeyboardInterrupt

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    last_snapshot = snapshot()
    rebuild_pdf()
    pending_since: float | None = None

    try:
        while True:
            if server.poll() is not None:
                return server.returncode or 0

            current_snapshot = snapshot()
            if current_snapshot != last_snapshot:
                last_snapshot = current_snapshot
                pending_since = time.monotonic()

            if pending_since is not None and time.monotonic() - pending_since >= SETTLE_SECONDS:
                snapshot_before_build = last_snapshot
                rebuild_pdf()
                snapshot_after_build = snapshot()
                last_snapshot = snapshot_after_build
                pending_since = (
                    time.monotonic() if snapshot_after_build != snapshot_before_build else None
                )

            time.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        return 0
    finally:
        shutdown(server)


if __name__ == "__main__":
    sys.exit(main())
