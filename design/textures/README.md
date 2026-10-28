# Motion textures

Grayscale long-exposure motion-blur + film-grain images used as **blended overlays** on brand-colour
gradients. Because they are grayscale, the palette and Light/Dark mode recolour them; the image never changes.

| File | Variant | Use |
|---|---|---|
| `motion-hero.png` | dark, high contrast | hero areas, big headers |
| `motion-calm.png` | light, low contrast | page backgrounds behind content (text contrast must still pass) |

## Regenerate
```
python3 -I motion_texture.py motion-hero.png 1440 900 8 hero 0.25
python3 -I motion_texture.py motion-calm.png 1440 900 8 calm 0.25
```
Arguments: `OUT WIDTH HEIGHT SEED VARIANT [DIAGONAL]`. Needs `numpy` and `Pillow`. Same seed gives the same image;
the image tiles horizontally.

## Recipe in Figma (palette B1 · Pitch Frost)
- Hero: bottom = linear gradient `brand/deep → action/primary → mid green`; over it the hero PNG as image fill,
  blend `SOFT_LIGHT` 100 %, and again with blend `OVERLAY` at 40 %.
- Calm: solid `bg/base`, calm PNG as image fill with blend `SOFT_LIGHT` (90 % light mode, 55 % dark mode),
  plus a green gradient at 22 % (light) / 35 % (dark) fading out.
- Texture never sits directly behind body text without passing the contrast rules in `design.md`.
