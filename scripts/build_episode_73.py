#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 73: "The Captain Returns"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-18: Episode 73 brings Osadebe home from his full
moon in Udo, spent answering the same careful questions again and
again for a council still unable to agree on what a second old power
actually requires of the crown. He returns to find the danger he
spent a month describing in the abstract has already arrived in the
flesh, come and gone, in the time it took Udo to keep deliberating.
Chidebe and Amara walk him through everything he missed. Osadebe,
weighing a month of careful crown caution against a single night that
nearly cost a family everything, is left with the uncomfortable
question of what his own service to the throne is actually worth if
the throne moves this much slower than the danger it employs him to
watch.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_73.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Three"},
    {"type": "title_ep_name", "text": "The Captain Returns"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A MOON OF CAREFUL QUESTIONS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe rode the last stretch of the river road alone, "
        "having sent his escort ahead days before, and felt Idoro "
        "settle back into view exactly as he had left it, fields "
        "worked, market open, boundary quiet, and understood, even "
        "before Chidebe reached him at the edge of the compound, that "
        "something in the quiet did not sit the way it should."
    )},
    {"type": "body", "text": (
        "\"You have the look of a man who spent a full moon answering "
        "the same three questions in different order,\" Chidebe said, "
        "by way of greeting, and Osadebe managed something close to a "
        "tired laugh."
    )},
    {"type": "body", "text": (
        "\"Nkiruka asked me to describe the presence's voice register "
        "four separate times,\" he said. \"Eze Amadi wanted to know, "
        "twice, whether the entity's stillness felt more like patience "
        "or more like restraint, as though the two were easily told "
        "apart from across a boundary in the dark. I have never spent "
        "so long being thorough about so little forward motion in "
        "twelve years of crown service.\""
    )},
    {"type": "body", "text": (
        "\"Then you are about to feel considerably worse,\" Chidebe "
        "said, \"because the danger you spent a moon describing in the "
        "abstract arrived here in the flesh twelve days ago, and left "
        "again before Udo had finished agreeing on what to call it.\""
    )},
    {"type": "body", "text": (
        "Osadebe felt the ordinary fatigue of the road drop away from "
        "him all at once, replaced by a colder, more immediate "
        "attention. \"Say that again, plainly,\" he said. \"Not the "
        "shape of it. Whether everyone in this village is still "
        "breathing.\""
    )},
    {"type": "body", "text": (
        "\"Everyone is still breathing,\" Chidebe said. \"That is the "
        "only mercy in the whole account, and it is not a mercy either "
        "of us can take credit for arranging. Come. You will want to "
        "hear the rest of it sitting down, and you will want to hear "
        "it from more than one voice before you decide what any of it "
        "actually means.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT TWELVE DAYS HAD COST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe walked him through all of it without softening any "
        "part for the sake of easing him back into Idoro gently: "
        "Mfoniso's two days on the tree line, her walk through the "
        "market, Zara's third and closest sense of her, the charm that "
        "drew Kene from his own bed, and the presence reaching further "
        "than it had ever reached to save him. Osadebe listened in a "
        "silence that deepened with every new detail, the particular "
        "stillness of a man recalculating everything he had spent a "
        "month explaining to people who had never stood where he had "
        "stood."
    )},
    {"type": "body", "text": (
        "\"I told the king's own council, in careful, measured "
        "language, that this danger required patience and thorough "
        "understanding before any action,\" he said finally. \"I stand "
        "here now being told that same danger walked unrecognized "
        "through this market and nearly took a child while I was "
        "three hundred miles away providing that thorough "
        "understanding to people who have never once had to run "
        "barefoot toward a stream in the dark.\""
    )},
    {"type": "body", "text": (
        "Amara, joining them at the compound gate, did not soften the "
        "account either. \"We survived it,\" she told him plainly. \"I "
        "do not say that to comfort you. I say it because it is the "
        "only fact in this whole story that has not yet cost us "
        "everything, and I have learned this season not to spend "
        "comfort on facts that are not true yet.\""
    )},
    {"type": "body", "text": (
        "She called Kene over from where he was playing near the "
        "doorway, unable to stop herself wanting Osadebe to see with "
        "his own eyes the ordinary, whole child every careful word in "
        "her account was actually about. Kene, who did not remember "
        "Osadebe at all from the captain's earlier posting, greeted "
        "him with the unguarded curiosity of any small boy meeting a "
        "stranger in traveling clothes, entirely unaware of how "
        "closely a room full of adults had just been discussing the "
        "night that nearly took him. Osadebe knelt to greet him "
        "properly, and felt something in his own chest tighten at how "
        "small the whole abstract danger suddenly became, standing "
        "close enough to see it wearing an actual child's face."
    )},
    {"type": "body", "text": (
        "Osadebe absorbed that, and something in his careful, "
        "practiced composure finally cracked open into plain, "
        "unguarded anger, rare enough from him that both Amara and "
        "Chidebe fell quiet to let it pass. \"I have spent twelve years "
        "believing the crown's caution existed to protect people like "
        "you from decisions made too quickly and too carelessly,\" he "
        "said. \"I am no longer certain caution this slow is "
        "protecting anyone at all. It only protects the crown from "
        "having decided wrongly, which is a considerably smaller thing "
        "to protect.\""
    )},
    {"type": "body", "text": (
        "Chidebe took no offense at the anger, understanding it was "
        "never truly aimed at him, but offered his own accounting "
        "anyway, unwilling to let Osadebe carry a guilt that belonged "
        "at least partly to the garrison itself. \"My own watch failed "
        "that night,\" he said. \"A soldier's attention pulled by a "
        "sound she planted on purpose. I have spent every day since "
        "asking whether a captain who trained his men better would "
        "have caught it. I do not have a comfortable answer to that "
        "question either. I do not think either of us gets to keep "
        "one much longer, in this work.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A REPORT HE DID NOT WANT TO WRITE AGAIN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "That evening, alone in the hut he had left a moon before, "
        "Osadebe stared at a fresh sheet of paper for a long while "
        "before setting down a single line: a full account follows. "
        "He did not yet have the words for what would need to fill the "
        "space beneath it, only the certain knowledge that whatever he "
        "wrote next would need to travel faster and land harder than "
        "anything he had carried to Udo before."
    )},
    {"type": "body", "text": (
        "Chibundu found him there before the ink had dried further "
        "than that first line, having asked the entity to walk with "
        "him partway to the boundary once word reached Oso that the "
        "captain had finally returned. \"You look like a man who does "
        "not know where to begin,\" he said."
    )},
    {"type": "body", "text": (
        "\"I do not,\" Osadebe admitted. \"I have spent a month "
        "learning exactly how carefully Udo wants its danger "
        "described. I am no longer certain careful description is what "
        "this moment actually calls for.\""
    )},
    {"type": "body", "text": (
        "\"Then tell them plainly,\" Chibundu said, \"the way I have "
        "had to learn to tell the people I love the hardest things "
        "this season has handed me. Not perfectly measured. True, and "
        "as fast as the truth can travel.\" Osadebe looked at the boy "
        "a long moment, and picked the pen back up with something "
        "closer to purpose than he had held all evening."
    )},
    {"type": "body", "text": (
        "Chibundu hesitated at the doorway before leaving him to it, "
        "weighing a promise made to the entity against a debt he felt "
        "he owed a man who had just carried this family's danger to "
        "Udo and back without ever once being given the full truth of "
        "what he carried. \"There is one more thing you should know "
        "before you write a single word,\" he said finally. \"Not for "
        "the village yet. For your own report, so you do not write it "
        "blind.\""
    )},
    {"type": "body", "text": (
        "He told him plainly: the presence's weakened state, the cost "
        "of reaching this far, the fear that the reach itself may have "
        "been heard by something neither old power had ever let itself "
        "name. Osadebe listened without interrupting, and when Chibundu "
        "finished, set his pen down a moment, absorbing one more layer "
        "of danger on top of everything he had already learned that "
        "same evening."
    )},
    {"type": "body", "text": (
        "\"Thank you for trusting me with that,\" he said finally. \"I "
        "will carry it as carefully as everything else you have ever "
        "given me to carry.\" He picked the pen back up, and began, at "
        "last, to write the report he had been avoiding all evening, "
        "certain now that whatever words he chose, they would need to "
        "be truer and faster than any report he had ever sent north "
        "before."
    )},
    {"type": "body", "text": (
        "The entity, sensing the boundary Chibundu had just crossed "
        "without permission, said nothing critical of it when he "
        "returned to Oso, only turned the choice over carefully rather "
        "than reacting to it at once. \"You gave him something I asked "
        "you to hold back,\" it said finally."
    )},
    {"type": "body", "text": (
        "\"I did,\" Chibundu said, without apology. \"I judged that a "
        "man about to write the truth to a throne deserved the whole "
        "of it, even while the rest of the village still waits a few "
        "more days for theirs. I do not think that contradicts what "
        "you asked. I think it simply means the circle of who needs "
        "the truth first was larger than either of us first "
        "accounted for.\""
    )},
    {"type": "body", "text": (
        "The entity considered that a long moment, and found, at the "
        "end of its considering, only agreement waiting for it. \"You "
        "are learning to judge that circle better than I ever have,\" "
        "it said. \"I do not think that is a small thing to have "
        "learned, at your age, in a single difficult season.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with that a while, watching the ordinary dark "
        "settle over Oso the same way it had settled every night this "
        "whole long season, and found himself, for the first time in "
        "days, allowing something close to steadiness rather than mere "
        "endurance. Whatever Udo decided once Osadebe's honest report "
        "finally reached it, at least this time the truth traveling "
        "north would not be missing the pieces that mattered most, "
        "whatever the crown ultimately chose to do with them."
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
    print("  THE DARK RISE — Episode 73: \"The Captain Returns\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_73.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_73.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
