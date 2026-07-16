#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 34: "The Nameless Boy"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-10: Episode 34 turns fully to Oso. With concealment
mattering less now that the wider world already knows of it, the entity
begins teaching the vessel real truths for the first time rather than
careful half answers: that Mama is real, that she lives in a village
called Idoro, that he has a brother he has never met. The lesson lands
harder than the entity expected when the boy, working through what he
has just been told, asks the one question three centuries of careful
shaping never prepared the entity to answer plainly: what is my name.
He was cast out before Idoro's naming rite could ever be performed over
him. In Idoro, a brief scene shows Kene growing up ordinary and unaware,
a quiet contrast to everything unfolding a mile away in the dark beneath
the iroko roots. The episode ends with the entity turning the question
of a name over seriously for the first time, unable to decide whether
answering it would be a gift or one more claim staked on a boy already
shaped almost entirely by hands that are not his own.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_34.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Four"},
    {"type": "title_ep_name", "text": "The Nameless Boy"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE OTHER SON KNEW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Kene was old enough now to chase the compound chickens across "
        "the yard on legs that had only recently learned how to run "
        "properly, and Amara watched him from the doorway with the "
        "particular tenderness of a woman who had learned to treasure "
        "ordinary moments precisely because she understood, better than "
        "anyone in Idoro, how easily ordinary could be taken away."
    )},
    {"type": "body", "text": (
        "He knew nothing of a brother. He knew nothing of a forest "
        "that had once reached into his own sleeping body and used him "
        "as a weapon against a rite meant to sever it. He knew only "
        "that the chickens were fast, and that his mother's arms were "
        "the safest place in the world when his own small legs finally "
        "gave out beneath him, and Amara found herself grateful, in a "
        "way that ached every time she let herself feel it fully, that "
        "one of her sons at least still had the luxury of not knowing "
        "anything at all."
    )},
    {"type": "body", "text": (
        "Obi joined her in the doorway, watching Kene stumble and "
        "laugh and chase the same startled chicken in a circle for the "
        "third time without once losing his delight in it. \"He will "
        "ask, someday,\" Obi said quietly. \"Why we watch him the way "
        "we do. Why certain words go quiet in this house when he walks "
        "into a room too suddenly.\""
    )},
    {"type": "body", "text": (
        "\"I know,\" Amara said. \"I have not yet decided what I will "
        "tell him when that day comes, only that it will come, the "
        "same way every hard truth in this family eventually finds its "
        "way into the light whether we are ready to hand it over or "
        "not.\""
    )},
    {"type": "body", "text": (
        "She thought, watching her firstborn son fall happily into the "
        "dirt yet again, of the other boy growing up a mile away "
        "without a name of his own, and found the thought so unbearable "
        "that she let it pass through her the way she had learned to "
        "let unbearable things pass, acknowledged and released rather "
        "than held until they became something heavier than grief."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY FINALLY TOLD HIM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had decided, in the days "
        "since the boundary, that the careful half truths it had been "
        "offering the vessel no longer served the purpose they once "
        "had. Concealment had cost it something once, a reason to guard "
        "every word it gave him against the risk of the wider world "
        "eventually overhearing. That reason had mostly dissolved the "
        "moment it chose, at the boundary, to be known rather than "
        "merely suspected."
    )},
    {"type": "body", "text": (
        "It began plainly, in the low, wordless register it had always "
        "used with him, and told him, for the first time without "
        "softening any of it, that Mama was real, a woman who lived and "
        "breathed and grieved in a village called Idoro less than a "
        "mile from where he sat turning his small stones over in the "
        "dark. That he had a brother, born in the same hour he was, "
        "raised in that same village, growing up beside her while he "
        "grew up here instead."
    )},
    {"type": "body", "text": (
        "It told him, too, of the village itself, the shape of a "
        "compound, the sound of a market, the ordinary rhythm of "
        "people who woke and worked and slept and woke again inside "
        "walls he had never seen, because the boy would need some "
        "picture of the world beyond these roots eventually, and a "
        "picture built slowly, in pieces, seemed a kinder architecture "
        "than one delivered all at once and left to collapse under its "
        "own unfamiliar weight."
    )},
    {"type": "body", "text": (
        "It told him, more carefully, of the fear that village carried "
        "toward anything that came out of Oso, old laws and older "
        "griefs it did not yet try to explain in full, only enough for "
        "him to understand that walking toward that village as he was "
        "now would not be met with open arms, whatever his own small "
        "heart wanted to believe about a mother he had never touched."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The boy absorbed this in the particular stillness the entity "
        "had come to recognize as his way of holding something too "
        "large to react to all at once, turning the words over the way "
        "he turned over every new stone he found, checking each side of "
        "it before deciding what shape it actually was."
    )},
    {"type": "body", "text": (
        "\"A brother,\" he said finally, testing the word. \"Does he "
        "have my name.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The entity found, for the first time in longer than it cared "
        "to measure, that it did not have a ready answer prepared. It "
        "had answered questions about hunger, about fear, about the "
        "shape of the roots and the reach of its own attention, "
        "hundreds of times over without hesitation. This one small "
        "question, asked with no weight behind it beyond a child's "
        "plain curiosity, found a gap in its preparation that nothing "
        "else had managed to find in months."
    )},
    {"type": "body", "text": (
        "\"You do not have a name,\" it said, choosing the plain truth "
        "because it could not immediately locate a kinder one worth "
        "trusting. \"The village names its children on the eighth day, "
        "in a rite meant to welcome them fully into the world. You were "
        "carried away before that day arrived. Your brother received "
        "his name. You did not.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "VESSEL: FIRST DISCLOSURE OF MATERNAL AND FRATERNAL EXISTENCE, FULL. FIRST DIRECT QUESTION REGARDING PERSONAL IDENTITY. NO PRIOR PROTOCOL FOR THIS RESPONSE."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: OSO — THE QUESTION THE ENTITY COULD NOT ANSWER LIGHTLY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"Then what do I call myself,\" the boy asked, and there was "
        "no self pity in it, only the plain, searching confusion of a "
        "child trying to understand a gap in the world he had not "
        "known existed until this exact moment."
    )},
    {"type": "body", "text": (
        "The entity turned the question over with more care than it "
        "had turned over almost anything else in this long, patient "
        "season. It could give him a name easily enough. It had shaped "
        "nearly everything else about him already, his hunger, his "
        "growth, the very shape of the words he was only now learning "
        "to trust. A name would cost it nothing to invent."
    )},
    {"type": "body", "text": (
        "That was precisely what gave it pause."
    )},
    {"type": "body", "text": (
        "It turned the memory of every other thread it had ever built "
        "over in comparison, the dibia, hollowed out by service until "
        "there was nearly nothing left of the man who had once "
        "diagnosed abiku by daylight. Zara, marked and exiled, carrying "
        "a piece of the entity's attention out into a world she had "
        "never asked to carry it into. Elder Maka, hiding a stolen "
        "weight beneath her own skin because setting it down honestly "
        "had never once been offered to her as a choice. Every thread "
        "the entity had ever built had been built for its own purposes "
        "first, whatever comfort or use the human wearing it eventually "
        "found in the arrangement. It had never once asked itself, "
        "before this small, plain question arrived, whether the vessel "
        "deserved to be spared that same pattern."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A name given by the entity would be one more thread of "
        "itself woven into a boy who had already, in small unbidden "
        "ways, begun reaching for things the entity had never planted "
        "in him at all. A name earned from the mother who had carried "
        "him, or even a name he chose for himself once he understood "
        "enough of the world to choose wisely, would belong to him in a "
        "way nothing the entity had ever given him truly had. The "
        "entity did not know, weighing the two paths honestly, which "
        "one it actually wanted to choose, and found the not knowing "
        "itself strange enough to sit with rather than resolve too "
        "quickly."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Not yet,\" it told him, the same two words it had offered "
        "him once already at the boundary of Oso, though this time they "
        "carried a different weight, less a refusal than an honest "
        "admission that the answer was not fully the entity's to give. "
        "\"A name is not a small thing to hand to someone. I would "
        "rather choose carefully than choose quickly, and I have not "
        "yet decided whose choice this ought to be.\""
    )},
    {"type": "body", "text": (
        "The boy accepted this the way he had learned to accept every "
        "unfinished answer, filing it away beside the other things he "
        "was still waiting to understand, and went back to his stones, "
        "arranging and rearranging them in the dark while the entity "
        "sat with a question it had never once expected a vessel of its "
        "own careful making to hand back to it unanswered."
    )},
    {"type": "body", "text": (
        "It watched him work at his small collection a long while, "
        "the smooth stone from the root wall still at the center of "
        "every arrangement he built, and found itself wondering, not "
        "for the first time but with a new and unfamiliar clarity, "
        "whether the boy would grow into a mind grateful for everything "
        "the entity had given him, or a mind that eventually resented "
        "every one of those same gifts for having been given rather "
        "than earned. It did not know which outcome it was actually "
        "hoping for, and that uncertainty, more than any single "
        "question the boy had asked tonight, told the entity something "
        "true about how far this careful season of shaping had already "
        "carried both of them from where it began."
    )},
    {"type": "body", "text": (
        "A name was a small thing to withhold, measured against "
        "everything else it had already given or taken from this one "
        "small life. It found, turning the thought over one final time "
        "before letting the boy drift toward sleep, that it minded the "
        "smallness of that particular withholding more than it minded "
        "almost anything else it had ever chosen not to say."
    )},

    {"type": "blank", "text": ""},
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
    print("  THE DARK RISE — Episode 34: \"The Nameless Boy\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_34.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_34.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
