---
applyTo: "**/*.py"
description: Conventions for the Python EXIF / focal-length tooling at the repo root.
---

# Python tooling instructions

These scripts analyze a personal photo library on Windows and write timestamped
reports. Follow the patterns already established in
[analyze_focal_lengths.py](../../analyze_focal_lengths.py),
[extract_camera_crop_factors.py](../../extract_camera_crop_factors.py), and
[filter_photos_by_focal_length.py](../../filter_photos_by_focal_length.py).

## Environment

- Python 3 with the pinned dependencies in
  [requirements.txt](../../requirements.txt). Do not bump versions casually —
  `jupyter-book==1.0.3` is held back intentionally (later 2.x versions cause
  EISDIR build errors).
- Activate the local venv before running scripts:
  `& .venv\Scripts\Activate.ps1` (PowerShell).

## Config files

- Read folder lists and camera data from YAML using `pyyaml`.
- Preserve the **comment-driven enable/disable** pattern in
  [photo_folders.yaml](../../photo_folders.yaml): lines starting with `#` are
  treated as disabled entries; never silently strip or rewrite them.
- When updating [camera_crop_factors.yaml](../../camera_crop_factors.yaml),
  keep the existing key ordering and grouping comments intact.

## EXIF handling

- Use Pillow's `Image.getexif()` plus the EXIF sub-IFD (`get_ifd(IFD.Exif)`) for
  fields like `FocalLength` and `FocalLengthIn35mmFilm` — see
  `get_exif_data()` in [analyze_focal_lengths.py](../../analyze_focal_lengths.py).
- Treat missing or unreadable EXIF as a soft skip with a logged warning; do not
  raise.

## Output conventions

- Write outputs to **timestamped** sibling directories using
  `datetime.now().strftime("%Y%m%d_%H%M%S")`, matching `focal_length_analysis_*`
  and `filtered_photos_*`. Never overwrite a previous run.
- Mirror console output to a report file using a `Tee`-style helper rather than
  duplicating `print` calls.

## Paths

- Photo libraries live on `D:\` and `F:\`. Use `pathlib.Path` and accept
  Windows-style paths from YAML as-is.
- Do not hard-code absolute paths in scripts — they belong in the YAML configs.
