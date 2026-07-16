#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 35: "What He Was Not Taught"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-11: Episode 35 pays off the Episode 20 thread of the
trader's story spreading north — Idoro's canoe trade begins drying up as
river towns grow wary of a village the crown itself now watches, and
Osadebe realizes his own presence has become part of what frightens
outsiders away. The new council holds its first real test, with Amara
pushing honesty over concealment and Osadebe offering to personally vouch
for the village upriver. In Oso, the vessel is caught repeating a soft
word to himself that the entity never taught him and cannot trace to
anything it planted — the first real gap between what it has shaped and
what the boy actually is. The episode ends on the entity recognizing
something older than itself pressed into the shape of that word, a
pressure it has felt only at the far edges of Oso in three centuries and
never once been able to name.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_35.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Five"},
    {"type": "title_ep_name", "text": "What He Was Not Taught"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE PRICE OF BEING WATCHED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The canoe did not stop. Obi watched it from the riverbank the "
        "way he had once watched his own stall go untouched at market, "
        "a small private wound reopening in a place he had thought "
        "already scarred over, as the trader who usually beached his "
        "boat at Idoro's landing every third morning lifted his pole "
        "instead and pushed on toward the next village downriver "
        "without so much as slowing."
    )},
    {"type": "body", "text": (
        "He was not the first. Three canoes in ten days had done the "
        "same, and the fish Obi had smoked to trade for salt and cloth "
        "sat drying past their worth in his own compound, because a "
        "village that had once been merely feared by its neighbors for "
        "an old law about twins was now, according to whatever story "
        "had traveled upriver ahead of him, a village the crown itself "
        "sent soldiers to watch."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe heard the same story secondhand that evening, sitting "
        "at the edge of the compound Amara had given him, and felt the "
        "shape of it settle into his stomach like a stone he had "
        "swallowed without meaning to. He had come to Idoro to learn "
        "the truth and to watch it carefully. He had not considered, "
        "riding south with his small unremarkable party, that his own "
        "presence would become part of the story frightening honest "
        "traders away from a village that had done nothing to deserve "
        "losing its salt and cloth on top of everything else it had "
        "already lost."
    )},
    {"type": "body", "text": (
        "\"They do not fear Oso,\" Amara told him plainly, when he "
        "raised it with her the next morning. \"Or they do, but that "
        "fear is old and it has a shape they know how to live around. "
        "What frightens them now is newer. A crown that sends a captain "
        "to watch a village means, to a river trader, that the crown "
        "expects something bad enough to be worth watching. They are "
        "not wrong to be afraid of that. I am not certain I disagree "
        "with them.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The council met that afternoon under the mango tree that had "
        "once served only Elder Maka's judgments, now rearranged into a "
        "rough half circle of stools that still did not sit quite right "
        "together, four people still learning the shape of sharing "
        "authority none of them had asked to share. Ozoemena came "
        "carrying water for the others rather than an opinion, true to "
        "his promise to serve through labor rather than judgment, and "
        "said nothing until Amara asked him directly what he thought."
    )},
    {"type": "body", "text": (
        "\"I do not trust my own thinking anymore,\" he admitted, "
        "setting the water down carefully. \"But if you are asking "
        "whether I believe hiding this from the traders would work "
        "better than telling them the truth, I would remind everyone "
        "here that hiding is the thing that got the dibia killed and "
        "put me in this circle instead of leading it. I have had my "
        "fill of hiding.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe offered the only thing he had that might weigh "
        "against a rumor: himself, and the crown's name behind him. He "
        "would travel the river road personally to the two nearest "
        "market towns, he said, and tell the traders plainly what the "
        "crown's captain had actually been sent to do, which was to "
        "watch and report, not to punish or quarantine a village that "
        "had asked for nothing and been given a great deal of grief in "
        "return. It would not undo the story already traveling ahead of "
        "him, but a captain's own mouth carried a different weight than "
        "a trader's secondhand telling."
    )},
    {"type": "body", "text": (
        "\"And if they ask you what exactly you are watching,\" Amara "
        "said, \"what will you tell them.\""
    )},
    {"type": "body", "text": (
        "Osadebe held her eyes a moment before answering, aware that "
        "every answer he had ever given anyone since arriving in Idoro "
        "had cost this family something, and that this one would be no "
        "different. \"The truth, in the smallest amount that keeps "
        "anyone from panicking and keeps you and your household safe. I "
        "have learned that much from watching what happens here when "
        "truth is rationed out in the wrong order.\""
    )},
    {"type": "body", "text": (
        "It was not a promise that satisfied everyone at the mango "
        "tree, but it was the first decision the new council had made "
        "together since Osadebe's arrival forced it into existence, and "
        "Amara found something almost steadying in watching four people "
        "who agreed on very little agree, at least, that a lie built to "
        "buy a little peace tended, in this particular village, to cost "
        "considerably more than it saved."
    )},
    {"type": "body", "text": (
        "As the council broke apart, Amara noticed Adaugo standing at "
        "the edge of the clearing, close enough to have heard all of "
        "it, watching her mother's empty stool the way a person watches "
        "a door they have not yet decided whether to walk back through. "
        "She had come nearer to the compound these last weeks than she "
        "had in months, though never quite near enough to cross the "
        "threshold, and Amara let her be, remembering what it had cost "
        "her own family to have every private grief argued over in "
        "public before it was ready."
    )},
    {"type": "body", "text": (
        "Osadebe found her there afterward and asked, carefully, "
        "whether she thought Elder Maka would ever be given a seat at "
        "that half circle of stools again. Amara considered the "
        "question longer than he expected before answering. \"That is "
        "not mine to decide, or yours. But I have learned that a "
        "village which only knows how to cast people out rarely "
        "survives long enough to need anyone left to cast out. Idoro is "
        "learning that lesson slower than I would like. It is still "
        "learning it.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE WORD IT NEVER GAVE HIM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the boy had taken to murmuring a "
        "single soft word over his stones while he arranged them, low "
        "and rhythmic, the way a much older child might hum without "
        "noticing he was doing it, and the entity, which had shaped "
        "nearly every sound that had ever left his mouth, did not "
        "recognize the word at all."
    )},
    {"type": "body", "text": (
        "It was not Mama. It was not brother, or Idoro, or any of the "
        "small plain words it had spent the last handful of days "
        "carefully building into him. It was shorter than those, two "
        "soft syllables that rose and fell like breath, and the boy "
        "said it the way he said his own name for the smooth stone from "
        "the root wall, as though it already belonged to something and "
        "he had simply been the one to notice."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"Where did you hear that,\" the entity asked him, keeping its "
        "voice as even as it kept every other question it had learned "
        "to ask him gently rather than sharply, though something in it "
        "had gone very still, the particular stillness of a thing "
        "listening for a second sound beneath a first one."
    )},
    {"type": "body", "text": (
        "The boy looked up from his stones, unbothered, the way he "
        "looked up from anything that did not yet strike him as "
        "important. \"I did not hear it,\" he said. \"It was already "
        "there. Like the stone was already smooth before I picked it "
        "up.\""
    )},
    {"type": "body", "text": (
        "He went back to arranging his stones and said the word again, "
        "unprompted, folding it into the small private rhythm of his "
        "play as though it cost him nothing at all, while the entity "
        "turned the sound over inside itself with a care it had not "
        "needed to spend on anything the boy had said or done in weeks."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "It searched every corner of what it had given him. The shapes "
        "and patterns taught directly into his mind since before he "
        "could speak. The handful of true words it had offered him "
        "these last days, chosen carefully, each one accounted for. The "
        "half language it sometimes let slip into its own long private "
        "thinking, which the boy should have had no way to reach, "
        "sealed as it had always kept that part of itself, even from "
        "him."
    )},
    {"type": "body", "text": (
        "None of it matched. The word the boy kept saying belonged to "
        "none of them, and the entity, which had spent three centuries "
        "coming to know the exact shape and weight of its own hunger, "
        "found that it did not entirely know what it was hearing, only "
        "that it had felt something like it before, at the very furthest "
        "edges of Oso, in the older, deeper dark past even the reach of "
        "its own roots, a pressure it had always assumed belonged to "
        "the forest itself and had never once thought to name."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "VESSEL: FIRST VERBAL PATTERN NOT TRACEABLE TO ANY TAUGHT "
        "SOURCE. ORIGIN UNKNOWN. RECURRENCE UNPROMPTED, THREE SEPARATE "
        "INSTANCES WITHIN ONE NIGHT."
    )},
    {"type": "body", "text": (
        "It had told itself, across every one of these last careful "
        "days, that the boy's unclaimed will was a small and gentle "
        "thing, a grain of something not planted by its own hand, "
        "worth watching but never worth fearing, a child reaching "
        "for a mother's name out of nothing but a child's plain "
        "longing. It had not, until this exact moment, considered that "
        "some of what grew in him unclaimed might not be coming from "
        "nowhere at all, but from somewhere older than the entity "
        "itself, somewhere it had shared this forest with in silence "
        "for three hundred years without ever once being asked what "
        "else might be listening."
    )},
    {"type": "body", "text": (
        "It considered, and discarded, the idea of asking him to stop "
        "saying it. That would require explaining why, and the entity "
        "was no longer certain explaining why would not simply teach "
        "the boy that the sound carried a weight worth testing further, "
        "the exact opposite of what three careful days of honesty had "
        "been meant to accomplish. Silence, for once, felt like the "
        "safer shape of patience, though it did not feel like patience "
        "at all. It felt like waiting for a door to open on a room it "
        "had never once been permitted to enter."
    )},
    {"type": "body", "text": (
        "The boy yawned, arranged his final stone, and let the word "
        "trail off into sleep the way he let everything trail off into "
        "sleep lately, unaware that the sound leaving his own mouth had "
        "just done something no single word he had spoken before it "
        "ever managed. It had made the thing that raised him afraid."
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
    print("  THE DARK RISE — Episode 35: \"What He Was Not Taught\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_35.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_35.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
