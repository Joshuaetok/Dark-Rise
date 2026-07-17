#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 45: "A Different Kind of Watching"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-21: Episode 45 brings the crown's garrison to Idoro,
introducing its commander, a disciplined, by the book officer named
Chidebe who answers to Udo rather than to Osadebe and reads his orders
literally: hold the boundary, and understand what is actually being held
before committing his men to holding it. His first instinct is to inspect
the tree line himself, the exact request that nearly got a foreign
agent's men killed weeks earlier, forcing Osadebe into the position of
warning off the crown's own soldiers rather than a hostile stranger. In
Oso, the entity registers a new flavor of tension at its border —
organized, disciplined, entirely unlike the mercenary aggression it met
with violence in Episode 40 — and chooses restraint for the first time
under real pressure, testing whether the training it has been giving the
vessel can also teach him when not to act. The boy, eager to prove
himself useful after weeks of practice, has to learn the harder half of
the same lesson: that holding back is its own kind of control, and that
these men, unlike the last ones, have done nothing yet to deserve harm.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_45.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Five"},
    {"type": "title_ep_name", "text": "A Different Kind of Watching"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — SOLDIERS WHO ANSWER TO A DIFFERENT VOICE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Captain Chidebe arrived at the head of thirty men in disciplined "
        "column, tents and provisions carried on two mule trains rather "
        "than promised later, and made camp at the field's edge with the "
        "brisk efficiency of a man who had done this exact task in a "
        "dozen other villages and expected this one to unfold no "
        "differently. He greeted Osadebe with correct, careful respect "
        "and made his first request within the hour."
    )},
    {"type": "body", "text": (
        "Idoro watched the tents rise with an unease that had nothing "
        "to do with fear of the men themselves and everything to do "
        "with a village that had spent a lifetime learning what it cost "
        "to be watched closely by anyone, crown or otherwise. Children "
        "who had grown bold enough to stare openly at Amara in the "
        "market now stared instead at the neat rows of canvas at the "
        "field's edge, unsure whether armed strangers camped so near "
        "their homes counted as protection or simply a different shape "
        "of danger wearing the crown's own colors. The older women said "
        "less and watched more, which in Idoro had always been the "
        "surer measure of how deep an unease actually ran."
    )},
    {"type": "body", "text": (
        "Ikwuano's careful orders, read aloud by Osadebe to the "
        "assembled council that same morning exactly as instructed, "
        "helped less than Eze Amadi had hoped. The words themselves "
        "were plain enough. Protection of the boundary, no survey, no "
        "interference with village governance. But Ozoemena, still "
        "recovering his own credibility one small honest act at a time, "
        "voiced the doubt several others were clearly holding back. \"We "
        "have heard careful words from Udo before,\" he said. \"They were "
        "true words, as far as I know. But careful words and careful "
        "soldiers are not always the same promise, and this village has "
        "learned that difference the hard way more than once already.\""
    )},
    {"type": "body", "text": (
        "\"I am to hold this boundary,\" he said, studying the tree "
        "line beyond the last planted stone with the flat, assessing "
        "look of a man measuring ground he intends to defend rather "
        "than merely admire. \"I cannot hold what I have not seen. I "
        "will need to walk the line myself before dusk, Captain, with "
        "your permission or without it. My orders are clear on that "
        "point even if they were vague on most others.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "Osadebe felt the particular, exhausted dread of a man watching "
        "the same mistake approach from a new direction, dressed this "
        "time in the crown's own colors rather than a foreign House's "
        "good cloth. \"The last party that walked toward that line "
        "uninvited left two men unable to stand on their own,\" he "
        "said. \"I am not stopping you from your duty. I am telling you "
        "plainly that duty and survival are not the same thing on this "
        "ground, and that whatever guards it does not distinguish "
        "between a mercenary and a soldier of the crown when it "
        "decides someone has come too close.\""
    )},
    {"type": "body", "text": (
        "Chidebe weighed this with the careful stillness of a man who "
        "took warnings seriously without necessarily believing every "
        "word of them yet. \"I will walk to the last stone, and no "
        "further,\" he said finally. \"I need to see the ground I am "
        "defending, Captain. I do not need to test whatever waits past "
        "it to do my job well. If your warning proves accurate, I will "
        "have learned something valuable at no cost. If it proves "
        "excessive, I will have lost nothing but a single quiet "
        "afternoon.\""
    )},
    {"type": "body", "text": (
        "It was, Osadebe admitted to Amara that evening, the most "
        "reasonable response he could have hoped for from a stranger "
        "hearing a warning this strange for the first time, and he "
        "found himself unexpectedly grateful for a caution that felt "
        "earned rather than simply obedient. \"He is not the agent,\" "
        "Amara said. \"He did not come here wanting anything from that "
        "ground. That alone may be the difference that matters most.\""
    )},
    {"type": "body", "text": (
        "Chidebe walked the boundary that same afternoon exactly as "
        "promised, Osadebe at his side and half the village watching "
        "from a careful distance, having learned in the worst possible "
        "way what this particular field could produce when strangers "
        "misjudged it. He moved without hurry, studying the ground, "
        "the tree line, the still, watchful quiet of the iroko roots "
        "themselves, and stopped precisely at the last planted stone, "
        "exactly where he had said he would, without needing to be "
        "reminded or restrained."
    )},
    {"type": "body", "text": (
        "\"I have seen enough,\" he said, after a long moment of "
        "simply standing and looking, close enough to the tree line "
        "that Osadebe found himself counting his own breaths without "
        "meaning to. \"I do not need to understand what lives past "
        "this line to know that my orders are to hold this side of it, "
        "not to test the patience of whatever holds the other.\" He "
        "turned back toward the field without a further word, and "
        "Osadebe found himself, for the first time since arriving in "
        "Idoro, genuinely relieved by how little curiosity a crown "
        "officer had chosen to indulge."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — LEARNING WHEN NOT TO ACT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity felt the new arrivals "
        "settle at Idoro's edge as a shift in the ambient texture of "
        "the village's fear, organized and disciplined in a way the "
        "mercenary party's ragged aggression had never been, closer to "
        "the low, patient tension of men prepared for danger than the "
        "hungry certainty of men hunting for it."
    )},
    {"type": "body", "text": (
        "The boy felt it too, the way he now felt most things moving "
        "through the entity's attention even when it did not "
        "deliberately share them, and asked, already half reaching for "
        "the readiness their training had built into him these last "
        "weeks, whether this was the moment the entity had been "
        "preparing him for."
    )},
    {"type": "body", "text": (
        "The entity watched the officer's careful walk along the "
        "boundary through the same faint attention it kept trained on "
        "everything crossing near its borders now, and felt something "
        "close to surprise at how precisely the man stopped, as though "
        "he had measured the exact distance of safety by instinct "
        "alone rather than any warning Osadebe could have given him in "
        "words. It let him look his fill and turn away, offering "
        "nothing back, neither threat nor welcome, the first time in "
        "weeks it had let a stranger approach the tree line and leave "
        "again having felt nothing from the ground at all."
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "\"No,\" the entity said, more firmly than it had said "
        "anything to him in days. \"These men have done nothing yet "
        "but walk toward a line and stop exactly where they said they "
        "would. That is not a threat. That is caution, the same "
        "caution I am teaching you to use instead of force whenever "
        "force is not yet required.\""
    )},
    {"type": "body", "text": (
        "\"But last time,\" the boy said, \"you did not wait to see "
        "what they would do. You struck first, before they reached the "
        "trees.\""
    )},
    {"type": "body", "text": (
        "The entity considered the distinction carefully, aware the "
        "boy had caught a genuine inconsistency rather than a "
        "misunderstanding. \"Last time, six armed men crossed every "
        "boundary stone your own village had planted, ignoring every "
        "warning offered to them first,\" it said. \"These men stopped "
        "at the very last stone and asked permission before doing even "
        "that much. The difference is not in what I am willing to do. "
        "It is in what they have actually done. Force spent on someone "
        "who has not yet earned it is not strength. It is simply "
        "cruelty wearing strength's clothes.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "The flat voice entered the lesson in its ledger."
    )},
    {"type": "system", "text": "Vessel: first lesson in restraint as deliberate act rather than passive absence of force. Distinction between threat and caution successfully communicated, though not yet fully tested under pressure."},
    {"type": "body", "text": (
        "The boy sat with this longer than the entity expected, "
        "turning the idea over the way he turned over every lesson "
        "that asked him to hold two true things at once without "
        "collapsing one into the other. \"That is harder than moving a "
        "stone,\" he said finally. \"Choosing to act was hard enough to "
        "learn. Choosing not to, when some part of me already wants "
        "to, feels like learning the same thing backward.\""
    )},
    {"type": "body", "text": (
        "\"It is the same thing,\" the entity told him. \"Control was "
        "never only about making something happen. It was always, "
        "just as much, about being able to stop it from happening when "
        "stopping is the harder, better choice.\""
    )},
    {"type": "body", "text": (
        "The boy considered his own hands a while, the same small "
        "careful study he had given them the night at the boundary, "
        "and asked a question the entity had not expected. \"How did "
        "you learn it,\" he said. \"The stopping part. You have been "
        "patient for three hundred years. Did something teach you "
        "that, or did you simply decide it on your own.\""
    )},
    {"type": "body", "text": (
        "The entity found, turning the question over, that it did not "
        "have a clean answer ready, an increasingly familiar feeling "
        "these last weeks. \"I do not fully remember deciding it,\" it "
        "admitted. \"Patience simply became the only strategy that "
        "kept working, across enough failed attempts at haste, until "
        "haste stopped feeling like an option worth reaching for at "
        "all. I do not know if that counts as being taught or simply "
        "being worn down slowly enough to mistake the wearing for "
        "wisdom.\""
    )},
    {"type": "body", "text": (
        "It watched him return to his stones afterward, quieter than "
        "usual, arranging them with a new deliberateness that looked "
        "less like play and more like rehearsal, and understood that "
        "this particular lesson, unlike every one before it, would not "
        "be proven learned until the exact moment it was tested by "
        "something the entity could not schedule, predict, or soften "
        "in advance."
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
    print("  THE DARK RISE — Episode 45: \"A Different Kind of Watching\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_45.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_45.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
