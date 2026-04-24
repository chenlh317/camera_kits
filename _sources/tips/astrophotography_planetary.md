# Planetary Astrophotography from Oslo: Beginner's Field Guide <!-- omit in toc -->

- **Date:** April 2026
- **Author / Skill Level:** Casual amateur — first season of dedicated planetary work
- **Camera Body:** Sony A7C II (Full-Frame, E-Mount)
- **Telescope:** Celestron NexStar 90 SLT — 90 mm Maksutov-Cassegrain, 1250 mm focal length, f/13.9
  computerised Alt-Az mount, currently used in equatorial wedge configuration
- **Barlow Lens:** None yet (discussed below)
- **Location:** Oslo, Norway — latitude ≈ 59° N
- **Primary Target So Far:** Jupiter (four Galilean moons + two main cloud belts captured)
- **Companion Note:** This chapter distils the discussion notes with ChatGPT into a structured field guide.

---

(astro-executive-summary)=
## 📋 Executive Summary

**Planetary astrophotography from 59° N is a roughly seven-month season — practical
any time from October through April — and your current 90 mm SLT is genuinely
capable of more than you've extracted from it.** The next jump in image quality
will come not from a bigger telescope, but from changing *how you capture* —
moving from single long-exposure stills to **short-exposure video + lucky imaging stacking**.
A 2× Barlow and (eventually) a larger aperture are real upgrades, but only after the
capture-and-stacking workflow is solid.

(astro-key-findings)=
### Key Realities for an Oslo-Based Beginner

| Reality                       | Implication                                                               |
| ----------------------------- | ------------------------------------------------------------------------- |
| **Latitude 59° N**            | Jupiter / Saturn culminate at only ~20–30° altitude — atmosphere matters  |
| **Polar summer**              | May–July are essentially useless for planets; deep-sky also limited       |
| **Practical season Oct–Apr**  | Seven months of usable darkness; Nov–Feb is *prime*, Mar–Apr is *bonus*   |
| **90 mm aperture**            | Theoretical resolution ≈ 1.3″ — comfortably resolves Jupiter's belts      |
| **f/13.9 native focal ratio** | Already long; a Barlow pushes you into the diffraction-limited regime     |
| **A7C II full-frame sensor**  | Oversized for planets; you will be using a tiny crop region of the sensor |

(astro-quick-reference)=
### Quick Reference: What to Do When

| Situation                              | Recommended Approach                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Jupiter, Oct–Apr, near culmination** | A7C II video, 4K 50–60 fps (or 1080p + 2× Barlow), 1/80–1/125 s, ISO 200–800, 30–60 s clips |
| **Late-spring Jupiter (Mar–Apr)**      | Same recipe; warmer, more pleasant nights; catch it before twilight closes in               |
| **Visual only — show a friend**        | Skip the camera — use a 25 mm + 10 mm eyepiece, no Barlow                                   |
| **Saturn season (Aug–Nov 2026–2030)**  | Now rising into autumn evenings; rings re-opening yearly — your **best** five-year window   |
| **Moon (any phase)**                   | Single short exposures are fine — the Moon is bright; lucky imaging optional                |
| **Polar summer (May–Jul)**             | Practise daytime terrestrial use of the OTA, or do solar (with proper filter)               |
| **Strong star twinkling overhead**     | Pack up. Atmospheric seeing is the limiting factor, not your gear                           |

(astro-bottom-line)=
### The Bottom Line

For at least the next season, your image-quality ceiling is set by **atmospheric seeing
and capture technique**, not by aperture. Master video + AutoStakkert + RegiStax on the
90 SLT first. A 2× Barlow is the single highest-value accessory upgrade
(~€50–100, doubles effective focal length to 2500 mm). A telescope upgrade to the
**127 SLT MAK** or **NexStar 6 SE** is a real improvement, but the gain is
*proportional to aperture* (~1.4× and ~1.7× resolution respectively) — meaningful,
but not transformative until your capture pipeline is squeezing every photon out
of the 90 mm first.

---

```{contents}
:depth: 3
```

---

(1-the-oslo-observing-calendar)=
## **1. The Oslo Observing Calendar**

At 59° N, the planetary observing year is a sharply asymmetric curve. Roughly:

| Month         | Darkness                         | Comfort           | Planetary Quality                                              |
| ------------- | -------------------------------- | ----------------- | -------------------------------------------------------------- |
| **Oct – Dec** | Deep, long nights                | Cold, often damp  | **Optimum** — opposition season for outer planets              |
| **Jan – Feb** | 14–16 h of true darkness         | Coldest of year   | **Excellent** — Jupiter still high after opposition            |
| **Mar – Apr** | Astronomical twilight returns    | **Most pleasant** | **Very usable** — shorter dark window, but warm and dry nights |
| **May – Jul** | No astronomical darkness         | Mild              | **Effectively zero** — sky never fully dark                    |
| **Aug**       | Astro-darkness returns mid-month | Mild              | Marginal; planets low                                          |
| **Sep**       | Real nights return               | Cooling           | Improving; targets rising                                      |

Two latitude-driven facts you cannot escape:

1. **Outer planets culminate low.** Jupiter peaks at roughly 30–35° altitude during a
   typical Oslo opposition; Saturn at 20–25°. Compared to 40° N this means thicker air
   and more atmospheric blurring.
2. **Opposition timing matters more here than at lower latitudes.** A summer opposition
   (e.g. Saturn currently) is essentially wasted from Oslo — you cannot observe it in
   true darkness.

> 💡 **Don't dismiss March–April.** Late spring is genuinely the most *pleasant*
> half of the season: temperatures of +5 to +10 °C instead of −10 °C, much less
> dewing and frost on the optics, and no need for heavy gloves while focusing.
> The trade-off is a shrinking dark window — by mid-April astronomical darkness
> is already gone and you're working in nautical twilight — but Jupiter at
> mag −2 is bright enough to image *through* twilight as long as it's still
> reasonably high in the sky. For a casual amateur, an April Jupiter session
> in shirt-sleeves is often a better experience than a January one in a parka.

> 💡 **Plan around opposition + culmination.** For each target, find:
> (a) the opposition date for the year, and (b) the time the planet crosses the
> meridian on a given night (Stellarium or SkySafari). Aim for the ±1 h window
> around culmination; that is when you are looking through the *least* atmosphere.

(1-1-jupiter-the-realistic-target)=
### 1.1 Jupiter — Your Realistic Primary Target

Jupiter is the right first project from Oslo because:

- It is **bright** (mag −2 to −3), tolerating short exposures and high frame rates.
- Its disc (~40–45″ at opposition) is **large enough** for a 90 mm scope at 1250 mm
  to resolve the two main equatorial belts and — with patience — the Great Red Spot
  and moon shadow transits.
- Its opposition cycle currently lands in the **autumn-to-winter** Oslo sweet spot.

You have already captured the **four Galilean moons** and **two main cloud belts**.
That confirms the optical chain and your collimation/focus discipline are sound.
The next visible step is **belt structure**, **polar darkening**, and eventually
**Great Red Spot rotation**.

(1-2-saturn-the-second-target)=
### 1.2 Saturn — The Second Target, Now Coming Back

Saturn passed through the **edge-on ring-plane crossing** in March 2025 and is
now re-opening its rings each year. Its declination is also climbing back
northward through this decade, with successive oppositions in **Pisces → Aries
→ Taurus** (2026–2030). From Oslo this means Saturn culminates at a usable
**30–40° altitude** during autumn opposition season — not as high as Jupiter
at its best, but very much worth imaging. The 90 SLT can show:

- The ring system clearly separated from the disc at any reasonable magnification.
- The **Cassini division** on a good night at 150–200×.
- The dark equatorial band on the disc.
- **Titan** as an obvious bright moon; Rhea / Tethys / Dione on a dark night.

The practical season is **August through November** of each year, peaking around
opposition (see the five-year calendar in §1.6).

(1-3-the-moon-the-always-available-fallback)=
### 1.3 The Moon — The Always-Available Fallback

The Moon is bright enough that:

- A single 1/250–1/1000 s exposure at ISO 100 is properly exposed.
- Lucky imaging is *optional* but still helps for crater detail.
- It is high in the winter sky (full moon near zenith in December).

Use the Moon to **practise focusing, framing, and tracking** when planets are not
cooperative. It rewards you instantly and trains every skill you'll later apply
to Jupiter.

(1-4-double-stars)=
### 1.4 Double Stars — The All-Weather, All-Season Target

**Double stars** are pairs (or small groups) of stars that appear very close
together in the sky. They come in two flavours:

- **True binaries** — two stars physically bound by gravity, orbiting a common
  centre of mass. The majority of catalogued doubles.
- **Optical doubles** — unrelated stars at very different distances that just
  happen to line up along the same line of sight.

Through the eyepiece they look like one fuzzy "star" at low power; at higher
magnification they **split** into two distinct points — often with striking
colour contrast (gold + blue, white + orange, etc.).

**Why they're a perfect 90 SLT target — even from Oslo:**

- They are **point sources**, so atmospheric seeing affects them far less than
  extended planetary detail. A mediocre night that ruins Jupiter still splits
  most pairs cleanly.
- The 90 mm aperture has the resolution to split pairs down to about **1.3″**
  apart (Dawes limit) — plenty for the classic showpiece doubles.
- They are **bright** — unbothered by Oslo's light pollution.
- Your **9 mm eyepiece at 139×** is well-suited to splitting close pairs.
- They are visible **year-round**, including the polar-summer months when
  planetary work is dead — the brightest doubles punch through twilight.

**A short Oslo-friendly showpiece list:**

| Star              | Constellation | Separation      | Best Season   | What You See                                               |
| ----------------- | ------------- | --------------- | ------------- | ---------------------------------------------------------- |
| **Albireo**       | Cygnus        | 35″             | Summer–autumn | Famous gold + sapphire-blue pair — easy split at any power |
| **Mizar & Alcor** | Ursa Major    | 14″ (Mizar A–B) | Year-round    | Bright pair in the Big Dipper's handle; circumpolar        |
| **Castor**        | Gemini        | 5″              | Winter        | Tight white-white pair — needs the 9 mm                    |
| **γ Andromedae**  | Andromeda     | 10″             | Autumn–winter | Gold + blue, an Albireo cousin                             |
| **ε Lyrae**       | Lyra          | "Double-double" | Summer–autumn | Wide pair; each component is itself a tight pair           |
| **ι Cassiopeiae** | Cassiopeia    | 2.5″ / 7″       | Year-round    | A triple system; circumpolar                               |
| **Polaris**       | Ursa Minor    | 18″             | Year-round    | Faint companion next to the bright Pole Star               |

> 💡 **Use doubles to learn the scope.** When the planets are unavailable
> (May–July) or seeing is too poor for Jupiter detail, an evening of double-star
> hunting is a perfect way to keep your alignment, GoTo, and eyepiece-swap
> habits sharp — with guaranteed satisfying results.

(1-5-what-else-is-within-reach-of-the-90-slt)=
### 1.5 What Else Is Within Reach of the 90 SLT

The 90 SLT is a **planetary / lunar / double-star instrument first**, and a
*selective* deep-sky instrument second. The 1250 mm focal length at f/13.9
gives a tiny native field of view (≈0.5° with a 25 mm eyepiece) and a slow
focal ratio that punishes faint extended objects. Within those constraints
the following targets are genuinely worthwhile:

(planets-of-interest)=
#### Planets — Realistic Expectations

| Target      | Best Season          | Visual Result on a Decent Oslo Night                                          | Photographic Result (lucky imaging)                           |
| ----------- | -------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Venus**   | Around elongations   | Bright crescent / half phase, dazzling; no surface detail                     | Crisp phase shape; UV/IR filter can hint at cloud bands       |
| **Mars**    | ±2 months opposition | Tiny orange disc; polar cap on a great night; **only useful near opposition** | Polar cap + 1–2 albedo features at opposition; a hard target  |
| **Jupiter** | Oct–Apr, near opp.   | 2 main belts, 4 Galilean moons as points, occasional GRS                      | Belts + zones, GRS, moon shadow transits — your prime target  |
| **Saturn**  | Oct–Dec, near opp.   | Rings clearly separated from disc; Cassini division on top nights; Titan      | Rings, Cassini, equatorial belt; demanding but very rewarding |
| Mercury     | Around elongations   | Tiny phase only; very low altitude from Oslo — usually not worth the effort   | Skip                                                          |
| Uranus      | Near opposition      | Pale blue-green dot, just barely non-stellar at high power                    | Skip                                                          |
| Neptune     | Near opposition      | Star-like; only confirmable with a chart                                      | Skip                                                          |

> 💡 **Venus needs care, not power.** Venus is brightest pre-sunrise or
> post-sunset; observing it during *daytime* (planet still above horizon
> after sunrise) actually gives a steadier, less glare-blown view through
> a small Mak. Never sweep near the Sun without absolute certainty of the
> Sun's position.

(deep-sky-targets-90slt)=
#### Deep-Sky — What Actually Works at f/13.9

| Target                                   | Visual Verdict on 90 SLT                                                                | Imaging Verdict                                          |
| ---------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **M31 Andromeda Galaxy**                 | Bright **core only** — the full galaxy spans 3°+, so it overflows the field by 6×       | ❌ Wrong scope. Use a camera + 85–200 mm lens on a tripod |
| **M42 Orion Nebula**                     | ✅ **Excellent.** Trapezium resolved as 4 stars, nebulosity in the wings clearly visible | ✅ Doable — short stacked exposures, even from a city sky |
| **M45 Pleiades**                         | Stars are pretty but the cluster is 2° wide — overflows the field                       | ❌ Wrong scope                                            |
| **Double Cluster (NGC 869/884) Perseus** | Two halves don't quite fit together; pick one at a time — still beautiful               | Marginal                                                 |
| **M13 Hercules Globular**                | A misty ball at low power; partly resolved into stars at high power on a good night     | ✓ Possible with stacking                                 |
| **M57 Ring Nebula** (Lyra)               | Small but unmistakably a smoke ring at 100×+                                            | ✓ Possible — small target suits long focal length        |
| **M27 Dumbbell Nebula** (Vulpecula)      | Larger than M57, dimmer; visible as a hazy patch                                        | Marginal from Oslo skies                                 |
| **Open clusters M35, M36, M37, M38**     | Pretty winter targets; M37 in particular is rich and just fits                          | Light imaging worthwhile                                 |
| **Comets (when bright, mag ≤ 6)**        | Surprisingly good — high contrast against dark sky                                      | Stacked exposures show tail structure                    |

*(For double stars, see §1.4 above — the 90 SLT excels at splitting close colour-contrast pairs.)*

(other-targets-90slt)=
#### Other Targets Worth Knowing About

- **The Sun** — *only* with a properly fitted full-aperture **white-light solar
  filter** (Baader AstroSolar film, ≈€30 in DIY form). Sunspots and faculae are
  beautifully sharp through a 90 mm Mak. **Never observe the Sun without a
  certified front-end filter** — eyepiece-end "sun filters" can crack and blind
  you instantly.
- **The ISS and bright satellite passes** — visually impressive at high power
  if you can manually track; photographically, a single short exposure at 1/2000 s
  during a bright pass can resolve the solar panel structure.
- **Lunar occultations and Galilean-moon transits/shadows** — predictable events
  worth planning around. Cloudoutside.com and the *In-The-Sky.org* event list
  show these.
- **Conjunctions and close approaches** — Jupiter–Saturn type events are
  trivially in reach and make natural shareable photos.

> ⚠️ **Honest deep-sky verdict.** The 90 SLT will *not* turn into a
> deep-sky imaging rig. If a Norwegian aurora season ever pulls you toward
> wide-field nightscape work, the right tool is your A7C II + SIRUI 35 mm f/1.4
> on a normal tripod — not the telescope. Use the SLT for what it's good at:
> **point sources, planets, the Moon, and small bright nebulae.**

(1-6-five-year-planetary-calendar)=
### 1.6 Five-Year Planetary Calendar (Oslo, 2026–2030)

Approximate opposition dates (Mars / Jupiter / Saturn) and greatest-elongation
dates (Venus / Mercury) for the **next five years from Oslo's perspective**.
Best observing window is roughly **±2 months around opposition** for outer planets
and **±3 weeks around elongation** for inner planets.

> ⚠️ **Always verify dates** in Stellarium / SkySafari before planning a session
> — these are rounded to the nearest week and can shift by a day or two
> depending on source.

| Year     | Venus (greatest elongation)                | Mars (opposition)              | Jupiter (opposition)               | Saturn (opposition)             | Notes for Oslo                                                   |
| -------- | ------------------------------------------ | ------------------------------ | ---------------------------------- | ------------------------------- | ---------------------------------------------------------------- |
| **2026** | **Aug 13** — evening (E. elongation 46°)   | —                              | (Jan 10, 2026 — already passed)    | **Oct 4** — in Pisces           | Saturn well placed, rings re-opening; Venus best at evening      |
| **2027** | **Jan 7** — morning (W. elongation 47°)    | **Feb 19** — in Leo, ~14″ disc | **Feb 11** — high, Cancer/Leo      | **Oct 18** — high, Aries        | **Best year of the 5**: Mars + Jupiter near same time, both high |
| **2028** | **Mar 25** — evening; **Aug 26** — morning | —                              | **Mar 12** — Leo, dropping lower   | **Oct 31** — near max altitude  | Saturn at its best of the cycle from Oslo                        |
| **2029** | **Oct 31** — evening (E. elongation 47°)   | **May 4** — Cancer, ~14″ disc  | **Apr 12** — Virgo, low and late   | **Nov 13** — still high, Taurus | Jupiter increasingly difficult from 59° N                        |
| **2030** | **Mar 21** — morning (W. elongation 46°)   | —                              | **May 13** — low, lost in twilight | **Nov 27** — high in Taurus     | Plan around Saturn; Jupiter season effectively over              |

**How to read this table:**

- **Jupiter** is *high* (good for Oslo) in 2026–2027 and progressively lower each
  year — the planet's ecliptic latitude is decreasing through this cycle.
  **Prioritise Jupiter sessions in 2026–2027.**
- **Saturn** is in its *best* northern apparition in 2027–2030 — the entire
  five-year window is excellent. Ring tilt closes through 2025 (edge-on) and
  re-opens through 2030, so rings get more dramatic each year.
- **Mars** has only **two oppositions** in the window (Feb 2027, May 2029).
  Both produce small discs (~14″ in each case) — useful but not the spectacular
  perihelic 2018/2035-style apparitions. Worth attempting; don't expect dramatic results.
- **Venus** alternates evening↔morning visibility through its 19-month synodic
  cycle; each greatest elongation gives ~6 weeks of crescent-to-half phase observation.
- **Mercury** elongations occur ~6× per year but from Oslo Mercury is almost
  always too low to bother with; not tabulated.

> 💡 **The headline:** if you image Jupiter hard in **2026–2027** and pivot to
> Saturn for the rest of the decade, you will catch each planet at its
> Oslo-optimum and have a complete planetary portfolio by 2030.

---

(2-the-capture-method-shift-stills-to-lucky-imaging)=
## **2. The Capture Method Shift: From Stills to Lucky Imaging**

This is the single biggest change you can make right now, and it costs nothing.

(2-1-why-your-current-stills-look-soft)=
### 2.1 Why Your Current Stills Look Soft

Your initial Jupiter frames used **ISO 50, 1/10 s**. The arithmetic is unforgiving:
in 100 ms the atmosphere overhead at Oslo altitude wobbles many times, and your
sensor integrates the *average* of all those wobbles — a mush. The planet is
correctly exposed but smeared by atmospheric turbulence (often called "seeing").

> ⚠️ **The 100 ms problem.** At 59° N, near-zenith seeing on a typical night
> is 2–4″. Atmospheric coherence time is on the order of 5–20 ms.
> Any single exposure longer than ~30 ms is, in practice, a long exposure.

(2-2-the-lucky-imaging-principle)=
### 2.2 The Lucky Imaging Principle

```
   Many short frames → discard the bad ones → align & stack the good ones
   ──────────────────────────────────────────────────────────────────────
   Result:  resolution of the best moments,  noise of the full set
```

You shoot a **video** at the highest practical frame rate, with each exposure
shorter than the seeing coherence time. Most frames are blurred, but a small
percentage (the "lucky" ones) are essentially diffraction-limited. Software
ranks the frames by sharpness, keeps the top 10–30%, aligns them on planetary
features, and averages them — beating down sensor noise without
re-introducing the blur.

(2-3-recommended-a7c-ii-video-settings)=
### 2.3 Recommended A7C II Video Settings (Prime Focus)

| Parameter           | Recommendation                                      | Reasoning                                                             |
| ------------------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| **Resolution**      | **4K (UHD)** preferred; 1080p only with a 2× Barlow | 1080p downsamples ~3.6× from native; the planet ends up under-sampled |
| **Crop mode**       | APS-C / Super-35 if available                       | Effective 1.5× reach with no optical penalty                          |
| **Frame rate**      | 50 or 60 fps                                        | More frames = better statistics; 60p preferred if stable              |
| **Shutter**         | 1/80 – 1/125 s                                      | ≤ atmospheric coherence; freezes seeing                               |
| **ISO**             | 200 – 800                                           | Start 400; raise if histogram is left-clipped                         |
| **Picture profile** | Standard / no S-Log                                 | You want linear-ish data, not log curves                              |
| **Clip length**     | 30 – 60 s                                           | 1500–3600 frames is plenty; longer ⇒ Jupiter rotation blurs           |
| **White balance**   | Daylight (fixed)                                    | Auto WB will jump frame to frame and ruin colour stacking             |
| **Stabilisation**   | Off                                                 | The mount tracks; IBIS will fight it                                  |
| **Focus**           | Manual, magnified                                   | Use focus magnification on a moon, then lock                          |

> 💡 **Why ≤ 60 s?** Jupiter rotates once in ~9.9 h, so a feature near the equator
> moves visibly in ~90 s. Longer clips produce **rotational smear** that no
> stacking can recover. Keep individual videos short; capture multiple back-to-back
> clips if you want more data, then process them separately or use WinJUPOS to
> de-rotate before final combination.

(2-4-the-processing-pipeline)=
### 2.4 The Processing Pipeline

The free, standard, Windows-friendly pipeline is:

```
   .MP4 / .MOV  →  PIPP  →  .SER / .AVI  →  AutoStakkert!4  →  stacked .TIF
                                                ↓
                                            RegiStax 6  →  wavelet sharpening
                                                ↓
                                  Lightroom / Photoshop  →  final cropping & colour
```

1. **PIPP** (Planetary Imaging Pre-Processor) — convert the A7C II video to a
   monochrome-or-RGB SER file, centre the planet in each frame, and crop to a small
   ROI around it. Massively speeds up the next step.
2. **AutoStakkert!4** — analyse, place alignment points (AP grid), pick the top
   10–25 % of frames, stack. Output is a clean but soft TIFF.
3. **RegiStax 6 wavelets** — restore detail. Start *gentle*:
   Layer 1 = 0.10–0.20, Layer 2 = 0.10–0.20, Layer 3 = 0.05–0.10. Stop the
   moment you see dark haloes around the limb — that's over-sharpening.
4. **Lightroom / Photoshop** — final crop, mild contrast, colour balance,
   small noise reduction in the background sky.

> ⚠️ **Don't sharpen what you didn't capture.** Wavelets cannot invent detail
> the optics never recorded. If the stacked image is featureless, the answer is
> *better seeing or more aperture*, not stronger wavelets.

(2-5-coupling-the-a7c-ii-to-the-90-slt)=
### 2.5 Coupling the A7C II to the 90 SLT

Two practical methods, in increasing order of effort:

- **Afocal** — point the camera with a normal lens (e.g. 85 mm f/2) into a
  high-power eyepiece. Cheap and simple; vignettes badly and is hard to align.
  Use only as a one-night experiment.
- **Prime focus (recommended)** — remove the eyepiece, screw a **T-ring + 1.25″
  T-adapter** onto the A7C II, slide it into the 90 SLT's focuser. The
  telescope itself becomes a 1250 mm f/13.9 telephoto. Sharpest, simplest,
  most repeatable. This is what the video settings above assume.

> 💡 **Backfocus check.** Maksutov-Cassegrain scopes — the 90 SLT included —
> sometimes need a small extension tube to reach focus on a mirrorless body,
> but more often the issue is the *opposite*: a Mak's focuser has plenty of
> in-travel and the T-ring + adapter usually works directly. Verify on the
> Moon before chasing Jupiter — the Moon is far more forgiving of framing fumbles.

---

(3-eyepieces-and-the-barlow-lens)=
## **3. Eyepieces and the Barlow Lens**

(3-1-how-eyepieces-work)=
### 3.1 How Eyepieces Work — Your 25 mm and 9 mm

The 90 SLT ships with two eyepieces marked **25 mm** and **9 mm**. Those numbers
are the eyepiece's own **focal length in millimetres**, and together with the
telescope's focal length they determine magnification:

```
   Magnification = telescope focal length  /  eyepiece focal length
                 = 1250 mm  /  eyepiece mm
```

So your two stock eyepieces give:

| Eyepiece        | Magnification on 90 SLT | True Field of View (≈) | Exit Pupil | Best For                                                         |
| --------------- | :---------------------: | :--------------------: | :--------: | ---------------------------------------------------------------- |
| **25 mm** (low) |         **50×**         |         ~1.0°          |   1.8 mm   | Finding targets, the Moon at full disc, M42, open clusters       |
| **9 mm** (high) |        **139×**         |         ~0.4°          |  0.65 mm   | Planets (Jupiter belts, Saturn rings), Moon detail, double stars |

A few things worth understanding:

- **Lower eyepiece focal length = higher magnification.** Counter-intuitive at
  first, but it falls straight out of the formula above. The "9" is the
  *high-power* eyepiece, the "25" is the *low-power* one.
- **Higher magnification = darker, smaller field, dimmer image.** Light from
  the planet is spread over more of your retina. This is why high power
  needs *bright* targets (planets, Moon).
- **Exit pupil** is the diameter of the light cone leaving the eyepiece into
  your eye (= aperture / magnification, in mm). Below about 0.5 mm the image
  becomes uncomfortably dim and your own eye's floaters become visible. The
  9 mm is already close to that limit on the 90 SLT.
- **Magnification has a ceiling.** The empirical maximum useful magnification
  is roughly **2× per mm of aperture** — so ~180× on the 90 SLT. Your 9 mm
  at 139× is comfortably under this; pushing past it (e.g. with a 3× Barlow)
  gives only **empty magnification** — a bigger but blurrier image.

(when-to-use-which-eyepiece)=
#### When to Use Which

1. **Always start with the 25 mm.** Its wider field (~1°) makes it far easier
   to find the target after a GoTo slew, and the brighter, calmer image is
   better for confirming focus and centering.
2. **Switch to the 9 mm once the target is centred** — for any high-detail
   work on planets, the Moon, or close double stars.
3. **Stay on the 25 mm** for extended dim objects (M31's core, M42's nebulosity,
   M13, open clusters) — the lower magnification gives you a brighter image
   per unit area, which is what your eye needs for faint extended targets.
4. **Re-centre and re-focus after every swap.** Eyepieces have slightly
   different parfocal positions; the 9 mm in particular needs a careful
   focus pass.

> 💡 **A typical observing session.** Slew with GoTo → confirm with **25 mm**
> at 50× → centre the planet → swap to **9 mm** at 139× → refocus → observe.
> When sharing the view with someone else, leave the 25 mm in for the wider,
> more forgiving image.

> ⚠️ **Eyepieces are visual-only for you.** For lucky-imaging video you
> remove the eyepiece entirely and use prime focus (see §2.5). Keep the
> eyepieces for *visual* use, family demos, and — most importantly — for
> **judging whether tonight's seeing is worth setting up the camera at all**
> (see the "Use it visually first" tip in §3.4).

(3-2-what-a-barlow-actually-does)=
### 3.2 What a Barlow Actually Does

A Barlow is a **diverging lens** placed in front of the eyepiece (visual) or
camera sensor (imaging) that multiplies the system focal length:

```
   Native:    1250 mm  f/13.9
   + 2× Barlow: 2500 mm f/27.8     (image 2× larger, 4× dimmer per pixel)
   + 3× Barlow: 3750 mm f/41.7     (image 3× larger, 9× dimmer per pixel)
```

Three consequences flow from this:

1. **The planet's image grows** on the sensor — more pixels per arcsecond.
2. **The image dims** by the square of the multiplier — you must compensate
   with longer shutter or higher ISO, both of which fight lucky imaging.
3. **Tracking and focus errors are also magnified.** Anything wobbly becomes
   2× wobblier.

> 💡 **A Barlow on your eyepieces.** A 2× Barlow turns your 25 mm into an
> effective 12.5 mm (100×) and your 9 mm into an effective 4.5 mm (~280×).
> The 4.5 mm-equivalent is *past* the 90 SLT's useful magnification ceiling —
> fine to try on a great-seeing Jupiter night, but expect a soft, dim view.
> The 12.5 mm-equivalent (100×) is the more useful combination for visual
> planetary work.

(3-3-do-you-need-one-now)=
### 3.3 Do You Need One *Now*?

**Short answer: not for the first season; yes by the second — unless you stay in 1080p video, in which case effectively yes immediately.**

The A7C II's native sensor pitch is **~3.76 µm** (33 MP full-frame). At
1250 mm prime focus this gives:

```
   Image scale ≈ 206265 × pixel_size_mm / focal_length_mm
              ≈ 206265 × 3.76e-3 / 1250  ≈ 0.62 ″/pixel  (native still photo)
```

Jupiter's disc at 45″ therefore spans about **70 px wide on a still photo**.
The classic *Nyquist for planetary imaging* guideline says you want
**2–3 pixels per resolution element**, and the 90 mm diffraction limit (Dawes)
is ~1.3″, so an ideal image scale is ~0.4–0.6 ″/px. Native focal length already
satisfies this **for stills**.

Video is different, because the camera downsamples the sensor to the chosen
output resolution:

| Capture mode                  | Effective output pixel scale | Jupiter disc on screen |
| ----------------------------- | ---------------------------- | ---------------------- |
| Still photo (native 33 MP)    | ~0.62 ″/px                   | ~70 px wide            |
| 4K video (full-frame readout) | ~1.1 ″/px                    | ~40 px wide            |
| 4K video (APS-C / S35 crop)   | ~0.75 ″/px                   | ~60 px wide            |
| **1080p video (FHD)**         | **~2.3 ″/px**                | **~20 px wide**        |

**Implications:**

- In **4K** — especially in APS-C crop mode — native focal length is close to
  optimum for the 90 mm aperture. A Barlow is helpful, not essential.
- In **1080p** the planet is severely under-sampled at native focal length; a
  **2× Barlow becomes essentially required** to get back to ~1.1 ″/px and
  ~40 px disc width. This is the easiest case for buying a Barlow soon.
- A 2× Barlow on top of 4K APS-C crop pushes you to ~0.38 ″/px — slight
  over-sampling, but useful for AP alignment and wavelet headroom.

(3-4-recommendation-when-you-do-buy)=
### 3.4 Recommendation When You Do Buy

| Choice               | Verdict                                                        |
| -------------------- | -------------------------------------------------------------- |
| **2× Barlow**        | ✅ Right answer. Cheap, useful for both visual and imaging      |
| **3× Barlow**        | ❌ Skip. Empty magnification on a 90 mm; you'll just see blur   |
| **Powermate 2×**     | ✅ Optical quality upgrade vs. budget Barlow if you can stretch |
| **Cheap kit Barlow** | ⚠️ Often soft and adds chromatic aberration; avoid the bundled  |

Look for a **branded short 2× Barlow** (Celestron Omni, Tele Vue, Baader, GSO).
Budget around €50–100 for something that won't be the optical bottleneck.

> 💡 **Use it visually first.** Drop the 2× Barlow under a 10 mm eyepiece on the
> 90 SLT to get 250× — at the *very* limit of useful magnification for 90 mm,
> but a great way to learn whether your typical Oslo seeing supports that
> magnification on a given night. If the view is mush, the camera will record mush.

(3-5-image-quality-gain-realistic)=
### 3.5 Realistic Image-Quality Gain

On a *good seeing* night the 2× Barlow + 90 SLT + A7C II should give you:

- A planet that fills a noticeably larger crop of the frame (easier framing)
- Cleaner wavelet output (more pixels for the algorithm to work with)
- The first credible look at the Great Red Spot and finer belt structure

On a *typical* Oslo night (mediocre seeing) it gives you the *same detail*
as native focal length, just larger and dimmer. Which is to say: **a Barlow
multiplies your good nights and does nothing for your bad ones.**

---

(4-aperture-upgrade-90-vs-127-mak-vs-nexstar-6)=
## **4. Aperture Upgrade: 90 SLT vs 127 MAK vs NexStar 6 SE**

This is the question every amateur asks at this stage. The honest answer involves
three numbers: **aperture (light + resolution)**, **focal length (image scale)**,
and **focal ratio (exposure speed)**.

(4-1-the-numbers-side-by-side)=
### 4.1 The Numbers, Side by Side

| Spec                       | NexStar 90 SLT (current) | NexStar 127 SLT MAK | NexStar 6 SE       |
| -------------------------- | ------------------------ | ------------------- | ------------------ |
| **Aperture**               | 90 mm                    | 127 mm              | 150 mm             |
| **Focal length**           | 1250 mm                  | 1500 mm             | 1500 mm            |
| **Focal ratio**            | f/13.9                   | f/11.8              | f/10               |
| **Optical design**         | Maksutov-Cassegrain      | Maksutov-Cassegrain | Schmidt-Cassegrain |
| **Dawes resolution limit** | 1.29″                    | 0.91″               | 0.77″              |
| **Light gathering vs 90**  | 1.0×                     | 2.0×                | 2.8×               |
| **Tube weight**            | ~1.5 kg                  | ~3.4 kg             | ~4.5 kg            |
| **Mount**                  | Light SLT (Alt-Az)       | Same SLT            | Heavier single-arm |
| **Cooldown to ambient**    | 15–20 min                | 30–45 min           | 30–60 min          |
| **Approx. price (new)**    | (owned)                  | €600–800            | €900–1100          |

(4-2-what-aperture-actually-buys-you)=
### 4.2 What Aperture Actually Buys You

Two independent gains scale with aperture:

1. **Resolution** scales **linearly** with aperture (Dawes/Rayleigh). 127 mm
   resolves features ~1.4× finer than 90 mm; 150 mm resolves ~1.7× finer.
2. **Light gathering** scales with the **square** of aperture. 127 mm collects
   2.0× more light; 150 mm collects 2.8× more. This means you can use shorter
   exposures (better for lucky imaging) at the same SNR.

Both gains are real **only when atmospheric seeing supports them**. From Oslo
on a typical night, seeing is 2–4″ — *worse* than the 90 SLT's resolution
limit. On those nights, a 150 mm scope sees the same blurry blob as a 90 mm.
On the rare excellent night (sub-1.5″ seeing, perhaps 10–20% of clear nights at
your latitude), the larger aperture genuinely shows you finer detail.

> ⚠️ **Aperture without good seeing is just brightness.** The marketing
> resolution numbers assume textbook conditions. Norway is not Chile.

(4-3-the-127-slt-mak-the-conservative-upgrade)=
### 4.3 The 127 SLT MAK — The Conservative Upgrade

**Image quality gain over 90 SLT:** moderate but real (≈1.4× resolution,
2× light), within the same SLT mount/tripod ecosystem.

**Strengths:**

- **Maksutov design is essentially perfect for planets** — closed tube, no
  diffraction spikes, very high contrast, near-zero chromatic aberration.
  Many amateurs consider 127–180 mm Maks the sweet spot for planetary visual.
- **Drop-in replacement** on your existing SLT mount — no new mount, tripod,
  or wedge purchase. Your equatorial wedge experience transfers directly.
- **Long focal length (1500 mm, f/11.8)** means high native magnification —
  a 2× Barlow gives 3000 mm f/24, very close to optimum for 127 mm aperture.
- **Modest weight** keeps the SLT mount within its comfort zone.

**Weaknesses:**

- **Longer thermal cooldown than the 90** — 30–45 minutes outside before images
  settle, vs. ~15–20 min for the smaller 90 SLT (also a Mak, but with much less
  glass to equalise). In Oslo winter (often −5 to −15 °C), cooldown is *the*
  dominant practical limitation. Plan accordingly: set up early, observe later.
- **Dewing on the front corrector plate** — already a familiar issue with the
  90 SLT, and it gets worse with the larger 127 mm corrector exposed to Oslo's
  humidity. A **dew shield** (DIY from camping mat is fine) is essentially mandatory.
- Very narrow native field of view; not a good deep-sky or Milky Way scope.

**When it makes sense:** when you have proven you can extract everything from
the 90 SLT, when you want a planetary-specialist optic, and when you don't
want to deal with a new mount.

(4-4-the-nexstar-6-se-the-bigger-step)=
### 4.4 The NexStar 6 SE — The Bigger Step

**Image quality gain over 90 SLT:** substantial (≈1.7× resolution, 2.8× light),
but with real ergonomic costs.

**Strengths:**

- **Largest aperture** of the three — the only one that genuinely outperforms
  the 90 + 2× Barlow on a great-seeing night.
- **Schmidt-Cassegrain** is more versatile than Mak: shorter tube length,
  slightly faster (f/10) so usable for some deep-sky targets too.
- Single-fork mount is a sturdier platform than the SLT; better for any
  imaging beyond pure planetary lucky imaging.

**Weaknesses:**

- **Heavier tube + heavier mount** — less of a "grab and go" instrument.
  Setup time roughly doubles compared to the 90 SLT.
- **Same cooldown problem as the Maks**, possibly worse due to thicker corrector.
- **Higher price**, and the SE mount is *not* an equatorial design — for
  planetary-only work this is fine, but it caps any future deep-sky ambitions.
- **Diffraction effects from the secondary mirror obstruction** very slightly
  reduce contrast vs. an equivalent unobstructed refractor — invisible to most
  amateurs, and not a practical difference vs. your existing 90 Mak, but worth knowing.

**When it makes sense:** when you have caught the bug, your processing pipeline
is mature, and you suspect your Oslo "good nights" are being limited by
aperture rather than seeing. Also if you ever plan to image deep-sky objects,
the 6 SE is a far more versatile starting point than either SLT.

(4-5-comparison-of-realistic-jupiter-results)=
### 4.5 Realistic Jupiter Results, Side by Side

A rough table of what each setup can be expected to *resolve on Jupiter* under
typical Oslo seeing (2.5–3″) and best-case Oslo seeing (1.5″):

| Detail                         | 90 SLT (now)  | 90 + 2× Barlow | 127 MAK  | NexStar 6 SE |
| ------------------------------ | :-----------: | :------------: | :------: | :----------: |
| Galilean moons as discs        | ✓ (sometimes) |       ✓        |    ✓     |      ✓       |
| Two main equatorial belts      |       ✓       |       ✓        |    ✓     |      ✓       |
| Belt fine structure / festoons |     rare      |   occasional   | regular  |   regular    |
| Great Red Spot as a feature    |     rare      |   occasional   | regular  |   regular    |
| GRS internal detail            |       ✗       |  ✗ (typical)   | ✓ (best) |   ✓ (best)   |
| Polar region darkening         |     rare      |   occasional   | regular  |   regular    |
| Moon shadow transits sharp     |       ✓       |       ✓        |    ✓     |   ✓ (best)   |

The honest pattern: **the 127 MAK is the biggest *quality-per-euro* upgrade,
the 6 SE is the biggest *capability* upgrade.**

---

(5-the-pragmatic-roadmap)=
## **5. The Pragmatic Roadmap**

A staged plan that respects your "casual amateur" framing and Oslo's climate:

(5-1-this-season-winter-2026-2027)=
### 5.1 This Season (Winter 2026–2027) — Free / Cheap Wins

1. **Build the lucky-imaging pipeline on the 90 SLT.** Capture Jupiter video
   with the A7C II at the settings in §2.3, run it through PIPP →
   AutoStakkert → RegiStax. Repeat until each step is muscle memory.
2. **Buy a T-ring + 1.25″ T-adapter** for the A7C II (~€25). Mandatory for
   prime-focus capture.
3. **Buy a decent 2× Barlow** (~€50–100) once the pipeline is producing
   clean stacks — you'll feel the moment you want more image scale.
4. **Add a dew shield and a small 12 V dew heater band** if you start to lose
   clear nights to fogging optics.
5. **Practise on the Moon** during planetary downtime — every workflow gain
   transfers directly.

(5-2-next-season-and-beyond)=
### 5.2 Next Season and Beyond — Hardware Upgrade Decision

Make the upgrade decision *based on your own stacked images*, not on forum
advice. Specifically, ask:

- Are your best 2026–27 stacks *clearly limited by image scale* (planet too
  small even with Barlow)? → 127 MAK helps most.
- Are they limited by *noise* (too few photons in short exposures)? →
  bigger aperture (127 or 150) helps.
- Are they limited by *seeing* (random blur that wavelets can't fix)? →
  no telescope upgrade will help; consider a travel trip to lower latitude
  instead, or accept Oslo's reality.

> 💡 **A heuristic:** if 30% or more of your individual *best* video frames
> already look diffraction-limited at 1250 mm, you have room to grow with
> aperture. If under 10% do, you are seeing-limited and should not upgrade
> the optics yet.

(5-3-what-not-to-buy-yet)=
### 5.3 What *Not* to Buy Yet

- **A dedicated planetary camera (ASI224MC etc.)** — eventually a real
  upgrade, but only after the A7C II workflow is mature. The A7C II is
  perfectly capable of getting you to "Great Red Spot visible" results.
- **A 3× Barlow** — empty magnification on a 90 mm.
- **An EQ mount upgrade** — irrelevant for short-clip planetary lucky imaging.
  Only relevant if you start chasing deep-sky.
- **Expensive eyepieces** — for *imaging* you don't use eyepieces at all.
  Spend the money on a Barlow and a dew shield.

---

(6-one-paragraph-summary)=
## **6. One-Paragraph Summary**

From Oslo at 59° N, planetary astrophotography is a **roughly seven-month season
(October through April)** built on **short-exposure video + lucky imaging stacking**
— with November–February as the technical optimum and March–April as the most
physically pleasant nights to actually be outside. Your 90 SLT plus A7C II
already has more capability than your current single-still workflow extracts;
moving to 1080p 50–60 fps clips at 1/80–1/125 s, processed through PIPP →
AutoStakkert → RegiStax, will produce visibly better Jupiter images than any
hardware upgrade at this stage. A **2× Barlow** is the right *first* purchase
once that pipeline is working. A **127 SLT MAK** is the right *conservative*
telescope upgrade — same mount, optimised for planets, ~1.4× the resolution
and 2× the light. A **NexStar 6 SE** is the right *ambitious* upgrade — ~1.7×
the resolution and 2.8× the light, but heavier, slower to cool, and likely
overkill until your processing has matured. In all cases, the ceiling is
**Oslo seeing**, not Oslo gear.
