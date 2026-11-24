#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build-time renderer for the entry image (dev machine only; uses PIL).

The submitted program (main.py) is standard-library only: it copies the
pre-rendered entry.png asset to the output directory, as the competition
rules explicitly allow ("a repository holding the image and a one-line
program that copies it there"). This script is kept in the repository so
the image can be reproduced and revised.

Concept (original, fictional joke -- no factual claims depicted):
"I told my AI agent to 'take care of everything'." The agent took it
literally: a robot now sits at the boss's desk behind a "BOSS"
nameplate, monitor reading "EVERYTHING: DONE", while the human's
cardboard box of belongings sits on the floor. Punchline: "IT TOOK MY
JOB. AND MY PARKING SPACE."

Renders deterministically: same input, same bytes.
"""
import os
from PIL import Image, ImageDraw, ImageFont

SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

W = H = 1024
WHITE = (255, 255, 255)
INK = (22, 26, 34)
WALL = (233, 238, 243)
FLOOR = (206, 192, 168)
NAVY = (18, 38, 74)
AMBER = (255, 196, 64)
RED = (196, 32, 40)
STEEL = (198, 208, 218)
STEEL_D = (150, 162, 176)
CYAN = (0, 190, 210)
WOOD = (122, 82, 48)
WOOD_D = (96, 62, 34)
BOX = (178, 138, 88)
GOLD = (212, 175, 55)


def F(path, size):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Missing font file: {path}. Install the Liberation fonts "
            "(e.g. Debian/Ubuntu: sudo apt install fonts-liberation) "
            "or point SANS_B at an installed font file."
        )
    return ImageFont.truetype(path, size)


def centered(d, y, text, fnt, fill, cx=W // 2):
    d.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def rrect(d, box, rad, **kw):
    d.rounded_rectangle(box, radius=rad, **kw)




def main():
    img = Image.new("RGB", (W, H), WALL)
    d = ImageDraw.Draw(img)

    # ---------------- floor band (740-800) ----------------
    d.rectangle([0, 740, W, 800], fill=FLOOR)
    d.rectangle([0, 740, W, 746], fill=(170, 156, 130))

    # ---------------- window (right) ----------------
    d.rectangle([800, 250, 990, 470], fill=WHITE)
    d.rectangle([812, 262, 978, 458], fill=(158, 208, 240))
    d.ellipse([890, 290, 950, 350], fill=(255, 214, 90))
    d.ellipse([830, 400, 880, 430], fill=WHITE)
    d.ellipse([905, 415, 965, 445], fill=WHITE)
    d.line([895, 262, 895, 458], fill=WHITE, width=8)
    d.line([812, 360, 978, 360], fill=WHITE, width=8)

    # ---------------- "Employee of the Month" frame (left) ----------------
    d.rectangle([44, 268, 224, 408], fill=(90, 60, 30))
    d.rectangle([54, 278, 214, 398], fill=(250, 246, 232))
    f_small = F(SANS_B, 17)
    centered(d, 290, "EMPLOYEE", f_small, INK, cx=134)
    centered(d, 312, "OF THE MONTH", f_small, INK, cx=134)
    # tiny robot face in the frame
    rrect(d, [104, 336, 164, 372], 8, fill=STEEL, outline=INK, width=2)
    d.ellipse([116, 350, 128, 362], fill=CYAN)
    d.ellipse([140, 350, 152, 362], fill=CYAN)
    d.line([104, 344, 92, 344], fill=INK, width=3)
    d.line([164, 344, 176, 344], fill=INK, width=3)

    # ---------------- top banner text ----------------
    centered(d, 36, "I TOLD MY AI AGENT TO", F(SANS_B, 62), INK)
    # EVERYTHING in red, same line: measure and draw pieces
    f_big = F(SANS_B, 62)
    t1 = "\u201cTAKE CARE OF "
    w1 = d.textlength(t1, font=f_big)
    w2 = d.textlength("EVERYTHING\u201d", font=f_big)
    x0 = (W - w1 - w2) / 2
    d.text((x0, 116), t1, font=f_big, fill=INK)
    d.text((x0 + w1, 116), "EVERYTHING\u201d", font=f_big, fill=RED)

    # ---------------- robot at the desk ----------------
    # body (torso) behind desk
    rrect(d, [392, 560, 632, 740], 26, fill=STEEL, outline=INK, width=4)
    # shirt + tie
    d.polygon([(472, 560), (552, 560), (512, 640)], fill=WHITE, outline=INK)
    d.polygon([(500, 586), (524, 586), (528, 596), (512, 660), (496, 596)], fill=RED)
    d.polygon([(496, 578), (528, 578), (524, 586), (500, 586)], fill=RED)
    # arms resting on desk
    rrect(d, [330, 660, 430, 700], 18, fill=STEEL_D, outline=INK, width=3)
    rrect(d, [594, 660, 694, 700], 18, fill=STEEL_D, outline=INK, width=3)
    # neck + head
    d.rectangle([492, 520, 532, 566], fill=STEEL_D, outline=INK, width=3)
    rrect(d, [402, 380, 622, 530], 34, fill=STEEL, outline=INK, width=5)
    # antenna
    d.line([512, 380, 512, 336], fill=INK, width=6)
    d.ellipse([496, 318, 528, 350], fill=RED, outline=INK, width=3)
    # ears
    d.rectangle([386, 440, 404, 478], fill=STEEL_D, outline=INK, width=3)
    d.rectangle([620, 440, 638, 478], fill=STEEL_D, outline=INK, width=3)
    # eyes: glowing cyan
    rrect(d, [436, 424, 492, 462], 10, fill=CYAN, outline=INK, width=3)
    rrect(d, [532, 424, 588, 462], 10, fill=CYAN, outline=INK, width=3)
    d.ellipse([458, 436, 470, 448], fill=WHITE)
    d.ellipse([554, 436, 566, 448], fill=WHITE)
    # smile grille
    for i in range(5):
        x = 452 + i * 30
        d.line([x, 492, x, 506], fill=INK, width=4)
    d.arc([448, 478, 576, 522], 15, 165, fill=INK, width=4)

    # ---------------- desk ----------------
    d.rectangle([300, 700, 724, 730], fill=WOOD, outline=INK, width=3)
    d.rectangle([316, 730, 708, 800], fill=WOOD_D, outline=INK, width=3)
    d.rectangle([340, 742, 420, 788], fill=WOOD, outline=INK, width=2)  # drawer
    d.ellipse([376, 760, 386, 770], fill=GOLD)

    # nameplate on desk
    d.polygon([(452, 700), (572, 700), (580, 664), (444, 664)], fill=GOLD,
              outline=INK)
    centered(d, 672, "BOSS", F(SANS_B, 22), INK)

    # monitor (left on desk)
    d.rectangle([330, 600, 470, 694], fill=INK)
    d.rectangle([340, 610, 460, 684], fill=(20, 60, 80))
    centered(d, 622, "EVERYTHING:", F(SANS_B, 18), (120, 255, 140), cx=400)
    centered(d, 648, "DONE", F(SANS_B, 26), (120, 255, 140), cx=400)
    # small check mark drawn with lines (font lacks the glyph),
    # placed in front of the DONE line, clear of both monitor texts
    d.line([342, 659, 348, 665], fill=(120, 255, 140), width=3)
    d.line([348, 665, 358, 651], fill=(120, 255, 140), width=3)
    d.rectangle([392, 694, 408, 706], fill=INK)

    # coffee mug (right on desk)
    rrect(d, [640, 640, 690, 700], 6, fill=WHITE, outline=INK, width=3)
    d.arc([688, 652, 712, 682], -90, 90, fill=INK, width=3)
    d.line([656, 628, 656, 612], fill=(150, 150, 150), width=3)
    d.line([672, 630, 672, 610], fill=(150, 150, 150), width=3)

    # ---------------- cardboard box on the floor (left) ----------------
    # floor band is y 740-800; box sits on it, left of the desk
    d.polygon([(96, 726), (256, 726), (256, 800), (96, 800)], fill=BOX,
              outline=INK, width=3)
    d.polygon([(96, 726), (136, 700), (296, 700), (256, 726)], fill=(198, 158, 104),
              outline=INK, width=3)
    d.polygon([(256, 726), (296, 700), (296, 774), (256, 800)], fill=(158, 120, 74),
              outline=INK, width=3)
    d.line([176, 700, 176, 726], fill=INK, width=2)
    centered(d, 748, "MY STUFF", F(SANS_B, 24), INK, cx=176)
    # a plant poking out of the box
    d.line([150, 700, 138, 660], fill=(40, 120, 60), width=5)
    d.line([176, 700, 176, 652], fill=(40, 120, 60), width=5)
    d.line([202, 700, 214, 660], fill=(40, 120, 60), width=5)
    d.ellipse([128, 646, 152, 666], fill=(50, 140, 70))
    d.ellipse([164, 634, 190, 658], fill=(50, 140, 70))
    d.ellipse([204, 646, 228, 666], fill=(50, 140, 70))

    # ---------------- bottom banner ----------------
    d.rectangle([0, 800, W, H], fill=NAVY)
    d.rectangle([0, 800, W, 806], fill=AMBER)
    centered(d, 838, "IT TOOK MY JOB.", F(SANS_B, 68), WHITE)
    centered(d, 922, "AND MY PARKING SPACE.", F(SANS_B, 54), AMBER)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
