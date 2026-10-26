# design.md

Rulebook for every screen and component in this project (Figma and code).
Read together with `docs/design-principles.md` (Nielsen, Krug, consistency, Gestalt).
Sections 1 and 2 are the owner's principles. Section 3 records the decisions made so far in
Figma (file *Design Work*, page "UI Kit · luonnos") so they can be checked and corrected.

---

## 1. Core principles of timeless UI

- **Clarity over cleverness.** Prioritize clean communication and intuitive layouts so users
  never feel lost or forced to learn a new interface.
- **Build familiarity into novelty.** Keep about 70 % of the interface rooted in standard,
  predictable patterns (where menus and buttons live) and use novelty sparingly.
- **Strong visual hierarchy.** Use typography, scale and whitespace deliberately to guide the
  eye to what matters most.
- **Generous whitespace.** Give elements room to breathe instead of cramming the screen with
  decorative noise or heavy borders.
- **A design system built on details.** Lock down the core tokens (spacing, grid, typography
  scale, neutral colour foundations) before adding stylistic flair.

Sources noted by the owner: wujata.me ("5 timeless design principles"), Medium
(technology-core "3 laws of timeless UI/UX"), Erik D. Kennedy ("7 rules for creating gorgeous
UI"), UX Planet ("importance of creating timeless design systems").

## 2. Design process

1. **Start in grayscale.** Lay out structure and information architecture in black and white
   first to test contrast and hierarchy without colour.
2. **Establish a strict component library.** Reusable, predictable primitives (inputs, buttons,
   cards) so the product stays cohesive as it scales.
3. **Audit for muscle memory.** Test flows against standard conventions so a new user can
   navigate without a tutorial.
4. **Resist fad-chasing.** Avoid heavy reliance on hyper-specific micro-trends (excessive
   glassmorphism, noisy neo-brutalism) unless they directly serve the core utility of the app.

### Direction: sports-card style, glass only on selected layers (decided)

Pure glassmorphism is a niche, Apple-like style. Sport brands use other languages, so the
reference is trading cards (Panini football cards, Topps gold frames, MVP hockey cards):

- **Club theme.** Each club picks two colours. Everything else (deep, tints, on-colour text)
  is derived and contrast-checked. In Figma this is the `Seura` variable collection (modes per
  club) that the semantic roles alias, so the whole screen re-themes by switching one mode.
- **Hero background.** Large graphic shapes in the club colours, an oversized number or letter at
  16 % opacity, a dot pattern and a star (component `Tausta / Hero`). Only behind the hero area,
  never behind body text.
- **Metallic accents.** Gold and silver gradients for frame lines, achievements and membership
  cards, the primary button and the selected nav item. Decoration only, never a text colour.
- **Surfaces.** Cards, list rows, day strip, quick actions and the bottom bar are **solid** (`bg/raised`).
  Glass is allowed only over the hero photo (selectors, role `bg/overlay`, fill at least 90 %).
- Shadows stay subtle (max 16 px blur, low opacity). Corners follow the 8 / 16 / 24 + full scale (section 3.3).
- Layout, navigation and component behaviour stay standard (the 70 % familiar rule).

## 3. Decisions so far (draft, for review)

### 3.1 Colour

- Two token layers in Figma: collection **Primitives** (raw values in folders `light/` and
  `dark/`) and collection **Myclub** (semantic roles with modes *Vaalea* and *Tumma* that alias
  the primitives). Components use only roles. No raw hex anywhere.
- Palette direction: **Pitch Frost** (green + amber on cool icy neutrals, no beige) is the default
  club theme ("Pitch"). Other clubs (e.g. Sininen, Keltainen) are modes of the `Seura` collection;
  contrast is computed per club and mode. Known adjustment: Sininen dark `action` is `#2F68DB`.
- Roles: `bg/base`, `bg/raised`, `bg/sunken`, `border/default`, `text/primary`,
  `text/secondary`, `text/muted`, `text/on-fill`, `text/on-accent`, `action/primary`,
  `action/on-primary`, `fill/green`, `accent`, `brand/deep`, `status/success`,
  `status/danger`, `glass/*`, `shadow/color`, `glow/color`, `icon/detail`, `avatar/*`,
  `chrome/home-indicator`.
- Contrast: text 4.5:1, large text and icons 3:1. Colour never carries meaning alone (a dot for
  Treeni/Peli always has its label). `text/muted` only on `bg/raised`. `fill/green` and `accent`
  carry dark text (`text/on-accent`).
- Checked per club and mode (6 combinations): all text pairs ≥ 4.5:1. `action/primary` as text on `bg/raised` fails in
  Pitch and Sininen dark (3.2 / 3.1), so it is used only for icons and fills, never for text. The active nav item
  uses `text/primary` for label and icon (same colour) plus the gold marker. `icon/detail` is decorative only.
- Open: pressed and disabled states need tokens (`action/pressed`, `action/disabled`).

### 3.2 Typography

- Font: **Raleway**. Text styles (folder `Myclub/`): H1 28/34 Bold, H2 22/28 Bold,
  H3 18/24 Bold, Text 16/22 SemiBold, Text-strong 16/22 Bold, Small-text 14/20 Medium,
  Small-text-strong 14/20 SemiBold, Button 14/20 Bold, Caption 12/16 Medium,
  Badge 12/16 Bold, Nav 11/14 SemiBold, Nav-active 11/14 Bold.
- No ad-hoc sizes. Long text is truncated: titles max 2 lines, everything else 1 line with an
  ellipsis. Example content in designs must always be long (real worst case).

### 3.3 Spacing, radius, depth

- Spacing tokens (collection *Myclub · Muoto*): none 0, 2xs 2, xs 4, sm 8, md 12, lg 16,
  xl 20, 2xl 24, 3xl 32. All padding and gaps use them.
- Layout rules: screen margin `lg` (16); cards and list rows are **370 px** wide
  (402 − 2 × 16) with padding `lg` on all sides; gap between cards `md` (12); gap inside a card
  `sm` (8). The bottom bar is 394 px wide (4 px margins).
- Radius: none 0, xs 4, sm 6, md 8, **lg 16 (cards, rows, tiles), xl 24 (selectors, bottom bar top corners)**, full (avatars, dots, counters).
- Metal follows the club's colour temperature: gold for warm themes (Pitch, Keltainen), silver for cool (Sininen). One
  paint style `Myclub/metal-club` bound to Seura variables `club/metal-1..5`; all metal edges and the nav marker use it.
- Nav item: active = label and icon in `text/accent` = the club colour (Pitch green, Sininen blue, Keltainen yellow). Light mode uses
  the strong club colour (Keltainen: dark gold `#7A5A12`, because yellow on white is 1.6:1); dark mode uses `fill/green` (club tint, ≥ 7.9:1) plus the metal line above, in the club's own metal (`Myclub/metal-nav`: green metal for Pitch, silver for Sininen, gold for Keltainen);
  inactive = label and icon both `text/secondary`.
- Metal edges are not used on cards or tiles (plain `border/default`); the metal frame belongs to the hero background (`Metallikehys`,
  two nested lines in `metal-club`, under the photo so the player breaks out of the frame).
- Player photos: cut out without outline, edges feathered, one drop shadow (`shadow-md`); same image in both modes.
- Hero backgrounds: component set `Tausta / Seura` (Seura=KTP: vertical stripes + large shapes; KuPS: diagonal bands + ball
  circles; HJK: concentric rings). Common layers: brushed-metal line texture (SOFT_LIGHT 40 %), `metal-club` ring lines, depth
  from `shadow/depth` (drop and inner shadows, edge vignette). Shapes use role fills with node opacity (paint opacity is lost on
  variable-bound paints). Hero area only, never behind body text.
- Metal and glass edges: hero selectors have a 2 px outside glass rim (`Myclub/glass-edge`); the metal edge sits on Primary and Secondary buttons,
  quick-action tiles and the active-nav marker. Space above the next-event card is `2xl` (24).
- Home layout B (chosen, all clubs, both modes): compact hero (250 px, photo above the sheet), a rounded `bg/base` sheet (radius xl)
  holding the child and club selectors, the next-event card and a 2x2 grid of quick-action tiles (60 px high). The week strip and the
  selected day's events are the scrolled second screen (`Tämä viikko`, "Näytä koko viikko"). Layouts A (week first) and C (week on
  top) were explored and are kept as archive frames. Gaps between blocks are
  at least `md` (12); the fixed bottom bar (98 px + 34 px home indicator) never covers content at rest.
- Bottom bar labels stay on one line (items hug their text; label lengths are part of the copy rules).
- Effects: `glass`, `glass-flat`, `shadow-sm`, `shadow-md`, `glow`, `button-glow`,
  `blur-bar`; all colours and sizes come from variables.

### 3.4 Icons and phone chrome

- Icons: **Heroicons v2, outline, 24 px** (20 px inside buttons), stroke bound to a colour
  role. Library licence: MIT.
- Phone chrome: iOS status bar and **home indicator** (134 × 5 px in a 34 px safe area, with
  background blur). The bottom bar sits above the safe area.

### 3.5 Texture and motion

- Hero backgrounds: see "Direction" above (`Tausta / Hero`). The older grain/ribbon texture
  recipe (`design/textures/`) remains available as an optional overlay.
- Metal tokens: paint styles `Myclub/metal-gold`, `metal-silver`, `metal-gold-line`, effect
  `metal-glow`, bound to `metal/*` roles.
- Movement is expressed through the texture. Motion tokens (durations, easings, reduced
  motion) are not defined yet.

### 3.6 Components (Figma, page "UI Kit · luonnos")

Painike (Primary/Secondary × icon none/left/right), Kortti (Pinta/Lasi), Listarivi,
Tilamerkki, Tyyppipiste, Laskuri, Päiväsolu, Navi-valinta, Alapalkki. In progress: Valitsin
(child, club) and Tapahtumarivi.
Rule: no new colours, sizes or spacing without asking; every deviation is proposed first.

### 3.7 Content rules

- UI language: Finnish. Child name is the first name only. Team names are real-style
  ("Töölö 2017 Siniset", "Töölö 2017 Keltavalkoiset"), never plain "P2016".
- A place always has the location icon. A selected child always has a visible name (no icon-only
  switching), also with five or six children.
- Real people, club crests and photos are placeholders until rights are confirmed. Themed examples use
  KTP (Pitch), HJK (Sininen) and KuPS (Keltainen) with their own team names and invented player names.

## 4. Open questions

1. Pressed and disabled button states: which colours?
2. Motion tokens: durations, easings, reduced-motion behaviour.
3. Should the "70 % familiar" rule be checked against iOS and Android navigation conventions
   (bottom tabs, back gesture) per screen?
4. Which exact club colours do real clubs choose, and who validates contrast when a club picks its own?
5. Metallic primary button and nav ring are not applied to the components yet.
