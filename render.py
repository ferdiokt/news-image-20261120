"""Draws entry.png (1024x1024) and SOURCES.md from stories.py. Dev-only: needs Pillow and the URW base35 fonts.

    python3 render.py      # writes entry.png and SOURCES.md next to this file
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from stories import S, DATE, REGIONS, KEY_NUMBERS, TIMELINE, DROPPED

HERE = Path(__file__).parent
FD = "/usr/share/fonts/opentype/urw-base35/"
K = 2  # draw at 2048, downsample to 1024
W = 1024

PAPER, INK, MUTED, RULE = "#F2F4F7", "#111A2B", "#5A6577", "#C9D0DA"
TAG = {"REPORTED": "#2350C8", "CLAIM": "#D98E04", "FORECAST": "#0F8C7A"}
RED = "#CC2B2B"
REGION_COL = {"Europe": "#2350C8", "Middle East": "#C8641E", "Asia": "#B8336A",
              "Africa": "#2F8A3A", "Americas": "#6C45B8", "Global": "#3E4A5C"}

_fc = {}


def F(name, size):
    key = (name, size)
    if key not in _fc:
        _fc[key] = ImageFont.truetype(FD + name + ".otf", int(round(size * K)))
    return _fc[key]


GOTH, NB, NR, SB = "URWGothic-Demi", "NimbusSansNarrow-Bold", "NimbusSansNarrow-Regular", "NimbusSans-Bold"

img = Image.new("RGB", (W * K, W * K), PAPER)
d = ImageDraw.Draw(img)


def P(*v):
    return [x * K for x in v]


def tw(text, font):
    return font.getlength(text) / K


def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x * K, y * K), s, font=font, fill=fill, anchor=anchor)


def wrap(s, font, width, max_lines):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    assert len(lines) <= max_lines and all(tw(l, font) <= width for l in lines), (s, lines)
    return lines


def fit(s, font, width):
    assert tw(s, font) <= width, ("OVER", s, round(tw(s, font)), width)
    return s


def rect(x0, y0, x1, y1, fill=None, outline=None, r=0, w=1):
    d.rounded_rectangle(P(x0, y0, x1, y1), radius=r * K, fill=fill, outline=outline, width=w * K)


def disc(cx, cy, r, fill, label, size=12, fg="white"):
    d.ellipse(P(cx - r, cy - r, cx + r, cy + r), fill=fill)
    text(cx, cy + 0.5, label, F(SB, size), fg, "mm")


def chip(x_right, y, tag, size=10):
    f = F(SB, size)
    wdt = tw(tag, f) + 10
    rect(x_right - wdt, y, x_right, y + size + 7, fill=TAG[tag], r=3)
    text(x_right - wdt / 2, y + (size + 7) / 2 + 0.5, tag, f, "white", "mm")
    return wdt


leads = [s for s in S if s["kind"] == "lead"]
cards = [s for s in S if s["kind"] == "card"]
briefs = [s for s in S if s["kind"] == "brief"]
for i, s in enumerate(leads + cards, 1):
    s["n"] = i
counts = {r: sum(s["region"] == r for s in S) for r in REGIONS}
assert sum(counts.values()) == len(S)

# ---------------- masthead ----------------
rect(20, 16, 98, 98, fill="white", outline=INK, r=6, w=2)
rect(20, 16, 98, 38, fill=RED, r=6)
d.rectangle(P(21, 30, 97, 38), fill=RED)
text(59, 28, "NOV 2026", F(SB, 11.5), "white", "mm")
text(59, 70, "20", F(GOTH, 46), INK, "mm")
text(59, 90, "Friday", F(NB, 12), MUTED, "mm")
text(114, 12, fit(DATE, F(GOTH, 58), 890), F(GOTH, 58))
dek = "Wall Street falls into correction; Russian missiles hit Kyiv, crash in Poland; COP31 runs over"
text(116, 80, fit(dek, F(NB, 19.5), 888), F(NB, 19.5), INK)

# ---------------- count bar ----------------
y = 108
d.line(P(20, y, 1004, y), fill=INK, width=2 * K)
nreg = sum(1 for v in counts.values() if v)
head = f"{len(S)} stories from {nreg} regions"
text(20, y + 7, head, F(SB, 15), INK)
x = 24 + tw(head, F(SB, 15)) + 14
for r in REGIONS:
    if not counts[r]:
        continue
    d.rectangle(P(x, y + 10, x + 11, y + 21), fill=REGION_COL[r])
    lab = f"{r} {counts[r]}"
    text(x + 16, y + 8, lab, F(NB, 15), INK)
    x += 16 + tw(lab, F(NB, 15)) + 14
assert x < 1004 - 180, x
# proportional strip
sx, sw = 1004 - 176, 176
for r in REGIONS:
    seg = sw * counts[r] / len(S)
    d.rectangle(P(sx, y + 10, sx + seg, y + 22), fill=REGION_COL[r])
    sx += seg

# ---------------- leads ----------------
LY, LH, LW, ART = 140, 278, 322, 118
LX = [20, 351, 682]
ART_BG = ["#1C2B4A", "#43506A", "#12514F"]


def art_markets(x, y):
    # stock-exchange facade with a falling arrow
    c = "#AFC0DA"
    d.polygon(P(x + 22, y + 46, x + 112, y + 20, x + 202, y + 46), fill=c)
    d.rectangle(P(x + 26, y + 46, x + 198, y + 54), fill=c)
    for i in range(6):
        cx = x + 38 + i * 29.5
        d.rectangle(P(cx, y + 58, cx + 13, y + 100), fill=c)
    d.rectangle(P(x + 20, y + 102, x + 204, y + 110), fill=c)
    # arrow
    d.line(P(x + 214, y + 18, x + 262, y + 66), fill=RED, width=14 * K)
    d.polygon(P(x + 280, y + 84, x + 238, y + 78, x + 274, y + 42), fill=RED)


def art_war(x, y):
    # river, a broken arch bridge, missile trails; dashed border marker at left
    d.rectangle(P(x, y + 88, x + LW, y + ART), fill="#2E6B8F")
    deck = "#D6DCE6"
    for (a, b) in ((x + 70, x + 160), (x + 196, x + 300)):
        d.rectangle(P(a, y + 70, b, y + 78), fill=deck)
        d.arc(P(a + 4, y + 70, b - 4, y + 126), 180, 360, fill=deck, width=5 * K)
    for px in (x + 74, x + 156, x + 200, x + 296):
        d.rectangle(P(px - 3, y + 74, px + 3, y + 96), fill=deck)
    # explosion at the gap
    cx, cy = x + 178, y + 70
    pts = []
    for i in range(16):
        rr = 22 if i % 2 == 0 else 11
        a = math.pi * 2 * i / 16
        pts += [cx + rr * math.cos(a), cy + rr * math.sin(a)]
    d.polygon(P(*pts), fill="#F29B2E")
    d.ellipse(P(cx - 8, cy - 8, cx + 8, cy + 8), fill="#FFE08A")
    for (sx_, sy_, ex, ey) in ((x + 300, y + 6, x + 236, y + 40), (x + 250, y + 2, x + 196, y + 30)):
        d.line(P(sx_, sy_, ex, ey), fill="#E9EDF3", width=3 * K)
        d.ellipse(P(ex - 4, ey - 4, ex + 4, ey + 4), fill="#E9EDF3")
    for yy in range(8, 84, 12):
        d.line(P(x + 40, y + yy, x + 40, y + yy + 6), fill="#E9EDF3", width=2 * K)
    text(x + 14, y + 56, "PL", F(SB, 12), "#E9EDF3")
    d.line(P(x + 34, y + 8, x + 22, y + 34), fill="#E9EDF3", width=2 * K)
    d.polygon(P(x + 22, y + 30, x + 28, y + 38, x + 22, y + 46, x + 16, y + 38), fill="#F29B2E")
    text(x + 48, y + 56, "UA", F(SB, 12), "#E9EDF3")


def art_climate(x, y):
    # globe and a clock past its deadline
    gx, gy, gr = x + 78, y + 60, 44
    d.ellipse(P(gx - gr, gy - gr, gx + gr, gy + gr), fill="#3E8FC9")
    d.polygon(P(gx - 30, gy - 26, gx - 6, gy - 34, gx + 4, gy - 14, gx - 12, gy + 2, gx - 30, gy - 6), fill="#5DB36A")
    d.polygon(P(gx + 8, gy + 4, gx + 32, gy - 6, gx + 36, gy + 18, gx + 16, gy + 34, gx + 4, gy + 22), fill="#5DB36A")
    cx, cy, cr = x + 226, y + 60, 46
    d.ellipse(P(cx - cr, cy - cr, cx + cr, cy + cr), fill="#F4F6F9")
    d.pieslice(P(cx - cr + 6, cy - cr + 6, cx + cr - 6, cy + cr - 6), -90, -20, fill="#F2B233")
    for i in range(12):
        a = math.pi * 2 * i / 12
        d.line(P(cx + 36 * math.cos(a), cy + 36 * math.sin(a), cx + 41 * math.cos(a), cy + 41 * math.sin(a)),
               fill=INK, width=2 * K)
    a = math.radians(-20)
    d.line(P(cx, cy, cx + 32 * math.cos(a), cy + 32 * math.sin(a)), fill=INK, width=3 * K)
    d.line(P(cx, cy, cx, cy - 24), fill=INK, width=4 * K)
    d.ellipse(P(cx - 4, cy - 4, cx + 4, cy + 4), fill=INK)
    text(x + 300, y + 112, "overtime", F(NB, 14), "#F2B233", "rb")


ARTS = [art_markets, art_war, art_climate]
for i, s in enumerate(leads):
    x = LX[i]
    rect(x, LY, x + LW, LY + LH, fill="white", outline=RULE, r=6)
    rect(x, LY, x + LW, LY + ART, fill=ART_BG[i], r=6)
    d.rectangle(P(x, LY + ART - 8, x + LW, LY + ART), fill=ART_BG[i])
    ARTS[i](x, LY)
    disc(x + 18, LY + 18, 13, "white", str(s["n"]), 14, INK)
    yy = LY + ART + 8
    lab = f'{s["place"]}  /  {s["field"]}'
    text(x + 12, yy, fit(lab, F(SB, 12.5), LW - 100), F(SB, 12.5), REGION_COL[s["region"]])
    chip(x + LW - 10, yy - 2, s["tag"], 10.5)
    yy += 20
    for ln in wrap(s["head"], F(NB, 31.5), LW - 24, 2):
        text(x + 12, yy, ln, F(NB, 31.5))
        yy += 35
    yy += 3
    for ln in wrap(s["fact"], F(NR, 16), LW - 24, 2):
        text(x + 12, yy, ln, F(NR, 16), "#2B3445")
        yy += 18
    assert yy <= LY + LH - 4, (s["head"], yy)

# ---------------- key numbers ----------------
KY, KH = LY + LH + 8, 52
cw = (1004 - 20) / len(KEY_NUMBERS)
rect(20, KY, 1004, KY + KH, fill=INK, r=6)
for i, (v, lab, _) in enumerate(KEY_NUMBERS):
    x = 20 + i * cw
    if i:
        d.line(P(x, KY + 10, x, KY + KH - 10), fill="#3A4558", width=1 * K)
    col = "#FF8A80" if v.startswith("-") else "white"
    v = v.replace("-", "\u2212")
    text(x + cw / 2, KY + 6, fit(v, F(GOTH, 24), cw - 10), F(GOTH, 24), col, "ma")
    text(x + cw / 2, KY + 34, fit(lab, F(NR, 13), cw - 10), F(NR, 13), "#C4CCD8", "ma")

# ---------------- cards ----------------
CY0, CH, CWd, CG = KY + KH + 8, 124, 240, 8


def icon(field, x, y, c):
    s_ = 24
    if field == "Diplomacy":
        d.ellipse(P(x, y + 4, x + 15, y + 19), outline=c, width=3 * K)
        d.ellipse(P(x + 9, y + 4, x + 24, y + 19), outline=c, width=3 * K)
    elif field == "Security":
        d.rectangle(P(x, y + 8, x + s_, y + 14), fill=c)
        d.rectangle(P(x + 1, y + 14, x + 4, y + 24), fill=c)
        d.rectangle(P(x + 20, y + 14, x + 23, y + 24), fill=c)
        for k in range(3):
            d.rectangle(P(x + 4 + k * 7, y + 8, x + 7 + k * 7, y + 14), fill="white")
    elif field == "Weather":
        for k, rr in enumerate((11, 7, 3)):
            d.arc(P(x + 12 - rr, y + 12 - rr, x + 12 + rr, y + 12 + rr), 20 + k * 90, 300 + k * 90, fill=c, width=3 * K)
    elif field == "Justice":
        d.rectangle(P(x + 3, y + 3, x + 15, y + 10), fill=c)
        d.line(P(x + 9, y + 10, x + 20, y + 21), fill=c, width=3 * K)
        d.rectangle(P(x, y + 21, x + 14, y + 24), fill=c)
    elif field == "Disaster":
        d.line(P(x, y + 12, x + 5, y + 12, x + 8, y + 2, x + 12, y + 22, x + 16, y + 6, x + 19, y + 12, x + 24, y + 12),
               fill=c, width=3 * K, joint="curve")
    elif field == "Politics":
        d.rectangle(P(x + 4, y + 12, x + 20, y + 24), fill=c)
        d.rectangle(P(x + 10, y + 2, x + 14, y + 12), fill=c)
        d.ellipse(P(x + 8, y, x + 16, y + 6), fill=c)
    elif field == "Conflict":
        d.polygon(P(x, y + 24, x + 4, y + 14, x + 16, y + 2, x + 22, y + 2, x + 22, y + 8, x + 10, y + 20), fill=c)
    elif field == "Health":
        d.rectangle(P(x + 8, y + 1, x + 16, y + 23), fill=c)
        d.rectangle(P(x + 1, y + 8, x + 23, y + 16), fill=c)
    else:
        raise AssertionError(field)


for i, s in enumerate(cards):
    x = 20 + (i % 4) * (CWd + CG)
    y = CY0 + (i // 4) * (CH + CG)
    rc = REGION_COL[s["region"]]
    rect(x, y, x + CWd, y + CH, fill="white", outline=RULE, r=6)
    d.rectangle(P(x, y + 6, x + 4, y + CH - 6), fill=rc)
    disc(x + 20, y + 17, 11, rc, str(s["n"]), 12)
    cwid = chip(x + CWd - 8, y + 9, s["tag"], 9.5)
    lab = f'{s["place"]} / {s["field"]}'
    text(x + 36, y + 9, fit(lab, F(NB, 13.5), CWd - 50 - cwid), F(NB, 13.5), rc)
    yy = y + 32
    for ln in wrap(s["head"], F(NB, 24.5), CWd - 20, 2):
        text(x + 12, yy, ln, F(NB, 24.5))
        yy += 26
    yy = y + 87
    for ln in wrap(s["fact"], F(NR, 14), CWd - 50, 2):
        text(x + 12, yy, ln, F(NR, 14), "#2B3445")
        yy += 16
    assert yy <= y + CH - 2, (s["head"], yy)
    icon(s["field"], x + CWd - 34, y + CH - 34, rc)

# ---------------- bottom band: map / timeline / briefs ----------------
BY = CY0 + 2 * CH + CG + 10
BH = 1024 - 34 - BY
assert BH >= 200, BH

# map (own sub-canvas so polygons are clipped)
MX, MW = 20, 330
text(MX, BY, "Where it happened", F(SB, 13), INK)
text(MX + 128, BY + 1, "pins match lead and card numbers", F(NR, 12), MUTED)
LON0, LON1, LAT0, LAT1 = -108, 112, -24, 66
mh = int(MW * (LAT1 - LAT0) / (LON1 - LON0))
MY = BY + 20
mimg = Image.new("RGB", (MW * K, mh * K), "#E4ECF4")
md = ImageDraw.Draw(mimg)


def proj(lon, lat):
    return ((lon - LON0) / (LON1 - LON0) * MW, (LAT1 - lat) / (LAT1 - LAT0) * mh)


LAND = [
    [(-168, 66), (-140, 70), (-100, 72), (-80, 72), (-62, 60), (-56, 52), (-66, 44), (-76, 36), (-81, 30), (-80, 25), (-82, 29),
     (-90, 29), (-97, 26), (-97, 21), (-88, 21), (-87, 15), (-83, 9), (-79, 8), (-85, 12), (-92, 15), (-105, 20), (-110, 24),
     (-117, 32), (-124, 40), (-124, 48), (-135, 58), (-150, 60), (-165, 60)],
    [(-55, 60), (-44, 60), (-20, 70), (-20, 80), (-60, 82), (-70, 77), (-55, 70)],
    [(-79, 8), (-72, 12), (-62, 10), (-50, 0), (-35, -5), (-38, -13), (-40, -22), (-48, -26), (-53, -34), (-58, -38), (-65, -41),
     (-68, -50), (-70, -54), (-74, -50), (-73, -40), (-71, -30), (-70, -18), (-76, -14), (-81, -5), (-80, 0), (-77, 4)],
    [(-10, 36), (-9, 43), (-2, 44), (-5, 48), (2, 51), (5, 53), (8, 54), (10, 57), (12, 55), (14, 54), (20, 55), (22, 58), (24, 60),
     (30, 60), (28, 65), (25, 65), (22, 63), (18, 60), (16, 57), (12, 59), (5, 58), (5, 62), (14, 67), (20, 70), (28, 71), (40, 68),
     (60, 70), (80, 73), (110, 76), (140, 73), (180, 66), (163, 60), (150, 59), (135, 55), (141, 53), (141, 48), (130, 43),
     (129, 35), (125, 40), (121, 37), (122, 30), (117, 23), (108, 21), (109, 12), (104, 10), (103, 1), (98, 8), (98, 16),
     (94, 17), (92, 22), (87, 21), (80, 16), (80, 13), (77, 8), (72, 21), (67, 25), (57, 25), (52, 16), (43, 13), (39, 22),
     (35, 28), (36, 36), (30, 37), (26, 40), (23, 40), (22, 37), (20, 40), (16, 38), (12, 41), (9, 44), (3, 42), (0, 39), (-6, 36)],
    [(-17, 21), (-16, 12), (-8, 4), (5, 4), (9, 4), (9, -1), (13, -6), (12, -17), (15, -27), (18, -34), (26, -34), (33, -26),
     (35, -18), (40, -15), (40, -3), (44, 2), (51, 11), (43, 12), (37, 20), (33, 31), (25, 32), (20, 31), (10, 34), (10, 37),
     (-1, 36), (-6, 35), (-10, 30), (-15, 26)],
    [(114, -22), (122, -18), (130, -12), (137, -12), (142, -11), (146, -19), (153, -26), (150, -37), (141, -38), (131, -31), (115, -34)],
    [(130, 31), (135, 34), (140, 35), (142, 40), (141, 45), (139, 38), (132, 34)],
    [(-5, 50), (1, 51), (2, 53), (-2, 56), (-3, 58.5), (-6, 58), (-5, 55), (-3, 54), (-5, 52)],
    [(95, 5), (105, -6), (115, -8), (120, -9), (110, -2), (104, 1)],
]
SEAS = [[(28, 41), (41, 41), (40, 44), (35, 45), (30, 46)], [(47, 37), (54, 37), (53, 42), (50, 46), (47, 44)],
        [(48, 30), (50, 28), (56, 26), (54, 24), (51, 25)]]
for poly in LAND:
    md.polygon([c * K for p in poly for c in proj(*p)], fill="#A7B5C7")
for poly in SEAS:
    md.polygon([c * K for p in poly for c in proj(*p)], fill="#E4ECF4")
img.paste(mimg, (MX * K, MY * K))
d.rectangle(P(MX, MY, MX + MW, MY + mh), outline=RULE, width=1 * K)
NUDGE = {1: (7, -5), 9: (-7, 6), 5: (-8, 3), 2: (5, 3), 4: (-4, 0), 6: (-5, 4), 7: (6, -5), 11: (-8, 0)}
for s in leads + cards:
    px, py = proj(*s["lonlat"])
    dx, dy = NUDGE.get(s["n"], (0, 0))
    cx, cy = MX + px + dx, MY + py + dy
    assert MX + 8 <= cx <= MX + MW - 8 and MY + 8 <= cy <= MY + mh - 8, s["head"]
    d.ellipse(P(cx - 9, cy - 9, cx + 9, cy + 9), fill="white")
    disc(cx, cy, 8, REGION_COL[s["region"]], str(s["n"]), 9.5)
assert MY + mh <= 1024 - 36, MY + mh

# timeline
TX, TWd = 362, 262
text(TX, BY, "Day by the clock", F(SB, 13), INK)
text(TX + 110, BY + 1, "selected local times", F(NR, 12), MUTED)
ty0, step = BY + 34, (BH - 62) / (len(TIMELINE) - 1)
d.line(P(TX + 8, ty0, TX + 8, ty0 + step * (len(TIMELINE) - 1)), fill=RULE, width=3 * K)
for i, (t, _, lab) in enumerate(TIMELINE):
    yy = ty0 + i * step
    d.ellipse(P(TX + 2, yy - 6, TX + 14, yy + 6), fill=INK)
    text(TX + 24, yy - 14, t, F(GOTH, 15), INK)
    text(TX + 24, yy + 3, fit(lab, F(NR, 14), TWd - 30), F(NR, 14), "#2B3445")
    assert yy + 20 <= 1024 - 36, yy

# briefs
BX, BWd = 636, 368
text(BX, BY, "Also on 20 November", F(SB, 13), INK)
by, bstep = BY + 22, (BH - 24) / len(briefs)
assert bstep >= 15.5, bstep
for s in briefs:
    d.ellipse(P(BX, by + 4, BX + 8, by + 12), fill=TAG[s["tag"]])
    pl = s["place"] + ": "
    text(BX + 13, by, pl, F(NB, 13.5), REGION_COL[s["region"]])
    text(BX + 13 + tw(pl, F(NB, 13.5)), by, fit(s["head"], F(NR, 13.5), BWd - 16 - tw(pl, F(NB, 13.5))), F(NR, 13.5))
    by += bstep

# ---------------- legend + footer ----------------
FY = 1024 - 30
d.line(P(20, FY - 4, 1004, FY - 4), fill=INK, width=1 * K)
x = 20
for tag, meaning in (("REPORTED", "by named outlets"), ("CLAIM", "one side, unverified"), ("FORECAST", "poll or schedule")):
    wdt = chip(x + tw(tag, F(SB, 9)) + 10, FY + 1, tag, 9)
    text(x + wdt + 5, FY + 1, meaning, F(NR, 12), MUTED)
    x += wdt + 5 + tw(meaning, F(NR, 12)) + 14
foot1 = "Every story shows a development that happened or was first reported on 20 November 2026."
foot2 = "Sources: AP, Reuters, BBC, Al Jazeera, The Guardian, AFP, CNBC, WHO, UN News, Kyodo, ERR, Andina, Indian Express"
text(1004, FY - 1, fit(foot1, F(NB, 12.5), 1004 - x), F(NB, 12.5), INK, "ra")
text(1004, FY + 13, fit(foot2, F(NR, 11), 1004 - x), F(NR, 11), MUTED, "ra")

out = img.resize((W, W), Image.LANCZOS)
out.save(HERE / "entry.png", optimize=True)

# ---------------- SOURCES.md ----------------
md_ = [f"# Sources: {DATE}", "",
       f"{len(S)} stories from {nreg} regions: " + ", ".join(f"{r} {counts[r]}" for r in REGIONS if counts[r]) + ".",
       "Tags: REPORTED = reported by named outlets; CLAIM = one side's statement, not independently verified; "
       "FORECAST = poll or scheduled event. Times are local as reported.", ""]
for title, group in (("Leads", leads), ("Cards", cards), ("Briefs", briefs)):
    md_ += [f"## {title}", ""]
    for s in group:
        n = f'{s["n"]}. ' if "n" in s else ""
        md_ += [f'### {n}{s["head"]}', "",
                f'- {s["place"]} ({s["region"]}), {s["field"]}; **{s["tag"]}**; time: {s["time"] or "not given"}',
                f'- Fact: {s["fact"]}'] + [f"- {u}" for u in s["urls"]] + [""]
md_ += ["## Key numbers", ""] + [f"- {v} {lab}: {src}" for v, lab, src in KEY_NUMBERS] + [""]
md_ += ["## Timeline (selected local times)", ""] + [f"- {t}: {lab}" for t, _, lab in TIMELINE] + [""]
md_ += ["## Left out: other days (not counted, not in the image)", ""] + \
       [f"- {dt}: {what}. {u}" for dt, what, u in DROPPED] + [""]
(HERE / "SOURCES.md").write_text("\n".join(md_))
print("ok", (HERE / "entry.png").stat().st_size, "bytes;", counts)
