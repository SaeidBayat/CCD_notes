#!/usr/bin/env python

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageSequence


ROOT = Path(__file__).resolve().parents[1]
TEMP_ROOT = ROOT / "_build" / "temp"
OUTPUT_PDF = ROOT / "exports" / "notes.pdf"
PDF_TEMP_ROOT = ROOT / "tmp" / "pdfs"
MYST_BUILD_LOG = PDF_TEMP_ROOT / "myst-build.log"
LATEX_BUILD_LOG = PDF_TEMP_ROOT / "latex-build.log"
BEGIN_FRAMED = r"\begin{framed}"
END_FRAMED = r"\end{framed}"
EMOJI_REPLACEMENTS = {
    "\ufe0f": "",
    "✍": "handwritten",
    "✅": "True",
    "❌": "False",
    "🎥": "video",
}
SOURCE_DIRS = [
    "00_math_foundations",
    "01_introduction_to_control_co_design",
    "02_Dynamic_Systems_and_Feedback_Control",
    "03_Engineering_Design_Optimization",
    "04_Mathematical_Formulation_of_CCD",
    "05_CCD_Architectures_and_Coordination",
    "06_Optimal_Control_and_Closed_Loop_CCD",
    "07_Numerical_Methods_for_CCD",
    "08_Practical_CCD_Studies",
]
ENV_BY_KIND = {
    "note": "mystnote",
    "tip": "mysttip",
    "warning": "mystwarning",
    "attention": "mystattention",
    "seealso": "mystseealso",
    "admonition": "mystgeneric",
}
INDEX_TEX_NAME = "notes-index-frontmatter.tex"


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, text=True, check=check)


def latest_build_dir(temp_root: Path, before: set[Path]) -> Path:
    candidates = [
        path
        for path in temp_root.glob("myst*")
        if path.is_dir() and (path / "notes.tex").exists() and (path / "files").is_dir()
    ]
    new_candidates = [path for path in candidates if path.resolve() not in before]
    if new_candidates:
        candidates = new_candidates
    if not candidates:
        raise RuntimeError("Could not locate a MyST LaTeX temp directory")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def repo_last_commit() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%h"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        iso = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "Git metadata unavailable"
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone()
    hour = dt.strftime("%I").lstrip("0") or "0"
    return f"{dt:%B} {dt.day}, {dt:%Y} at {hour}:{dt:%M} {dt:%p} {dt:%Z} ({sha})"


def normalize_title(text: str) -> str:
    text = text.strip()
    text = text.replace("**", "")
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\\+", r"\\", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_title_kind_map() -> dict[str, str]:
    title_kind: dict[str, str] = {}

    def register(kind: str, title: str) -> None:
        normalized = normalize_title(title or kind.title())
        if normalized:
            title_kind[normalized] = kind

    for path in [ROOT / "advice.md", ROOT / "index.ipynb"]:
        if path.suffix == ".md":
            for line in path.read_text().splitlines():
                if line.startswith(":::"):
                    match = re.match(r":::\{([a-z]+)\}\s*(.*)", line)
                    if match:
                        register(match.group(1), match.group(2))
        else:
            data = json.loads(path.read_text())
            for cell in data.get("cells", []):
                if cell.get("cell_type") != "markdown":
                    continue
                source = "".join(cell.get("source", []))
                for line in source.splitlines():
                    if line.startswith(":::"):
                        match = re.match(r":::\{([a-z]+)\}\s*(.*)", line)
                        if match:
                            register(match.group(1), match.group(2))

    for dirname in SOURCE_DIRS:
        source_paths = sorted((ROOT / dirname).glob("*.ipynb"))
        source_paths += sorted((ROOT / dirname).glob("*.md"))
        for path in source_paths:
            if path.suffix == ".md":
                sources = [path.read_text()]
            else:
                data = json.loads(path.read_text())
                sources = [
                    "".join(cell.get("source", []))
                    for cell in data.get("cells", [])
                    if cell.get("cell_type") == "markdown"
                ]
            for source in sources:
                for line in source.splitlines():
                    if line.startswith(":::"):
                        match = re.match(r":::\{([a-z]+)\}\s*(.*)", line)
                        if match:
                            register(match.group(1), match.group(2))
    return title_kind


def parse_braced(text: str, brace_start: int) -> tuple[str, int]:
    if brace_start >= len(text) or text[brace_start] != "{":
        raise ValueError("Expected opening brace")
    depth = 0
    buffer: list[str] = []
    for idx in range(brace_start, len(text)):
        char = text[idx]
        escaped = idx > 0 and text[idx - 1] == "\\"
        if char == "{" and not escaped:
            depth += 1
            if depth > 1:
                buffer.append(char)
            continue
        if char == "}" and not escaped:
            depth -= 1
            if depth == 0:
                return "".join(buffer), idx + 1
            buffer.append(char)
            continue
        if depth >= 1:
            buffer.append(char)
    raise ValueError("Unbalanced braces in framed title")


def strip_latex_wrappers(text: str) -> str:
    out = text
    patterns = [
        re.compile(r"\\textbf\{([^{}]*)\}"),
        re.compile(r"\\texttt\{([^{}]*)\}"),
        re.compile(r"\\emph\{([^{}]*)\}"),
    ]
    changed = True
    while changed:
        changed = False
        for pattern in patterns:
            new_out = pattern.sub(r"\1", out)
            changed = changed or new_out != out
            out = new_out
    out = out.replace(r"\:", " ")
    out = out.replace(r"\\", " ")
    out = re.sub(r"\s+", " ", out)
    return normalize_title(out)


def classify_title(title: str, title_kind_map: dict[str, str]) -> str:
    normalized = strip_latex_wrappers(title)
    if normalized in title_kind_map:
        return title_kind_map[normalized]
    lowered = normalized.lower()
    if "activity" in lowered:
        return "tip"
    if lowered in {"solution", "solutions"}:
        return "seealso"
    if lowered.startswith("definition"):
        return "note"
    if lowered.startswith("warning"):
        return "warning"
    return "admonition"


def extract_framed_title(content: str) -> tuple[str, str]:
    stripped = content.lstrip()
    prefix = r"\textbf"
    if not stripped.startswith(prefix + "{"):
        return "Note", stripped
    title, end = parse_braced(stripped, len(prefix))
    remainder = stripped[end:]
    if remainder.startswith(r"\\"):
        remainder = remainder[2:]
    remainder = remainder.lstrip("\n")
    return title.strip(), remainder


def transform_framed_blocks(text: str, title_kind_map: dict[str, str]) -> str:
    def walk(start: int, stop_token: str | None = None) -> tuple[str, int]:
        pieces: list[str] = []
        idx = start
        while idx < len(text):
            if stop_token and text.startswith(stop_token, idx):
                return "".join(pieces), idx + len(stop_token)
            if text.startswith(BEGIN_FRAMED, idx):
                inner, idx = walk(idx + len(BEGIN_FRAMED), END_FRAMED)
                title, body = extract_framed_title(inner)
                kind = classify_title(title, title_kind_map)
                env_name = ENV_BY_KIND.get(kind, "mystgeneric")
                pieces.append(
                    f"\n\\begin{{{env_name}}}{{{title}}}\n{body.strip()}\n\\end{{{env_name}}}\n"
                )
                continue
            pieces.append(text[idx])
            idx += 1
        if stop_token:
            raise ValueError(f"Unclosed token {stop_token}")
        return "".join(pieces), idx

    return walk(0)[0]


def replace_color_commands(text: str) -> str:
    def convert(match: re.Match[str]) -> str:
        value = match.group(1)
        if re.fullmatch(r"#?[0-9A-Fa-f]{6}", value):
            hex_value = value.lstrip("#").upper()
            return rf"\color[HTML]{{{hex_value}}}"
        return match.group(0)

    return re.sub(r"\\color\{([^}]+)\}", convert, text)


def fix_oversized_figures(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        options = match.group(1)
        path = match.group(2)
        width_match = re.search(r"width=([0-9.]+)\\linewidth", options)
        if width_match and float(width_match.group(1)) > 0.98:
            options = re.sub(r"width=[0-9.]+\\linewidth", r"width=0.98\\linewidth", options)
        return rf"\includegraphics[{options}]{{{path}}}"

    return re.sub(r"\\includegraphics\[([^\]]+)\]\{([^}]+)\}", repl, text)


def patch_main_tex(text: str, last_commit: str) -> str:
    text = text.replace("%%LAST_COMMIT%%", last_commit)
    text = text.replace(
        "\\begin{document}\n\\maketitle",
        "\\begin{document}\n\\maketitle\n\n\\frontmatter",
        1,
    )
    text = text.replace(
        "\\frontmatter\n\n\n\n\\include{notes-advice}",
        "\\frontmatter\n\n\\include{notes-index-frontmatter}\n\n\\include{notes-advice}",
        1,
    )
    text = re.sub(r"\\section\{Chapter \d+: ([^}]*)\}", r"\\chapter{\1}", text)
    math_foundations = r"\chapter{Mathematical Prerequisites}"
    text = text.replace(
        math_foundations,
        "\\mainmatter\n\\setcounter{chapter}{-1}\n\n" + math_foundations,
        1,
    )
    return text


def index_markdown() -> str:
    notebook = json.loads((ROOT / "index.ipynb").read_text())
    cells: list[str] = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            cells.append("".join(cell.get("source", [])))
    return "\n\n".join(cells).strip() + "\n"


def markdown_to_latex(markdown: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "markdown+raw_tex", "-t", "latex"],
        input=markdown,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def render_index_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    pieces: list[str] = []
    markdown_buffer: list[str] = []

    def flush_markdown() -> None:
        if not markdown_buffer:
            return
        pieces.append(markdown_to_latex("\n".join(markdown_buffer).strip() + "\n"))
        markdown_buffer.clear()

    idx = 0
    while idx < len(lines):
        line = lines[idx]
        match = re.match(r":::\{([a-z]+)\}\s*(.*)", line)
        if not match:
            markdown_buffer.append(line)
            idx += 1
            continue

        flush_markdown()
        kind = match.group(1)
        title = match.group(2).strip() or kind.title()
        env_name = ENV_BY_KIND.get(kind, "mystgeneric")
        body: list[str] = []
        idx += 1
        while idx < len(lines) and lines[idx].strip() != ":::":
            body.append(lines[idx])
            idx += 1
        idx += 1
        body_latex = markdown_to_latex("\n".join(body).strip() + "\n").strip()
        pieces.append(f"\\begin{{{env_name}}}{{{title}}}\n{body_latex}\n\\end{{{env_name}}}\n")

    flush_markdown()
    return "".join(pieces)


def build_index_tex(title_kind_map: dict[str, str]) -> str:
    text = render_index_markdown(index_markdown())
    text = re.sub(r"\\section\{[^}]+\}\\label\{[^}]+\}\n+", "", text, count=1)
    text = text.replace(r"\subsubsection{", r"@@INDEX_SUBSUBSECTION@@{")
    text = text.replace(r"\subsection{", r"\section{")
    text = text.replace(r"@@INDEX_SUBSUBSECTION@@{", r"\subsection{")
    text = replace_color_commands(text)
    text = fix_oversized_figures(text)
    text = transform_framed_blocks(text, title_kind_map)
    return (
        r"\chapter*{About These Notes}\addcontentsline{toc}{chapter}{About These Notes}" + "\n\n" + text
    )


def patch_included_tex(
    text: str,
    filename: str,
    title_kind_map: dict[str, str],
    build_dir: Path,
) -> str:
    for original, replacement in EMOJI_REPLACEMENTS.items():
        text = text.replace(original, replacement)

    text = replace_color_commands(text)
    text = text.replace(".gif}", ".png}")
    text = text.replace(".svg}", ".pdf}")
    text = text.replace(r"\includesvg{", r"\includegraphics[width=0.98\linewidth]{")
    text = re.sub(r"(?m)^\\newline\s*$", r"\\par", text)
    text = re.sub(r"\A\\section\{Chapter \d+:[^}]*\}\s*", "", text, count=1)
    text = fix_oversized_figures(text)

    def prefer_vector(match: re.Match[str]) -> str:
        options, relative = match.groups()
        path = Path(relative)
        vector = path.with_suffix(".pdf")
        if path.suffix.lower() == ".png" and (build_dir / vector).exists():
            relative = vector.as_posix()
        return rf"\includegraphics[{options}]{{{relative}}}"

    text = re.sub(
        r"\\includegraphics\[([^\]]+)\]\{(files/[^}]+)\}",
        prefer_vector,
        text,
    )
    text = re.sub(
        r"\\includegraphics\[[^\]]*\]\{files/undefined\}",
        lambda _match: r"\begin{mystwarning}{PDF note}An external animated image used in the web notes was omitted from this PDF export.\end{mystwarning}",
        text,
    )

    if filename == "notes-advice.tex":
        text = text.replace(
            r"\section{Advice to Students}",
            r"\chapter*{Advice to Students}\addcontentsline{toc}{chapter}{Advice to Students}",
            1,
        )
    else:
        text = text.replace(r"\subsubsection*{", r"@@SUBSECTIONSTAR@@{")
        text = text.replace(r"\subsubsection{", r"@@SUBSECTION@@{")
        text = text.replace(r"\subsection{", r"\section{")
        text = text.replace(r"@@SUBSECTIONSTAR@@{", r"\subsection*{")
        text = text.replace(r"@@SUBSECTION@@{", r"\subsection{")

    return transform_framed_blocks(text, title_kind_map)


def convert_svg(svg: Path, pdf: Path) -> None:
    # Use a short-lived process for every SVG so the renderer cannot retain
    # decoded image data across the dozens of course figures.
    converter = shutil.which("rsvg-convert")
    if converter is not None:
        subprocess.run(
            [converter, "--format", "pdf", "--output", str(pdf), str(svg)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return

    try:
        import cairosvg

        cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))
    except (ImportError, OSError) as error:
        raise RuntimeError(
            "SVG conversion requires rsvg-convert or CairoSVG with its native Cairo library."
        ) from error


def stage_project(stage_root: Path) -> None:
    """Create a PDF-only project whose figure references use vector PDFs.

    MyST otherwise rasterizes every SVG through its image pipeline before it
    writes LaTeX. With a full nine-chapter book, that conversion can exhaust
    memory. The staged copy leaves the web sources untouched.
    """
    for filename in ["myst.yml", "index.ipynb", "advice.md"]:
        shutil.copy2(ROOT / filename, stage_root / filename)

    for dirname in [*SOURCE_DIRS, "assets", "templates", "plugins"]:
        source = ROOT / dirname
        if source.exists():
            shutil.copytree(source, stage_root / dirname)

    svg_paths = sorted(stage_root.rglob("*.svg"))
    print(f"Converting {len(svg_paths)} SVG figures to vector PDF one at a time")
    for svg in svg_paths:
        convert_svg(svg, svg.with_suffix(".pdf"))

    for pattern in ["*.md", "*.ipynb", "*.yml"]:
        for source_path in stage_root.rglob(pattern):
            text = source_path.read_text()
            replaced = text.replace(".svg", ".pdf")
            if replaced != text:
                source_path.write_text(replaced)


def generate_latex(stage_root: Path) -> Path:
    stage_temp_root = stage_root / "_build" / "temp"
    stage_temp_root.mkdir(parents=True, exist_ok=True)
    before = {path.resolve() for path in stage_temp_root.glob("myst*") if path.is_dir()}
    MYST_BUILD_LOG.parent.mkdir(parents=True, exist_ok=True)
    with MYST_BUILD_LOG.open("w") as log:
        result = subprocess.run(
            ["npx", "myst", "build", "--pdf"],
            cwd=stage_root,
            text=True,
            stdout=log,
            stderr=subprocess.STDOUT,
            check=False,
        )
    if result.returncode != 0:
        tail = "\n".join(MYST_BUILD_LOG.read_text().splitlines()[-80:])
        raise RuntimeError(f"MyST LaTeX generation failed:\n{tail}")
    return latest_build_dir(stage_temp_root, before)


def convert_assets(build_dir: Path) -> None:
    files_dir = build_dir / "files"
    for gif in files_dir.glob("*.gif"):
        png = gif.with_suffix(".png")
        with Image.open(gif) as image:
            frame = next(ImageSequence.Iterator(image)).convert("RGBA")
            background = Image.new("RGB", frame.size, "white")
            alpha = frame.getchannel("A") if "A" in frame.getbands() else None
            background.paste(frame, mask=alpha)
            background.save(png)

    for svg in files_dir.glob("*.svg"):
        pdf = svg.with_suffix(".pdf")
        convert_svg(svg, pdf)

    # MyST's SVG fallback can produce 16-bit RGBA PNGs whose alpha mask is
    # interpreted as fully transparent by older xdvipdfmx versions. Flatten
    # alpha onto white so diagrams remain visible in the compiled PDF.
    for png in files_dir.glob("*.png"):
        with Image.open(png) as image:
            if "A" not in image.getbands():
                continue
            rgba = image.convert("RGBA")
            background = Image.new("RGB", rgba.size, "white")
            background.paste(rgba, mask=rgba.getchannel("A"))
            background.save(png)


def compile_pdf(build_dir: Path) -> Path:
    LATEX_BUILD_LOG.parent.mkdir(parents=True, exist_ok=True)
    with LATEX_BUILD_LOG.open("w") as log:
        result = subprocess.run(
            [
                "latexmk",
                "-f",
                "-xelatex",
                "-synctex=1",
                "-interaction=batchmode",
                "-file-line-error",
                "notes.tex",
            ],
            cwd=build_dir,
            text=True,
            stdout=log,
            stderr=subprocess.STDOUT,
            check=False,
        )
    pdf = build_dir / "notes.pdf"
    if not pdf.exists():
        tail = "\n".join(LATEX_BUILD_LOG.read_text().splitlines()[-100:])
        raise RuntimeError(
            f"PDF compile failed with exit code {result.returncode}:\n{tail}"
        )
    return pdf


def main() -> int:
    PDF_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="myst-vector-", dir=PDF_TEMP_ROOT) as temp_dir:
        stage_root = Path(temp_dir)
        stage_project(stage_root)
        build_dir = generate_latex(stage_root)
        print("Using build directory:", build_dir)

        last_commit = repo_last_commit()
        title_kind_map = build_title_kind_map()
        convert_assets(build_dir)
        index_asset_dir = build_dir / "assets"
        index_asset_dir.mkdir(exist_ok=True)
        convert_svg(
            ROOT / "assets" / "control-co-design-overview.svg",
            index_asset_dir / "control-co-design-overview.pdf",
        )
        (build_dir / INDEX_TEX_NAME).write_text(build_index_tex(title_kind_map))

        for tex_path in build_dir.glob("*.tex"):
            text = tex_path.read_text()
            if tex_path.name == "notes.tex":
                text = patch_main_tex(text, last_commit)
            else:
                text = patch_included_tex(text, tex_path.name, title_kind_map, build_dir)
            tex_path.write_text(text)

        pdf = compile_pdf(build_dir)
        OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, OUTPUT_PDF)
    print("Wrote", OUTPUT_PDF)
    return 0


if __name__ == "__main__":
    sys.exit(main())
