#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 71: "The Morning After"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-16: Episode 71 opens the new ten episode block in the
exhausted daylight after Episode 70's near disaster. Chidebe walks
back through exactly how his watch failed, and understands for the
first time that the sound in the tree line was not chance but a
deliberate distraction, meaning Mfoniso can misdirect a trained
soldier's attention from a distance without ever being seen doing it.
Word of the attempt spreads through Idoro by midday despite no
official announcement, and the council convenes to decide how much of
the truth the wider village should be told. At Amara's compound, Obi
raises the hardest question of all: whether the family should leave
Idoro rather than keep gambling Kene's life on watches and old powers
that came within a held breath of failing.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_71.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy One"},
    {"type": "title_ep_name", "text": "The Morning After"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE SOUND THAT WAS NEVER CHANCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe walked the young soldier back through the whole "
        "night a second time at dawn, patient rather than angry, "
        "unwilling to waste a lesson this costly on a man too "
        "frightened of punishment to think clearly. \"Tell me again "
        "exactly what you heard,\" he said. \"Not what you assumed it "
        "was. What you actually heard.\""
    )},
    {"type": "body", "text": (
        "\"A branch breaking,\" the soldier said. \"Once, off toward "
        "the tree line, the kind of sound a stray animal makes at "
        "night. It did not repeat. I turned to look because a sound "
        "that does not repeat is usually nothing. I have turned "
        "toward a hundred sounds exactly like it and found nothing "
        "every time before last night.\""
    )},
    {"type": "body", "text": (
        "Chidebe absorbed that with the particular stillness of a man "
        "recalculating an enemy's whole method from a single new "
        "fact. \"It was not nothing this time,\" he said. \"And I no "
        "longer believe it was chance either. She needed exactly ten "
        "breaths of your attention elsewhere, and she produced exactly "
        "the kind of sound a trained soldier learns to dismiss rather "
        "than investigate. That is not luck. That is someone who has "
        "studied how soldiers are trained to think.\""
    )},
    {"type": "body", "text": (
        "He carried the realization to Osadebe's empty hut out of "
        "old habit before remembering the captain was still weeks from "
        "Udo, and stood a moment in the doorway feeling the absence "
        "more sharply than he had allowed himself to since the "
        "summons first came. Whatever came next, he would meet it "
        "without the one voice in Idoro most practiced at turning "
        "chaos into a plan."
    )},
    {"type": "body", "text": (
        "He found Zara next, not to question her further but to "
        "thank her plainly, a courtesy he suspected she had not "
        "received nearly often enough for a gift this costly to keep "
        "giving. \"You saved him,\" he said. \"Not the presence. You. "
        "None of us would have known to run if you had not screamed "
        "first.\" Zara accepted the thanks with a tired, uncertain "
        "nod, still turning over the particular exhaustion of a body "
        "that had spent three nights now being asked to feel danger "
        "before anyone else could."
    )},
    {"type": "body", "text": (
        "\"I do not know how many more times I can feel it before it "
        "stops leaving me any warning at all,\" she admitted. \"Each "
        "time it has come faster, and closer, and cost me more to "
        "recover from. I do not know what happens the time it decides "
        "not to give me even the little warning it has given me so "
        "far.\" Chidebe had no honest comfort to offer that fear, and "
        "did not insult her by pretending otherwise."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A VILLAGE THAT ALREADY KNEW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "No one had announced the night's events by midday, and by "
        "midday Idoro already knew regardless, the way a village "
        "always eventually learns exactly the thing its leaders hoped "
        "to control the telling of. Amara felt the market's stares "
        "differently that afternoon, not the old fear that once "
        "followed Kene's brother's name, but something rawer and more "
        "immediate: the particular horror of neighbors imagining their "
        "own children in his place."
    )},
    {"type": "body", "text": (
        "The council convened before evening, smaller and quicker "
        "than its usual sessions, everyone present understanding there "
        "was little left to debate about whether the danger was real. "
        "\"The question is not whether to tell the village,\" Elder Maka "
        "said. \"The village has already told itself. The question is "
        "whether we let the story arrive as rumor, growing wilder with "
        "every retelling, or whether we shape it into something "
        "closer to the truth before it finishes shaping itself.\""
    )},
    {"type": "body", "text": (
        "Ozoemena, quieter than usual, offered the one piece of "
        "practical wisdom his own long fall had taught him better than "
        "anyone else in the circle. \"Tell them enough that they stop "
        "inventing the rest,\" he said. \"Not everything. Enough. I "
        "learned the difference between those two choices at a cost I "
        "do not wish repeated on anyone else's account.\""
    )},
    {"type": "body", "text": (
        "Amara, given a seat in the circle by right of what her own "
        "family had just survived, argued for slightly more honesty "
        "than the others seemed inclined to offer. \"Tell them enough "
        "to trust us with their own children too,\" she said. \"A "
        "stranger walked our market once already unnoticed. If she or "
        "another comes again, I would rather every mother in Idoro "
        "already know to watch for a quiet traveler buying cloth than "
        "learn it only after losing someone the way we nearly lost "
        "Kene.\""
    )},
    {"type": "body", "text": (
        "The council settled, in the end, on a plain account read "
        "aloud at the mango tree the next morning: a stranger had "
        "entered the market, a child had been threatened in the night, "
        "and the old powers guarding Idoro had answered in time. No "
        "names. No mention of the presence reaching further than it "
        "ever had, or of exactly how close the margin had truly been. "
        "Enough, Chidebe judged, reviewing the wording twice, to settle "
        "the wilder rumors without handing a returning enemy anything "
        "further to work with, and enough, Amara insisted successfully, "
        "to put every parent in Idoro on the same watch her own family "
        "now kept."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: A DIFFERENT KIND OF TRAINING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, Chibundu turned Chidebe's realization over with the "
        "entity that evening, unable to shake the discomfort of a "
        "danger that had studied soldiers well enough to know exactly "
        "which sounds they would dismiss. \"We have spent this whole "
        "season training me to control force,\" he said. \"Restraint. "
        "Patience. I do not think either of those things would have "
        "helped Kene last night. What good is any of it against "
        "someone who does not need to fight anyone at all.\""
    )},
    {"type": "body", "text": (
        "\"None,\" the entity admitted. \"Which means we have been "
        "training for the wrong danger, or at least an incomplete "
        "one. Force answers force. It does not answer patience aimed "
        "at the exact seams no one else has thought to guard. I do "
        "not yet know what training answers that instead, and I do "
        "not intend to pretend to you that I do until I have actually "
        "found it.\""
    )},
    {"type": "body", "text": (
        "Chibundu considered that, turning over the whole shape of "
        "the last several days. \"Then maybe the answer is not more "
        "training for me at all,\" he said. \"Maybe it is simply more "
        "honesty, faster, between everyone this danger could reach. "
        "Zara felt it because she was willing to say so immediately. "
        "Chidebe caught the pattern because his soldier admitted the "
        "lapse instead of hiding it. This whole family has learned, "
        "one hard lesson at a time, that speed and honesty might be "
        "the only defense a patience like hers cannot easily plan "
        "around.\""
    )},
    {"type": "body", "text": (
        "The entity felt something close to pride move through it, "
        "watching the boy arrive at a conclusion it had not handed "
        "him. \"That may be the truest thing either of us has said "
        "about this danger yet,\" it said. \"I only hope it proves "
        "enough, the next time patience decides it is done waiting.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: THE QUESTION OBI FINALLY ASKED ALOUD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "That night, once Kene was finally asleep again and the "
        "compound had gone quiet, Obi asked Amara the question he had "
        "been turning over silently since the moment he found their "
        "son's bed empty. \"Should we leave,\" he said. \"Not Idoro "
        "forever. Just far enough that whatever hunts Chibundu has to "
        "work considerably harder to reach the rest of us.\""
    )},
    {"type": "body", "text": (
        "Amara felt the question land with the full weight of "
        "everything it was actually asking. \"And go where,\" she "
        "said. \"A stranger crossed a continent to stand in our own "
        "market unnoticed. I do not believe there is a village far "
        "enough away that patience like that could not eventually "
        "find it, if it decided the distance was worth spending on "
        "us.\""
    )},
    {"type": "body", "text": (
        "\"Then what do we actually have,\" Obi asked, \"that a hunter "
        "this patient cannot eventually plan around.\""
    )},
    {"type": "body", "text": (
        "Amara did not have a clean answer, and did not pretend to "
        "one. \"I do not know,\" she said. \"I know only that running "
        "gave Zara nothing, all those years ago, and staying and "
        "fighting has cost this family more than either of us ever "
        "wanted to pay. I do not think there is a door left in front "
        "of us that does not cost something. I would rather choose "
        "which cost, together, than let fear choose it for us in the "
        "middle of another night like the last one.\""
    )},
    {"type": "body", "text": (
        "Obi took her hand, and they sat together a long while in the "
        "dark, neither one certain of the answer, both understanding "
        "that whatever they decided, it would have to be decided soon, "
        "before patience this deep found a second night as quiet as "
        "the last one had almost been."
    )},
    {"type": "body", "text": (
        "\"I do not want to raise our sons deciding safety by how far "
        "we can run,\" Amara said eventually, breaking the long "
        "silence between them. \"I want to raise them deciding it by "
        "how honestly the people around them speak, and how quickly. "
        "That is not a wall. I know that. It is the only thing I have "
        "ever actually watched work, across a whole season of far "
        "worse nights than this one.\""
    )},
    {"type": "body", "text": (
        "Obi held that a long moment before answering, and when he "
        "did, some of the tightness finally eased out of his own "
        "shoulders. \"Then we stay,\" he said, \"and we keep choosing "
        "honesty over distance, the same way we have chosen it every "
        "other time this family has been tested. I would rather fail "
        "trying that than succeed at running and still wonder, every "
        "single night afterward, whether it had actually bought us "
        "anything at all.\""
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
    print("  THE DARK RISE — Episode 71: \"The Morning After\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_71.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_71.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
