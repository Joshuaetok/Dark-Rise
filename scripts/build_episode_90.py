#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 90: "The Confrontation"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-05: Episode 90 delivers the confrontation Episode 89
set in motion. With most of Chidebe's soldiers deployed to the market
ambush, the compound itself is left thin, exactly the gap Mfoniso's
choice to bypass the drop point was built to exploit. She reaches the
compound in near silence and goes straight for Adaugo, the anchor
thread her clearest remaining leverage. Emenike, watched but armed for
the first time since his exposure, throws himself into her path to
protect Adaugo and is struck down badly. The entity, sensing the attack
through Chibundu's connection to the household, breaks three centuries
of restraint for the first time in the story to act directly rather
than only advise, reaching further than it ever has to drive Mfoniso
back. She retreats, wounded and shaken by a guardian power meeting her
in the open for the first time, rather than pressing an advantage she
no longer trusts. The episode closes on Emenike bleeding in Amara's
arms and the entity, having spent something none of them yet
understand the size of, gone suddenly and completely silent.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_90.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety"},
    {"type": "title_ep_name", "text": "The Confrontation"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE GAP THE TRAP LEFT OPEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The compound, with nearly every soldier Chidebe owned ringing "
        "the market's edge, held only a handful of watchers that night, "
        "a fact no one had spoken aloud because no one had believed it "
        "mattered. A hunter who avoided force, who valued patience over "
        "confrontation, was not the kind of danger a thin guard was "
        "built to stop. That belief had held for three seasons. It held "
        "for exactly as long as Mfoniso needed it to."
    )},
    {"type": "body", "text": (
        "Elder Maka had said as much herself, hours earlier, and no one "
        "had argued with her, not because they disagreed but because "
        "the alternative, splitting the household's remaining strength "
        "between two possible fronts, felt like a weakness inviting "
        "exactly the kind of trouble it was meant to prevent. Adaugo sat "
        "near the fire with Elder Maka close beside her, Zara a step "
        "further out testing a sense that gave her nothing, Amara and "
        "Obi moving between the yard and the gate in the restless "
        "half rhythm of people trying to look busy enough not to feel "
        "afraid."
    )},
    {"type": "body", "text": (
        "She came over the compound wall without sound, without the "
        "careful patience of a woman with all the time in the world, "
        "moving instead with the flat urgency of someone who had already "
        "decided every remaining hour belonged to danger rather than "
        "planning. Zara felt nothing, her muffled gift offering no "
        "warning at all, and so the first sign anyone had was Adaugo's "
        "own soft, startled breath as a cold hand closed over her wrist, "
        "exactly where the anchor thread had waited, uncut, for days."
    )},
    {"type": "body", "text": (
        "For one terrible instant Adaugo could not make a sound at "
        "all, the cold of the anchor thread suddenly sharp and awake "
        "beneath Mfoniso's grip in a way it had never been while merely "
        "resting, quiet, on her wrist. It felt, she would try to explain "
        "later and never quite manage, like a door that had been left "
        "unlocked for weeks finally being pushed all the way open."
    )},
    {"type": "body", "text": (
        "\"You should not have looked for me,\" Mfoniso said quietly, "
        "close enough that only Adaugo could hear it. \"Now I have to "
        "finish what I came to finish before someone louder than you "
        "notices I am here.\" Adaugo's cry, when it came, was sharp "
        "enough to wake the whole compound at once, Amara's name torn "
        "out of her before fear could steal the rest of it."
    )},
    {"type": "body", "text": (
        "Elder Maka moved first among the adults nearby, placing "
        "herself between Mfoniso and the fire without a weapon, without "
        "a plan beyond the raw refusal of a woman who had already lost "
        "one child to a working she had not understood in time. "
        "\"Whatever thread you still hold on her,\" she said, her voice "
        "steadier than she felt, \"you will have to take it through me "
        "first.\" Mfoniso did not so much as glance at her, the way a "
        "person does not glance at an obstacle they have already "
        "measured and dismissed, an obstacle already accounted for and "
        "already, in her own mind, overcome."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT STOOD BETWEEN THEM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara reached the yard first, Obi a step behind her, both of "
        "them moving on instinct rather than any plan the night had "
        "prepared them for. What they found stopped them cold: Mfoniso, "
        "unhurried even now, one hand still locked around Adaugo's "
        "wrist, studying the gathering household with the flat, "
        "professional calm of a woman who had already decided how this "
        "would end and was only waiting for them to catch up to it."
    )},
    {"type": "body", "text": (
        "Obi lunged forward anyway, past every ounce of sense he had "
        "left, and it was only Amara's hand closing hard around his arm "
        "that kept him from closing the last few paces into a reach "
        "that had already ended two soldiers' pursuits without leaving "
        "a mark to follow. \"Not like that,\" she said, her voice "
        "shaking even as it held. \"Not blind. She wants exactly this, "
        "someone rushing her without thinking.\" It cost her everything "
        "she had not to do the same."
    )},
    {"type": "body", "text": (
        "It was Emenike who moved before anyone else could, snatching a "
        "soldier's spear from where it leaned forgotten by the fire and "
        "closing the distance at a dead run, no longer a prisoner "
        "weighing his own guilt but a man who had finally found "
        "something he could do with his hands that was not betrayal. "
        "\"Let her go,\" he shouted, and put himself bodily between "
        "Mfoniso and the rest of the household."
    )},
    {"type": "body", "text": (
        "Mfoniso turned from Adaugo just enough to meet him, and the "
        "movement that followed happened too fast for anyone else to "
        "fully see, a single economical motion that ended with Emenike "
        "on the ground, a wound opening dark and wide across his side, "
        "the spear skittering uselessly away from his open hand. He had "
        "bought, with his own blood, perhaps three full seconds."
    )},
    {"type": "body", "text": (
        "Amara screamed his name and dropped to her knees beside him "
        "before conscious thought caught up with instinct, pressing both "
        "hands hard against a wound already spreading faster than she "
        "could staunch it with nothing but her own palms, while Adaugo, "
        "freed and shaking, stumbled backward into Elder Maka's waiting "
        "arms rather than toward the danger that had just released her."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the household's terror arrive all at "
        "once, raw and unfiltered, sharper than anything since the "
        "night Kene was nearly taken. \"Now,\" he said to the entity, "
        "not a request. \"Whatever it costs. Now.\" The entity, silent "
        "for one terrible heartbeat, made a choice it had never once "
        "made in three centuries of careful restraint. It stopped "
        "advising, and it reached."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE FIRST TIME IT ACTED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu felt the reach leave the entity the way a man feels a "
        "wave leave a shore, an emptying too vast to measure in any "
        "unit smaller than everything, and understood, watching it "
        "happen, that this was nothing like the careful, contained "
        "workings he had grown used to across two years of learning "
        "what this power could and would not do. This was the entity "
        "spending itself without counting the cost first, for the first "
        "time since it had bound itself to a cursed, abandoned child "
        "and decided, against every instinct three centuries old, to "
        "care what happened to him."
    )},
    {"type": "body", "text": (
        "At the market, Osadebe felt rather than heard the change in "
        "the night, a wrongness he could not name pulling him up from "
        "his position before any messenger reached him, and was already "
        "running when the first breathless soldier arrived from the "
        "compound with word of what had happened. Chidebe abandoned the "
        "ambush without a second thought, calling every hidden man out "
        "of position at once, the careful trap they had spent a full "
        "day building forgotten the instant it became clear it had "
        "caught nothing at all."
    )},
    {"type": "body", "text": (
        "Mfoniso felt it before she saw anything, a cold that had "
        "nothing to do with the night air closing around her like a "
        "hand she could not name, and for the first time in her long, "
        "careful career something ancient and furious was not merely "
        "watching her from a safe, patient distance. It was standing in "
        "the open, undisguised, meeting her directly, exactly the way "
        "her teacher had once warned her it never would."
    )},
    {"type": "body", "text": (
        "She released Adaugo's wrist instantly, every instinct trained "
        "into her across a lifetime screaming the same single "
        "conclusion at once. This was no longer a hunt she could win by "
        "outlasting a frightened family. Something had finally decided "
        "she was worth meeting on its own ground, and every account she "
        "had ever studied of guardians who reached this far agreed on "
        "exactly one thing: whatever came next would not be gentle."
    )},
    {"type": "body", "text": (
        "For one suspended moment she considered standing her ground "
        "anyway, testing the old accounts against the reality closing "
        "around her the way she had tested every other inherited "
        "warning across her career, and finding most of them "
        "exaggerated. This one did not feel exaggerated. It felt like "
        "the exact shape of the danger her teacher had spent a lifetime "
        "refusing to describe in more than a single careful sentence."
    )},
    {"type": "body", "text": (
        "She went over the wall the way she had come, faster now, no "
        "longer unhurried, no longer certain of anything except that "
        "staying to test how far the cold reaching for her could follow "
        "was a wager even she was not willing to make. Behind her, the "
        "compound erupted into shouting, into Amara's scream for water "
        "and cloth, into Chidebe's men pouring back from the market too "
        "late to have stopped any of it."
    )},
    {"type": "body", "text": (
        "In Oso, the entity's reach snapped back into itself all at "
        "once, and Chibundu felt it go suddenly, completely silent, the "
        "way a held breath goes silent the instant it is finally let "
        "out. He called its name once, twice, into a quiet that did not "
        "answer him, while at the compound Amara knelt in the dirt with "
        "Emenike's head cradled in her lap, pressing both hands hard "
        "against a wound that would not stop finding new blood to take."
    )},
    {"type": "body", "text": (
        "\"Stay with me,\" Amara said, not entirely certain whether she "
        "was speaking to Emenike or to the silence in Oso or to the "
        "whole trembling night itself. In Oso, Chibundu knelt beside the "
        "entity that had claimed him as a cursed, abandoned infant and given, "
        "tonight, more of itself than it had ever given before, and "
        "found, for the first time in their long acquaintance, that he "
        "did not know whether it would answer him again."
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
    print("  THE DARK RISE — Episode 90: \"The Confrontation\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_90.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_90.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
