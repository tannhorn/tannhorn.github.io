#!/usr/bin/env python3
"""Render TeX files from YAML data and Jinja2 templates."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

try:
    import jinja2  # type: ignore
except ImportError:  # pragma: no cover
    jinja2 = None
try:
    import pypandoc  # type: ignore
except ImportError:  # pragma: no cover
    pypandoc = None


def latex_escape(text: str) -> str:
    if text is None:
        return ""
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text


def date_range_to_latex(text: str) -> str:
    if text is None:
        return ""
    return text.replace(" to ", " -- ")


def simple_md_to_latex(text: str) -> str:
    if text is None:
        return ""
    # Convert Markdown emphasis.
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<!\*)\*(.+?)\*", r"\\emph{\1}", text)
    # Wrap bare URLs.
    text = re.sub(r"(https?://\S+)", r"\\url{\1}", text)
    return latex_escape(text)


def md_to_latex(text: str, pandoc_path: str | None, use_pypandoc: bool) -> str:
    if text is None:
        return ""
    if use_pypandoc and pypandoc is not None:
        try:
            return pypandoc.convert_text(text, "latex", format="markdown").strip()
        except (RuntimeError, OSError):  # pragma: no cover
            return simple_md_to_latex(text)
    if pandoc_path:
        try:
            result = subprocess.run(
                [pandoc_path, "-f", "markdown", "-t", "latex"],
                input=text,
                text=True,
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            return simple_md_to_latex(text)
        return result.stdout.strip()
    return simple_md_to_latex(text)


def load_yaml(path: Path) -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML is not installed.")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return data or {}


def load_front_matter(path: Path) -> dict:
    if yaml is None:
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def build_site_context(root: Path) -> dict:
    config = {}
    index_meta = {}
    if (root / "_config.yml").exists() and yaml is not None:
        config = load_yaml(root / "_config.yml")
    if (root / "index.md").exists():
        index_meta = load_front_matter(root / "index.md")

    url = (config.get("url") or "").rstrip("/")
    baseurl = (config.get("baseurl") or "").rstrip("/")
    website = url + baseurl if url else index_meta.get("consulting_url", "")

    return {
        "email": config.get("email", ""),
        "website": website,
        "linkedin": index_meta.get("linkedin_url", ""),
        "orcid": index_meta.get("orcid_url", ""),
        "tagline": config.get("tagline", ""),
    }

def format_url_display(url: str) -> str:
    display = re.sub(r"^https?://", "", url or "")
    return display.rstrip("/")


def build_contact_lines(site: dict) -> dict:
    def link(url: str, icon: str) -> str:
        display = format_url_display(url)
        icon_part = f"{icon}\\ " if icon else ""
        return r"%s\href{%s}{%s}" % (icon_part, url, display)

    primary = []
    secondary = []

    email = site.get("email")
    if email:
        primary.append(r"\faEnvelope\ \href{mailto:%s}{%s}" % (email, email))
    if site.get("website"):
        primary.append(link(site["website"], r"\faGlobe"))
    if site.get("linkedin"):
        secondary.append(link(site["linkedin"], r"\faLinkedin"))
    if site.get("orcid"):
        secondary.append(link(site["orcid"], r"\faOrcid"))

    separator = r" \textbar\textbar\ "
    return {
        "primary": separator.join(primary),
        "secondary": separator.join(secondary),
    }


def render_templates(root: Path) -> int:
    if yaml is None:
        print("PyYAML is not installed. Install it to render TeX (pip install pyyaml).")
        return 1
    if jinja2 is None:
        print("Jinja2 is not installed. Install it to render TeX (pip install jinja2).")
        return 1

    data_dir = root / "_data"
    cv_data = load_yaml(data_dir / "cv.yml")
    publications_data = load_yaml(data_dir / "publications.yml")
    site = build_site_context(root)

    pandoc_path = shutil.which("pandoc")
    use_pypandoc = pypandoc is not None
    if pandoc_path is None and not use_pypandoc:
        print("pandoc not found; Markdown fields will use a minimal LaTeX conversion.")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(root / "tex" / "templates")),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["latex_escape"] = latex_escape
    env.filters["date_range_to_latex"] = date_range_to_latex
    env.filters["md_to_latex"] = lambda text: md_to_latex(text, pandoc_path, use_pypandoc)
    env.filters["url_display"] = format_url_display

    out_dir = root / "tex" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    contact_lines = build_contact_lines(site)
    context = {
        "cv": cv_data,
        "publications": publications_data,
        "site": site,
        "contact_line_primary": contact_lines["primary"],
        "contact_line_secondary": contact_lines["secondary"],
    }

    for name, output in (("cv.tex.j2", out_dir / "cv.tex"), ("publications.tex.j2", out_dir / "publications.tex")):
        template = env.get_template(name)
        rendered = template.render(**context)
        output.write_text(rendered, encoding="utf-8")
        print(f"Rendered {output}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Render TeX files from YAML data.")
    parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    try:
        return render_templates(root)
    except RuntimeError as exc:
        print(str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
