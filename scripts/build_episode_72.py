#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 72: "The Cost Not Yet Paid"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-17: Episode 72 makes the presence's Episode 70 cost
concrete. It has not reached for Chibundu unprompted since that
night, a departure from the pattern it only just began in Episode 67,
and Oso itself feels subtly duller to the entity, roots slower to
answer, the iroko tree's usual restlessness gone quiet. Chibundu goes
to the cold place uninvited again and finds the presence genuinely
weakened, admitting the reach cost more than it let itself believe in
the moment and that it does not know how long recovery will take.
Worse, it admits that extending itself that far may have done more
than save Kene — it may have made the presence visible, for the first
time, to whatever it has spent this whole story refusing to name.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_72.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Two"},
    {"type": "title_ep_name", "text": "The Cost Not Yet Paid"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A GROUND GONE QUIET
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The entity noticed it first in the roots themselves, a "
        "sluggishness in ground that had answered its will instantly "
        "for three centuries, and mentioned it to Chibundu carefully, "
        "unwilling to name a fear before it was certain the fear was "
        "warranted. \"Oso feels duller today,\" it said. \"Not broken. "
        "Simply slower to answer, the way a limb answers slower after "
        "it has been asked to carry more weight than it was built "
        "for.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt the observation settle into a shape he had "
        "been half avoiding since the stream. \"It has not reached for "
        "me since that night,\" he said. \"Not once. It started "
        "reaching on its own only a few days ago, and I let myself "
        "believe that meant something had changed for good between us. "
        "I do not like how quickly it stopped again.\""
    )},
    {"type": "body", "text": (
        "\"Then go to it,\" the entity said. \"You do not need my "
        "permission for that door any longer, and I do not believe "
        "either of us will feel settled again until we know plainly "
        "what that night actually cost.\""
    )},
    {"type": "body", "text": (
        "It walked with him partway, an unspoken concession that it "
        "no longer trusted the ground between the hollow and the cold "
        "place to behave as reliably as it once had, and Chibundu felt "
        "the entity's own unease in the careful, deliberate way it "
        "chose each step, testing footing it had never once needed to "
        "test before this week. \"Even you feel it,\" he said. \"Not "
        "only the presence's ground. Yours too.\""
    )},
    {"type": "body", "text": (
        "\"Ours has always been more tangled together than either of "
        "us liked to admit,\" the entity said. \"I do not know whether "
        "what I am feeling is my own weariness borrowed from watching "
        "it happen, or something closer to a shared wound neither of "
        "us fully understands the shape of yet. I only know I would "
        "rather learn the answer standing beside you than guessing at "
        "it alone.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT REACHING THAT FAR TOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The cold place felt different when Chibundu reached it this "
        "time, thinner somehow, the patient stillness he had come to "
        "expect replaced by something that took a long moment to "
        "gather itself into any recognizable shape at all. You came "
        "sooner than I expected, the presence said finally, its voice "
        "carrying a weariness Chibundu had never once heard from it "
        "before. I am sorry I did not reach for you first. I am not "
        "certain, at the moment, that reaching is a thing I can spend "
        "carelessly."
    )},
    {"type": "body", "text": (
        "\"Tell me what it actually cost,\" Chibundu said. \"Not the "
        "size of it in words neither of us can measure. What it "
        "means, plainly, for tomorrow, and the day after that.\""
    )},
    {"type": "body", "text": (
        "I spent something I did not know I still had to spend, the "
        "presence said. Three centuries of patience taught me to "
        "husband my strength carefully, to never reach further than I "
        "was certain I could afford. I broke that habit without "
        "hesitating, the night your brother needed it broken, and I "
        "do not yet know how long the ground I spent will take to "
        "grow back, or whether it grows back the same each time or "
        "less."
    )},
    {"type": "body", "text": (
        "Chibundu felt something cold move through him at that "
        "uncertainty. \"So if it happens again soon,\" he said, \"you "
        "may not be able to do what you did last time.\""
    )},
    {"type": "body", "text": (
        "I do not know, the presence said, and the honesty of it "
        "cost visibly more than a comforting guess would have. I would "
        "like to promise you I could. I have learned, across this "
        "whole season, that a promise I am not certain I can keep is "
        "worth less to you than an uncertainty offered plainly, and I "
        "will not spend your trust cheaply now simply because the "
        "truth frightens both of us."
    )},
    {"type": "body", "text": (
        "\"There is something else,\" it said, before Chibundu could "
        "answer, the weariness in its voice sharpening into something "
        "closer to dread. Reaching that far was not only a matter of "
        "spent strength. It was also, very likely, the loudest thing I "
        "have ever done in three centuries of trying not to be heard "
        "at all. I do not know yet whether the silence I have always "
        "kept from the thing I have never let myself name was actually "
        "protecting me, or simply meant it had not yet noticed I was "
        "here to protect."
    )},
    {"type": "body", "text": (
        "Chibundu felt the particular vertigo of watching something "
        "ancient admit to a fear this plain, and understood, sitting "
        "with it in the thinned, unfamiliar quiet of the cold place, "
        "that some part of the balance between them had shifted "
        "without either of them quite deciding it should. \"You have "
        "spent this whole season teaching me how to carry fear without "
        "letting it decide everything for me,\" he said. \"Let me sit "
        "with you in this the same way, rather than simply receiving "
        "the lesson one direction only.\""
    )},
    {"type": "body", "text": (
        "The presence was quiet a long moment at that, something in "
        "its ancient stillness softening in a way Chibundu had not "
        "felt from it before. I did not expect comfort offered back to "
        "me, it said finally. I have given a great many things across "
        "three centuries. I do not believe anyone has ever offered me "
        "that one before tonight."
    )},
    {"type": "body", "text": (
        "\"Then it is overdue,\" Chibundu said simply, and sat with it "
        "a while longer in the quiet, neither of them needing further "
        "words to fill the space between them."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT ZARA NOTICED WITHOUT BEING TOLD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara felt it too, though she could not have named what "
        "exactly had changed, only that the ordinary background hum "
        "of the entity's and the presence's combined attention, the "
        "one she had lived alongside long enough to stop consciously "
        "noticing, had gone thinner sometime in the last few days, "
        "the way a familiar sound grows noticeable only once it "
        "quiets."
    )},
    {"type": "body", "text": (
        "She mentioned it to Amara carefully, unwilling to sound as "
        "though she were inventing a new fear simply because the last "
        "one had proven so real. \"I do not know if it means anything,\" "
        "she said. \"Only that whatever usually sits at the edge of my "
        "own senses feels quieter than it has in months. I noticed it "
        "the morning after Kene was taken, and it has not gone back to "
        "how it was before.\""
    )},
    {"type": "body", "text": (
        "Amara turned that over carefully, unwilling to press for an "
        "answer neither of them had, and resolved, quietly, to ask "
        "Chibundu directly the next time she saw him rather than let "
        "another private worry sit unspoken in this household for even "
        "one more day than it had to. She had learned, across a whole "
        "season of costly silences, that the question asked plainly "
        "and early nearly always hurt less than the one left to fester "
        "quietly until circumstance finally forced it into the open."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A QUIET NEITHER POWER TRUSTED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu carried the whole account back to the entity, and "
        "watched it absorb the new uncertainty with the same careful "
        "stillness it now gave every danger too large to answer with a "
        "single clean plan. \"Then we tell no one outside this ground "
        "how weakened it truly is,\" the entity said. \"Not Amara. Not "
        "Chidebe. Not even Zara, whose own senses might otherwise "
        "carry the fact somewhere it does not need to travel yet. A "
        "weakened guardian known to be weakened is a door held open "
        "for anyone patient enough to notice.\""
    )},
    {"type": "body", "text": (
        "\"That is one more secret in a season that has already cost "
        "this family every secret it ever tried to keep,\" Chibundu "
        "said, uneasy with the shape of the plan even as he understood "
        "its logic. \"You once told me yourself that honesty shared "
        "early is smaller than honesty discovered late. I do not see "
        "how this is any different simply because the truth this time "
        "belongs to you rather than to me.\""
    )},
    {"type": "body", "text": (
        "\"It is not different,\" the entity admitted. \"It is simply "
        "a harder truth to share while it is still unfolding, before "
        "either of us knows its full shape. I am not asking you to "
        "hide it forever. I am asking for a few days to understand "
        "what we are actually protecting them from, rather than "
        "handing them a fear neither of us can yet explain clearly "
        "enough to be useful.\""
    )},
    {"type": "body", "text": (
        "\"It is,\" the entity agreed. \"I do not offer it lightly, and "
        "I will not keep it a day longer than the danger requires. But "
        "I have learned this season, the same as you, that not every "
        "truth shared early is a truth that makes anyone safer for the "
        "sharing. Some truths simply need a little more time to become "
        "useful instead of merely frightening.\""
    )},
    {"type": "body", "text": (
        "Chibundu did not fully agree, and did not fully argue either, "
        "sitting instead with the uncomfortable weight of guarding a "
        "secret meant to protect the very people it was being kept "
        "from, and wondered, watching Oso's dulled, patient dark settle "
        "back around him, how many more nights this fragile, "
        "unfinished quiet could actually be trusted to hold."
    )},
    {"type": "body", "text": (
        "He thought, turning the whole night over one last time "
        "before finally letting himself rest, of Amara's promise that "
        "she would rather choose a cost together than let fear choose "
        "it for her family in secret. He did not yet know how to "
        "reconcile that promise with the entity's own insistence on "
        "silence, and understood, drifting finally toward an uneasy "
        "sleep, that the question would not stay comfortably unasked "
        "for very much longer, and that when it finally came, he would "
        "have to choose, in the moment, which promise he was more "
        "afraid of breaking."
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
    print("  THE DARK RISE — Episode 72: \"The Cost Not Yet Paid\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_72.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_72.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
