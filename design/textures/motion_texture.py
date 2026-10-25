"""Procedural long-exposure motion-blur + film-grain texture (grayscale PNG).

Built like a real exposure: a crisp, blotchy random scene is smeared horizontally with a blur length that
changes from row to row (so streaks start and end raggedly), then toned and grained.
Used as a blended overlay (SOFT_LIGHT / OVERLAY) over a brand-colour gradient, so the same grayscale asset is
recoloured by the palette and by Light/Dark mode. Deterministic: same seed -> same image. Tileable horizontally.

Usage:  python3 -I motion_texture.py OUT.png WIDTH HEIGHT SEED VARIANT [DIAGONAL]
        VARIANT  = hero (dark, high contrast, for hero areas) | calm (light, low contrast, behind content)
        DIAGONAL = optional, shear of the motion as a fraction of the width (e.g. 0.25), default 0
Needs:  numpy, Pillow
"""
import sys
import numpy as np
from PIL import Image

out, W, H, seed, variant = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
diag = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
if variant not in ('hero', 'calm'):
    sys.exit('VARIANT must be hero or calm')
rng = np.random.default_rng(seed)
U = np.fft.fftfreq(W)[None, :]
V = np.fft.fftfreq(H)[:, None]

def blur(a, sx, sy):
    g = np.exp(-2 * np.pi ** 2 * ((sx * U) ** 2 + (sy * V) ** 2))
    return np.fft.ifft2(np.fft.fft2(a) * g).real

def norm(a):
    return (a - a.mean()) / a.std()

def smooth1d(n, scale):
    v = np.fft.fftfreq(n)
    x = np.fft.ifft(np.fft.fft(rng.standard_normal(n)) * np.exp(-2 * np.pi ** 2 * (scale * v) ** 2)).real
    return x / x.std()

# 1) the "scene": blotchy, multi-scale, with fairly hard edges (this is what gets smeared)
scene = sum(w * norm(blur(rng.standard_normal((H, W)), s, s)) for s, w in [(3, 0.4), (9, 0.9), (24, 1.0), (60, 0.9), (150, 0.7)])
scene = 1 / (1 + np.exp(-norm(scene) * 1.8))

# 2) horizontal smear whose length varies per row (short = crisp, long = silky)
levels = [14, 40, 90, 190, 380, 700]
stack = [blur(scene, s, 0.6) for s in levels]
p = smooth1d(H, H * 0.05)                       # row-wise "exposure length" profile
p = np.clip((p * 0.9 + 2.2) / 4.4 * (len(levels) - 1) + 0.0, 0, len(levels) - 1.001)
lo = np.floor(p).astype(int); fr = (p - lo)[:, None]
rows = np.arange(H)
smear = np.stack([stack[lo[y]][y] * (1 - fr[y]) + stack[lo[y] + 1][y] * fr[y] for y in rows])

# 3) optional diagonal drift (shear) + large light/dark masses like the reference exposures
if diag:
    sh = (diag * W * (rows / H - 0.5)).astype(int)
    smear = np.take_along_axis(smear, (np.arange(W)[None, :] - sh[:, None]) % W, axis=1)
mass = norm(blur(rng.standard_normal((H, W)), W * 0.45, H * 0.16))
f = norm(smear) * 0.85 + mass * 0.9
f = norm(blur(f, 3, 0.5))

# 4) tone
f = (f - np.percentile(f, 2)) / (np.percentile(f, 98) - np.percentile(f, 2))
f = np.clip(f, 0, 1)
if variant == 'hero':
    f = 1 / (1 + np.exp(-(f - 0.46) * 7.0))
else:
    f = 1 / (1 + np.exp(-(f - 0.5) * 3.5))
f = (f - f.min()) / (f.max() - f.min())
if variant == 'hero':
    yy, xx = np.mgrid[0:H, 0:W]
    f *= 1 - 0.18 * (((yy - H / 2) / (H / 2)) ** 2) - 0.08 * (((xx - W / 2) / (W / 2)) ** 2)
else:
    f = 0.38 + 0.42 * f
# 5) film grain, strongest in the mid-tones
grain = rng.standard_normal((H, W))
gb = blur(grain, 0.5, 0.5)
grain = 0.65 * grain + 0.35 * gb / gb.std()
f = np.clip(f + grain * (0.05 if variant == 'hero' else 0.035) * (0.4 + 3.0 * f * (1 - f)), 0, 1)
Image.fromarray((f * 255).astype(np.uint8), 'L').save(out, optimize=True)
print(out, W, H, variant, round(float(f.mean()), 3))
