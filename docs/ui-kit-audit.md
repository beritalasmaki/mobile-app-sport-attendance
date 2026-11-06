# Club Coach: UI kit audit (draft for approval)

Status: **approved by the owner 2026-11-06, mostly built** (step 2 of `docs/plan.md`). See section 7 for what was built and what is open. Basis: read-only scan of the UI Kit page and all 14 mid-fi screens on 2026-11-06.

## 1. What the kit contains
28 component sets or components and 43 icons. Used by the 14 mid-fi screens (instances): Nav item 59, Tab 24, Counter 14, Day cell 14, Type dot 13, Bottom bar 11, RSVP choice 8, Card 8, Selector 6, Event card 6, Filter chip 6, Participant row 5, Button 5, Search field 4, Event row 4, Invoice card 4, Message bubble 3, Bottom bar · Parent 3, Background / Club 2, Reminder row 2, Attachment row 1, Message field 1.

| Component | Variants | Used | Verdict |
|---|---|---|---|
| Button, Card, List row, Counter, Type dot, Day cell, Nav item, Selector, Event row, Search field, Tab, Filter chip, RSVP choice, Event card, Participant row, Message bubble, Message field, Attachment row, Invoice card, Reminder row, Background / Club | | yes | **Keep** |
| Bottom bar · Parent (5 items) | 5 | 3 screens | **Keep**, main bar |
| Bottom bar (4 items) | 4 | 11 old screens | **Deprecate**: move to archive together with section 05 after lo-fi is approved (cannot be removed while the old screens use it) |
| Status badge | 4 | 0 instances (Invoice card draws its own copy) | **Keep**, rebuild Invoice card to nest it |
| Link row | 1 | 0 | **Keep**, needed in event description |
| Background / Hero, Player/No, Player/Yes | 3 | 0 | Already in `99 Archive` |
| Phone / Home indicator | 1 | 14 | **Keep**, add to device frames |
| Icons | 43 | | Keep; 7 not used by any screen yet (gift, shopping-bag, star, trophy, ticket, megaphone, receipt-percent), kept for Me and announcements |

## 2. Repeated but not componentised (drawn by hand on every screen)
| Element | Screens | Proposal |
|---|---|---|
| Status bar (9:41, signal, battery) | 14 | New component **Status bar** (iOS and Android variants) |
| Top bar (back, title, action) | 5 | New component **Top bar** |
| Screen header (title + one-line description) | 9 | New component **Screen header** |
| Tabs row with description line | 8 | New component **Tab bar** (Tab set + description) |
| Info row (icon + label + value, copy action) | 7 (time, address, participants) | New component **Info row** |
| Summary card (event date, type, title, team, RSVP) | 1 | Make a component **Summary card** (used by Event details, reusable for Invoice summary) |
| Date tile (weekday + date) | 3 | Keep inside Event card, expose as nested instance |
| Message area (thread container) | 1 | Layout, not a component |
| Invoice card status | 4 | Replace the hand-drawn badge with the Status badge instance |

## 3. Missing for the planned parent screens
Screens planned for lo-fi (about 19): Today, Today week, Calendar (Upcoming, Mine, Sign-ups), Event details, Participants, Event conversation, Sign-up detail, Conversations (Events, Announcements), Announcement, Invoices, Invoice, Message to biller, Me hub, Children and teams, Membership cards, Settings and notifications.

| New element | Needed by | Note |
|---|---|---|
| Avatar (photo, initials) | Selector, Participant row, Me | exists only as a token example |
| Section header | Invoices (Unpaid / Paid), Participants, Me | |
| Toggle row | Settings, notifications | |
| Bottom sheet | Child and club switch, RSVP change | becomes side sheet on medium and larger |
| Dialog | "Leaving the app to pay" confirm | |
| Toast | RSVP saved, copied | |
| Banner | unpaid invoice, deadline (today the Reminder row) | decide if Reminder row covers it |
| Empty state | every list | illustration slot; mascot is an open idea from the references |
| Nav rail | medium, expanded, Duo | replaces Bottom bar |
| Pane layout (list + detail) | Calendar, Conversations, Invoices | container with max width |
| Duo side bar (vertical controls) | Duo outer and inner landscape | tab bar and toolbar on the trailing edge |
| Reserved region overlays | Duo frames | camera and fold area; Apple's kit has them |
| Device frames | all | 402, 440, 707, 669 and 466 wide, with status bar and home indicator |

## 4. Missing states and gaps
- Pressed, disabled and focus states do not exist for Button, Tab, Filter chip, RSVP choice, List row, Search field, Message field; the fields also lack an error state. (Open since the first version of `design.md`.)
- Radius frame lacks swatches for lg 16 and xl 24; Button variants clip at the right edge in the component doc.
- Text scaling (Dynamic Type) is not checked on any screen.
- Tokens for new needs: highlight tint for search terms (the references suggest a highlighter yellow), asked first, not added.

## 5. Proposed order
1. Done now: translate leftover layer names.
2. Componentise the hand-drawn repeats (status bar, top bar, screen header, tab bar, info row, summary card) and rebuild Invoice card with a nested Status badge.
3. Add new structural elements (avatar, section header, toggle row, sheet, dialog, toast, empty state, banner decision).
4. Add adaptive elements (nav rail, pane layout, Duo side bar, reserved regions, device frames).
5. States (pressed, disabled, focus, error): proposal is to do them in step 5 (hi-fi) and only draw what lo-fi needs now.
6. Fix the radius frame and the Button doc; update the kit documentation page and `design.md`; archive the old four-item bar after lo-fi.

## 6. Decisions needed
1. Approve the list in sections 2 and 3 (add, drop or rename items).
2. States now or in hi-fi (proposal: hi-fi).
3. Is the Reminder row enough as a Banner?
4. Scope of Me: hub, children and teams, membership cards, settings (as in the screen list), or less?

## 7. Result (built 2026-11-06, UI Kit page, section `05 · Screen structure and adaptive`)
Built from the approved list; states, the Banner and the Me scope followed the proposals (states in hi-fi, Reminder row is the banner, Me as in the screen list).

| Done | Notes |
|---|---|
| Status bar (set: Default, Over image) | Replaced 14 hand-drawn copies; Over image is transparent with light text for hero screens |
| Screen header (Title, Description) | 8 screens |
| Top bar (Label) | 5 screens |
| Info row (Icon swap, Text, Copy action) | replaces time, address and participants rows on Event details |
| Avatar (40 px, Initial) | one size only; more sizes need an owner decision |
| Section header (Title, Action) | |
| Toggle row (Off, On) | switch 44 x 24 is a new size, flag for review |
| Toast, Dialog, Bottom sheet, Empty state | Dialog uses the Button component; sheet becomes a side sheet in adaptive layouts |
| Nav rail | five Nav items, for medium, expanded and Duo |
| Duo side bar | back and primary action on top, tab bar at the bottom (vertical controls) |
| Pane layout | list pane (max 320) + detail pane, 707 x 823 |
| Reserved region | annotation overlay for camera and fold |
| Device frame (set) | iPhone 402 x 874, Pro Max 440 x 956, Android medium 707 x 823, Duo inner 669 x 951, Duo outer 466 x 678 |
| Component property names | 33 Finnish names translated (Text, Icon left, Title, ...) |

Not done or changed from the proposal:
- **Tab bar** (tabs row with description): not built; the row is composed of Tab instances and a description text. Revisit in mid-fi.
- **Summary card**: single use on Event details, not componentised.
- **Invoice card with nested Status badge**: done (Status badge variants Unpaid, Overdue, Paid added; Invoice card nests them).
- **Radius frame** (swatches lg 16 and xl 24 added) and **Button doc clipping** (set resized): done.
- The old four-item Bottom bar stays until section 05 is archived after lo-fi approval.
- Reserved region is a generic overlay; Apple's own overlays (outer camera, fold) are in the Apple kit, not copied.
- Duo side bar and Nav rail are static; the active item is fixed to Today (set Active per screen when used).

Checks (2026-11-06): the new section was viewed in Light + Pitch, Dark + Blue and Light + Yellow. One defect found and fixed: the Default Status bar had a raw white fill (now bound to `bg/base`). The Over image status bar is meant for photos only. Not yet checked: Dark + Pitch, Dark + Yellow, Light + Blue (the same roles are used, so low risk, but not verified).
