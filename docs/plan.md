# Club Coach: plan for the English, adaptive redesign

Status: **agreed 2026-11-06**, step 0 not yet started. Scope: **Club Coach (parents) only**. The coach app is parked, see `docs/coach-app-parked.md`.

## Decisions
| Topic | Decision |
|---|---|
| Language | Everything in English: screen text, layer, component, variable, mode and page names, docs. Reason: the project is a portfolio use case. |
| Devices | iPhone, Android phone, foldable Android (unfolded and cover screen), Apple dual-screen "Duo" device. |
| Apple Duo | The owner will paste the specs. Until then no sizes are invented; the device is a placeholder in the device matrix. |
| App scope | Parent app only (5 tabs and their sub-screens, about 14-16 screens). |
| Foldable coverage | 5-6 key screens get a foldable variant: Today, Calendar + event detail (list-detail panes), Conversations, Invoice. Other screens get notes (max width, reflow, nav rail). |
| Existing mid-fi | Section 05 (old structure) goes to the archive after the lo-fi is approved. Section 06 and the rationale blocks are the starting point for mid-fi. |

## Device rules (from the Android adaptive guide, to confirm in step 0)
- Design by window size class, width first: compact = 1 pane, medium = 1-2 panes, expanded = multiple panes. Do not lock to portrait.
- Constrain content and component width; never stretch inputs and buttons. Components change presentation (bottom sheet -> side sheet, bottom bar -> nav rail).
- Foldables: unfolded inner screen and the small cover screen are both targets. Avoid placing controls across the hinge.
- Apple: guidance from the pages in `docs/references.md` (to be added with the pasted Duo specs); iPhone frame stays 402 x 874.

## Steps and gates
| # | Step | Result | Gate |
|---|---|---|---|
| 0 | Decisions and docs | Device matrix, language rules, `design.md` and process meter updated | Owner approves the matrix |
| 1 | English translation | Inventory of all text nodes, FI -> EN glossary, then text, names, tokens, pages, docs | Glossary approved before applying; no Finnish left |
| 2 | UI kit audit | List of elements used per screen vs the kit; missing ones added (nav rail, pane container, hinge gap, ...), unused moved to archive | Audit list approved |
| 3 | Lo-fi | Grey box screens on `Low fidelity` page, structure and content visible, compact + key foldable screens | Screen list and key flows approved |
| 4 | Mid-fi | Built from lo-fi with kit components in the grey mode, rationale blocks kept | Key flows clickable as prototype |
| 5 | Hi-fi | 3 clubs x light/dark, foldable variants for key screens, contrast check | All combinations checked |

After every step: update `docs/project-log.md`. Never edit a frame the owner has touched without reading its current state first.

## Open questions
- Apple Duo specs (owner to paste).
- Date, time and currency format in English UI (e.g. `Thu 18 May, 17:30` and `EUR 120.00`, or keep Finnish club context with `18.5.`)?
- Names: keep Finnish club and team names (KTP, HJK, KuPS, Kotka 2017 Vihreät) as fictional examples?
- Rename token modes: `Vaalea/Tumma/Harmaa` -> `Light/Dark/Grey`, `Teema` -> `Theme`, `Pitch/Sininen/Keltainen` -> `Pitch/Blue/Yellow`. To confirm in the glossary (step 1).
