#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 33: "The New Council"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-09: Episode 33 brings Osadebe back to Idoro, no longer a
passing visitor but a permanent presence attached to the village by royal
decision. His return forces the question the council has avoided for
weeks: who actually speaks for Idoro now. Rather than crown a single
successor the way it crowned Ozoemena, the village settles on something
it has never tried before, a shared council with Amara given a real seat
at last, her instinct for the truth too proven now to keep sidelining.
In Oso, the entity continues its careful, unhurried work, unaware that
the village it has spent months quietly destabilizing has just made
itself, structurally, harder to destabilize the same way twice. The
episode ends with Osadebe asking the one question Amara has been dreading
since his arrival: what, exactly, is Elder Maka's condition, and why has
no one in Idoro been willing to name it to him plainly.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_33.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Three"},
    {"type": "title_ep_name", "text": "The New Council"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE VILLAGE BUILT INSTEAD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe returned to Idoro with a small cart of his own "
        "belongings and the particular resigned patience of a man who "
        "had been told, in no uncertain terms, that this posting was "
        "not a temporary one, and the village he rode back into looked, "
        "he thought, exactly like a place still deciding what shape to "
        "settle back into after being bent nearly to breaking twice in "
        "one season."
    )},
    {"type": "body", "text": (
        "He had chosen a small hut near the compound's edge, close "
        "enough to the center of the village to see most of its daily "
        "business, far enough apart that no one household could claim "
        "him as its own particular ally, a positioning Amara suspected "
        "was as deliberate as everything else about the man."
    )},
    {"type": "body", "text": (
        "The council met the evening of his return, and this time no "
        "one stood to claim the whole of Elder Maka's old authority for "
        "himself. The lesson of Ozoemena sat too fresh in every mind "
        "present for anyone to trust a single voice again so soon."
    )},
    {"type": "body", "text": (
        "\"We tried one woman who knew too much and grew too certain "
        "of her own judgment,\" the old man who had once challenged "
        "Elder Maka said, standing before the gathered elders. \"We "
        "tried one man who knew too little and trusted his own "
        "confidence to fill the gap. I propose we stop trying one of "
        "anything. Let the council itself hold what authority remains, "
        "shared, argued over, slower to move and harder to fool because "
        "of it.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"And Amara,\" another elder said, \"who has been right about "
        "nearly everything this village refused to believe her about, "
        "should sit among us rather than stand outside waiting to be "
        "asked.\""
    )},
    {"type": "body", "text": (
        "Amara had not expected the proposal, and found herself, in "
        "the silence that followed it, weighing an old instinct to "
        "refuse against a newer, harder won understanding that refusing "
        "power out of caution was its own kind of danger now, in a "
        "village that had already paid twice for handing its authority "
        "to people less careful than they believed themselves to be."
    )},
    {"type": "body", "text": (
        "\"I will sit,\" she said finally. \"Not because I want the "
        "weight of it. Because I have carried a version of this weight "
        "alone for months already, and I would rather carry it beside "
        "people who might actually listen when I say something is "
        "wrong before it costs us another grave.\""
    )},
    {"type": "body", "text": (
        "Obi caught her eye across the gathering, and something passed "
        "between them that needed no words, the particular understanding "
        "of two people who had spent months learning exactly how much a "
        "single household could be made to carry alone before it broke. "
        "He did not ask for a seat of his own. He had learned, watching "
        "his wife these last months, that some weights were better "
        "carried by whichever partner already knew how to hold them "
        "without dropping anything else in the process."
    )},
    {"type": "body", "text": (
        "Ozoemena, seated at the very back where he had placed himself "
        "since the night he stepped down, spoke once more before the "
        "council dispersed. \"I have no claim left to a voice in this "
        "room,\" he said, \"but I would ask, if it is permitted, to "
        "serve wherever plain labor is needed rather than judgment. I "
        "have learned I trust my own judgment considerably less than I "
        "once did.\""
    )},
    {"type": "body", "text": (
        "No one objected, and the old man who had proposed the shared "
        "council nodded once, a small, grudging acknowledgment that a "
        "man capable of admitting that much aloud had already done more "
        "to earn a place in Idoro's future than most of the elders who "
        "had once granted him power so easily."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT A HARDER VILLAGE WAS WORTH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the shape of Idoro's "
        "new arrangement settle into place with the same unhurried "
        "attention it gave every shift in the village's structure, and "
        "found, weighing the change honestly, that it altered very "
        "little about the accounting that actually mattered to it."
    )},
    {"type": "body", "text": (
        "A shared council was harder to panic than a single frightened "
        "leader, harder to flatter into a single reckless mistake the "
        "way Ozoemena's pride had been flattered. That cost the entity "
        "something, in the long slow arithmetic of fear it had been "
        "running against this village for months. It did not cost "
        "enough to matter urgently. The village's remaining threads sat "
        "exactly where they had always sat, unguarded by any structure "
        "of council or crown, and a harder target reached more slowly "
        "was still, eventually, a target reached."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel practiced a new sentence to himself "
        "in the quiet hours, testing each word the way he tested every "
        "new shape before trusting it, and the entity, listening, felt "
        "the small private satisfaction of watching something it had "
        "shaped grow steadily closer to whatever it was eventually meant "
        "to become."
    )},
    {"type": "body", "text": (
        "It considered, briefly, whether Idoro's new arrangement was "
        "worth disrupting before it could fully take root, a well "
        "placed word through some still unguarded corner of the "
        "village, a fresh distraction planted at exactly the moment a "
        "fragile new structure was least equipped to withstand one. It "
        "decided against it, the same way it had decided against so "
        "many tempting, immediate actions across these last months. A "
        "council still finding its footing would make its own mistakes "
        "soon enough without any help. Every human structure it had "
        "ever watched eventually did."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "IDORO GOVERNANCE: DISTRIBUTED, HARDER TO DESTABILIZE VIA SINGLE ACTOR. THREAT LEVEL: UNCHANGED. VESSEL: SENTENCE COMPLEXITY INCREASING."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT OSADEBE ASKED PLAINLY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe found Amara alone at the well two days later, the "
        "same well where she had once learned exactly how far Idoro "
        "was willing to hold her at arm's length, and fell into step "
        "beside her without preamble."
    )},
    {"type": "body", "text": (
        "\"I have been here a week now,\" he said. \"Long enough to "
        "notice that everyone in this village speaks carefully around "
        "one name in particular. Elder Maka. I am told she was marked "
        "in some way during the events that cost this village its "
        "dibia. No one has told me plainly what that marking actually "
        "means.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara kept walking a moment longer before she answered, "
        "buying herself the same small span of thought she had learned "
        "to buy herself before every dangerous truth she had ever "
        "handed to someone new."
    )},
    {"type": "body", "text": (
        "She had known this question would come eventually, from the "
        "moment she first watched Osadebe's careful stillness settle "
        "over him at the boundary. A man who investigated for a living "
        "did not stop noticing careful silences simply because he had "
        "already been given one large truth to carry. She had simply "
        "hoped, in the quiet, unreasonable way a person hopes for a "
        "delay they know cannot last, that the question would come "
        "later rather than this soon."
    )},
    {"type": "body", "text": (
        "\"She carries a thread of the same presence you heard at the "
        "boundary,\" Amara said finally. \"She took it into her own "
        "body during a rite meant to save my son, rather than let it "
        "scatter somewhere she could not control. She has lived with "
        "it since, mostly alone, mostly unwatched, because the village "
        "already broke her once for carrying it and I am not certain "
        "how much more breaking a person can survive in a single "
        "season.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Osadebe absorbed this in silence, the same careful stillness "
        "he gave every difficult fact, and when he spoke again his "
        "voice was quieter than she expected."
    )},
    {"type": "body", "text": (
        "\"My king asked me to watch and report,\" he said. \"He did "
        "not ask me to decide, on my own judgment, which truths were "
        "safe to leave unreported. I do not yet know what I am required "
        "to do with what you have just told me. I am telling you that "
        "honestly, because you have earned honesty from me and I do "
        "not intend to spend it carelessly.\""
    )},
    {"type": "body", "text": (
        "\"Then decide carefully,\" Amara said. \"She is not the danger "
        "your report was sent to find. She is what is left of a woman "
        "this danger has already cost enough.\""
    )},
    {"type": "body", "text": (
        "\"What of her daughter,\" Osadebe asked. \"I have seen a young "
        "woman near that compound who watches her mother the way a "
        "person watches a wound they are not certain has finished "
        "bleeding.\""
    )},
    {"type": "body", "text": (
        "\"Adaugo,\" Amara said. \"She learned everything at once, the "
        "same day the whole village did. A dead brother she never knew "
        "she had. A mother marked by the same darkness she has spent "
        "her whole life being taught to fear. I do not think she has "
        "found her way back to solid ground yet, and I would ask you "
        "not to be the one who decides for her which ground is safe to "
        "stand on.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Neither of them had an answer ready for what came next, and "
        "they walked the rest of the way back into the village in a "
        "silence neither one hurried to break, both of them carrying, "
        "now, the same uneasy weight of a secret that had just stopped "
        "belonging only to Idoro."
    )},
    {"type": "body", "text": (
        "Amara thought, walking beside him, of every careful choice "
        "she had made about what to share and what to protect since "
        "the night her sons were born, and understood that Osadebe's "
        "presence had changed the shape of that calculation permanently. "
        "She was no longer only weighing her own family's safety "
        "against a village's fear. She was weighing it now against a "
        "throne's judgment as well, delivered by a careful man doing "
        "his honest best to serve two masters that did not always want "
        "the same thing from him."
    )},
    {"type": "body", "text": (
        "Whatever Osadebe eventually decided to write in his next "
        "report, Amara understood she would not be the one holding the "
        "pen, and that fact alone, after months of controlling every "
        "truth that left her own household, unsettled her more than "
        "she wanted to admit aloud to anyone, even to herself."
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
    print("  THE DARK RISE — Episode 33: \"The New Council\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_33.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_33.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
