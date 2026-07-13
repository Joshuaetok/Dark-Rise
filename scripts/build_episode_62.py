#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 62: "The Cold Place, Uninvited"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-07: Episode 62 delivers the confrontation Episode 61
set in motion. Chibundu reaches the cold place on his own will for the
first time, furious rather than curious, and demands the presence
answer for taking his voice. The presence does not hide behind its own
age or grief; it admits plainly that it saw the Factor's offer collapse
into the exact shape of the offer that once cost it an entire ground,
and acted from fear rather than calculation. Chibundu refuses to let
fear excuse the violation, and extracts the hardest promise he can
get, though the presence — kept deliberately unresolved per the
project's mandate that both old powers stay ambiguous — will not give
an unconditional vow never to act again, only a narrower one bound to
mortal danger alone. The episode closes on the presence admitting,
unprompted, that its fear was not only about the offer itself: something
else is approaching on a timeline faster than it had hoped, and it did
not want Chibundu's attention divided by a choice that might not matter
by the time it arrives.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_62.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Two"},
    {"type": "title_ep_name", "text": "The Cold Place, Uninvited"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A FEAR, NOT A CALCULATION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The path to the cold place had always felt, in every dream "
        "Chibundu had ever walked it in, like sinking rather than "
        "walking, the warm root laced dark of Oso's hollow giving way "
        "gradually to something colder and stiller the further down he "
        "went. Awake, on his own two feet, with his own fury driving "
        "each step, it felt instead like descending into a held "
        "breath, the ordinary sounds of Oso falling away one at a time "
        "until even his own footsteps stopped answering him back."
    )},
    {"type": "body", "text": (
        "The entity had not tried to stop him leaving, though Chibundu "
        "had felt its worry follow him the first several strides like "
        "a hand not quite touching his shoulder. It had said only one "
        "thing before he crossed out of its easy reach: that it would "
        "be waiting exactly where he left it, for as long as this took, "
        "and would not come looking unless he called for it by name. "
        "Chibundu had not answered, saving what little steadiness he "
        "had left for the ground still ahead of him."
    )},
    {"type": "body", "text": (
        "He reached the cold place and stopped at its very edge, "
        "refusing to let himself sink any further into it than he "
        "needed to be heard. \"Show yourself,\" he said, his voice "
        "carrying strangely in ground that swallowed every ordinary "
        "sound. \"Not a pressure. Not a feeling arranging itself into "
        "meaning. I want an answer, and I want it the way one person "
        "owes another person an answer, not the way something ancient "
        "deigns to explain itself to a child.\""
    )},
    {"type": "body", "text": (
        "You are angry, the presence said, and there was no defensiveness "
        "folded into the observation, only a plain, careful attention "
        "that felt, for the first time since Chibundu had begun visiting "
        "this place, genuinely uncertain of its own footing. You have a "
        "right to be. I did not ask. I have never once asked you for "
        "anything, and the first time I took instead of asked, I took "
        "the one thing you have spent this entire season learning to "
        "hold."
    )},
    {"type": "body", "text": (
        "\"Then tell me why,\" Chibundu said. \"Not what you did. I "
        "already know what you did. I felt it happen inside my own "
        "throat. Tell me why it felt urgent enough to become worth "
        "doing without asking me first.\""
    )},
    {"type": "body", "text": (
        "I heard the shape of the offer before I heard its words, the "
        "presence said. Not through you. Through the pattern of it, the "
        "particular rhythm patient hungers use when they have learned "
        "exactly how to make surrender sound like wisdom. I have heard "
        "that rhythm once before, in the last moments before I lost "
        "everything I failed to protect. I did not calculate what to do "
        "when I heard it again. I simply could not let it finish "
        "landing a second time."
    )},

    {"type": "body", "text": (
        "\"Tell me what it looked like,\" Chibundu said, quieter now, "
        "the fury in him briefly making room for something closer to "
        "need. \"The place you lost. Not to excuse what you did today. "
        "I want to understand what fear this large actually comes "
        "from, rather than simply being told it exists.\""
    )},
    {"type": "body", "text": (
        "It looked like this one, in the ways that mattered, the "
        "presence said, after a silence long enough that Chibundu "
        "wondered if it would answer at all. Ordinary people, living "
        "ordinary lives beside a ground they feared and depended on in "
        "equal measure. A patient hunger that learned their fears "
        "before it ever asked them for anything. I did not lose that "
        "ground to an army. I lost it to a bargain very much like the "
        "one offered you this morning, accepted by people who believed, "
        "reasonably, that safety bought slowly was still safety. I "
        "have not let myself describe it in this much detail to "
        "anyone, ever, until tonight."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE PROMISE IT WOULD NOT GIVE WHOLE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"That is a reason,\" Chibundu said. \"It is not an excuse. "
        "You told me once that patience was the hardest thing you had "
        "learned across three centuries of watching. You have just "
        "shown me that fear can undo all of it in a single instant, and "
        "I do not think you understand yet how much that frightens me "
        "more than the Factor ever did.\""
    )},
    {"type": "body", "text": (
        "The stillness around him shifted, something in it settling "
        "lower, closer to grief than to argument. You are the second "
        "person I have ever done this to, it said. The first time, I "
        "told myself I was only watching, only reaching, never taking. "
        "I have had a very long time to decide that distinction "
        "mattered less than I once believed it did. It did not matter "
        "less to you, watching your own mouth move without you. I "
        "understand that now in a way I did not fully understand it "
        "before this morning."
    )},
    {"type": "body", "text": (
        "\"Then promise me,\" Chibundu said, the words arriving with the "
        "same immovable clarity he had brought to setting his own terms "
        "for the boundary meeting. \"Never again. Not for fear, not for "
        "protection, not because you have decided the reason is good "
        "enough. My voice stays mine, always, or whatever trust we have "
        "built ends here, in this cold place, tonight.\""
    )},
    {"type": "body", "text": (
        "I cannot promise you always, the presence said, and Chibundu "
        "felt something in his chest go tight at the answer's plain, "
        "unflinching honesty, worse somehow than a comforting lie would "
        "have been. I can promise you this. I will not take your voice "
        "for a choice, however large, however dangerous it looks to me. "
        "I will only ever take it again if the alternative is watching "
        "you die in front of me with a breath still left that could "
        "have saved you. That is the only door I am willing to leave "
        "open, and I will not pretend to you that it is fully closed "
        "simply because closing it whole would be easier for you to "
        "hear."
    )},
    {"type": "body", "text": (
        "Chibundu sat with that, turning the narrower promise over the "
        "way he turned over every hard thing now, and found, testing "
        "it from every angle he could manage in his own anger, that it "
        "was not the promise he had asked for, and also, uncomfortably, "
        "the most honest one he was likely to get from something this "
        "old. \"That will have to be enough for tonight,\" he said. \"It "
        "is not enough forever. I want that understood plainly, the "
        "same way you have understood everything else plainly with "
        "me.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "There is one more thing, the presence said, and something in "
        "its register shifted again, reluctant in a way Chibundu had "
        "not felt from it before. My fear this morning was not only "
        "for the shape of the offer. I have felt something else moving "
        "at the edges of my own oldest attention these last several "
        "days, sooner than I had hoped to feel it, and I did not want "
        "your voice spent on a bargain that may not matter at all by "
        "the time it finally arrives."
    )},
    {"type": "body", "text": (
        "\"What is coming,\" Chibundu asked, the anger in him going "
        "suddenly, sharply cold with a new and different fear "
        "altogether."
    )},
    {"type": "body", "text": (
        "I do not know yet, the presence said. I only know it is not "
        "the Factor, and it is not his House, and it is closer than "
        "either of those things ever managed to get before I felt it "
        "coming. I am telling you now rather than waiting, because "
        "after this morning I understand exactly what waiting to tell "
        "you a hard thing actually costs, and I am no longer willing to "
        "pay that cost twice in the same week."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: WHAT HE CARRIED BACK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu climbed back out of the cold place into Oso's "
        "ordinary dark feeling both lighter and heavier than he had "
        "when he went in, the particular exhaustion of an argument won "
        "only partway. The entity was waiting exactly where it had "
        "promised to be, and did not ask what had happened until he was "
        "ready to offer it himself."
    )},
    {"type": "body", "text": (
        "\"It will not promise me everything,\" Chibundu said. \"Only "
        "that it will not take my voice again unless I am dying in "
        "front of it. I do not know yet whether that is enough to "
        "trust or simply the largest promise I could force out of "
        "something that old.\" He told the entity the rest of it "
        "plainly, the lost ground, the warning of something else "
        "approaching sooner than either power had hoped, watching the "
        "entity's stillness sharpen with every new piece of it."
    )},
    {"type": "body", "text": (
        "\"Then we have two dangers now instead of one,\" the entity "
        "said, \"and considerably less patience than either of us had "
        "this time yesterday to meet them with.\" It said nothing more "
        "for a long moment, turning the boy's account over the way it "
        "turned over everything that threatened him now, and found, at "
        "the end of that turning, only one honest thing left to offer "
        "him. \"I am glad you went alone,\" it said. \"And I am sorry it "
        "was necessary that you had to.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with him a while longer in the ordinary dark, "
        "neither of them speaking, both turning over the same "
        "unanswered question from opposite directions: what shape a "
        "danger takes when even the oldest power either of them has "
        "ever met admits it does not yet know what it is facing. \"I "
        "promised Amara I would tell her everything,\" he said finally. "
        "\"I do not know yet how to tell her this part without giving "
        "her one more thing to carry that she cannot do anything about "
        "yet.\""
    )},
    {"type": "body", "text": (
        "\"Tell her the truth in the size she can use tonight,\" the "
        "entity said, \"and the rest of it when there is something more "
        "than a feeling to hand her. That is not the same as hiding it. "
        "It is the same lesson you taught me at the boundary council, "
        "given back to you now that you need it for yourself.\" "
        "Chibundu managed, for the first time since the meeting had "
        "ended, something close to a real smile, and rose to keep the "
        "promise he had made at the furthest line."
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
    print("  THE DARK RISE — Episode 62: \"The Cold Place, Uninvited\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_62.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_62.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
