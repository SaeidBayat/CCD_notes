#!/usr/bin/env python

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PDF = ROOT / "exports" / "notes.pdf"
SITE_ROOT = ROOT / "_build" / "html"
SITE_PDF = ROOT / "_build" / "html" / "exports" / "notes.pdf"
CUSTOM_DOMAIN = ROOT / "CNAME"
SITE_CNAME = SITE_ROOT / "CNAME"


def advertised_pdf_paths() -> list[Path]:
    config_path = SITE_ROOT / "config.json"
    if not config_path.exists():
        return []

    config = json.loads(config_path.read_text())
    urls: set[str] = set()

    for action in config.get("actions", []):
        if action.get("format") == "pdf" and action.get("url"):
            urls.add(action["url"])

    for project in config.get("projects", []):
        for export in project.get("exports", []):
            if export.get("format") == "pdf" and export.get("url"):
                urls.add(export["url"])

    paths: list[Path] = []
    for url in sorted(urls):
        relative = url.lstrip("/")
        if relative:
            paths.append(SITE_ROOT / relative)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-pdf",
        action="store_true",
        help="Skip regenerating the PDF before building the site.",
    )
    args = parser.parse_args()

    if not args.skip_pdf:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_pdf.py")],
            cwd=ROOT,
            text=True,
            check=True,
        )

    subprocess.run(
        ["npx", "myst", "build", "--html", "--force", "--ci"],
        cwd=ROOT,
        text=True,
        check=True,
    )
    if CUSTOM_DOMAIN.exists():
        shutil.copy2(CUSTOM_DOMAIN, SITE_CNAME)
        print("Copied", CUSTOM_DOMAIN, "to", SITE_CNAME)
    if OUTPUT_PDF.exists():
        SITE_PDF.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(OUTPUT_PDF, SITE_PDF)
        print("Copied", OUTPUT_PDF, "to", SITE_PDF)
        for path in advertised_pdf_paths():
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(OUTPUT_PDF, path)
            print("Copied", OUTPUT_PDF, "to", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
