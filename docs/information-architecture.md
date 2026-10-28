# Club Coach: information architecture (draft for approval)

Purpose: replace the structure inherited from the original club app (Aloitussivu, Tapahtumat, Viestit ja laskut, Omat tiedot, plus Ilmoittautumiset and Jäsenkortit as extras)
before the mid-fi screens are redrawn. Status: **proposal, not yet approved**. Problem statements are hypotheses, not research.

## 1. Users and roles
- **Vanhempi** (primary): one or more children, one or more clubs and teams. Wants to know what happens today, sign up fast, pay, ask questions.
- **Valmentaja / apuvalmentaja**: leads one or more teams. Wants to see who is coming, record attendance, message the group, create events.
- One person can be both: role is chosen per team ("Vanhempi" or "Valmentaja"), not by a global mode.
- Out of scope now: club admin tools, shop, in-app payment.

## 2. Principles that shape the structure
1. **One day, whole family** on the first screen: no hunting through menus.
2. **Messages live where the topic lives**: every thread belongs to an event, an invoice or a club announcement. No free-floating inbox of mixed content.
3. **Sign up is the core action**, reachable from list, detail and reminder.
4. **Coach tools appear in context** (inside the event), not as a separate app.

## 3. Navigation (4 items, fixed bottom bar)
| Tab | Parent view | Coach view (same screen, extra tools) |
|---|---|---|
| **Tänään** | Today and this week for all children, unanswered sign-ups, unpaid invoice banner, unread threads | Next events of my teams, who has not answered |
| **Kalenteri** | Tabs: Tulevat / Omat / Ilmoittautumiset (camps, tournaments with deadlines). Filter: child, team, type | Same + "Luo tapahtuma" |
| **Keskustelut** | Threads grouped by topic. Tabs: Tapahtumat / Laskut / Tiedotteet. Unread first | Same + group message to team |
| **Minä** | Children, clubs and teams, Jäsenkortit and passes, Maksut (invoice history), settings, role per team | Joukkueeni (players, parents' contacts) |

Removed from navigation: Verkkokauppa (no need now), separate Ilmoittautumiset and Jäsenkortit entries (moved into Kalenteri and Minä).

## 4. Screens
- **Tänään**: child and club selector, next event card with RSVP, day strip with selected day's events, banners (invoice due, sign-up deadline).
- **Kalenteri**: search, tabs, filter chips, event cards with RSVP. **Tapahtuma**: summary card with RSVP, tabs Tiedot / Osallistujat / Keskustelu (+ Läsnäolo and Kokoonpano for coach).
- **Keskustelut**: list; **Keskustelu** (thread with recipients, composer); invoice threads open **Lasku**.
- **Lasku**: amount, subject, due date, status, details, pay, message to billing (the thread).
- **Minä**: profile hub; **Jäsenkortit** (QR); **Maksut**; **Joukkueeni** (coach); settings.

## 5. Key flows (to be drawn as mid-fi)
1. Parent signs a child up: Tänään banner or Kalenteri card, RSVP, done (2 taps).
2. Parent asks about a ride: Tapahtuma > Keskustelu, choose recipients (parents / coach), send.
3. Parent pays: Tänään banner > Lasku > Maksa; question to billing opens the invoice thread.
4. Coach records attendance: Tapahtuma > Läsnäolo, mark players, save; late changes notify parents.
5. Coach messages team: Keskustelut or Tapahtuma > Keskustelu, recipients = whole team, send.

## 6. Mapping from current mid-fi screens
| Current | New |
|---|---|
| Aloitussivu B | Tänään (keep selector, event card; drop quick tiles, add banners) |
| Tapahtumat lista | Kalenteri (add Ilmoittautumiset tab) |
| Tapahtuma tiedot / osallistujat / viestit | Keep; rename Viestit to Keskustelu; add coach tabs |
| Ilmoittautumiset lista | Becomes tab in Kalenteri |
| Jäsenkortit lista | Under Minä |
| Viestit ja laskut lista, Laskut lista | Keskustelut (tabs Tapahtumat / Laskut / Tiedotteet) |
| Lasku tiedot, Lasku viesti | Keep |
| (new) Minä, Maksut, Joukkueeni, Läsnäolo (coach), Luo tapahtuma | New |

## 7. Open questions
- Is one global role switch per team enough, or does a coach also need a parent view for own child on the same team?
- Do announcements (Tiedotteet) allow replies?
- Invoice payment: external link only, or deep link to bank / MobilePay?
