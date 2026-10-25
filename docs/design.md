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

### Note on glass and texture (to confirm)

The current home screen uses glass surfaces over a textured background. Principle 2.4 says
trends must serve utility. Proposed rule so the glass stays restrained:

- Glass is only used on top of the textured background (cards, selectors, nav bar), never on
  plain surfaces. Text on glass must still pass contrast (see section 3.1).
- Shadows are subtle (max 16 px blur, low opacity). Corners are at most 8 px.
- Core information (next event, who and which club) must be readable without the texture.

## 3. Decisions so far (draft, for review)

### 3.1 Colour

- Two token layers in Figma: collection **Primitives** (raw values in folders `light/` and
  `dark/`) and collection **Myclub** (semantic roles with modes *Vaalea* and *Tumma* that alias
  the primitives). Components use only roles. No raw hex anywhere.
- Palette direction: **Pitch Frost** (green + amber on cool icy neutrals, no beige).
- Roles: `bg/base`, `bg/raised`, `bg/sunken`, `border/default`, `text/primary`,
  `text/secondary`, `text/muted`, `text/on-fill`, `text/on-accent`, `action/primary`,
  `action/on-primary`, `fill/green`, `accent`, `brand/deep`, `status/success`,
  `status/danger`, `glass/*`, `shadow/color`, `glow/color`, `icon/detail`, `avatar/*`,
  `chrome/home-indicator`.
- Contrast: text 4.5:1, large text and icons 3:1. Colour never carries meaning alone (a dot for
  Treeni/Peli always has its label). `text/muted` only on `bg/raised`. `fill/green` and `accent`
  carry dark text (`text/on-accent`).
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
- Radius: none 0, xs 4, sm 6, **md 8 (max)**, full (only avatars, dots, counters).
- Effects: `glass`, `glass-flat`, `shadow-sm`, `shadow-md`, `glow`, `button-glow`,
  `blur-bar`; all colours and sizes come from variables.

### 3.4 Icons and phone chrome

- Icons: **Heroicons v2, outline, 24 px** (20 px inside buttons), stroke bound to a colour
  role. Library licence: MIT.
- Phone chrome: iOS status bar and **home indicator** (134 × 5 px in a 34 px safe area, with
  background blur). The bottom bar sits above the safe area.

### 3.5 Texture and motion

- Backgrounds: colour glow + soft ribbon + fine grain (grayscale PNG blended over a
  gradient). Generator and recipe: `design/textures/`.
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
- Real people, club crests and photos are placeholders until rights are confirmed.

## 4. Open questions

1. Pressed and disabled button states: which colours?
2. Motion tokens: durations, easings, reduced-motion behaviour.
3. Should the "70 % familiar" rule be checked against iOS and Android navigation conventions
   (bottom tabs, back gesture) per screen?
4. Is the glass treatment kept on every card, or only on the home screen?
