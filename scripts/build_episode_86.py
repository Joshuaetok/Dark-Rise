#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 86: "The False Patrol"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-01: Episode 86 executes the test Chidebe and Osadebe
designed at the end of Episode 85. They split the six-name shortlist
into small, isolated groups and give each a different false patrol
detail, telling no one it is a test. Chidebe struggles openly with
including Emenike, the soldier he trusts most. Over two tense days
most of the false details go nowhere, but one, given only to Emenike's
small group, draws Mfoniso to a specific fabricated location. That
night, Osadebe and Chidebe follow Emenike in secret rather than confront
him outright, and the episode closes as they watch him slip away from
his post toward the market's edge in the dark, exactly where the drop
point is believed to be, moments before he reaches it.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_86.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Six"},
    {"type": "title_ep_name", "text": "The False Patrol"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: SIX LIES, TOLD SEPARATELY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe built the test the way he built everything that "
        "mattered, in silence, alone, before he trusted himself to say "
        "it aloud to anyone else. Six names. Six small groups, no group "
        "larger than two men, each told a different route, a different "
        "hour, a different fabricated stretch of ground that Idoro's "
        "patrols would never actually walk. No man would know he was "
        "being tested. No man would know any group existed but his own."
    )},
    {"type": "body", "text": (
        "\"If only one man from a group is questioned, we learn "
        "nothing,\" Osadebe said, watching Chidebe divide the names on "
        "the hide map. \"If a false detail reaches her, we learn "
        "exactly which door it walked through.\" Chidebe did not answer "
        "right away. He was looking at one name in particular, set apart "
        "from the others with a smaller mark only he would recognize."
    )},
    {"type": "body", "text": (
        "\"I am putting Emenike with Adaeku,\" he said finally, naming "
        "the quietest of the six, a man barely spoken to outside his own "
        "watch. \"A route that does not exist, along the old grain path "
        "past the second well, timed for tomorrow's last light. If "
        "nothing comes of it, I will have doubted the best soldier I "
        "own for nothing, and I will live with that gladly. It is a "
        "small price, set beside what it costs to be wrong the other "
        "way.\""
    )},
    {"type": "body", "text": (
        "Osadebe did not offer comfort, because he had none honest to "
        "give. \"And if something does come of it,\" he said instead, "
        "\"we will both live with the other thing.\" Chidebe folded the "
        "hide map without answering, and the two men separated to carry "
        "six different lies to six different corners of the compound "
        "before the sun was fully up."
    )},
    {"type": "body", "text": (
        "Amara found Chidebe before he left to deliver his share of the "
        "false routes and asked the question plainly, the way she asked "
        "every hard question now. \"You are going to lie to six of your "
        "own soldiers,\" she said. \"Men who trust you completely.\" "
        "Chidebe did not try to make it sound gentler than it was. \"Five "
        "of them will never know it happened,\" he said. \"The sixth "
        "already betrayed a trust larger than the one I am about to "
        "bend. I have made my peace with which lie costs more.\""
    )},
    {"type": "body", "text": (
        "She did not argue with him, though the look she gave him "
        "carried the weight of a woman who understood exactly how thin "
        "the line was between protecting a house and quietly becoming "
        "the kind of person who lies to the people inside it. \"Find "
        "the truth,\" she said finally. \"Quickly. I do not want this "
        "kind of watching to become how we do things here.\" Chidebe "
        "promised her it would not, and meant it, and hoped he would "
        "still mean it after tonight."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT TWO DAYS OF WAITING COST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The first day produced nothing at all from five of the six "
        "false routes, which told Chidebe only that five men, whatever "
        "else might be true of them, had not passed a single word "
        "beyond the ones he had given them. He found himself relieved "
        "and unsatisfied in equal measure, no closer to an answer, only "
        "closer to running out of names to doubt."
    )},
    {"type": "body", "text": (
        "The compound tried, in the meantime, to hold onto something "
        "resembling an ordinary day. Adaugo sat with Elder Maka through "
        "another lesson on the old rites, though her attention kept "
        "drifting toward the gate every time a soldier passed it, and "
        "Elder Maka did not scold her for the distraction, only asked "
        "gently what frightened her more, a hunter she had already met "
        "or a stranger she had not yet found. Adaugo did not have an "
        "answer, and Elder Maka told her that not having one was itself "
        "an honest place to start."
    )},
    {"type": "body", "text": (
        "Kene, too young to be told the shape of what his parents were "
        "waiting for, noticed only that his mother kept glancing toward "
        "the market road more than usual, and asked her once, without "
        "prompting, whether the bad woman had a friend. Amara knelt to "
        "answer him honestly, the way she had promised herself she "
        "always would. \"We do not know yet,\" she said. \"But we are "
        "trying very hard to find out, so that no one else has to be "
        "afraid of a friend they cannot see.\""
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the strange, taut patience radiating from "
        "the compound and asked the entity what it made of a household "
        "that had turned itself into its own trap. \"It is not without "
        "precedent,\" the entity said. \"Guardians have done worse to "
        "their own people, chasing a leak that turned out to be nothing "
        "more than bad luck dressed as betrayal. I hope, for their sake, "
        "this is not that.\" The presence, listening from further away "
        "than usual, offered only a single unsettled thought of its own. "
        "\"A test like this can catch the guilty,\" it said. \"It can "
        "also break the innocent who only look guilty for a day.\""
    )},
    {"type": "body", "text": (
        "By the second evening, word reached Chidebe through a soldier "
        "posted near the old grain path that fresh signs had appeared "
        "exactly where the fabricated route claimed a patrol would "
        "stand at last light, ground disturbed in the particular way "
        "Idoro's watchers had learned to recognize over the last several "
        "days. Nowhere else. No other false route had drawn so much as "
        "a bent blade of grass."
    )},
    {"type": "body", "text": (
        "Osadebe walked the grain path himself before bringing the "
        "report to Chidebe, unwilling to trust a fact this heavy to "
        "another man's eyes alone. The marks were plain once he knew "
        "where to look, a single set of footprints crossing the "
        "fabricated route at the exact hour it supposedly existed, then "
        "vanishing back toward the tree line with the same unhurried "
        "confidence Mfoniso had shown at the third bend. There was no "
        "mistaking it for anything else."
    )},
    {"type": "body", "text": (
        "Chidebe stood with the report in his hand for a long time "
        "before he could make himself walk it to Osadebe, and when he "
        "did, his voice came out steadier than he felt. \"Only one lie "
        "answered,\" he said. \"Emenike and Adaeku's. Two men. I need it "
        "to be Adaeku. I have known Emenike since he was a boy begging "
        "at my gate to be given a chance.\" Osadebe put a hand briefly "
        "on his shoulder, an unusual gesture for a man who rarely "
        "offered one. \"Wanting it to be someone else does not make it "
        "so,\" he said gently. \"But it does not make it Emenike either. "
        "Not yet. We watch both, tonight, and let the watching decide "
        "it instead of our fear.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE WATCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They followed both men that night without either soldier "
        "knowing it, Osadebe trailing Adaeku's quiet walk home to a hut "
        "at the far edge of the compound, where he ate a plain meal "
        "alone and slept without incident, watched the whole while by a "
        "man who found himself, despite everything, hoping the trail "
        "led nowhere."
    )},
    {"type": "body", "text": (
        "Chidebe took Emenike, telling himself he was simply walking the "
        "same evening route he always walked, though both men knew, "
        "without saying it, that nothing about tonight was ordinary. "
        "Emenike finished his watch on time, spoke to the relief soldier "
        "with his usual quiet courtesy, and turned, as he always did, "
        "toward the soldiers' quarters near the gate."
    )},
    {"type": "body", "text": (
        "For a long stretch nothing happened at all, and Chidebe let "
        "himself hope, standing in the shadow of a storage hut with his "
        "back pressed to cool mud brick, that the report from the grain "
        "path had meant something else entirely, some coincidence he "
        "had not yet imagined, anything other than the answer he had "
        "spent two days dreading. Emenike walked slowly, unhurried, a "
        "tired soldier heading toward a well earned bed like any other "
        "night in years of nights just like it."
    )},
    {"type": "body", "text": (
        "Then, a hundred paces short of his own bed, he stopped, looked "
        "once around him in the dark with the practiced care of a man "
        "checking whether he was alone, and turned instead toward the "
        "market road, walking quickly now, no longer a soldier finishing "
        "an ordinary night but a man moving with clear purpose toward a "
        "place he had no honest reason to be."
    )},
    {"type": "body", "text": (
        "Chidebe followed at a distance that felt at once too close and "
        "nowhere near close enough, his own heartbeat loud in his ears, "
        "every step forward a small and terrible confirmation of "
        "something he had spent two days praying would not be true. He "
        "thought, absurdly, of the boy who had once stood at his gate "
        "three separate times asking only for the chance to be useful, "
        "and wondered when exactly that boy had learned to move through "
        "darkness this carefully, this quietly, as though he had "
        "practiced it a hundred times before tonight."
    )},
    {"type": "body", "text": (
        "Ahead of him in the dark, Emenike slowed near the market's "
        "edge, glanced back once toward the compound he had just left, "
        "and began closing the last distance toward the place Chidebe "
        "now understood, with a certainty that felt like a wound "
        "opening, could only be the drop point itself."
    )},
    {"type": "body", "text": (
        "Chidebe stopped walking. Whatever he did in the next few "
        "steps, he understood, could not be undone, and for one brief, "
        "aching moment he let himself wish he had never agreed to build "
        "the test at all, before he made himself move forward anyway, "
        "toward whatever truth was waiting for him at the edge of the "
        "market."
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
    print("  THE DARK RISE — Episode 86: \"The False Patrol\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_86.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_86.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
