---
agent: agent
description: Restructure an article so its sections are well-organized and flow logically.
---

Review the active article and ensure that all of its sections are well-structured
and logically organized.

Specifically:

- Check for clear, descriptive **headings and subheadings** at consistent levels
  (respect `myst_heading_anchors: 3` from
  [photo_book/_config.yml](../../photo_book/_config.yml) — H1–H3 produce stable
  anchors).
- Ensure a **logical flow of information** that guides the reader from overview
  to detail (e.g. context → comparison → recommendation → caveats).
- Promote, demote, merge, or split sections as needed; update the article's
  quick-links / table-of-contents block to match.
- Update [photo_book/_toc.yml](../../photo_book/_toc.yml) if the article's
  position or filename in the book changes.
- Preserve all factual content; this prompt is about structure and flow, not
  rewriting prose. If you do rephrase for clarity, keep the original meaning and
  voice.

At the end, list the structural changes you made (sections moved, renamed,
merged, or split) so the diff is easy to review.
