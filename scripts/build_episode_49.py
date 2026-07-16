#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 49: "What the Boundary Will Allow"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-25: Episode 49 turns the promise from Episode 48 into an
actual plan. The entity and Chibundu agree on the shape of a meeting —
brief, at night, at the boundary itself rather than deeper in Idoro,
entity close enough to intervene if anything goes wrong. On the Idoro
side, Osadebe has to solve a practical problem the entity never has to
consider: Chidebe's garrison patrols that exact ground every night on a
fixed schedule, and letting the boy approach unannounced risks a
confrontation neither side wants. Rather than deceive a man who has
earned real trust, Osadebe tells Chidebe the truth and asks him to stand
his patrol down for one night, a request that tests exactly how far the
captain's disciplined loyalty to his orders can bend toward simple human
mercy. The episode closes with everything arranged for the following
night — and Amara learning, from a nervous trader passing through, that
the scholar never actually left the area at all, and has been quietly
watching Idoro's boundary from a discreet distance ever since her
request was refused.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_49.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Nine"},
    {"type": "title_ep_name", "text": "What the Boundary Will Allow"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — ASKING A SOLDIER TO STAND DOWN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe found Chidebe reviewing the night's patrol roster by "
        "lamplight and asked for a private word before he could talk "
        "himself out of the honesty he had already decided, walking "
        "over, was the only approach that would not eventually cost "
        "them both more than it saved. \"Tomorrow night, I am asking you to pull "
        "your patrol back from the tree line for two hours,\" he said. "
        "\"I will not pretend this is a small request, or explain it "
        "away as routine. I am asking because a mother is going to see "
        "her son for the first time in over a year, and I do not want "
        "your men's presence to be the reason that meeting ends in "
        "bloodshed neither of them deserves.\""
    )},
    {"type": "body", "text": (
        "Chidebe set the roster down slowly, weighing the request with "
        "the same flat, careful attention he brought to everything "
        "that fell outside the clean shape of his written orders. \"You "
        "understand what you are asking,\" he said, not quite a "
        "question. \"You are asking me to leave the one piece of "
        "ground I was specifically sent to hold, unguarded, on the "
        "same night the thing my orders describe as dangerous is "
        "expected to be standing on it.\""
    )},
    {"type": "body", "text": (
        "\"I am asking exactly that,\" Osadebe admitted, meeting his "
        "eyes without flinching from it. \"I could have found a "
        "gentler way to say it. I decided you had earned the plain "
        "version instead.\""
    )},
    {"type": "body", "text": (
        "\"My orders are to hold this boundary against foreign "
        "encroachment,\" Chidebe said finally. \"They say nothing about "
        "a village woman visiting her own child.\" He was quiet a "
        "moment longer. \"I will grant you your two hours, Captain. "
        "Not because I fully understand what I am permitting. Because "
        "I have watched this village long enough now to know the "
        "difference between an order that protects people and an "
        "order that would simply get in the way of something that was "
        "never actually anyone's enemy to begin with.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe thanked him with more feeling than he had expected "
        "to carry into the exchange, and found, walking back toward "
        "Amara's compound to deliver the news, that some part of him "
        "had genuinely doubted, until that exact moment, whether a "
        "soldier this disciplined could bend for a reason this "
        "entirely unmilitary. It gave him a small, unfamiliar hope for "
        "everything the crown's growing presence in Idoro might still "
        "become, if enough of the men wearing its colors turned out to "
        "carry Chidebe's particular sense of where duty actually ended "
        "and cruelty quietly began."
    )},
    {"type": "body", "text": (
        "Amara received the news from Osadebe with a stillness that "
        "did not fully break until she was alone, and only then let "
        "herself feel the full, disorienting size of what tomorrow "
        "night would actually be. She had imagined this reunion, in "
        "some form, nearly every day for over a year. She found now "
        "that none of her imagining had prepared her for how it would "
        "actually feel to have a date, a place, and a number of hours "
        "attached to a hope she had never quite let herself believe "
        "would arrive at all."
    )},
    {"type": "body", "text": (
        "She told only Obi and Zara, deciding, after turning the "
        "question over more than once, that a wider circle would only "
        "invite a wider argument about whether this should be allowed "
        "to happen at all. Zara took the news quietly, still carrying "
        "the particular exhaustion the boundary had left in her, and "
        "asked only whether Amara wanted company for the walk there. "
        "\"No,\" Amara said, gently. \"You have already given this "
        "family more than anyone should have to give twice. Whatever "
        "happens tomorrow night, it should be mine and his to carry, "
        "not yours as well.\""
    )},
    {"type": "body", "text": (
        "Obi said little when she told him, turning the news over in "
        "the particular silence he had learned, across a hard year, "
        "meant he was feeling something too large to speak plainly "
        "yet. \"I want to come,\" he said finally. \"Not to the "
        "boundary. I do not think either of you needs me standing "
        "there. But close enough to walk you home after, whatever "
        "happens.\" Amara did not refuse him, grateful for a kind of "
        "presence that asked for nothing except to be allowed to wait, "
        "steady and unhurried, the way he had learned to wait for her "
        "through every hard season this last year had asked of them "
        "both."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — PRACTICING FOR A NIGHT THAT ACTUALLY COMES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity and Chibundu spent the "
        "day building the shape of the meeting the way they had once "
        "built the shape of a moved stone, piece by careful piece. The "
        "boundary itself, not deeper in Idoro. Night, when fewer eyes "
        "could witness what neither of them yet knew how to explain to "
        "a wider village. A fixed, short span of time, agreed on "
        "before either of them could let hope stretch it further than "
        "safety actually allowed."
    )},
    {"type": "body", "text": (
        "\"I will stay close,\" the entity told him, for what was "
        "likely the fourth time that day, aware the repetition served "
        "its own nerves nearly as much as his. \"Not between you. Close "
        "enough to reach you if something goes truly wrong, far enough "
        "that the meeting still belongs to the two of you rather than "
        "to me standing over it.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Chibundu practiced holding still through the telling of it, "
        "the same deliberate stillness he had learned watching Chidebe "
        "stop exactly at the last stone weeks before, and asked, once, "
        "the only question that seemed to matter more than any of the "
        "careful logistics laid out around it. \"What if she is afraid "
        "of me,\" he said. \"Not of what I am. Of me. My face. My "
        "hands. What I did to those men at the boundary.\""
    )},
    {"type": "body", "text": (
        "The entity had turned that same fear over more than once "
        "itself and offered him the only honest answer it had found. "
        "\"She might be, for a moment. Fear and love are not opposites. "
        "They have lived in the same house inside her since the night "
        "you were carried away from her. I do not think either of us "
        "gets to promise you she will feel nothing but joy. I think "
        "the only thing worth promising is that whatever she feels, "
        "she chose to come anyway, and that choosing is not nothing.\""
    )},
    {"type": "body", "text": (
        "Chibundu turned that answer over the way he turned over "
        "every stone before deciding where it belonged, quiet for a "
        "long stretch afterward. \"What should I say first,\" he "
        "asked. \"I have thought of a hundred things and none of them "
        "feel large enough for how long I have waited to say any of "
        "them.\""
    )},
    {"type": "body", "text": (
        "\"You do not need the largest words,\" the entity told him. "
        "\"You have spent your whole life so far learning to hold "
        "enormous things carefully. This is one more enormous thing. I "
        "do not think it needs a speech. I think it only needs you, "
        "standing there, being exactly who you already are.\""
    )},
    {"type": "body", "text": (
        "\"And if I forget everything I meant to say the moment I "
        "see her,\" Chibundu pressed, \"what then.\""
    )},
    {"type": "body", "text": (
        "\"Then you will have stood in front of your mother and felt "
        "too much to speak,\" the entity said. \"I have watched three "
        "long centuries of humans do exactly that at moments far "
        "smaller than this one. It has never once meant the moment "
        "failed. It usually only means the moment was real.\""
    )},
    {"type": "body", "text": (
        "VESSEL: FIRST SCHEDULED, DELIBERATE PHYSICAL REUNION WITH "
        "MATERNAL FIGURE. LOGISTICS CONFIRMED AND AGREED BY BOTH "
        "PARTIES. EMOTIONAL PREPARATION INCOMPLETE BY DEFINITION — NO "
        "PRIOR PRECEDENT AVAILABLE TO DRAW FROM."
    )},
    {"type": "body", "text": (
        "They sat with the plan a long while after that, the entity "
        "turning over every remaining risk it could still name and "
        "several it privately suspected it could not, until word "
        "reached them, carried on the same thin thread of ambient "
        "unease the entity now kept trained on Idoro at all times, "
        "that Amara had learned something that evening the entity had "
        "not yet learned itself. A trader passing through, nervous and "
        "eager to unburden himself of gossip that clearly frightened "
        "him more than it interested him, had told her plainly: the "
        "scholar had never actually left. She had simply stopped "
        "asking, and started watching, from a discreet distance, "
        "exactly the ground her request had been refused for."
    )},
    {"type": "body", "text": (
        "The entity sat with that new fact a long while, weighing it "
        "against a plan already set and a boy already hoping too hard "
        "to easily be talked back down from it, and understood, "
        "turning it over from every angle it could manage, that "
        "tomorrow night would now have to hold two very different "
        "kinds of watching at once, only one of which either of them "
        "had actually agreed to."
    )},
    {"type": "body", "text": (
        "It considered calling the meeting off, and discarded the "
        "thought almost as quickly as the boy's face rose unbidden "
        "behind it, a boy who had waited a year and a name's worth of "
        "patience for exactly this chance. It considered telling him "
        "nothing of the scholar at all, and discarded that too, aware "
        "that whatever trust it had built these last careful weeks "
        "would not survive a single convenient silence dressed up as "
        "protection, however well intentioned that protection might "
        "feel in the moment. It settled, in the end, on the only path "
        "that had actually served it since it first chose honesty over "
        "concealment: telling him plainly, and letting him decide, "
        "together with the entity, whether the risk still felt worth "
        "carrying."
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
    print("  THE DARK RISE — Episode 49: \"What the Boundary Will Allow\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_49.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_49.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
