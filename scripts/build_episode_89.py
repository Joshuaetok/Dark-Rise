#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 89: "A Trap With No Leak Left"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-04: Episode 89 resolves Episode 88's two-night
deadline. The council decides against forging a message in Emenike's
hand, judging Mfoniso too skilled a reader of deception to fool safely,
and chooses instead to let the drop stone stay empty for the first time
in two seasons, while Chidebe and Osadebe quietly ring the market's
edge with hidden soldiers, betting Mfoniso will come herself to learn
why her informant went silent. The household spends the tense hours
before the deadline preparing in every way it can, while Emenike,
watched but no longer bound, is allowed to help plan the one detail
that might keep his sister safe regardless of what happens to him. The
episode closes on Mfoniso's own side: two seasons of perfect
reliability breaking without warning reads to her not as chance but as
proof her informant is compromised, and rather than walk into unknown
ground to investigate, she decides the household's silence is itself
enough reason to strike directly and immediately, bypassing the drop
point trap laid for her entirely.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_89.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Nine"},
    {"type": "title_ep_name", "text": "A Trap With No Leak Left"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE STONE STAYS EMPTY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe raised the idea first, and hated it even as he said it "
        "aloud. \"We could write something in his hand,\" he said. "
        "\"Lure her to a place of our choosing instead of hers.\" "
        "Emenike, still watched but no longer bound, shook his head "
        "before anyone else could answer. \"She has read my hand for two "
        "seasons,\" he said. \"She will know a false word from a true "
        "one faster than any of us can practice hiding it. You would be "
        "handing her the proof that something has changed, wrapped in a "
        "ribbon.\""
    )},
    {"type": "body", "text": (
        "Osadebe agreed, reluctantly. \"A forged message risks more "
        "than an empty stone,\" he said. \"An empty stone is only "
        "silence. She has to guess what silence means. A bad forgery "
        "tells her exactly what happened and exactly who did it.\" Elder "
        "Maka nodded slowly, the decision settling into place. \"Then we "
        "give her silence,\" she said, \"and we make certain silence is "
        "the last thing she is ever comfortable walking toward again.\""
    )},
    {"type": "body", "text": (
        "Obi asked the question no one else had wanted to be the one to "
        "raise. \"And if she does not come at all,\" he said. \"If she "
        "simply vanishes into that country west of us and we never see "
        "her again.\" Elder Maka considered that honestly rather than "
        "offering comfort she did not feel. \"Then we have lost a "
        "chance,\" she said, \"but we have not lost more than we already "
        "stood to lose by waiting. A hunter who disappears rather than "
        "risk discovery is still a hunter who no longer trusts this "
        "ground. That is not nothing.\""
    )},
    {"type": "body", "text": (
        "Ozoemena, listening from the edge of the gathering, offered "
        "the plainest objection of all. \"We are placing a great deal "
        "of faith in guessing correctly what a woman we have never truly "
        "understood will do with a silence she has never before been "
        "given,\" he said. No one disputed it, because no one could. It "
        "was, Amara admitted quietly, the truest sentence spoken all "
        "day."
    )},
    {"type": "body", "text": (
        "The plan took its final shape by midday. No message. No token. "
        "The stone would sit exactly as it always had, undisturbed, "
        "while Chidebe's soldiers took up hidden positions around the "
        "market's edge, patient and unseen, on the theory that a hunter "
        "this careful would not simply vanish over one missed contact "
        "without first coming to learn why."
    )},
    {"type": "body", "text": (
        "Amara sat with Emenike through the afternoon exactly as Elder "
        "Maka had asked, learning every remaining detail of two seasons "
        "of coercion, and found herself, despite everything, grateful "
        "for his help rather than merely tolerant of it. \"If this works "
        "and she is taken,\" Amara told him carefully, \"it does not "
        "guarantee your sister's safety. Whoever holds her may not learn "
        "what happened here for days, if ever.\" Emenike understood that "
        "already, plainly, and helped anyway, because helping was the "
        "only thing left he had any power to do."
    )},
    {"type": "body", "text": (
        "Kene, sensing only that the compound had grown strange and "
        "quiet in a way he did not have words for, spent the afternoon "
        "close to Zara instead of at his usual games, drawing another "
        "unbidden spiral in the dirt beside her without seeming to "
        "notice he had done it. Zara watched his small hand trace the "
        "familiar shape and felt an old unease she could not name "
        "settle over the rest of her preparations for the evening ahead."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE RING AROUND THE MARKET
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe walked the market's edge himself before dusk, choosing "
        "each hiding place with the same care he had once given the "
        "false patrol routes, mindful that a woman who could vanish "
        "from Osadebe's pursuit without a trail would not be caught by "
        "carelessness now. Soldiers took shuttered stalls, rooftops, the "
        "shadowed gap between two storage huts, each of them briefed "
        "only on their own small piece of the ring rather than the "
        "whole shape of it."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the tension radiating from the compound "
        "sharpen into something almost unbearable, and asked the entity "
        "whether it could sense anything of the woman they were waiting "
        "for. \"Nothing,\" the entity admitted. \"I have never once "
        "sensed her coming. I do not expect tonight to be different.\" "
        "The presence, still recovering, offered only a single warning "
        "before falling quiet again. \"A trap built around silence "
        "assumes the other side reads silence the way you do,\" it "
        "said. \"Do not assume that. Ever.\""
    )},
    {"type": "body", "text": (
        "Chidebe briefed each small group with only the details that "
        "group needed, a habit carried over from the false patrol test "
        "that no one questioned anymore. If Mfoniso somehow turned the "
        "tables and found a way to compromise the ambush itself, he "
        "reasoned, no single captured man should be able to hand her "
        "the whole shape of it."
    )},
    {"type": "body", "text": (
        "Osadebe took the position nearest the stone itself, unwilling "
        "to trust the moment of confirmation to anyone who had not "
        "already seen Mfoniso's face twice and lived. He settled into "
        "the dark with the particular stillness of a man who had spent "
        "two seasons of failed pursuits learning exactly how much "
        "patience this hunt required, and made himself a promise not to "
        "move a fraction before he was certain."
    )},
    {"type": "body", "text": (
        "The evening stretched long and silent, the ordinary sounds of "
        "a market closing for the night giving way, hour by hour, to "
        "the deeper quiet of a village that did not know a trap had "
        "been laid inside it. Chidebe checked each hidden position "
        "twice, found every man exactly where he had left him, and "
        "allowed himself, briefly, to believe the plan might actually "
        "work exactly as designed. Somewhere beyond the stalls a dog "
        "barked twice and went quiet, and every hidden man tightened "
        "and then eased again, one breath at a time."
    )},
    {"type": "body", "text": (
        "Adaugo sat with Elder Maka near the compound rather than the "
        "market, forbidden from anywhere close to the ambush itself, and "
        "found the waiting almost harder than danger she could see "
        "directly. \"What do we do if it works,\" she asked quietly. "
        "\"If they truly catch her.\" Elder Maka did not have a tidy "
        "answer. \"We ask her the questions three seasons of chasing her "
        "shadow never let us ask,\" she said. \"And we hope she is more "
        "willing to answer them caught than she has ever been free.\" "
        "It was not a promise. It was the nearest thing to one either "
        "of them had left to offer."
    )},
    {"type": "body", "text": (
        "Zara, still muffled but restless, walked the compound's edge "
        "twice that evening testing whatever remained of her borrowed "
        "sense, and found only the same flat, cottoned silence that had "
        "followed her since Mfoniso's working first took hold of it. "
        "\"I hate not knowing,\" she admitted to Adaugo. \"For months my "
        "fear was at least useful to someone. Tonight it is only mine "
        "to carry.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT SILENCE TOLD HER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A day and a half west of Idoro, Mfoniso sat with an unlit fire "
        "and an unmet deadline, counting the hours since her informant's "
        "silence had passed from unusual into impossible. Two seasons. "
        "Not once, in all that time, had the stone failed to answer her "
        "on schedule, not through illness, not through fear, not even "
        "through the household's own growing suspicion, which she had "
        "assumed would slow him rather than stop him entirely."
    )},
    {"type": "body", "text": (
        "She turned the silence over the way she turned over every "
        "piece of information a hunt gave her, refusing to let hope "
        "shape her reading of it. A missed contact could mean many "
        "ordinary things. It could also mean the one thing her training "
        "had taught her to fear above nearly everything else: that her "
        "informant had been found, and that whatever he knew of her "
        "methods, her patience, her patterns, now belonged to the "
        "household she had spent months studying."
    )},
    {"type": "body", "text": (
        "The reasonable choice, the patient choice, the choice every "
        "teacher she had ever trained under would have counseled, was "
        "to investigate carefully, from a careful distance, before "
        "committing to anything as loud as walking into ground that "
        "might now be waiting for her. Mfoniso considered that choice "
        "for a long moment, weighing it against everything the silence "
        "actually told her, and set it aside."
    )},
    {"type": "body", "text": (
        "She thought, unbidden, of the guardian that had reached back "
        "along Adaugo's anchor thread weeks ago, the first time in her "
        "career something old enough to remember being hunted had ever "
        "noticed her looking. Her teacher's warning returned to her "
        "again, worn smooth from repetition. It remembers what was done "
        "to it, and it will not forgive being reminded twice. If that "
        "warning had ever applied to any hunt of hers, it applied to "
        "this one, and every day of delay only handed the household "
        "more time to remember harder."
    )},
    {"type": "body", "text": (
        "\"If they know about him,\" she said quietly, to the unlit "
        "fire, to no one, \"then they already know I am coming, "
        "whatever I do next. Patience only spends time I no longer have "
        "for free.\" She rose, checked the small collection of tools she "
        "had carried across three seasons of this hunt, and made the "
        "decision that would have startled her own teacher more than "
        "any other choice in her long, careful career. Not the drop "
        "point. Not the stone, and whatever waited quietly around it. "
        "Straight to the family itself, tonight, before they finished "
        "preparing for whichever version of her arrival they had "
        "imagined."
    )},
    {"type": "body", "text": (
        "She left the dead fire exactly as it was, a habit kept from "
        "long practice rather than any present need, and began walking "
        "east through the dark toward Idoro at a pace she had not "
        "allowed herself since the night she first lost Kene, patience "
        "finally, fully spent."
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
    print("  THE DARK RISE — Episode 89: \"A Trap With No Leak Left\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_89.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_89.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
