#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
from datetime import datetime
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

# optional typography: smartypants
try:
    import smartypants
    TYPOGRAPHY = True
except Exception:
    TYPOGRAPHY = False

ROOT = Path(__file__).parent.resolve()
SRC = ROOT / "site-src"
TEMPLATES = ROOT / "theme" / "templates"
ASSETS_SRC = ROOT / "theme" / "assets"
BUILD = ROOT / "build"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(['html', 'xml'])
)

def ensure_build_dirs():
    (BUILD / "assets" / "css").mkdir(parents=True, exist_ok=True)
    (BUILD / "assets" / "js").mkdir(parents=True, exist_ok=True)

def copy_assets():
    dst_assets = BUILD / "assets"
    if dst_assets.exists():
        shutil.rmtree(dst_assets)
    shutil.copytree(ASSETS_SRC, dst_assets)

def render_pages():
    template = env.get_template('base.html')
    files = list(SRC.glob("*.md"))
    if not files:
        print("Нет markdown файлов в site-src/")
        return
    for mdfile in files:
        post = frontmatter.load(mdfile)
        html_body = markdown.markdown(
            post.content,
            extensions=[
                'fenced_code',
                'tables',
                'codehilite'
            ]
        )
        if TYPOGRAPHY:
            html_body = smartypants.smartypants(html_body)
        meta = post.metadata or {}
        site_meta = {
            "title": meta.get("site_title", None) or "Мой сайт",
            "author": meta.get("author", None)
        }
        now = datetime.utcnow()
        rendered = template.render(content=html_body, meta=meta, site=site_meta, now=now)
        out_path = BUILD / f"{mdfile.stem}.html"
        out_path.write_text(rendered, encoding="utf-8")
        print(f"Rendered {mdfile.name} -> {out_path}")

def main():
    ensure_build_dirs()
    copy_assets()
    render_pages()
    print("Готово: сгенерированы html-страницы в build/ (далее — npm run build для сборки статики и минификации).")
    if TYPOGRAPHY:
        print("Типографика (smartypants) включена.")
    else:
        print("Типографика (smartypants) НЕ установлена — можно установить `pip install smartypants` для улучшений.")

if __name__ == "__main__":
    main()
