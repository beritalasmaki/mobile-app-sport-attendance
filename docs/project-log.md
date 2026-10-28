# Project log: CLUB COACH, sports club app design

Portfolio case file. Chronological record of how the design evolved, why decisions were made, what went wrong and what is next.
Rules and tokens live in `docs/design.md`; this file keeps the story.

## 1. Brief
- **Product:** mobile app for sports-club families: attendance, events, membership, messages, shop. Finnish UI. A parent can have several
  children and several clubs, so switching person and club must be obvious.
- **Goal of this phase:** a token-based UI kit and a home screen in light and dark mode, themable per club, documented well enough to hand over.
- **Way of working:** designer (owner) directs, an AI assistant builds in Figma through the Figma MCP and keeps the repo documentation.
  Rule agreed early: planning decisions are confirmed, token deviations are asked first, every change is checked in light and dark.
- **Inputs:** owner's mid- and hi-fi frames, design principles (Nielsen, Krug, consistency, Gestalt), reference sports cards (Panini, Topps).

## 2. Timeline
1. **Reset.** Three first colour variations were rejected: clashing purple and cyan, flat fills, photo dropped in without framing rules.
   Decision: stop styling screens, build foundations (tokens, roles, components) first.
2. **Palette and texture.** Three palette boards (Pace, Pitch, Violet). Pitch chosen, beige rejected, cool "Frost" neutrals instead.
   A procedural motion-blur texture was tried, tuned twice and later dropped in favour of the card-style hero.
3. **Glass direction.** Home screen built with glassmorphism; accepted first, later judged niche and hard to read.
4. **Token system.** Colour: Primitives -> semantic roles with Light/Dark modes. Shape tokens (spacing, radius, blur, shadow, glow). Heroicons set.
   Every frame audited for raw colours and unbound spacing (target: zero).
5. **Components.** Eleven component sets with variants and properties: button, card, list row, badges, counter, day cell, nav item, bottom bar,
   selector, event row. Documentation frame per component.
6. **Sports-card direction.** Owner supplied card references. New concept: club picks two colours, big graphic shapes, gold/silver accents,
   glass only over photos. Implemented as a variable collection (`Seura`, later renamed `Teema`) (modes per club) that all roles alias, so one switch re-themes a screen.
7. **Real content.** Owner's cut-out player photo as hero, club crest and team names per theme (KTP, HJK, KuPS), long example texts for stress testing.
8. **Rework after feedback.** Nav label wrapped, glass looked bad in dark mode, bottom of home screen was cluttered. New rules: radius 8/16/24,
   solid surfaces, one row of quick actions, week strip with the selected day's events.
9. **Polish loop.** Contrast audit for 6 club x mode combinations; active nav colour per club; metal per club (gold warm, silver cool); photo
   cut-outs without outlines, feathered, drop shadow; club-specific hero backgrounds with depth.
10. **Layout exploration.** Three layouts (A week first, B sheet, C week on top) for one club, B chosen and rolled out to all clubs.
11. **Mid-fi rebuild.** Third Club Coach mode (grey) so wireframes reuse real components; new search, tab, chip, RSVP and event-card components; six grey screens (Tapahtumat list and detail, Ilmoittautumiset, Jäsenkortit, Viestit ja laskut, Aloitussivu) with status bar and bottom nav.
12. **Feedback round on event and invoices.** Owner asked for event tabs (info, participants, messages), description with links and attachments, Google Maps link, participant photos with full names, and a clearer invoice list with a billing message. Six new components and six grey screens added.
13. **Rationale blocks.** Each of the 11 mid-fi screens got a text card above it answering "which user friction does this solve and why is it designed this way", labelled as hypotheses for the case study.
14. **Owner redesign of event detail.** The owner edited the detail screen directly (summary card with RSVP first); I had overwritten it by rebuilding. Lesson: read the current frame state before editing and never rebuild a frame the owner has touched. Added copy action, map block and stronger selected RSVP.
15. **Scope change and rename.** No permission to redesign the original club app, so the owner builds an own product, **Club Coach**. Shop removed from navigation for now (four items). Variable collections, styles and the Figma page were renamed from the old name to Club Coach.
16. **Cleanup.** Pages restructured into sections, old drafts archived, component docs updated, repo docs reduced to one `design.md`.

17. **Information architecture.** The mid-fi screens copied the original app's structure, so a new IA was drafted (`docs/information-architecture.md`).
    The owner asked whether coaches and parents could have separate apps. Decision: design two apps, **Club Coach** and **Club Coach Valmentaja**, on one design system and account.
    Announcements are read-only; invoices are paid by links to the bank and MobilePay. Mid-fi is redrawn only after the owner approves the IA.

18. **Technology and portfolio scope.** The owner builds front-end and design; backend and security would be hired. Decision: portfolio version = Figma prototype plus an installable PWA with mock data (React, Vite, TypeScript, Tailwind, Vercel), two apps from one monorepo. Backend is specified as an interface (`docs/technology.md`). Owner answers to the IA: invoices get their own tab (five tabs for parents), the coach app gets a purple accent and icon, repo name stays.

19. **Parent app redraw started and process timeline.** Five-item bottom bar component, new Tänään (RSVP in the next-event card, reminder rows for invoice and sign-up deadline) and Kalenteri screens in Figma section `06`. A process timeline (five phases, items marked Valmis / Käynnissä / Tulossa with icon, fill or dashed outline, never colour alone) is in section `07 · Prosessi · timeline` for the case study; it is updated as phases progress.

20. **Token architecture.** Text styles grouped into Heading / Body / Component. Primitives regrouped by palette (brand primary / secondary / tertiary per club, neutral, status, effect, metal); `Seura` renamed `Teema` with groups primary, secondary, tertiary, metal, nav; role `fill/green` renamed `fill/club` (it is not always green). Names only changed, all bindings and values verified unchanged. Architecture diagram added in Figma section `08 · Design system -arkkitehtuuri`.

## 3. Key decisions and trade-offs
| Decision | Why | Cost |
|---|---|---|
| Tokens before screens | Colours chosen per screen produced random combinations | Slower start, much faster iteration later |
| Primitives -> roles -> club modes | One switch themes everything, light/dark independent | More variables to maintain |
| Solid surfaces, glass only on photos | Glass was unreadable and inaccessible in dark mode | Less "trendy" look, better legibility |
| Radius 8/16/24 instead of max 8 | Owner liked rounded forms, hierarchy by size | Rule changed mid-project, all components rebound |
| Metal by colour temperature | Cool club = silver, warm = gold reads coherent | Extra Teema variables |
| `text/accent` role | No single colour passed contrast in both modes | Dark gold instead of yellow in light Keltainen theme |
| Club-specific hero backgrounds | Each club should feel different, like trading cards | More layers, opacity set on nodes |
| Two apps (parent, coach) instead of one with role switch | Different jobs and mental models (home vs work), smaller navigation per app, no wrong-audience messages, no role-per-team UI | Two store listings and releases, two notification streams for dual-role users (shared account, deep links, per-app settings); fallback: one app with Koti / Työ mode |
| Portfolio PWA with mock data, backend as interface | Shows the owner's real skills (front-end to production) without collecting children's data or claiming security work | Not a full-stack product; must be stated honestly in the case study |
| Invoices as own tab (5 tabs) | Payment is a frequent, time-critical task and needs a visible badge | Tab items narrower (80 px), a fifth tab is the practical iOS maximum |
| Purple accent for the coach app | Home and work apps are told apart at a glance on the home screen | New accent needs contrast checks in both modes |
| Announcements read-only | General notices; replies would turn them into mixed threads | Questions must go to event or invoice threads |
| Invoice payment by bank / MobilePay links | No payment integration or card handling needed in v1 | User leaves the app to pay; no automatic paid status until later |
| Layout B (sheet) | Keeps hero emotion and first-screen essentials; week on second screen | Week view needs scrolling |

## 4. Problems and what they taught
- **Opacity lost on variable-bound paints** in Figma: set node opacity, not paint opacity.
- **Instance overrides hid component fixes** (old translucent fills stayed): reset overrides and re-bind after component edits.
- **Shadow colour too faint for depth**: added a dedicated `shadow/depth` role instead of abusing the UI shadow.
- **Contrast surprises**: club blue and green fail as text on dark cards (3.1-3.2:1); fixed by a role, not by ad hoc colours.
- **Failing scripts roll back everything** in Figma; scripts were written to be idempotent and verified with screenshots in both modes.
- **Fonts must be loaded for every text style** before creating text in Figma scripts; a missing font rolled a whole script back. Text node heights can also be stale; fixed heights solved overlapping headings.
- **Process lesson:** announcing why a change was made and asking before deviating built trust; checking only dark mode once broke light mode.

## 5. Results
- 1 design file, 3 club themes x 2 modes, 6 full home screens + 6 scrolled week screens, 11 component sets + 1 background set.
- Token layers: colour roles with light/dark values, club variables, spacing 9, radius 7, effects 8, text styles 13, paint styles for metal.
- Contrast verified for all club x mode pairs; one rule per exception (`action/primary` never as text on dark).
- Documentation: `docs/design.md` (rulebook, under 100 lines) and this log. Figma pages organised into numbered sections with an archive.

## 6. Next
- More views: Tapahtumat, Omat tiedot, Jäsenkortit, Saavutukset, built from the same components.
- Pressed/disabled states, motion tokens, HJK crest file, rights for photos and crests, hand-off notes for developers.
- Code: not started; tokens map 1:1 to CSS variables (colour roles, spacing, radius, shadows) when implementation begins.
