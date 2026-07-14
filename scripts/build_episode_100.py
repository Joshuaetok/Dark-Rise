#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 100: "West of Everything Known"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-15: Episode 100, a milestone episode, sends the search
party out from Idoro at dawn, Zara walking the first stretch of road
with them exactly as promised before turning back. As Osadebe, Emenike,
Ifeanyi, and Okonjo travel steadily further west than any of them have
ever gone, Chibundu keeps pressing the presence for more than its
earlier admission that it recognizes the bearing. Under that pressure,
and as the search draws physically closer to the direction it named,
the presence finally tells Chibundu the fuller truth it has carried
silently for three centuries: the guardian ground it lost to the
hunter who trained Mfoniso's lineage lay along this exact bearing, and
it has never once, in all that time, learned what became of that
ground or the people it once protected there. The search for Ijeoma
and the presence's oldest unhealed grief are, for the first time,
revealed to run along the very same road. The episode closes on the
search party making camp at the edge of country entirely unfamiliar to
all four of them, unaware they may be walking toward two answers at
once.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_100.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred"},
    {"type": "title_ep_name", "text": "West of Everything Known"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE FIRST STRETCH OF ROAD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The search party left Idoro at first light exactly as planned, "
        "Osadebe and Emenike walking ahead with Ifeanyi and Okonjo a "
        "careful pace behind, provisions and Ubani's borrowed maps "
        "distributed evenly enough that no single man's fall would cost "
        "the party everything it carried. Half the compound turned out "
        "to see them off, though none of them made a ceremony of it, as "
        "though naming the moment too plainly might tempt the danger "
        "they were all trying not to speak of aloud."
    )},
    {"type": "body", "text": (
        "Amara held Emenike's face in both hands before he could fall "
        "into step behind Osadebe, the way she had once held her own "
        "children's faces before every danger this family had ever "
        "walked into. \"You are not simply a soldier to this house "
        "anymore,\" she told him. \"You have not been for a long time. "
        "Come home. Both of you, if the road allows it. If it does not "
        "allow both, come home yourself, and let us grieve together "
        "rather than have you grieve alone out there.\" Emenike could "
        "not find words steady enough to answer her properly, and so he "
        "simply held her hands a moment longer before letting them go."
    )},
    {"type": "body", "text": (
        "Elder Maka blessed the party's departure with the same old "
        "rite she had once used to steady Adaugo before her hardest "
        "lessons, small words of protection older than the crown itself, "
        "and pressed a plaited cord into Emenike's palm before he left. "
        "\"It will not stop a blade,\" she told him plainly. \"It will "
        "remind you, when the road grows long, that a whole village is "
        "still holding its breath for you both.\""
    )},
    {"type": "body", "text": (
        "Zara walked the first stretch exactly as she had promised, her "
        "borrowed sense flickering weakly but present at her side the "
        "whole way, reaching out toward the western road every few "
        "hundred paces to test it for anything worth naming a warning. "
        "She found nothing, which she told Emenike honestly rather than "
        "letting him believe her silence meant safety. \"It is not "
        "strong enough yet to promise you the road ahead is clear,\" "
        "she said. \"I can only promise you it is not screaming at me "
        "yet. That is the most honest gift I have left to give you.\""
    )},
    {"type": "body", "text": (
        "She embraced him at the boundary stone that marked the edge of "
        "ground she had ever walked before, holding on a moment longer "
        "than either of them had planned. \"Bring her home,\" she said. "
        "\"And bring yourself home to finish healing properly. Ijeoma "
        "does not need a brother who arrives already broken.\" Emenike "
        "promised what he could honestly promise, and no more, and "
        "watched her turn back toward Idoro until the road bent and "
        "took her from sight."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: COUNTRY NONE OF THEM HAD NAMED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By the third day the party had crossed the furthest edge of "
        "Ubani's finished survey, the careful ink lines of the crown's "
        "map giving way to Osadebe's own rougher sketches, drawn fresh "
        "each evening from whatever the day's walking had taught him. "
        "The land itself changed with the maps, the familiar delta "
        "green thinning into drier, harder country none of the four men "
        "had ever had reason to cross before."
    )},
    {"type": "body", "text": (
        "Ifeanyi noticed it first, the particular quality of quiet that "
        "settled over certain stretches of the road for no reason his "
        "soldier's instincts could name, and mentioned it to Okonjo in "
        "the low, careful voice men use for observations they are not "
        "yet ready to call fears. \"This ground does not feel walked,\" "
        "he said. \"Not abandoned. Walked around. As though something "
        "taught the animals here, a very long time ago, exactly which "
        "paths to avoid.\""
    )},
    {"type": "body", "text": (
        "Okonjo, less inclined toward Ifeanyi's careful unease, found "
        "his own kind of comfort in the sheer size of the country "
        "opening ahead of them, having spent his whole life within a "
        "day's walk of Idoro's market. \"I have never stood anywhere "
        "this far from everything I know,\" he admitted one evening, "
        "not quite ashamed of the wonder in his own voice. \"I did not "
        "expect fear to feel so similar to this.\" Osadebe, overhearing, "
        "allowed himself a rare, tired smile. \"That is because they "
        "very often are the same feeling,\" he said, \"wearing two "
        "different names.\""
    )},
    {"type": "body", "text": (
        "Emenike found the pace easier than he had expected, though his "
        "side still ached by each evening's camp, and spent the long "
        "walking hours turning over, again and again, every detail he "
        "had ever learned of his sister's captivity, searching each one "
        "for anything he might have missed the first ten times he "
        "examined it. Osadebe let him talk when he needed to and let "
        "him walk in silence when he needed that instead, matching his "
        "pace without ever once commenting on it."
    )},
    {"type": "body", "text": (
        "\"You do not have to carry all of it alone, out here,\" "
        "Osadebe told him on the third night, watching Emenike stare "
        "into the fire with the same restless intensity he had carried "
        "since the road began. \"I have chased this House's cruelty for "
        "longer than you have known your own part in it. Let me carry "
        "some of the weight. That is what the rest of us are here for.\" "
        "Emenike accepted the offer the only way he knew how, by finally "
        "sleeping through a full night for the first time since they "
        "had left Idoro."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE PRESENCE FINALLY SAID
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, Chibundu felt the search party's slow progress the way "
        "he had learned to feel Idoro's other distant griefs, a faint "
        "tug along threads he could not fully see, and carried word of "
        "each day's distance to the presence without being asked, "
        "watching for any further sign of the stillness that had "
        "gripped it the night the search was first planned."
    )},
    {"type": "body", "text": (
        "On the third night, as Ifeanyi's uneasy observation about "
        "walked around ground reached him through Osadebe's own report, "
        "Chibundu finally pressed the question he had held back out of "
        "respect for the presence's earlier request. \"They are close "
        "enough now that the ground itself is behaving strangely "
        "around them,\" he said. \"I think you know why. I think you "
        "have known since the night this search was first spoken "
        "aloud. I am asking you to stop protecting me from it.\""
    )},
    {"type": "body", "text": (
        "The presence was quiet long enough that Chibundu began to "
        "wonder whether it would answer at all, and when it finally "
        "spoke, its voice carried none of its usual careful distance, "
        "only a rawness he had heard from it perhaps twice before in "
        "their entire acquaintance. \"That bearing,\" it said, \"west "
        "and slightly south of Oso, was the exact direction of my own "
        "guardian ground, three centuries ago, before the hunter who "
        "trained Mfoniso's line took it from me.\""
    )},
    {"type": "body", "text": (
        "The entity, listening in careful silence through the whole "
        "exchange, spoke at last with something unusually gentle in "
        "its old, transactional voice. \"In three centuries beside you,\" "
        "it told the presence, \"I have never once heard you name what "
        "you lost this plainly. Whatever this search finds, you have "
        "already given Chibundu something today you have never given "
        "either of us before.\" The presence did not answer that "
        "directly, but Chibundu felt, faintly, something in it ease "
        "that had been held tight for longer than he had been alive."
    )},
    {"type": "body", "text": (
        "Chibundu felt the shape of it land fully, three separate "
        "threads of this story, Mfoniso's inherited craft, Ijeoma's "
        "captivity, and the presence's oldest wound, all running toward "
        "the same unmarked ground. \"You believe Ijeoma is being held "
        "on the same land you once protected,\" he said slowly. \"You "
        "believe the House that holds her now stands where your own "
        "guardian ground once stood.\""
    )},
    {"type": "body", "text": (
        "\"I do not know that yet,\" the presence said, \"and I am "
        "afraid of how badly I want it to be true. I have spent three "
        "centuries not knowing what became of the people I protected "
        "there, or the ground itself, because the not knowing was "
        "easier to carry than confirming the worst of what I already "
        "feared. Your search party may be about to answer a question I "
        "stopped asking a very long time ago, and I do not yet know if "
        "I am prepared for whichever answer it brings back.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with that admission a long while, understanding, "
        "for the first time in their whole acquaintance, the full "
        "weight of a grief the presence had carried silently through "
        "every episode of its long, patient watching. \"Then we will "
        "carry the not knowing together, however much longer it "
        "lasts,\" he said. \"You have never once made me face a fear "
        "alone since the day you named me. I do not intend to let you "
        "face this one alone either.\""
    )},
    {"type": "body", "text": (
        "West of Idoro, unaware their small, tired fire sat somewhere "
        "near the edge of a three centuries old grief neither of them "
        "yet knew they were walking toward, Osadebe and Emenike settled "
        "in for the night at the border of country none of the four men "
        "had ever had a name for, the last known ground behind them and "
        "an answer neither the household nor Oso itself could yet "
        "predict waiting somewhere in the dark ahead."
    )},
    {"type": "body", "text": (
        "Emenike banked their small fire before sleep, the plaited cord "
        "Elder Maka had given him still wound twice around his wrist, "
        "and allowed himself, for the first time since the search began, "
        "a single clear thought about what it might actually feel like "
        "to see his sister's face again after two seasons of nothing "
        "but a bracelet and a stranger's cruel proof that she still "
        "lived. He did not let the thought grow any larger than that "
        "before sleep finally took him. It was, for tonight, exactly as "
        "much hope as he trusted himself to carry."
    )},
]

# ─── OOXML HELPERS ────────────────────────────────────────────────────────────

NS_WORD = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"

ET.register_namespace("w", NS_WORD)
ET.register_namespace("mc", NS_MC)


def qn(tag):
    return f"{{{NS_WORD}}}{tag}"


def make_element(tag, attrib=None, text=None):
    el = Element(qn(tag), attrib=attrib or {})
    if text is not None:
        el.text = text
    return el


def make_run(text, bold=False, font_name="Georgia", font_size=24, caps=False):
    r = make_element("r")
    rPr = make_element("rPr")

    rFonts = make_element("rFonts", {
        f"{{{NS_WORD}}}ascii": font_name,
        f"{{{NS_WORD}}}hAnsi": font_name,
        f"{{{NS_WORD}}}cs": font_name,
    })
    rPr.append(rFonts)

    sz = make_element("sz", {f"{{{NS_WORD}}}val": str(font_size)})
    rPr.append(sz)
    szCs = make_element("szCs", {f"{{{NS_WORD}}}val": str(font_size)})
    rPr.append(szCs)

    if bold:
        rPr.append(make_element("b"))
        rPr.append(make_element("bCs"))

    if caps:
        rPr.append(make_element("caps"))

    r.append(rPr)

    t = make_element("t", {"xml:space": "preserve"}, text)
    r.append(t)

    return r


def make_paragraph(runs, spacing_after=120, spacing_line=360, alignment="left",
                    first_line_indent=None):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing = make_element("spacing", {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    })
    pPr.append(spacing)

    if alignment != "left":
        jc = make_element("jc", {f"{{{NS_WORD}}}val": alignment})
        pPr.append(jc)

    if first_line_indent:
        ind = make_element("ind", {f"{{{NS_WORD}}}firstLine": str(first_line_indent)})
        pPr.append(ind)

    p.append(pPr)

    for run in runs:
        p.append(run)

    return p


def make_title_paragraph(text, font_size=32, bold=True, alignment="center",
                          spacing_after=60, spacing_line=360):
    runs = [make_run(text, bold=bold, font_size=font_size)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment=alignment)


def make_body_paragraph(text, spacing_after=60, spacing_line=360):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360)


def make_system_paragraph(text, spacing_after=120, spacing_line=360):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

        if typ == "title_series":
            para = make_title_paragraph(text, font_size=36, bold=True,
                                         alignment="center", spacing_after=0)
        elif typ == "title_subtitle":
            para = make_title_paragraph(text, font_size=28, bold=False,
                                         alignment="center", spacing_after=0)
        elif typ == "title_ep_num":
            para = make_title_paragraph(text, font_size=26, bold=False,
                                         alignment="center", spacing_after=0)
        elif typ == "title_ep_name":
            para = make_title_paragraph(text, font_size=30, bold=True,
                                         alignment="center", spacing_after=0)
        elif typ == "page_break":
            para = make_element("p")
            pPr = make_element("pPr")
            run = make_element("r")
            br = make_element("br", {f"{{{NS_WORD}}}type": "page"})
            run.append(br)
            para.append(pPr)
            para.append(run)
        elif typ == "body":
            para = make_body_paragraph(text)
        elif typ == "system":
            para = make_system_paragraph(text)
        elif typ == "blank":
            para = make_blank_paragraph()
        else:
            continue

        body.append(para)

    sectPr = make_element("sectPr")
    pgSz = make_element("pgSz", {
        f"{{{NS_WORD}}}w": "12240",
        f"{{{NS_WORD}}}h": "15840",
    })
    sectPr.append(pgSz)
    pgMar = make_element("pgMar", {
        f"{{{NS_WORD}}}top": "1440",
        f"{{{NS_WORD}}}right": "1440",
        f"{{{NS_WORD}}}bottom": "1440",
        f"{{{NS_WORD}}}left": "1440",
        f"{{{NS_WORD}}}header": "720",
        f"{{{NS_WORD}}}footer": "720",
        f"{{{NS_WORD}}}gutter": "0",
    })
    sectPr.append(pgMar)
    body.append(sectPr)

    return document


# ─── BUILD .DOCX PACKAGE ─────────────────────────────────────────────────────

def build_docx(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        + tostring(build_document_xml(), encoding="unicode")
    )

    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType='
        '"application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType='
        '"application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
        '</Types>'
    )

    rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type='
        '"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"'
        ' Target="word/document.xml"/>'
        '<Relationship Id="rId2" Type='
        '"http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties"'
        ' Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" Type='
        '"http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties"'
        ' Target="docProps/app.xml"/>'
        '</Relationships>'
    )

    doc_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type='
        '"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"'
        ' Target="styles.xml"/>'
        '</Relationships>'
    )

    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:docDefaults>'
        '<w:rPrDefault><w:rPr>'
        '<w:rFonts w:ascii="Georgia" w:hAnsi="Georgia" w:cs="Georgia"/>'
        '<w:sz w:val="24"/><w:szCs w:val="24"/>'
        '</w:rPr></w:rPrDefault>'
        '</w:docDefaults>'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
        '<w:name w:val="Normal"/>'
        '</w:style>'
        '</w:styles>'
    )

    core_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties '
        'xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/">'
        '<dc:title>The Dark Rise</dc:title>'
        '<dc:creator>The Dark Rise</dc:creator>'
        '</cp:coreProperties>'
    )

    app_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns='
        '"http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
        '<Application>The Dark Rise Build Script</Application>'
        '</Properties>'
    )

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml)
        zf.writestr("_rels/.rels", rels_xml)
        zf.writestr("word/document.xml", doc_xml)
        zf.writestr("word/_rels/document.xml.rels", doc_rels_xml)
        zf.writestr("word/styles.xml", styles_xml)
        zf.writestr("docProps/core.xml", core_xml)
        zf.writestr("docProps/app.xml", app_xml)

    return output_path


# ─── WORD COUNT ───────────────────────────────────────────────────────────────

def count_words():
    total = 0
    for item in EPISODE_CONTENT:
        if item["type"] in ("body", "system"):
            total += len(item["text"].split())
    return total


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 100: \"West of Everything Known\"")
    print("  Build Script")
    print("=" * 60)
    print()

    wc = count_words()
    print(f"  Word count: {wc}")
    if wc < 1550:
        print(f"  WARNING: Under minimum (1,550). Need {1550 - wc} more.")
    elif wc > 2150:
        print(f"  WARNING: Over maximum (2,150). Need to cut {wc - 2150}.")
    else:
        print(f"  Word count in range (1,550-2,150)")
    print(f"  Estimated duration: {wc / 130:.1f}-{wc / 150:.1f} minutes")
    print()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_docx(OUTPUT_FILE)
    print(f"  Created: {OUTPUT_FILE}")
    print()

    try:
        os.makedirs(OUTPUT_DIR_USER, exist_ok=True)
        import shutil
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_100.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_100.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
