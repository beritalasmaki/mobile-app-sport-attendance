# design.md — outline and review checklist

Purpose: the rulebook every screen and component follows (Figma and code). You write `design.md`;
Claude reviews it against the checklist at the bottom, then builds the UI kit from it.
Rule of thumb: if a rule cannot be checked (a number, a token name, a yes/no), it is not finished.

Proposed palette boards (pick one direction, or mix): Figma file *Design Work*, page **"UI Kit · luonnos"**
(A · Pace, B · Pitch, C · Violetti korjattu). Each shows Light + Dark, role mapping, computed contrast.

## 1. Principles and tone
- Link `docs/design-principles.md` (Nielsen 10, Krug, consistency, Gestalt).
- The feeling in 3 words (e.g. "in motion, warm, clear"). What it must never feel like.
- UI language: Finnish. Voice, forbidden jargon, date/time/number formats.

## 2. Colour
- Primitives: raw ramps (hex), named by hue + step (e.g. `indigo-900`).
- **Semantic roles** (the only names components may use), each with a **Light and a Dark** value:
  `bg/base`, `bg/raised`, `bg/sunken`, `text/primary|secondary|muted`, `text/on-action`,
  `action/primary` (+ pressed, disabled), `action/secondary`, `accent`, `brand/deep`, `status/success|warning|danger|info`,
  `border/default`, `focus/ring`, gradient stops.
- Rule for each role: where it may be used, where it may not.

## 3. Allowed pairings (matrix)
| Foreground | Background | Min contrast | Allowed? |
Rows for every text/icon colour on every surface; mark forbidden combos (e.g. "accent never as text").
Text ≥ 4.5:1, large text and icons ≥ 3:1. Colour never carries meaning alone.

## 4. Typography (Raleway)
Scale with size / weight / line height / letter spacing; numerals; max line length; truncation rules.

## 5. Space, shape, depth
4 pt spacing scale; radius scale; elevation levels; glass/blur rules; minimum touch target 44 × 44 px.

## 6. Texture and movement (not flat)
- Background recipes (e.g. gradient flow, speed lines, track-lane curves, grain) with exact layers and opacities.
- Where texture is allowed (page background, hero) and where not (behind body text, inside inputs).
- Max intensity so text contrast is still met on top of it.
- Figma note: the file accepts the `TEXTURE` effect, not `NOISE`; grain may need an image asset.

## 7. Motion tokens
Durations, easings, press / enter / exit / shared-element, drifting-gradient speed, `prefers-reduced-motion` behaviour.

## 8. Imagery framing
Allowed aspect ratios, corner radius, face-safe crop zone, overlay gradient for text over photos,
placeholder rules (no real people or real club marks in kit assets).

## 9. Components
Core set: Button, Card, List row, Tile, Badge, Chip/status dot, Club switcher, Nav item + Nav bar,
Photo frame, Event card. For each: variants, states (default, pressed, disabled, focus, loading, error), naming.

## 10. Accessibility baseline
Contrast, focus ring, dynamic type, touch targets, reduced motion, screen-reader labels for icon-only controls.

---

## Claude's review checklist (applied to your design.md)
- [ ] Every semantic role has a Light **and** a Dark value
- [ ] Every pair in the matrix has a computed ratio and passes (4.5 / 3)
- [ ] No colour is used without a role; no role without a use
- [ ] Texture and motion are limited to named surfaces and never lower text contrast
- [ ] Photo framing is concrete enough to implement (ratio, radius, crop zone)
- [ ] Touch targets, focus and disabled states defined
- [ ] One name per thing; no contradictions with `docs/design-principles.md`
- [ ] Anything unclear is listed as a question, not guessed
