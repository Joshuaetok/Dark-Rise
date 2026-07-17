#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 64: "What the Factor Carries Home"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-09: Episode 64 leaves Idoro for the first time in
several episodes to follow the Factor back to his own House, a
coastal trading post several days downriver, where he reports to the
Warden, the House's senior keeper of old and dangerous knowledge — a
figure who answers to no one below the House's founding family and
who has spent decades collecting the same kind of history Nkiruka
keeps for the crown. The Warden's reaction reframes everything the
Factor believed he was sent to secure: the House has lost ground to a
patient hunger before too, in an old account eerily similar to what
the presence described to Chibundu, and the Warden recognizes in the
description of a second, older power something the House has hunted,
unsuccessfully, for longer than its trade in oil or ivory. The episode
ends with the Warden making a decision the Factor did not expect and
does not welcome: rather than send more coin or more soldiers, the
House will send a specialist suited to handling powers precisely like
the one Chibundu named. Someone who does not ask kindly.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_64.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Four"},
    {"type": "title_ep_name", "text": "What the Factor Carries Home"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE WARDEN'S OWN ARCHIVE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Factor traveled three full days downriver to reach it, the "
        "water widening and slowing the further he went until the delta "
        "finally opened onto brackish water and the low, unlit "
        "silhouette of the Ijoma Concern's true business, a trading "
        "post built to look like nothing more than warehouses and a "
        "modest dock to anyone passing it by boat, its real purpose "
        "kept several rooms deeper than any tax collector had ever "
        "cared to look. Even the river seemed to arrive at the place "
        "quietly, as though the water itself had learned the House's "
        "preference for going unremarked."
    )},
    {"type": "body", "text": (
        "He delivered his report in a windowless room lit by a single "
        "oil lamp, to a woman the House's younger agents knew only as "
        "the Warden, older than anyone else who still walked the "
        "Concern's halls unassisted, keeper of every account the House "
        "had ever paid dearly to learn and never once dared to "
        "publish. She listened to the whole of his account without "
        "once interrupting, her hands folded, her attention entirely "
        "still in a way that made the Factor, who had faced an ancient "
        "power without flinching only days before, feel unaccountably "
        "young."
    )},
    {"type": "body", "text": (
        "\"He refused the partnership,\" the Factor said, \"in his own "
        "voice, after refusing it first in a voice that was not his "
        "own at all. I have never in twenty years watched a boy that "
        "young survive an old power taking his mouth from him and "
        "still find the composure to speak for himself again minutes "
        "later. Whatever else this House decides about that boundary, "
        "I would ask that it remember what I just described was not "
        "weakness. It was the opposite of weakness, arriving in a body "
        "that has not yet finished its first year of life.\""
    )},
    {"type": "body", "text": (
        "The Warden did not react the way the Factor had expected, "
        "with disappointment or irritation at a failed negotiation. "
        "She reacted instead with the slow, careful stillness of "
        "someone recognizing a shape she had spent a great deal of her "
        "own life searching for. \"Describe the second voice again,\" "
        "she said. \"Every detail. Its register, its patience, the "
        "exact words it used before the boy took his own voice back.\""
    )},
    {"type": "body", "text": (
        "The Factor obliged, and watched something in the Warden's "
        "expression settle into a certainty that unsettled him more "
        "than her earlier stillness had. \"You know what it is,\" he "
        "said. \"Or you believe you do.\""
    )},
    {"type": "body", "text": (
        "\"I know what guarded a ground much like this one, once, "
        "against a House much like ours,\" the Warden said. \"That "
        "House lost every hand it ever sent against it, one patient "
        "refusal at a time, until it abandoned the ground rather than "
        "lose anyone else to it. I have spent thirty years assuming "
        "the account was a warning meant to keep us cautious. I did "
        "not expect, in my own lifetime, to hear a description that "
        "matches it this closely.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A SPECIALIST, NOT A SOLDIER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"Then we should be cautious now, above everything else,\" the "
        "Factor said. \"I came home prepared to argue for patience. I "
        "did not expect to need to argue for it against my own "
        "House.\""
    )},
    {"type": "body", "text": (
        "\"I am not arguing for haste,\" the Warden said. \"I am "
        "arguing that patience and inaction are not the same choice, "
        "and that the House which lost everything to this pattern "
        "before lost it precisely because it mistook one for the "
        "other. We will not send soldiers. Soldiers already failed "
        "once, and the boy proved plainly this morning that he no "
        "longer needs anyone's mercy to survive an ambush.\""
    )},
    {"type": "body", "text": (
        "\"Then what,\" the Factor asked, though some part of him "
        "already suspected he would not like the answer waiting for "
        "him."
    )},
    {"type": "body", "text": (
        "\"A specialist,\" the Warden said. \"Someone trained for "
        "exactly this kind of power, the old, patient, guarding kind "
        "that cannot be bribed, cannot be waited out, and will not be "
        "moved by any offer reasonable enough to move a human heart. We "
        "have one such person still living, retained precisely for an "
        "occasion I hoped, thirty years ago, would never actually "
        "arrive. I will send word tonight.\""
    )},
    {"type": "body", "text": (
        "The Factor felt something colder than the room's own damp "
        "settle over him, understanding in the Warden's careful choice "
        "of words exactly what kind of person the House kept retained "
        "for an occasion like this one. \"You are describing a hunter,\" "
        "he said. \"Not a diplomat. Not a scholar. Something built to "
        "end an old power, not bargain with one.\""
    )},
    {"type": "body", "text": (
        "\"I do not send this person lightly,\" the Warden said, before "
        "he could press further, \"and I have not sent them at all in "
        "longer than you have been alive. Every occasion before this "
        "one where I considered it, I found a gentler answer instead, "
        "and was glad afterward that I had looked harder for one.\""
    )},
    {"type": "body", "text": (
        "\"And this time,\" the Factor asked, \"you did not look "
        "harder.\""
    )},
    {"type": "body", "text": (
        "\"This time I looked exactly as hard as every other time,\" "
        "the Warden said, \"and found nothing gentler waiting for me. A "
        "power that grieves is a power that has already lost something "
        "it could not bear to lose twice. I do not believe patience "
        "reaches something in that condition. I believe only removal "
        "does, cleanly, before it decides on its own that its grief is "
        "reason enough to stop being patient with us instead.\""
    )},
    {"type": "body", "text": (
        "\"I am describing someone who has done this exact work "
        "before, successfully, when patience alone was not enough to "
        "save what needed saving,\" the Warden said. \"I would rather "
        "send that person now, while the danger is still a description "
        "in a report, than wait until it has become the same shape of "
        "loss our old records already warned me about.\""
    )},
    {"type": "body", "text": (
        "\"And if removing it costs the boy something neither of us "
        "intends,\" the Factor asked. \"He stood beside that power "
        "willingly. He defended it, in his own words, more than once "
        "this very morning. I do not believe he will thank this House "
        "for ending something he has clearly chosen to trust, however "
        "imperfectly.\""
    )},
    {"type": "body", "text": (
        "\"Then we will owe him an explanation he does not want, once "
        "it is finished,\" the Warden said. \"I did not say this choice "
        "was without cost. I said it was the only choice our own "
        "history actually supports. The account I keep does not "
        "describe what became of the children a guardian like this one "
        "was protecting, once the guardian itself was gone. I have "
        "spent thirty years hoping I would never need to find out.\""
    )},
    {"type": "body", "text": (
        "The Factor thought of the boy standing calm and unarmed at "
        "the boundary, of the fury in his voice reclaiming his own "
        "answer, of the second power's grief folded so plainly into "
        "everything it had done. \"That boy is not the danger you read "
        "about in your old account,\" he said. \"Whatever this "
        "specialist is trained to end, I do not believe it is him.\""
    )},
    {"type": "body", "text": (
        "\"I did not say it was,\" the Warden said, and something in "
        "her voice, for the first time in the whole conversation, "
        "carried a weight that sounded almost like warning rather than "
        "command. \"I said the power standing beside him is exactly "
        "what this specialist was trained to end. I would advise you, "
        "when you return south, to make very certain the boy is "
        "standing somewhere else entirely when that happens.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: THE LETTER LEAVES THE POST BEFORE THE FACTOR DOES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden did not wait for the Factor's answer before "
        "calling for paper and a sealed pouch, writing quickly in a "
        "hand the Factor had never seen her use for anything else, "
        "short and unadorned, nothing like the careful, patient prose "
        "she used for every other letter the House sent south. She "
        "sealed it herself, without a House mark, and handed it to a "
        "runner already waiting at the door before the Factor had "
        "fully understood how long she must have expected to need him."
    )},
    {"type": "body", "text": (
        "Far to the east, in a quiet compound the Ijoma Concern kept "
        "no official record of owning, the letter would not arrive for "
        "another six days. Its intended reader was already awake when "
        "it did, as though some part of the news had reached ahead of "
        "the ink itself, and read it once, standing, before setting it "
        "down and beginning, without a single wasted motion, to pack "
        "for a journey they had clearly been expecting to make again "
        "someday, for a very long time."
    )},
    {"type": "body", "text": (
        "They packed lightly, the way a person packs who has learned "
        "across many years that most of what a task requires cannot be "
        "carried in a bag at all, and paused only once, at the door, "
        "to look back at a small shelf of ordinary keepsakes kept "
        "otherwise untouched for longer than the Factor had been "
        "alive. They took nothing from it. They only looked, the way a "
        "person looks at a life they have set carefully aside rather "
        "than one they have forgotten, and then closed the door behind "
        "them and began the long walk west."
    )},
    {"type": "body", "text": (
        "None of it, not the Warden's careful account, not the "
        "Factor's quiet unease, not the reader's short pause at an "
        "untouched shelf, reached Idoro before the day's ordinary "
        "business closed over it entirely. A boy trained his will "
        "against a stone in a hollow that had raised him. A mother "
        "mended cloth by a fire that had not yet burned down. A "
        "captain wrote a careful report for a king who would not learn "
        "for many days yet that somewhere far to the east, someone "
        "already answering a summons was walking toward the very "
        "boundary his own soldiers had only just learned to guard."
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
    print("  THE DARK RISE — Episode 64: \"What the Factor Carries Home\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_64.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_64.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
