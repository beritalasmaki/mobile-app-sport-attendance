# Club Coach design system: README

What each part of the design system is, why it is named the way it is, and when it may be changed.
`docs/design.md` is the short rulebook (principles and token values, max 100 lines). This README explains the system behind it.
The Figma file is *Design Work*: page `UI Kit · luonnos` (tokens and components), section `08 · Design system -arkkitehtuuri` on page `CLUB COACH` (the diagram).

## 1. The idea in one paragraph
Everything on a screen is built from **tokens** (named values), never from raw hex colours or loose sizes.
Tokens sit in layers. A layer only refers to the layer below it (alias), so a change at the bottom shows up everywhere above it, and a change at the top never touches the bottom.
That is what makes three club themes, light and dark mode and a grey wireframe mode possible with the same components.

```
6 Sovellukset      Club Coach (parents, blue icon) · Club Coach Valmentaja (coaches, purple icon)
5 Ruudut           mid-fi and hi-fi screens
4 Komponentit      Painike, Kortti, Listarivi, Alapalkki ...
3 Roolit + Tyylit  Club Coach roles (bg, text, action ...) · text styles · effect styles · Muoto
2 Teema            club choice: Pitch (KTP), Sininen (HJK), Keltainen (KuPS)
1 Primitives       raw values
```

## 2. Variable collections (Figma)
| Collection | Modes | What it holds |
|---|---|---|
| **Primitives** | Arvo (one) | Raw colour values, grouped by palette. Not used directly on screens. |
| **Teema** | Pitch, Sininen, Keltainen | The club's colours as `primary`, `secondary`, `tertiary`, `metal`, `nav`. Choosing a mode re-themes a whole screen. |
| **Club Coach** | Vaalea, Tumma, Harmaa (mid-fi) | The **roles**: what a colour is *for* (`bg/base`, `text/primary`, `action/primary` ...). Components bind only to these. |
| **Club Coach · Muoto** | Mode 1 | Spacing, radius and effect sizes (numbers). |

How the layers connect: a role in `Club Coach` points either to `Teema` (when the colour belongs to the club) or straight to `Primitives` (neutral greys, status colours, glass).
`Teema` points to `Primitives`. So *club mode* × *Vaalea/Tumma* = 3 × 2 = 6 looks; Harmaa is the grey mid-fi look.

## 3. Primitives: palette folders
```
brand/<pitch|sininen|keltainen>/<light|dark>/primary | secondary | tertiary | on-primary | fill
neutral/<light|dark|mid>/bg, text, border, icon, chrome, avatar
status/<light|dark|mid>/success | danger
effect/<light|dark|mid>/glass, shadow, glow
metal/gold|silver|green/1-5          (grey-mode variants: metal/mid/...)
```
- **primary, secondary, tertiary** is the usual palette naming (Material Design): *primary* is the main brand colour, *secondary* a supporting shade (here the deep, dark shade), *tertiary* the accent. "Supportive" is not a standard term.
- `fill` is a lighter club colour used for fills and dark-mode accents. `tint` in Teema is the same idea.
- `light`, `dark`, `mid` = the value used in Vaalea, Tumma and Harmaa.
- `metal/…/1-5` are the five gradient stops of a gold, silver or green metal finish (dark edge, mid, highlight, mid, dark edge).

## 4. Teema: the club layer
Groups: `primary/` (`base`, `on`, `tint`, `text`), `secondary/` (`base`), `tertiary/` (`base`), `metal/` (1–5), `nav/` (1–5, the active-link line).
- A club has no light or dark mode of its own, so the dark value sits beside the light one with a `-dark` suffix (`base`, `base-dark`). The Club Coach roles pick the right one per mode.
- `primary/text` is the club colour darkened enough to read as text on a light surface (yellow on white is only 1.6:1, so Keltainen uses a dark gold).

## 5. Roles (Club Coach collection) and why they are named this way
**Naming pattern: `<purpose>/<variant>`.**
- **`on-X`** means "the content (text or icon) that sits on top of X". `action/primary` is a button background and `action/on-primary` is its label. Pairing them guarantees the contrast, whatever colours X takes in a theme. Never put another colour on X without checking.
- **Surfaces by depth:** `bg/base` (page), `bg/raised` (cards, above the page), `bg/sunken` (panels set into the page), `bg/overlay` (translucent selectors on photos).
- **Text by emphasis:** `text/primary` (main), `text/secondary` (supporting), `text/muted` (hints, only on `bg/raised`), `text/accent` (links and active navigation).
- **Fixed pairs:** `text/on-fill` (text on strong club or dark fills and photo heroes), `text/on-accent` (text on `accent`).

| Role | Use |
|---|---|
| `bg/base · raised · sunken · overlay` | Surfaces |
| `text/primary · secondary · muted · accent · on-fill · on-accent` | Text and icons |
| `action/primary`, `action/on-primary` | Primary buttons and selected states. **Never used as text on dark surfaces** (3.1–3.2:1). |
| `fill/club` | Club colour fill (named *club* because it is not always green) |
| `accent`, `brand/deep` | Club accent, club deep shade |
| `status/success · danger` | State. Always with an icon or text, never colour alone |
| `border/default` | Thin outlines and dividers |
| `glass/*`, `shadow/color`, `shadow/depth`, `glow/color` | Effects. Glass only over the hero photo; `shadow/depth` for the hero only |
| `icon/detail`, `avatar/from·to`, `chrome/home-indicator` | Decorative details, avatar gradient, iOS home indicator |
| `metal/gold-1..5`, `metal/silver-1..5` | Metal finishes (also as paint styles) |

When a colour may or may not be used, with computed contrast for every pair: `colour-usage.md`.

## 6. Styles
- **Text styles**, font Raleway, folder `Club Coach/`:
  `Heading/` Display, H1, H2, H3 · `Body/` Text, Text-strong, Small-text, Small-text-strong, Caption · `Component/` Button, Badge, Nav, Nav-active.
  Folder = where the text lives: headings, running text, or text inside a component (button, tab, navigation, badge). Dropdown and input text use Body.
  Suffix `-strong` = same size, heavier weight.
- **Paint styles**: `metal-gold`, `metal-silver`, `metal-club`, `metal-nav`, `glass-edge` (gradients that variables cannot express).
- **Effect styles**: `shadow-sm`, `shadow-md`, `glass`, `glass-flat`, `glow`, `button-glow`, `blur-bar`, `metal-glow`.
- **Muoto** (shape): spacing `none 0, 2xs 2, xs 4, sm 8, md 12, lg 16, xl 20, 2xl 24, 3xl 32`; radius `none 0, xs 4, sm 6, md 8, lg 16, xl 24, full`. T-shirt sizes grow left to right; `lg` radius is for cards, `xl` for selectors, sheets and navigation.

## 7. Components
Finnish names (the UI is Finnish): Painike, Kortti, Listarivi, Tilamerkki, Tyyppipiste, Laskuri, Päiväsolu, Navi-valinta, Alapalkki, Alapalkki · Vanhempi, Valitsin, Tapahtumarivi, Hakukenttä, Välilehti, Suodatinchip, Ilmoittautumisvalinta, Tapahtumakortti, Osallistujarivi, Viestikupla, Viestikenttä, Liiterivi, Linkkirivi, Laskukortti, Osoitekortti, Ilmoitusrivi, Tausta / Seura.
- Variants carry state (`Tila=Valittu`) and type; content (text, icon) is a component property.
- Icons: `Ikoni / <heroicons name>` (Heroicons v2 outline, 24 px).

## 8. When may things be changed?
Ask the owner before any change marked **ask**. Record every change with a reason in `docs/project-log.md` and update `docs/design.md`.

| Layer | May change when | Not allowed | Required checks |
|---|---|---|---|
| **Primitives (raw values)** | **ask.** (a) A contrast check fails, (b) the club's official colour changes, (c) a new club or palette is added | Tuning a colour for one screen or one component | Recompute contrast for every text/surface pair in all six club × mode combinations; check screens in light and dark |
| **Teema** | A club is added (new mode with every variable filled), or a club value changes (as for Primitives) | Changing what a group means (e.g. `tertiary` stops being the accent) | Same as Primitives; the active-nav and metal pairing per club |
| **Roles** | A **new purpose** appears that no role covers; or a role is re-pointed to fix contrast (**ask**) | A new role just for a new colour; a role with values in fewer than three modes | Values in Vaalea, Tumma and Harmaa; contrast of its `on-` pair |
| **Text styles** | A size or weight change that applies everywhere; a new style only when used in at least two places | A one-off size on a single text | Look for truncation (titles max 2 lines, other text 1 line) |
| **Muoto** | Rarely. Adding a step is fine; changing a value moves every screen (**ask**) | Raw numbers for gaps, padding or radius | Screenshot all screens |
| **Components** | Edit the main component; instances only override content | Detaching instances; local colour or size overrides | Check usages, both modes, all three clubs |
| **Screens** | Content, layout and structure | Raw hex, unbound spacing or radius, unnamed frames | Run the audit (no raw colour, no unbound value) |

Rules that always hold:
1. **Renaming is safe, deleting is not.** Names change without breaking bindings; deleting a variable breaks everything bound to it. Retire a token by moving it to a `_deprecated` folder first, delete only when nothing uses it.
2. **Check light and dark and all three clubs** before reporting a change as done.
3. **Do not alter frames the owner has edited by hand.** Read the frame first.
4. **Explain the reason** for a design choice and ask before deviating from the tokens.

## 9. How to add things
- **A new club:** add a mode to `Teema`, fill every variable, add its `brand/<club>` primitives (light and dark), compute contrast for all pairs, add a hero background variant.
- **The coach app accent (purple):** planned as a new tertiary or primary value set in `Teema` (or a mode), only after its contrast is checked in both modes.
- **A new role:** only if no existing role fits the purpose. Name `<purpose>/<variant>`, give it Vaalea, Tumma and Harmaa values, bind from components.
- **A new component:** build from tokens only, auto-layout, 44 px touch target, variants for states, document it in the UI Kit page.

## 10. Known gaps
Pressed, disabled and focus states; motion tokens; the purple coach accent; the grey mode still shows a few club-colour leftovers (nav marker, legend dots); club crests and photos are placeholders pending rights; tokens are not yet exported to code (they map 1:1 to CSS variables and a Tailwind theme when implementation starts, see `docs/technology.md`).
