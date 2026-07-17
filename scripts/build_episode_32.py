#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 32: "The Old Records"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-08: Episode 32 follows Eze Amadi as he searches for
precedent before committing to a decision. He summons Nkiruka, keeper of
the crown's oldest rites and records, a position more ceremonial than
consulted in living memory, and learns that his grandmother's half
remembered story was not the only account of its kind in the kingdom's
long history. The old records do not explain what waits at Oso. They
only confirm that something like it has been encountered before, always
briefly, always ending in silence rather than resolution. In Oso, the
entity continues its patient work, unaware of exactly how far its
message has already traveled through Udo's oldest memory. Eze Amadi
settles on a measured path: no soldiers, no public declaration, but a
permanent crown presence attached to Idoro, with Osadebe placed there to
watch and report. The episode ends with Nkiruka offering one piece of
old counsel the king did not ask for, and cannot quite dismiss.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_32.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Two"},
    {"type": "title_ep_name", "text": "The Old Records"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: UDO — WHAT NKIRUKA WAS ASKED TO FIND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Nkiruka had held the title of keeper of the old rites for "
        "eleven years without once being summoned for anything beyond "
        "the ceremonial blessings a new season or a royal birth "
        "required, and she arrived at the private summons with the "
        "particular wariness of a woman whose position had quietly "
        "become more decoration than duty."
    )},
    {"type": "body", "text": (
        "\"I am told this concerns something old,\" she said, once Eze "
        "Amadi had dismissed everyone else from the room. \"Older than "
        "trade disputes and provincial taxes, at any rate.\""
    )},
    {"type": "body", "text": (
        "\"Older than this kingdom, possibly,\" the king said. \"I "
        "want to know if the crown's own memory holds anything about a "
        "presence that lives beneath a forest, claims abandoned "
        "children, and grows strong enough, given time, to speak "
        "directly into the minds of grown men without any mouth to "
        "carry the words.\""
    )},
    {"type": "body", "text": (
        "He told her the whole of it, plainly, the way he had decided "
        "he would tell anyone whose counsel he genuinely needed rather "
        "than merely wanted to hear agree with him. Idoro. The dibia. "
        "The elder marked by her own hand. Osadebe standing at a "
        "forest's edge with a mother and her husband, hearing a voice "
        "address them all at once. He watched Nkiruka's face carefully "
        "as he spoke, the way he had once watched Osadebe's, searching "
        "for the particular flicker that told him whether he was "
        "delivering news or merely confirming something already half "
        "suspected."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Nkiruka was quiet for a long moment, and something in her "
        "face told Amadi, before she spoke again, that his question had "
        "not surprised her nearly as much as he had expected it to."
    )},
    {"type": "body", "text": (
        "\"There are three accounts in the oldest scrolls,\" she said "
        "finally. \"Each from a different reign, each separated from "
        "the others by more than a hundred years. Each describes "
        "something that sounds very much like what you have just "
        "described to me. None of them end with the presence explained, "
        "defeated, or bargained with successfully. They end, every "
        "time, with the presence simply going quiet again, for reasons "
        "the records never manage to name.\""
    )},
    {"type": "body", "text": (
        "\"How were they written,\" the king asked. \"As certainty, or "
        "as rumor a frightened scribe felt obligated to record and "
        "hoped no one would ever ask him to defend.\""
    )},
    {"type": "body", "text": (
        "\"The first, I would call rumor,\" Nkiruka said. \"Secondhand, "
        "uncertain, the kind of account a careful reader learns to "
        "discount by half. The second is more troubling. It was "
        "recorded by a royal physician sent to examine a possessed "
        "healer much the way your captain examined this village's "
        "dibia, and the physician's own account reads exactly like a "
        "man trying, and failing, to explain away something he had "
        "personally witnessed with his own eyes. The third account is "
        "the most troubling of all, because it was written by a king's "
        "hand directly, and kings, in my experience, rarely commit "
        "their own fear to permanent record unless the fear has already "
        "proven itself impossible to dismiss.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE RECORDS COULD NOT YET REACH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had no awareness at all "
        "that its own long history, three separate encounters spread "
        "across more than three centuries of this kingdom's memory, had "
        "just been read aloud in a private chamber a hundred miles "
        "north."
    )},
    {"type": "body", "text": (
        "It would not have been surprised to learn of the records, had "
        "it known. It remembered every one of those earlier encounters "
        "itself, filed away in the same patient accounting it kept of "
        "everything it had ever touched, three separate moments across "
        "three separate centuries when a human authority had come "
        "close enough to notice it and had, each time, eventually "
        "decided the wiser course was distance rather than confrontation. "
        "It had learned to expect that outcome by now. Kingdoms, like "
        "villages, eventually chose the same caution once they "
        "understood the true shape of the cost involved in choosing "
        "otherwise."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel had begun, in these last days, "
        "asking his first real questions, small halting sentences built "
        "from the words he had gathered so far, testing what answers "
        "the patient presence around him was willing to give and which "
        "ones it still withheld. The entity answered some honestly. It "
        "answered others the way it had answered the question at the "
        "boundary weeks earlier, with just enough truth to satisfy a "
        "small mind not yet ready for the whole of it."
    )},
    {"type": "body", "text": (
        "Why do the trees stay so close, the boy had asked, in his own "
        "halting words, only the day before, and the entity had told "
        "him the trees stayed close because they loved him, which was "
        "not quite a lie and not quite the whole shape of the truth "
        "either. The roots kept him because they had been asked to, in "
        "the oldest sense the entity understood asking, and because a "
        "vessel worth the centuries of care already spent on him was "
        "not a thing to be left loose and unwatched before he was ready "
        "for whatever came after this slow, careful shaping finally "
        "finished."
    )},
    {"type": "body", "text": (
        "It found, turning its own answer over afterward, that it was "
        "growing less comfortable than it had once been with the small "
        "gaps it kept leaving in every truth it offered him. That "
        "discomfort was new. It did not yet know what to do with it, "
        "only that it was there, the way a stone in a shoe is there "
        "long before a walker finally stops to ask what has been "
        "bothering his stride."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "It did not know, and had no way yet of knowing, that its own "
        "long silence toward the crown had just been reclassified, in "
        "a private chamber a hundred miles away, from an absence of "
        "danger into a pattern still actively unfolding."
    )},

    {"type": "body", "text": (
        "The cold voice consulted its oldest pages and spoke."
    )},
    {"type": "system", "text": "Historical pattern confirmed, unknown to subject: three prior human authority encounters across three centuries, all resolved through distance. Vessel: first independent questions observed."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: UDO — WHAT THE KING DECIDED, AND WHAT HE WAS TOLD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"If it has always gone quiet again on its own,\" Eze Amadi "
        "said, \"perhaps the wisest course is the one every king before "
        "me apparently chose. Distance. Patience. Let it tire of "
        "whatever it wants and withdraw the way it withdrew three times "
        "before.\""
    )},
    {"type": "body", "text": (
        "\"Perhaps,\" Nkiruka said. \"Though I would ask you to notice "
        "something the records themselves seem to have missed, or did "
        "not think worth writing down. Each account grows more direct "
        "than the one before it. The first speaks of villagers going "
        "missing near a cursed grove. The second speaks of a healer "
        "possessed for a season before the possession simply stopped. "
        "The third, the one closest to your grandmother's lifetime, "
        "speaks of a voice heard by more than one person at once, much "
        "the way your own captain describes hearing it. Whatever this "
        "is, it does not appear to be repeating the same small pattern "
        "each time it wakes. It appears to be growing bolder with "
        "practice.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Eze Amadi absorbed that in silence, the particular stillness "
        "of a ruler recalculating a decision he had believed, only "
        "moments earlier, was already settled."
    )},
    {"type": "body", "text": (
        "\"Bolder how,\" he asked. \"Bolder in what it takes, or "
        "bolder in what it is willing to be seen doing.\""
    )},
    {"type": "body", "text": (
        "\"The second, I believe,\" Nkiruka said. \"Nothing in these "
        "records suggests it has ever needed to grow more powerful "
        "than it already was. Only more willing to let itself be "
        "known. That is not the same danger as an army massing at a "
        "border, my king, but I would not call it a smaller one "
        "either. A thing patient enough to wait three hundred years "
        "before deciding it wished to be believed is a thing that has "
        "already decided something else as well, something none of "
        "these old scrolls ever managed to record before its author's "
        "reign ended.\""
    )},

    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "\"Then I will not simply wait and hope this cycle repeats "
        "itself kindly,\" he said. \"I will send no army. I will make "
        "no public declaration that might cost me the trade Ejikeme is "
        "so afraid of losing. But I will not treat this as a matter "
        "that resolves itself either. Osadebe remains attached to "
        "Idoro, permanently, watching and reporting, until we "
        "understand this well enough to know whether patience is truly "
        "the wisest answer or simply the most comfortable one.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Nkiruka bowed to leave, and paused at the door, offering one "
        "final piece of counsel the king had not asked for."
    )},
    {"type": "body", "text": (
        "\"You asked what the records say about the presence itself,\" "
        "she said. \"You did not ask what they say about the children "
        "it claims. I would ask you to consider that question before "
        "this grows any older, my king. In every account I have read, "
        "the presence was never the whole of the danger. It was only "
        "ever the hand that shaped what came after it, and it is what "
        "comes after that no record has ever survived long enough to "
        "describe in full.\""
    )},
    {"type": "body", "text": (
        "She left him alone with that thought, and Eze Amadi sat a "
        "long while in the quiet of his own chamber, turning her final "
        "words over with the same unease he had carried since the "
        "morning Ikwuano first brought him a frightened village's "
        "story, no longer entirely certain which part of this "
        "unfolding danger deserved his deepest caution."
    )},
    {"type": "body", "text": (
        "He thought of the child described in Osadebe's report, alive "
        "somewhere beneath that same patient forest, being shaped by "
        "hands that were not human into something none of the old "
        "records had ever managed to name plainly. A king learned, "
        "across enough years on a throne, to weigh threats by the "
        "armies and the coin behind them. He found himself, that night, "
        "trying and failing to weigh a threat that might simply be a "
        "small child, and finding no ledger anywhere in his long "
        "experience equipped to hold that particular number honestly."
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
    print("  THE DARK RISE — Episode 32: \"The Old Records\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_32.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_32.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
