#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 95: "What the Quiet Held"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-10: Episode 95 closes the informant and confrontation
arc that ran from Episode 84 with a quieter episode of recovery and
character throughlines rather than another crisis. Emenike continues
healing, easier now among a household that has fully accepted him;
Elder Maka takes a symbolic step in Adaugo's training toward
succession. Amara and Elder Maka check on Kene's unbidden spiral and
find it has gone still, unresolved rather than healed, precisely
mirroring Zara's own gift, which shows its first faint flicker of
returning after weeks fully muffled. The entity, still resting since
Episode 90, speaks to Chibundu only briefly, still far weaker than
before. The episode closes on the crown's survey party arriving at
Idoro's outskirts for the first time under Episode 94's authorization,
walking measuring lines toward the edge of Oso itself while Chibundu
and the weakened entity watch new outside eyes approach the one
boundary that has always kept their secret — a quiet dread opening the
next arc rather than resolving the last one.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_95.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Five"},
    {"type": "title_ep_name", "text": "What the Quiet Held"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: AN ORDINARY WEEK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The compound settled, over the days that followed, into "
        "something close to an ordinary rhythm for the first time in "
        "longer than anyone could comfortably count, meals cooked "
        "without a soldier posted at every door, children allowed back "
        "into the yard without a parent's hand on their shoulder. "
        "Emenike walked the short distance from his sleeping mat to the "
        "fire unassisted for the first time, and the whole household "
        "found some small reason to be nearby when he managed it."
    )},
    {"type": "body", "text": (
        "\"You are all pretending you were not watching,\" he said, "
        "settling himself by the fire with the careful movements of a "
        "man still mistrustful of his own healing side. Ozoemena, "
        "caught in the act, did not bother denying it. \"We were "
        "watching,\" he said. \"A man does not nearly die in this "
        "compound and then get to walk anywhere unremarked. That is "
        "simply the price of having survived it.\""
    )},
    {"type": "body", "text": (
        "Obi sat with him a while by the fire, saying little, simply "
        "keeping company the way he had learned across many years that "
        "some kinds of healing needed nothing more than a quiet "
        "presence nearby. \"Chidebe tells me your season of watching "
        "ends earlier than promised, if you keep proving yourself the "
        "way you have,\" Obi said eventually. Emenike managed a small, "
        "tired smile. \"I would rather earn it slowly and fully,\" he "
        "said, \"than have it handed to me early out of pity for what "
        "happened to me. I have had enough of things being decided for "
        "me by other people's fear.\""
    )},
    {"type": "body", "text": (
        "Osadebe stopped by briefly with word that the crown's promised "
        "reinforcements were already on the river road, a full season "
        "sooner than such requests usually moved, and allowed himself, "
        "for once, something close to satisfaction at a system that had "
        "finally responded at the speed the danger actually demanded. "
        "\"It should not have taken this much blood to move this "
        "quickly,\" he said to Chidebe. \"But I will not pretend I am "
        "not relieved it finally has.\""
    )},
    {"type": "body", "text": (
        "Elder Maka found Adaugo at the iroko tree's edge that same "
        "afternoon, practicing the small, careful working she had been "
        "taught only the week before, and watched her complete it clean "
        "on the third attempt without needing correction. \"You are "
        "ready for the next rite,\" Elder Maka said simply, and the "
        "words carried a weight Adaugo felt settle into her chest, "
        "another step taken, however quietly, toward becoming the woman "
        "this village would one day need her to be."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: TWO THREADS, STILL UNFINISHED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara found Kene in the yard on a quiet morning, kneeling over "
        "a patch of bare dirt with a stick in hand, and felt her breath "
        "catch the way it always caught now at the sight, before she "
        "saw that his hand had gone still, the stick resting unused "
        "beside an old, half faded spiral rather than tracing a new "
        "one. \"I do not want to draw it today,\" he told her, when she "
        "asked. \"It does not feel like it wants me to, either.\""
    )},
    {"type": "body", "text": (
        "She carried the report to Elder Maka exactly as she had "
        "learned to carry every strange, small thing about her son, and "
        "Elder Maka considered it carefully before answering. \"That is "
        "not the same as gone,\" she said. \"But it is not nothing "
        "either. Whatever thread the presence left in him during the "
        "rescue may simply be resting, the same way greater things than "
        "a boy's hand have needed rest lately.\" Neither of them said "
        "the entity's name aloud, but both understood exactly which "
        "greater thing she meant."
    )},
    {"type": "body", "text": (
        "Amara knelt beside Kene and looked at the half faded spiral "
        "herself, tracing its curve with one careful finger without "
        "quite touching the dirt. \"Does it frighten you,\" she asked "
        "him gently, \"not knowing what it means.\" Kene considered the "
        "question with the grave seriousness he brought to every "
        "question lately. \"A little,\" he admitted. \"But you are "
        "still here when I ask you about it. That helps more than "
        "knowing would, I think.\" Amara held him a long moment at "
        "that, grateful for a son young enough to still say exactly "
        "what he meant."
    )},
    {"type": "body", "text": (
        "Zara felt it first as barely more than a suggestion, standing "
        "at the tree line where she had tested her muffled gift so many "
        "disappointing times before, a faint, uncertain flicker of the "
        "old awareness she had once trusted completely. She did not "
        "call out to anyone right away, unwilling to name it before she "
        "trusted it herself, and stood there a long while simply "
        "feeling for it again, like pressing a bruise to see whether it "
        "had finally begun to heal."
    )},
    {"type": "body", "text": (
        "\"It is not back,\" she told Adaugo carefully, once she "
        "finally allowed herself to speak of it. \"But it is not fully "
        "gone either, and for the first time since it went quiet, that "
        "difference feels like it might mean something.\" Adaugo took "
        "her hand, remembering her own wrist's long silence before it "
        "finally broke for good, and did not promise her anything "
        "beyond simply staying close while she found out."
    )},
    {"type": "body", "text": (
        "Elder Maka examined Zara that evening at Amara's quiet "
        "request, checking the same old signs she had once used to "
        "diagnose the muffling in the first place, and found nothing "
        "conclusive either way. \"Workings this deliberate do not "
        "always fail cleanly,\" she said. \"Whatever Mfoniso built to "
        "blind you may simply be fraying at the edges rather than "
        "breaking all at once. I would not trust it fully yet. I would "
        "not dismiss it either.\" Zara accepted the uncertainty better "
        "than she once might have, having learned, across everything "
        "this season had asked of her, that most true things arrived "
        "slowly rather than all at once."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu checked on the entity as he had every day "
        "since the confrontation, finding it present now, at least, "
        "rather than wholly silent, though its voice still came thin "
        "and slow, like a fire burning low rather than out. \"I am "
        "mending,\" it told him, before he could ask. \"Slowly. Do not "
        "mistake slowly for not at all.\" Chibundu accepted that, "
        "because it was, for now, the only answer either of them had to "
        "give."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE MEASURING LINES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The crown's survey party reached Idoro's outskirts eight days "
        "after Eze Amadi's council rose, exactly as swiftly as Ejikeme "
        "had promised, a dozen quiet men with rope and marked poles "
        "rather than soldiers, though Chidebe posted a discreet guard "
        "around them all the same. They began, as surveys always began, "
        "at the village's known boundaries, walking careful, measured "
        "lines from the river to the market to the compound wall."
    )},
    {"type": "body", "text": (
        "The lead surveyor, a precise, unhurried man named for no one "
        "in the household to particularly remember, presented himself "
        "to Amara on the first morning with a courtesy that felt almost "
        "foreign after so many weeks of danger arriving disguised as "
        "ordinary strangers. \"We are here only to measure and record,\" "
        "he told her. \"Nothing more. The Eze was specific that this "
        "village's cooperation, not its obedience, was what he wanted "
        "from us.\" Amara thanked him for the courtesy and gave it "
        "exactly as much trust as it had earned so far, which was to "
        "say, some, but not yet all of it."
    )},
    {"type": "body", "text": (
        "Amara watched them work from a distance for most of the "
        "morning, grateful, in principle, for a crown finally willing "
        "to see her village clearly, and uneasy in a way she could not "
        "fully name at the sight of strangers walking Idoro's ground "
        "with such careful, official attention. Some fears, she was "
        "learning, did not disappear simply because the danger behind "
        "them had finally been taken seriously."
    )},
    {"type": "body", "text": (
        "Chidebe walked the survey's daily perimeter himself rather "
        "than delegate it, less from distrust of the surveyors "
        "specifically than from a hard learned habit of trusting his "
        "own eyes over anyone else's account of what a stranger's "
        "presence near Idoro actually meant. \"Ejikeme swears they are "
        "exactly what they claim to be,\" he told Amara. \"I believe "
        "him. I am simply no longer capable of believing anything fully "
        "without watching it myself first.\""
    )},
    {"type": "body", "text": (
        "By the third day the measuring lines had crept, slowly and "
        "without any apparent malice, toward the tree line at Oso's "
        "outer edge, the surveyors following the logical shape of the "
        "land rather than any map of secrets they had no way of "
        "knowing existed. In Oso, Chibundu felt the entity's attention "
        "sharpen for the first time in days, weak but unmistakably "
        "alert."
    )},
    {"type": "body", "text": (
        "\"They are close,\" the entity said, its voice thin but "
        "certain. \"Closer than any crown eyes have walked in longer "
        "than you have been alive.\" Chibundu felt the old, familiar "
        "tightness return to his chest, a fear that had nothing to do "
        "with Mfoniso at all. \"Should we be afraid of them,\" he "
        "asked. The entity considered the question with the same "
        "careful weight it gave everything now, its strength too thin "
        "to spend carelessly even on an answer. \"I do not yet know,\" "
        "it said. \"I only know that a secret kept for three centuries "
        "has just had its first honest look from the one power capable "
        "of deciding, someday, that it no longer wishes to keep it.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with that answer long after the entity had gone "
        "quiet again, resting rather than retreating, and watched, from "
        "the boundary he had grown up believing absolute, the small, "
        "distant figures of strangers with rope and measuring poles "
        "walking closer to Oso than anyone outside this family had ever "
        "been permitted to walk before."
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
    print("  THE DARK RISE — Episode 95: \"What the Quiet Held\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_95.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_95.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
