#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 65: "The Crown Hears of Two Powers"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-10: Episode 65 returns to Udo as Osadebe's unsoftened
report of the boundary meeting finally arrives, telling Eze Amadi's
council for the first time that a second old power, distinct from the
entity, has been present at Idoro since at least Episode 47's naming.
Nkiruka, asked to weigh the report against her own three historical
accounts, realizes with real alarm that the pattern she has spent
years reading as one power growing steadily bolder makes far more
sense as two separate powers acting across the same centuries,
misread as one because no one ever thought to ask. Eze Amadi, unable
to simply add a second unknown to a report he has not finished
absorbing the first of, makes a decision that pulls Osadebe away from
Idoro at the worst possible moment: he summons the captain back to
Udo in person to answer questions no letter can hold, leaving the
village without its steadiest crown liaison just as something neither
side has named yet continues closing the distance.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_65.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Five"},
    {"type": "title_ep_name", "text": "The Crown Hears of Two Powers"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A SECOND NAME IN THE REPORT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Eze Amadi read Osadebe's report alone first, the way he had "
        "read every report to reach him about Idoro since the captain's "
        "very first posting, and set it down afterward with the "
        "particular stillness of a man who has just realized a "
        "question he believed settled was, in fact, only half asked. "
        "He summoned Nkiruka and Ejikeme both before the ink of his own "
        "notes had finished drying."
    )},
    {"type": "body", "text": (
        "\"A second power,\" Ejikeme said, once he had read it through "
        "himself, his voice carrying none of its old confidence about "
        "what patience or coin could reliably manage. \"Not merely a "
        "second name for the same thing we have been tracking since "
        "Osadebe first stood at that boundary. Something the entity "
        "itself did not know existed until it reached into that boy's "
        "own throat and took his voice from him.\""
    )},
    {"type": "body", "text": (
        "\"That is what troubles me most in the whole account,\" Eze "
        "Amadi said. \"Not that it exists. That it has been reaching "
        "that boy since at least the naming at the boundary, and none "
        "of us, not the crown, not Osadebe, not even the power we "
        "believed we finally understood, noticed it standing there "
        "until it chose to act.\""
    )},
    {"type": "body", "text": (
        "Ejikeme set the report down and rubbed a hand across his "
        "face, the gesture of a man doing arithmetic he did not want "
        "to be doing. \"Every argument I have built this season rests "
        "on understanding what we are actually negotiating with,\" he "
        "said. \"I have spent months learning to weigh one old power's "
        "patience against a trading House's greed. I do not yet know "
        "how to weigh anything against a power that took a decision out "
        "of a child's own mouth without so much as a warning first. I "
        "am no longer certain patience is even the right word for what "
        "we are dealing with now.\""
    )},
    {"type": "body", "text": (
        "\"It is still the right word,\" Eze Amadi said. \"It is simply "
        "no longer the only word we need. A power that grieves, "
        "Osadebe's report says the boy was told. Grief is not the same "
        "as hunger, and I do not believe we can afford to keep treating "
        "every old thing at that boundary as though it wants the same "
        "single thing the entity has always wanted. That mistake alone "
        "could cost us as much as underestimating any of them.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: ONE PATTERN, READ WRONG
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Nkiruka asked for a full day alone with the report and her "
        "own old records before she would offer anything more than "
        "careful silence, and returned to the council with an "
        "expression Eze Amadi had not seen on her in all the years she "
        "had served this court. \"I need to correct something I told "
        "you in this very room, seasons ago,\" she said. \"I believe I "
        "was wrong, and I believe the shape of that wrongness matters "
        "considerably more than a simple mistake.\""
    )},
    {"type": "body", "text": (
        "\"Wrong how,\" Eze Amadi asked."
    )},
    {"type": "body", "text": (
        "\"I told you the three old accounts described one power "
        "growing steadily bolder across three centuries,\" Nkiruka "
        "said. \"Each encounter more direct than the last, I said, a "
        "pattern of confidence rather than repetition. I have spent "
        "this last day reading those same three accounts again, "
        "knowing now that a second power exists, and I no longer "
        "believe I was reading one power's growing confidence at all. "
        "I believe I was reading two different powers, acting across "
        "the same long stretch of time, mistaken for one because no "
        "prior keeper of this archive ever thought to ask whether more "
        "than one voice might be speaking.\""
    )},
    {"type": "body", "text": (
        "The chamber went very still. \"If that is true,\" Ejikeme "
        "said slowly, \"then the second power has been moving through "
        "this kingdom's history for as long as the first one has. Not "
        "newly arrived. Not recently woken. Simply unnoticed, the same "
        "way it went unnoticed at that boundary until it chose to be "
        "seen.\""
    )},
    {"type": "body", "text": (
        "\"That is precisely my fear,\" Nkiruka said. \"A power patient "
        "enough to go unnoticed inside a kingdom's own written "
        "history for three centuries is not a power I know how to "
        "advise this council to prepare for. I do not know its "
        "appetite. I do not know its limits. I know only that it has "
        "apparently found something in that boy worth breaking its own "
        "long silence for, and I would like very much to understand "
        "why before it decides to break anything else.\""
    )},
    {"type": "body", "text": (
        "\"Can you separate the accounts,\" Eze Amadi asked. \"Now that "
        "you suspect two voices rather than one, can you tell which "
        "moments in your own archive belong to which power.\""
    )},
    {"type": "body", "text": (
        "\"Some of them,\" Nkiruka said. \"The direct messages, the "
        "ones spoken plainly to a watching authority, all carry the "
        "same patient, transactional weight I have come to associate "
        "with the entity Osadebe himself met at that boundary. But "
        "there are older fragments in the archive, half stories, "
        "third hand accounts too faded to trust fully, that describe "
        "something quieter reaching specific people rather than whole "
        "villages. I dismissed them for years as embellishment. I no "
        "longer feel confident dismissing anything in that archive at "
        "all.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi turned the whole of it over in a silence that "
        "stretched long enough to make even Ejikeme uncomfortable, and "
        "when he finally spoke, his decision arrived already fully "
        "formed, the way his hardest decisions about Idoro always "
        "seemed to. \"I want Osadebe here, in this room, answering "
        "questions a letter cannot hold,\" he said. \"Send for him. Not "
        "a written summons carried by the next courier south. I want "
        "him standing where I am standing, telling me himself what a "
        "second old power's voice actually sounded like coming out of "
        "a child's own mouth.\""
    )},
    {"type": "body", "text": (
        "\"That will take him from Idoro for the better part of a "
        "moon,\" Nkiruka said, the first hesitation she had shown all "
        "morning. \"Given everything in this report, I am not certain "
        "that is a season this village can safely spare its steadiest "
        "crown voice.\""
    )},
    {"type": "body", "text": (
        "\"I am aware of the cost,\" Eze Amadi said. \"I am also aware "
        "that I have spent this entire season making decisions about "
        "that village based on secondhand accounts filtered through "
        "however much a letter can carry. I would rather understand "
        "the danger fully, once, at the price of a moon's absence, "
        "than keep governing it blind at no cost at all until the day "
        "blindness finally costs someone their life.\" He rose, ending "
        "the session before either counselor could argue further. "
        "\"Send for him. Chidebe's garrison will hold the ground in his "
        "absence. I have made harder wagers than this on far less "
        "certain ground.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: THE SUMMONS REACHES IDORO
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The king's summons reached Idoro nine days later, and Osadebe "
        "read it twice before he trusted himself to say its contents "
        "aloud to Chidebe. \"He wants me in Udo,\" he said. \"In person. "
        "A moon's absence, perhaps longer, answering questions a letter "
        "cannot hold.\" Chidebe took the news the way he took most hard "
        "news now, with a short, steady nod rather than argument."
    )},
    {"type": "body", "text": (
        "\"Then I will hold the ground until you return,\" Chidebe "
        "said, \"the same as I told you I would the day my own garrison "
        "first arrived. I did not take this posting expecting it to "
        "stay easy the whole time I held it.\""
    )},
    {"type": "body", "text": (
        "Amara, told the news that same evening, felt an old, familiar "
        "unease settle over her at the timing of it, though she could "
        "not yet say exactly why it troubled her more than the words "
        "themselves seemed to justify. \"You have been the steadiest "
        "voice this village has had between itself and that crown "
        "since the day you first walked into it,\" she said. \"I do not "
        "like watching that voice travel a moon away from us, not "
        "while something we cannot yet name is still somewhere between "
        "here and wherever it started.\""
    )},
    {"type": "body", "text": (
        "\"I do not like it either,\" Osadebe admitted. \"But a king who "
        "governs a danger this size on secondhand letters alone is a "
        "king who eventually governs it wrong, and I would rather "
        "spend a moon answering his questions properly than leave him "
        "guessing at the shape of something none of us fully understand "
        "ourselves yet.\" He began packing that same night, unwilling "
        "to let the crown's summons wait any longer than it had to, "
        "leaving behind a boundary that felt, to everyone still "
        "standing on it, considerably less watched than it had the "
        "morning before."
    )},
    {"type": "body", "text": (
        "Chibundu, told of the departure by Amara before Osadebe left "
        "at first light, asked the entity afterward whether it thought "
        "the timing meant anything, or whether he was simply learning "
        "to see a shape in every ordinary inconvenience now. \"I do not "
        "know if it means anything,\" the entity told him honestly. \"I "
        "only know that very little about this season has turned out "
        "to be a coincidence once we understood it fully, and I would "
        "rather we both stayed watchful than assume this is the "
        "exception.\""
    )},
    {"type": "body", "text": (
        "Chibundu nodded slowly, filing the answer away with the same "
        "careful attention he now gave most uncertainties, and looked "
        "south down the river road for a long moment, toward a captain "
        "already a full day's travel toward a throne that had only "
        "just begun to understand how much it still did not know about "
        "the ground it had spent a season learning to protect, and "
        "hoped, without fully knowing why the hope felt so urgent, that "
        "a moon was a short enough absence for whatever was still "
        "closing in on them to wait out."
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
    print("  THE DARK RISE — Episode 65: \"The Crown Hears of Two Powers\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_65.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_65.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
