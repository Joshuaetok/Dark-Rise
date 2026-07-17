#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 69: "A Face in the Market"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-14: Episode 69 brings the specialist into Idoro itself
for the first time, walking the market in plain traveler's cloth to
finish what two days of watching from the tree line began. Zara,
resting near the market rather than at the compound, feels the cold,
testing touch a third time, stronger and closer than either prior
occurrence, and understands at once that whatever has been reaching
for her has finally arrived close enough to see with her own eyes.
Unlike her old silences, she raises the alarm immediately rather than
sitting with the fear alone. The household tightens around Kene
within the hour, and the episode closes with the specialist — named
here for the first time as Mfoniso — recognizing the sudden shift in
vigilance for what it is and deciding, calmly, that patience has just
become a slower tool than the moment actually calls for.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_69.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Nine"},
    {"type": "title_ep_name", "text": "A Face in the Market"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: AN ORDINARY WOMAN, BUYING CLOTH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso walked into Idoro's market at its busiest hour, "
        "exactly when a new face drew the least attention, and moved "
        "through it the way she had moved through a hundred markets "
        "before this one, unhurried, unremarkable, pausing here and "
        "there to finger a length of cloth or ask an ordinary "
        "question about the price of fish. No one who watched her "
        "pass would have remembered her face an hour later. That, "
        "after so many years doing this exact work, was precisely the "
        "point."
    )},
    {"type": "body", "text": (
        "She did not go near the compound directly, nor toward the "
        "stream where a small boy she had watched for two days liked "
        "to play. She only walked the market's edge once, slowly, "
        "learning the shape of Idoro's ordinary daylight the way she "
        "had already learned its ordinary night from the tree line, "
        "and let herself be seen buying cloth from a stall two paths "
        "over from the one Uduak had once kept, before the trader who "
        "held it now had ever heard the old one's name."
    )},
    {"type": "body", "text": (
        "She carried, beneath the plain cloth of her own bundle, a "
        "small wrapped object she touched only once, briefly, checking "
        "it was still settled correctly against her hip, an old habit "
        "worn smooth by decades of the same careful motion. Whatever "
        "it was, it made no sound and drew no eye. It simply waited, "
        "the way she herself had learned to wait, for the moment it "
        "would finally be needed."
    )},
    {"type": "body", "text": (
        "She passed a mother scolding a small boy for wandering too "
        "far from a market stall, and felt, for exactly the length of "
        "one held breath, something in her own careful composure "
        "waver, a memory older than this entire commission surfacing "
        "uninvited before she set it firmly back where it belonged. "
        "She had learned, across many years and several homes she no "
        "longer let herself name aloud, that this particular work went "
        "easier when a person stopped noticing which children reminded "
        "her of anything at all."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE THIRD TOUCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara felt it the moment Mfoniso crossed within sight of the "
        "market's central well, a cold so total and so close that she "
        "dropped the calabash she had been carrying, water spreading "
        "dark across the dry ground before she even registered her own "
        "hands had opened. This was not the brief, testing brush she "
        "had described to Amara and Elder Maka twice already. This "
        "arrived whole, and stayed, and felt, for the first time, "
        "close enough to have a direction."
    )},
    {"type": "body", "text": (
        "She did not sit with it this time, turning it over in "
        "private the way she once would have. She turned instead, "
        "scanning the crowded market with a wild, searching urgency, "
        "and called out to the first familiar face she found. \"Elder "
        "Maka,\" she said, her voice carrying further than she "
        "intended in the market's ordinary noise. \"It is here. Not "
        "reaching from somewhere far off. Here, now, close enough to "
        "touch.\""
    )},
    {"type": "body", "text": (
        "Elder Maka crossed to her at once, and Zara pointed, her hand "
        "shaking, toward the loose, unremarkable crowd moving between "
        "the stalls, unable to single out any one face from among the "
        "ordinary dozens buying and selling around them. \"I cannot "
        "tell you which one,\" she said. \"Only that it is close, and "
        "that it did not feel like this from any distance before "
        "today.\""
    )},
    {"type": "body", "text": (
        "Word reached Chidebe within minutes, carried at a run by one "
        "of Elder Maka's own watchers, and he did not waste time "
        "asking for a description he already knew Zara could not give "
        "him. \"Double the watch on the compound and the stream both, "
        "now,\" he told the nearest soldier. \"Whatever this is, we do "
        "not need to see its face to close every door it might be "
        "hoping to walk through unnoticed.\""
    )},
    {"type": "body", "text": (
        "He found Zara himself minutes later, still shaking near the "
        "spilled calabash, and crouched to meet her at eye level rather "
        "than tower over a fear this raw. \"Tell me anything at all,\" "
        "he said. \"Even a feeling with no shape to it yet. A "
        "direction. A height. Whether it felt like it was moving "
        "toward the compound or away from it.\""
    )},
    {"type": "body", "text": (
        "\"Toward,\" Zara said, certain of that much even through the "
        "residual cold still gripping her hands. \"It was moving "
        "toward the compound when I felt it, or had just come from "
        "that direction. I am sorry. I know that is not enough to act "
        "on cleanly.\""
    )},
    {"type": "body", "text": (
        "\"It is considerably more than we had an hour ago,\" Chidebe "
        "said, and meant it, already turning to relay the direction to "
        "his men rather than waste another moment on comfort neither "
        "of them had time to spend. Elder Maka stayed with Zara a "
        "while longer, saying little, letting her simply shake in "
        "peace now that the alarm was already moving through Idoro "
        "without her having to carry it any further herself."
    )},
    {"type": "body", "text": (
        "Amara reached Kene before the soldiers did, pulling him from "
        "his afternoon game at the compound's edge with an urgency he "
        "did not understand and did not fight, some part of him "
        "already fluent enough in his mother's fear to know better "
        "than to ask questions in the moment it arrived. She held him "
        "close, watching the ordinary path toward the fields the way "
        "she had watched it every evening since the warning first "
        "reached her, and found no comfort at all in how empty and "
        "unremarkable it continued to look."
    )},
    {"type": "body", "text": (
        "The entity felt the sudden spike in Idoro's fear reach it "
        "across the distance within minutes, sharp and specific in a "
        "way ordinary village worry never was, and relayed it to "
        "Chibundu at once rather than spend even a moment deciding how "
        "much of it to soften. \"Zara felt it close,\" it told him. "
        "\"Closer than either of us has managed to sense it ourselves, "
        "which tells me this danger may simply move too quietly, or "
        "too humanly, for either of our own senses to catch cleanly.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt something cold settle through him at that, the "
        "particular helplessness of a threat neither the entity's old "
        "patience nor the presence's older grief could actually see "
        "coming. \"Then Zara may be the only warning any of us gets "
        "before it moves,\" he said. \"I do not like how much this "
        "family's safety has come to depend on one woman's borrowed "
        "senses rather than on either of you.\""
    )},
    {"type": "body", "text": (
        "\"Neither do I,\" the entity admitted. \"But I would rather "
        "depend on an imperfect warning that arrives in time than a "
        "perfect one that arrives after. Whatever Zara felt today, it "
        "has already bought your family more warning than either of "
        "us managed to give them on our own, and I intend to make sure "
        "she never again has cause to wonder whether telling us "
        "quickly mattered.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A PATIENCE THAT DECIDED TO END
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso felt the market's mood shift within the same hour, "
        "the particular tightening of a village suddenly watching its "
        "own children more closely than it had that morning, and knew "
        "at once, without needing to be told, exactly what had given "
        "her away. She had accounted for soldiers. She had accounted "
        "for two old powers slow to notice a human threat moving "
        "quietly among ordinary people. She had not fully accounted "
        "for a woman whose own hands had once been claimed by "
        "something patient enough to leave a permanent mark."
    )},
    {"type": "body", "text": (
        "She did not panic. Panic was not a tool she had carried in "
        "longer than she could easily remember. She simply revised "
        "the plan she had spent two careful days building, the way "
        "she had revised a hundred plans before this one when the "
        "ground shifted under her early. Patience remained the better "
        "tool in most circumstances. It was, however, only ever a "
        "tool, and a tool that had just been noticed was a tool that "
        "had stopped being useful in its current shape."
    )},
    {"type": "body", "text": (
        "She finished her small, ordinary purchase of cloth, thanked "
        "the trader plainly, and walked out of Idoro's market at the "
        "same unhurried pace she had walked into it, giving no watching "
        "eye any reason to mark her as anything other than a traveler "
        "passing through. But her mind had already moved past the "
        "market entirely, turning over a smaller, faster shape of the "
        "same plan, one that would not require the two more days of "
        "patient waiting she had originally allowed herself."
    )},
    {"type": "body", "text": (
        "The wrapped object at her hip would do most of the work "
        "itself, once she was close enough, requiring nothing from her "
        "but proximity and a single quiet word she had spoken so many "
        "times across so many years that it no longer felt like "
        "language at all, only muscle and breath moving together. She "
        "did not need the boy brought to her. She needed only enough "
        "of the night's ordinary darkness, and enough of Idoro's "
        "attention still turned toward the market rather than the "
        "stream, to close the last small distance between herself and "
        "an opening she had already spent two patient days confirming "
        "was real."
    )},
    {"type": "body", "text": (
        "Idoro had just taught her, without meaning to, that whatever "
        "window still remained would need to be used tonight, before "
        "a village's sharpened fear finished closing every door she "
        "had spent this long, careful season learning to walk through "
        "unnoticed. She had lost the advantage of being unnoticed. She "
        "still held, for a few hours longer at least, the advantage of "
        "being underestimated, and she did not intend to let that "
        "second advantage go to waste alongside the first."
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
    print("  THE DARK RISE — Episode 69: \"A Face in the Market\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_69.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_69.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
