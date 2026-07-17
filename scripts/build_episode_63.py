#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 63: "What Amara Was Promised"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-08: Episode 63 follows Chibundu keeping the promise he
made at the furthest line, telling Amara everything the cold place
gave him, in a size she can actually use rather than withholding it
the way secrets have cost this family before. Amara insists the
warning of a new, unidentified danger cannot stay private, and the
council is told before the day is finished. Elder Maka's grandmother's
stories offer no clean answer this time, only more dread. The episode
closes on Zara, resting at Amara's compound, feeling a texture of
wrongness reach her that matches neither the entity's old grip nor the
presence's patient one — a third kind of touch, unnamed and
unwelcome, confirming from an entirely human, unwitting source that
whatever is coming is already close enough to be felt.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_63.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Three"},
    {"type": "title_ep_name", "text": "What Amara Was Promised"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE SIZE SHE COULD USE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu found Amara waiting at the boundary rather than back "
        "at the compound, unwilling, she admitted, to put even a "
        "field's width between herself and whatever answer he brought "
        "back with him. \"Tell me,\" she said, \"the way you told the "
        "Factor your own answer. Plainly, and all of it.\""
    )},
    {"type": "body", "text": (
        "The morning had turned warm and ordinary around them by then, "
        "the mist that had hidden the Factor's approach long since "
        "burned off, birds moving through the tree line as though "
        "nothing unusual had happened there at all, and Chibundu found "
        "himself grateful for the plainness of it, a world going on "
        "being itself while he tried to find the words for something "
        "that refused to feel ordinary at all."
    )},
    {"type": "body", "text": (
        "He told her the whole shape of it, the cold place's stillness, "
        "the presence's grief over a ground it had lost long before her "
        "own grandmother's grandmother was born, the narrower promise "
        "it had finally offered in place of the whole one he had "
        "demanded. Amara listened without once interrupting, her face "
        "carrying the particular stillness of a mother deciding, in "
        "real time, how much fear she could afford to show him while he "
        "still needed to see that she could hold it."
    )},
    {"type": "body", "text": (
        "\"And the last part,\" she said, once he had finished. \"The "
        "thing it says is coming. Tell me that part too, exactly the "
        "way it told you, without smoothing any of the edges off it for "
        "my sake.\""
    )},
    {"type": "body", "text": (
        "\"It does not know what it is yet,\" Chibundu said. \"Only "
        "that it is not the Factor's House, and that it is closer than "
        "either old power expected it to be this soon.\" He watched her "
        "absorb that, and added, before she could ask, the thing he had "
        "decided walking back that she most needed to hear. \"I am "
        "telling you this because you asked me to, and because I have "
        "learned, watching this whole family nearly come apart over "
        "secrets kept with good intentions, that a fear shared early is "
        "smaller than a fear discovered late.\""
    )},
    {"type": "body", "text": (
        "Obi, waiting a short distance off with Kene asleep against his "
        "shoulder, had listened to all of it without moving closer, "
        "understanding by now when a conversation belonged to Amara and "
        "Chibundu alone and when it belonged to the whole family. Once "
        "Chibundu finished, he stepped forward and set a hand briefly "
        "on the boy's shoulder, the closest thing to an embrace the "
        "sleeping toddler between them allowed. \"You did not have to "
        "carry that back yourself,\" he said. \"I am glad you chose to "
        "anyway.\""
    )},
    {"type": "body", "text": (
        "\"I did have to,\" Chibundu said. \"Not because anyone required "
        "it of me. Because I decided, somewhere in that cold place, "
        "that I would rather be the one who tells this family hard "
        "things than the one who lets something else decide when they "
        "are finally allowed to know them.\" Amara felt something in her "
        "chest ache at hearing her own hard won lesson handed back to "
        "her, spoken now in a voice that had learned it faster and more "
        "completely than she ever had."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A COUNCIL THAT HAS LEARNED SOMETHING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara carried the news to the council herself that same "
        "afternoon rather than let it sit even one more night unshared, "
        "and found, gathering the circle beneath the mango tree, that "
        "no one argued the wisdom of hearing it plainly. \"We have all "
        "watched what a hidden fear costs this village,\" Ozoemena said, "
        "before she had finished speaking. \"I do not intend to be the "
        "reason it costs us again.\""
    )},
    {"type": "body", "text": (
        "Osadebe took the account down carefully, the same flat, "
        "practiced attention he brought to every report, though "
        "Chidebe noticed his pen slowed considerably at the part "
        "describing a power older than the entity admitting fear of its "
        "own. \"I do not know how I write this for Udo in a way that "
        "sounds like information rather than a ghost story,\" he "
        "admitted. \"And yet I intend to write it plainly regardless, "
        "since a captain who only reports comfortable truths is not "
        "worth the coin the crown pays him.\""
    )},
    {"type": "body", "text": (
        "\"Write it exactly as she gave it to you,\" Chidebe said. \"If "
        "Udo thinks its captain has begun inventing ghost stories, that "
        "is a smaller cost than Udo discovering later that its captain "
        "knew and stayed silent to spare himself the embarrassment of "
        "sounding frightened.\" Osadebe allowed himself a short, tired "
        "laugh at that, the first either man had managed since the "
        "meeting, and bent back over the page with renewed, if grim, "
        "purpose."
    )},
    {"type": "body", "text": (
        "Elder Maka listened with the particular stillness she "
        "reserved now for anything touching her grandmother's old "
        "stories, and when Amara finished, shook her head slowly, "
        "honest in her own limits for once rather than reaching for a "
        "certainty she did not actually have. \"My grandmother's "
        "stories warned of houses that hunt spirits,\" she said. \"They "
        "never once warned me what to do when the spirits themselves "
        "admit to being frightened of something we cannot yet name. I "
        "have no old wisdom left to offer this particular fear. I can "
        "only tell you that a power admitting its own limits is rarer, "
        "in every story I was ever told, than a power pretending it has "
        "none.\""
    )},
    {"type": "body", "text": (
        "Chidebe, practical as ever, asked the only question that "
        "actually changed what the council could do before nightfall. "
        "\"Does this danger announce itself the way an army does, or the "
        "way the Factor did,\" he said. \"Because I know how to ready "
        "men against the first. I am considerably less certain how to "
        "ready them against the second.\""
    )},
    {"type": "body", "text": (
        "\"Neither the entity nor the presence could tell me,\" "
        "Chibundu admitted. \"That is, I think, the truest measure of "
        "how unfamiliar this is to both of them. Whatever readiness "
        "looks like this time, I do not believe it will look like "
        "soldiers at a boundary stone.\" The council sat with that "
        "answer a long moment, the particular discomfort of a group of "
        "people who had only just finished learning to prepare for one "
        "kind of danger being told, plainly, that the next one would "
        "not resemble it at all."
    )},
    {"type": "body", "text": (
        "Adaugo, seated at her mother's side through the whole "
        "session, asked the question that seemed to have occurred to "
        "no one else in the circle. \"If neither old power recognizes "
        "this danger,\" she said, \"then perhaps it is not a danger "
        "either of them has met before. Perhaps it is something that "
        "belongs entirely to the human part of this, the crown, the "
        "House, Idoro itself, and we are the ones who should be looking "
        "for its shape rather than waiting for the entity to name it "
        "for us.\" Elder Maka looked at her daughter with something "
        "close to startled pride, and the council took the thought "
        "seriously enough to sit with it a long while before the "
        "session finally closed."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A THIRD KIND OF TOUCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "At Amara's compound, Zara sat mending a torn cloth by the "
        "evening fire, still recovering the last of her strength from "
        "the boundary naming weeks before, and felt, without warning, "
        "her needle still itself between her fingers. She had learned "
        "by now to recognize the entity's old, curious grip and the "
        "presence's slower, more patient one, two different textures "
        "she had grown, uneasily, almost fluent in telling apart."
    )},
    {"type": "body", "text": (
        "This was neither. It arrived cold in a way that had no "
        "patience folded into it at all, no curiosity, nothing that "
        "resembled either old power's particular attention, only a "
        "brief, indifferent pressure that touched her and moved on "
        "before she could even find the fear to name it properly. It "
        "was gone again almost before she trusted that it had been "
        "there at all, leaving behind only the certain, unshakable "
        "knowledge that something new had just noticed her existed."
    )},
    {"type": "body", "text": (
        "She sat very still for a long moment afterward, waiting to "
        "see if it would return, the way the entity's early touches "
        "always had, curious and testing. It did not. Whatever had "
        "brushed against her seemed to have taken exactly what it "
        "wanted from the noticing alone and moved on without any "
        "further interest in lingering, which frightened her more, "
        "turning it over, than a longer, more deliberate touch might "
        "have. A hunger that lingers can at least be watched. A hunger "
        "that simply confirms something and leaves gives nothing back "
        "to prepare for it with."
    )},
    {"type": "body", "text": (
        "She said nothing at first, turning the strange, cold touch "
        "over in private the way she had once turned over her first "
        "waking intrusion before ever telling a soul, and felt the old, "
        "familiar pull toward silence rise in her exactly the way it "
        "always had, patient and reasonable and, she now knew with hard "
        "won certainty, never once actually kind."
    )},
    {"type": "body", "text": (
        "She set the mending down instead, and rose to find Amara "
        "before the fire could finish settling into embers. Whatever "
        "this was, cold and indifferent and entirely unlike anything "
        "that had ever reached for her before, she had already spent "
        "one season of her life learning exactly what a held secret "
        "costs a household that trusts her. She did not intend to spend "
        "a second one relearning it the same hard way."
    )},
    {"type": "body", "text": (
        "Amara was still awake when Zara found her, sitting with Obi "
        "over the last of the evening's small talk, and read the look "
        "on the midwife's face before a single word passed between "
        "them. \"Something touched you,\" Amara said, not quite a "
        "question. Zara nodded, and began, without being asked twice, "
        "to describe a cold she had no name for yet, the two of them "
        "leaning toward the fire together the way this whole household "
        "had learned, across a long, difficult season, to lean toward "
        "hard truths rather than away from them."
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
    print("  THE DARK RISE — Episode 63: \"What Amara Was Promised\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_63.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_63.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
