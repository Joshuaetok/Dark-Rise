#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 48: "A Name Changes the Report"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-24: Episode 48 handles the fallout of Episode 47's
naming. Osadebe must decide how to report what happened to Udo, and
recognizes that a named child reads entirely differently in a formal
report than an unnamed presence's vessel — a name implies a person, and
a person implies rights, grief, and political complications a report
about "a dangerous entity" never had to account for. Idoro itself absorbs
the news in fragments, uncertain what to make of a boundary that gave
something a name rather than simply taking something away. In Oso, the
entity begins using the name for the first time, and Chibundu, testing
the shape of his own new identity, asks for something he has never
directly asked for before: to see his mother's face again, awake and
close, rather than glimpsed once from a boundary he was pulled back from
crying. The episode closes on the entity, unable to refuse him outright
after everything that has already been taken out of its hands this
season, agreeing to consider it — the first time it has treated the
question of Chibundu actually reaching Idoro as a matter of when rather
than never.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_48.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Eight"},
    {"type": "title_ep_name", "text": "A Name Changes the Report"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT A NAME COSTS A REPORT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe sat with a blank sheet longer than he had sat with "
        "any report since arriving in Idoro, aware that every version "
        "he drafted kept snagging on the same single word. He had "
        "written, months ago, about an entity, a presence, a danger "
        "sustained on dread. He had written since then about roots "
        "moving with targeted violence, about wounded strangers "
        "carried home. Writing that the same presence had just spoken "
        "a name into the world, unprompted and unasked, felt like "
        "describing an entirely different kind of thing altogether, "
        "and he was no longer certain the crown's careful policies "
        "built around danger would translate cleanly onto whatever "
        "this had just become."
    )},
    {"type": "body", "text": (
        "\"A name changes how this reads in Udo,\" he told Amara, "
        "turning the problem over aloud the way he had learned to do "
        "with her more than with anyone else in this village. \"A "
        "dangerous presence, the council can debate freely, survey or "
        "starve out or simply avoid. A named child with a mother "
        "living a mile from where he sleeps is a different question "
        "entirely, one this kingdom has laws and customs for that were "
        "never written with Oso in mind.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Amara felt something complicated move through her hearing "
        "it framed that plainly, a grief she had carried privately for "
        "over a year suddenly handed a shape other people might "
        "finally be forced to reckon with. \"He has always been a "
        "child with a mother,\" she said. \"The rest of you are only "
        "now catching up to a fact I have never once stopped living "
        "inside.\""
    )},
    {"type": "body", "text": (
        "Word of what had happened at the boundary moved through "
        "Idoro in careful, incomplete fragments over the following "
        "days, shaped less by what Amara and Zara actually said than "
        "by what the rest of the village imagined must have happened "
        "to leave both women so visibly, unmistakably shaken. Ozoemena, hauling "
        "water past the mango tree, stopped Amara long enough to ask "
        "the one question everyone else seemed too uncertain to voice "
        "aloud. \"Does he have a mother's love for you the way Kene "
        "does,\" he asked her plainly, \"or only a mother's blood.\" "
        "Amara found she did not yet have an honest answer ready, only "
        "the certainty that the question itself no longer felt like "
        "the wrong one to ask."
    )},
    {"type": "body", "text": (
        "Chidebe took the news with the same flat, practical stillness "
        "he brought to everything else, turning it over less as a "
        "grief and more as a new variable his orders had never "
        "accounted for. \"A named child with living family is not the "
        "same threat a nameless presence was,\" he told Osadebe "
        "plainly, setting down the report before he had finished "
        "reading every line of it twice. \"I do not know yet whether "
        "that makes my duty easier or considerably harder. I suspect I "
        "will not know until the day I am actually asked to choose "
        "between the two.\""
    )},
    {"type": "body", "text": (
        "Osadebe wrote the report honestly in the end, naming "
        "Chibundu the way the presence itself had named him, and "
        "found, sealing the letter, that he had no real guess left for "
        "how Eze Amadi's council would receive a report that no longer "
        "described a monster but a boy old enough, in some form beyond "
        "his actual months of life, to have been given a name by "
        "something that had watched him longer than either the entity "
        "or his own mother had."
    )},
    {"type": "body", "text": (
        "Obi read the news in Amara's face before she managed to "
        "shape it into words, and sat with her a long while once she "
        "finally did, Kene asleep between them the way he so often was "
        "now, a small warm anchor holding both of them to the "
        "ordinary world even as they discussed something that felt "
        "anything but. \"A name,\" Obi said finally, turning the word "
        "over like a stone he was not yet sure he trusted the weight "
        "of. \"After everything he has been called instead. Abiku. "
        "Curse. Threat. A name is the first word anyone has ever given "
        "him that was not also an accusation.\""
    )},
    {"type": "body", "text": (
        "\"It was not given by anyone who loves him,\" Amara said "
        "quietly. \"Not yet. It was given by something that has "
        "watched him the way a trader watches a promising field, "
        "waiting for the harvest to be worth claiming.\" She paused, "
        "surprised by her own bitterness, and let the silence sit "
        "between them a moment before finishing. \"I do not know why "
        "that should matter more than the name itself. But it does. I "
        "wanted to be the one who gave him something that was only "
        "love and nothing else. I do not think I will ever get that "
        "chance now.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — LEARNING TO SAY IT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity found itself stumbling "
        "over the name in a way it had not expected, three centuries "
        "of careful, deliberate speech suddenly catching on four "
        "simple syllables that belonged to someone else's choosing "
        "rather than its own. It said it anyway, quietly, again and "
        "again, until the stumbling smoothed into something closer to "
        "habit, because refusing to use it, however uncomfortable the "
        "discomfort, would have cost the boy something the entity was "
        "no longer willing to spend."
    )},
    {"type": "body", "text": (
        "\"Chibundu,\" it said, quietly, testing the shape of it once "
        "more before letting it settle, and watched him look up from "
        "his stones the way he had never quite looked up from "
        "anything before, a small, unguarded brightness crossing his "
        "face at hearing the entity use it plainly, without "
        "hesitation, as though it had always belonged to him rather "
        "than only just arrived."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"I want to see her,\" he said, once the brightness settled "
        "into something steadier. \"Not from the wall, the way I saw "
        "the trees that one time before you carried me back. I want "
        "to actually see her face. Close. Awake. I have a name now. I "
        "do not think I am the same small thing you were protecting by "
        "keeping me here before.\""
    )},
    {"type": "body", "text": (
        "He said it without demand, the same plain, patient certainty "
        "he had carried into every hard question since the first time "
        "he asked what Mama meant, and the entity found itself, not "
        "for the first time, measuring the distance between the "
        "infant it had once sheltered out of pure necessity and the "
        "boy sitting before it now, old enough in every way that "
        "actually mattered to ask for something plainly and expect to "
        "be answered honestly rather than gently managed."
    )},
    {"type": "body", "text": (
        "The entity considered every careful reason it had spent "
        "months building for why that meeting could not yet happen "
        "safely, and found, turning each one over honestly in the "
        "light of everything that had already been taken out of its "
        "own hands this season, that most of those reasons had quietly "
        "stopped being entirely true. Idoro no longer simply feared "
        "him in the old, uncomplicated way, not since the boundary had "
        "shown it exactly what protecting them could look like. A "
        "crown garrison held the boundary now, not to attack but to "
        "hold ground. A trading House already knew a named being lived "
        "past that tree line. Concealment had been spent, piece by "
        "piece, until almost nothing of the old caution remained worth "
        "protecting."
    )},
    {"type": "body", "text": (
        "VESSEL: DIRECT, UNPROMPTED REQUEST FOR PHYSICAL REUNION WITH "
        "MATERNAL FIGURE. PRIOR REFUSALS BASED ON RISK ASSESSMENT NOW "
        "PARTIALLY OBSOLETE. FULL REFUSAL NO LONGER DEFENSIBLE ON "
        "GROUNDS PREVIOUSLY USED."
    )},
    {"type": "body", "text": (
        "\"I will not promise you tomorrow,\" the entity told him, "
        "carefully, aware that a promise made too quickly now would "
        "cost more than any promise it had ever broken slowly before. "
        "\"I will not promise you next week. But I will stop telling "
        "you it cannot happen at all. I will start deciding, honestly, "
        "what it would take for it to happen safely, for both of you, "
        "rather than deciding it should simply never be tried.\""
    )},
    {"type": "body", "text": (
        "Chibundu accepted this the way he had learned to accept "
        "every answer that cost the entity something real to give, "
        "and went back to his stones with a new, quiet purposefulness "
        "that the entity recognized, with a mixture of pride and dread "
        "it did not fully know how to separate, as the exact shape of "
        "a boy who had just heard the word not yet turn, for the very "
        "first time in his short and difficult life, into something "
        "that finally sounded like soon."
    )},
    {"type": "body", "text": (
        "He paused once more before sleep found him, stones half "
        "arranged around their new center. \"What will she call me,\" "
        "he asked, \"when she finally sees me. I do not know if she "
        "already knows the name the presence gave me, or if I will "
        "need to be the one who tells her.\""
    )},
    {"type": "body", "text": (
        "The entity had no honest answer ready for that either, and "
        "said so, choosing, as it had chosen so often these last "
        "difficult weeks, to sit inside the not knowing with him "
        "rather than paper over it with a comfort it could not "
        "actually promise. It understood, watching him finally drift "
        "toward sleep beside his half finished pattern of stones, that "
        "whatever answer eventually came would not belong to the "
        "entity to give either. That answer, like the name itself, "
        "would have to be earned in a room the entity could not fully "
        "control, by two people who had never yet been allowed to "
        "simply sit together in daylight and decide, on their own "
        "terms, what came next."
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
    print("  THE DARK RISE — Episode 48: \"A Name Changes the Report\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_48.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_48.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
