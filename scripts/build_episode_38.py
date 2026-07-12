#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 38: "The First Refusal"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-14: Episode 38 pairs two versions of the same failure of
protection. In Idoro, Osadebe brings the council word that the crown has
prepared but not ordered a survey of their land, leaving Idoro suspended
between decisions made elsewhere; Ozoemena responds by organizing the
village to mark and document its own boundaries, a small assertion of
agency against a danger no one there can out argue. In Oso, the entity,
still shaken by Episode 37's discovery that something else has been
reaching the vessel in his sleep, tries for the first time to actually
restrain him rather than merely guide him, forbidding him from the root
wall where the dreams seem strongest. The boy, growing into a will the
entity itself has always known was not fully its own, defies the
instruction outright: this is the story's first real confrontation
between protagonist and entity. He reaches the cold dark place again
despite the entity's attempt to block him, and this time it does not stay
silent — the episode closes on the first single, deliberate sound to ever
come back to him from that dark, no longer merely a presence but
something that has decided to answer.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_38.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Eight"},
    {"type": "title_ep_name", "text": "The First Refusal"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — MARKING WHAT IS ALREADY THEIRS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe delivered the news from Udo plainly, the way he had "
        "learned this particular council preferred its truths handed "
        "over. The crown would not survey Idoro's land, not yet. The "
        "crown had also not promised it never would. Everything stood "
        "prepared, waiting only on a decision none of them in this "
        "clearing had any part in making."
    )},
    {"type": "body", "text": (
        "\"So we are still waiting,\" Amara said, not quite a "
        "question, more a tired naming of a condition Idoro seemed "
        "never fully able to leave. \"Waiting on the entity to decide "
        "what it wants from my son. Waiting on the council in Udo to "
        "decide what our ground is worth. I begin to think waiting is "
        "the only thing this village has ever been permitted to do "
        "well.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Ozoemena, standing at the edge of the circle with a jar of "
        "water balanced on one shoulder, set it down slowly. \"Then let "
        "us stop waiting on the part we can actually do something "
        "about,\" he said. \"I cannot argue with a foreign House or a "
        "king I have never met. But I can walk every boundary stone "
        "this village has ever planted and make certain each one still "
        "stands exactly where our grandparents left it. If someone "
        "someday claims this ground was never truly held by anyone, "
        "let them find every stone accounted for and every elder alive "
        "and willing to swear to it before a single spade ever touches "
        "the soil.\""
    )},
    {"type": "body", "text": (
        "It was, Amara thought, the smallest possible answer to a "
        "danger built from surveys and tribute and men who had never "
        "once walked Idoro's soil themselves, and it was also, for the "
        "first time in weeks, something that did not require anyone's "
        "permission but their own. She agreed to walk the boundary with "
        "him the following morning, and found herself grateful, "
        "watching Ozoemena's careful new humility do more good for the "
        "village than his old certainty ever had, that some kinds of "
        "atonement actually did outlast the mistake that made them "
        "necessary."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The walk itself took most of the following day, boundary "
        "stone by boundary stone, three elders arguing gently over "
        "which half buried marker belonged to which family's memory "
        "until Amara, on instinct more than plan, suggested they send "
        "for Elder Maka, whose own grandmother had walked this same "
        "line two generations before any of them were born."
    )},
    {"type": "body", "text": (
        "Elder Maka came slowly, unused yet to being asked for "
        "anything by the village that had stripped her, and stood "
        "silent a long moment at the first disputed stone before "
        "correcting its placement with a certainty no one else in the "
        "group could argue against. \"My grandmother made me learn "
        "every one of these before she would teach me anything else,\" "
        "she said, not quite meeting anyone's eyes. \"She said a people "
        "who forget where their own ground begins deserve whatever "
        "someone else eventually decides to call it.\""
    )},
    {"type": "body", "text": (
        "It was the longest anyone had heard her speak since her "
        "authority fell, her voice steadier than it had sounded in "
        "weeks, and by the time the boundary walk finished at dusk, "
        "three younger elders had begun asking her, unprompted, about "
        "markers further out that none of them had ever thought to "
        "question. Amara said nothing about it to her directly, but "
        "walked home that evening thinking that a village which had "
        "only known how to cast people out might, slowly and without "
        "ever quite admitting it was doing so, be learning the "
        "opposite skill instead."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe watched the two of them plan a boundary walk with a "
        "quiet satisfaction he did not entirely trust in himself. He "
        "had come to Idoro as the crown's eyes, and some part of him "
        "still was, faithfully, whatever else he had also become to "
        "this village in the weeks since. He wondered, watching Amara "
        "and Ozoemena argue amicably over which elder to ask first, "
        "whether the report he sent north tonight should mention that "
        "Idoro had begun defending itself in the one language a survey "
        "could not easily erase, and decided, for once, that some "
        "truths were more useful kept close a little longer than "
        "shared immediately."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE BOY WHO WOULD NOT BE HELD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity had spent a full day "
        "deciding how to keep the boy from the cold dark place without "
        "telling him why, and had concluded, reluctantly, that there "
        "was no version of the instruction that did not sound exactly "
        "like what it was: a door being closed on him for the first "
        "time in his short, carefully tended life."
    )},
    {"type": "body", "text": (
        "\"You are not to go there again,\" it told him, as gently as "
        "the words allowed, when he settled among his stones that "
        "evening. \"Not to the cold place. Not while you sleep, if you "
        "can help it, and I will help you if you cannot.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The boy looked up at that, something new moving across his "
        "small face, an expression the entity had shaped almost every "
        "other one of his expressions and did not recognize this one "
        "at all. \"Why,\" he asked, and it was not the plain, searching "
        "why of a child wanting information. It carried an edge the "
        "entity had never once heard from him."
    )},
    {"type": "body", "text": (
        "\"Because I do not yet know what waits there,\" the entity "
        "said, choosing honesty over authority because it had learned, "
        "across these last careful weeks, that authority alone no "
        "longer moved him the way it once had. \"And until I know what "
        "it is, I would rather you stayed somewhere I can reach you.\""
    )},
    {"type": "body", "text": (
        "\"You did not know what waited there either time you went "
        "yourself,\" the boy said. \"You went anyway.\" He said it "
        "without anger, which somehow made it land harder than anger "
        "would have, a simple fact laid down between them that the "
        "entity had no honest way to argue against."
    )},
    {"type": "body", "text": (
        "It searched, briefly and without success, for a version of "
        "the truth that would satisfy him without frightening him, the "
        "same search it had run a hundred times since deciding "
        "concealment no longer served either of them, and found this "
        "particular truth too heavy to hand over whole. Everything it "
        "had built in him this last season had been built on the "
        "assumption that it alone stood between the boy and whatever "
        "Idoro or the wider world might someday do to him. It had "
        "never once prepared an answer for a danger reaching him from "
        "the same direction the entity itself had come from. \"I am "
        "allowed to risk myself,\" it told him instead, aware even as "
        "it spoke how thin the reasoning sounded. \"I am not yet "
        "willing to risk you.\""
    )},
    {"type": "body", "text": (
        "\"You already have,\" the boy said. \"Every night I go there "
        "and you do not know it, you are risking me. Telling me to "
        "stop does not undo the nights before you noticed.\" He said "
        "this last part quietly, almost kindly, the way a much older "
        "mind might correct a smaller one out of genuine concern rather "
        "than defiance, and the entity understood, hearing it, that the "
        "boy was not fighting to be disobedient. He was fighting "
        "because the instruction itself did not match anything true "
        "about the shape of the danger they were both actually facing."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "VESSEL: FIRST DIRECT VERBAL DEFIANCE OF EXPLICIT INSTRUCTION. "
        "REASONING SOUND, NOT IMPULSIVE. UNABLE TO COUNTER WITHOUT "
        "INVOKING AUTHORITY ALONE."
    )},
    {"type": "body", "text": (
        "It tried anyway, because trying was the only tool it had left "
        "that did not depend on him agreeing with it, weaving a "
        "careful, close binding around his sleeping mind that night, "
        "the gentlest hold it had ever placed on him, meant only to "
        "keep his wandering attention pinned to the hollow rather than "
        "the deeper dark beyond it."
    )},
    {"type": "body", "text": (
        "It held for the better part of the night. Then, sometime past "
        "the deepest hour, the entity felt the binding give the way a "
        "held breath finally gives, not broken so much as simply set "
        "aside, as though the boy had found the exact seam in a knot "
        "the entity itself had tied and worked it loose without ever "
        "fully waking to do it."
    )},
    {"type": "body", "text": (
        "It was not strength that undid the binding. The entity would "
        "have recognized strength immediately, having built and broken "
        "far greater holds than this one across three centuries of "
        "practice. This was something closer to familiarity, a mind "
        "moving through a knot it had already loosened many times "
        "before without either of them ever once noticing, and the "
        "entity understood, chasing after him too late to stop it, "
        "that it had spent this whole confrontation assuming a "
        "strength contest it had already lost long before it ever "
        "issued the instruction."
    )},
    {"type": "body", "text": (
        "By the time the entity reached him, he was already standing "
        "in the cold place, small and unafraid among roots that were "
        "not the entity's roots, and this time the silence that had "
        "always waited there did not hold its breath. A single sound "
        "moved through the dark, low and deliberate, shaped enough to "
        "be a word without yet being one the entity understood, aimed "
        "unmistakably at the boy rather than at anything that had come "
        "looking for it."
    )},
    {"type": "body", "text": (
        "For the first time since it had claimed this ground, the "
        "thing beneath the ak-pu roots understood that the silence on "
        "the other side of its own borders had just stopped waiting "
        "and started speaking, and that it had chosen, deliberately, "
        "to do it on a night the entity had tried hardest to keep the "
        "boy away."
    )},
    {"type": "body", "text": (
        "The boy turned toward the sound with the same unbothered "
        "recognition he gave everything in that dark, unaware he had "
        "just become the first living thing in three centuries to hear "
        "something out there choose, deliberately, to be heard."
    )},

    {"type": "blank", "text": ""},
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
    print("  THE DARK RISE — Episode 38: \"The First Refusal\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_38.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_38.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
