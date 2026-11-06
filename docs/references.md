# Club Coach: references and notes

Owner's notes from the sources used in this project. What each means for the project is written in "Use here". Items that would change a rule in `docs/design.md` are proposals until the owner approves them.

## Sources
- Apple: Designing for iPhone Duo (published 2026-09-09), Designing for iOS, Apple Design Resources (Figma kit with Duo bezels and layout guides, file key `Ps3Fb1X547hJQU906rqkDh`).
- Android: layout basics and adapt layout (developer.android.com/design/ui/mobile/guides/layout-and-content).
- Samsung: One UI design guidelines (PDF supplied by the owner).
- Video notes (Chris Raroque): "My App Design Process", "How I Make Apps FEEL 10x Better". Apple WWDC25: "Design foundations from idea to interface".

## Foundations from idea to interface (WWDC25)
- Every screen answers: Where am I? What can I do? Where can I go from here? -> add to the review checklist in `design.md`.
- IA: write down everything the app does, then prune without mercy, rename unclear items, group what belongs together (done in `docs/information-architecture.md`).
- Tab bar = top-level destinations only, never actions ("Add" belongs inside a page). Toolbar = screen title plus the screen's main actions.
- Progressive disclosure: show the essential, offer detail on demand. Group by time, progress or theme. Lists for text, grids for visual content.
- Visual anchor by size and contrast. System text styles (Dynamic Type) and semantic colours instead of hard-coded values (our colour roles already work this way; text scaling is not yet covered).

## Design process (My App Design Process)
1. Mood board and inspiration before the first own sketch. 2. Several parallel prototypes in Figma (layout options, cards vs lists, grouping). 3. Best one in code with real data on a real device. 4. Keep iterating on the device.
Real data exposes UX problems that perfect mock text hides.
Use here: lo-fi shows two or three layout options for the Today screen before one is chosen; the PWA test uses realistic long names and uneven data.

## Search findings
- Card backgrounds for results added depth without function; grouping results by type broke relevance order; type icons added nothing (checkboxes made open tasks easier to scan); yellow highlight won for the search term.
Use here: review the type dot and card containers in the Calendar list during the UI kit audit (step 2); a plain ranked list for search results; highlight search terms with a highlighter-style tint (needs a token, ask first).

## Feel (5 design secrets)
Custom animations (split into small motions), mascots for empty states, considered haptics (light for repeated actions, heavier for bigger choices), one icon style (outline = inactive, filled = active), keep collecting inspiration.
Use here (proposals, to decide later): empty-state screens in lo-fi; motion tokens (open item in `design.md`); filled Heroicons variant for the active nav item (deviation from outline-only rule, ask first); haptics in the PWA where the platform allows.

## Foldables and Duo
See `docs/devices.md` for sizes and layout rules.
- Duo: do not draw a layout per pose; use compact width (outer) and regular width (inner). Split view expands on the inner display and collapses to one pane on the outer. Arrangement views (split or overlay) hold a primary and a secondary view; navigation stays outside them.
- Duo side controls: top of the side bar = Back/Close and primary action, bottom = tab bar. In a partial fold, interactive elements move away from the fold. Table pose: content above the fold, touch controls below; architecture identical.
- Android: window size class first (width, then height), panes: compact 1, medium 1-2, expanded multiple; max width on content; components change presentation.
