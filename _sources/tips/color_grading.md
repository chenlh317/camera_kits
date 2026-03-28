# Color Grading: In-Camera & Post-Processing Tips <!-- omit in toc -->

- **Date:** March 2026
- **Camera Body:** Sony A7C II (Full-Frame, E-Mount)
- **Current Lenses:** Sigma 20-200mm f/3.5-6.3, SIRUI Aurora 35mm f/1.4, Viltrox AF 85mm f/2.0 Evo
- **Creative Look Foundations:** FL (Film) and IN (Instant)
- **Post-Processing Software:** Adobe Photoshop, Adobe Lightroom Classic
- **Context:** Practical color grading for a casual photographer — prioritize
  in-camera presets that look great straight out of camera (SOOC),
  with PC post-processing as a secondary skill for special edits

---

(color-grading-executive-summary)=
## 📋 Executive Summary

**Your philosophy is efficiency: get great color in-camera so you rarely need to sit at a PC.**
Sony's Creative Looks on the A7C II let you bake a color grade into your JPEGs (and video)
at the moment of capture. This chapter builds on **FL (Film)** and **IN (Instant)** —
the two looks you already like — with targeted fine-tuning for your real-world scenarios.

(why-fl-and-in-are-strong-foundations)=
### Why FL and IN Are Strong Foundations

| Creative Look    | Character                                                  | Strengths                                                                | Best Suited For                                                        |
| ---------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **FL (Film)**    | Warm highlights, desaturated shadows, gentle roll-off      | Nostalgic, organic feel; flattering skin tones; forgiving in mixed light | Portraits, golden-hour cityscapes, travel memories, museums            |
| **IN (Instant)** | Punchy contrast, boosted saturation, slightly faded blacks | Vibrant, high-impact; makes colors pop; strong visual presence           | Daytime cityscapes, nature landscapes, street photography, bold scenes |

**Key insight:** FL leans warm and gentle (people-centric), IN leans vivid and punchy (scene-centric).
Between these two, you cover most casual shooting — the fine-tuning below
lets you adapt each to specific scenarios without starting from scratch.

> ⚠️ **Known issue with FL — the "stiff" (愣) look:**
> FL out of the box can sometimes look cold, hard, and overly digital — especially in:
> indoor mixed-light scenes, grey city streets without sky/greenery, and close-up portraits.
> This is because FL's default emphasizes sky blue and greenery green while maintaining
> high contrast and edge sharpness. The result: colors feel "present but rigid" instead of organic.
> The fix is NOT to switch away from FL, but to **tame its aggressiveness** —
> pull down Contrast, Highlights, and Clarity, and add a **WB Shift of A+1 / M+1**
> to counteract FL's tendency toward a blue-green tint.
> All FL-based recommendations below already incorporate these fixes.

> 💡 **When FL doesn't work — alternative Creative Looks:**
> In certain situations, even fine-tuned FL may not be the best choice:
> - **Harsh midday sun portraits:** PT (Portrait) handles skin more gracefully under hard top-light
> - **Bright, colorful indoor scenes (markets, malls, LED-heavy):** SH (Soft Highlight) renders
>   mixed artificial lighting more cleanly than FL
> - **When you want maximum skin safety:** IN with reduced saturation is the most "un-ruinable"
>   base for faces — it's not the most characterful, but it has the highest success rate
>
> You don't need to memorize this — just know that if FL looks wrong and tweaks don't help,
> try PT (for people) or SH (for vibrant indoor scenes) as fallbacks.

(color-grading-quick-reference)=
### Quick Reference: Which Look for What

| Scenario                                       | Base Look | Why                                                       |
| ---------------------------------------------- | --------- | --------------------------------------------------------- |
| **Portraits (friends, strangers, cosplayers)** | FL        | Warm, flattering skin; soft contrast hides blemishes      |
| **Cityscape — daytime**                        | IN        | Punchy color makes architecture and signage pop           |
| **Cityscape — night**                          | FL        | Gentle highlight roll-off tames neon/harsh street lights  |
| **Nature landscapes**                          | IN        | Vivid greens, blues, and earth tones for maximum impact   |
| **Piano recording at home**                    | FL        | Warm, cinematic mood; gentle on indoor mixed lighting     |
| **Museums (classical art)**                    | FL        | Preserves painting warmth; doesn't over-saturate pigments |

---

```{contents}
:depth: 3
```

---

(0-color-grading-theory)=
## **0. How Color Grading Actually Works — The Theory Behind the Numbers**

Before dialing in specific values, it helps to understand *what each parameter does
to your image* and *how they interact*. This section explains the mechanism
so you can improvise confidently instead of memorizing preset tables.

(the-tonal-range-mental-model)=
### The Tonal Range — Your Mental Model

Every pixel in a photo has a **luminance value** from pure black (0) to pure white (255).
Color grading parameters carve this 0–255 range into zones and let you push each zone
brighter or darker. Think of it as a stack of layers:

```
  255 ──── Highlights (brightest 20-25% of pixels)
   │
   │       Clarity operates here
   │       ↕ (mid-tone contrast)
   │
  128 ──── Midtones (the bulk of your image — skin, buildings, foliage)
   │
   │       Contrast stretches or compresses this entire range
   │       ↕
   │
   30 ──── Shadows (darkest 20-25% of pixels)
   │
   │       Fade lifts this floor
   │       ↕
    0 ──── Black point
```

**Key insight:** Highlights, Shadows, and Fade target *specific zones*,
while Contrast and Clarity affect the *relationship between zones*.
Understanding which zone you're targeting is the difference between
a purposeful adjustment and random slider-pushing.

(parameter-deep-dive)=
### What Each Parameter Actually Does

**(1) Contrast — Global Tonal Separation**

Contrast controls the *distance* between the darkest and brightest tones.

- **Positive contrast** (+): Darks get darker, brights get brighter → more "punch," more drama.
  The tonal range *stretches* — small differences in tone become visible.
- **Negative contrast** (−): Darks lift, brights dim → flatter, softer image.
  The tonal range *compresses* — the image looks gentler, more "matte."

**Interaction:** Contrast is the broadest brush. It affects highlights, midtones,
and shadows simultaneously. If you push Contrast high (+2 or more),
you may need to *pull Highlights negative* to prevent the bright end from clipping,
and *push Shadows positive* to keep dark areas readable.
This "Contrast up / Highlights down / Shadows up" trio is the single most common
combination in color grading — it adds perceived punch while preserving detail at both ends.

**(2) Highlights — Bright Area Control**

Highlights target roughly the top 20-25% of the tonal range:
sky, white clothing, reflections, bright skin patches, light sources.

- **Negative** (−): Recovers blown-out detail (clouds reappear, skin texture returns).
  This is *the most frequently used negative adjustment* in photography.
- **Positive** (+): Brightens already-bright areas. Rarely useful — usually causes clipping.

**Interaction with Contrast:** When you raise Contrast, highlights get pushed brighter.
Pulling Highlights negative *selectively undoes* that brightness in the top zone
without affecting the midtone punch you added. That's why "Contrast +1, Highlights −2"
is a staple pairing — you get the midtone energy of higher contrast
while protecting the sky/skin highlights.

**(3) Shadows — Dark Area Control**

Shadows target roughly the bottom 20-25% of the tonal range:
under-chin shadows, dark alleys, shadowed building facades, eye sockets.

- **Positive** (+): Lifts dark areas → reveals hidden detail, opens up shadows.
- **Negative** (−): Crushes dark areas → dramatic, high-contrast look with deep blacks.

**Interaction with Contrast:** Raising Contrast pushes shadows darker.
Pushing Shadows positive *selectively undoes* that darkening in the bottom zone.
This is the mirror of the Highlights trick: "Contrast +1, Shadows +1"
keeps the midtone punch but prevents shadow detail from being lost.

**Interaction with Fade:** Both Shadows and Fade affect the dark end,
but differently. Shadows *reveals detail* in dark areas (like turning up a dimmer
in a dark room — you see more stuff). Fade *lifts the black floor itself*
(like adding fog to the room — the darkest point is no longer black, it's dark grey).
They can stack: Shadows +1 + Fade 1 creates a very open, airy shadow rendering.
Or they can be used independently for different effects.

**(4) Fade — Black Point Lift**

Fade lifts the absolute black point of the image. Instead of true black (0),
the darkest pixel becomes dark grey (~20-40 on the 0–255 scale).

- **Higher values** (1-9): Matte, filmic look. Blacks become milky/faded. Classic film print look.
- **Zero (0):** Solid, punchy blacks. More "digital" / modern look. No fade applied.

> ⚠️ **A7C II range: 0 to 9 only.** There are no negative Fade values.
> Zero means no black-point lift; higher values progressively lift the black floor.

**Why Fade matters:**
This single parameter is responsible for the "film vs digital" divide in modern photography.
Film negatives physically cannot produce absolute black — there's always base density
in the film emulsion. Fade simulates this. It's why FL (Film) creative look
has inherently lifted blacks, and why adding more Fade to FL enhances the film character.

**Interaction with Contrast:** Fade and Contrast work in *opposite directions*
on the shadow end. High Contrast pushes blacks deeper; high Fade lifts them.
If you set Contrast +2 and Fade 2, the Contrast darkens the shadows
but Fade prevents them from reaching true black — the result is punchy midtones
with matte shadows, a look popularized by cinema color grading.

**(5) Saturation — Color Intensity**

Saturation controls how vivid or muted all colors are, uniformly across the image.

- **Positive** (+): Colors become more vivid, more "saturated." Greens pop, blues deepen, reds intensify.
- **Negative** (−): Colors become muted, washed-out. At extreme negative, the image approaches monochrome.

**Why restraint matters:** Saturation is the easiest parameter to overdo.
Human perception is non-linear — a small boost looks "better," but excess looks garish.
The difference between +1 (pleasant) and +3 (radioactive) is smaller than you'd think.

**Interaction with Contrast:** Higher Contrast *perceptually* increases saturation —
when tones separate more, colors appear more vivid even without touching the Saturation slider.
This means that if you push Contrast +2, you might want Saturation 0 or even −1
to compensate for the perceived saturation boost. Conversely, low Contrast (−2)
makes the image look naturally desaturated, so you may want Saturation +1 to compensate.

**Interaction with Creative Look base:** FL already desaturates shadows
(warm highlights + muted shadows = "film" look). Adding further negative Saturation
to FL can quickly make the image look too flat. IN starts more vivid,
so it tolerates Saturation +1 or +2 before looking unnatural.

**(6) Sharpness — Edge Acuity**

Sharpness enhances contrast *along edges* — the boundaries between different-toned areas.
It doesn't add real detail; it makes existing edges appear crisper by brightening
the bright side and darkening the dark side of each edge.

- **Higher values** (3-9): Crisper edges, more "defined" look. Good for architecture, text, landscapes.
- **Zero (0):** Minimum sharpening — the softest the camera can produce in-camera.
  For portraits, keep Sharpness at 0 to let skin texture stay smooth.

> ⚠️ **A7C II range: 0 to 9 only.** There are no negative Sharpness values.
> For a "dreamy" soft-focus portrait look, you can't go below 0 in-camera —
> pair Sharpness 0 with a physical diffusion filter (your 1/4 Black Mist)
> or use Lightroom's negative Sharpening in post.

**Why it exists separately from Clarity:**
Sharpness works at the *pixel level* (fine edges), while Clarity works at the *region level*
(larger tonal transitions). You can have high Sharpness with low Clarity
(sharp details in a smooth-toned image — good for portraits with textured clothing)
or low Sharpness with high Clarity (well-defined shapes but soft texturing — unusual).

**(7) Sharpness Range — How Deep the Sharpening Goes**

Sharpness Range controls the *radius* of the sharpening effect —
whether it sharpens only the finest details (low range) or also medium-scale textures.

- **Higher values** (3-5): Sharpening extends to medium-scale textures (brick patterns, tree bark, fabric weave).
- **Minimum (1):** Only fine edges are sharpened.

> ⚠️ **A7C II range: 1 to 5 only.** There are no zero or negative Sharpness Range values.

**Practical rule:** Push Sharpness Range higher only when you also push Sharpness higher.
There's no benefit to extending range if Sharpness is at 0.

**(8) Clarity — Mid-Tone Contrast (Texture & Depth)**

Clarity is *localized contrast in the midtones*. It doesn't affect
the overall bright/dark balance — it enhances (or suppresses) the contrast
*within* the midtone band, making textures and surfaces more (or less) prominent.

- **Higher values** (3-9): Textures pop. Stone grain, cloud structure, leaf detail, building surfaces
  all become more three-dimensional. Can look "gritty" or "HDR-ish" at extreme values.
- **Zero (0):** Minimum midtone contrast — the smoothest available in-camera.
  For portraits, keep Clarity at 0 for the softest skin rendering.

> ⚠️ **A7C II range: 0 to 9 only.** There are no negative Clarity values in-camera.
> The "Orton effect" / "soft glow" look requires negative Clarity in Lightroom (−20 to −40),
> which is one reason to shoot RAW for special portrait edits.

**Interaction with Contrast:** Contrast affects the *global* tonal range;
Clarity affects *local* tonal variation. You can have low global Contrast (flat, matte)
with high Clarity (textured surfaces) — this produces the "matte but detailed" look
used in cinematic color grading. Or high Contrast with low Clarity —
punchy tonal range but smooth surfaces, used for beauty/fashion portraits.

**The key pairing to understand:** Contrast + Clarity together determine
the "visual energy" of the image. Both high → aggressive, punchy (landscape/architecture).
Both at 0 → calm, gentle (portraits/film emulation). One high and one at 0 → specialty looks.

> ⚠️ **In-camera vs Lightroom:** On the A7C II, Sharpness and Clarity bottom out at 0.
> If the "zero" setting isn't soft enough (e.g., beauty portraits), you need either
> a physical filter (Black Mist 1/4) or negative values in Lightroom's Develop module.

(parameter-interaction-map)=
### How Parameters Interact — The Quick Reference Map

Understanding interactions lets you predict what happens when you move multiple sliders:

| Pairing                                   | Effect                                                                               | Common Use                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------ |
| **Contrast ↑ + Highlights ↓**             | Punchy midtones, protected bright areas                                              | Cityscapes, landscapes         |
| **Contrast ↑ + Shadows ↑**                | Punchy midtones, open dark areas                                                     | Street, travel                 |
| **Contrast ↑ + Highlights ↓ + Shadows ↑** | Maximum detail across full range with midtone energy                                 | The "universal" starting combo |
| **Contrast ↓ + Fade ↑**                   | Soft, matte, filmic — the classic "film look"                                        | Portraits, vintage mood        |
| **Contrast ↑ + Saturation ↓**             | Strong structure but muted colors — "desaturated drama"                              | Cinematic, moody night         |
| **Contrast ↓ + Saturation ↑**             | Flat tones but vivid colors — "pastel" look                                          | Whimsical, editorial           |
| **Clarity ↑ + Sharpness ↑**               | Maximum texture and edge definition                                                  | Landscape, architecture        |
| **Clarity 0 + Sharpness 0**               | Smoothest possible in-camera rendering (pair with Black Mist filter for dreamy look) | Portraits, beauty              |
| **Clarity ↑ + Contrast ↓**                | Textured surfaces in a flat tonal field — "cinematic detail"                         | Film-grade color work          |
| **Fade ↑ + Shadows ↑**                    | Very open, airy shadows with matte blacks                                            | Airy portrait, editorial       |
| **Highlights ↓ + Shadows ↑**              | Compressed dynamic range — "HDR-like" detail everywhere                              | Complex scenes, interiors      |

> 💡 **The golden rule of parameter interaction:**
> When two parameters push the *same zone in the same direction*, the effect compounds.
> When they push the *same zone in opposite directions*, they partially cancel out.
> Intentional cancellation is a powerful technique — e.g., Contrast ↑ (darkens shadows) + Shadows ↑
> (brightens shadows) = the shadow zone stays roughly neutral
> while midtones get the contrast boost.

(tonal-curve-visualization)=
### Visualizing It: The Tone Curve Connection

If you've seen a **tone curve** in Lightroom or Photoshop,
the Creative Look parameters map directly onto it:

```
Output                ┌── Highlights ↓ pulls this corner down
(brightness)         ╱     (protects sky/skin from blowing out)
  255 ┤             ╱
      │            ╱
      │           ╱◄── Contrast changes the steepness
      │          ╱      (steeper = more contrast)
      │         ╱
  128 ┤        ╱◄──── Clarity affects the "wiggliness" here
      │       ╱        (more clarity = more local contrast in midtones)
      │      ╱
   30 ┤     ╱◄──── Shadows ↑ lifts this zone
      │        (reveals detail in darks)
      ┤
      ├── Fade ↑ lifts this point off zero
    0 ┤    (no more true black)
      └──┬──┬──┬──┬──┬──┬──┬───
         0     64   128  192   255
              Input (original brightness)
```

**Reading this diagram:**
- The diagonal line represents how input brightness maps to output brightness
- A steeper line = more contrast (small input differences → large output differences)
- Lifting the bottom = Fade (minimum output is no longer zero)
- Pulling down the top = Highlights recovery (maximum output is held back)
- The curve's shape in the middle = Clarity's domain (local midtone contrast)

Once you internalize this mental model, every parameter adjustment makes intuitive sense:
you're simply reshaping how the camera maps "real world light" to "displayed brightness."

(color-vs-tone)=
### Color vs. Tone: Two Independent Dimensions

A final concept: **tone** (the brightness/darkness adjustments above)
and **color** (Saturation, plus White Balance) are *largely independent*.
You can set your tonal rendering first (Contrast, Highlights, Shadows, Fade, Clarity)
and then adjust color (Saturation, WB) without undoing the tonal work.

This is why this chapter separates the topics:
- **Sections 1–2** focus primarily on tonal + color parameters together as practical recipes
- **Section 4** handles White Balance (the *foundation* of color accuracy) separately
- **Section 5** (Leica/Hasselblad emulation) combines both tonal and color adjustments
  for a complete "color science" emulation

**The practical takeaway:**
When your photo looks wrong, diagnose *which dimension* is off:
- If it looks too flat or too harsh → adjust **tone** (Contrast, Highlights, Shadows, Clarity)
- If it looks too warm, too cool, or too vivid → adjust **color** (WB, Saturation)
- Don't use Saturation to fix a Contrast problem, or Contrast to fix a WB problem

---

(1-in-camera-creative-look-fine-tuning)=
## **1. In-Camera Creative Look Fine-Tuning**

On the A7C II, each Creative Look exposes **eight adjustment parameters**
you can dial in: Contrast, Highlights, Shadows, Fade, Saturation, Sharpness,
Sharpness Range, and Clarity. Below are scenario-specific tweaks
starting from your FL and IN bases.

> 💡 **How to access:** Menu → Exposure/Color → Color/Tone → Creative Look →
> select FL or IN → press right arrow to enter fine-tuning sub-menu.
> Each parameter range depends on the type:
> **Contrast, Highlights, Shadows, Saturation:** −9 to +9 (0 = default).
> **Fade, Sharpness, Clarity:** 0 to 9 (no negative values — 0 = minimum).
> **Sharpness Range:** 1 to 5 (no zero value — 1 = minimum).

(fine-tune-portraits)=
### 1.1 Portraits — Based on FL

**Goal:** Warm, flattering skin tones; soft transitions; gentle background rendering.
Works for both your Viltrox 85mm f/2.0 Evo portrait sessions
and casual friend/family shots with the SIRUI 35mm f/1.4.

| Parameter           | Adjustment | Rationale                                                             |
| ------------------- | ---------- | --------------------------------------------------------------------- |
| **Contrast**        | −1 to −2   | Softens skin; reduces harsh shadow lines on faces                     |
| **Highlights**      | −1         | Protects skin highlights from blowing out (esp. bright sunlight)      |
| **Shadows**         | +1         | Opens up eye sockets and under-chin shadows slightly                  |
| **Fade**            | 1          | Lifts the deepest blacks for a gentle, approachable look              |
| **Saturation**      | −1         | Pulls back FL's warmth just enough to keep skin natural, not orange   |
| **Sharpness**       | 0          | Minimum sharpening — lets skin texture stay smooth                    |
| **Sharpness Range** | 1          | Leave at minimum — fine detail sharpness isn't needed for portraits   |
| **Clarity**         | 0          | Minimum micro-contrast — smoothest skin rendering available in-camera |

> **Tip — Pair with the 1/4 Black Mist filter:** Sharpness and Clarity are already
> at their minimum (0) in this preset. For an even softer, dreamier portrait look,
> mount the 1/4 Black Mist filter on the Viltrox 85mm f/2.0 Evo —
> this provides physical diffusion that goes beyond what the camera's 0 setting can achieve.
> For Lightroom post-processing, you can push Clarity negative (−20 to −40) on RAW files
> to add the "Orton glow" that isn't available in-camera.

> **Tip — Indoor portraits (home, restaurants):** Add **+1 Shadows** beyond the above
> to compensate for overhead lighting that creates unflattering under-eye shadows.

(fine-tune-cityscapes)=
### 1.2 Cityscapes — Daylight & Night, Indoor & Outdoor

Cityscapes benefit from a split approach: **IN for daytime punch, FL for nighttime atmosphere**.

**Daytime Cityscapes (outdoor) — Based on IN:**

| Parameter           | Adjustment | Rationale                                                   |
| ------------------- | ---------- | ----------------------------------------------------------- |
| **Contrast**        | +1         | Adds punch to buildings and skylines against the sky        |
| **Highlights**      | −1 to −2   | Protects bright sky areas and white building facades        |
| **Shadows**         | +1         | Opens up shadow detail in narrow streets and alleys         |
| **Fade**            | 0          | Keep IN's default — faded blacks weaken architectural shots |
| **Saturation**      | 0 to +1    | IN is already vibrant; only boost if overcast/flat light    |
| **Sharpness**       | 1          | Crisps up architectural edges and signage                   |
| **Sharpness Range** | 1          | Extends sharpening to fine details (brick, tile, lettering) |
| **Clarity**         | 1 to 2     | Emphasizes building texture and surface detail              |

**Night Cityscapes (outdoor) — Based on FL:**

| Parameter           | Adjustment | Rationale                                                          |
| ------------------- | ---------- | ------------------------------------------------------------------ |
| **Contrast**        | −1         | Prevents neon signs and street lamps from clipping harshly         |
| **Highlights**      | −2 to −3   | Tames bright light sources (neon, LEDs, car headlights)            |
| **Shadows**         | +1 to +2   | Reveals detail in dark building facades and alleyways              |
| **Fade**            | 1 to 2     | Lifts shadows for a cinematic, film-noir mood                      |
| **Saturation**      | 0          | FL's natural warmth is enough; don't oversaturate neon colors      |
| **Sharpness**       | 0          | Night shots rarely benefit from extra sharpening (amplifies noise) |
| **Sharpness Range** | 1          | Leave at minimum at night — less sharpening = cleaner result       |
| **Clarity**         | 0 to 1     | Slight clarity helps building outlines; too much amplifies noise   |

> **Tip — Night shooting on SIRUI 35mm f/1.4:** At f/1.4, point light sources
> naturally bloom into soft circles (bokeh balls). FL's gentle highlight roll-off
> complements this beautifully — don't fight it with aggressive highlight recovery.
> The slight glow IS the night-city mood.

**Indoor Cityscapes (shopping malls, metro stations, lobbies) — Based on FL:**

| Parameter           | Adjustment | Rationale                                                                            |
| ------------------- | ---------- | ------------------------------------------------------------------------------------ |
| **Contrast**        | 0          | Indoor lighting is already controlled; no need to push                               |
| **Highlights**      | −1         | Prevents ceiling light fixtures from blowing out                                     |
| **Shadows**         | +1         | Lifts floor-level shadow areas in large interior spaces                              |
| **Fade**            | 1          | Softens the corporate/sterile feel of artificial lighting                            |
| **Saturation**      | 0 to +1    | Boost slightly if the interior is visually interesting (e.g., colorful market halls) |
| **Sharpness**       | 0          | Standard sharpness is fine for interiors                                             |
| **Sharpness Range** | 1          | Minimum — default                                                                    |
| **Clarity**         | 0 to 1     | Adds definition to architectural details if desired                                  |

(fine-tune-nature)=
### 1.3 Nature Landscapes — Based on IN

**Goal:** Vivid, high-impact landscapes with rich greens, deep blues,
and warm earth tones. Optimized for the Sigma 20-200mm on daytime hikes and scenic viewpoints.

| Parameter           | Adjustment | Rationale                                                         |
| ------------------- | ---------- | ----------------------------------------------------------------- |
| **Contrast**        | +1 to +2   | Strengthens the separation between sky, mountains, and foreground |
| **Highlights**      | −2 to −3   | Preserves cloud detail and prevents sky blow-out                  |
| **Shadows**         | +1 to +2   | Reveals detail in shadowed valleys, forests, and rock faces       |
| **Fade**            | 0          | Keep blacks solid for landscape punch                             |
| **Saturation**      | +1 to +2   | Boosts foliage greens and sky blues — the "postcard" look         |
| **Sharpness**       | 1 to 2     | Crisps up foliage, rock textures, and distant details             |
| **Sharpness Range** | 1          | Extends sharpening reach for distant landscape layers             |
| **Clarity**         | 2 to 3     | Maximizes texture in mountains, clouds, and vegetation            |

> **Tip — Use with CPL filter:** Your CPL filter on the Sigma 20-200mm
> already deepens sky blue and cuts haze. Combined with IN's saturation boost,
> you get vivid landscapes SOOC without any post-processing.
> Rotate the CPL to taste — maximum effect is ~90° to the sun.

> ⚠️ **Watch the saturation ceiling:** IN + Saturation +2 + CPL can push greens
> and blues into unnatural territory on very sunny days.
> If colors look "radioactive" on the rear screen, dial Saturation back to 0.

(fine-tune-piano-recording)=
### 1.4 Piano Performance Video Recording at Home — Based on FL

**Goal:** Warm, cinematic mood for home video. The FL look naturally produces
a "cozy living room concert" vibe that suits piano performance footage.
Since this is video, consistency and gentle grading matter more than punch.

| Parameter           | Adjustment | Rationale                                                             |
| ------------------- | ---------- | --------------------------------------------------------------------- |
| **Contrast**        | −1         | Keeps the dynamic range open for video; prevents harsh clipping       |
| **Highlights**      | −1 to −2   | Protects window light or lamp highlights in the frame                 |
| **Shadows**         | +1 to +2   | Opens up the darker corners of the room; keeps pianist visible        |
| **Fade**            | 1          | Gives a gentle, filmic lift to shadows — adds warmth to the mood      |
| **Saturation**      | 0 to −1    | Slightly desaturated = more "cinematic"; avoids distracting colors    |
| **Sharpness**       | 0          | Video sharpening is handled differently; don't over-sharpen in-camera |
| **Sharpness Range** | 1          | Minimum — default for video                                           |
| **Clarity**         | 0          | Video at high clarity can look artificial; keep neutral               |

> **Tip — Lock your white balance for video:** Auto WB can shift mid-performance
> as you move or room lighting changes slightly. Set a **Custom White Balance**
> or lock to a specific Kelvin value (see [Section 4: White Balance Fine-Tuning](#4-white-balance-fine-tuning))
> before pressing record. Nothing looks worse than color shifting during a piano piece.

> **Tip — SIRUI 35mm f/1.4 is your best video lens here.**
> At f/1.4-f/2.0, you get gorgeous bokeh on the room background,
> the pianist is beautifully isolated, and you gather plenty of light
> even in a living room with just a desk lamp and overhead light.
> The 35mm field of view captures the pianist + part of the piano naturally.

> **Tip — Picture Profile vs Creative Look for video:**
> For casual piano recording, Creative Looks (FL) are perfectly fine —
> they bake in a finished look and require zero post-processing.
> Picture Profiles (like S-Log3 or S-Cinetone) are meant for color grading in post,
> which contradicts your efficiency-first approach.
> **Use Creative Look FL for piano video unless you plan to edit every clip.**

(fine-tune-museums)=
### 1.5 Museums — Classical Artworks (e.g., Louvre) — Based on FL

**Goal:** Faithful color reproduction of paintings, sculptures, and exhibits
under challenging museum lighting (warm tungsten, cool LED, mixed spotlights).
FL's gentle warmth complements classical artwork without distorting pigment colors.

| Parameter           | Adjustment | Rationale                                                                                     |
| ------------------- | ---------- | --------------------------------------------------------------------------------------------- |
| **Contrast**        | −1         | Preserves the tonal range in paintings (dark Baroque works need shadow detail)                |
| **Highlights**      | −1 to −2   | Protects bright areas in paintings (skies, white fabrics in oil paintings)                    |
| **Shadows**         | +1         | Reveals detail in darker painting regions and sculpture cavities                              |
| **Fade**            | 0 to 1     | Slight fade can complement the aged look of classical works; 0 for modern exhibits            |
| **Saturation**      | −1 to −2   | **Critical:** Desaturate slightly to avoid misrepresenting pigment colors under spot lighting |
| **Sharpness**       | 1          | Helps resolve fine brushwork and texture in paintings                                         |
| **Sharpness Range** | 1          | Extends sharpening to the fine details in artwork                                             |
| **Clarity**         | 0 to 1     | Slight clarity brings out surface texture (canvas weave, marble grain)                        |

> **Tip — Saturation restraint is key in museums.**
> Spot-lit paintings under warm tungsten can appear over-saturated in photos
> even at default settings. Pulling saturation back by −1 or −2
> ensures your photos match what your eyes actually saw,
> not a hyper-vivid version. This is especially important for old master paintings
> where accurate color is part of the artwork's character.

> **Tip — Use the SIRUI 35mm f/1.4 for gallery rooms, Viltrox 85mm f/2.0 for painting details.**
> At the Louvre, galleries are often dim — f/1.4 keeps ISO low and images clean.
> For close-ups of specific paintings (brushwork, face details in a portrait),
> swap to the Viltrox 85mm. Remove the Black Mist filter — you want maximum sharpness
> to capture artwork detail.

> **Tip — Shoot RAW+JPEG in museums.** Museums are the one scenario where
> post-processing in Lightroom is most valuable — you can correct white balance
> (notoriously tricky under mixed museum lighting) and recover highlight/shadow detail
> that in-camera processing may clip. The JPEG gives you an instant "good enough" result;
> the RAW is your insurance for special paintings worth editing.

---

(2-three-preset-plans-for-sony-a7c2)=
## **2. Three Ready-to-Use Preset Plans for Your A7C II**

The A7C II allows you to store multiple Creative Look configurations.
Here are three pre-built presets you can save and recall instantly,
covering your three most common scenarios.

> 💡 **How to save:** Dial in the settings below under Creative Look fine-tuning,
> then register to a **Custom Shooting Set** (Menu → Shooting → Shooting Mode →
> MR Memory Recall / M1-M4). Assign each to a memory slot for instant recall.

(preset-1-portrait-warm)=
### Preset 1: "Portrait Warm" — FL-Based

**Use for:** Portraits, friend/family photos, cosplayer shoots, indoor casual shots.

| Parameter       | Value  |
| --------------- | ------ |
| **Base Look**   | **FL** |
| Contrast        | **−2** |
| Highlights      | **−1** |
| Shadows         | **+1** |
| Fade            | **1**  |
| Saturation      | **−1** |
| Sharpness       | **0**  |
| Sharpness Range | **1**  |
| Clarity         | **0**  |

**Character:** Warm, soft, flattering. Skin tones glow without being orange.
Shadows are lifted for an airy feel. Micro-contrast is reduced for smooth skin rendering.

**Pair with:** Viltrox 85mm f/2.0 Evo + 1/4 Black Mist (outdoor portraits),
SIRUI 35mm f/1.4 (indoor/environmental portraits).

**White Balance for this preset:**

| Condition                     | WB Mode  | Kelvin     | WB Shift   | Notes                                            |
| ----------------------------- | -------- | ---------- | ---------- | ------------------------------------------------ |
| **Outdoor daylight**          | Daylight | 5600K      | A+1        | Preserves golden-hour warmth; flatters skin      |
| **Indoor (home, restaurant)** | Custom K | 4000-4500K | A+1 to A+2 | Stable under mixed LED/tungsten                  |
| **Cosplayer / street**        | AWB      | —          | A+1        | Fast-changing light; amber shift keeps skin warm |

(preset-2-city-vivid)=
### Preset 2: "City Vivid" — IN-Based

**Use for:** Daytime cityscapes, street photography, architecture, markets, travel snapshots.

| Parameter       | Value  |
| --------------- | ------ |
| **Base Look**   | **IN** |
| Contrast        | **+1** |
| Highlights      | **−2** |
| Shadows         | **+1** |
| Fade            | **0**  |
| Saturation      | **+1** |
| Sharpness       | **1**  |
| Sharpness Range | **1**  |
| Clarity         | **2**  |

**Character:** Punchy, vivid, sharp. Architecture pops, signage is crisp,
sky colors are deep. The pulled highlights protect bright facades and sky.

**Pair with:** Sigma 20-200mm (daytime sightseeing — your one-lens solution).

**White Balance for this preset:**

| Condition                 | WB Mode         | Kelvin     | WB Shift | Notes                                                                          |
| ------------------------- | --------------- | ---------- | -------- | ------------------------------------------------------------------------------ |
| **Sunny day**             | AWB or Daylight | — / 5600K  | None     | Consistent outdoor light; let the Creative Look set the mood                   |
| **Overcast / flat light** | Cloudy          | 6000K      | None     | Adds slight warmth to prevent clinical grey tones                              |
| **Night city walk**       | Custom K        | 3500-4200K | M+1      | Lock K for consistent neon/street-light rendering; magenta counters green cast |

(preset-3-landscape-bold)=
### Preset 3: "Landscape Bold" — IN-Based

**Use for:** Nature landscapes, scenic viewpoints, parks, gardens, hiking.

| Parameter       | Value  |
| --------------- | ------ |
| **Base Look**   | **IN** |
| Contrast        | **+2** |
| Highlights      | **−3** |
| Shadows         | **+2** |
| Fade            | **0**  |
| Saturation      | **+2** |
| Sharpness       | **2**  |
| Sharpness Range | **1**  |
| Clarity         | **3**  |

**Character:** Bold, dramatic, high-impact. Maximum texture and color depth.
Cloud detail is preserved while shadows reveal forest and valley detail.
This is the "postcard" preset — scenes look stunning straight out of camera.

**Pair with:** Sigma 20-200mm + CPL filter (daytime landscapes).

**White Balance for this preset:**

| Condition            | WB Mode           | Kelvin     | WB Shift | Notes                                                |
| -------------------- | ----------------- | ---------- | -------- | ---------------------------------------------------- |
| **Sunny day**        | Daylight          | 5600K      | None     | Preserves warm sunlight quality on foliage and earth |
| **Golden hour**      | Daylight or Shade | 5600-7000K | A+1      | Shade adds extra warmth for dramatic golden light    |
| **Overcast / shade** | Shade or Cloudy   | 6000-7000K | None     | Counteracts blue cast in open shade                  |
| **Autumn foliage**   | Daylight          | 5600K      | A+1      | Emphasizes reds and oranges in fall colors           |
| **Snow / winter**    | Daylight          | 5600K      | B+1      | Blue shift keeps snow cool/white, not warm/yellow    |

> ⚠️ **Note on Landscape Bold:** This is an aggressive preset.
> On overcast days with flat light, the high Contrast and Clarity settings
> will add welcome drama. On very bright sunny days,
> the Saturation +2 may push colors too far — dial back to +1
> or switch to City Vivid, which is more moderate.

(preset-piano-petrof)=
### Bonus Preset: "Petrof Indoor" — FL-Based (Field-Validated)

**Use for:** Piano performance recording, indoor family life, warm-light home scenes.

This preset was validated through real-world testing: photographing piano practice
at home with warm wood floors, a black Petrof piano, white sheet music, and mixed indoor lighting.
The name comes from the observation that the resulting color palette
resembles the Petrof piano's sound character — warm, woody, with a thick midrange
that isn't overly bright or analytical.

| Parameter       | Value  |
| --------------- | ------ |
| **Base Look**   | **FL** |
| Contrast        | **−1** |
| Highlights      | **−2** |
| Shadows         | **+1** |
| Fade            | **1**  |
| Saturation      | **−1** |
| Sharpness       | **1**  |
| Sharpness Range | **1**  |
| Clarity         | **1**  |

**White Balance:** AWB, **WB Shift: A+2 / M+1**

**Exposure:** +0.3 EV (brightens faces under indoor lighting)

**Why these values (not a copy of one specific photo):**

- **Contrast −1** (not −2): Indoor lighting is inherently lower-contrast than outdoor.
  Pulling too far negative makes the image look flat and lifeless under warm lamps.
  −1 gently tames FL's default punch while keeping indoor surfaces (wood grain, piano lacquer)
  visually separable. For extreme black-piano-vs-white-sheet-music scenes, you can push to −2.
- **Highlights −2** (not −3): Indoor highlights (lamps, white walls, sheet music)
  are less intense than outdoor sky/sun. −2 provides solid protection without dampening
  the overall luminosity that makes indoor scenes feel warm and inviting.
  −3 is only needed if you have direct window light flooding the frame.
- **Shadows +1**: Indoor rooms always have darker corners, under-furniture shadows,
  and shadowed faces from overhead lighting. +1 reveals enough detail
  to keep the room feeling "lived in" rather than cave-like.
- **Fade 1**: Prevents truly crushed blacks on dark furniture, piano bodies,
  and shadowed walls. Adds to the filmic warmth without making the image look washed out.
- **Saturation −1**: FL's desaturated-shadow character already provides mood.
  Pulling back by 1 prevents indoor warm-light from making skin tones too orange
  or wood tones too saturated under tungsten/LED mix.
- **Sharpness 1 / Sharpness Range 1**: Mild sharpening preserves important detail
  (piano keys, hands, sheet music notation, book spines) without the clinical edge
  that makes indoor photos look like product shots. If the scene includes close-up faces,
  you can drop to 0 for softer skin.
- **Clarity 1**: A touch of midtone contrast gives indoor surfaces some dimensionality
  (wood grain, fabric texture, piano lacquer depth) without the "over-processed" harshness
  that high Clarity creates under artificial lighting.

**Character:** Warm, woody, intimate. FL's film-like tonal foundation gives the scene
a nostalgic depth that feels like an evening practice session, not a clinical recording.
Wood tones and skin tones harmonize naturally. The black piano surface retains
subtle warmth rather than becoming a dead black void.

**Pair with:** SIRUI 35mm f/1.4 (captures pianist + part of piano naturally at f/1.4-f/2.0;
bokeh on room background adds a "living room concert" intimacy).

> 💡 **Why FL works here despite being an "outdoor" look:**
> FL's known weakness is its blue-green bias and aggressive contrast —
> but that's the *default* FL. With Contrast −1 and Highlights −2,
> the stiff character is tamed. What remains is FL's core strength:
> its desaturated-shadow / warm-highlight tonal rendering,
> which translates beautifully to indoor scenes with warm wood and warm lighting.
> The WB Shift A+2 / M+1 finishes the job by steering FL away from its green tendency
> and into the warm-amber zone that makes indoor life photos glow.
>
> A neutral base like IN would also work here, but FL's inherent film character
> adds a layer of mood that IN — steady and forgiving as it is — simply doesn't have.
> In field testing, the FL version produced noticeably more emotional depth
> than IN with identical scene and lighting — FL's tonal curves add weight
> to scenes that already have natural warmth. IN renders them accurately but flatly.

> **Tip — This preset also works for:** reading in bed, family dinner tables,
> child playing in the living room, any warm-lit indoor home moment.
> The key is the WB Shift A+2 / M+1 — this steers the entire palette
> into a warm, lived-in register that makes indoor life photos look
> like how the room *feels*, not how the sensor *measured* it.

(preset-comparison-table)=
### Side-by-Side Comparison

| Parameter       | Portrait Warm (FL)  | City Vivid (IN)  | Landscape Bold (IN) |
| --------------- | ------------------- | ---------------- | ------------------- |
| Contrast        | −2                  | +1               | +2                  |
| Highlights      | −1                  | −2               | −3                  |
| Shadows         | +1                  | +1               | +2                  |
| Fade            | 1                   | 0                | 0                   |
| Saturation      | −1                  | +1               | +2                  |
| Sharpness       | 0                   | 1                | 2                   |
| Sharpness Range | 1                   | 1                | 1                   |
| Clarity         | 0                   | 2                | 3                   |
| **WB Mode**     | Daylight / Custom K | AWB / Cloudy     | Daylight / Shade    |
| **WB Shift**    | A+1 to A+2          | None / M+1 night | None / A+1 autumn   |

(practical-shooting-habits)=
### Habits That Matter More Than Parameters

The notes from real-world testing and community experience reveal that
these shooting habits have a bigger impact on SOOC quality than any parameter tweak:

**1. Slight underexposure protects Sony JPEG quality**

Sony JPEGs look their worst when highlights blow out — skin becomes waxy,
skies turn to white voids, and the image screams "digital."
A small exposure compensation prevents this:

| Scenario                          | Exposure Compensation | Why                                                     |
| --------------------------------- | --------------------- | ------------------------------------------------------- |
| **Daytime street / sightseeing**  | **−0.3 EV**           | Protects sky, white walls, and car reflections          |
| **Night city / neon**             | **−0.7 EV**           | Prevents neon signs and LED billboards from blowing out |
| **Portrait — backlit / overcast** | **+0.3 EV**           | Brightens faces that would otherwise go dark            |
| **Portrait — direct sun**         | **0 EV or −0.3 EV**   | Prevents skin highlights from clipping                  |
| **Snow / glacier / bright water** | **−0.7 EV**           | Extreme reflections need more protection                |

> 💡 **The principle:** Shadows can be recovered in post (and your presets already lift them).
> Blown highlights are gone forever in JPEG. When in doubt, protect the highlights.

**2. White balance *direction* matters more than saturation *intensity***

A common beginner mistake is reaching for Saturation +3 to make colors "better."
In practice, adjusting WB Shift by even 1 step has a more natural, impactful effect:

| If you want...              | Don't do this | Do this instead    |
| --------------------------- | ------------- | ------------------ |
| Warmer, more inviting skin  | Saturation +2 | WB Shift A+1 / M+1 |
| Cooler, moodier street feel | Saturation −2 | WB Shift B+1 / G+1 |
| Warm golden-hour emphasis   | Saturation +2 | WB Shift A+2 / M+1 |

> **Why:** Saturation boosts *all* colors equally, making everything louder.
> WB Shift changes the *direction* of color — steering the entire palette warmer/cooler
> or toward magenta/green. Direction change looks natural; intensity change looks filtered.
> Sony's common complaint of looking "greenish and cold" is a WB *direction* problem,
> not a saturation problem — A+1 / M+1 fixes it without touching Saturation at all.

**3. Start conservative, iterate after real shooting**

Don't try to perfect your presets before taking a single photo.
The most effective workflow:

1. Load the presets above into your camera (M1/M2/M3)
2. Shoot for **at least two weeks** across different conditions (sun, cloud, indoor, night)
3. Review your JPEGs and notice patterns:
   - "Portraits still feel a bit cold" → increase WB Shift from A+1 to A+2
   - "Cityscapes still feel too hard" → reduce Clarity by 1 more step
   - "Landscapes aren't punchy enough" → increase Contrast from +1 to +2
4. Adjust **one parameter at a time** and shoot another round

> This iterative approach is more reliable than trying to design the "perfect" preset
> in your head. The presets above are already good starting points —
> real-world refinement makes them *yours*.

---

(3-post-processing-basics-lightroom-photoshop)=
## **3. Post-Processing Basics: Adobe Lightroom Classic & Photoshop**

For most photos, your in-camera Creative Looks are sufficient.
But for special shots — a stunning sunset, a perfectly lit museum painting,
a portrait you want to print — knowing basic post-processing
lets you take a good photo and make it great.

> 💡 **Workflow principle:** Shoot **RAW+JPEG** when you think a scene is worth editing later.
> Use the JPEG as your "instant result" and the RAW as your editing source.
> For everyday snapshots, JPEG-only with Creative Looks is perfectly fine.

(lightroom-classic-essentials)=
### 3.1 Lightroom Classic — Your Primary Editing Tool

Lightroom Classic is where you should do **95% of your editing**.
It's non-destructive (original files are never modified),
has powerful batch processing, and its Develop module maps closely
to the same parameters you already understand from Creative Looks.

**The Develop Module — Six Adjustments That Cover 90% of Edits:**

| Lightroom Slider | What It Does                           | Equivalent Creative Look Parameter       |
| ---------------- | -------------------------------------- | ---------------------------------------- |
| **Exposure**     | Overall brightness                     | (no direct equivalent — global lift/cut) |
| **Contrast**     | Tonal separation                       | Contrast                                 |
| **Highlights**   | Bright area recovery                   | Highlights                               |
| **Shadows**      | Dark area recovery                     | Shadows                                  |
| **Vibrance**     | Smart saturation (protects skin tones) | Saturation (but smarter)                 |
| **Clarity**      | Mid-tone contrast / micro-detail       | Clarity                                  |

> **Tip — Vibrance vs Saturation in Lightroom:**
> Always use **Vibrance** instead of Saturation for general color boosting.
> Vibrance selectively boosts muted colors while protecting already-saturated tones
> and skin tones — it's the "smart" version of saturation.
> Reserve the Saturation slider for deliberate, heavy-handed color effects.

**Basic Editing Workflow (5-minute edit):**

1. **Import RAW files** into Lightroom Classic (File → Import)
2. **Auto tone** (click "Auto" in the Basic panel) — surprisingly good starting point
3. **Fine-tune Highlights** (usually pull negative to recover bright areas)
4. **Fine-tune Shadows** (usually push positive to reveal detail)
5. **Add Vibrance** (+10 to +25 for landscape punch, 0 to +10 for portraits)
6. **Adjust White Balance** if colors look off (see [Section 4](#4-white-balance-fine-tuning))
7. **Crop** if needed (shortcut: R)
8. **Export** (File → Export → JPEG, quality 85-95%, long edge 4000px for sharing)

**Batch Editing — Your Efficiency Superpower:**

The biggest advantage of Lightroom for a casual photographer:
edit one photo, then apply the same adjustments to dozens of similar photos in one click.

1. Edit one photo from a set (e.g., one museum gallery shot)
2. Select all similar photos in the filmstrip
3. Click **Sync Settings** (or Ctrl+Shift+S)
4. Choose which adjustments to apply → Synchronize
5. Fine-tune individual outliers if needed

> **Tip — Create Lightroom Presets that mirror your camera presets.**
> Build a "Portrait Warm," "City Vivid," and "Landscape Bold" preset in Lightroom
> that mimics your in-camera Creative Look settings. Apply them on import
> as a starting point, so your RAW files immediately look like your JPEGs —
> then fine-tune from there.

(photoshop-when-to-use)=
### 3.2 Adobe Photoshop — When to Use It

Photoshop is overkill for 95% of photo editing. Use it **only** for tasks
Lightroom can't do:

| Task                       | Use Photoshop?  | Why                                                              |
| -------------------------- | --------------- | ---------------------------------------------------------------- |
| Color/exposure adjustment  | ❌ Use Lightroom | Lightroom is faster and non-destructive                          |
| Batch processing           | ❌ Use Lightroom | Lightroom handles hundreds of photos; Photoshop is one-at-a-time |
| Remove distracting objects | ✅ Photoshop     | Content-Aware Fill / Generative Fill is superior                 |
| Complex compositing        | ✅ Photoshop     | Layers, masks, blending modes                                    |
| Deep skin retouching       | ✅ Photoshop     | Frequency separation, dodge & burn                               |
| Text/graphic overlays      | ✅ Photoshop     | Add watermarks, titles, or graphics to photos                    |
| Sky replacement            | ✅ Photoshop     | AI-powered sky replacement (Select → Sky)                        |

**Practical Photoshop uses for your style:**

- **Remove tourists from museum shots:** Photoshop's Generative Fill can erase
  people blocking your view of a painting or sculpture. Shoot 3-5 frames,
  then use Photoshop to combine them or use Content-Aware Fill on a single frame.
- **Clean up distractions:** Wires, trash cans, signs that ruin a landscape composition.
- **Sky replacement for travel photos:** If that one perfect cityscape has a blown-out white sky,
  Photoshop's sky replacement can add a dramatic cloud layer.

> **Workflow tip:** Edit in Lightroom first (global adjustments), then "Edit in Photoshop"
> (right-click → Edit In → Adobe Photoshop) for pixel-level fixes.
> Photoshop saves back into your Lightroom catalog automatically.

---

(4-white-balance-fine-tuning)=
## **4. White Balance Fine-Tuning**

White balance (WB) is the single most impactful color setting —
the wrong WB makes everything look too blue (cold) or too orange (warm),
and no amount of Creative Look fine-tuning can fix a bad WB foundation.

> 💡 **From real-world testing: Sony's most common color problem is not saturation, but WB direction.**
> The A7C II default rendering often leans slightly green and cool,
> especially under mixed or artificial lighting. This is why many Sony users find
> their photos look "clinical" or "cold" even with warm Creative Looks like FL.
> A simple **WB Shift of A+1 / M+1** (amber + magenta) often fixes 80% of Sony's
> color complaints without touching Saturation at all.

(wb-how-sony-a7c2-handles-it)=
### 4.1 How the A7C II Handles White Balance

| WB Mode          | Kelvin Range   | Best For                                                |
| ---------------- | -------------- | ------------------------------------------------------- |
| **AWB (Auto)**   | Camera decides | General shooting, changing conditions                   |
| **Daylight**     | ~5600K         | Outdoor sun, preserves warm golden-hour tones           |
| **Shade**        | ~7000K         | Open shade (adds warmth to counteract blue shade light) |
| **Cloudy**       | ~6000K         | Overcast days (slight warming)                          |
| **Incandescent** | ~3200K         | Warm tungsten/filament indoor lighting                  |
| **Fluorescent**  | ~4000K         | Office/commercial fluorescent lights                    |
| **Flash**        | ~5500K         | Fill flash photography                                  |
| **Custom K**     | 2500-9900K     | Manual Kelvin — full control                            |
| **Custom WB**    | Measured       | Gray card / white reference — most accurate             |

(wb-use-case-recommendations)=
### 4.2 White Balance by Use Case

**Portraits:**

- **Outdoor daylight:** AWB is reliable. For golden-hour portraits,
  switch to **Daylight (5600K)** to preserve the warm tones —
  AWB often "corrects" golden hour and removes the warmth you want.
- **Indoor (home, restaurants):** **Custom K at 4000-4500K** for mixed LED/tungsten environments.
  AWB tends to oscillate between warm and cool under mixed indoor lighting.
- **Fine-tune:** Add **A+1 to A+2** (Amber shift) on the A7C II's WB fine-tuning screen
  (Menu → Exposure/Color → White Balance → WB Shift). This adds a subtle warm bias
  that flatters skin in all lighting conditions.

**Cityscapes — Daytime:**

- **AWB** works well in consistent outdoor light.
- **Overcast days:** Switch to **Cloudy (6000K)** to add slight warmth —
  otherwise AWB makes overcast city shots look clinical and grey.
- **Fine-tune:** Neutral — no shift needed.
  Let the Creative Look handle the mood, not the WB.

**Cityscapes — Night:**

- **Custom K at 3500-4200K** depending on dominant light source.
  Night city lighting is the most challenging WB scenario:
  neon signs, sodium street lamps, LED billboards, and tungsten shop windows
  all coexist at wildly different color temperatures.
- **Do NOT use AWB at night.** AWB shifts between frames as you point at different light sources,
  creating inconsistent colors across your night photo series.
- **Strategy:** Set a Custom K at the start of your night walk and leave it.
  ~3800K is a good starting point for Asian night markets;
  ~4200K for European city streets with more LED/cool lighting.
- **Fine-tune:** Add **M+1** (Magenta shift) to counteract the green cast
  from sodium/fluorescent street lighting.

**Nature Landscapes:**

- **Daylight (5600K)** for sunny conditions — preserves the warm quality of direct sunlight.
- **Shade (7000K)** when the landscape is in open shade or when you want extra warmth in golden hour.
- **AWB** is acceptable here — outdoor natural light is the easiest WB scenario.
- **Fine-tune:** For autumn foliage, add **A+1** to emphasize warm tones.
  For snowy landscapes, switch to **Daylight** and add **B+1** (Blue shift)
  to keep snow looking cool/white rather than warm/yellow.

**Piano Recording at Home:**

- ⚠️ **Never use AWB for video.** AWB shifts during recording = color drift mid-performance.
- **Custom White Balance is ideal:** Hold a white card or piece of paper
  under your room's lighting, then Menu → Exposure/Color → White Balance →
  Custom Setup → capture reference. This gives the most accurate result.
- **Alternative:** Set **Custom K** to match your room lighting:
  - LED ceiling light: ~4500-5500K
  - Warm lamp (tungsten/filament bulb): ~2800-3200K
  - Mixed: ~3800-4200K (compromise)
- **Fine-tune:** For a warmer, cozier "concert" feel, add **A+1 to A+2**
  after setting the correct base K value. This intentional warm shift
  adds cinematic character while the correct base K prevents skin from going orange.

**Museums (Classical Artworks):**

- **Custom K at 3200-3800K** for traditional museums with warm tungsten spot-lighting
  (Louvre galleries, most old European museums fall in this range).
- **Custom K at 4500-5000K** for modern museum wings with LED lighting.
- **AWB is risky in museums:** Gallery-to-gallery lighting changes dramatically
  (warm spotlights on paintings vs. cool LED hallways), causing color inconsistency.
- **Best practice:** Set Custom K as you enter each gallery and take a test shot.
  If the painting whites look neutral on the rear screen, you're close enough.
  Fine-tune in Lightroom later for critical shots (RAW+JPEG workflow).
- **Fine-tune:** For warm-toned Old Master paintings (Rembrandt, Vermeer, Caravaggio),
  keep WB slightly warm (A+1) rather than clinically neutral —
  these paintings were made to be viewed by candlelight, and a slight warm bias
  honors that.

(wb-quick-reference-table)=
### 4.3 White Balance Quick Reference

| Scenario                    | WB Mode         | Kelvin (if Custom K)  | WB Shift          | Notes                                |
| --------------------------- | --------------- | --------------------- | ----------------- | ------------------------------------ |
| **Portrait — outdoor**      | Daylight        | 5600K                 | A+1               | Preserves golden hour; flatters skin |
| **Portrait — indoor**       | Custom K        | 4000-4500K            | A+1 to A+2        | Stable under mixed indoor lighting   |
| **Cityscape — day**         | AWB or Cloudy   | — / 6000K             | None              | AWB is fine in consistent light      |
| **Cityscape — night**       | Custom K        | 3500-4200K            | M+1               | Lock K to avoid frame-to-frame shift |
| **Nature — sunny**          | Daylight        | 5600K                 | None / A+1 autumn | Preserves natural warmth             |
| **Nature — shade/overcast** | Shade or Cloudy | 6000-7000K            | None              | Adds warmth to counteract blue       |
| **Piano video**             | Custom WB or K  | 3200-5000K (per room) | A+1 to A+2        | **Lock before recording — no AWB**   |
| **Museum — tungsten**       | Custom K        | 3200-3800K            | A+1               | Honors warm classical painting tones |
| **Museum — LED**            | Custom K        | 4500-5000K            | None              | Modern gallery lighting              |

---

(5-leica-hasselblad-color-emulation)=
## **5. Emulating Leica, Hasselblad & China Photo Studio Color Science on Your A7C II**

Leica, Hasselblad, and China Photo Studio (中国照相馆) each developed legendary,
distinctive color rendering through decades of craft. While you can't perfectly
replicate their sensor/processing/hand-coloring pipelines on a Sony,
you can get surprisingly close by understanding *what* makes their colors special
and tuning your A7C II's Creative Looks + Lightroom to approximate the character.

(leica-color-character)=
### 5.1 Leica Color Character

**What makes Leica color distinctive:**

- **Rich, warm midtones** — skin tones are warm but never orange; greens lean olive/warm
- **Controlled, non-crushed shadows** — deep blacks with subtle detail retained
- **Smooth highlight roll-off** — highlights transition gradually, never harsh
- **Restrained saturation** — colors feel "present" but not pushed; understated elegance
- **Slight warm color cast** — the overall image leans subtly amber/warm
- **Classic "Leica glow"** — a combination of gentle contrast and warm-toned rendering

**In-Camera Emulation — FL Base + Leica-Style Tweaks:**

| Parameter           | Adjustment   | Why                                                                                       |
| ------------------- | ------------ | ----------------------------------------------------------------------------------------- |
| **Base Look**       | **FL**       | FL's warm, filmic character is the closest Sony base to Leica's rendering                 |
| **Contrast**        | **−1 to −2** | Leica images have gentle, restrained contrast                                             |
| **Highlights**      | **−2**       | Smooth highlight roll-off is a Leica signature                                            |
| **Shadows**         | **+1**       | Lifted shadows — Leica retains shadow detail without crushing                             |
| **Fade**            | **2**        | Lifted blacks = Leica's "never truly black" shadow rendering                              |
| **Saturation**      | **−2 to −3** | Leica's restrained saturation — colors present but not vivid                              |
| **Sharpness**       | **0**        | Minimum sharpening — Leica's "drawing" quality is gentle, not clinical                    |
| **Sharpness Range** | **1**        | Minimum — default                                                                         |
| **Clarity**         | **0**        | Minimum clarity — smooth, gentle rendering (go negative in Lightroom for full Leica glow) |

> **Tip — The Leica look is about restraint.**
> Where IN pushes saturation and clarity UP, the Leica emulation keeps everything at minimum.
> The image should feel calm, warm, and "analog" — like a beautifully exposed film negative.
> For the full Leica glow in post, apply negative Clarity (−15 to −25) in Lightroom
> to go softer than what the A7C II's in-camera Clarity 0 can achieve.

**White Balance — warm amber foundation:**

Leica's warmth lives on the amber axis — golden, not pink.
The WB strategy is to add a gentle amber push without any magenta,
keeping the palette in the warm-gold family that defines the Leica character.

| Scenario                              | WB Mode  | Kelvin     | WB Shift | Why                                                                             |
| ------------------------------------- | -------- | ---------- | -------- | ------------------------------------------------------------------------------- |
| **Street portraits — daylight**       | Daylight | 5600K      | **A+1**  | Preserves golden-hour warmth; amber push matches Leica's warm midtone signature |
| **Street portraits — overcast**       | Cloudy   | 6000K      | **A+1**  | Cloudy adds base warmth; A+1 finishes the Leica amber cast                      |
| **Environmental / travel — daylight** | Daylight | 5600K      | **A+1**  | Consistent warm rendering across a travel series                                |
| **Golden hour / sunset**              | Daylight | 5600K      | **None** | Golden hour is already warm enough — adding more risks orange skin              |
| **Indoor — warm lighting**            | Custom K | 3800-4500K | **A+1**  | Lock K to avoid AWB drift; amber push adds Leica warmth on top of accurate base |
| **Night street**                      | Custom K | 3500-4000K | **A+1**  | Locked K prevents frame-to-frame shift; amber keeps the mood warm, not clinical |

> 💡 **Key principle — Leica warmth is pure amber, not rose.**
> Use **A+1 only** — no magenta shift. If you add M+1, you start drifting
> toward the China Photo Studio rose territory. Leica's character is gold-amber,
> and the A-axis alone delivers this. The restrained Saturation (−2 to −3)
> ensures the amber shift stays subtle rather than turning everything orange.

> **Tip — Don't use AWB for Leica emulation.**
> AWB can neutralize the warm cast you're deliberately building.
> Daylight or locked Custom K preserves the intentional warmth across an entire shoot,
> giving your photos the consistent amber palette that makes Leica images recognizable.

**Post-Processing in Lightroom — Leica Refinement:**

After importing your RAW files, apply these on top of baseline exposure adjustments:

1. **Tone Curve:** Lift the bottom-left point (shadow end) up slightly —
   this prevents true black and mimics Leica's shadow rendering.
   Pull the top-right point (highlight end) down slightly for controlled highlights.
2. **HSL — Hue:** Shift Orange toward Yellow by −5 to −10 (warms skin without going orange).
   Shift Green toward Yellow by +10 to +15 (olive/warm greens = Leica signature).
3. **HSL — Saturation:** Pull Blues −10, Greens −10, Reds −5 (across-the-board restraint).
4. **HSL — Luminance:** Push Orange +10 (brightens skin), pull Blue −10 (darkens skies slightly).
5. **Split Toning / Color Grading:** Add a subtle warm tone to shadows
   (Orange-Amber, ~10-15% saturation); slight warm highlight tone (~5% saturation).
6. **Calibration tab:** Shift Red Primary Hue to +5, Blue Primary Hue to −5.
   This subtly warms the overall rendering at the sensor level.

> 💡 **Save as a Lightroom preset** named "Leica Classic" and apply on import
> to any batch of photos you want this treatment.

(hasselblad-color-character)=
### 5.2 Hasselblad Color Character

**What makes Hasselblad color distinctive (HNCS — Hasselblad Natural Colour Solution):**

- **Extremely accurate, neutral color** — "what your eyes saw" fidelity
- **Wide tonal range** — smooth gradations from highlights to shadows
- **Gentle, natural saturation** — colors are rich but true-to-life, never artificial
- **Cool-neutral shadows** — where Leica warms shadows, Hasselblad keeps them neutral/cool
- **Refined highlight handling** — very smooth roll-off in medium-format style
- **"Medium format look"** — largely a function of shallow DoF + wide tonal range,
  partially replicable with fast primes on full-frame

**In-Camera Emulation — FL Base + Hasselblad-Style Tweaks:**

| Parameter           | Adjustment   | Why                                                                                                     |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| **Base Look**       | **FL**       | FL provides the smooth tonal foundation; alternatively start from **ST (Standard)** for more neutrality |
| **Contrast**        | **−2**       | Hasselblad images have very gentle, wide-range contrast                                                 |
| **Highlights**      | **−2 to −3** | Ultra-smooth highlight roll-off — medium-format hallmark                                                |
| **Shadows**         | **0 to +1**  | Shadows maintained but not aggressively lifted (Hasselblad keeps shadow structure)                      |
| **Fade**            | **0 to 1**   | Minimal fade — Hasselblad retains true blacks more than Leica                                           |
| **Saturation**      | **−1 to −2** | Natural, true-to-life; less desaturated than Leica, but not vivid                                       |
| **Sharpness**       | **0**        | Neutral sharpness — Hasselblad's look relies on lens resolving power, not digital sharpening            |
| **Sharpness Range** | **1**        | Minimum — default                                                                                       |
| **Clarity**         | **0**        | Neutral clarity — the medium-format "smoothness" comes from low clarity                                 |

> **Tip — Hasselblad vs Leica in one sentence:**
> Leica says "warm and nostalgic"; Hasselblad says "accurate and refined."
> If you want emotion, go Leica-style. If you want fidelity, go Hasselblad-style.

**White Balance — neutral accuracy above all:**

Hasselblad's HNCS philosophy is "show the scene as it was."
The WB strategy is the opposite of Leica: *remove* color casts rather than *add* them.
The goal is a perfectly neutral, true-to-life foundation that lets the scene's own colors speak.

| Scenario                          | WB Mode         | Kelvin     | WB Shift        | Why                                                                                    |
| --------------------------------- | --------------- | ---------- | --------------- | -------------------------------------------------------------------------------------- |
| **Landscape — sunny**             | Daylight        | 5600K      | **None**        | Accurate outdoor rendering; let the scene's natural warmth come through unaltered      |
| **Landscape — overcast / shade**  | Cloudy or Shade | 6000-7000K | **None**        | Compensates for blue cast in shade — restoring neutral, not adding warmth              |
| **Architecture — daylight**       | Daylight        | 5600K      | **None**        | Neutral rendering preserves material colors (stone, glass, metal) accurately           |
| **Architecture — mixed / indoor** | Custom K        | 4000-5000K | **None**        | Match the dominant light source; Hasselblad look demands accurate WB, not mood WB      |
| **Portrait — outdoor**            | Daylight        | 5600K      | **None**        | Completely neutral skin — Hasselblad renders skin as-is, never flatters or warms       |
| **Portrait — indoor**             | Custom K        | 4000-4800K | **None or G+1** | Custom K for accuracy; optional G+1 counters tungsten's magenta cast for pure neutral  |
| **Golden hour**                   | Daylight        | 5600K      | **B+1**         | Counteract excessive warmth — Hasselblad preserves golden light but doesn't amplify it |

> 💡 **Key principle — Hasselblad warmth comes from the scene, not the camera.**
> Use **no WB Shift** in most conditions. Where Leica *adds* amber warmth (A+1)
> and China Photo Studio *adds* rose warmth (A+2/M+2), the Hasselblad approach
> *removes* any camera-introduced cast. If the scene itself is warm (golden hour, tungsten),
> that warmth shows through naturally — but it's the scene's warmth, not yours.

> **Tip — AWB is actually acceptable for Hasselblad emulation.**
> Unlike Leica and China Photo Studio where you need to *build* a deliberate color cast,
> the Hasselblad look benefits from AWB's neutralizing behavior.
> AWB's goal (remove color casts) aligns with Hasselblad's goal (show accurate color).
> Use AWB when conditions change rapidly (travel walk, mixed indoor/outdoor);
> switch to Daylight or Custom K when you want frame-to-frame consistency.

> **Tip — The B+1 golden-hour trick:** Hasselblad images of sunsets
> look different from Leica images of the same sunset — they're still warm,
> but with restraint. A subtle **B+1** (Blue shift) at golden hour
> pulls back some of the extreme warmth, producing the "refined, not screaming"
> golden-hour rendering that medium-format Hasselblad images are known for.
> Don't push to B+2 — that kills the mood entirely.

**Post-Processing in Lightroom — Hasselblad Refinement:**

1. **Tone Curve:** Very subtle S-curve — barely perceptible contrast boost.
   Keep the curve gentle; Hasselblad avoids heavy contrast manipulation.
2. **HSL — Hue:** Minimal changes. Shift Green slightly toward Cyan by +5 (cooler, truer greens).
   Keep skin tones (Orange) completely unshifted — Hasselblad prides itself on accurate skin.
3. **HSL — Saturation:** Reduce globally by −5 to −10 across all channels.
   The goal is "rich but not pushed."
4. **HSL — Luminance:** Moderate adjustments only.
   Push Skin (Orange) +5 for glow; pull Blue −5 for slightly deeper skies.
5. **Color Grading:** Keep shadows **neutral** — no warm/cool tinting.
   Add an extremely subtle blue-grey tone to shadows if anything (~5% saturation, blue-grey hue).
   Highlights: completely neutral.
6. **Calibration tab:** Minimal changes. Shift Blue Primary Saturation −5
   to reduce any blue-channel excess. Keep Red and Green at default.

> 💡 **Save as a Lightroom preset** named "Hasselblad HNCS" and apply selectively
> to your best landscape and architectural shots — this look rewards
> technically clean images with good exposure.

(china-photo-studio-color-character)=
### 5.3 China Photo Studio (中国照相馆) Color Character

China Photo Studio (中国照相馆), founded in 1937 in Shanghai and later relocated
to Beijing's Wangfujing Street, is one of China's most iconic photography institutions
— a "China Time-Honored Brand" (中华老字号). For decades it defined what a
"proper portrait" looked like for Chinese families: the studio photographed
everyone from national leaders to newlyweds, producing millions of portraits
that became the visual standard of Chinese portraiture from the 1950s through the 1980s.

Their signature look comes from a unique historical convergence:
the era's reliance on **hand-colored black-and-white prints** (手工着色),
combined with carefully controlled studio lighting and meticulous retouching.
Even after color film became standard, the aesthetic DNA persisted —
colors are *applied with restraint and intention*, never left to chance.

**What makes China Photo Studio color distinctive:**

- **Rosy, porcelain skin tones** — the defining signature. Skin has a warm pink-peach
  undertone, never the amber-orange of Western golden-hour photography.
  Think "porcelain with a blush" — luminous, smooth, slightly idealized
- **Warm rose-amber overall cast** — the entire image leans toward a warm
  rose-amber palette, distinctly different from Leica's pure amber warmth.
  There is always a hint of magenta/pink in the warmth
- **Moderate, flattering contrast** — softer than modern digital but not flat.
  Shadows exist for dimensionality but never cut harshly across faces.
  The hand-coloring heritage demanded gentle tonal foundations
- **Rich, deep reds without garish saturation** — clothing reds, lip color, and
  background reds are wine-to-vermillion, never neon. Saturation is present
  but refined — colors feel *painted on* rather than *blasted in*
- **Slightly elevated black point** — hand-coloring over silver gelatin prints
  never produced absolute black. The deepest tones carry a subtle warm density
  rather than a digital void
- **Muted, harmonious backgrounds** — backgrounds are desaturated relative to the subject,
  directing all attention to the person. Deep maroon, muted green, and neutral grey
  were typical studio choices
- **Smooth, idealized skin with preserved structure** — retouching smooths blemishes
  but maintains facial bone structure and dimensionality.
  The result looks "better than reality" without looking fake

> 💡 **China Photo Studio vs Leica in one sentence:**
> Leica says "amber warmth and nostalgic restraint"; China Photo Studio says
> "rose warmth and porcelain refinement." The key difference is in the *hue* of warmth:
> Leica leans amber-gold (A-axis); China Photo Studio leans amber-rose (A+M axes).

**In-Camera Emulation — FL Base + China Photo Studio Tweaks:**

FL is the natural starting point: its warm-highlight / desaturated-shadow film character
provides the closest foundation to the hand-colored print aesthetic.
The key adjustment is steering FL's warmth from amber toward rose
with WB Shift and careful saturation control.

| Parameter           | Adjustment | Why                                                                                |
| ------------------- | ---------- | ---------------------------------------------------------------------------------- |
| **Base Look**       | **FL**     | FL's film-like tonal rendering matches the hand-colored print aesthetic            |
| **Contrast**        | **−1**     | Gentle but not flat — studio portraits had dimensionality from controlled lighting |
| **Highlights**      | **−2**     | Smooth highlight roll-off; skin highlights glow rather than clip                   |
| **Shadows**         | **+1**     | Lifted shadows — hand-colored prints retained detail in shadow areas               |
| **Fade**            | **1**      | Slightly lifted blacks — the hand-coloring "floor" was never true black            |
| **Saturation**      | **−1**     | Restrained but not absent — colors feel intentional, not blasted                   |
| **Sharpness**       | **0**      | Minimum — the look is soft and smooth, never clinical                              |
| **Sharpness Range** | **1**      | Minimum — default                                                                  |
| **Clarity**         | **0**      | Minimum — skin should be porcelain-smooth; micro-contrast works against this look  |

**White Balance — the critical differentiator:**

The rose-amber warmth is what separates this look from generic "warm portrait" presets.
WB Shift is where you steer FL's amber warmth toward the distinctive pink-rose territory.

| WB Setting   | Value                             | Why                                                                            |
| ------------ | --------------------------------- | ------------------------------------------------------------------------------ |
| **WB Mode**  | Daylight or Custom K (4500-5200K) | Stable base; indoor studio conditions                                          |
| **WB Shift** | **A+2 / M+2**                     | The M+2 is the key move — pushes warmth from amber into rose-magenta territory |

> ⚠️ **The M+2 shift is essential.** Without it, you get a Leica-like amber portrait.
> With it, the warmth acquires the distinctive pink-rose quality of Chinese studio portraiture.
> If M+2 feels too strong on your subject's skin, try M+1 — but don't drop to M+0,
> or you lose the China Photo Studio character entirely.

**Pair with:** Viltrox 85mm f/2.0 Evo for classic bust portraits (the 85mm compression
matches studio portrait focal lengths), or SIRUI 35mm f/1.4 for environmental portraits.
Mount the 1/4 Black Mist filter for the soft, luminous skin quality
that defines this aesthetic — it physically approximates the hand-colored print softness.

**Post-Processing in Lightroom — China Photo Studio Refinement:**

For RAW files where you want to push deeper into the aesthetic:

1. **Tone Curve:** Lift the bottom-left point slightly (like Leica, but less aggressively).
   Gently pull down the top-right for controlled highlights.
   The curve should be smooth — no harsh S-curves.
2. **HSL — Hue:** Shift Orange toward Red by +5 to +10
   (pushes skin from orange-warm toward pink-warm — the defining move).
   Shift Yellow toward Orange by +5 (warms yellows to harmonize with rosy skin).
3. **HSL — Saturation:** Pull Orange (skin) by −5 to −10 (prevents skin from going too vivid).
   Pull Blue and Green by −15 to −20 (backgrounds should recede; only the subject's warmth matters).
   Keep Red at 0 or +5 (lips and red clothing should remain rich).
4. **HSL — Luminance:** Push Orange +10 to +15 (brightens skin for the luminous porcelain quality).
   Push Red +5 (keeps red clothing/lips from going too dark).
5. **Color Grading:** Add a rose-pink tone to midtones (~340° hue / pink-magenta, 8-12% saturation).
   Add a subtle warm tone to shadows (~30° hue / warm amber, 5-8% saturation).
   Highlights: very subtle warm pink (~350° hue, ~5% saturation).
6. **Calibration tab:** Shift Red Primary Hue to +10 (pushes reds toward orange-rose).
   Shift Blue Primary Hue to −10 (reduces blue-channel coldness).
   Shift Green Primary Saturation to −10 (suppresses greens for the studio portrait feel).

> 💡 **Save as a Lightroom preset** named "China Photo Studio Classic" (中国照相馆经典)
> and apply to portrait sessions where you want this distinctive aesthetic.
> It works especially well for: formal family portraits, couple photos,
> portraits against simple/dark backgrounds, and any image where you want
> that timeless Chinese studio portraiture quality.

> **Tip — When to use this vs Leica-style:**
> Use China Photo Studio style when the subject is the absolute focus
> and you want *flattering, rose-toned skin* above all else — family portraits,
> headshots, commemorative photos. Use Leica style when the *scene and mood*
> matter as much as the subject — street portraits, travel, environmental shots.
> The China Photo Studio look is portrait-first; Leica is scene-first.

(leica-hasselblad-comparison)=
### 5.4 Quick Comparison: Sony Default vs Leica-Style vs Hasselblad-Style vs China Photo Studio

| Aspect                 | Sony FL (Default) | Leica-Style              | Hasselblad-Style                   | China Photo Studio                      |
| ---------------------- | ----------------- | ------------------------ | ---------------------------------- | --------------------------------------- |
| **Overall Tone**       | Warm, filmic      | Warmer, nostalgic        | Neutral, refined                   | Warm rose-amber, porcelain              |
| **Saturation**         | Moderate          | Restrained (−2 to −3)    | Natural (−1 to −2)                 | Restrained (−1), rosy bias              |
| **Contrast**           | Moderate          | Gentle (−1 to −2)        | Very gentle (−2)                   | Gentle (−1), flattering                 |
| **Shadows**            | Slightly lifted   | Clearly lifted (Fade 2)  | Maintained (Fade 0)                | Slightly lifted (Fade 1)                |
| **Highlight Roll-Off** | Good              | Smooth (−2)              | Ultra-smooth (−2 to −3)            | Smooth (−2), luminous                   |
| **Skin Tones**         | Warm              | Warm-amber               | Accurate-neutral                   | Rose-peach, porcelain                   |
| **Green Rendering**    | Natural           | Olive/warm               | Cool/true                          | Muted/suppressed                        |
| **WB Shift Key**       | None              | A+1                      | None                               | A+2 / M+2                               |
| **Best For**           | General use       | Mood, emotion, portraits | Fidelity, landscapes, architecture | Formal portraits, family, commemorative |
| **Personality**        | "Easy-going"      | "Romantic"               | "Precise"                          | "Porcelain elegance" (端庄)             |

> **Final tip — Don't chase perfection.** These emulations capture the *character*
> of Leica, Hasselblad, and China Photo Studio color science, not an exact replica.
> The real value of those systems comes from their lenses, sensor design,
> and (in China Photo Studio's case) decades of hand-coloring craftsmanship,
> which can't be fully replicated in software. But for social media, prints,
> and personal memories, these tweaks produce a noticeably different,
> refined aesthetic that elevates your photos beyond Sony's defaults.
> Experiment, adjust to taste, and make them your own.

---

(6-summary-and-workflow)=
## **6. Summary: Your Color Grading Workflow**

```{mermaid}
flowchart TD
    A[Pick Your Scene] --> B{Which scenario?}
    B -->|Portrait| C[Mount Preset 1: Portrait Warm - FL]
    B -->|City Day| D[Mount Preset 2: City Vivid - IN]
    B -->|Landscape| E[Mount Preset 3: Landscape Bold - IN]
    B -->|Night City| F[Dial FL + Night City tweaks]
    B -->|Piano Video| G[Dial FL + Video tweaks + Lock WB]
    B -->|Museum| H[Dial FL + Museum tweaks + Lock WB]
    C --> I[Set White Balance per Section 4]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
    I --> J{Special shot worth editing?}
    J -->|No| K[JPEG is done — enjoy]
    J -->|Yes| L[Shoot RAW+JPEG]
    L --> M[Import RAW into Lightroom Classic]
    M --> N{Want Leica/Hasselblad/China Photo Studio look?}
    N -->|Leica| O[Apply Leica Classic preset]
    N -->|Hasselblad| P[Apply Hasselblad HNCS preset]
    N -->|China Photo Studio| P2[Apply China Photo Studio Classic preset]
    N -->|Standard| Q[Apply matching camera preset]
    O --> R[Fine-tune & Export]
    P --> R
    P2 --> R
    Q --> R
```

**The 80/20 Rule for Your Color Workflow:**

- **80% of photos:** In-camera Creative Look presets → JPEG → done. No PC needed.
- **15% of photos:** Minor Lightroom tweaks (WB correction, exposure, crop) → 5 minutes.
- **5% of photos:** Full Lightroom edit + optional Leica/Hasselblad/China Photo Studio treatment → 10-15 minutes.
- **<1% of photos:** Photoshop for object removal, compositing, or deep retouching.

This matches your efficiency-first philosophy: get it right in-camera,
and only sit at the PC for photos that truly deserve it.
