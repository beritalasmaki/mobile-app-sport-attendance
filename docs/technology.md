# Club Coach: technology approach

Status: proposal. Purpose: a portfolio case where the design is also a working, installable PWA. Backend and security are out of the designer's scope and would be done by hired experts.

## 1. Scope for the portfolio
1. **Figma prototype** of the approved hi-fi screens (shared link, embedded in the portfolio).
2. **PWA front-end with mock data**: React + Vite + TypeScript + Tailwind, deployed to Vercel, installable on a phone's home screen.
3. **Two apps from one codebase**: monorepo with a shared package (tokens, components, mock data, types) and two apps (Club Coach for parents, Club Coach Valmentaja for coaches).

No real accounts, no real data. Names, teams and clubs are fictional. Real crests, photos and any material from the original club app are not used. Children's data is not collected anywhere in the portfolio version.

## 2. What the PWA demonstrates, and what it does not
- Demonstrates: build pipeline, hosting, HTTPS, web manifest and icons (blue for parents, purple for coaches), service worker and offline shell, installability, responsive and safe-area layout, light/dark and club themes from tokens, accessibility checks, tests, CI deploy on push.
- Does not demonstrate: real authentication, a database, server-side permissions, push notifications at scale, data protection in operation. Say so in the case study: "front-end to production; backend specified as an interface".

## 3. Token pipeline
Figma variables map 1:1 to CSS variables (colour roles per mode, club modes, spacing, radius, shadows) and to the Tailwind theme. The tokens live once in the shared package; a club or the coach accent is a different set of variable values, not different components.

## 4. Backend interface (for later, by experts)
- **OpenAPI description** of: events, RSVPs, attendance, threads and messages, announcements (read-only), invoices (amount, subject, due date, status, payment links), teams, roles.
- TypeScript types are written first and the mock data uses them, so replacing mock data with the real API does not change the screens.
- **Roles and permissions** (a product decision, written by the designer): a guardian sees only their own children and their teams; a coach sees the players and guardians of their teams; announcements are sent by coaches and admins and cannot be replied to; invoices are visible only to the guardian they are addressed to.
- **Data protection checklist**: minors' data, guardian relationships, photos, health and allergy information, retention and deletion, consent, data export.
- **Hire**: backend developer, security specialist (authentication, access control, testing), data protection advisor. Push notifications and store publishing need their own work.

## 5. Open choices (decided later, with the experts)
- Native wrapper (React Native/Expo or a Capacitor wrapper) versus staying a PWA, depending on notification and store-presence needs.
- Managed backend (e.g. Supabase, Firebase) versus a custom one. Either needs a reviewed permission model because the data concerns children.
- Sign-in method for guardians and coaches.
