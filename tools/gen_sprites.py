from __future__ import annotations

from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]


def rgba(color: str, alpha: int = 255):
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def canvas(size: int, color=(0, 0, 0, 0)):
    return Image.new("RGBA", (size, size), color)


def save(img: Image.Image, rel: str):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG")


def paste(dst: Image.Image, src: Image.Image):
    return Image.alpha_composite(dst, src)


def glow_layer(size: int, center, color, radius: float, strength: int = 180):
    img = canvas(size)
    draw = ImageDraw.Draw(img)
    cx, cy = center
    for r in range(int(radius), 0, -1):
        t = r / radius
        a = int(strength * (1 - t) ** 1.7)
        if a <= 0:
            continue
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color[:-1] + (a,))
    return img.filter(ImageFilter.GaussianBlur(1.25))


def soft_sheen(draw: ImageDraw.ImageDraw, box, color):
    x1, y1, x2, y2 = box
    draw.arc((x1, y1, x2, y2), 210, 330, fill=color, width=2)


def base_machine(size: int, margin: int = 4):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    x1 = margin
    y1 = margin
    x2 = size - margin - 1
    y2 = size - margin - 1
    d.rounded_rectangle((x1, y1, x2, y2), radius=max(3, size // 10), fill=rgba("24323f"), outline=rgba("6d7584"), width=2)
    d.rounded_rectangle((x1 + 3, y1 + 3, x2 - 3, y2 - 3), radius=max(2, size // 12), fill=rgba("3b4453"), outline=rgba("aeb7c7", 210), width=1)
    return img


def add_holy_core(img: Image.Image, center, outer_radius, inner_radius, glow="#ffd45e"):
    img = paste(img, glow_layer(img.size[0], center, rgba(glow), outer_radius, 180))
    d = ImageDraw.Draw(img)
    cx, cy = center
    d.ellipse((cx - inner_radius, cy - inner_radius, cx + inner_radius, cy + inner_radius), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    d.line((cx - inner_radius + 2, cy - inner_radius + 2, cx + inner_radius - 2, cy + inner_radius - 2), fill=rgba("fff8e8", 120), width=1)
    return img


def add_metal_braces(draw: ImageDraw.ImageDraw, size: int, margin: int = 4):
    s = size - margin - 1
    draw.line((margin + 2, margin + 6, margin + 6, margin + 2), fill=rgba("8f99ab"), width=2)
    draw.line((s - 2, margin + 6, s - 6, margin + 2), fill=rgba("8f99ab"), width=2)
    draw.line((margin + 2, s - 6, margin + 6, s - 2), fill=rgba("8f99ab"), width=2)
    draw.line((s - 2, s - 6, s - 6, s - 2), fill=rgba("8f99ab"), width=2)


def make_item_icon(theme: str):
    img = canvas(32)
    d = ImageDraw.Draw(img)
    d.ellipse((3, 3, 29, 29), fill=rgba("33261a"), outline=rgba("a47a2f"), width=2)
    img = paste(img, glow_layer(32, (16, 16), rgba(theme), 12, 140))
    d = ImageDraw.Draw(img)
    d.polygon([(16, 5), (22, 9), (20, 15), (13, 13), (11, 8)], fill=rgba(theme), outline=rgba("fff0bb"))
    d.polygon([(9, 16), (13, 12), (18, 15), (16, 22), (10, 20)], fill=rgba("e0b445"), outline=rgba("fff4cf"))
    d.polygon([(18, 16), (24, 14), (27, 18), (23, 24), (18, 21)], fill=rgba("f3cd68"), outline=rgba("fff6d5"))
    for p in [(6, 8), (24, 7), (7, 24), (24, 24), (4, 16), (28, 16)]:
        d.point(p, fill=rgba("fff8df"))
    return img.filter(ImageFilter.GaussianBlur(0.15))


def make_water_icon():
    img = canvas(32)
    d = ImageDraw.Draw(img)
    img = paste(img, glow_layer(32, (16, 16), rgba("86d7ff"), 13, 120))
    d = ImageDraw.Draw(img)
    d.ellipse((6, 5, 26, 27), fill=rgba("78cfff", 210), outline=rgba("e6fbff"), width=2)
    d.polygon([(16, 4), (22, 11), (16, 17), (10, 11)], fill=rgba("9be4ff", 220), outline=rgba("ffffff"))
    soft_sheen(d, (9, 8, 22, 19), rgba("ffffff", 150))
    d.ellipse((11, 10, 15, 14), fill=rgba("ffffff", 170))
    return img.filter(ImageFilter.GaussianBlur(0.15))


def make_refinery(size: int):
    img = base_machine(size)
    d = ImageDraw.Draw(img)
    m = 4
    s = size - m - 1
    d.rounded_rectangle((m + 8, m + 10, s - 8, s - 10), radius=5, fill=rgba("535d6d"), outline=rgba("c1c8d3"), width=2)
    d.rounded_rectangle((m + 15, m + 18, s - 15, s - 16), radius=4, fill=rgba("70461d"), outline=rgba("ffd45e"), width=2)
    d.rectangle((m + 10, s - 15, s - 10, s - 8), fill=rgba("424b5b"), outline=rgba("aab3c1"), width=1)
    d.line((size // 2, m + 5, size // 2, m + 16), fill=rgba("fff4cf"), width=2)
    img = add_holy_core(img, (size // 2, size // 2 + 3), size // 4, size // 8)
    d = ImageDraw.Draw(img)
    d.line((m + 7, size // 2 - 3, m + 14, size // 2 - 3), fill=rgba("c07a3a"), width=3)
    d.line((s - 7, size // 2 - 3, s - 14, size // 2 - 3), fill=rgba("c07a3a"), width=3)
    d.rectangle((size // 2 - 6, size // 2 + 10, size // 2 + 6, size // 2 + 16), fill=rgba("ffe7a7"))
    return img.filter(ImageFilter.GaussianBlur(0.2))


def make_drill_body(size: int, tier: int, glow: str):
    img = base_machine(size)
    d = ImageDraw.Draw(img)
    m = 4
    c = size // 2
    d.rectangle((c - 5, m + 8, c + 5, size - m - 10), fill=rgba("6c7484"), outline=rgba("d5dbe5"), width=1)
    d.polygon([(c - 11, m + 16), (c - 3, m + 10), (c - 1, m + 16), (c - 8, m + 22)], fill=rgba("8c96a9"))
    d.polygon([(c + 11, m + 16), (c + 3, m + 10), (c + 1, m + 16), (c + 8, m + 22)], fill=rgba("8c96a9"))
    d.rectangle((m + 10, size - m - 13, size - m - 10, size - m - 8), fill=rgba("7c8596"))
    d.rectangle((size - m - 13, size - m - 13, size - m - 10, size - m - 8), fill=rgba("7c8596"))
    img = paste(img, glow_layer(size, (c, c), rgba(glow), size * 0.28, 120))
    d = ImageDraw.Draw(img)
    img = add_holy_core(img, (c, c - 1), size // 5, max(3, size // 10), glow)
    if tier >= 4:
        d.ellipse((c - 6, c + 5, c + 6, c + 17), fill=rgba("fff2b8"), outline=rgba("ffd45e"))
    soft_sheen(d, (m + 6, m + 6, size - m - 6, size - m - 6), rgba("fff8df", 90))
    return img.filter(ImageFilter.GaussianBlur(0.2))


def make_drill_rotator(size: int, glow: str):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    arm = max(7, size // 4)
    d.polygon([(c, c - arm), (c + 5, c - 5), (c + 16, c - 12), (c + 12, c - 2), (c + 7, c + 7), (c + 2, c + 5)], fill=rgba("7b8598"), outline=rgba("dce2ea"))
    d.polygon([(c, c + arm), (c + 5, c + 5), (c + 16, c + 12), (c + 12, c + 2), (c + 7, c - 7), (c + 2, c - 5)], fill=rgba("7b8598"), outline=rgba("dce2ea"))
    d.polygon([(c - arm, c), (c - 5, c + 5), (c - 12, c + 16), (c - 2, c + 12), (c + 7, c + 7), (c + 5, c + 2)], fill=rgba("7b8598"), outline=rgba("dce2ea"))
    d.polygon([(c + arm, c), (c + 5, c + 5), (c + 12, c + 16), (c + 2, c + 12), (c - 7, c + 7), (c - 5, c + 2)], fill=rgba("7b8598"), outline=rgba("dce2ea"))
    img = paste(img, glow_layer(size, (c, c), rgba(glow), size * 0.24, 90))
    d = ImageDraw.Draw(img)
    d.ellipse((c - 4, c - 4, c + 4, c + 4), fill=rgba("ffd45e"), outline=rgba("fff8df"))
    return img.filter(ImageFilter.GaussianBlur(0.1))


def make_drill_top(size: int, glow: str, wide: bool = False):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    if wide:
        d.rounded_rectangle((c - 12, c - 7, c + 12, c + 7), radius=4, fill=rgba("4d5768"), outline=rgba("d9deea"))
    else:
        d.rounded_rectangle((c - 10, c - 6, c + 10, c + 6), radius=3, fill=rgba("4d5768"), outline=rgba("d9deea"))
    d.line((c, c - 8, c, c + 8), fill=rgba(glow), width=2)
    d.line((c - 8, c, c + 8, c), fill=rgba(glow), width=2)
    return img


def make_generator(size: int, mode: str):
    img = base_machine(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    m = 4
    if mode == "dust-reactor":
        d.rounded_rectangle((m + 8, m + 8, size - m - 9, size - m - 9), radius=6, fill=rgba("433b34"), outline=rgba("c8a156"), width=2)
        img = paste(img, glow_layer(size, (c, c), rgba("ffd45e"), size * 0.28, 150))
        d = ImageDraw.Draw(img)
        d.ellipse((c - 10, c - 10, c + 10, c + 10), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
        d.line((c, m + 6, c, m + 16), fill=rgba("fff4cf"), width=2)
        d.rectangle((m + 7, size - m - 14, m + 16, size - m - 7), fill=rgba("c8a156"))
        d.rectangle((size - m - 16, size - m - 14, size - m - 7, size - m - 7), fill=rgba("c8a156"))
    elif mode == "blessed-turbine":
        d.rounded_rectangle((m + 9, m + 12, size - m - 10, size - m - 8), radius=6, fill=rgba("40505f"), outline=rgba("aeb7c7"), width=2)
        img = paste(img, glow_layer(size, (c, c), rgba("86d7ff"), size * 0.24, 120))
        d = ImageDraw.Draw(img)
        d.ellipse((c - 11, c - 11, c + 11, c + 11), fill=rgba("7fd8ff"), outline=rgba("e8fbff"), width=2)
        d.line((c, m + 8, c, m + 18), fill=rgba("e8fbff"), width=2)
        d.polygon([(c - 13, c + 5), (c - 18, c + 10), (c - 10, c + 12), (c - 7, c + 7)], fill=rgba("7b8798"))
        d.polygon([(c + 13, c + 5), (c + 18, c + 10), (c + 10, c + 12), (c + 7, c + 7)], fill=rgba("7b8798"))
    else:  # holy-panel
        d.rounded_rectangle((m + 10, m + 10, size - m - 10, size - m - 10), radius=5, fill=rgba("3e4655"), outline=rgba("aeb7c7"), width=2)
        img = paste(img, glow_layer(size, (c, c), rgba("ffd45e"), size * 0.22, 90))
        d = ImageDraw.Draw(img)
        d.rectangle((m + 14, m + 15, size - m - 15, size - m - 15), fill=rgba("6689a8"), outline=rgba("fff4cf"), width=1)
        d.line((m + 15, c, size - m - 15, c), fill=rgba("dfe8f3", 80), width=1)
        d.line((c, m + 15, c, size - m - 15), fill=rgba("dfe8f3", 80), width=1)
        d.ellipse((c - 4, c - 4, c + 4, c + 4), fill=rgba("ffd45e"))
    return img.filter(ImageFilter.GaussianBlur(0.15))


def make_generator_top(size: int, mode: str):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    if mode == "dust-reactor":
        d.rectangle((c - 6, c - 11, c + 6, c + 11), fill=rgba("7d8796"), outline=rgba("dbe1ea"))
        d.line((c - 8, c - 6, c + 8, c - 6), fill=rgba("ffd45e"), width=2)
        d.line((c - 8, c + 6, c + 8, c + 6), fill=rgba("ffd45e"), width=2)
    elif mode == "blessed-turbine":
        d.ellipse((c - 11, c - 11, c + 11, c + 11), outline=rgba("e9fbff"), width=2)
        for i in range(6):
            ang = i * (2 * pi / 6)
            x = c + cos(ang) * 8
            y = c + sin(ang) * 8
            d.line((c, c, x, y), fill=rgba("9fe3ff"), width=2)
        d.ellipse((c - 4, c - 4, c + 4, c + 4), fill=rgba("e9fbff"))
    else:
        d.rectangle((c - 12, c - 3, c + 12, c + 3), fill=rgba("ffd45e"))
        d.rectangle((c - 3, c - 12, c + 3, c + 12), fill=rgba("ffd45e"))
    return img


def make_turret(size: int, mode: str):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    m = 4
    img = paste(img, glow_layer(size, (c, c), rgba("ffd45e"), size * 0.3, 120))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((m + 8, size - m - 14, size - m - 9, size - m - 6), radius=5, fill=rgba("3c4657"), outline=rgba("96a1b4"), width=2)
    d.rounded_rectangle((m + 13, m + 15, size - m - 13, size - m - 17), radius=5, fill=rgba("536072"), outline=rgba("d5dce7"), width=2)
    d.ellipse((c - 10, c - 10, c + 10, c + 10), fill=rgba("ffd45e"), outline=rgba("fff3c6"), width=2)
    d.rectangle((c - 4, m + 7, c + 4, c + 16), fill=rgba("667182"), outline=rgba("d5dce7"), width=1)
    if mode == "mortar":
        d.rounded_rectangle((c - 5, m + 2, c + 5, m + 16), radius=3, fill=rgba("5f6878"), outline=rgba("dce1ea"), width=1)
        d.line((c, m + 1, c, m + 12), fill=rgba("fff4cf"), width=2)
    elif mode == "sanctifier":
        d.rounded_rectangle((c - 4, m + 2, c + 4, m + 20), radius=3, fill=rgba("5f6878"), outline=rgba("dce1ea"), width=1)
        d.line((c, m + 1, c, m + 20), fill=rgba("fff4cf"), width=2)
    elif mode == "radiant":
        d.rounded_rectangle((c - 7, m + 1, c + 7, m + 20), radius=3, fill=rgba("5f6878"), outline=rgba("dce1ea"), width=1)
        d.line((c, m + 1, c, m + 22), fill=rgba("fff4cf"), width=2)
    else:  # aegis
        d.rounded_rectangle((c - 4, m + 5, c + 4, m + 17), radius=3, fill=rgba("5f6878"), outline=rgba("dce1ea"), width=1)
        d.line((c, m + 5, c, m + 15), fill=rgba("fff4cf"), width=2)
        d.polygon([(m + 8, c), (m + 16, c - 5), (m + 16, c + 5)], fill=rgba("667182"))
        d.polygon([(size - m - 8, c), (size - m - 16, c - 5), (size - m - 16, c + 5)], fill=rgba("667182"))
    return img.filter(ImageFilter.GaussianBlur(0.15))


def make_factory_like(size: int, mode: str):
    img = base_machine(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    m = 4
    img = paste(img, glow_layer(size, (c, c + 2), rgba("ffd45e"), size * 0.22, 110))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((m + 8, m + 12, size - m - 8, size - m - 8), radius=5, fill=rgba("44505f"), outline=rgba("c7cfdb"), width=2)
    if mode == "factory":
        d.rectangle((m + 12, m + 17, size - m - 12, size - m - 17), fill=rgba("70512d"), outline=rgba("ffd45e"), width=2)
        d.rectangle((c - 7, m + 5, c + 7, m + 16), fill=rgba("687485"), outline=rgba("dbe2ec"), width=1)
        d.line((c, m + 4, c, m + 15), fill=rgba("fff4cf"), width=2)
    elif mode == "ascender":
        d.polygon([(c, m + 6), (c + 12, m + 18), (c, m + 30), (c - 12, m + 18)], fill=rgba("6f4a24"), outline=rgba("ffd45e"))
        d.rectangle((c - 6, size - m - 18, c + 6, size - m - 8), fill=rgba("687485"), outline=rgba("dbe2ec"), width=1)
        d.line((c, size - m - 19, c, size - m - 9), fill=rgba("fff4cf"), width=2)
    else:  # transcender
        d.polygon([(c, m + 6), (c + 16, m + 22), (c, m + 38), (c - 16, m + 22)], fill=rgba("6f4a24"), outline=rgba("ffd45e"))
        d.rectangle((c - 7, size - m - 20, c + 7, size - m - 8), fill=rgba("687485"), outline=rgba("dbe2ec"), width=1)
        d.line((c, size - m - 21, c, size - m - 9), fill=rgba("fff4cf"), width=2)
    return img


def make_factory_top(size: int, mode: str):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    if mode == "factory":
        d.rectangle((c - 10, c - 4, c + 10, c + 4), fill=rgba("ffd45e"))
        d.rectangle((c - 4, c - 10, c + 4, c + 10), fill=rgba("ffd45e"))
    elif mode == "ascender":
        d.ellipse((c - 9, c - 9, c + 9, c + 9), outline=rgba("ffd45e"), width=2)
        d.line((c - 6, c + 4, c + 6, c - 4), fill=rgba("fff4cf"), width=2)
    else:
        d.ellipse((c - 12, c - 12, c + 12, c + 12), outline=rgba("ffd45e"), width=2)
        d.line((c - 8, c + 6, c + 8, c - 6), fill=rgba("fff4cf"), width=2)
        d.line((c - 8, c - 6, c + 8, c + 6), fill=rgba("fff4cf"), width=2)
    return img


def unit_body(size: int, variant: str):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    m = size // 10
    # outer glow
    img = paste(img, glow_layer(size, (c, c), rgba("ffd45e"), size * 0.18, 90))
    d = ImageDraw.Draw(img)
    if variant == "scout":
        d.polygon([(c, m + 3), (size - m - 9, c), (c, size - m - 3), (m + 9, c)], fill=rgba("465060"), outline=rgba("cbd3df"))
        d.polygon([(c, m + 10), (size - m - 15, c), (c, size - m - 10), (m + 15, c)], fill=rgba("657182"))
        d.ellipse((c - 7, c - 7, c + 7, c + 7), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    elif variant == "guard":
        d.rounded_rectangle((m + 10, m + 8, size - m - 10, size - m - 8), radius=7, fill=rgba("465060"), outline=rgba("cbd3df"), width=2)
        d.rounded_rectangle((m + 16, m + 14, size - m - 16, size - m - 14), radius=5, fill=rgba("657182"), outline=rgba("ffd45e"), width=2)
        d.ellipse((c - 6, c - 6, c + 6, c + 6), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    elif variant == "warden":
        d.polygon([(c, m + 6), (size - m - 14, c), (c, size - m - 6), (m + 14, c)], fill=rgba("414b5b"), outline=rgba("c7cfdb"))
        d.polygon([(c, m + 14), (size - m - 22, c), (c, size - m - 14), (m + 22, c)], fill=rgba("617082"), outline=rgba("ffd45e"))
        d.ellipse((c - 8, c - 8, c + 8, c + 8), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    elif variant == "seraph":
        d.polygon([(c, m + 5), (size - m - 8, c), (c, size - m - 5), (m + 8, c)], fill=rgba("3f495a"), outline=rgba("c7cfdb"))
        d.polygon([(c, m + 12), (size - m - 18, c), (c, size - m - 12), (m + 18, c)], fill=rgba("677686"), outline=rgba("ffd45e"))
        d.ellipse((c - 10, c - 10, c + 10, c + 10), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    else:  # templar
        d.rounded_rectangle((m + 11, m + 9, size - m - 11, size - m - 9), radius=9, fill=rgba("3f495a"), outline=rgba("c7cfdb"), width=2)
        d.rounded_rectangle((m + 18, m + 15, size - m - 18, size - m - 15), radius=6, fill=rgba("677686"), outline=rgba("ffd45e"), width=2)
        d.ellipse((c - 11, c - 11, c + 11, c + 11), fill=rgba("ffd45e"), outline=rgba("fff4cf"), width=2)
    return img.filter(ImageFilter.GaussianBlur(0.15))


def unit_cell(size: int):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    s = max(6, size // 10)
    d.ellipse((c - s, c - s, c + s, c + s), fill=rgba("ffffff"), outline=rgba("dcc6c6"), width=2)
    d.ellipse((c - s + 2, c - s + 2, c + s - 2, c + s - 2), fill=rgba("dcc6c6"))
    return img


def weapon_sprite(theme: str, size: int = 32):
    img = canvas(size)
    d = ImageDraw.Draw(img)
    c = size // 2
    m = 6
    d.rounded_rectangle((m + 2, c - 4, size - m - 2, c + 4), radius=2, fill=rgba("55606f"), outline=rgba("dce2ea"), width=1)
    d.rounded_rectangle((c - 3, m + 2, c + 3, size - m - 2), radius=2, fill=rgba("687282"), outline=rgba("dce2ea"), width=1)
    img = paste(img, glow_layer(size, (c, c), rgba(theme), size * 0.18, 100))
    d = ImageDraw.Draw(img)
    d.ellipse((c - 4, c - 4, c + 4, c + 4), fill=rgba(theme), outline=rgba("fff4cf"), width=1)
    return img.filter(ImageFilter.GaussianBlur(0.1))


def generate():
    # Preserve existing root art; generate only new assets.
    files = {
        "sprites/items/holy-dust.png": make_item_icon("ffd45e"),
        "sprites/liquids/blessed-water.png": make_water_icon(),
        "sprites/blocks/holy-refinery.png": make_refinery(96),
        "sprites/blocks/holy-drill-i.png": make_drill_body(64, 3, "ffd45e"),
        "sprites/blocks/holy-drill-i-rotator.png": make_drill_rotator(64, "ffd45e"),
        "sprites/blocks/holy-drill-i-top.png": make_drill_top(64, "ffd45e"),
        "sprites/blocks/holy-drill-ii.png": make_drill_body(64, 4, "ffde7a"),
        "sprites/blocks/holy-drill-ii-rotator.png": make_drill_rotator(64, "ffde7a"),
        "sprites/blocks/holy-drill-ii-top.png": make_drill_top(64, "ffde7a"),
        "sprites/blocks/holy-drill-iii.png": make_drill_body(96, 5, "ffe08e"),
        "sprites/blocks/holy-drill-iii-rotator.png": make_drill_rotator(96, "ffe08e"),
        "sprites/blocks/holy-drill-iii-top.png": make_drill_top(96, "ffe08e", wide=True),
        "sprites/blocks/holy-bore.png": make_drill_body(96, 5, "86d7ff"),
        "sprites/blocks/holy-bore-rotator.png": make_drill_rotator(96, "86d7ff"),
        "sprites/blocks/holy-bore-top.png": make_drill_top(96, "86d7ff", wide=True),
        "sprites/blocks/holy-quarry.png": make_drill_body(128, 6, "fff0b5"),
        "sprites/blocks/holy-quarry-rotator.png": make_drill_rotator(128, "fff0b5"),
        "sprites/blocks/holy-quarry-top.png": make_drill_top(128, "fff0b5", wide=True),
        "sprites/blocks/dust-reactor.png": make_generator(64, "dust-reactor"),
        "sprites/blocks/dust-reactor-top.png": make_generator_top(64, "dust-reactor"),
        "sprites/blocks/blessed-turbine.png": make_generator(64, "blessed-turbine"),
        "sprites/blocks/blessed-turbine-top.png": make_generator_top(64, "blessed-turbine"),
        "sprites/blocks/holy-panel.png": make_generator(64, "holy-panel"),
        "sprites/blocks/hallowed-mortar.png": make_turret(64, "mortar"),
        "sprites/blocks/sanctifier.png": make_turret(64, "sanctifier"),
        "sprites/blocks/radiant-cannon.png": make_turret(96, "radiant"),
        "sprites/blocks/aegis-array.png": make_turret(64, "aegis"),
        "sprites/blocks/holy-t1-shields.png": make_factory_like(96, "factory"),
        "sprites/blocks/holy-t1-shields-top.png": make_factory_top(96, "factory"),
        "sprites/blocks/holy-ascender.png": make_factory_like(96, "ascender"),
        "sprites/blocks/holy-ascender-top.png": make_factory_top(96, "ascender"),
        "sprites/blocks/holy-transcender.png": make_factory_like(128, "transcender"),
        "sprites/blocks/holy-transcender-top.png": make_factory_top(128, "transcender"),
        "sprites/units/holy-scout.png": unit_body(64, "scout"),
        "sprites/units/holy-scout-cell.png": unit_cell(64),
        "sprites/units/holy-guard.png": unit_body(64, "guard"),
        "sprites/units/holy-guard-cell.png": unit_cell(64),
        "sprites/units/holy-warden.png": unit_body(96, "warden"),
        "sprites/units/holy-warden-cell.png": unit_cell(96),
        "sprites/units/holy-seraph.png": unit_body(128, "seraph"),
        "sprites/units/holy-seraph-cell.png": unit_cell(128),
        "sprites/units/holy-templar.png": unit_body(128, "templar"),
        "sprites/units/holy-templar-cell.png": unit_cell(128),
        "sprites/units/weapons/goddustry-holy-scout-beam.png": weapon_sprite("ffd45e"),
        "sprites/units/weapons/goddustry-holy-guard-caster.png": weapon_sprite("fff0b5"),
        "sprites/units/weapons/goddustry-holy-warden-lance.png": weapon_sprite("86d7ff"),
        "sprites/units/weapons/goddustry-holy-seraph-cannon.png": weapon_sprite("ffd45e"),
        "sprites/units/weapons/goddustry-holy-templar-judge.png": weapon_sprite("fff4cf"),
    }
    for rel, img in files.items():
        save(img, rel)


if __name__ == "__main__":
    generate()
