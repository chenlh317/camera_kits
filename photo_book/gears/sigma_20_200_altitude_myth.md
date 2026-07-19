# The Sigma 20-200mm "Altitude Sickness" Claim: An Evidence Check

A circulating claim in the Chinese-language photography community holds that the
[Sigma 20-200mm f/3.5-6.3 DG DN Contemporary](https://www.sigma-global.com/en/lenses/c025_20_200_35_63/)
goes soft — "blurry from near to far" — once you take it to high altitude. This
chapter examines that claim against the sample photos that are usually cited,
against basic optics and physics, and against how the evidence has actually been
presented. It is a reasoning exercise, not an accusation about any specific
person.

```{admonition} Summary
:class: tip
The "sample photos" behind this claim do not survive scrutiny. Their softness is
fully explained by heavy crop-and-upscale, motion blur at the long end, and
atmospheric haze over distance — not by any lens defect. The proposed mechanism
("the barrel is too airtight to cope with air-pressure change") is physically
impossible for a zoom lens. And a genuine *optical* defect would be reproducible
worldwide, yet no authoritative outlet has ever reproduced it. Absent raw files,
EXIF, and controlled testing, the claim does not rise to the level of usable
negative information.
```

```{contents}
:depth: 4
```

## What the claim says

The narrative has a few stable, recognisable ingredients:

- The lens is said to become soft specifically **at high altitude** (typically
  the Tibetan Plateau / Qinghai-Gansu high country).
- The failure is described as **uniform** — "every shot on the trip was blurry",
  often "only noticed after getting home".
- A **pseudo-scientific mechanism** is offered: the lens groups are "sealed too
  well", so the barrel "cannot adapt to the pressure change" at altitude, and the
  image degrades. The catchy shorthand used is the lens catching *"altitude
  sickness"* (镜头"高反").
- The discussion is **confined to one language market**; no non-Chinese outlet
  or reviewer discusses it.

Each ingredient matters, because each is testable.

## Reading the sample photos

The images most often passed around fall into two groups, and the split between
them is the single most informative thing about the whole set.

**The full-frame originals are actually sharp.** A wide salt-lake / Yardang
landscape, a snow-mountain-and-tent scene, and a glacier-with-figure shot all
resolve fine detail normally — ridge texture, rock strata, water ripples, and
distant terrain are all distinguishable, with normal colour and contrast. A lens
that had "failed at altitude" could not produce these on the same trip with the
same body.

**The "problem" images are almost all extreme crops.** The pictures labelled as
proof — a dancing figure by the water, an arm close-up, a person against a
glacier — are small regions cropped out of already-compressed uploads and then
enlarged to fill the frame. Their softness is what you get when you magnify a
limited number of pixels together with the JPEG compression artefacts. Any lens,
including the very best, looks like this when you crop this hard into a
social-platform re-compression.

Broken down by cause, in rough order of contribution:

| Observation in the "problem" shots                                 | Most likely cause                                                                                             | Points to a lens defect?             |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Soft, "mushy", jelly-edged detail                                  | Extreme crop-and-upscale of a re-compressed upload                                                            | No                                   |
| A moving subject smeared while the static background stays sharper | Motion blur / camera shake — slow shutter at the long end                                                     | No                                   |
| Low-contrast, hazy distant subjects (glacier, snow peak)           | Long-range telephoto through atmosphere: localized water vapour / mist over ice and water, plus residual haze | No — environmental, affects any lens |
| Slight smearing / edge halos                                       | Platform re-compression plus denoise/sharpen post-processing                                                  | No                                   |

Crucially, none of the real **fingerprints** of an optical defect appear:

- **Decentering** would show one side of the frame soft and the other sharp,
  consistently across images. It does not appear — the wide originals are even
  across the frame.
- **Field curvature / corner softness** would show a sharp centre with a regular
  fall-off to the corners. The softness here tracks *which region was enlarged*,
  not position in the frame.
- **Uniformly soft across all originals** would be the signature of a genuinely
  poor copy. The opposite is true: multiple full-frame originals are sharp.
- **Runaway lateral CA / purple fringing** on high-contrast edges is not
  systematically present.

So the dominant "blur" was largely *manufactured after capture* by cropping and
enlarging a re-compressed upload, with additional, genuinely-captured
contributions from motion (shake / moving subjects) and atmosphere. None of it
requires — or points to — a lens defect.

```{admonition} Sample photos
:class: note
The circulating "sample" images discussed here are available as a download:
{download}`sample_pics.zip <sample_pics.zip>`. They carry third-party
watermarks / platform IDs and are provided only so the "sharp full-frame
original vs. soft extreme-crop" contradiction can be inspected first-hand.
```

### Could it be deliberate defocus?

A soft "sample" is trivial to manufacture with a perfectly healthy lens: stop
down to about f/8, switch to manual focus, and rack the focus ring past the
infinity hard-stop without dialling back. Modern focus-by-wire lenses deliberately
focus *beyond* true infinity (to allow for thermal expansion and calibration
margin), so the focal plane ends up behind everything in the scene and near *and*
far go soft at once. This matters as an epistemic point: a blurry frame proves
almost nothing, because a good copy can be *made* to look "defective" on demand.

But do the circulating samples actually look like beyond-infinity defocus? **No** —
and the distinction is worth drawing, because defocus has a specific, recognisable
signature that these images do *not* match:

| Defocus (past infinity) would show                                        | The samples actually show                                                                                                                        |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Global, uniform** softness — every distance out of focus together       | Several full-frame originals are properly sharp (salt-lake, snow-mountain tent, turret house, figure on the salt flat)                           |
| **Isotropic** blur — points spread into round discs, edge halos symmetric | **Directional** streaks — arms with doubled outlines pulled one way, ground smeared along the direction of travel                                |
| **No moving-vs-static distinction** — everything equally soft             | Static subjects **sharp**, movers **soft** in the same frame (the house's roof tiles and window frame are crisp while the girl beside it smears) |

Two of these are decisive. The **directional streaking** is the fingerprint of
*motion*, not focus (defocus is non-directional). And the **static-sharp /
mover-soft** frame is self-refuting for any whole-image defocus: if the lens were
focused behind the scene, the house would be exactly as blurred as the girl —
since it is not, the lens *was* focused correctly.

So the two arguments are separate and both hold: deliberate defocus shows that
*"blurry ≠ defective lens,"* while the specific circulating images fail to
implicate the lens for a *different* reason — motion blur, extreme crop-and-upscale,
and atmospheric haze, exactly as catalogued in the table above.

## Why altitude (almost) cannot blur a lens

The proposed mechanism is the weakest link, and it fails on basic physics.

- **A zoom lens is not sealed — it is effectively an air pump.** A 20-200mm
  superzoom changes internal volume dramatically as the barrel extends and
  retracts; air is drawn in and pushed out as you zoom (many lenses have
  dedicated venting / dust structures for exactly this). "Too airtight" is
  self-contradictory for a lens that breathes air to zoom.
- **Even if it were sealed, the pressure difference cannot blur glass.** At
  ~4000 m the pressure is roughly 60% of sea level. That differential acting on
  rigid glass elements will not deform their surface figure enough to affect
  resolution — glass is not a balloon. Any pressure load is on the barrel shell,
  not on optical focus.
- **What actually changes with altitude is temperature, not image-forming
  pressure.** Cold affects battery life, grease feel, and mechanical tolerances —
  none of which produce "whole-frame double-imaging and blown highlights".
- **Thin, dry high-altitude air is usually *clearer* overall,** with less haze and
  water vapour, so distant subjects tend to be *more* crisp, not less. (The
  exception is extreme-telephoto shots across many kilometres — or across ice and
  water, where local vapour and mist linger — which is exactly the
  environmental, lens-agnostic softness noted in the table above.)

"Altitude sickness" is a metaphor for people, retrofitted onto a lens. It is
technobabble: memorable, easy to spread, and unfalsifiable — but it does not
describe a real optical mechanism. A real defect is discussed in concrete,
measurable terms (decentering, field curvature, dispersion, an MTF drop at a
specific focal length and aperture), not a poetic analogy.

## Why "worldwide silence" is the strongest tell

Optics do not respect borders. If "high altitude → sealed groups → blur" were a
real optical phenomenon, it would be reproducible everywhere: the Andes, the
Himalaya, the Alps, Colorado, Bolivia. Outlets that run standardized optical
tests or large-sample failure data — DPReview, LensTip, teardown channels, and
especially rental-house statistics like LensRentals — would have something to
say. Instead the phenomenon exists only inside a single language market and
vanishes outside it.

A "defect" that appears only in one language community is more naturally a
**market phenomenon than a physical one.** Physics does not pick a language;
marketing campaigns do.

## Astroturfing vs. genuine feedback: how to tell them apart

Once a claim looks more like a market phenomenon than a physical one, a fair
question follows: how would you distinguish *organized smearing* (有组织抹黑) from
ordinary negative feedback? This section is deliberately **general** — it is a
way of reasoning about any suspiciously one-sided pile-on, not an accusation
against any specific person or account. The honest position is that individual
posts almost never prove anything; only a *pattern* of several independent
anomalies is informative.

Some signals that, **taken together**, are more consistent with a coordinated
campaign than with spontaneous word-of-mouth:

| Signal                                            | Why it is suspicious in aggregate                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sustained, cross-platform complaints for months   | Real buyers usually vent in a short burst (get a bad unit → return/exchange → move on). Long, multi-platform campaigning with no personal remedy at stake is an odd use of one's time.                                                                                                                                       |
| Complaints that funnel to *one* competing model   | Genuine gripes say "this lens let me down." They rarely converge, in unison, on the same specific alternative. "Complaint + precise product recommendation" is a marketing move.                                                                                                                                             |
| No falsifiable evidence, ever                     | Original RAW/JPEG, EXIF, repair tickets, and support-chat logs are systematically absent — while emotion and confident conclusions are abundant. A wronged buyer usually rushes to show proof.                                                                                                                               |
| A catchy, unfalsifiable, pseudo-scientific slogan | A memorable but physically wrong "mechanism" (here, "the lens caught altitude sickness") spreads for its stickiness, not its correctness.                                                                                                                                                                                    |
| "Aged but thin" account profiles                  | Accounts that are years old yet sparse, whose few posts are unrelated, but which carry one or two laser-focused complaint posts. Maturity plus sudden single-topic focus is a known nurtured-account (养号) shape.                                                                                                           |
| Internally contradictory accounts                 | The story mutates under questioning: "I didn't realise every shot was blurry until I got home" — yet, when pressed in the comments, the same person says "I even tried switching to manual focus and it was still blurry." Noticing badly enough to troubleshoot MF on the spot cannot coexist with not noticing until home. |
| Narrative devices that dodge scrutiny             | Framings such as "I only noticed every shot was blurry after I got home" both maximise emotional impact and conveniently explain away the missing on-the-spot parameters — even though real shooters routinely chimp (zoom in to check sharpness) as they shoot.                                                             |

The decisive variable is still the one from the sections above: **is there any
reproducible, falsifiable evidence, and does the chorus funnel to a single
competitor?** A combination of "zero original evidence + tidy funnelling" tilts
the scale toward a guided campaign.

### Guard against over-reading it, too

Every signal above also has an innocent explanation, and intellectual honesty
requires holding both in view:

- **Memes converge on their own.** One early, catchy post can seed a slogan that
  later posters sincerely believe and repeat — uniform wording does not by itself
  prove a coordinated script.
- **Language silos are real.** Chinese and English communities are naturally
  separated by platform and language, so a discussion can stay contained within
  one of them even when the subject matter is not region-specific.
- **Recommendation algorithms and affiliate creators** routinely surface a
  competing product under any popular item's negative posts — not necessarily the
  same organized group.
- **Survivorship bias:** satisfied owners stay quiet while unhappy ones post
  repeatedly, which alone concentrates negative voices.
- **Plain internet anger** exists: real people can be emotional, vague on
  parameters, and unwilling to screenshot, without being paid actors.

So "**looks like astroturfing**" is not "**is astroturfing**," and "**easy to
fabricate**" is not "**was fabricated**." The useful conclusion does not require
identifying anyone: by Occam's razor, when several *orthogonal* anomalies stack
up — no original evidence, aged-but-thin accounts, a scrutiny-dodging narrative,
tidy funnelling to one competitor, a catchy pseudo-scientific slogan, and global
non-reproduction — "spontaneous genuine word-of-mouth" becomes the most expensive
hypothesis to hold. You never have to prove a campaign; the burden of proof for a
defect stays with whoever asserts it.

## What would actually count as evidence


The claim would become worth weighing the moment any of the following appeared —
and, notably, they have not:

1. **Unretouched original files** (RAW or full-resolution JPEG) with intact EXIF,
   not screen re-shots or platform re-uploads.
2. **A controlled comparison:** tripod, remote/timer release, correct
   image-stabilisation handling, a static distant target (a ridge, a sign), at
   both low and high altitude.
3. **EXIF that rules out slow-shutter motion blur** — shutter speed at or above
   the reciprocal of the focal length at the long end.
4. **A consistent, cross-image defect fingerprint** (e.g. one-sided softness for
   decentering) rather than "whatever region was enlarged".

Note where the burden of proof sits: it is on the party asserting a defect. Until
reproducible, falsifiable evidence exists, the softness in the circulating images
is better explained by shooting technique and file handling than by the lens.

## Why "altitude" reads as motion blur in disguise

There is a mundane reason high-altitude trips *feel* like they produce softer
long-lens shots — and it has nothing to do with the glass:

- **Slow shutter at the long end.** At 200mm the maximum aperture is only f/6.3.
  In dimmer light the camera drops shutter speed to expose, and hand-holding a
  200mm-equivalent frame below its safe shutter (~1/200 s) smears easily.
- **Wind.** High, open terrain is windy; both subject and photographer move more.
- **Cold and thin air** reduce hand steadiness and attention.
- **Strong backlight / snow glare** invite exposure and focus errors.

The real culprit is *slow shutter + hand-holding + long focal length*, which is
easy to misread as "the lens broke at altitude." This is also why the smeared
shots show a moving subject soft while the static background stays sharper — the
classic signature of motion blur, not optics. See
{ref}`museum indoor guidance <museum-indoor-visits>` and the long-end habits in
{doc}`../tips/photographing_tips` for the same slow-shutter trade-off in other
settings.

## A note from actually owning this lens

I own this Sigma 20-200mm. It does not deliver superb resolution — it is a
very-high-ratio travel zoom, and like all such lenses it is "good enough rather
than exceptional", generally soft wide-open at the extremes. But across my own
use it has done its job without optical or mechanical flaws. I have not shot it at
high altitude, so my experience cannot *disprove* a high-altitude-specific claim —
and that cuts both ways: my "it's fine for me" carries no more weight against the
claim than an anonymous "it broke for me" carries for it. What settles the
question is not either anecdote, but reproducible evidence — which, so far, only
one side is missing.

For where this lens fits as a kit-simplifying superzoom (and its documented,
*real* optical trade-offs — 20mm distortion, vignetting, edge softness at 200mm),
see Option 1B in {doc}`lens_recommendation`.

## Bottom line

A claimed *physical* defect that (1) offers no falsifiable original evidence,
(2) rests on a mechanism that violates basic optics, and (3) is reproduced by no
authoritative outlet and exists in only one language market — does not constitute
valid negative information and should not carry weight in a purchase decision.
This verdict is about the *evidence*, not about any individual: even if a genuine
bad copy exists somewhere, the burden of proof lies with the party asserting the
defect, and the softness in the circulating "samples" is fully accounted for by
crop-and-upscale, motion blur, and atmosphere.
