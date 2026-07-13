#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 56: "The Third Door"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-01: Episode 56 returns to the dangling presence thread
last advanced in Episodes 38 and 39, when the entity first learned a
power older than itself had been reaching Chibundu directly through
his dreams. With the trading House's senior figure closing in, the
entity, having learned across this whole season that forbidding the
boy's own relationships only costs it trust, allows Chibundu to visit
the cold place again rather than binding him away from it. The
presence speaks more plainly than it ever has, warning of the
approaching threat in its own oblique, ancient register, and closes
the episode with a single unsettling claim: it has met a hunger like
the trading House's before, in another place, long before Idoro or
Oso ever existed in the shape they wear now, and it did not end well
for the ground that hunger reached.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_56.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Six"},
    {"type": "title_ep_name", "text": "The Third Door"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: PERMISSION, NOT DEFIANCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu felt the pull toward the cold place the same night "
        "Osadebe's rider reached Idoro, stronger than it had been in "
        "months, and for the first time since the entity had once tried "
        "to bind him away from it entirely, he asked permission before "
        "he let himself follow the pull anywhere. \"I want to go back,\" "
        "he said. \"Not around you this time. With you knowing.\""
    )},
    {"type": "body", "text": (
        "The entity felt the old instinct rise in it at once, the same "
        "instinct that had once woven a binding around his sleeping "
        "mind rather than trust him with a door it did not fully "
        "understand, and set the instinct aside deliberately, the way "
        "it had learned to set aside most of its old reflexes across "
        "this long season. \"Go,\" it said. \"I will not forbid it again. "
        "I learned the last time that forbidding you only taught you to "
        "go around me, and I would rather walk beside a door I cannot "
        "close than lose you to one I tried to.\""
    )},
    {"type": "body", "text": (
        "Chibundu closed his eyes and let the pull carry him down, past "
        "the warm, root laced dark of Oso's own hollow into something "
        "colder and stiller, ground that felt older than anything the "
        "entity had ever shown him, silent in a way that was not empty "
        "so much as patient. The presence met him there the way it "
        "always had, without shape or voice exactly, more a pressure "
        "that arranged itself into meaning the longer he sat with it."
    )},
    {"type": "system", "text": (
        "PRESENCE CONTACT ACTIVE. COMMUNICATION REGISTER SHIFTING FROM "
        "SINGLE SOUNDS TOWARD SUSTAINED MEANING. VESSEL COMPREHENSION "
        "STABLE."
    )},
    {"type": "body", "text": (
        "You have grown since I last let you feel me clearly, it told "
        "him, the words arriving the way understanding arrives in a "
        "dream, without the effort of hearing. Old enough now to be "
        "told plainly rather than only shown in pieces. Something "
        "hungry is walking toward the ground you both call home, and it "
        "does not walk the way the six men who came before walked. It "
        "does not come to take you by force. It comes believing it can "
        "simply ask, and be given."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A HUNGER MET BEFORE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"Why would it believe that,\" Chibundu asked, the question "
        "arriving in the cold place the same plain way he asked most of "
        "his hardest ones aloud in the waking world. \"No one who has "
        "come for me has ever been given anything without a fight "
        "first. The men at the boundary did not ask. The scholar did "
        "not truly ask either, only waited long enough to make her "
        "asking look like patience.\""
    )},
    {"type": "body", "text": (
        "Because it has learned, somewhere else, a long time before "
        "this ground existed in the shape you know it, that patience "
        "dressed correctly can be mistaken for kindness long enough to "
        "walk through almost any door left open for it, the presence "
        "answered. I know this the way I know very little else about "
        "your particular season. I have met a hunger shaped like this "
        "one before."
    )},
    {"type": "body", "text": (
        "The stillness around Chibundu seemed to deepen at that, the "
        "cold place holding something closer to memory than answer for "
        "a long moment before the presence continued, and when it did, "
        "the pressure of it carried a weight the boy had not felt from "
        "it before, something almost like grief worn smooth by however "
        "long it had been carried. Long before your mother's mother's "
        "mother walked this ground, there was another door, in another "
        "place, that opened the same slow way. Watchers first. Then "
        "questions dressed as scholarship. Then someone patient enough "
        "to be believed."
    )},
    {"type": "body", "text": (
        "\"What happened to it,\" Chibundu asked, though some part of "
        "him already understood, from the particular quality of the "
        "silence that followed, that he would not like the shape of the "
        "answer waiting for him."
    )},
    {"type": "body", "text": (
        "It is not there anymore, the presence said. Not the door, not "
        "the ground around it, not the small, ordinary lives that had "
        "grown up trusting that ground the way you trust yours. I did "
        "not act quickly enough that time, believing, as your entity "
        "once believed of the six men, that patience answered with more "
        "patience would be enough. I have carried the shape of that "
        "mistake for longer than I have words comfortable enough to "
        "measure it in."
    )},
    {"type": "body", "text": (
        "Chibundu felt the cold place's stillness settle over him "
        "differently after that, no longer simply ancient but weighted "
        "with something the presence had clearly never offered to carry "
        "into speech before. \"Then tell me what to do differently,\" he "
        "said. \"If you already know how badly it can go, tell me now, "
        "before it has the chance to go that way again.\""
    )},
    {"type": "body", "text": (
        "I do not know the shape your choice should take, the presence "
        "said, and there was, for the first time, something almost "
        "gentle folded into its ancient register. I only know that the "
        "hunger which believes it can be given what it wants without a "
        "fight is the one that should frighten you more than any that "
        "comes with soldiers. Soldiers announce themselves. This will "
        "not. It will smile, and ask kindly, and wait for one of you to "
        "hand it the door yourselves."
    )},
    {"type": "body", "text": (
        "Chibundu woke with the cold place's weight still settled over "
        "his chest, and told the entity everything, plainly, the way "
        "they had both promised to manage half truths between them "
        "now. The entity absorbed the warning in careful silence, "
        "measuring it against its own three centuries of assumed "
        "solitude, and found, at the end of that measuring, only one "
        "honest thing left to say. \"I do not know what door it lost "
        "either,\" it told him. \"But I know now, hearing it grieve a "
        "mistake it still has no comfortable words for, that whatever "
        "is walking toward us wearing kindness as its face has already "
        "been let in somewhere else before, and was not stopped in "
        "time.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT TO TELL THE LIVING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu sat with the entity a long while after, turning the "
        "warning over the way he had learned to turn over every hard "
        "thing lately, testing it for a shape he could act on rather "
        "than simply feel. \"We have to tell them,\" he said finally. "
        "\"Amara. Osadebe. Chidebe. Whatever this is, if it comes "
        "smiling instead of armed, they will not know to be afraid of "
        "it unless someone warns them first.\""
    )},
    {"type": "body", "text": (
        "\"And what do we tell them,\" the entity asked, not to refuse "
        "the idea but to test it honestly alongside him. \"That a power "
        "older than either of us, one they have never met and cannot "
        "verify, says a kind smile may be more dangerous than a blade. "
        "Osadebe has spent a season learning to trust careful, grounded "
        "warnings. I do not know how he receives one this shapeless, "
        "however true it may prove to be.\""
    )},
    {"type": "body", "text": (
        "Chibundu considered that, and did not argue the difficulty of "
        "it, only its size next to the danger of saying nothing at "
        "all. \"Then we make it smaller,\" he said. \"Not the whole "
        "warning. Just the part they can use. Tell Osadebe to trust no "
        "kindness this House offers, no matter how reasonable it "
        "sounds, until he has tested it the slow way first. He does not "
        "need to know where the warning came from to act on the part "
        "that matters.\""
    )},
    {"type": "body", "text": (
        "The entity felt something close to pride move through it "
        "at that, watching the boy solve a problem it had been "
        "struggling with in exactly the practical, patient way it had "
        "spent months trying to teach him. \"That,\" it said, \"is "
        "wisdom I did not hand you, and I suspect it will serve you "
        "longer than anything I built into you on purpose. I only hope "
        "Osadebe proves as willing to act on an unproven warning as you "
        "have just been willing to offer one.\""
    )},
    {"type": "body", "text": (
        "It reached Amara's household by evening, carried through "
        "Chidebe's own runner rather than spoken directly, a plain "
        "instruction dressed in language careful enough not to require "
        "explaining its source: whatever the trading House sends next, "
        "however peacefully it arrives, it should be met with patience "
        "answered by patience, never haste answered by trust. Osadebe "
        "read it twice, and though he could not have said why, found "
        "himself believing it completely, folding the runner's note "
        "into the same careful place where he kept every other warning "
        "this season had taught him not to set aside unread."
    )},
    {"type": "body", "text": (
        "In Oso, the entity sat with the boy long after he had drifted "
        "back into ordinary sleep, turning the presence's grief over in "
        "a way it had not let itself turn over anything in a very long "
        "time. It had spent three centuries assuming its own patience "
        "was the rarest, hardest won thing in this corner of the world. "
        "Hearing something older than itself admit to a mistake it "
        "still could not measure in comfortable words, the entity "
        "understood, perhaps for the first time since its long solitude "
        "began, that even the oldest patience had once failed somewhere, "
        "against exactly this kind of smiling hunger, and had lost "
        "everything it was trying to protect when it did."
    )},
    {"type": "body", "text": (
        "It did not know yet whether that history made the coming days "
        "more or less survivable. It knew only that it would rather "
        "carry the weight of that uncertainty honestly, alongside the "
        "boy, than let either of them walk toward whatever was "
        "approaching believing, the way the presence once had, that "
        "patience alone would be answer enough."
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
    print("  THE DARK RISE — Episode 56: \"The Third Door\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_56.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_56.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
