# PyWeb_Task2.2 — Кастомизация статического сайта

## [Посмотреть сайт](https://kekachy.github.io/PyWeb_Task2.2/)

## О проекте
Реализована собственная тема (header, footer, стилизованная главная страница).  
Сайт генерируется из Markdown файлов (site-src/*.md) в HTML через Jinja2 (скрипт `build.py`), после чего выполняется сборка статики: PostCSS для CSS, terser для JS; HTML минифицируется и валидируется. CI реализован через GitHub Actions; деплой — на GitHub Pages.

## Что сделано (требования задания)
- Кастомная тема: `theme/templates/*` (header, footer, базовый шаблон).
- Метаданные: title, description, author — в meta-тегах шаблона.
- Сборка статики: PostCSS (autoprefixer, cssnano) — `npm run build:css`.
- Минификация JS: terser — `npm run build:js`.
- Генерация HTML: `python build.py` (markdown → Jinja2).
- Минификация HTML: `html-minifier-terser` (`npm run minify:html`).
- Валидация HTML: `html-validate` (`npm run validate:html`).
- CI/CD: `.github/workflows/ci.yml` — рендер, сборка, валидация, деплой на `gh-pages`.

## Как запустить локально (Windows / Linux / macOS)
1. Клонировать репозиторий:
```bash
git clone https://github.com/KEKACHY/PyWeb_Task2.2.git
cd PyWeb_Task2.2
```
2. Установить Python-зависимости:
```bash
python -m pip install -r requirements.txt
```
3. Установить Node.js (если не установлен) и зависимости:
```bash
npm ci
```
4. Сгенерировать HTML из Markdown:
```bash
python build.py
```
5. Собрать статику и минифицировать:
```bash
npm run build
```
6. Открыть build/index.html в браузере.
