#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 20: "The First Word"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-27: Episode 20 closes this ten episode block on two
converging hooks. In Oso, the vessel speaks his first true word, and it is
not a word the entity taught him or chose for him: it is "Mama," spoken
unprompted, a small crack of ordinary human longing surfacing through
months of careful shaping, which the entity notes with something closer
to genuine reconsideration than its usual flat calculation. In Idoro,
Amara and Obi try to steady a household still reeling from Elder Maka's
fall, with no new authority yet in place to fill the space she left. Far
beyond the village, the trader who witnessed Zara's aborted departure
reaches a river market crowded enough to hold a man who serves, however
distantly, the crown at Udo, and tells his growing story to exactly the
kind of ear built to carry it further. The episode ends on the shared
understanding, held by the reader alone, that the quiet village crisis
Amara has spent nineteen episodes fighting in private is no longer
contained to Idoro at all.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_20.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty"},
    {"type": "title_ep_name", "text": "The First Word"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A VILLAGE WITH NO ONE AT ITS CENTER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three days after the council stripped Elder Maka of her "
        "authority, Idoro still had not decided who, if anyone, was "
        "meant to hold it now."
    )},
    {"type": "body", "text": (
        "The elders met again, and argued, and adjourned without "
        "naming a successor, each of them privately unwilling to stand "
        "in the exact place Elder Maka had stood when the entity chose "
        "to ruin her in front of everyone she had ever judged. Fear, "
        "Amara had come to understand, did not only flow downward from "
        "those who held power. It could just as easily flow away from "
        "power altogether, leaving a shape at the center of a village "
        "that no one wanted to fill."
    )},
    {"type": "body", "text": (
        "The watchers no longer came to her compound at all. There was "
        "no one left to send them, and no one left to receive their "
        "reports. Amara found she almost missed the small, irritating "
        "certainty of being watched. An unwatched fear was somehow "
        "worse than a guarded one, the way an unlatched door left open "
        "all night is worse than one merely locked poorly."
    )},
    {"type": "body", "text": (
        "She visited Elder Maka once, on the second of those three "
        "days, and found her sitting alone in a compound that had "
        "already begun to look neglected, weeds creeping up through "
        "packed earth no one had swept in days. Neither woman spoke for "
        "a long while. There did not seem to be much left to say that "
        "the whole village had not already said louder, in front of "
        "more witnesses, than either of them could manage now."
    )},
    {"type": "body", "text": (
        "\"Adaugo has not come back,\" Elder Maka said finally, not "
        "quite a question."
    )},
    {"type": "body", "text": (
        "\"Give her time,\" Amara said. \"You gave the whole village "
        "thirty and four years to learn how to fear you properly. She "
        "has had three days to learn how to stop.\""
    )},
    {"type": "body", "text": (
        "It was not gentle, and Amara had not meant it to be. Elder "
        "Maka accepted it anyway, the way a person accepts a truth they "
        "have already told themselves in the dark, and said nothing "
        "further before Amara let herself out."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi spent those three days trying, and mostly failing, to "
        "rebuild what the market had cost him, and came home each "
        "evening a little more silent than the evening before, the "
        "particular silence of a man watching a wound heal crooked and "
        "deciding not to say so aloud. Kene, sealed now against "
        "whatever had once reached for him, grew the ordinary way "
        "ordinary children grow, oblivious to everything that had been "
        "spent to make his growing ordinary again."
    )},
    {"type": "body", "text": (
        "\"We are still standing,\" Amara said one evening, more to "
        "convince herself than Obi. \"Whatever else this village has "
        "lost, we are still standing in it.\""
    )},
    {"type": "body", "text": (
        "\"Standing is not the same as safe,\" Obi said. \"I have "
        "learned that much these last months, if nothing else, and I do "
        "not expect the lesson to stop teaching itself any time soon.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE WORD THE ENTITY DID NOT CHOOSE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the vessel had been shaping sound "
        "into something closer and closer to language for days, small "
        "deliberate syllables strung together and pulled apart again, "
        "practice without an audience beyond the patient presence that "
        "had taught him almost everything else he knew."
    )},
    {"type": "body", "text": (
        "The entity had assumed, without examining the assumption very "
        "closely, that the first true word would be one it had shaped "
        "itself, a name for the roots, a name for the dark, a name for "
        "the entity's own presence pressed so closely against his mind "
        "that the two of them had begun to blur at the edges the way "
        "two colors blur where they meet."
    )},
    {"type": "body", "text": (
        "It was wrong."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The boy said it in the stillest part of the night, quietly, "
        "testing the shape of it the way he had tested every shape "
        "before it, and there was nothing taught or borrowed in the "
        "sound at all."
    )},
    {"type": "body", "text": (
        "\"Mama.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The entity went very still, in whatever manner a presence "
        "without a body could be said to go still, turning the single "
        "small word over with an attention it had not expected to spend "
        "on it. It had shaped this child's hunger, his fear, his growth, "
        "his first uncertain steps and his first joined syllables, and "
        "somewhere beneath all of that careful shaping, something "
        "entirely its own had grown anyway, untaught, unchosen, reaching "
        "for a woman the boy had never once seen with his own eyes."
    )},
    {"type": "body", "text": (
        "It could have corrected this. A small adjustment, a redirection "
        "of the boy's earliest want toward the entity's own presence "
        "instead, would have cost it almost nothing to attempt. It found, "
        "turning the option over, that it did not want to attempt it, "
        "and took its time deciding whether that reluctance was mercy, "
        "or simply another kind of patience it had not yet learned the "
        "name of."
    )},
    {"type": "body", "text": (
        "It considered, too, what the word implied about everything "
        "still growing in the boy beneath its own careful shaping. A "
        "vessel built only from what the entity poured into him would "
        "have been simpler to predict, easier to finish, a tool without "
        "the inconvenience of wanting anything the entity had not first "
        "decided he should want. This small, unchosen word suggested "
        "something messier than a tool was taking shape in that body, "
        "something with a grain of its own the entity would need to "
        "work with rather than simply carve against."
    )},
    {"type": "body", "text": (
        "It did not know yet whether that grain would serve its "
        "purposes or eventually work against them. It found, examining "
        "the uncertainty honestly, that this was the first question "
        "concerning the vessel it had ever asked itself without already "
        "knowing the answer."
    )},
    {"type": "body", "text": (
        "It let the word stand. For now."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In its old ledger, the cold voice entered the night's one new "
        "fact."
    )},
    {"type": "system", "text": "Vessel: first true word formed, unprompted, maternal referent. Entity response: no correction applied."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE RIVER ROAD — WHERE THE STORY WENT NEXT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three days north of Idoro, the trader reached the river "
        "market at the bend where boats from the delta traded palm oil "
        "and dried fish for salt and cloth carried down from the "
        "capital, and told his story again, embellished a little more "
        "each time the way any good story is embellished by an honest "
        "man who does not think of himself as a liar."
    )},
    {"type": "body", "text": (
        "He told it to a fellow trader over a shared fire, who told it "
        "to a boatman waiting on a delayed cargo, who told it, almost "
        "as an afterthought, to a quiet, watchful man who had been "
        "sitting near enough to hear all three versions and had said "
        "almost nothing the whole evening."
    )},
    {"type": "body", "text": (
        "The quiet man served, in a distant and unglamorous capacity, "
        "the crown at Udo, one of a dozen such men scattered along the "
        "river roads whose only duty was to notice things worth "
        "noticing and carry them home when the season's business was "
        "finished. He had heard a hundred exaggerated village stories in "
        "his years on this road, curses and possessions and vengeful "
        "spirits blamed for every drought and every stillbirth, and had "
        "learned to let most of them pass through him without taking "
        "root."
    )},
    {"type": "body", "text": (
        "This one, for reasons he could not entirely name even to "
        "himself, he chose to remember."
    )},
    {"type": "body", "text": (
        "It was not the possession itself that stayed with him. He had "
        "heard possession stories before, told by firelight in a dozen "
        "villages up and down this same river, most of them dressing up "
        "an ordinary sickness or an ordinary grudge in borrowed language "
        "too frightened to name the real thing plainly. What stayed with "
        "him was the detail the trader had almost left out, mentioned "
        "only once, in passing: that the same voice, weeks earlier, had "
        "spoken through a different mouth entirely, a village healer, to "
        "say a single word before its host went silent again."
    )},
    {"type": "body", "text": (
        "Coming."
    )},
    {"type": "body", "text": (
        "One frightened story of a spirit speaking through a healer was "
        "easy to dismiss. A second voice, in a different mouth, weeks "
        "later, delivering fear precisely enough to break an old woman "
        "who had ruled unquestioned for thirty and four years, was "
        "something else. It suggested a pattern, and the quiet man had "
        "learned, across many seasons on this road, that patterns were "
        "the only rumors worth carrying home at all."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "A whole village's authority broken in a single morning by a "
        "voice that spoke through another woman's mouth in front of "
        "every witness gathered to see her exiled. An old law enforcer "
        "marked by the very thing she had spent her life condemning. A "
        "village called Idoro, in the Oji Delta, further from Udo than "
        "most of the court would ever think to look."
    )},
    {"type": "body", "text": (
        "It was not urgent. It was not, on its own, anything the "
        "throne would trouble itself over. But it was strange enough, "
        "and specific enough, to be worth a single line in the report he "
        "would carry home when the trading season ended, and the quiet "
        "man filed it away exactly the way he filed away every other "
        "small, strange thing the river brought him, never once "
        "suspecting that he had just become the first thread connecting "
        "a forgotten delta village to the throne of Ijendu itself."
    )},
    {"type": "body", "text": (
        "In Idoro, no one yet knew that word of their unraveling had "
        "traveled even as far as the river bend. In Oso, no one yet knew "
        "that a word far smaller than that one, a single syllable meant "
        "for a mother who had never once held the child who spoke it, "
        "had just changed the shape of what the entity believed it was "
        "building beneath the iroko roots. Both words were already "
        "moving, quietly, toward futures neither speaker could yet "
        "imagine, one carried on the current of an ordinary river, the "
        "other carried on nothing more than a child's first unguarded "
        "reach toward a woman he had never met, and would not meet, for "
        "a long while yet."
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
    print("  THE DARK RISE — Episode 20: \"The First Word\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_20.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_20.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
