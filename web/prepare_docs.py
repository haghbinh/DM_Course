"""Copy the notes into docs/ for the MkDocs website.

The notes stay in their Obsidian folders. This script copies the Part folders,
img/ and the teaching plan into docs/, makes README.md the home page and turns
Obsidian-only syntax (wikilinks and embedded images) into standard Markdown.
Code blocks and inline code are left untouched. Callouts (> [!note]) are
handled by the mkdocs-callouts plugin; the rest by web/hooks.py.
"""
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

if DOCS.exists():
    shutil.rmtree(DOCS)
DOCS.mkdir()

for item in ROOT.iterdir():
    if item.name.startswith("Part ") or item.name in ("img", "Teaching Plan.md"):
        if item.is_dir():
            shutil.copytree(item, DOCS / item.name)
        else:
            shutil.copy2(item, DOCS / item.name)

assets = DOCS / "assets"
assets.mkdir()
for name in ("extra.css", "mathjax.js"):
    shutil.copy2(ROOT / "web" / name, assets / name)

# README becomes the home page (without the GitHub-only RTL <div> wrapper)
readme = (ROOT / "README.md").read_text(encoding="utf-8")
readme = re.sub(r'^<div dir="rtl">\s*$|^</div>\s*$', "", readme, flags=re.M)
# folder links and notebooks open on GitHub (the site has no folder pages;
# GitHub renders notebooks)
GITHUB = "https://github.com/haghbinh/DM_Course"
readme = re.sub(r"\]\(((?:Part%20|img)[^)#]*?)\)",
                lambda m: f"]({GITHUB}/{'blob' if m.group(1).endswith('.ipynb') else 'tree'}/main/{m.group(1)})"
                if not m.group(1).endswith(".md") else m.group(0), readme)
(DOCS / "index.md").write_text(readme, encoding="utf-8")

# Remove Dropbox conflicted copies
for p in list(DOCS.rglob("*conflicted copy*")):
    p.unlink()

# Index every file by name (and by name without .md) for wikilink lookup
index = {}
for p in DOCS.rglob("*"):
    if p.is_file():
        index.setdefault(p.name, p)
        if p.suffix == ".md":
            index.setdefault(p.stem, p)


def link_to(target: Path, src: Path) -> str:
    rel = os.path.relpath(target, src.parent).replace(os.sep, "/")
    return quote(rel)


def slug(heading: str) -> str:
    # Close to Python-Markdown's default toc slugify for Persian text
    s = re.sub(r"[^\w\s-]", "", heading).strip().lower()
    return re.sub(r"[\s-]+", "-", s)


WIKI = re.compile(r"(!?)\[\[([^\[\]\n]+?)\]\]")


def convert(text: str, src: Path) -> str:
    def repl(m):
        embed, inner = m.group(1), m.group(2)
        target, _, alias = inner.partition("|")
        name, _, heading = target.partition("#")
        name = name.strip()
        found = (index.get(name) or index.get(name + ".md")) if name else src
        if found is None:
            return m.group(0)  # unknown target: leave as is
        url = link_to(found, src) if name else ""
        if heading:
            url += "#" + slug(heading)
        if embed:
            attrs = ""
            if alias.strip().isdigit():
                attrs = '{ width="%s" }' % alias.strip()
            return f"![{name}]({url}){attrs}"
        label = alias.strip() or (heading.strip() if not name else
                                  re.sub(r"^[0-9۰-۹]+\s*-\s*", "", name))
        return f"[{label}]({url})"

    out, in_fence, fence = [], False, ""
    for line in text.split("\n"):
        stripped = line.lstrip("> ").lstrip()
        fm = re.match(r"(`{3,}|~{3,})", stripped)
        if fm:
            if not in_fence:
                in_fence, fence = True, fm.group(1)
            elif stripped.startswith(fence):
                in_fence = False
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        parts = re.split(r"(`+[^`]*`+)", line)  # protect inline code spans
        parts = [p if p.startswith("`") else WIKI.sub(repl, p) for p in parts]
        out.append("".join(parts))
    return "\n".join(out)


for md in DOCS.rglob("*.md"):
    md.write_text(convert(md.read_text(encoding="utf-8"), md), encoding="utf-8")

print("docs/ prepared:", sum(1 for _ in DOCS.rglob("*.md")), "markdown files")
