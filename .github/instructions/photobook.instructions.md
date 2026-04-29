---
applyTo: "photo_book/**/*.md"
description: MyST / Jupyter Book conventions for PhotoBook content.
---

# PhotoBook (Jupyter Book) instructions

PhotoBook is built with [jupyter-book 1.0.3](https://jupyterbook.org/) using
MyST Markdown. Configuration lives in
[photo_book/_config.yml](../../photo_book/_config.yml) and the table of
contents in [photo_book/_toc.yml](../../photo_book/_toc.yml).

## Headings and anchors

- `myst_heading_anchors: 3` is set, so H1–H3 produce stable auto-generated
  anchor IDs. Reference them with `` {ref}`Label <anchor-id>` ``.
- Keep heading wording stable once anchors are referenced from elsewhere
  (`index.md` quick-links, sibling chapters). If you must rename a heading,
  search the whole `photo_book/` tree for the old anchor and update every
  reference.

## Roles and directives

- Cross-references: `` {ref}`...` `` for headings, `` {doc}`...` `` for whole
  files, `` {numref}`...` `` for numbered figures/tables.
- Diagrams: use `sphinxcontrib-mermaid` fenced blocks (` ```{mermaid} `).
- Images: store under [photo_book/pics/](../../photo_book/pics/) and embed via
  the `figure` directive so they get captions and numbering.

## Table of contents

- When adding a new chapter, register it in
  [photo_book/_toc.yml](../../photo_book/_toc.yml) under the appropriate
  `caption` (Gears / Tips / Notes).
- File paths in `_toc.yml` are relative to `photo_book/` and omit the `.md`
  extension.

## Validation

- After non-trivial edits, run [build_photo_book.bat](../../build_photo_book.bat)
  and check the output for warnings (broken refs, duplicate labels, missing
  images).
- Do not edit anything under `photo_book/_build/` — it is regenerated.

## Style

- Gear pages (`gears/`) and tips (`tips/`) are analytical / reference-style:
  prefer tables, bullet lists, and numbered steps.
- Preserve mixed-language content (Chinese, English, Norwegian, etc.) as-is.
