# Club Coach: device matrix (draft for approval)

Status: **draft, step 0 of `docs/plan.md`**. Sizes supplied by the owner (Android, iPhone) and read from Apple's Figma kit (Duo: `Product Bezels`, `Layout Guides`). Units are dp (Android) and pt (Apple), 1:1 with Figma pixels.
Android size classes by window width: compact < 600, medium 600-839, expanded >= 840. Apple Duo: compact width on the outer display, regular width on the inner display.

## Devices
| Device / display | Size (w x h) | Class | Role in this project |
|---|---|---|---|
| iPhone 17 Pro / 18 Pro | 402 x 874 | compact | **Base frame**, all screens |
| iPhone 17 Pro Max | 440 x 956 | compact | Not drawn; checked with constraints (fill width, no fixed widths) |
| Galaxy Z Fold 6 cover | 360 x 883 | compact | Narrowest Android width; check for truncation, not drawn |
| Pixel Fold cover | 412 x 841 | compact | Android phone reference frame |
| Galaxy Z Fold 6 inner | 707 x 823 (portrait) | medium | **Foldable frame**: list-detail, bottom bar or nav rail |
| Pixel Fold inner | 841 x 700 (landscape, as supplied); portrait 700 x 841 is medium | expanded in landscape (841 is 1 dp over the limit) | Note: nav rail and two panes; not drawn separately |
| iPhone Duo inner, portrait | 669 x 951 | regular width | **Duo frame**: horizontal bars, two panes |
| iPhone Duo inner, landscape | 951 x 669 | regular width | Note: controls on the side, two panes |
| iPhone Duo outer, portrait | 466 x 678 | compact width | **Duo frame**: single pane, controls on the side |
| iPhone Duo outer, landscape | 678 x 466 | compact width | Note |

To confirm: orientation of the two supplied foldable sizes (Fold 6 inner given as 707 x 823, Pixel Fold inner as 841 x 700), and that the Android phone reference is the Pixel Fold cover (412 x 841) instead of a 412 x 915 phone I had assumed earlier.

## Frames to draw for key screens (5-6 screens)
1. Compact 402 x 874 (every screen).
2. Android medium 707 x 823.
3. Duo inner 669 x 951.
4. Duo outer 466 x 678.
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
