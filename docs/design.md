# design.md

Single source of truth for UI design in this project (Figma file *Design Work* and code). UI text, names and docs are in English (translation done 2026-11-06, glossary in `docs/glossary.md`). Devices and layout rules: `docs/devices.md`. Sources: `docs/references.md`.
Change a token here and in Figma together. Do not add colours, sizes or spacing that are not tokens without asking.

## 1. Principles
1. **Ten interaction principles (Nielsen).** Show system state, speak the user's language, give control (cancel always has an X),
   be consistent, prevent errors, recognise rather than recall, stay flexible, stay minimal, explain errors, help only when needed.
2. **Don't make me think (Krug).** Every screen is self-evident; users scan, so use hierarchy and short text. If it needs explaining it is not done.
3. **Consistency.** Same token, component and word everywhere; exceptions only with a clear reason. Reuse components, not one-off styles.
4. **Gestalt.** Proximity groups, similarity unites, common region (cards) contains, figure/ground gives contrast.
5. **Timeless UI.** Clarity over cleverness; about 70 % standard patterns; strong hierarchy; generous whitespace; tokens before flair.
6. **Process.** Grayscale structure first, strict component library, audit for muscle memory, resist fads (glass only on photos).

## 2. Colour tokens (Figma: Primitives, Club Coach, Theme)
- Layers: `Primitives` (raw values by palette: `brand/<club>/<light|dark>/primary|secondary|tertiary|on-primary|fill`, `neutral/`, `status/`, `effect/`, `metal/`) -> `Club Coach` roles (modes **Light / Dark / Grey**) -> `Theme` (modes **Pitch, Blue, Yellow**; groups `primary/`, `secondary/`, `tertiary/`, `metal/`, `nav/`). Palette names: Primary = club colour, Secondary = deep shade, Tertiary = accent.
- Surfaces: `bg/base` page, `bg/raised` cards, `bg/sunken` panels, `bg/overlay` selectors on photos (92 %), `border/default`.
- Text: `text/primary`, `text/secondary`, `text/muted` (only on raised), `text/on-fill`, `text/on-accent`, `text/accent` (club colour, see below).
- Action: `action/primary` + `action/on-primary`; `fill/club` (club colour fill), `accent`, `brand/deep`, `status/success|danger`.
- `action/primary` is never used as text on dark surfaces (3.1-3.2:1). Links and active nav use `text/accent`:
  light = strong club colour (Yellow: dark gold `#7A5A12`, yellow on white is 1.6:1), dark = `fill/club` (7.9:1 or more).
- Club themes: Pitch = KTP (green, gold metal), Blue = HJK (blue, silver metal), Yellow = KuPS (yellow, gold metal).
- Metal: paint styles `metal-club` (edges, hero frame) and `metal-nav` (active nav line: green metal / silver / gold) bound to Theme variables.
- Depth: `shadow/color` (UI, subtle), `shadow/depth` (hero only), `glass/*`, `glow/color`, `icon/detail` (decorative only), `chrome/home-indicator`.
- Contrast: text 4.5:1, icons and graphics 3:1; colour never carries meaning alone. All six club x mode combinations checked.

## 3. Type, space, shape, depth
- Font **Raleway**. Text styles in three folders. `Club Coach/Heading/`: H1 28/34 Bold, H2 22/28 Bold, H3 18/24, Display (large numerals). `Club Coach/Body/`: Text 16/22 SemiBold, Text-strong Bold,
  Small-text 14/20 Medium, Small-text-strong SemiBold, Caption 12/16 Medium. `Club Coach/Component/`: Button 14/20 Bold, Badge 12/16 Bold, Nav 11/14 SemiBold (Nav-active Bold). Titles max 2 lines, other text 1 line with ellipsis.
- Spacing (`Club Coach · Shape`): none 0, 2xs 2, xs 4, sm 8, md 12, lg 16, xl 20, 2xl 24, 3xl 32. Screen margin lg, card gap md, card padding lg, no gap under md.
- Radius: none 0, xs 4, sm 6, md 8, **lg 16** (cards, rows, tiles), **xl 24** (selectors, sheet, nav), full (avatars, dots).
- Effects: `shadow-sm`, `shadow-md` (low opacity, no strong shadows), `glow`, `button-glow`, `glass`, `glass-flat`, `blur-bar`, `metal-glow`.
- Icons: Heroicons v2 outline (MIT), 24 px (20 in buttons), stroke follows the text role. iOS home indicator 134x5 in a 34 px safe area.
- Touch targets at least 44 px. Cards and rows 370 px wide on a 402 px screen.

## 4. Components and layout
- Mid-fi wireframes use Club Coach mode **Grey (mid-fi)** (grey roles `mid/*`) on the same components; sections `05 Mid-fidelity (old structure, to archive)` and `06 Mid-fidelity · Parent (new structure)` on the `★★ Mid fidelity` page.
- Event detail has tabs Details / Participants / Conversation (description with links, attachments, Google Maps link, participants as "Last name First name" with photo, event message thread). Invoices (Invoice card) show amount, subject, due date and status badge (icon + text, never colour only); the detail screen has a "Message the biller" action.
- Tabs (Tab, 16 px, 4 px marker, no side padding: first tab and its underline start at the 16 px margin like the text below, 24 px between tabs) are larger than filter pills (Filter chip, 36 px high, 14 px text); every tab has a one-line description below it. Buttons carry a descriptive icon (e.g. credit-card for pay, chat for message). Addresses are shown large (16 px bold) with a Copy button and a Google Maps link. Quick tile for sign-ups is named "Sign-ups".
- Product is two apps on one design system: **Club Coach** (parents) and **Club Coach for Coaches** (coaches); structure in `docs/information-architecture.md`.
  Parent bottom nav has five items (Today, Calendar, Conversations, Invoices, Me; component `Bottom bar · Parent`, items fill the width, about 77 px, Invoices shows the unpaid count); the coach app has a purple accent and app icon, the parent app blue.
  Announcements are read-only (no replies). Invoices are paid through links to the bank and MobilePay, no in-app payment.
- Every mid-fi screen has a rationale block above it (Hypothesis: problem / friction, Solution, Principle); problem statements are design hypotheses, not research findings.
- Event detail follows the owner's layout: summary card (date, type, title, team, RSVP) on top, tabs, info rows (time, address with Copy action, participants), description, attachment, large map block that opens Google Maps. RSVP: the chosen option is filled (`action/primary`, shadow, bold label), the others are muted.
- Kit (Figma page *UI Kit*): Participant row, Message bubble, Message field, Attachment row, Link row, Invoice card, Search field, Tab, Filter chip, RSVP choice, Event card, Button, Card, List row, Status badge, Type dot, Counter, Day cell, Nav item, Bottom bar, Selector, Event row, Reminder row, Background / Club.
- Surfaces are solid (`bg/raised`, thin border, `shadow-sm`). Glass only over the hero photo (selectors with `glass-edge`, 2 px rim).
- **Home layout B (chosen):** compact hero 250 px (club background + player photo), rounded `bg/base` sheet with child and club selectors,
  next-event card and 2x2 quick tiles; week strip with the selected day's events is the scrolled second screen. Fixed bottom nav.
- Old four-item bottom nav (kept for archived screens): four equal 92 px items (Home, Events, Inbox, My details; no shop in this phase), one-line labels. Active = icon and label in `text/accent` + metal line above. Inactive = `text/secondary`.
- Hero backgrounds are club specific (KTP stripes and shapes, KuPS diagonals and circles, HJK rings), hero area only, never behind body text.
  Layers: `brand/deep`, shapes, brushed-metal lines (SOFT_LIGHT 40 %), metal rings and double frame, `shadow/depth`, edge vignette, photo.
- Player photos: cut out without outline, feathered edge, one drop shadow, same image in both modes. Shape opacity via node opacity.

## 5. Content rules
- English UI (dates `Thu 12 Nov, 17:30`, money `EUR 120.00`, 24 h clock; fictional "today" is Thu 12 Nov 2026). Child shown by first name only. Team names are realistic fictional Finnish names (Töölö 2017 Siniset, Kotka 2017 Vihreät) and stay as proper names. A place always has the pin icon.
- Examples use long text to expose truncation. No real people, crests or photos are final: placeholders until rights are confirmed.

## 6. Working rules
- Every screen answers: Where am I? What can I do? Where can I go from here? Tab bar = top-level destinations only, never actions.
- Always check light and dark mode, and all three clubs, before reporting a change. Explain why a design choice was made and ask before deviating.
- Figma pages: `🌟 Plan` (design system architecture, process meter), `★ Low fidelity`, `★★ Mid fidelity`, `★★★ High fidelity`, `▢ UI Kit` (`00 Palette`, `01 Tokens`, `02 Components`, `03 Icons and phone`, `04 Backgrounds (clubs)`, `99 Archive`), `✎ Brainstorming & archive` (old drafts, kept in Finnish). Progress and decisions: `docs/project-log.md`.
- Open: pressed/disabled states, motion tokens, HJK crest file, photo and crest rights, other views (events, messages, shop, profile), radius swatches lg 16 and xl 24 missing in the UI Kit radius frame, Button variants clipped at the right edge in the component doc.
