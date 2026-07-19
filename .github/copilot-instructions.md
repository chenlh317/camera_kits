# Copilot Instructions — camera_kits

This repository combines Python utilities for analyzing a personal photo
library (by EXIF focal length, camera, and crop factor) with a
[Jupyter Book](https://jupyterbook.org/) ("PhotoBook") that documents gear
notes, lens recommendations, and trip write-ups.

This file holds **repo-wide** guidance only. Scoped conventions live under
[.github/instructions/](./instructions/) and auto-attach via `applyTo` globs:

- [python-tooling.instructions.md](./instructions/python-tooling.instructions.md) — `**/*.py`
- [photobook.instructions.md](./instructions/photobook.instructions.md) — `photo_book/**/*.md`
- [trip-notes.instructions.md](./instructions/trip-notes.instructions.md) — `photo_book/notes/**/*.md`

## Repository layout

- **Python tooling** (root):
  - [analyze_focal_lengths.py](../analyze_focal_lengths.py) — scans folders
    listed in [photo_folders.yaml](../photo_folders.yaml), reads EXIF, and
    writes per-folder reports into a timestamped
    `focal_length_analysis_YYYYMMDD_HHMMSS/` directory.
  - [extract_camera_crop_factors.py](../extract_camera_crop_factors.py) —
    maintains [camera_crop_factors.yaml](../camera_crop_factors.yaml).
  - [filter_photos_by_focal_length.py](../filter_photos_by_focal_length.py) —
    copies matching photos into `filtered_photos_*` folders.
  - [build_photo_book.bat](../build_photo_book.bat) — builds the Jupyter Book.
  - [requirements.txt](../requirements.txt) — pinned dependencies.
- **PhotoBook content** ([photo_book/](../photo_book/)):
  - `index.md`, `_config.yml`, `_toc.yml` — Jupyter Book entry points.
  - `gears/`, `notes/`, `tips/`, `pics/` — chapter sources and figures.
- **Generated artifacts** (do not hand-edit):
  - `focal_length_analysis_*/` — analysis reports.
  - `filtered_photos_*/` — copied photo subsets.
  - `photo_book/_build/` — built site.

## General principles

- Prefer **fact-checking against files already in the repo** (gear pages, trip
  notes, YAML configs, focal-length reports) before consulting the web. Cite
  external sources inline when you do use them.
- Keep paths Windows-friendly — the user's photo libraries live on `D:\` and
  `F:\`.
- Match the surrounding tone of whatever file you are editing.
- Preserve mixed-language content (Chinese, English, Norwegian, etc.) as-is.
- Never label a summary "TL;DR" — use "Summary" instead.

## Reusable prompts

Common multi-step editing workflows are stored as prompt files under
[.github/prompts/](./prompts/). Invoke them from Copilot Chat with `/`
(e.g. `/fact-check-and-polish`) rather than re-typing the instructions.
