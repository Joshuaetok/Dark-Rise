#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 78: "The Stranger at the Grinding Stone"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-23: Episode 78 follows directly from Episode 77's
discovery. Zara tests what remains of her senses at the boundary
itself and finds nothing answers her. Elder Maka, drawing on her own
experience carrying a thread since Episode 12, diagnoses the muffling
as a deliberate working rather than exhaustion, and her grandmother's
old stories give the family their first concrete shape for the danger:
a house that blinds a guardian's watchers before it strikes the
guardian itself, a working that requires the attacker to have come
physically close, again and again, undetected. The episode closes on
Mfoniso, disguised as an ordinary traveler, gently extracting Adaugo's
exact routine at the market grinding stone, confirming the family's
fear is already one step behind the danger closing on them.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_78.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Eight"},
    {"type": "title_ep_name", "text": "The Stranger at the Grinding Stone"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: WHAT REMAINED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara left Amara's compound before the household woke, walking "
        "the familiar path toward Idoro's outer fields with her sandals "
        "carried in one hand so the sound of her own feet would not "
        "wake anyone into stopping her. She told herself she only meant "
        "to test what remained of the thing she had spent three seasons "
        "trusting, one careful stride closer to the tree line than she "
        "had walked alone since the night Obi found her three strides "
        "from it a whole season ago."
    )},
    {"type": "body", "text": (
        "She stopped where the fields gave way to rougher ground, "
        "closed her eyes, and waited for the old, familiar cold to "
        "answer her the way it always had before Mfoniso's name existed "
        "for any of them. Nothing came. Not the faint prickle that once "
        "warned her of an approaching stranger in the market. Not the "
        "deeper cold that once woke her at the exact instant Kene's bed "
        "went empty. She stood in the gray morning light feeling for a "
        "danger she used to be able to name without trying, and felt "
        "nothing at all, which frightened her considerably more than "
        "any cold ever had."
    )},
    {"type": "body", "text": (
        "\"You should not be out here alone,\" Amara said behind her, "
        "breathless from half running the path once she found Zara's "
        "sleeping mat empty. \"Not now. Not until we understand what "
        "has been done to you.\""
    )},
    {"type": "body", "text": (
        "\"I needed to know for myself,\" Zara said, not turning "
        "around. \"I needed to feel it fail with my own body, rather "
        "than only believe Chibundu's account of what the entity "
        "noticed from somewhere I could not see for myself.\" She "
        "turned then, and her face carried none of the calm she had "
        "offered Adaugo the evening before. \"It failed, Amara. "
        "Whatever I once had, it did not answer me even standing this "
        "close to where danger has always lived.\""
    )},
    {"type": "body", "text": (
        "Amara took her hand and led her back toward the compound "
        "without further argument, already deciding, before she had "
        "even said it aloud, that today would not pass without Elder "
        "Maka's eyes on whatever this actually was."
    )},
    {"type": "body", "text": (
        "They walked in silence most of the way back, Zara's bare "
        "feet finding the same path she had walked barefoot once "
        "before under a very different kind of compulsion, and Amara "
        "found herself watching her friend's face more closely than "
        "she watched the road, cataloguing every small sign of the "
        "fear Zara was working hard not to show. She had learned, "
        "across a whole season of watching people she loved carry "
        "burdens quietly, that the ones who hid their fear best were "
        "usually the ones closest to being overwhelmed by it."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT ELDER MAKA FOUND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka received them in the modest compound she had "
        "slowly begun rebuilding since Adaugo's return, and listened "
        "to the whole account without interrupting, the particular "
        "stillness she now reserved for anything touching the old, "
        "dangerous edges of this family's story settling over her "
        "features."
    )},
    {"type": "body", "text": (
        "\"Give me your hand,\" she said finally, and Zara obeyed, "
        "watching Elder Maka's face rather than her own hand as the "
        "older woman held it loosely, eyes closed, searching for "
        "something she alone among the living women of Idoro had any "
        "practice finding."
    )},
    {"type": "body", "text": (
        "\"This is not exhaustion,\" Elder Maka said after a long "
        "moment, opening her eyes. \"I know exhaustion. I have carried "
        "it myself, quietly, since the night I absorbed Kene's severed "
        "thread into my own body. Exhaustion thins a gift. It does not "
        "smother it whole the way something has smothered yours.\" She "
        "released Zara's hand slowly. \"This feels laid over you, "
        "deliberately, the way a cloth is laid over a fire to choke it "
        "rather than put it out. My grandmother told stories of exactly "
        "this, long before any of us had reason to believe them. Houses "
        "that hunt spirits do not always strike the guardian directly. "
        "Sometimes they blind its watchers first, quietly, so the "
        "guardian never sees the true blow coming until it has already "
        "landed.\""
    )},
    {"type": "body", "text": (
        "\"Can it be undone,\" Amara asked, the same question she had "
        "asked about Kene's spiral only two days earlier, already "
        "dreading an answer shaped the same way."
    )},
    {"type": "body", "text": (
        "\"I do not know,\" Elder Maka admitted. \"I have never "
        "attempted to lift a working I did not lay myself, against a "
        "hand I have never met. What I can tell you is this. My "
        "grandmother's stories always insisted such workings require "
        "nearness, repeated across many nights, not a single distant "
        "gesture. Whoever has done this to you has not merely watched "
        "Idoro from a hillside. She has been close enough, again and "
        "again, to reach you directly, closer than any of Chidebe's "
        "watchers have ever caught her being.\""
    )},
    {"type": "body", "text": (
        "The words settled over the room like a held breath. \"Then "
        "she has already proven she can come as close as she wishes,\" "
        "Zara said quietly, \"and none of us would know until she chose "
        "to let us.\""
    )},
    {"type": "body", "text": (
        "Elder Maka's face did not soften. \"Then we stop waiting for "
        "her to choose when we learn that,\" she said. \"I will teach "
        "you what I know of holding a thread steady even when it "
        "cannot be strengthened, the same patience I have had to learn "
        "holding my own. It will not give you back what she took. It "
        "may keep her from taking more.\""
    )},
    {"type": "body", "text": (
        "Amara sat with the two of them a long while after, saying "
        "little, turning Elder Maka's words over the way she had once "
        "turned over every hard truth this family had been handed. "
        "\"If she has been close enough to reach Zara again and again,\" "
        "she said finally, \"then she has been close enough to see the "
        "rest of us too. I do not want to learn what else she has been "
        "counting only after she chooses to use it.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT THE HILLSIDE REMEMBERED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Word reached Chidebe within the hour, and he doubled the "
        "watch a second time that day, spacing his soldiers along "
        "paths Idoro had never before thought needed guarding. "
        "Osadebe rode out personally to walk the high ground above the "
        "outer fields, the same patient vantage Elder Maka's grandmother "
        "would have called a hunter's rightful seat, and found what he "
        "had gone looking for without truly expecting to find it: old, "
        "careful footprints, already half erased by two days of wind, "
        "leading close enough to the compound to have watched its "
        "evening fire and turning back long before any patrol had ever "
        "passed near enough to notice."
    )},
    {"type": "body", "text": (
        "He crouched over the faint impressions a long while, reading "
        "what little the ground would still tell him. Whoever had "
        "stood here had stood still for a long time, patient enough "
        "not to shift her own weight, careful enough to leave nothing "
        "but the shape of her own feet behind. \"She has been closer "
        "than we ever gave her credit for,\" he told Chidebe that "
        "evening, \"and patient enough that our own watch walked past "
        "her without once looking twice.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE ENTITY MADE OF IT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu carried Elder Maka's diagnosis to the entity that "
        "same afternoon, watching it turn the shape of the danger over "
        "with the same careful attention it once gave the trading "
        "House's every move. A working that requires nearness, "
        "repeated across nights, it said slowly. Then she has walked "
        "past every ward either the presence or I have ever kept "
        "watch over, more than once, and neither of us felt her "
        "coming."
    )},
    {"type": "body", "text": (
        "\"Can you feel her now,\" Chibundu asked. \"Knowing what to "
        "look for.\""
    )},
    {"type": "body", "text": (
        "No, the entity admitted. And that troubles me more than "
        "finding her would. Whatever lets her move this quietly past "
        "two old powers who have spent three centuries learning to "
        "sense exactly this kind of intrusion is not a small gift. It "
        "is a skill built, patiently, against guardians exactly like "
        "us. I do not think we will feel her until she wants to be "
        "felt, the same as Zara did not feel her being taken from, "
        "night after night, until it was already done."
    )},
    {"type": "body", "text": (
        "Chibundu absorbed that with the same steadiness he had "
        "learned to bring to every hard truth this season had handed "
        "him. \"Then we stop relying on feeling her,\" he said, echoing "
        "Elder Maka's own words back without knowing it. \"We watch "
        "what she would actually want. Zara first. Then whoever stands "
        "closest to Zara.\""
    )},
    {"type": "body", "text": (
        "The entity said nothing for a long moment, and Chibundu felt "
        "the particular quality of its silence that meant it had "
        "already reached the same thought and did not want to be the "
        "one to say it aloud first."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: THE GRINDING STONE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "At the edge of the market, unaware of any of it, Adaugo knelt "
        "at the grinding stone she had used every morning of her adult "
        "life, turning millet into flour with the same steady rhythm "
        "that had carried her through every hard season this family "
        "had survived. The morning was ordinary in every way she could "
        "have named: traders calling their prices, children chasing "
        "one another between the stalls, the same unremarkable noise "
        "Idoro had made every market day since long before any of this "
        "began."
    )},
    {"type": "body", "text": (
        "A traveling woman she did not recognize crouched nearby, "
        "admiring the stone with polite, unhurried curiosity, and "
        "asked, gently, whether the healer everyone in the market "
        "seemed worried about was resting somewhere close, or had "
        "already been sent away for her own safety."
    )},
    {"type": "body", "text": (
        "Adaugo, seeing nothing in the question but ordinary village "
        "concern, answered honestly and at some length, the way she "
        "had answered a hundred such questions from a hundred such "
        "travelers before. Zara was resting at Amara's compound, just "
        "past the third bend in the river path, and Adaugo herself "
        "visited most evenings once her own work was finished, usually "
        "a little before the last light."
    )},
    {"type": "body", "text": (
        "The traveling woman thanked her warmly, admired the stone "
        "once more, and asked one final question, almost as an "
        "afterthought, about whether Adaugo ever walked that river "
        "path alone. Adaugo, still seeing nothing to guard against in "
        "a stranger's ordinary curiosity, said that she usually did, "
        "the compound being close enough that no one had ever thought "
        "to worry over it."
    )},
    {"type": "body", "text": (
        "The traveling woman walked on toward the river without haste, "
        "already carrying home more than she had come for. Adaugo "
        "returned to her grinding, humming softly to herself, entirely "
        "unaware that she had just handed a stranger the exact hour, "
        "the exact path, and the exact solitude on which she could "
        "always be found. Behind her, unseen, unhurried, the same "
        "patient hand that had already dulled Zara's every warning had "
        "just finished choosing its next quiet, unguarded door."
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
                    first_line_indent=None, spacing_before=0):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing_attrs = {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    }
    if spacing_before:
        spacing_attrs[f"{{{NS_WORD}}}before"] = str(spacing_before)
    spacing = make_element("spacing", spacing_attrs)
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


def make_body_paragraph(text, spacing_after=60, spacing_line=360,
                        spacing_before=0):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360,
                           spacing_before=spacing_before)


def make_system_paragraph(text, spacing_after=120, spacing_line=360,
                          spacing_before=0):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0,
                           spacing_before=spacing_before)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

# Vertical space (twips) inserted before the first paragraph of a new scene.
# 480 twips = 24pt: the page shows a clear scene break, but no empty
# paragraph exists for the TTS engine to turn into dead air.
SCENE_BREAK_SPACE = 480

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    pending_scene_break = False

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

        if typ == "scene_break":
            pending_scene_break = True
            continue

        before = SCENE_BREAK_SPACE if pending_scene_break else 0

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
            para = make_body_paragraph(text, spacing_before=before)
            pending_scene_break = False
        elif typ == "system":
            para = make_system_paragraph(text, spacing_before=before)
            pending_scene_break = False
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

# --- LINT (TTS pacing, CLAUDE.md Section 3.10) ---

def lint_content():
    """Check narration text for TTS pacing violations."""
    problems = []
    for i, item in enumerate(EPISODE_CONTENT):
        if item["type"] not in ("body", "system"):
            continue
        text = item["text"]
        if "\u2014" in text or "\u2013" in text:
            problems.append(f"  item {i}: contains a dash: {text[:60]}")
        if "  " in text:
            problems.append(f"  item {i}: double space: {text[:60]}")
        if re.search(r"\w-\w", text):
            problems.append(f"  item {i}: hyphenated word: {text[:60]}")
    return problems


def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 78: \"The Stranger at the Grinding Stone\"")
    print("  Build Script")
    print("=" * 60)
    print()

    problems = lint_content()
    if problems:
        print("  LINT PROBLEMS:")
        for p in problems:
            print(p)
        print()
    else:
        print("  Lint clean: no dashes, double spaces, or hyphenated words")

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_78.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_78.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
