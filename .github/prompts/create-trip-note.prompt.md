---
agent: agent
description: Draft a new trip-reflection note in photo_book/notes (or photo_book/tips).
---

Read this project to understand its content, context, and style — especially
existing trip notes under [photo_book/notes/](../../photo_book/notes/) such as
[202604_alesund_road_trip.md](../../photo_book/notes/202604_alesund_road_trip.md)
and [202603_luoyang_post_purchase_usage.md](../../photo_book/notes/202603_luoyang_post_purchase_usage.md).
The scoped instructions in
[.github/instructions/trip-notes.instructions.md](../instructions/trip-notes.instructions.md)
will auto-attach.

> For general reference / how-to articles (gear evaluations, technique guides,
> upgrade-decision discussions), use **`/create-article`** instead.

## Spec

- **Target folder:** `photo_book/${input:folder|notes}/`
  (default `notes`; use `tips` if the post-trip *lessons* outweigh the
  narrative — the trip becomes a case study)
- **Filename:** `YYYYMM_location_topic.md`, lowercase with underscores
  (e.g. `202604_alesund_road_trip.md`).
- **Voice:** first-person, narrative, reflective. Reflective asides about
  gear choices and shooting decisions are welcome and on-brand.

## Brief — paste / attach the relevant inputs

Provide whichever of these apply; the agent will weave them in.

### 1. Trip context

- Route / locations, dates, weather, temperature, solo or with companions,
  purpose of the trip.

### 2. Photographic highlights

- A short list of the locations / subjects that mattered most.

### 3. Gear taken — and a one-line verdict per item

For each body / lens / accessory:

- what it was useful for,
- what it wasn't used for and why,
- any specific in-field test or comparison you ran.

### 4. In-field tests or experiments to analyze

For each test, describe:

- methodology (what was compared, at which focal length / aperture / ISO),
- scenarios covered (e.g. bright outdoor / well-lit indoor / poorly-lit indoor),
- results (qualitative or quantitative),
- the question you want answered (e.g. "when is it still worth bringing
  both cameras?").

### 5. Color grading / post-processing reflections

- Which existing presets in
  [color_grading.md](../../photo_book/tips/color_grading.md) worked or
  didn't, and why (lighting, weather, subject mix, tonal range…).
- Any **candidate new preset scheme** you want evaluated. The article should
  assess feasibility and suggest fine-tuning parameters (white balance,
  exposure, contrast, highlights / shadows, saturation, vibrance, etc.).

### 6. Open questions

- Anything you want the article to explicitly leave for future trips to
  answer.

## Article requirements

1. **Tone:** first-person narrative, even when the article lives in `tips/`.
2. Use **H1 for the title** and **H2/H3 for sections** — stay within H1–H3
   so MyST anchors remain stable under `myst_heading_anchors: 3`.
3. Recommended section skeleton (adapt as needed):
   - **TL;DR** — one short paragraph
   - **Trip context** (route, weather, dates, solo/with whom)
   - **Photographic highlights** (per location)
   - **Gear-by-gear verdicts** (preferably as a table + per-item prose)
   - **In-field tests & analysis** (one subsection per test, with a
     conclusion)
   - **Color grading reflections** (evaluate existing presets; if a new
     scheme was proposed, give a feasibility verdict + suggested parameters,
     ideally as a table)
   - **Lessons learned**
   - **Open questions**
4. **Cross-link** to related chapters with `` {doc}`...` `` and to anchors
   with `` {ref}`...` ``. Likely candidates:
   - [color_grading.md](../../photo_book/tips/color_grading.md)
   - [lens_recommendation.md](../../photo_book/gears/lens_recommendation.md)
   - sibling trip notes under [photo_book/notes/](../../photo_book/notes/).
5. **Fact-check** dates, place names, gear specs, and focal lengths against
   repo files first ([camera_crop_factors.yaml](../../camera_crop_factors.yaml),
   focal-length reports, prior notes); cite external sources inline if used.
6. **Register the new file** in
   [photo_book/_toc.yml](../../photo_book/_toc.yml) under the `Notes` caption
   (or `Tips`, if the article lives in `tips/`), in chronological order.
7. **Do not invent figures.** Leave a `TODO` placeholder (HTML comment)
   wherever an image from [photo_book/pics/](../../photo_book/pics/) would
   belong.
8. **Preserve mixed-language content** (Chinese place names, Norwegian
   terms, English narration) exactly as it appears in the brief.
9. **No invented subjective claims.** The first-person voice invites reflective
   asides about gear and shooting decisions — those are welcome — but do not
   manufacture reactions, surprises, superlatives, or value judgements ("this
   surprised me most", "more than I expected", "the single most useful thing I
   learned", "my favourite") that the brief did not supply. When no reaction was
   given, report the fact or decision neutrally (see the *Claims and voice*
   rules in [photobook.instructions.md](../instructions/photobook.instructions.md)).

## At the end of your response, summarize

- the new file path,
- the `_toc.yml` change,
- any analysis conclusions the reader should sanity-check (especially for
  in-field tests and proposed color-grading presets),
- any open questions or assumptions worth verifying.
