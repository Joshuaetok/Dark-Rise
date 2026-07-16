#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 44: "What the Crown Decides"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-20: Episode 44 brings Osadebe's Episode 41 report of open
violence at Idoro's boundary to Eze Amadi's council. Ejikeme uses the
proof of the trading House's willingness to use force to argue harder
than ever for a crown ordered survey — better the crown establish
authority now than lose all leverage to a House that has already shown
it will not wait politely. Nkiruka counters with the same old caution,
and Eze Amadi settles on a middle path neither side fully wanted:
stationing a real crown garrison at Idoro, not to move against the
entity, but to hold the ground against foreign encroachment while the
larger question waits. It is the first time the crown's presence in
Idoro has grown from a single watching captain into something with real
weight and numbers. In Oso, the entity, having promised the vessel it
would try to protect Zara and having watched him act with real, untrained
force at the boundary, begins actively teaching him to control what
moved through him rather than simply letting it happen when danger
demands it. The first lesson goes further than either of them expected,
and the episode closes on the entity recalibrating, again, exactly how
much of what grows in the vessel is still something it can shape at all.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_44.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Four"},
    {"type": "title_ep_name", "text": "What the Crown Decides"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: UDO — GROUND HELD RATHER THAN GROUND TAKEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Eze Amadi read Osadebe's report twice before allowing the "
        "council to discuss it, the second reading slower than the "
        "first, as though the words might rearrange themselves into "
        "something less alarming if he simply gave them enough "
        "attention. Six armed men struck down by roots that moved with "
        "targeted, deliberate violence. A foreign agent carried away "
        "wounded, already almost certainly reporting back to superiors "
        "who would not let a beating end their interest so much as "
        "confirm it. He set the letter down at last and looked around "
        "the chamber at faces already arranging themselves into the "
        "familiar shapes of argument."
    )},
    {"type": "body", "text": (
        "\"This is the proof I have been asking this council to "
        "prepare for since the first agent's questions reached us,\" "
        "Ejikeme said, and for once there was no careful political "
        "shading in his voice, only plain urgency. \"That House will "
        "not stop because six of its men were hurt. It will return "
        "with more, better armed, better prepared, and if the crown "
        "has not established some claim on that ground before then, "
        "we will be negotiating from a position with nothing left to "
        "offer but apology.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"You are still describing a survey,\" Eze Amadi said. \"A "
        "survey ordered in response to violence looks, to anyone "
        "watching, exactly like a crown seizing an opportunity rather "
        "than protecting a village. I have not forgotten what you "
        "yourself once called the difference between protection and "
        "taking. I do not think Idoro has forgotten it either.\""
    )},
    {"type": "body", "text": (
        "\"Then let me ask a harder question,\" Ejikeme said, "
        "unwilling to yield the point entirely. \"If we do nothing, "
        "and that House returns in greater force and is met the same "
        "way, what happens to this kingdom's standing with every other "
        "House that trades along our coast. They will not see a "
        "village defended by something ancient and just. They will see "
        "a crown that allowed its own subjects to be struck down on "
        "soil it claimed to protect, and did nothing but write letters "
        "about it afterward. I am not arguing for greed, my lord. I am "
        "arguing that inaction has a cost too, and that cost does not "
        "fall only on Idoro.\""
    )},
    {"type": "body", "text": (
        "Nkiruka spoke before Ejikeme could answer, her voice carrying "
        "the particular weight it had earned since her warnings about "
        "the old records had proven, twice now, worth listening to "
        "closely. \"Every account I read to you named the claimed "
        "children as the true danger, never the presence guarding "
        "them. A survey crew digging into that ground would not be "
        "provoking a landlord protecting its property. It would be "
        "provoking a parent.\" She let the word settle before "
        "continuing. \"I do not know what a parent that old and that "
        "patient does when it decides its child is under threat. I "
        "would rather this kingdom not be the one that finds out.\""
    )},
    {"type": "body", "text": (
        "Ikwuano, silent until this point as was his habit in matters "
        "already well argued by louder voices, offered one further "
        "observation before the council could settle. \"There is a "
        "third audience in this decision neither of you has spoken "
        "for,\" he said. \"Idoro itself. If we send soldiers with "
        "orders to hold ground against foreign Houses, that village "
        "will read our arrival as protection. If those same soldiers "
        "arrive with any hint of Ejikeme's survey folded into their "
        "purpose, they will read it, correctly, as the beginning of "
        "the very seizure Amara's household has spent a year fearing "
        "from every direction at once. The orders we write today will "
        "matter as much as the soldiers themselves.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi sat with both arguments a long while, weighing a "
        "danger he could measure against one he could not, and arrived "
        "finally at a decision that satisfied neither man fully, which "
        "he had learned, across enough years on this throne, was often "
        "the surest sign a decision was actually sound. \"No survey,\" "
        "he said. \"But Idoro will no longer hold that boundary with "
        "one captain and a handful of men. I will send a real "
        "garrison, enough to hold the ground against any House bold "
        "enough to test it again, and enough to remind Idoro's own "
        "council that the crown's protection, however slow it has "
        "been to arrive, has not stopped meaning something.\""
    )},
    {"type": "body", "text": (
        "He turned to Ikwuano before dismissing the chamber. \"Draft "
        "the orders yourself, and have Osadebe read them aloud to "
        "Idoro's council before a single soldier crosses their fields. "
        "I would rather this garrison be understood before it is seen "
        "than seen before it is understood. This kingdom has made that "
        "particular mistake with that village once already, and I do "
        "not intend to make it twice.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — TEACHING A HAND TO CLOSE ON PURPOSE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had decided that a "
        "promise to protect Zara, and every promise like it that would "
        "follow, meant little if the only power backing it remained "
        "something the vessel could summon by accident but not yet "
        "command on purpose. It gathered a handful of loose stones "
        "from the boy's own careful collection and set them in a row "
        "before him, an offering he received with the immediate, "
        "focused interest he gave anything that resembled a game."
    )},
    {"type": "body", "text": (
        "\"The night at the boundary, something moved through you "
        "toward the men who came to hurt your mother's village,\" the "
        "entity told him. \"You did not choose it. It simply happened, "
        "the way a hand pulls back from fire before the mind has "
        "finished deciding to move it. I want to teach you to choose "
        "it instead, carefully, the same way you have learned to "
        "choose your words rather than simply blurt whatever crosses "
        "your mind first. Start small. This stone, nothing more. Move "
        "it without touching it.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The boy stared at the stone with the fierce, uncomplicated "
        "concentration of a child determined not to disappoint, brow "
        "furrowed the way it furrowed over a new word he was not yet "
        "certain he had shaped correctly, and nothing happened for "
        "long enough that the entity began quietly reconsidering "
        "whether the boundary's surge had truly been will at all, "
        "rather than simple, unrepeatable circumstance, fear finding a "
        "door open only once by pure accident of timing."
    )},
    {"type": "body", "text": (
        "Then the stone shifted, a small, ordinary inch, and both of "
        "them went very still, the boy first with delight and then, "
        "watching the entity's face for confirmation, with a "
        "particular pride the entity had never once had to teach him "
        "either. \"I did that,\" he said. \"That was me. Not you "
        "helping. Just me.\""
    )},
    {"type": "body", "text": (
        "\"Just you,\" the entity confirmed, and meant it fully, "
        "aware even as it said the words how much larger a single "
        "ordinary inch of stone had just become than it had any right "
        "to be, measured against everything else this careful season "
        "had already asked the two of them to carry together."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "It set a second stone beside the first, then a third, "
        "watching him work through each one with the same fierce "
        "concentration, the movements growing steadier and faster than "
        "any single evening of practice should have produced. By the "
        "fifth stone he was no longer straining to summon the "
        "sensation at all, simply reaching for it the way he reached "
        "for a familiar word, and the entity, watching the row of "
        "stones rearrange themselves into a shape he had not been "
        "asked to make, understood it was no longer teaching him to "
        "find something buried deep and reluctant inside him."
    )},
    {"type": "body", "text": (
        "\"Why does it matter if I can choose it,\" the boy asked, "
        "pausing between stones, \"if you already promised to protect "
        "Zara yourself.\""
    )},
    {"type": "body", "text": (
        "\"Because I am not always going to be fast enough,\" the "
        "entity told him honestly. \"The night at the boundary, you "
        "moved before I finished deciding how I would respond. If that "
        "happens again, against something I cannot outpace the way I "
        "outpaced six armed men, I would rather you know how to choose "
        "carefully than simply react and hope the reaction lands where "
        "it is needed.\" It did not say the rest of what it was "
        "thinking, that the presence beyond Oso's borders was patient "
        "enough that outpacing it might not always be a choice left "
        "available to either of them."
    )},
    {"type": "body", "text": (
        "The boy absorbed this with the same seriousness he gave "
        "every warning wrapped inside a lesson, and turned back to the "
        "stones with a new deliberateness, less like a child chasing a "
        "delightful trick and more like someone quietly practicing for "
        "a day he already understood was coming whether he felt ready "
        "for it or not."
    )},
    {"type": "body", "text": (
        "VESSEL: RATE OF SKILL ACQUISITION EXCEEDS ALL PRIOR "
        "DEVELOPMENTAL BENCHMARKS BY A WIDE MARGIN. HYPOTHESIS: "
        "CAPABILITY WAS ALREADY PRESENT AND FULLY FORMED PRIOR TO "
        "FIRST DELIBERATE ATTEMPT."
    )},
    {"type": "body", "text": (
        "It was simply teaching him to stop being surprised by "
        "something that had, in some form the entity still could not "
        "fully measure, always already been his."
    )},
    {"type": "body", "text": (
        "They worked until the boy's small shoulders finally sagged "
        "with an honest, ordinary tiredness rather than any strain the "
        "power itself had cost him, and the entity gathered the "
        "scattered stones back into their usual careful order while he "
        "drifted toward sleep, turning over a question it had not yet "
        "found the courage to ask him directly: whether teaching a "
        "child to reach for something this easily was wisdom, or "
        "simply the fastest possible way of making sure he would never "
        "again need the entity standing between him and whatever "
        "eventually came looking for him."
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
    print("  THE DARK RISE — Episode 44: \"What the Crown Decides\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_44.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_44.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
