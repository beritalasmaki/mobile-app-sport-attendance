# Colour usage rules

When a colour may be used, when it should be used, and when it must not be. Status: **proposal for the owner's approval**. The contrast numbers are computed from the Figma variables (all six combinations: Pitch, Sininen, Keltainen × Vaalea, Tumma), not estimated.
Part of the design system, see `README.md`. Token values: `docs/design.md`.

## 1. Principles
1. **Colour carries meaning, not decoration.** If a colour does not tell the user something (state, importance, identity, where they are), use a neutral.
2. **Neutrals first.** Roughly 85 % of a screen is `bg/*`, `text/*` and `border/default`. Club colour about 10 %, accent about 5 %. These shares are a guideline to spot over-coloured screens, not a measured rule.
3. **One primary action per screen** uses `action/primary`. A second filled button on the same screen is a sign the screen has two jobs.
4. **Identity is not state.** Club colours (primary, secondary, tertiary, fill, metal) say *whose* app this is. Only `status/*` says *what state* something is in. Never swap them: a green club must not make "paid" and "unpaid" look alike.
5. **Colour never works alone.** Every colour-coded meaning also has an icon, a label, a shape or a position.
6. **Use roles, not palettes.** Components bind to `Club Coach` roles; never to Primitives or Teema directly, and never to a raw hex.

## 2. Which colour for which job (decision order)
1. Is it a **state** (success, error)? → `status/success`, `status/danger`, with icon and text.
2. Is it the **main action** or a selected state? → `action/primary` fill with `action/on-primary` label.
3. Is it a **link or the active navigation item**? → `text/accent` (icon and label together).
4. Is it **club identity** (hero, selector marker, club chips, tab underline of the club)? → `brand/deep`, `fill/club`, Teema `primary`, `secondary`.
5. Is it a **highlight** (deadline, new, today)? → `accent`, sparingly, as a fill or marker, never as text.
6. Is it a **finish** (edge, frame, active-nav line)? → metal, see section 5.
7. Otherwise → neutral (`bg/*`, `text/*`, `border/default`).

## 3. Role rules (use / do not use)
| Role | Use it for | Do not |
|---|---|---|
| `text/primary` | Titles, body, icons | |
| `text/secondary` | Supporting text, inactive nav | Titles |
| `text/muted` | Hints and captions **on `bg/raised` only** | On `bg/base` or photos; for anything needed to complete a task |
| `text/accent` | Links, active nav | Decoration; body text |
| `action/primary` | Primary button fill, selected state fill, graphics | **As text on dark surfaces** (3.1–3.2:1) |
| `action/on-primary` | Label and icon on `action/primary` | On any other fill |
| `fill/club` | Club-colour fill, chips, markers, dark-mode accent | As text; in light mode as the only carrier of meaning (1.6–2.9:1 on white) |
| `accent` | Small highlights: deadline marker, today, badge | As text or thin icon in light mode (Pitch 1.9:1); as a large area |
| `brand/deep` | Hero base, deep fills, light-mode text/graphics | In dark mode as a graphic on `bg/raised` (1.7–2.4:1) |
| `status/*` | State only | As decoration or club colour |
| `border/default` | Dividers, card outlines | As the **only** edge of an input (1.4–1.5:1, needs 3:1) |
| `bg/overlay`, `glass/*` | Selectors over the hero photo | Over plain surfaces |

## 4. Verified pairs (lowest value across the six combinations)
Text needs 4.5:1, graphics and large icons 3:1.
| Pair | Lowest | Verdict |
|---|---|---|
| `text/primary` on `bg/base` / `bg/raised` | 14.2 / 15.3 | OK |
| `text/secondary` on `bg/raised` | 8.7 | OK |
| `text/muted` on `bg/raised` | 5.75 | OK |
| `text/accent` on `bg/base` / `bg/raised` | 5.56 / 6.37 | OK |
| `action/on-primary` on `action/primary` | 4.71 | OK |
| `text/on-accent` on `accent` | 4.53 | OK (marginal in Sininen/Keltainen light) |
| `text/on-accent` on `fill/club` | 5.53 | OK, **the safe text role on `fill/club`** |
| `status/success` / `status/danger` on `bg/raised` | 5.13 / 6.54 | OK |
| `action/primary` on `bg/raised`, as graphic | 3.12 (dark) | OK for graphics, **not text** |
| `border/default` on `bg/raised` | 1.41 | Decoration only |
| `fill/club` on `bg/raised` | 1.64 (light) | Fails in light; OK in dark (7.9+) |
| `accent` on `bg/raised` | 1.85 (light, Pitch) | Fails in light; OK in dark (6.8+) |
| `brand/deep` on `bg/raised` | 1.67 (dark) | OK in light (12.2+); fails in dark |
| `text/on-fill` on `brand/deep` | 2.01 (dark) | **Fails in dark** (12.2+ in light) |
| `text/on-fill` on `fill/club` | 1.64 (light) | **Fails in light** (9.5+ in dark) |

Not computed: `glass/*` and `bg/overlay` (translucent, depend on the photo behind them). Check those on the actual hero, per club.

## 5. Metal, glass and effects
- **Metal** (gold for warm clubs, silver for cool ones, green for the green nav line): hero frame edges, the active-navigation line, and special cards (Jäsenkortit, achievements) when they are drawn. One metal element per component. Never on text, never as a body surface, never as a button fill.
- **Glass** (`glass/*`, `bg/overlay`): only over the hero photo. Never on plain surfaces; there it reads as grey and fails in dark mode.
- **Shadow**: `shadow/color` is subtle UI depth; `shadow/depth` is for the hero only.

## 6. Modes
- **Vaalea / Tumma:** do not assume a role keeps its brightness. `text/on-fill` is light in Vaalea and dark in Tumma, so it pairs with `brand/deep` in Vaalea and `fill/club` in Tumma. When in doubt use the fixed pairs: `action/on-primary` on `action/primary`, `text/on-accent` on `accent` or `fill/club`.
- **Harmaa (mid-fi):** grey only. Colour returns in hi-fi. Known leftovers: green nav marker, legend dots.
- **Clubs:** a screen shows exactly one club theme. Never mix two clubs' colours on one screen.

## 7. Before you use a colour
1. Which job is it (section 2)? If none, use a neutral.
2. Is there already a role for that job? Use it; do not add a colour.
3. Text on it? Use its `on-` pair or a pair from section 4.
4. Does the meaning survive without the colour (icon, label)?
5. Check it in Vaalea and Tumma and in all three clubs.

## 8. Findings to resolve (need the owner's decision, nothing has been changed)
1. **`text/on-fill` flips brightness between modes.** On plain `brand/deep` in Tumma it is 2.0–2.9:1. Hero text sits on the photo and vignette, which must be checked separately; any text placed on plain `brand/deep` or `fill/club` should use a fixed pair. Option: re-point `text/on-fill` so it stays on-colour for `brand/deep` in both modes and add `text/on-fill-club` for `fill/club`.
2. **There is no warning or info status.** Overdue, deadline and "needs attention" currently have only `status/danger`. Option: add `status/warning` (with icon) rather than overloading `accent`.
3. **`border/default` is 1.4–1.5:1.** Fine for dividers, not enough to mark an input or a selected state on its own. Check Hakukenttä and Valitsin; add a stronger border role (e.g. `border/strong` at 3:1) if they rely on it.
4. **`accent` fails as a graphic on white in Pitch light (1.85:1).** Keep it to fills with `text/on-accent`, as in section 3.
