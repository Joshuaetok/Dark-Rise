#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 97: "The Line He Crossed"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-12: Episode 97 delivers the crossing Episode 96 set up.
Ubani walks into Oso alone at first light, Ude and Chidebe held back at
the boundary, unable to follow without confirming the very secret they
hope to protect. Inside, Ubani encounters nothing that resembles a
monster or a voice, only a mounting, formless wrongness the entity
allows to reach him deliberately and minimally: absolute silence,
disorientation, an animal certainty of being watched by something vast
that never shows itself. The entity chooses this ambient dread over any
direct confrontation, gambling that an ordinary man's own fear will
turn him back before curiosity carries him deeper. It works. Ubani
stumbles back out badly shaken, having seen nothing he can honestly
describe, and refuses to discuss what happened until he has decided,
alone, exactly how much of it belongs in an official crown record.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_97.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Seven"},
    {"type": "title_ep_name", "text": "The Line He Crossed"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: FIRST LIGHT AT THE TREE LINE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ubani reached the tree line before the sun had fully cleared "
        "it, his notebook tucked inside his shirt rather than carried "
        "openly, his measuring chain left behind entirely. Some ground, "
        "he had decided overnight, was better walked with empty hands "
        "and open eyes than with instruments that only measured what a "
        "man already expected to find."
    )},
    {"type": "body", "text": (
        "Chidebe and Ude waited at the boundary itself, close enough to "
        "see him and far enough, by Ubani's own quiet insistence, not "
        "to follow. \"If something is wrong in there,\" Ubani had told "
        "them at dawn, \"I would rather one man carry it out than "
        "three.\" Chidebe had not argued, though every instinct trained "
        "into him over years of guarding this exact ground screamed "
        "against letting anyone walk it alone. He had spent seasons "
        "learning exactly how much this ground could cost a person who "
        "wandered into it unprepared, and standing here now, watching a "
        "stranger do exactly that by choice, tested a different kind of "
        "nerve than any soldier's duty ever had."
    )},
    {"type": "body", "text": (
        "Amara watched from further back, close enough to see Ubani's "
        "shape disappear into the tree line and far enough to keep her "
        "own presence from becoming another variable he might have to "
        "explain later. Obi stood beside her, saying nothing, his hand "
        "finding hers without either of them looking away from the "
        "boundary. Neither of them had slept, and neither pretended "
        "otherwise. There was nothing left to plan, and no way to help "
        "beyond simply standing witness to whatever the morning "
        "decided to give them."
    )},
    {"type": "body", "text": (
        "Ubani stepped past the last ordinary tree at exactly the point "
        "his own measurements had marked three times over, and felt the "
        "birdsong behind him end as cleanly as a door closing. He noted "
        "it in his mind rather than his notebook, unwilling yet to stop "
        "walking long enough to write, and pressed on into a silence so "
        "complete it seemed to press back against his own footsteps."
    )},
    {"type": "body", "text": (
        "He counted his own steps out of old habit, a discipline from "
        "his very first commission that had never once failed to steady "
        "him in unfamiliar ground, and found, twenty paces in, that he "
        "had lost count entirely without noticing the moment it "
        "happened, an admission that troubled him more than anything "
        "his eyes had yet shown him."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE ENTITY CHOSE TO SHOW HIM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In the cold place beneath Oso's roots, the entity felt Ubani's "
        "presence the instant he crossed, unmistakable and entirely "
        "unlike anything that had ever walked this ground uninvited. "
        "Chibundu felt it too, through their shared awareness, and asked "
        "the only question that mattered before either of them decided "
        "anything else. \"What will you do.\""
    )},
    {"type": "body", "text": (
        "The entity considered its own weakness honestly before "
        "answering, weighing what little strength it had rebuilt since "
        "the confrontation against what a direct confrontation with an "
        "innocent, curious man would actually require. \"Nothing he "
        "could name afterward,\" it said finally. \"I do not have the "
        "strength to frighten him the way I frightened Mfoniso, and I "
        "would not spend it on a man who means us no harm even if I "
        "did. But an ordinary man's own mind, left alone in a silence "
        "this complete, will do most of the frightening for me.\""
    )},
    {"type": "body", "text": (
        "The presence, watching from its own distance beyond Oso's "
        "borders, offered a single word of caution before falling "
        "silent again. \"Be certain,\" it said, \"that you are choosing "
        "restraint because it is wise, and not merely because it is "
        "all the strength you currently have to spend. The two can "
        "look identical from the inside, and only one of them is truly "
        "a virtue.\" The entity did not answer that directly, though "
        "Chibundu felt it turn the words over carefully all the same."
    )},
    {"type": "body", "text": (
        "It did not manifest. It did not speak, or reach, or show "
        "itself in any shape a man could later describe to another man "
        "and be believed. It simply stopped softening the ordinary "
        "weight of Oso's ancient stillness, the way a host stops "
        "pretending a house is warmer than it truly is, and let Ubani "
        "feel the forest exactly as it had always felt to anything that "
        "did not belong there."
    )},
    {"type": "body", "text": (
        "Ubani felt it as a wrongness with no single cause he could "
        "isolate, a held breath that never released, a certainty, "
        "animal and immediate, that something vast was aware of exactly "
        "where he stood without ever once revealing where it stood "
        "itself. He turned in a slow circle, instruments forgotten, "
        "and found every direction equally, uselessly empty."
    )},
    {"type": "body", "text": (
        "The cold reached him next, not the cold of morning air but "
        "something that seemed to rise from the ground itself, climbing "
        "past his ankles the way water climbs a sinking man, and Ubani, "
        "a careful and rational man who had spent fifteen years "
        "trusting his instruments over his instincts, found his "
        "instincts, for the first time in his career, entirely and "
        "completely correct. He stood very still inside it for a "
        "moment, the way a man stands in a river deciding whether the "
        "current has grown too strong to cross."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT HE COULD NOT DESCRIBE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The wrongness built slowly enough that Ubani could not point "
        "to any single moment where curiosity became fear, only a long, "
        "gradual crossing from one state into the other, the way a "
        "man wading into a river only notices he has lost his footing "
        "once the current has already claimed him."
    )},
    {"type": "body", "text": (
        "He thought, absurdly, of his daughter, safe and ordinary in a "
        "house three days' travel from here, and found the thought did "
        "nothing to steady him the way such thoughts usually did in "
        "difficult ground. If anything it sharpened the fear, as though "
        "some part of him understood that whatever watched him here "
        "would have found a way to know about her too, given enough "
        "time and enough reason."
    )},
    {"type": "body", "text": (
        "He did not run, not exactly, but the walk he began back toward "
        "the boundary carried none of the measured, professional pace "
        "he had walked in with, and by the time the first ordinary "
        "birdsong reached him again he had nearly closed the distance "
        "at something close to a sprint, chest heaving, notebook still "
        "unopened against his ribs."
    )},
    {"type": "body", "text": (
        "Chidebe caught him at the boundary itself, steadying him by "
        "the shoulders before his own legs fully gave out beneath him. "
        "\"What did you see,\" Chidebe asked, careful to keep his own "
        "face unreadable. Ubani shook his head slowly, still catching "
        "his breath. \"Nothing,\" he said. \"That is the entire "
        "difficulty of it. I saw nothing at all, and it was the most "
        "frightening nothing I have encountered in fifteen years of "
        "this work.\""
    )},
    {"type": "body", "text": (
        "Ude offered him water with hands nearly as unsteady as Ubani's "
        "own, and Ubani drank without speaking further, staring back "
        "toward the tree line with an expression that had lost every "
        "trace of the polite, unbending certainty he had carried into "
        "it. \"I owe your village an apology,\" he said finally, to "
        "Chidebe. \"I called your fear superstition. I do not have "
        "another word for what I just felt, but I no longer believe "
        "superstition is the correct one either.\""
    )},
    {"type": "body", "text": (
        "Amara and Obi arrived at a careful distance, having watched "
        "the whole retreat from where they had waited, and Amara found "
        "herself, despite every reason she had to want Ubani discouraged "
        "and gone, genuinely moved by the sight of a proud, careful man "
        "so thoroughly shaken. \"You are safe,\" she told him, and meant "
        "it as more than simple courtesy. \"Whatever it was, it let you "
        "leave.\" Ubani looked at her with new understanding in his "
        "eyes, though not yet the full shape of it. \"You knew,\" he "
        "said quietly. \"Not everything. But something. You knew before "
        "I walked in there that it would let me leave.\" Amara did not "
        "deny it, and did not confirm it either, and Ubani, exhausted "
        "and shaken as he was, did not press her further."
    )},
    {"type": "body", "text": (
        "Chidebe asked him, as gently as the question allowed, what he "
        "intended to write in his official report. Ubani did not answer "
        "immediately, turning the question over with the same careful "
        "weight he gave every measurement he had ever taken. \"I do not "
        "know yet,\" he admitted. \"I have never once written a report "
        "I could not fully stand behind with instruments and witnesses. "
        "I do not know how to write one that stands behind nothing but "
        "my own fear, and I will not simply guess at the words until I "
        "have decided what they actually need to protect.\""
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt Ubani's retreat and allowed itself, "
        "for the first time since the confrontation, something close to "
        "relief rather than mere endurance. \"He is shaken,\" it told "
        "Chibundu, \"but he is whole, and he saw nothing he can point "
        "to as proof of anything at all. That may be the best outcome "
        "this ground has ever managed to offer a curious man.\" Chibundu "
        "did not fully share its relief. \"He still has to decide what "
        "to write,\" he said. \"Fear that cannot be named does not "
        "always stay silent simply because it has no proof to stand "
        "on.\""
    )},
    {"type": "body", "text": (
        "Ude walked Ubani slowly back toward the market rather than "
        "let him make the return journey alone, and neither man spoke "
        "much along the way, each carrying the morning's fear in his "
        "own private silence. It would be, Ubani thought, the strangest "
        "entry his career had ever demanded, and he still did not know, "
        "by the time the ordinary sounds of Idoro's market finally "
        "closed around them both, what shape the truth of it should "
        "take once it reached the crown's own hands."
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
    print("  THE DARK RISE — Episode 97: \"The Line He Crossed\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_97.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_97.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
