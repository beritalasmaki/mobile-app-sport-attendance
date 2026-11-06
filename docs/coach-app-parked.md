# Club Coach for Coaches (coach app): parked specs

Status: **out of scope for now** (decision 2026-11-06). Everything needed to restart is collected here. Sources stay in the other docs; this file is the entry point.
Names are English (translated 2026-11-06). The Finnish working names were Läsnäolo (Attendance), Kokoonpano (Line-up) and Joukkueet (Teams). App name: Club Coach for Coaches (was Club Coach Valmentaja).

## Purpose
For coaches and assistant coaches who lead teams. Jobs: roster, attendance, group messages, create events. Own small navigation and home, so home and work stay apart and the wrong audience is not messaged.

## Navigation (4 tabs, proposal)
| Tab | Content |
|---|---|
| Today | Next events of my teams, who has not answered, unread team threads |
| Events | List and filter by team, create event. Event: Details / Participants / Attendance / Line-up / Conversation |
| Messages | Team and event threads, group message to team or to parents |
| Teams | Players, parents' contacts, coaches and roles |

No payments and no member cards in the coach app.

## Identity
- Purple accent and purple app icon; the parent app stays blue. Implemented as a new mode of the club-colour variables (`Teema`/Theme), not as new components.
- Open: the purple needs a contrast check in light and dark mode before it is added to the tokens.

## Flows to draw
4. Coach records attendance: Event > Attendance, mark players, save; late changes notify parents.
5. Coach messages team: Messages or Event > Conversation, recipients = whole team, send.

## Components
- Coach only: attendance row, roster row, Attendance and Line-up views.
- Shared with the parent app: event card and row, tabs, filter chip, participant row, message bubble and field, attachment and link rows, address card, bottom bar, button, card, list row, status badge.

## Rules and cross-app behaviour
- A person who is both parent and coach installs both apps with one account; no role switch in an app. A coach's own child is handled in the parent app.
- Notifications are sent per app by role and shown once; deep links open the same item in the other app (same event and thread ids).
- Announcements are sent by coaches and admins and cannot be replied to.
- Fallback if testing shows two apps is too heavy: one app with a Home / Work mode switch in the profile tab.

## Where the full text lives
- `docs/information-architecture.md`: sections 1 (two apps), 4 (coach navigation), 7 (flows 4 and 5), 8 (components, cross-app rules), 10 (decisions).
- `docs/technology.md`: roles and permissions (a coach sees players and guardians of their teams), monorepo with two apps.
- `docs/project-log.md`: entries 17 (decision to split) and 18 (scope).
- Figma: process meter on the Plan page lists coach screens as "to do"; no coach screens exist yet.
