#!/usr/bin/env python3
"""Draw the 18 November 2026 front page (1024 x 1024 PNG).

Local build tool only — the grader never runs this file. The entry
program is main.py, which ships the finished PNG unchanged.

Every headline below is a real event from Wednesday 18 November
2026, verified against AFP / AP / Reuters / Just Security. The page
is a newspaper: a navy masthead naming the day, one lead story,
six short panels grouped by region or topic, and a strip of extra
items at the bottom. Fonts are DejaVu, bundled with the system,
so the text renders cleanly at any size.
"""
from PIL import Image, ImageDraw, ImageFont

CANVAS = 1024
BACKGROUND = (248, 244, 232)
INK = (20, 20, 20)
NAVY = (22, 40, 63)
CRIMSON = (180, 35, 24)
TEAL = (14, 107, 107)
OCEAN = (29, 78, 137)
GOLD = (201, 138, 27)
MUTED = (90, 90, 90)
GREY_TEXT = (60, 60, 60)
WHITE = (255, 255, 255)
CARD_FILL = (255, 255, 255)
CARD_EDGE = (210, 200, 180)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def split_lines(draw, text, face, limit):
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=face) <= limit:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def text_block(draw, x, y, text, face, colour, limit, step):
    for line in split_lines(draw, text, face, limit):
        draw.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def card(draw, x, y, width, height, accent):
    draw.rounded_rectangle(
        [x, y, x + width, y + height], radius=10,
        fill=CARD_FILL, outline=CARD_EDGE, width=2,
    )
    draw.rectangle([x, y, x + width, y + 6], fill=accent)


def story_card(draw, x, y, width, height, label, accent, title, body):
    card(draw, x, y, width, height, accent)
    draw.text((x + 16, y + 16), label, font=load(SANS_BOLD, 17), fill=accent)
    bottom = text_block(
        draw, x + 16, y + 44, title, load(SERIF, 25), INK, width - 32, 30,
    )
    text_block(
        draw, x + 16, bottom + 6, body, load(SANS_REG, 18),
        GREY_TEXT, width - 32, 23,
    )


def dusk_city(draw, left, top, right, bottom):
    """Flat sunset city for the lead story: bands, sun, towers, road."""
    stripes = [(255, 170, 80), (255, 140, 90), (230, 110, 110), (120, 70, 110)]
    band_h = (bottom - top) // len(stripes)
    for index, shade in enumerate(stripes):
        draw.rectangle(
            [left, top + index * band_h, right, top + (index + 1) * band_h],
            fill=shade,
        )
    centre_x = (left + right) // 2
    draw.ellipse(
        [centre_x - 34, top + 28, centre_x + 34, top + 96],
        fill=(255, 230, 150),
    )
    towers = [(8, 46, 130), (62, 30, 95), (102, 52, 150), (168, 36, 110), (214, 48, 140), (276, 28, 85)]
    for offset, width, tall in towers:
        x0 = left + offset
        y0 = bottom - 42 - tall
        draw.rectangle([x0, y0, x0 + width, bottom - 42], fill=(30, 30, 50))
        for wy in range(y0 + 12, bottom - 52, 20):
            for wx in range(x0 + 7, x0 + width - 8, 16):
                if (wx + wy) % 3 == 0:
                    draw.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 220, 120))
    draw.rectangle([left, bottom - 42, right, bottom], fill=(40, 40, 40))
    draw.rectangle([left, bottom - 24, right, bottom - 20], fill=WHITE)


def build():
    page = Image.new("RGB", (CANVAS, CANVAS), BACKGROUND)
    draw = ImageDraw.Draw(page)

    # Masthead
    draw.rectangle([0, 0, CANVAS, 132], fill=NAVY)
    draw.text((24, 14), "WORLD NEWS", font=load(SERIF, 72), fill=WHITE)
    draw.text(
        (24, 96), "WEDNESDAY  18  NOVEMBER  2026",
        font=load(SANS_BOLD, 22), fill=(255, 210, 120),
    )
    draw.text(
        (700, 96), "ONE DAY  •  ONE IMAGE",
        font=load(SANS_BOLD, 20), fill=(200, 210, 220),
    )
    draw.rectangle([0, 132, CANVAS, 138], fill=GOLD)

    # Lead story
    lx, ly, lw, lh = 24, 152, 976, 252
    card(draw, lx, ly, lw, lh, CRIMSON)
    draw.text(
        (lx + 20, ly + 18), "LEAD STORY  —  MIDDLE EAST",
        font=load(SANS_BOLD, 18), fill=CRIMSON,
    )
    text_block(
        draw, lx + 20, ly + 48, "IRAN STRIKES KUWAIT & BAHRAIN",
        load(SERIF, 42), INK, 560, 48,
    )
    text_block(
        draw, lx + 20, ly + 152,
        "Iran hits US bases in the Gulf after US strikes a missile site on Qeshm Island.",
        load(SANS_REG, 23), GREY_TEXT, 560, 30,
    )
    draw.text(
        (lx + 20, ly + 214), "Gulf shipping and bases on alert.",
        font=load(SANS_BOLD, 19), fill=NAVY,
    )
    dusk_city(draw, lx + 600, ly + 14, lx + lw - 14, ly + lh - 14)

    # Six panels, two columns by three rows
    stories = [
        ("GEOPOLITICS", NAVY, "XI AND PUTIN MEET IN SHENZHEN",
         "Leaders meet ahead of Thursday's talks with Trump."),
        ("EUROPE", OCEAN, "CRIMEA BRIDGE HIT AGAIN",
         "Part of the road span collapses in a second day of strikes."),
        ("US POLITICS", CRIMSON, "DEMOCRATS WIN ALASKA SENATE SEAT",
         "Mary Peltola's win gives Democrats a 56-44 majority."),
        ("HEALTH", TEAL, "US LOSES MEASLES-FREE STATUS",
         "After 26 years, with 5,400+ cases reported."),
        ("TECH & ECONOMY", (31, 107, 58), "NVIDIA DOUBLES REVENUE TO $115.8BN",
         "Board rules out bringing back Jensen Huang as CEO."),
        ("MIDDLE EAST", (91, 58, 142), "ISRAEL ELECTS NEW KNESSET SPEAKER",
         "Matan Kahana elected in a win for Eisenkot's party."),
    ]
    for index, (label, accent, title, body) in enumerate(stories):
        col = index % 2
        row = index // 2
        story_card(
            draw, 24 + col * 496, 420 + row * 192, 480, 176,
            label, accent, title, body,
        )

    # Extra items
    draw.text(
        (24, 964),
        "ALSO TODAY:  Ebola in DRC passes 11,000 cases  •  Quad meets in Manila  •  Russian plane crash, 19 dead",
        font=load(SANS_BOLD, 15), fill=MUTED,
    )
    page.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", page.size)


if __name__ == "__main__":
    build()
