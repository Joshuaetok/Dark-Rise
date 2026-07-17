#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 11: "The Mark"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-18: Episode 11 shows the human cost of Episode 10's public
argument. Elder Maka's two watchers take up their post outside Amara's
compound, and Idoro begins treating Amara's household the way it once
treated the osu, not through any formal decree but through a hundred small
withdrawals: a neighbor who no longer stops to talk, a trade quietly
refused, a distance kept without ever being named. Obi feels the same
distance close around him in the market. In Oso, the entity registers the
village's fracturing as fuel and continues shaping the vessel undisturbed.
The episode closes on Zara, whose skill as a midwife has served Idoro for
thirty years, turned away for the first time in her life by a laboring
mother's family afraid of what her hands might carry, and the entity
noting with interest how isolation makes a door easier to open.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_11.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eleven"},
    {"type": "title_ep_name", "text": "The Mark"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE DISTANCE IDORO KEPT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The two watchers arrived at dawn exactly as Elder Maka had "
        "promised, a pair of quiet young men Amara barely knew by name, "
        "and took up a post beneath the mango tree at the edge of the "
        "compound as though they had always belonged there."
    )},
    {"type": "body", "text": (
        "They did not speak to her. They did not need to. Their "
        "presence alone was a sentence passed every morning without a "
        "single word required to renew it, and Amara found herself "
        "arranging her whole day around the fact of being seen, the way "
        "a woman arranges her steps around a snake she has spotted but "
        "cannot be certain has moved on."
    )},
    {"type": "body", "text": (
        "By evening they had built themselves a small fire at the "
        "compound's edge, close enough to see the doorway, far enough "
        "to claim they were only keeping their own watch and not "
        "intruding on hers, and Amara understood that this fiction was "
        "the entire courtesy Elder Maka had left her. She could pretend "
        "to be an ordinary woman going about an ordinary evening, and "
        "two men would sit within earshot of every word she spoke to "
        "confirm whether the pretending was true."
    )},
    {"type": "body", "text": (
        "It was not the watchers who taught her what had truly changed, "
        "though. It was the well."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She went for water at the hour she always went, and found the "
        "usual cluster of women already gathered there with their "
        "gourds and their morning talk, and watched the talk falter the "
        "moment they saw her coming. Not silence exactly. Something "
        "smaller and more careful than silence, a rearrangement of "
        "bodies, a shifting of who stood beside whom, so that by the "
        "time Amara reached the water's edge a full arm's length of "
        "empty ground had opened around her without anyone appearing to "
        "have moved for that purpose at all."
    )},
    {"type": "body", "text": (
        "No one said an unkind word. No one needed to. Amara filled her "
        "gourd in a silence she recognized from somewhere older than "
        "this morning, the particular silence Idoro kept around anyone "
        "it had quietly decided to hold at arm's length, the same "
        "silence, she understood now with a coldness that had nothing to "
        "do with the water, that must have surrounded every marked child "
        "and marked mother the old law had ever touched."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi came home from the market at midday with his basket still "
        "half full of fish he had not sold, his jaw set in the way it "
        "had been set since the confrontation in their own compound."
    )},
    {"type": "body", "text": (
        "\"They buy from every stall around mine,\" he said, before "
        "Amara had even asked. \"They stand close enough to see the "
        "catch is good. And then they walk to the next stall instead.\""
    )},
    {"type": "body", "text": (
        "\"No one has said why,\" Amara said. It was not a question."
    )},
    {"type": "body", "text": (
        "\"No one has to say why,\" Obi said. \"I stood beside you in "
        "front of the whole village and told them what I believed. I "
        "did not think it would cost this much this quickly.\""
    )},
    {"type": "body", "text": (
        "He set the basket down harder than he needed to, and for a "
        "moment neither of them spoke, the unsold fish sitting between "
        "them like a small, ordinary proof of a much larger thing "
        "neither wanted to name aloud in their own home."
    )},
    {"type": "body", "text": (
        "\"Do you regret it,\" Amara asked finally."
    )},
    {"type": "body", "text": (
        "\"No,\" Obi said, and the certainty in it was the one warm "
        "thing in an otherwise cold day. \"I regret that it costs "
        "anything at all to say a true thing about my own son. That is "
        "not the same as regretting saying it.\""
    )},
    {"type": "body", "text": (
        "That night, Amara sat beside Kene's basket long after the "
        "compound had gone quiet, listening to the low murmur of the "
        "watchers' voices drifting in from their fire, and found "
        "herself thinking, unwillingly, of every story she had ever "
        "heard about children born strange in other villages, children "
        "whose mothers had been made to carry the same slow, wordless "
        "distance she had felt at the well that morning. She had never "
        "once, before this week, wondered what became of those mothers "
        "after the story ended. She wondered now."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT FED ON THE DISTANCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity tasted the shape Idoro's "
        "fear had taken and found it richer than the sharper, more "
        "concentrated dread the cleansing rite had produced, though "
        "slower to arrive and slower still to fade."
    )},
    {"type": "body", "text": (
        "Concentrated fear burned fast and left ash. This fear, thin "
        "and constant, spread through every small refusal and averted "
        "glance in Idoro, was a coal instead of a flame, banked and "
        "patient, feeding the entity in a steady trickle it did not "
        "need to work for at all. It had not lifted a single thread to "
        "produce this feast. The village was doing that labor entirely "
        "on its own, out of nothing more than the ordinary human "
        "instinct to step back from whatever frightened it."
    )},
    {"type": "body", "text": (
        "It had no interest in comforting anyone caught in that fear, "
        "and no interest either in stoking it faster than the village "
        "could produce it on its own. Haste was a young power's mistake. "
        "The entity had watched entire generations of Idoro's ancestors "
        "live and fear and die without once suspecting how carefully "
        "something beneath their forest had learned to let them do the "
        "work of their own undoing."
    )},
    {"type": "body", "text": (
        "The entity turned the greater share of its attention to the "
        "vessel while the village fed it without needing to be asked."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the boy who had once been eight days old and "
        "was now, by every measure but the calendar, well past his "
        "first year, sat upright unsupported for the length of an "
        "entire feeding, his eyes tracking the slow drift of light "
        "through the canopy above with an attention no true infant his "
        "apparent age should have possessed."
    )},
    {"type": "body", "text": (
        "The entity had begun teaching him shapes lately, simple ones, "
        "the outline of a hand, the outline of a door, patterns laid "
        "directly into the small mind the way a river lays a course "
        "into soft ground, patient and permanent. The boy had no words "
        "yet for what he was learning. He would not need words for a "
        "long while. He only needed to recognize the shapes when the "
        "day came that recognizing them mattered."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Beneath the iroko roots, the cold voice took its count."
    )},
    {"type": "system", "text": "Ambient fear yield: sustained, low effort. Vessel: early pattern recognition underway, no active intervention required."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ZARA LOST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara had delivered children in Idoro for thirty years, had "
        "caught more of the village in her own two hands than any "
        "living person could name without stopping to count, and she "
        "had never once, in all that time, been turned away from a "
        "birth."
    )},
    {"type": "body", "text": (
        "She was turned away that afternoon."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "A young mother two compounds over had gone into labor early, "
        "and Zara arrived with her bag of leaves and her practiced hands "
        "exactly as she had a hundred times before, and found the "
        "doorway blocked by the laboring woman's mother in law, a "
        "heavyset woman named for her sharp tongue long before any of "
        "this began."
    )},
    {"type": "body", "text": (
        "\"We have sent for the woman from the next village instead,\" "
        "the mother in law said, not quite meeting Zara's eyes. \"No "
        "offense meant. Only, with everything that has been said about "
        "you, we cannot risk it. Not tonight. Not with a first child.\""
    )},
    {"type": "body", "text": (
        "\"I have delivered half this village,\" Zara said, more "
        "startled than angry, the words coming out smaller than she "
        "intended them to. \"Nothing has changed in my hands.\""
    )},
    {"type": "body", "text": (
        "\"Something walked you to the edge of Oso in your sleep,\" the "
        "woman said. \"Forgive me if I do not want those same hands "
        "catching my grandchild tonight.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The door closed, gently enough, and Zara stood alone in the "
        "gathering dusk with her bag of leaves still hanging useless "
        "from her shoulder, listening to the laboring woman's first cry "
        "of pain carry out through walls she was no longer welcome "
        "behind."
    )},
    {"type": "body", "text": (
        "She walked home slowly, and no one stopped her on the way to "
        "offer comfort, because comfort would have meant standing close "
        "enough to be seen standing close, and Idoro had already decided "
        "tonight, without a single formal word spoken over it, exactly "
        "how close it was willing to stand to a woman who had once "
        "walked barefoot toward the forbidden bush."
    )},
    {"type": "body", "text": (
        "She did not go to her own hut. She found herself, instead, "
        "walking the familiar path to Amara's compound, past the "
        "watchers' small fire, past their carefully incurious faces, and "
        "when Amara opened the door and saw her standing there with her "
        "bag of leaves still slung uselessly over one shoulder, neither "
        "woman said anything for a long moment. There was nothing "
        "strange left to say between two people the village had already "
        "agreed to hold at the same distance."
    )},
    {"type": "body", "text": (
        "\"Sit,\" Amara said finally, and moved aside to let her in, and "
        "for one evening at least, Zara was not turned away from a "
        "single door in Idoro."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity felt the particular, sudden "
        "hollowness open in the midwife's thread, a loneliness sharper "
        "than anything it had tasted from her before, and understood, "
        "with the same flat attention it gave every useful thing, "
        "exactly what an isolated door was worth compared to one still "
        "surrounded by people willing to notice when it moved."
    )},
    {"type": "body", "text": (
        "It had felt this loneliness gather in the dibia too, once, in "
        "the earliest days after his apprentices fled, before it had "
        "even begun to speak through him. Isolation was not a "
        "coincidence attached to its doors. It was closer to a "
        "condition the entity had learned, patiently, to recognize and "
        "wait for, the way a farmer waits for ground to soften before "
        "he plants anything in it."
    )},
    {"type": "body", "text": (
        "A woman with no one left to wake her would sleep a great deal "
        "more soundly. The entity had all the patience in the world. It "
        "had just been handed, for free, one more reason not to need "
        "it much longer. That the mother of its own vessel had chosen, "
        "that same night, to be the one door Idoro had not yet managed "
        "to close, was a detail the entity noted and set aside, unsure "
        "yet whether it would matter, certain only that nothing in this "
        "village happened anymore without eventually mattering to "
        "something."
    )},

    {"type": "scene_break", "text": ""},
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
    print("  THE DARK RISE — Episode 11: \"The Mark\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_11.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_11.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
