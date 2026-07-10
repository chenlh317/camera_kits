---
agent: agent
description: Draft a new reference / how-to article in photo_book/gears or photo_book/tips.
---

Read this project to understand its content, context, and style — especially
the Jupyter Book under [photo_book/](../../photo_book/). Pay attention to:

- Existing chapters in
  [photo_book/gears/](../../photo_book/gears/) and
  [photo_book/tips/](../../photo_book/tips/) for tone, depth, and formatting.
- [photo_book/_config.yml](../../photo_book/_config.yml) and
  [photo_book/_toc.yml](../../photo_book/_toc.yml) for MyST settings and how
  chapters are registered.
- The scoped instructions under [.github/instructions/](../instructions/)
  (PhotoBook conventions auto-attach).

> For trip reflections / narrative write-ups, use **`/create-trip-note`**
> instead — that prompt is optimized for the trip-reflection pattern.

Then create a **new article** with the following spec:

- **Target folder:** `photo_book/${input:folder|tips}/` (`gears` or `tips`)
- **Topic:** ${input:topic:What is the article about?}
- **Filename:** descriptive lowercase with underscores
  (e.g. `astrophotography_planetary.md`).

## Brief — paste / attach the relevant inputs

The agent should weave whichever of these you provide into the article:

- **Reference files in the repo** to draw from (e.g. `chat.md`, prior gear
  pages, focal-length reports). Treat these as primary source material;
  quote or paraphrase as appropriate.
- **Current gear** — be specific (model names, focal lengths, mounts,
  accessories owned vs. *not* owned).
- **Open questions / decisions** the article should resolve, e.g.
  - "Do I need a Barlow lens? How would I use it? What image-quality gain?"
  - "What would I gain by upgrading from X to Y or Z?"
- **Location / environmental context** that affects the topic (latitude,
  climate, seasonal daylight, light pollution, etc.).
- **My skill level** so recommendations are calibrated
  (beginner / amateur / intermediate / advanced).

## Article requirements

1. **Match the surrounding tone** — analytical and reference-style. Read
   1–2 sibling articles before drafting.
2. Use **H1 for the title** and **H2/H3 for sections** — stay within H1–H3
   so MyST anchors remain stable under `myst_heading_anchors: 3`.
3. Open with a short **TL;DR / quick-take** near the top.
4. Where relevant, include:
   - a **comparison table** when discussing upgrade options or alternatives,
   - **practical "how to use"** subsections for techniques or accessories,
   - **caveats / when not to** sections to keep recommendations honest.
5. **Cross-link** to related chapters with `` {doc}`...` `` and to anchors
   with `` {ref}`...` ``. Likely candidates:
   - [lens_recommendation.md](../../photo_book/gears/lens_recommendation.md)
   - [prime_lens_recommendation.md](../../photo_book/gears/prime_lens_recommendation.md)
   - [color_grading.md](../../photo_book/tips/color_grading.md)
6. **Fact-check** claims against repo files first
   ([camera_crop_factors.yaml](../../camera_crop_factors.yaml), gear pages,
   focal-length reports), then reputable external sources; cite external
   sources inline.
7. **Register the new file** in
   [photo_book/_toc.yml](../../photo_book/_toc.yml) under the appropriate
   `caption` (Gears / Tips), in a sensible position relative to siblings.
8. **Do not invent figures** or reference images that don't exist in
   [photo_book/pics/](../../photo_book/pics/). Leave a `TODO` placeholder
   (HTML comment) where an image is needed.
9. **Preserve mixed-language content** as it appears in the brief — do not
   translate or transliterate without being asked.
10. **No invented subjective claims.** Do not add personal reactions,
    surprises, superlatives, or value judgements ("this surprised me most",
    "more than I expected", "the single most useful thing I learned", "my
    favourite") unless the brief explicitly supplied them. When no reaction was
    given, state the observable fact or the reasoning neutrally and let it stand
    on its own (see the *Claims and voice* rules in
    [photobook.instructions.md](../instructions/photobook.instructions.md)).

## At the end of your response, summarize

- the new file path,
- the `_toc.yml` change,
- any open questions or assumptions the reader should verify.
