#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 61: "The Reckoning at the Boundary"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-06: Episode 61 picks up in the same instant Episode 60
ended, with the entity mid-step, unsure whether completing it would
help Chibundu or simply prove that no promise made at this boundary
can actually be trusted to hold. It chooses to stop, letting Chibundu
finish the meeting on his own returned voice rather than have anyone,
entity or presence, speak over him twice in one morning. Chibundu
reclaims the conversation from the Factor directly, giving his own
answer in his own words even though it lands in the same place the
presence's stolen one did. The Factor leaves intrigued rather than
defeated, promising to learn what the second voice actually is. Once
he is gone, Chibundu turns his fury on the only two who cannot simply
walk away from it: the entity, for standing close enough to prevent
this and failing to, and the presence itself, wherever it is listening
from. The episode ends with Chibundu declaring he is going to the cold
place immediately, done waiting for an explanation to be offered on
anyone's schedule but his own.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_61.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty One"},
    {"type": "title_ep_name", "text": "The Reckoning at the Boundary"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: HIS OWN ANSWER, GIVEN TWICE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The entity stopped itself a half stride into the promise it "
        "had almost broken, held there by a single, clarifying "
        "thought arriving just quickly enough to matter: the danger "
        "had already finished happening. Stepping forward now would "
        "not undo a single word taken from the boy's mouth. It would "
        "only prove to him, in the same breath he was still finding "
        "his own voice again, that even a promise made the night "
        "before could be set aside the moment it grew inconvenient to "
        "keep."
    )},
    {"type": "body", "text": (
        "Chibundu felt the entity's stillness settle back into place "
        "beside him, and understood it without needing to be told, the "
        "particular relief of a held line rather than a broken one. He "
        "turned back to the Factor, his own voice returned to him now, "
        "rough at the edges but entirely his. \"That was not my "
        "answer,\" he said. \"I want you to hear my own before you "
        "decide what to carry back to your House.\""
    )},
    {"type": "body", "text": (
        "The Factor's attention sharpened further, delight and caution "
        "arriving together on his face in a combination Chibundu had "
        "not seen from him before. \"I am listening,\" he said. \"I "
        "confess I did not expect a third voice to speak this morning, "
        "after the first two already answered so decisively.\""
    )},
    {"type": "body", "text": (
        "\"It is not a third voice,\" Chibundu said. \"It is the same "
        "one you met at the start of this conversation, saying, in its "
        "own words, what was said for it without asking. I will not "
        "bless your House's hands in this ground. Not because "
        "something older than me forbade it. Because I have heard what "
        "your House already did upriver, and I do not believe a "
        "blessing from me changes what kind of hunger you actually "
        "are, only how comfortable people feel standing near it.\""
    )},
    {"type": "body", "text": (
        "The Factor studied him a long moment, and when he finally "
        "spoke, something in his careful warmth had cooled into a "
        "colder, more honest respect. \"That is a harder answer than "
        "the one I was given first,\" he said. \"The first was a "
        "door slammed shut by something protecting you. Yours is a "
        "door you closed yourself, having looked at what stood on the "
        "other side of it and chosen anyway. I will carry both answers "
        "back to my House, though I suspect only one of them will "
        "trouble my superiors as much as it should.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"You came here for a partnership,\" Chibundu said. \"What are "
        "you leaving with instead.\""
    )},
    {"type": "body", "text": (
        "\"A mystery,\" the Factor said, and the old, easy warmth "
        "returned to his face, though it no longer fully reached his "
        "eyes. \"My House rewards mysteries handsomely, young man, "
        "considerably more handsomely than it rewards refusals. I came "
        "prepared to bargain with one old power. I am leaving having "
        "learned there are at least two, and that the newer, quieter "
        "one apparently cares enough about you to risk your own trust "
        "in order to protect you from a choice it feared you might "
        "make wrongly. I intend to learn everything I can about that "
        "one before I return.\""
    )},
    {"type": "body", "text": (
        "He bowed once, the same unhurried courtesy he had arrived "
        "with, and turned back toward the mist without waiting to be "
        "dismissed. \"Give my regards to your council,\" he said over "
        "his shoulder. \"And to whichever voice answers next time I "
        "come asking.\" He walked until the grey morning swallowed him "
        "entirely, and the boundary he left behind felt, to everyone "
        "still standing in it, considerably less settled than it had "
        "before he arrived."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT WAS TAKEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu did not wait for the Factor's shape to fully "
        "disappear before he turned on the entity, the fear and "
        "adrenaline of the last few minutes curdling fast into "
        "something sharper. \"You promised me restraint would not cost "
        "me anything you were not willing to pay yourself,\" he said. "
        "\"You did not once mention that someone else entirely might "
        "reach into me and take the one thing this whole season was "
        "supposed to be building. My own voice. My own choice.\""
    )},
    {"type": "body", "text": (
        "\"I did not know it could,\" the entity said, and there was no "
        "defense in the answer, only a plain, unflinching honesty it "
        "had learned, across this long season, was the only currency "
        "worth spending with him now. \"I have spent three centuries "
        "certain that whatever threatened you would announce itself as "
        "a threat first. I did not plan for something that would call "
        "itself protection and take the exact thing I have spent months "
        "teaching you to hold.\""
    )},
    {"type": "body", "text": (
        "\"That is what it always calls itself,\" Chibundu said, his "
        "voice cracking now around an anger that had grief folded "
        "somewhere inside it. \"Ask Zara. Ask what it felt like the "
        "first time her own hand moved without her, the first time her "
        "own mouth said words she never chose. I used to feel sorry "
        "for her, hearing about it secondhand. I did not understand, "
        "until just now, exactly what that sorry should have cost me "
        "to feel.\""
    )},
    {"type": "body", "text": (
        "The entity absorbed that in silence, unwilling to offer any "
        "comfort it had not fully earned the right to give. \"I do not "
        "know why it chose this moment, above every other moment it "
        "could have chosen,\" it said finally. \"I only know it has "
        "grieved this exact mistake once before, in another place, and "
        "still moved to make some version of it again rather than let "
        "you risk what it feared losing.\""
    )},
    {"type": "body", "text": (
        "\"Then it can explain that to me itself,\" Chibundu said, and "
        "the entity felt the boy's resolve settle into something it "
        "recognized immediately as immovable, the same quality that had "
        "once set his own terms for this very meeting. \"Not tonight. "
        "Not when it decides I am ready to hear it. Now, while what it "
        "did is still sitting in my own throat like something "
        "swallowed wrong. I am going to the cold place, and I am not "
        "waiting for an invitation this time.\""
    )},
    {"type": "body", "text": (
        "The entity felt the old instinct rise once more, the "
        "instinct to guard the door itself rather than let him walk "
        "through it alone and furious, and set it aside for what felt "
        "like the hundredth time this season, understanding that "
        "whatever answer waited for him in that cold, root laced dark, "
        "it was owed to him directly, and not filtered, softened, or "
        "delayed by anyone standing between him and the power that had "
        "just proven it would reach past every one of them if it "
        "decided the reason was good enough."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT AMARA WAS TOLD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara reached him before he could take a single step toward "
        "the cold place, released from the furthest line the moment "
        "the Factor's shape vanished into the mist, Osadebe and Chidebe "
        "close behind her. \"Tell me what happened,\" she said, her "
        "hands already moving over him the way they had at his first "
        "reunion, checking for a wound she could not find because the "
        "wound this time had not been to his body."
    )},
    {"type": "body", "text": (
        "Chibundu told her plainly, the way he had promised himself he "
        "would tell people things now, without softening the shape of "
        "it for her comfort. \"The presence took my voice,\" he said. "
        "\"Not asked. Not warned. It simply reached in and spoke "
        "through me the way it once spoke through Zara, and I could not "
        "stop it, and I did not know it was happening until it was "
        "already finished happening.\""
    )},
    {"type": "body", "text": (
        "Amara felt something go cold and still in her that had "
        "nothing to do with the morning air, a mother's fury finding a "
        "target it had never once considered before. \"Then it will "
        "answer to me as well,\" she said, \"whatever it is, wherever it "
        "listens from. I have spent this whole season learning to fear "
        "houses and armies and captains. I did not think I would also "
        "need to fear the thing that gave my son his name.\""
    )},
    {"type": "body", "text": (
        "\"I need to be the one who goes first,\" Chibundu said, gently "
        "but without room for argument in it. \"Not because I do not "
        "want you beside me. Because if I let you fight this battle "
        "for me the way I once let the entity fight my battles for me, "
        "I will have learned nothing from this whole season, and I "
        "refuse to let what just happened cost me that too.\""
    )},
    {"type": "body", "text": (
        "Osadebe, watching the exchange with the same careful attention "
        "he brought to every report he would eventually have to write, "
        "spoke quietly to Chidebe rather than to either of them "
        "directly. \"I do not know how I am meant to explain any of "
        "this to Udo,\" he said. \"A refused offer, a second power, and "
        "a boy walking off alone to confront it, all inside a single "
        "morning. I begin to understand why Ikwuano always looked so "
        "tired reading my reports.\" Chidebe offered no comfort beyond "
        "a short, tired nod of his own, both men understanding that "
        "whatever words Osadebe eventually chose, no report could fully "
        "carry the weight of watching a boy's own voice be taken from "
        "him in front of a stranger they had all agreed to trust with "
        "exactly this much and no more."
    )},
    {"type": "body", "text": (
        "Amara held her son's face in both hands a long moment, "
        "searching it for the fear she knew had to be somewhere "
        "underneath the resolve, and found both sitting there plainly, "
        "neither one canceling the other out. \"Go, then,\" she said "
        "finally. \"But you will tell me everything after, the whole of "
        "it, the same way you just told me this. I did not survive "
        "losing you once to lose the truth of you now.\" Chibundu "
        "nodded once, and turned toward the cold place without waiting "
        "any longer for permission he had already decided he did not "
        "need."
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
    print("  THE DARK RISE — Episode 61: \"The Reckoning at the Boundary\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_61.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_61.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
