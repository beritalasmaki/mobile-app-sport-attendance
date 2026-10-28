# Club Coach: information architecture (draft for approval)

Purpose: replace the structure inherited from the original club app before the mid-fi screens are redrawn.
Status: **proposal, not yet approved**. Problem statements are hypotheses, not research.

## 1. Two apps, one system
- **Club Coach** (vanhemmat): for guardians of one or more children in one or more clubs.
- **Club Coach Valmentaja** (valmentajat ja apuvalmentajat): for people who lead teams.
- Shared: design system (tokens, components), account and login, backend, event and message data.
- A person who is both coach and parent installs both apps with the same account. No role switch inside an app.
- Out of scope now: club admin tools, shop, in-app payment.
- App identity: parents' app icon and accent are blue, the coach app uses a purple icon and accent. Same tokens, structure and components; the coach accent is a new mode of the club-colour variables.
- Fallback if testing shows two apps is too heavy: one app with a "Koti / Työ" mode switch in Minä, using the same screens.

Why two: the jobs differ (parent: answer, pay, ask; coach: roster, attendance, group messages, create events), so each app keeps its own small navigation and home.
Home and work stay apart, notifications are not mixed, and the risk of messaging the wrong audience falls.
Cost: two store listings and releases, two notification streams for dual-role users (mitigated by shared account, deep links between the apps and notification settings per app).

## 2. Principles
1. **One day, whole family** on the parent's first screen.
2. **Messages live where the topic lives**: every thread belongs to an event or an invoice. Announcements are separate and read-only.
3. **Sign up is the core parent action**, reachable from list, detail and reminder.
4. **Coach tools are the coach app's core**, not extras inside the parent flow.

## 3. Club Coach (vanhemmat): navigation, 5 tabs
| Tab | Content |
|---|---|
| **Tänään** | Today and this week for all children, unanswered sign-ups, unpaid invoice banner, unread threads |
| **Kalenteri** | Tabs: Tulevat / Omat / Ilmoittautumiset (camps, tournaments with deadlines). Filter: child, team, type |
| **Keskustelut** | Tabs: Tapahtumat / Tiedotteet. Unread first |
| **Laskut** | Unpaid first, then paid. Invoice detail with Maksa pankissa / Maksa MobilePaylla and the message to billing. Banner count on the tab |
| **Minä** | Children, clubs and teams, Jäsenkortit and passes, settings |

## 4. Club Coach Valmentaja: navigation, 4 tabs (proposal)
| Tab | Content |
|---|---|
| **Tänään** | Next events of my teams, who has not answered, unread team threads |
| **Tapahtumat** | List and filter by team, create event. Event: Tiedot / Osallistujat / Läsnäolo / Kokoonpano / Keskustelu |
| **Viestit** | Team and event threads, group message to team or to parents |
| **Joukkueet** | Players, parents' contacts, coaches and roles |

No payments and no Jäsenkortit in the coach app.

## 5. Screens
- **Tänään**: child and club selector (parent), next event card with RSVP, day strip with the selected day's events, banners (invoice due, sign-up deadline).
- **Kalenteri / Tapahtumat**: search, tabs, filter chips, event cards. **Tapahtuma**: summary card with RSVP, tabs Tiedot / Osallistujat / Keskustelu (coach adds Läsnäolo and Kokoonpano).
- **Laskut**: list (amount, subject, due date, status) and **Lasku** detail. **Keskustelut**: list. **Keskustelu**: thread with recipients and composer. **Tiedote**: read-only, no replies, no composer.
- **Lasku**: amount, subject, due date, status, details, buttons **Maksa pankissa** (icon banknotes) and **Maksa MobilePaylla** (icon device-phone-mobile), message to billing (the invoice thread).
- **Minä**: profile hub, Jäsenkortit (QR), settings. Paid invoices stay in Laskut.

## 6. Decisions on content
- **Announcements** are general notices: read-only, no replies. Questions go to event or invoice threads.
- **Invoice payment** = external links to the bank and MobilePay. No in-app payment, no card handling, no payment-provider integration in v1.

## 7. Key flows (to be drawn as mid-fi)
1. Parent signs a child up: Tänään banner or Kalenteri card, RSVP, done (2 taps).
2. Parent asks about a ride: Tapahtuma > Keskustelu, choose recipients (parents / coach), send.
3. Parent pays: Tänään banner or Laskut tab > Lasku > Maksa pankissa / MobilePaylla (leaves the app); question to billing opens the invoice thread.
4. Coach records attendance (coach app): Tapahtuma > Läsnäolo, mark players, save; late changes notify parents.
5. Coach messages team (coach app): Viestit or Tapahtuma > Keskustelu, recipients = whole team, send.

## 8. Shared components and cross-app rules
- Shared: Tapahtumakortti, Tapahtumarivi, Välilehti, Suodatinchip, Osallistujarivi, Viestikupla, Viestikenttä, Liiterivi, Linkkirivi, Osoitekortti, Alapalkki, Painike, Kortti, Listarivi, Tilamerkki.
- Parent only: Laskukortti, Jäsenkortti, Ilmoittautumisvalinta (own RSVP). Coach only: attendance row, roster row, Läsnäolo and Kokoonpano views.
- Notifications are sent per app by role. A dual-role user sees each notification only once, in the app that fits it, and can open the other app from it through a deep link.
- Both apps use the same event and thread ids, so a link from one opens the same item in the other.

## 9. Mapping from current mid-fi screens
| Current | New |
|---|---|
| Aloitussivu B | Parent: Tänään (keep selector, event card; drop quick tiles, add banners) |
| Tapahtumat lista | Parent: Kalenteri (add Ilmoittautumiset tab) |
| Tapahtuma tiedot / osallistujat / viestit | Parent: keep, rename Viestit to Keskustelu. Coach: same base plus Läsnäolo and Kokoonpano |
| Ilmoittautumiset lista | Tab in Kalenteri |
| Jäsenkortit lista | Under Minä (parent) |
| Viestit ja laskut lista | Keskustelut (tabs Tapahtumat / Tiedotteet) |
| Laskut lista | Laskut tab |
| Lasku tiedot | Keep, add the two payment link buttons |
| Lasku viesti | Keep |
| (new, parent) | Minä, Tiedote |
| (new, coach app) | Tänään, Tapahtumat, Läsnäolo, Kokoonpano, Luo tapahtuma, Viestit, Joukkueet |

## 10. Decided and open
- Decided: invoices have their own tab (5 tabs for parents; the bottom bar component is resized from 92 px to 80 px items, labels stay on one line).
- Decided: coach app has its own accent (purple, with a purple app icon); the parent app stays blue. A coach's own child is handled in the parent app.
- Open: purple accent needs a contrast check in light and dark mode before it is added to the tokens.
- Open: repo name stays `mobile-app-sport-attendance`.
