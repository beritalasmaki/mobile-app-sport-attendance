# Club Coach: information architecture (draft for approval)

Purpose: replace the structure inherited from the original club app before the mid-fi screens are redrawn.
Status: **proposal, not yet approved**. Problem statements are hypotheses, not research.

## 1. Two apps, one system
- **Club Coach** (parents): for guardians of one or more children in one or more clubs.
- **Club Coach for Coaches** (coaches and assistant coaches): for people who lead teams.
- Shared: design system (tokens, components), account and login, backend, event and message data.
- A person who is both coach and parent installs both apps with the same account. No role switch inside an app.
- Out of scope now: club admin tools, shop, in-app payment.
- App identity: parents' app icon and accent are blue, the coach app uses a purple icon and accent. Same tokens, structure and components; the coach accent is a new mode of the club-colour variables.
- Fallback if testing shows two apps is too heavy: one app with a "Home / Work" mode switch in Me, using the same screens.

Why two: the jobs differ (parent: answer, pay, ask; coach: roster, attendance, group messages, create events), so each app keeps its own small navigation and home.
Home and work stay apart, notifications are not mixed, and the risk of messaging the wrong audience falls.
Cost: two store listings and releases, two notification streams for dual-role users (mitigated by shared account, deep links between the apps and notification settings per app).

## 2. Principles
1. **One day, whole family** on the parent's first screen.
2. **Messages live where the topic lives**: every thread belongs to an event or an invoice. Announcements are separate and read-only.
3. **Sign up is the core parent action**, reachable from list, detail and reminder.
4. **Coach tools are the coach app's core**, not extras inside the parent flow.

## 3. Club Coach (parents): navigation, 5 tabs
| Tab | Content |
|---|---|
| **Today** | Today and this week for all children, unanswered sign-ups, unpaid invoice banner, unread threads |
| **Calendar** | Tabs: Upcoming / Mine / Sign-ups (camps, tournaments with deadlines). Filter: child, team, type |
| **Conversations** | Tabs: Events / Announcements. Unread first |
| **Invoices** | Unpaid first, then paid. Invoice detail with Pay with bank / Pay with MobilePay and the message to billing. Banner count on the tab |
| **Me** | Children, clubs and teams, Membership cards and passes, settings |

## 4. Club Coach for Coaches: navigation, 4 tabs (proposal)
| Tab | Content |
|---|---|
| **Today** | Next events of my teams, who has not answered, unread team threads |
| **Events** | List and filter by team, create event. Event: Details / Participants / Attendance / Line-up / Conversation |
| **Messages** | Team and event threads, group message to team or to parents |
| **Teams** | Players, parents' contacts, coaches and roles |

No payments and no Membership cards in the coach app.

## 5. Screens
- **Today**: child and club selector (parent), next event card with RSVP, day strip with the selected day's events, banners (invoice due, sign-up deadline).
- **Calendar / Events**: search, tabs, filter chips, event cards. **Event**: summary card with RSVP, tabs Details / Participants / Conversation (coach adds Attendance and Line-up).
- **Invoices**: list (amount, subject, due date, status) and **Invoice** detail. **Conversations**: list. **Conversation**: thread with recipients and composer. **Announcement**: read-only, no replies, no composer.
- **Invoice**: amount, subject, due date, status, details, buttons **Pay with bank** (icon banknotes) and **Pay with MobilePay** (icon device-phone-mobile), message to billing (the invoice thread).
- **Me**: profile hub, Membership cards (QR), settings. Paid invoices stay in Invoices.

## 6. Decisions on content
- **Announcements** are general notices: read-only, no replies. Questions go to event or invoice threads.
- **Invoice payment** = external links to the bank and MobilePay. No in-app payment, no card handling, no payment-provider integration in v1.

## 7. Key flows (to be drawn as mid-fi)
1. Parent signs a child up: Today banner or Calendar card, RSVP, done (2 taps).
2. Parent asks about a ride: Event > Conversation, choose recipients (parents / coach), send.
3. Parent pays: Today banner or Invoices tab > Invoice > Pay with bank / MobilePaylla (leaves the app); question to billing opens the invoice thread.
4. Coach records attendance (coach app): Event > Attendance, mark players, save; late changes notify parents.
5. Coach messages team (coach app): Messages or Event > Conversation, recipients = whole team, send.

## 8. Shared components and cross-app rules
- Shared: Event card, Event row, Tab, Filter chip, Participant row, Message bubble, Message field, Attachment row, Link row, Address card, Bottom bar, Button, Card, List row, Status badge.
- Parent only: Invoice card, Membership card, RSVP choice (own RSVP). Coach only: attendance row, roster row, Attendance and Line-up views.
- Notifications are sent per app by role. A dual-role user sees each notification only once, in the app that fits it, and can open the other app from it through a deep link.
- Both apps use the same event and thread ids, so a link from one opens the same item in the other.

## 9. Mapping from current mid-fi screens
| Current | New |
|---|---|
| Home B | Parent: Today (keep selector, event card; drop quick tiles, add banners) |
| Events list | Parent: Calendar (add Sign-ups tab) |
| Event details / participants / messages | Parent: keep, rename Messages to Conversation. Coach: same base plus Attendance and Line-up |
| Sign-ups list | Tab in Calendar |
| Membership cards lista | Under Me (parent) |
| Messages and invoices list | Conversations (tabs Events / Announcements) |
| Invoices list | Invoices tab |
| Invoice details | Keep, add the two payment link buttons |
| Invoice message | Keep |
| (new, parent) | Me, Announcement |
| (new, coach app) | Today, Events, Attendance, Line-up, Create event, Messages, Teams |

## 10. Decided and open
- Decided: invoices have their own tab (5 tabs for parents; the new component `Bottom bar · Parent` has items of about 77 px (the old 4-item `Bottom bar` stays for the archived screens), labels stay on one line).
- Decided: coach app has its own accent (purple, with a purple app icon); the parent app stays blue. A coach's own child is handled in the parent app.
- Open: purple accent needs a contrast check in light and dark mode before it is added to the tokens.
- Open: repo name stays `mobile-app-sport-attendance`.
