# Club Coach: plan for the English, adaptive redesign

Status: **agreed 2026-11-06**; steps 0, 1 and 2 done; step 3 (lo-fi) starts with the screen list for approval. Scope: **Club Coach (parents) only**. The coach app is parked, see `docs/coach-app-parked.md`.

## Decisions
| Topic | Decision |
|---|---|
| Language | Everything in English: screen text, layer, component, variable, mode and page names, docs. Reason: the project is a portfolio use case. |
| Devices | iPhone, Android phone, foldable Android (unfolded and cover screen), Apple dual-screen "Duo" device. |
| Apple Duo | Specs received and read from Apple's Figma kit: inner 669 x 951 / 951 x 669, outer 466 x 678 / 678 x 466. Device matrix and layout rules in `docs/devices.md`; notes and sources in `docs/references.md`. |
| App scope | Parent app only (5 tabs and their sub-screens, about 14-16 screens). |
| Foldable coverage | 5-6 key screens get a foldable variant: Today, Calendar + event detail (list-detail panes), Conversations, Invoice. Other screens get notes (max width, reflow, nav rail). |
| Android foldable | Generic medium class (600-839 dp), not one model. |
| Frames | Compact 402, Pro Max 440, Android medium 707, Duo inner 669, Duo outer 466 (`docs/devices.md`). |
| Formats | Dates `Thu 12 Nov, 17:30` (fictional "today" = Thu 12 Nov 2026), money `EUR 120.00`, 24 h clock, fictional Finnish club and team names stay. Token modes: `Light/Dark/Grey`, `Theme`, `Pitch/Blue/Yellow`. |
| Existing mid-fi | Section 05 (old structure) goes to the archive after the lo-fi is approved. Section 06 and the rationale blocks are the starting point for mid-fi. |

## Device rules (full list in `docs/devices.md`)
- Design by window size class, width first: compact = 1 pane, medium = 1-2 panes, expanded = multiple panes. Do not lock to portrait.
- Constrain content and component width; never stretch inputs and buttons. Components change presentation (bottom sheet -> side sheet, bottom bar -> nav rail).
- Foldables: unfolded inner screen and the small cover screen are both targets. Avoid placing controls across the hinge.
- Apple: Duo guidance in `docs/references.md` and `docs/devices.md`; iPhone frame stays 402 x 874.

## Steps and gates
| # | Step | Result | Gate |
|---|---|---|---|
| 0 (done) | Decisions and docs | Device matrix, language rules, `design.md` and process meter updated | Owner approves the matrix |
| 1 (done) | English translation | Inventory of all text nodes, FI -> EN glossary, then text, names, tokens, pages, docs | Glossary approved before applying; no Finnish left |
| 2 (done) | UI kit audit | List of elements used per screen vs the kit; missing ones added (nav rail, pane container, hinge gap, ...), unused moved to archive | Audit list approved |
| 3 | Lo-fi | Grey box screens on `Low fidelity` page, structure and content visible, compact + key foldable screens | Screen list and key flows approved |
| 4 | Mid-fi | Built from lo-fi with kit components in the grey mode, rationale blocks kept | Key flows clickable as prototype |
| 5 | Hi-fi | 3 clubs x light/dark, foldable variants for key screens, contrast check | All combinations checked |

After every step: update `docs/project-log.md`. Never edit a frame the owner has touched without reading its current state first.

## Open questions
- Process meter on the Plan page still shows the old phases (translated literally); rewrite it to the phases in this plan.
- Archive page drafts stay in Finnish by decision; they are labelled with a note.
