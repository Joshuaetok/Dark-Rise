#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 9: "The Reckoning"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-16: Episode 9 picks up the morning after Episode 8. Amara
visits Zara to check on her and the two women are forced to cover for each
other when a neighbor notices Zara's bandaged feet, a lie that costs Zara
more than she can keep paying. She tells Amara she must confess to Elder
Maka, and Amara, unlike Obi, lets her go without argument. In Oso, the
entity reads the rising tension bleeding out of the village as fuel, and
recalculates its plan for the Zara thread now that exposure has become more
likely, choosing patience over haste. Zara tells Elder Maka everything,
confirming from an independent source what Elder Maka had only suspected
about Kene, and Elder Maka goes straight to Amara's compound. The episode
ends mid confrontation, with Elder Maka naming what she now believes in
front of Amara and Obi both.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_09.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Nine"},
    {"type": "title_ep_name", "text": "The Reckoning"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE WOUNDS WOULD NOT LET HER HIDE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara went to Zara's hut at first light, telling herself she "
        "only wanted to see with her own eyes that the woman had "
        "survived the night, and finding, once she arrived, that some "
        "part of her had come for a colder reason too. If Zara had been "
        "moved once against her own will, Amara needed to know whether "
        "the moving had left a mark that could be read, the way Kene's "
        "darkened eyes had been a mark only she had known to look for."
    )},
    {"type": "body", "text": (
        "She found Zara sitting on her stool with both feet freshly "
        "wrapped in cloth, her hands unsteady around a cup of untouched "
        "water. Neither of them spoke at first. There was an "
        "awkwardness between them now that had not existed before last "
        "night, the particular discomfort of two women who had each "
        "learned something about the other that neither had chosen to "
        "share."
    )},
    {"type": "body", "text": (
        "They had barely exchanged a dozen words, a careful accounting "
        "of the night before, when a neighbor's wife put her head "
        "through the open doorway to ask after a fever remedy and "
        "stopped instead at the sight of Zara's bound feet."
    )},
    {"type": "body", "text": (
        "\"What happened to you,\" the woman asked, already reaching for "
        "the older, easier fear the village kept close these days. "
        "\"Did something in that forest reach as far as your own hut.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara opened her mouth, and for one unguarded moment nothing at "
        "all came out of it, and Amara heard herself speaking into the "
        "gap before she had decided to."
    )},
    {"type": "body", "text": (
        "\"She walked barefoot to my compound in the dark to sit with "
        "me,\" Amara said. \"Foolish of her, and foolish of me not to "
        "send her home with a lamp. Nothing reached her. Only bad "
        "ground.\""
    )},
    {"type": "body", "text": (
        "The neighbor accepted it, the way people accept any explanation "
        "that lets them stop being afraid a little sooner, and left with "
        "her fever remedy and her relief intact. When her footsteps had "
        "faded, Zara set down her cup with hands that had not stopped "
        "shaking."
    )},
    {"type": "body", "text": (
        "\"You lied for me,\" she said. \"As easily as breathing.\""
    )},
    {"type": "body", "text": (
        "\"I have had practice,\" Amara said, and did not soften it, "
        "because Zara deserved to know exactly what kind of woman had "
        "just covered for her."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara looked down at her wrapped feet for a long moment. \"I "
        "told your husband I would wait until I could speak plainly. I "
        "can speak plainly now, and every hour I do not go to Elder Maka "
        "is an hour I am also lying, only with my silence instead of my "
        "mouth. I do not think I can carry that the way you carry "
        "yours.\""
    )},
    {"type": "body", "text": (
        "Amara felt the old instinct rise in her, the one that wanted to "
        "argue, to delay, to buy one more day the way she had bought so "
        "many since the twins were born. She let it pass through her "
        "instead."
    )},
    {"type": "body", "text": (
        "\"Then go,\" Amara said. \"I will not ask you to carry a "
        "silence that is eating you alive simply because it would be "
        "convenient for me. You owe me nothing, Zara. You owe Elder Maka "
        "even less than you think you do. Go and tell her what "
        "happened, and tell her plainly, and let whatever comes of it "
        "come.\""
    )},
    {"type": "body", "text": (
        "It cost her something to say it, more than she let show on her "
        "face. But Amara had watched Obi try to hold another person's "
        "truth shut with a promise extracted in fear, and she would not "
        "make the same mistake twice in one household."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY CHOSE NOT TO RISK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity tasted the shift in the "
        "village long before either woman had finished speaking, the way "
        "a man standing in a river feels the water rise around his "
        "ankles before he understands a storm has broken somewhere "
        "upstream."
    )},
    {"type": "body", "text": (
        "Fear was moving through Idoro again, thinner and more anxious "
        "than the fear the cleansing rite had produced, but wider, "
        "touching more households at once. A secret passed between three "
        "people generates a certain pressure. A secret about to be "
        "confessed to the one woman in the village with the authority to "
        "act on it generates something sharper."
    )},
    {"type": "body", "text": (
        "The entity drank what reached it and considered what the shift "
        "meant for the thread it had opened in the midwife's blood."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It had planned to choose its own night, quietly, without any "
        "human eye positioned to interrupt a second time. That plan had "
        "assumed the midwife's silence would hold a while longer. Now "
        "the old woman who had once buried her own returned son was "
        "about to be told, in plain words, that something in Oso could "
        "walk a grown woman out of her bed and nearly to the tree line "
        "without her ever waking."
    )},
    {"type": "body", "text": (
        "A door watched openly was still a door. But a door watched by "
        "someone who had already killed one vessel with her own hands "
        "was a door that would be guarded, perhaps sealed, perhaps torn "
        "out entirely the way a farmer burns a single infected stalk to "
        "save the field around it."
    )},
    {"type": "body", "text": (
        "The entity weighed the cost of moving the thread again soon, "
        "before any such guard could be set, against the greater cost of "
        "being caught mid act by a woman with the will and the history "
        "to end it. It chose, as it had chosen with the dibia and would "
        "choose again with anything patient enough to be worth keeping, "
        "to wait. Better a door left merely open than a door forced and "
        "lost."
    )},
    {"type": "body", "text": (
        "In the hollow, the vessel's hair had begun to darken from the "
        "pale infant down it had carried since birth into something "
        "coarser, older, more suited to the body it was quickly becoming. "
        "The entity noted the change, filed it beside the other changes, "
        "and turned the whole of its patient attention back toward "
        "Idoro, waiting to learn exactly how much the coming confession "
        "would cost it."
    )},
    {"type": "body", "text": (
        "It had survived three centuries by knowing the difference "
        "between a door worth forcing and a door worth simply "
        "outwaiting. Every human it had ever touched believed their own "
        "moment of crisis was the whole of the story, urgent and final. "
        "The entity had watched enough such moments pass, unremarked, "
        "into the ordinary business of living, to know that patience "
        "cost it nothing a single lost door could not repay a season "
        "later."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "RISK REASSESSMENT: SECOND THREAD LIKELY TO BE REPORTED. ACTIVATION DELAYED. VESSEL DEVELOPMENT CONTINUES UNINTERRUPTED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ELDER MAKA NAMED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara found Elder Maka grinding camwood alone behind her own "
        "compound, and told her everything, plainly, the way she had "
        "promised Amara she would. The tingling in her hands. The walk "
        "she did not remember beginning. Obi's grip on her arm three "
        "strides from the tree line. Her own bare feet, cut open on "
        "ground she had crossed a thousand times before without ever "
        "once bleeding."
    )},
    {"type": "body", "text": (
        "Elder Maka listened without interrupting, her hands going still "
        "on the grinding stone somewhere in the telling, and when Zara "
        "finished, the old woman sat for a long moment with an "
        "expression Zara could not read at all."
    )},
    {"type": "body", "text": (
        "\"Who else knows,\" Elder Maka asked finally."
    )},
    {"type": "body", "text": (
        "\"Obi. And Amara.\""
    )},
    {"type": "body", "text": (
        "\"And how long have they known.\""
    )},
    {"type": "body", "text": (
        "\"Since that same night.\""
    )},
    {"type": "body", "text": (
        "Elder Maka's jaw tightened, and something old and grim settled "
        "over her face, the look of a woman watching a suspicion she had "
        "carried for days finally grow solid enough to hold. \"Then they "
        "have known for two full days and told no one. And you would "
        "have kept silent longer still, if the neighbor's wife had not "
        "seen your feet this morning.\""
    )},
    {"type": "body", "text": (
        "\"I came as soon as I could bear to,\" Zara said."
    )},
    {"type": "body", "text": (
        "\"I do not blame you for the fear,\" Elder Maka said, rising "
        "slowly, her knees protesting the movement the way they always "
        "did now. \"I blame the ones who asked you to carry it alone.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She left Zara sitting among the scattered camwood powder and "
        "walked, faster than her age should have allowed, straight "
        "toward Amara's compound."
    )},
    {"type": "body", "text": (
        "Amara was drawing water when Elder Maka arrived, and one look "
        "at the old woman's face told her the morning's small mercy to "
        "Zara had already found its way home to her own door. Obi came "
        "out from the yard behind her, drawn by the sound of Elder "
        "Maka's approach, and the three of them stood in a loose, tense "
        "triangle in the middle of the compound while a curious neighbor "
        "or two slowed their steps nearby, sensing something without yet "
        "knowing what."
    )},
    {"type": "body", "text": (
        "\"Zara has told me everything,\" Elder Maka said, without any "
        "greeting at all. \"A grown woman moved in her sleep toward Oso "
        "like a puppet on a string she never felt. And you both knew, "
        "and said nothing to me, while I sat in my own compound "
        "believing there was only one door left to watch.\""
    )},
    {"type": "body", "text": (
        "Amara set down the water jar carefully, buying herself one "
        "more breath before she had to answer. \"Elder Maka—\""
    )},
    {"type": "body", "text": (
        "\"Do not,\" Elder Maka said, raising one hand, her eyes moving "
        "from Amara's face to the basket where Kene lay sleeping in the "
        "shade, and back again, with a weight that made Amara's whole "
        "body go cold. \"I have buried a child that came back wrong "
        "once in my life. I will not be lied to twice by the same "
        "silence. There are two doors into this village now, and one of "
        "them is standing in a basket not three steps from where we are "
        "arguing, and I want to know, plainly, what you saw in your own "
        "son's eyes the night he screamed.\""
    )},
    {"type": "body", "text": (
        "The compound had gone entirely silent. Even the neighbors "
        "pretending not to listen had stopped pretending to do anything "
        "else. Obi's hand found Amara's arm, whether to steady her or "
        "himself she could not tell, and Amara stood in the space Elder "
        "Maka's question had opened, weighing every version of the "
        "truth she might offer against the life it could cost her son "
        "if she chose wrong."
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
    print("  THE DARK RISE — Episode 9: \"The Reckoning\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_09.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_09.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
