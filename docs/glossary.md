# Club Coach: FI -> EN glossary (draft for approval)

Status: **approved and applied 2026-11-06** (step 1 of `docs/plan.md`). Decisions taken: archive drafts stay Finnish (names translated), stale doc text fixed, new fictional "today" Thu 12 Nov 2026, tab `Me`, `Match`. Extra choices made while applying: old four-item bar label `Messages and invoices` is `Inbox` (fits one line); app name `Club Coach for Coaches`; `Töölön Pallo ry` is `Töölö Pallo`; the placeholder link seura.fi became club.example. Source: read-only inventory of the Figma file on 2026-11-06.

## Inventory
| Page | Text nodes | Unique strings | Note |
|---|---|---|---|
| UI Kit | 753 | 319 | tokens, components, documentation prose |
| Mid fidelity | 453 | 211 | 14 screens, 11 rationale blocks |
| Plan | about 130 | | architecture diagram and process meter (prose, translate as a whole) |
| Brainstorming & archive | 1456 | not listed | historical drafts |
| Variables | 4 collections, 225 variables | | modes and some names Finnish |
| Styles | 13 text, 8 effect, 20 paint | | already English |

## Decisions needed from the owner
1. **Archive page** (1456 nodes of old drafts): proposal = translate section and frame names only, leave the old drafts' text as a historical record, and say so in a label. Alternative: translate everything (large, low value).
2. **Stale documentation text on the UI Kit page** (it would otherwise be carried into the portfolio): fix while translating. Found: radius rule says "max 8 px" and "md" for buttons and cards (the system now has lg 16 and xl 24); role `fill/green` (renamed `fill/club`); "Seura-kokoelma" (now Theme); bottom bar "74 px" items (parent bar is about 77 px).
3. **Dates are inconsistent**: screens show "To 18.5." with "ma 18.5.2026" (18 May 2026 is a Monday). Proposal: one fictional "today" = **Thu 12 Nov 2026**; week strip Mon 9 - Sun 15 Nov; events Thu 12, Sat 14, Sun 15 Nov; invoice due dates and deadlines moved to match (due 30 Nov, deadline 20 Nov).
4. **Tab label Minä**: "Me" (proposal) or "Profile".
5. **Football vocabulary**: Peli = "Match" (proposal) or "Game".

## Navigation and screens
| FI | EN |
|---|---|
| Tänään | Today |
| Kalenteri | Calendar |
| Keskustelut | Conversations |
| Laskut | Invoices |
| Minä | Me |
| Aloitussivu (old) | Home |
| Tapahtumat (old) | Events |
| Viestit ja laskut (old) | Messages and invoices |
| Omat tiedot (old) | My details |
| Tulevat / Omat / Muut | Upcoming / Mine / Other |
| Ilmoittautumiset | Sign-ups |
| Viestit / Tiedotteet | Messages / Announcements |
| Kaikki / Treenit / Pelit | All / Training / Matches |
| Treeni / Peli (type dot) | Training / Match |
| Seuraava tapahtuma | Next event |
| Tämä viikko / Näytä koko viikko | This week / Show full week |
| Hae tapahtumia / Hae viestejä | Search events / Search messages |
| Takaisin / Avaa / Kopioi | Back / Open / Copy |
| Avaa Google Mapsissa | Open in Google Maps |

## Event, people, RSVP
| FI | EN |
|---|---|
| Tiedot / Osallistujat / Viestit (event tabs) | Details / Participants / Conversation |
| Osallistuu / Ei osallistu / Ei tiedossa | Going / Not going / Maybe |
| Ilmoittaudu / ILMOITTAUDU | Sign up / SIGN UP |
| 8/12 osallistujaa | 8/12 going |
| Pelaajat (12) / Valmentajat / Apuvalmentajat | Players (12) / Coaches / Assistant coaches |
| Pelaaja / Valmentaja / Apuvalmentaja | Player / Coach / Assistant coach |
| Kirjoita viesti | Write a message |
| Sukunimi Etunimi (name format) | Last name First name |
| Tallenna / Peruuta / Lisää kalenteriin | Save / Cancel / Add to calendar |

## Invoices and membership
| FI | EN |
|---|---|
| Lasku / Laskun tiedot | Invoice / Invoice details |
| Maksamatta / Maksettu / Erääntynyt | Unpaid / Paid / Overdue |
| Eräpäivä | Due date |
| Laskuttaja / Viitenumero / Tilinumero | Biller / Reference number / Account number |
| Aihe | Subject |
| Maksa lasku (old) | Pay invoice (new structure: Pay with bank / Pay with MobilePay) |
| Lähetä viesti laskuttajalle | Message the biller |
| Viesti laskuttajalle | Message to biller |
| Kausimaksu syksy 2026 | Autumn 2026 season fee |
| Turnausmaksu / Jäsenmaksu / Joukkueen takki | Tournament fee / Membership fee / Team jacket |
| Jäsenkortit / Jäsenkortti | Membership cards / Membership card |
| Jäsennumero / Voimassaolo päättyy | Member no. / Valid until |
| Jalkapallopassi / Vakuutusturva | Football passport / Insurance cover |
| 76 PÄIVÄÄ | 76 DAYS |
| Saavutukset / Edut | Achievements / Benefits |
| LUKEMATTA / LASKU | UNREAD / INVOICE |
| Töölön Pallo ry | Töölö Pallo |

## Formats and content
- Dates `Thu 18 May • 17:30-19:00`, money `EUR 120.00`, file size `PDF · 1.2 MB`, 24 h clock.
- Weekdays Ma Ti Ke To Pe La Su -> Mon Tue Wed Thu Fri Sat Sun.
- Fictional proper names stay (Elias Haapala, Antero-Santeri, KTP, HJK, KuPS, Töölö 2017 Siniset, Kotka 2017 Vihreät). Descriptive words are translated: "Sahara artificial turf, pitch 2", "North entrance", "Helsinki Football Club", "Example United".
- Rationale blocks: HYPOTEESI: ONGELMA / KITKA -> HYPOTHESIS: PROBLEM / FRICTION; RATKAISU -> SOLUTION; PERIAATE -> PRINCIPLE. The 11 sentences each are translated in full.

## Components, pages, tokens
| FI | EN |
|---|---|
| Painike / Kortti / Listarivi | Button / Card / List row |
| Tilamerkki / Tyyppipiste / Laskuri | Status badge / Type dot / Counter |
| Päiväsolu / Navi-valinta | Day cell / Nav item |
| Alapalkki / Alapalkki · Vanhempi | Bottom bar / Bottom bar · Parent |
| Aktiivinen=Tänään (variant) | Active=Today |
| Valitsin | Selector |
| Tapahtumarivi / Tapahtumakortti | Event row / Event card |
| Hakukenttä / Välilehti / Suodatinchip | Search field / Tab / Filter chip |
| Ilmoittautumisvalinta | RSVP choice |
| Osallistujarivi / Viestikupla / Viestikenttä | Participant row / Message bubble / Message field |
| Liiterivi / Linkkirivi | Attachment row / Link row |
| Laskukortti / Ilmoitusrivi | Invoice card / Reminder row |
| Tausta / Seura | Background / Club |
| Ikoni / ... , Puhelin / Kotipalkki | Icon / ... , Phone / Home indicator |
| 00 Paletti | 00 Palette |
| 01 Tokenit / 02 Komponentit | 01 Tokens / 02 Components |
| 03 Ikonit ja puhelin | 03 Icons and phone |
| 04 Taustat (seurat) | 04 Backgrounds (clubs) |
| 99 Arkisto | 99 Archive |
| 05 Mid-fidelity (uudet) | 05 Mid-fidelity (old structure, to archive) |
| 06 Mid-fidelity · Vanhempi (uusi rakenne) | 06 Mid-fidelity · Parent (new structure) |
| 07 Prosessimittari / 08 Design system -arkkitehtuuri | 07 Process meter / 08 Design system architecture |
| Collection `Club Coach · Muoto` | `Club Coach · Shape` |
| Collection `Teema` | `Theme` |
| Modes Vaalea / Tumma / Harmaa (mid-fi) | Light / Dark / Grey (mid-fi) |
| Theme modes Pitch / Sininen / Keltainen | Pitch / Blue / Yellow |
| Primitives mode `Arvo` | `Value` |
| Primitives groups `sininen`, `keltainen` | `blue`, `yellow` (variable paths checked in the apply step; bindings keep working because renames keep IDs) |
| Seura (club) in prose | Club |

## Apply order (after approval)
1. Variables, modes and collections (names only; verify bindings and values unchanged, light and dark, 3 themes).
2. Components, variants, pages, sections, frames.
3. Text on UI Kit, Plan and Mid fidelity (fonts loaded per style; dates and amounts per the format rules; screenshots before and after).
4. Archive names.
5. Docs: translate `design.md` names, `information-architecture.md`; update `project-log.md`.
Each step is checked with a search for remaining Finnish characters (ä, ö, å) and common Finnish words.
