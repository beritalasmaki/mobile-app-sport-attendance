# Club Coach: device matrix (draft for approval)

Status: **approved 2026-11-06** (step 0 of `docs/plan.md`). Sizes supplied by the owner (Android, iPhone) and read from Apple's Figma kit (Duo: `Product Bezels`, `Layout Guides`). Units are dp (Android) and pt (Apple), 1:1 with Figma pixels.
Android size classes by window width: compact < 600, medium 600-839, expanded >= 840. Apple Duo: compact width on the outer display, regular width on the inner display.

## Devices
| Device / display | Size (w x h) | Class | Role in this project |
|---|---|---|---|
| iPhone 17 Pro / 18 Pro | 402 x 874 | compact | **Base frame**, all screens |
| iPhone 17 Pro Max | 440 x 956 | compact | **Drawn** for key screens: covers the larger base phones before the foldables |
| Galaxy Z Fold 6 cover | 360 x 883 | compact | Narrowest Android width; check for truncation, not drawn |
| Pixel Fold cover | 412 x 841 | compact | Android phone reference frame |
| Android foldable, generic **medium** (600-839 dp) | frame 707 x 823 (Galaxy Z Fold 6 inner, used as the example width) | medium | **Foldable frame**: list-detail, bottom bar or nav rail. Not tied to one model; layout must hold from 600 to 839 dp |
| Pixel Fold inner | 841 x 700 (landscape, as supplied); portrait 700 x 841 is medium | expanded in landscape (841 is 1 dp over the limit) | Note: nav rail and two panes; not drawn separately |
| iPhone Duo inner, portrait | 669 x 951 | regular width | **Duo frame**: horizontal bars, two panes |
| iPhone Duo inner, landscape | 951 x 669 | regular width | Note: controls on the side, two panes |
| iPhone Duo outer, portrait | 466 x 678 | compact width | **Duo frame**: single pane, controls on the side |
| iPhone Duo outer, landscape | 678 x 466 | compact width | Note |

Decisions (owner, 2026-11-06): Android foldables use the generic medium class instead of one model; iPhone Pro Max is added to the drawn frames. The Android phone reference is the Pixel Fold cover (412 x 841). Expanded (>= 840 dp, e.g. Pixel Fold landscape) is covered by notes.

## Frames to draw for key screens (5-6 screens)
1. Compact 402 x 874 (every screen).
2. Compact large 440 x 956 (iPhone Pro Max, key screens).
3. Android medium 707 x 823 (key screens).
4. Duo inner 669 x 951 (key screens).
5. Duo outer 466 x 678 (key screens).
Other sizes are covered by rules, not frames.

## Layout rules
- Size classes and margins, no fixed widths; content gets a maximum width; inputs and buttons are never stretched.
- Compact: one pane, bottom bar (Duo outer: bar on the trailing side). Medium and regular: list-detail (Calendar + Event, Conversations + Thread, Invoices + Invoice). Expanded: nav rail instead of bottom bar.
- Same functions and same hierarchy on every size; the larger size adds one level (the detail pane), it does not rearrange the app.
- Duo: bars, toolbars and the back button move to the trailing edge on the outer display and in inner landscape. Top of the side bar: Back/Close and primary action; bottom: tab bar. Wide text buttons and segmented controls (our tabs, RSVP choice) stay in a horizontal bar. Content gets a horizontal safe-area offset.
- Duo fold: when partially folded, buttons, sheets and alerts move away from the centre; use an even number of grid columns; do not move controls drastically. Keep the controls that affect a list with that pane.
- Reserved regions on the Duo (outer camera / Dynamic Island, inner camera when active, folding region) are overlays in the kit; use them in the frames.
- Android: do not lock to portrait; a bottom sheet may become a side sheet; a card or grid must be rescaled, not just stretched.
- Check text scaling (Dynamic Type / font scale) for every key screen in hi-fi.
