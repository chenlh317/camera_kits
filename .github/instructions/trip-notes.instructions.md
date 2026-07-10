---
applyTo: "photo_book/notes/**/*.md"
description: Tone and structure for personal trip notes.
---

# Trip notes instructions

Files under [photo_book/notes/](../../photo_book/notes/) are personal,
narrative trip write-ups (e.g.
[202604_alesund_road_trip.md](../../photo_book/notes/202604_alesund_road_trip.md)).
They are *not* reference docs — match the existing voice.

## Naming

- Use `YYYYMM_location_topic.md`, lowercase with underscores
  (`202603_luoyang_post_purchase_usage.md`,
  `202604_alesund_road_trip.md`).
- After adding a new note, register it in
  [photo_book/_toc.yml](../../photo_book/_toc.yml) under the `Notes` caption,
  in chronological order.

## Voice and structure

- First-person, narrative, chronological. Reflective asides about gear choices
  and shooting decisions are welcome and on-brand — but *reflective* is not the
  same as *invented*. Do not put subjective reactions, surprises, or
  superlatives in the user's mouth (e.g. "this surprised me most", "more than I
  expected", "the single most useful thing I learned"). Only include such
  claims when the user actually supplied them; otherwise report the fact or
  decision neutrally. See the *Claims and voice* rules in
  [photobook.instructions.md](../../.github/instructions/photobook.instructions.md).
- Use H2 sections for days or major segments of the trip; H3 for sub-locations
  or themes. Stay within H1–H3 so MyST anchors remain stable.
- Inline figures with captions (`figure` directive) referencing
  [photo_book/pics/](../../photo_book/pics/). Photos generally illustrate the
  paragraph immediately above them.

## Content

- Preserve mixed-language content (Chinese place names, Norwegian terms,
  English narration) as it appears — do not translate or transliterate without
  being asked.
- Fact-check dates, place names, gear names, and focal lengths against:
  - [camera_crop_factors.yaml](../../camera_crop_factors.yaml)
  - matching `focal_length_analysis_*/` reports
  - other notes in this folder
  before turning to the web.
- It is fine — and often desirable — to link out to gear pages
  (`` {doc}`/gears/lens_recommendation` ``) when discussing lens choice.
