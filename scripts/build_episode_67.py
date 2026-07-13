#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 67: "The Lost Ground"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-12: Episode 67 gives the presence's grief its fullest
telling yet. For the first time, it reaches for Chibundu unprompted
rather than waiting to be sought, its old composure visibly strained.
It describes, plainly and without the ancient distance it usually
keeps, exactly how the guardian of its lost ground was defeated: not
in open combat, but by a hunter who turned the guardian's own loved
ones into leverage, forcing an impossible choice the guardian could
not win no matter which way it answered. The entity, brought into the
conversation as it happens, recognizes at once that Amara, Obi, and
Kene occupy exactly that same vulnerable position now, and the
episode closes on both old powers facing a problem neither patience
nor force has ever been built to solve: how to protect people from
becoming leverage without taking away the very choices that make them
worth protecting in the first place.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_67.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Seven"},
    {"type": "title_ep_name", "text": "The Lost Ground"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE FIRST TIME IT CAME UNASKED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The presence reached for Chibundu that evening before he had "
        "even settled toward sleep, the first time in their whole "
        "strange acquaintance it had ever come to him rather than "
        "waited to be sought, and he felt its old, patient composure "
        "arrive frayed at the edges in a way that frightened him more "
        "than any of its careful silences ever had."
    )},
    {"type": "body", "text": (
        "I need to tell you the rest of it, it said, without the "
        "usual courtesy of easing into the cold place first. Not the "
        "shape of the ground I lost. What was actually done to lose "
        "it. I did not have the words ready the last time you asked, "
        "and I do not think either of us can afford my carefulness "
        "any longer."
    )},
    {"type": "body", "text": (
        "Chibundu called the entity to him at once, unwilling to hold "
        "this alone the way he had once insisted on holding his fury "
        "alone, and felt both old powers settle into a wary, attentive "
        "stillness around him as the presence continued, its voice "
        "carrying a grief it no longer tried to smooth into something "
        "gentler."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: HOW THE GUARDIAN WAS TAKEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The one who guarded that ground before me was not defeated "
        "in the way you would expect, the presence said. No blade "
        "reached it. No army broke its will. The hunter who came for "
        "it understood, long before it ever arrived, that a power "
        "built entirely around protecting people cannot be threatened "
        "directly at all. It can only be threatened through the people "
        "themselves."
    )},
    {"type": "body", "text": (
        "\"What did it do,\" Chibundu asked, though some cold, certain "
        "part of him had already begun to guess the shape of the "
        "answer."
    )},
    {"type": "body", "text": (
        "It took two people the guardian loved, the presence said, and "
        "placed them somewhere it could reach and the guardian could "
        "not, without ever once threatening to harm either of them "
        "outright. It simply waited, patiently, for the guardian to "
        "make the only choice a power like that can ever make when "
        "faced with a threat aimed at what it loves rather than at "
        "itself. The guardian came. Not because it was tricked. "
        "Because it could not do otherwise and still be the thing it "
        "was."
    )},
    {"type": "body", "text": (
        "The entity felt something in itself go very still, turning "
        "the account over against its own three centuries of certainty "
        "that its greatest danger would always announce itself as "
        "danger first. \"And once it came,\" it said."
    )},
    {"type": "body", "text": (
        "The hunter did not need force after that, the presence said. "
        "It only needed patience, the same patience I once believed "
        "was my own greatest strength, turned back against me as a "
        "weapon. A guardian standing exactly where its enemy chose, "
        "already committed to protecting rather than to winning, is "
        "not difficult to end. It is only difficult to end quickly, "
        "and the hunter I am describing was never in any hurry at "
        "all."
    )},
    {"type": "body", "text": (
        "\"You keep saying the guardian,\" Chibundu said carefully, "
        "\"as though you are describing a stranger. Were you there. Did "
        "you see it happen.\""
    )},
    {"type": "body", "text": (
        "I was close enough to feel it happen, the presence said, and "
        "something in its voice folded further inward, a grief kept "
        "compressed for so long that even naming its edges seemed to "
        "cost it real effort. I was young then, by whatever measure "
        "something like me can be young, watching from ground "
        "adjacent to that guardian's own, close enough to feel every "
        "part of what was done and not close enough, or not brave "
        "enough, to reach across and stop it. I have spent every "
        "season since telling myself the distance between us was too "
        "great to cross in time. I no longer fully believe that "
        "excuse either."
    )},
    {"type": "body", "text": (
        "Chibundu felt the full weight of what was being told to him "
        "settle into place beside the fear he had already been "
        "carrying since Zara's first strange, cold touch. \"You are "
        "telling me this because you believe the same hunter, or one "
        "trained the same way, is coming here,\" he said. \"And that "
        "Amara, and Obi, and Kene, are exactly what it would use "
        "against you, or against the entity, or against me.\""
    )},
    {"type": "body", "text": (
        "The entity went very still, a realization arriving in it "
        "with the particular cold clarity of a mistake finally "
        "recognized long after the moment it mattered most. \"The "
        "Factor's men already tried a smaller version of exactly "
        "this,\" it said slowly. \"The reunion. Amara standing at the "
        "boundary, undefended, at a fixed hour anyone patient enough "
        "to watch could learn in advance. I called it an ambush of "
        "opportunity at the time. I no longer believe it was only "
        "that. It was a rehearsal, whether the Factor's House knew it "
        "or not, for exactly the method this hunter was trained to "
        "use.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt something cold settle low in his chest, the "
        "memory of that night arriving newly sharpened by everything "
        "he had just been told. \"Then it has already been tried on "
        "us once,\" he said. \"Before either of us understood there "
        "was a name for what was being tried.\""
    )},
    {"type": "body", "text": (
        "It very likely has, the presence said. I did not recognize "
        "the shape of it either, watching from where I watched that "
        "night. I was still learning, then, that this ground held "
        "anything worth this particular kind of patience. I do not "
        "have that excuse any longer, and I do not intend to make the "
        "same mistake of recognition twice."
    )},
    {"type": "body", "text": (
        "I believe it is possible, the presence said. I do not know "
        "it as certainty. I know only that I would rather you hear the "
        "worst shape of this danger from me, plainly, than discover it "
        "the way the guardian I once knew discovered it, standing "
        "already at the exact place his enemy had chosen for him."
    )},
    {"type": "body", "text": (
        "The entity absorbed the whole account in a silence that "
        "stretched long enough to worry Chibundu more than words might "
        "have. \"Then we have a problem neither patience nor force was "
        "ever built to solve,\" it said finally. \"How do we protect "
        "people from becoming leverage, without taking from them the "
        "very choices that make them worth protecting at all. I do not "
        "have an answer to that tonight. I do not think either of us "
        "does.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with both old powers in a silence that felt, for "
        "the first time in a long while, entirely without comfort in "
        "any direction, and understood, turning the account over "
        "himself, that the next danger to reach this boundary would "
        "not announce itself as danger at all. It would arrive looking "
        "exactly like an ordinary day, right up until the moment it no "
        "longer needed to."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A WARNING SHAPED DIFFERENTLY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"We have to tell them differently than we told them the last "
        "warning,\" Chibundu said finally. \"Not simply that something "
        "is coming. That it will not come for me, or for either of "
        "you, first. It will come for whoever it decides matters most "
        "to us, and it will not announce that intention beforehand.\""
    )},
    {"type": "body", "text": (
        "\"Then Amara, Obi, and Kene need to hear it exactly that "
        "plainly,\" the entity said, \"and so does Chidebe, since he "
        "holds the ground in Osadebe's absence and will need to think "
        "differently about what a boundary is even meant to guard "
        "against now.\" It paused, weighing something further before "
        "adding it. \"I would like to be the one who tells Amara "
        "myself, this time. Not through you. She deserves to hear it "
        "from the one who failed to recognize the danger once "
        "already.\""
    )},
    {"type": "body", "text": (
        "Chibundu considered that, and nodded slowly. \"She will "
        "respect that more than she would a softened version passed "
        "through me,\" he said. \"But I am coming with you when you "
        "tell her. Whatever this costs any of us to hear, I do not "
        "want to keep learning secondhand what was decided about my "
        "own family while I was somewhere else.\""
    )},
    {"type": "body", "text": (
        "The presence, quieter now, its grief spent for the moment "
        "though clearly not fully set down, offered the last thing it "
        "had left to give them both. I cannot promise this ends "
        "better than it did the last time, it said. I can promise you "
        "will not face it the way that guardian did, alone and only "
        "understanding the shape of the trap after it had already "
        "closed. That is a smaller comfort than either of you deserves "
        "tonight. It is, unfortunately, the only one I have left to "
        "offer."
    )},
    {"type": "body", "text": (
        "The entity considered that a long moment before answering, "
        "turning the presence's honesty over the way it now turned "
        "over most hard things this season had handed it. \"It is not "
        "as small as you think,\" it said finally. \"A guardian who "
        "warns the people it loves before the trap closes, rather "
        "than after, has already changed the shape of the danger "
        "considerably. I intend to hold onto that difference, even if "
        "it is the only advantage either of us has left to claim.\""
    )},
    {"type": "body", "text": (
        "Chibundu rose to go find Amara before the night grew any "
        "later, the entity beside him and the presence's grief still "
        "settling somewhere at the edge of his own awareness, and felt, "
        "walking toward a conversation he knew would frighten his "
        "mother badly, a strange, steadying certainty underneath the "
        "fear. Whatever this hunter had learned from an old, unwatched "
        "victory, it had not yet learned what a family that shares its "
        "hardest truths early, rather than late, might actually cost "
        "it to reach. He intended, whatever else this night still "
        "held, to make certain it learned that cost in full."
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
                    first_line_indent=None):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing = make_element("spacing", {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    })
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


def make_body_paragraph(text, spacing_after=60, spacing_line=360):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360)


def make_system_paragraph(text, spacing_after=120, spacing_line=360):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

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
            para = make_body_paragraph(text)
        elif typ == "system":
            para = make_system_paragraph(text)
        elif typ == "blank":
            para = make_blank_paragraph()
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

def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 67: \"The Lost Ground\"")
    print("  Build Script")
    print("=" * 60)
    print()

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_67.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_67.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
