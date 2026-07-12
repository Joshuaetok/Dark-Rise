#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 50: "What the Boundary Gave Back"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-26: Episode 50 closes the block that began with Episode
41 and delivers the reunion this entire stretch has been building toward.
Amara walks to the boundary at the arranged hour and meets Chibundu
properly for the first time since his birth — not glimpsed, not a
rumor, not a name spoken through someone else's mouth, but her own son,
standing in front of her, old enough in every way that matters to know
exactly what this moment costs and means. The scene is given real
weight: grief, tenderness, the specific ache of a year's absence finally
closing. But the trading House's scholar has not been watching idly.
With Chidebe's patrol pulled back exactly as arranged, her House's men
use the one undefended window they have been waiting weeks for, moving
on the boundary in the reunion's final minutes with intent to seize
rather than merely observe. The episode, and this ten episode block,
ends at the exact moment the entity registers the ambush and has to
choose, in a single instant, between protecting the boy it raised and
the mother he has only just been given back.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_50.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty"},
    {"type": "title_ep_name", "text": "What the Boundary Gave Back"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE BOUNDARY — A YEAR CLOSING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara reached the last stone at the appointed hour with her "
        "heart beating hard enough that she could feel it in her own "
        "throat, and found the tree line already different than she "
        "remembered it, the dark beyond it not empty the way it had "
        "always been but waiting, the particular waiting of a room "
        "that already knows someone is about to walk into it."
    )},
    {"type": "body", "text": (
        "He came forward slowly, the roots parting ahead of him "
        "without needing to be asked, and Amara felt every careful "
        "thing she had rehearsed saying leave her at once, replaced by "
        "the simple, overwhelming fact of him standing there in full "
        "view for the first time in her life. Taller than she had "
        "pictured, though she knew, distantly, that this should not "
        "have surprised her. Her own eyes, unmistakably, set into a "
        "face that was otherwise entirely his own."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"Chibundu,\" she said, his name the only word she trusted "
        "herself to manage first, and watched something in his careful "
        "stillness break gently open at hearing her say it, as though "
        "the name had been waiting its whole short life to be spoken "
        "by exactly this voice."
    )},
    {"type": "body", "text": (
        "\"You came,\" he said, and there was no accusation in it, "
        "only the plain, disbelieving wonder of a child confirming a "
        "promise he had not quite let himself trust until the promise "
        "was standing in front of him."
    )},
    {"type": "body", "text": (
        "\"I never stopped coming,\" Amara told him, closing the last "
        "distance between them before either of them could think "
        "better of it, and pulled him into an embrace that answered "
        "every question a year of grief had left unresolved between "
        "them, feeling him go rigid with surprise and then, slowly, "
        "fold into it the way a much smaller child might, all the "
        "careful control he had spent weeks learning momentarily "
        "forgotten in favor of simply being held."
    )},
    {"type": "body", "text": (
        "She held him longer than either of them had planned for, "
        "counting silently the way a mother counts a newborn's "
        "breaths, memorizing the exact weight and warmth of him "
        "against a year spent with nothing but memory and dread to "
        "hold instead. When she finally stepped back to look at him "
        "properly, she found herself laughing and crying in the same "
        "breath, an undignified, helpless sound she made no attempt to "
        "smooth into something calmer."
    )},
    {"type": "body", "text": (
        "\"I have imagined this so many ways,\" she admitted. \"None "
        "of them included laughing. I do not know why that surprises "
        "me. I suppose I never let myself imagine this moment being "
        "allowed to feel good at all.\""
    )},
    {"type": "body", "text": (
        "\"Is it,\" Chibundu asked, watching her face with the same "
        "careful attention he gave every new thing he was still "
        "learning to read. \"Allowed to feel good.\""
    )},
    {"type": "body", "text": (
        "\"Yes,\" Amara said, fierce and certain in a way that "
        "surprised even her. \"Whatever else is true about tonight, "
        "about you, about everything that had to happen to bring us "
        "both here. This part is allowed to simply be good. I will "
        "not let anyone, including myself, take that much away from "
        "us.\""
    )},
    {"type": "body", "text": (
        "They talked in fragments after that, neither of them managing "
        "the large speeches either had privately prepared, trading "
        "instead the small, ordinary details that somehow mattered "
        "more than anything grander could have. Kene's laugh. The "
        "shape of the compound. The particular way Chibundu arranged "
        "his stones, which Amara studied with a fierce, hungry "
        "attention, memorizing a habit she had never once been allowed "
        "to witness before. \"You have his eyes,\" she told him at one "
        "point, unable to stop herself. \"Your brother's. I did not "
        "expect that. I do not know why it undoes me the way it "
        "does.\""
    )},
    {"type": "body", "text": (
        "\"Tell me about the day we were born,\" he asked her, "
        "quietly, the one question he had apparently saved above "
        "every other. \"I have only ever heard it from the one who "
        "raised me. I want to hear it from you.\""
    )},
    {"type": "body", "text": (
        "Amara told him plainly, the way she had promised herself, "
        "walking here, that she would tell him everything he asked "
        "without softening it for either of their sakes. The dibia's "
        "hands. The cold walk to the tree line. The particular silence "
        "of a village that had already decided, before either twin "
        "took a single breath, which one it would let her keep. "
        "Chibundu listened without flinching, the same careful, "
        "practiced stillness he brought to every hard truth, and when "
        "she finished he was quiet a long moment before answering."
    )},
    {"type": "body", "text": (
        "\"I am not angry at you,\" he said. \"I want you to know "
        "that plainly, since I do not know how many more chances we "
        "will have to say true things to each other. You did not "
        "choose the law. You have spent every day since trying to "
        "undo what it cost.\""
    )},
    {"type": "body", "text": (
        "Amara felt something in her chest that had been clenched "
        "tight for over a year finally, carefully, begin to loosen, "
        "grief and relief arriving together in a single unsteady "
        "breath, the way the entity had once quietly warned him they "
        "might. She had braced herself, walking here, for accusation. "
        "She had not let herself hope for absolution, and found, "
        "receiving it anyway, that she did not fully know what to do "
        "with a gift this large and this unearned."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE UNDEFENDED WINDOW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The entity watched from a careful distance exactly as "
        "promised, close enough to feel every shift in the two of "
        "them and far enough to let the moment belong entirely to "
        "mother and son, and found itself, watching, holding something "
        "unfamiliar and unguarded of its own, a feeling with no clean "
        "name it had ever needed before tonight."
    )},
    {"type": "body", "text": (
        "It had spent three centuries certain that patience was its "
        "single greatest strength. Watching Chibundu laugh, actually "
        "laugh, at something small his mother said, the entity "
        "understood for the first time that patience had only ever "
        "been the means. This, whatever this feeling was, had always "
        "been the actual end it was working toward, whether it had "
        "known to name it that way or not."
    )},
    {"type": "body", "text": (
        "It thought, unwillingly, of every choice it had made across "
        "this long, careful season that had cost someone something to "
        "arrive at exactly this ordinary, unremarkable moment: a "
        "midwife's isolation, a healer's silenced voice, a woman's "
        "authority stripped down to nothing in front of the whole "
        "gathered village. It did not know, watching the two of them "
        "trade small stories neither had ever been allowed to tell the "
        "other before, whether the accounting balanced. It knew only "
        "that for the length of this one borrowed hour, it had stopped "
        "needing the accounting to balance at all."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The fixed span of time was nearly spent when the entity felt "
        "the first wrong shift in the ambient stillness of the "
        "surrounding dark, subtle enough that a lesser attention might "
        "have missed it entirely, unmistakable to something that had "
        "spent months learning to read exactly this kind of danger "
        "approaching. Not the scholar's familiar, patient watching. "
        "Movement. Several bodies, disciplined and quiet, closing on "
        "the boundary from the unguarded stretch of field Chidebe's "
        "patrol had left open exactly as arranged."
    )},
    {"type": "body", "text": (
        "VESSEL: HOSTILE PARTY APPROACHING THROUGH THE DELIBERATELY "
        "UNGUARDED BOUNDARY SECTION. TIMING CONSISTENT WITH DELIBERATE "
        "EXPLOITATION OF REUNION ARRANGEMENTS. BOTH MATERNAL FIGURE AND "
        "VESSEL PRESENT AND EXPOSED. RESPONSE WINDOW: SECONDS."
    )},
    {"type": "body", "text": (
        "The entity understood, in the same instant the realization "
        "landed, exactly what had happened, and exactly how thoroughly "
        "it had been outmaneuvered by a patience it had mistaken for "
        "simple retreat. The scholar had never needed to force her own "
        "way past the boundary. She had only needed to watch long "
        "enough to learn when Idoro would willingly open the door "
        "itself, and two hours of mercy, arranged in good faith by a "
        "soldier who had chosen kindness over strict duty, had handed "
        "her House the one undefended window it had been patiently "
        "waiting weeks to find."
    )},
    {"type": "body", "text": (
        "Amara felt the entity's attention snap taut beside them "
        "before she heard anything herself, and saw Chibundu's whole "
        "small frame go still in the particular way she now recognized "
        "as him reaching for the control he had spent weeks learning "
        "to hold rather than simply react without thinking. \"Someone "
        "is coming,\" he said, quiet and certain, already moving "
        "instinctively to place himself between his mother and the "
        "sound neither of them could yet see."
    )},
    {"type": "body", "text": (
        "The entity felt the choice arrive all at once, with no time "
        "left to weigh it the careful, patient way it had weighed "
        "every other decision this long, difficult season: strike now, "
        "before the approaching party closed the distance, and risk "
        "everything Idoro had only just begun to believe about "
        "restraint and mercy, or wait one breath longer to be certain, "
        "and risk losing, in a single unguarded window bought by "
        "someone else's kindness, the only two people it had ever "
        "learned to want to protect at exactly the same moment."
    )},
    {"type": "body", "text": (
        "Chibundu felt the same choice arrive inside himself a half "
        "breath later, the training of these last weeks rising to "
        "meet it without needing to be summoned, his small hands "
        "already curling at his sides the way they had curled once "
        "before, at a boundary very much like this one, when the only "
        "thing that had ever mattered was keeping harm away from "
        "someone he loved."
    )},
    {"type": "body", "text": (
        "Amara, feeling both of them go taut beside her, understood "
        "before either one spoke a single word that whatever this "
        "night had given her, it was not yet finished asking something "
        "back."
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
    print("  THE DARK RISE — Episode 50: \"What the Boundary Gave Back\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_50.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_50.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
