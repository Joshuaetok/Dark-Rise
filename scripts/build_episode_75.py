#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 75: "What Zara's Gift Costs"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-20: Episode 75 turns to Zara herself, whose exhaustion
since Episode 70 has only deepened rather than eased, three
increasingly costly senses of danger in as many weeks leaving her
thinner and more fragile than the household has let itself fully
acknowledge. Amara and Elder Maka raise, gently, whether she should
step back and rest rather than keep serving as Idoro's earliest
warning against a danger with no fixed shape. Zara herself insists on
staying useful, unwilling to let her own tiredness become one more
thing this family has to carry for her sake. The episode closes on
Mfoniso, already watching from a careful distance exactly as she once
watched the whole village, noting with professional interest that a
tired mind is measurably easier to reach than a rested one.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_75.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Five"},
    {"type": "title_ep_name", "text": "What Zara's Gift Costs"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A WOMAN GROWING THIN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara noticed it first in small things, the way a mother "
        "notices small things in anyone she has learned to watch "
        "closely: Zara eating less at the evening fire, her hands "
        "unsteady over ordinary mending, the particular grey exhaustion "
        "under her eyes that no single night's sleep seemed able to "
        "touch anymore. \"You have not rested properly since the "
        "market,\" Amara said, more observation than question."
    )},
    {"type": "body", "text": (
        "The mending in her lap that evening sat mostly untouched, "
        "her needle idle between two fingers that had once moved "
        "surely enough to catch a newborn slipping too fast into the "
        "world. \"I do not think I know how to rest properly anymore,\" Zara "
        "admitted. \"Every time I close my eyes I am listening for it, "
        "even when I know, plainly, that listening changes nothing "
        "about whether it comes. My body has not yet learned the "
        "difference between watching and worrying. I am not certain "
        "it ever will, now.\""
    )},
    {"type": "body", "text": (
        "Obi, watching from across the fire with Kene asleep against "
        "his shoulder, added the quieter worry he had been carrying "
        "since the market. \"You have delivered half the children in "
        "this village with those same hands,\" he said. \"I do not "
        "like watching them shake now over an ordinary mending needle. "
        "Whatever this family owes you, and it owes you a great deal "
        "already, I do not want to add exhaustion this deep to that "
        "debt without at least trying to lighten it first.\""
    )},
    {"type": "body", "text": (
        "Elder Maka, called over by Amara's quiet concern, studied "
        "her with the same careful attention she now gave most things "
        "touching the old, dangerous edges of this story. \"I carried "
        "a thread once myself, for a season, before it was finally "
        "severed,\" she said. \"I remember exactly this kind of "
        "tiredness. It does not announce itself as danger. It simply "
        "wears a person thinner every day, until the day arrives when "
        "thin enough finally becomes a problem larger than being "
        "tired.\""
    )},
    {"type": "body", "text": (
        "Word reached Chibundu the same evening, carried by Amara "
        "rather than left for Zara to explain herself, and he asked "
        "the entity directly whether either old power could ease what "
        "her own borrowed sense was costing her. \"I do not know how "
        "to lift a weight I did not put there myself,\" the entity "
        "admitted. \"Whatever she carries came from her own hands "
        "touching you both at birth, not from anything I gave her "
        "directly. I am not certain either of us has the right tool "
        "to unmake a cost neither of us caused.\""
    )},
    {"type": "body", "text": (
        "\"Then at least tell me if it is dangerous,\" Chibundu said. "
        "\"Not to us. To her. Whether her own body can keep paying "
        "this price indefinitely, or whether it has a limit neither "
        "of us has thought to ask about yet.\" The entity had no clean "
        "answer to offer him, and admitted as much, the uncertainty "
        "sitting uneasily between them the rest of that evening. "
        "\"I will watch for it more closely than I have,\" it said "
        "finally. \"I owe her that much, and considerably more besides, "
        "for what her own hands have already carried on this family's "
        "behalf without ever once being asked whether she wanted to "
        "carry it.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE OFFER SHE REFUSED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The council raised it gently that evening, Ozoemena speaking "
        "first, unwilling to let the matter wait for someone with less "
        "practice choosing hard words carefully. \"We are asking a "
        "great deal of one woman's tired body,\" he said. \"No one at "
        "this circle would think less of you for asking to rest, even "
        "for a season, and let the rest of us find another way to "
        "watch for what you have been watching for alone.\""
    )},
    {"type": "body", "text": (
        "Chidebe, who had come to value plain military accounting "
        "over comfortable reassurance, laid the practical shape of the "
        "problem out beside Ozoemena's gentler one. \"A tired sentry "
        "is a sentry who eventually misses something,\" he said. \"I "
        "would rather learn that now, sitting in this circle, than "
        "learn it the way I nearly learned it about my own soldier at "
        "the stream. I do not say this to push you out, Zara. I say "
        "it because I have already watched exhaustion cost this "
        "family once, and I would like very much not to watch it "
        "happen twice from two different directions.\""
    )},
    {"type": "body", "text": (
        "\"There is no other way,\" Zara said, before anyone else "
        "could soften the offer further. \"Neither old power caught "
        "what I caught in that market. Whatever I carry, it is doing "
        "something neither of them can do yet, and I do not believe "
        "stepping back keeps this family safer. I believe it only "
        "removes the one warning that has actually worked.\""
    )},
    {"type": "body", "text": (
        "\"It also removes you, slowly, if it continues costing what "
        "it has been costing,\" Amara said, gently but without "
        "backing down from the point. \"I did not fight to keep you "
        "in this family's life only to watch this season spend you "
        "the same way it has spent nearly everything else.\""
    )},
    {"type": "body", "text": (
        "Zara felt the care in that land somewhere she had not let "
        "herself feel fully tended in a long while, and answered it "
        "honestly rather than deflecting it the way exhaustion had "
        "taught her to deflect most things lately. \"Then let me rest "
        "in the ways that do not cost anyone else anything,\" she "
        "said. \"Sleep later in the mornings. Fewer births taken on "
        "for a season. But do not ask me to stop listening entirely. "
        "I do not think I could, even if I wanted to, and I do not "
        "want to, whatever it costs me.\""
    )},
    {"type": "body", "text": (
        "The council did not press further, recognizing in her answer "
        "the same immovable shape Chibundu's own choices had taken on "
        "this season, and settled instead on smaller mercies: fewer "
        "duties, more help around her own hut, Adaugo assigned to sit "
        "with her through the worst of the tired evenings so she was "
        "never quite as alone with it as she had been."
    )},
    {"type": "body", "text": (
        "Adaugo took to the assignment more readily than anyone "
        "expected, arriving at Zara's hut that first evening with "
        "mending of her own rather than empty hands, unwilling to sit "
        "and simply watch a tired woman the way she had once been "
        "watched, uselessly, during her own family's worst season. "
        "\"You do not have to talk to me,\" she said. \"I am only here "
        "so that whatever this costs you, it does not also cost you "
        "being alone with it.\""
    )},
    {"type": "body", "text": (
        "Zara found herself grateful for the company in a way she had "
        "not expected to be, the quiet, undemanding presence of "
        "another young woman mending cloth beside her doing more to "
        "ease the evening's particular dread than any of the "
        "council's careful mercies had managed. \"Your mother taught "
        "you well,\" she said eventually, \"whatever she once withheld "
        "from you in other seasons.\" Adaugo only smiled, and kept "
        "stitching, and neither of them said much more than that "
        "before the evening's tiredness finally pulled Zara under into "
        "something close to real sleep."
    )},
    {"type": "body", "text": (
        "She woke once in the night, briefly, certain for a "
        "disorienting moment that the cold touch had returned, and "
        "found instead only Adaugo still sitting quietly beside her, "
        "mending finished and set aside, keeping a watch of her own "
        "kind over a woman too exhausted to keep it for herself. Zara "
        "let herself drift back under without saying anything, "
        "grateful in a way she did not yet have the words to offer "
        "properly."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A TIRED MIND, NOTED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso watched the compound from a careful distance three "
        "days later, patient in exactly the way her whole life's work "
        "had trained her to be, and noted the woman she had come to "
        "study moving slower now than she had in the market, her "
        "shoulders carrying a visible weight no ordinary chore could "
        "explain."
    )},
    {"type": "body", "text": (
        "She had learned, across thirty years, that a tired mind kept "
        "a weaker hold on whatever borrowed gift it carried, the same "
        "way a tired hand gripped a blade less surely than a rested "
        "one. She did not yet know precisely how Zara's particular "
        "sense worked, only that it worked, and that exhaustion this "
        "visible was rarely without effect on a gift this delicate."
    )},
    {"type": "body", "text": (
        "She made no move yet, content to let the woman's own body do "
        "some of the work patience always eventually did better than "
        "force. Whatever door Zara's tiredness was quietly working "
        "open, Mfoniso intended to be standing exactly there, unhurried "
        "and ready, the day it finally opened wide enough to matter."
    )},
    {"type": "body", "text": (
        "She noted, too, the young woman who had begun sitting with "
        "Zara through the worst of the evenings, mending cloth beside "
        "her with the easy, undemanding company of someone who "
        "understood grief without needing it explained. A companion "
        "was, in Mfoniso's long experience, sometimes an obstacle and "
        "sometimes an opening of its own, depending entirely on how "
        "much that companion was trusted to be told the truth. She "
        "made a note of the daughter's name, unhurried, and added it "
        "to the small, patient accounting she was building of "
        "everyone this household had let close enough to matter."
    )},
    {"type": "body", "text": (
        "She did not yet know how she would use any of it. She had "
        "learned, across thirty years, that the using came later, "
        "shaped by whatever the moment eventually offered, and that "
        "the accounting itself was the only part of this work that "
        "could be done carefully, in advance, while everyone she was "
        "watching still believed themselves simply tired, or simply "
        "kind, rather than already counted, and quietly, patiently, "
        "already spoken for."
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
    print("  THE DARK RISE — Episode 75: \"What Zara's Gift Costs\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_75.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_75.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
