#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 59: "The Eve of Asking"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-04: Episode 59 covers the last hours before the
meeting Episode 58 set in motion. Chidebe positions his men at a
distance meant to matter only after the fact. The entity, tested by
its own promise to stand back, asks Chibundu directly whether it
should intervene if the conversation turns against him, and is told
plainly not to, no matter how it looks in the moment. Amara, still
carrying the fear of the last ambush in her body, is asked gently by
her own son to stay back this time rather than stand beside him, a
quiet reversal of every instinct that has driven her since Episode 1.
The episode closes at the boundary itself, the Factor's approach
already visible, and the entity feeling, for the first time since its
single deliberate parlay in Episode 39, the presence stirring at the
very edge of its awareness, uninvited and unexplained.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_59.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Nine"},
    {"type": "title_ep_name", "text": "The Eve of Asking"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A PROMISE TESTED IN ADVANCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe walked the ground himself the evening before, placing "
        "each of his men by hand rather than trust the positions to a "
        "shouted order, close enough to see everything and far enough "
        "to change nothing quickly. \"If this goes wrong,\" he told "
        "Osadebe quietly, \"my men will not be the reason it goes wrong "
        "faster. That is the only promise I can honestly make about "
        "tomorrow.\""
    )},
    {"type": "body", "text": (
        "Osadebe spent the same evening rereading his own last report "
        "to Udo, searching it for anything he might have gotten wrong "
        "badly enough to matter now. \"I have advised this king on "
        "three separate crises this season,\" he told Chidebe, \"and I "
        "find myself, on the eve of the fourth, no more confident than "
        "I was standing at this same boundary the very first time. I "
        "am beginning to wonder if confidence was ever the right thing "
        "to hope for out of any of this.\" Chidebe had no comfort to "
        "offer him beyond his own steady presence, which he gave "
        "freely, saying nothing further."
    )},
    {"type": "body", "text": (
        "Elsewhere in Idoro, Elder Maka sat with Adaugo long past the "
        "hour either of them usually kept, turning over the morning "
        "still to come. \"I voted to let a boy decide his own danger,\" "
        "she said, \"and I do not regret the vote. I only find I have "
        "not slept easily since casting it, wondering whether wisdom "
        "and hope look similar enough from the outside that I mistook "
        "one for the other without meaning to.\" Adaugo took her "
        "mother's hand, an ordinary gesture that would have been "
        "unthinkable between them only a season before, and said "
        "nothing, which seemed to be answer enough for both of them."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu asked the entity the question he had been "
        "circling all evening without quite reaching it directly. \"If "
        "it looks like I am losing,\" he said. \"If he says something "
        "that frightens me, or corners me, or makes me look small in "
        "front of everyone watching. Do you promise not to step in "
        "unless he actually moves to hurt me.\""
    )},
    {"type": "body", "text": (
        "The entity felt the old instinct rise in it exactly as it "
        "always did now, and set it aside exactly as it had promised "
        "the council it would. \"I promise,\" it said, and meant it more "
        "fully than it had meant almost anything else this season. \"You "
        "asked for this meeting to be yours, not mine wearing your "
        "face. I will not undo that the first time it becomes "
        "uncomfortable to watch. Losing an argument is not the same as "
        "losing you, and I have to trust you can tell the difference "
        "even if I am frightened watching you find out.\""
    )},
    {"type": "body", "text": (
        "\"And if I decide, in the middle of it, that I want you to "
        "step in after all,\" Chibundu asked. \"How would you even know, "
        "if I have already told you not to.\""
    )},
    {"type": "body", "text": (
        "\"You would say my name,\" the entity told him. \"Not as part "
        "of an argument. Plainly, the way you said it the first night "
        "you asked me anything at all. I will listen for that, and "
        "nothing less, the whole time you are standing there.\" "
        "Chibundu turned that over and, seeming satisfied, sat with the "
        "answer in a silence that felt, for once, more like readiness "
        "than fear, the particular quiet of a boy rehearsing not what "
        "he would say tomorrow, but what he would refuse to feel "
        "regardless of what was said to him."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT AMARA WAS ASKED TO GIVE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Before she left for the boundary, Obi caught Amara's hand at "
        "their own doorway, Kene asleep behind them, and said the "
        "thing he had clearly been holding back all evening. \"I have "
        "spent this whole season watching you walk toward every danger "
        "this family has faced,\" he said, \"and I have made my peace "
        "with not being the one who can follow you into most of it. I "
        "am only asking that whatever he decides tomorrow, you let me "
        "be the one waiting at the door when you both come home.\" "
        "Amara kissed him once, fiercely, and did not trust herself to "
        "answer in words."
    )},
    {"type": "body", "text": (
        "Amara came to the boundary that same evening, unable to stay "
        "away entirely even knowing the meeting itself was still a day "
        "off, and found Chibundu waiting for her the way he always "
        "seemed to be lately, as though he had learned to feel her "
        "coming before she arrived. \"I want to be there tomorrow,\" she "
        "said, before he could speak first. \"Not close. Just close "
        "enough to see you.\""
    )},
    {"type": "body", "text": (
        "\"I would rather you were not,\" Chibundu said, gently but "
        "without hesitation, and watched something in her face flinch "
        "at hearing it. \"Not because I do not want you near me. "
        "Because the last time I stood at this boundary with you beside "
        "me, someone used that closeness to try to reach us both "
        "through you. I do not know yet what this man wants. Until I "
        "do, I would rather be the only one standing where he can see "
        "me.\""
    )},
    {"type": "body", "text": (
        "Amara felt the whole shape of her own instinct war with the "
        "plain sense of what he was asking, a mother's body arguing "
        "with a mother's understanding. \"I have spent your whole life "
        "wanting to stand between you and every danger I could see "
        "coming,\" she said. \"You are asking me to let you be the one "
        "standing between me and this one instead.\""
    )},
    {"type": "body", "text": (
        "\"Yes,\" Chibundu said simply. \"I am asking you to let me. Not "
        "because I think I am stronger than you. Because I think, for "
        "the first time since I was born, I might actually be able to "
        "protect someone rather than only be protected, and I would "
        "like the chance to find out whether that is true before "
        "either of us decides it is not.\""
    )},
    {"type": "body", "text": (
        "Amara held him a long moment, the same fierce hold she had "
        "held him with at their very first reunion, and when she "
        "finally stepped back her eyes were wet but her voice was "
        "steady. \"Then I will wait at Chidebe's furthest line,\" she "
        "said, \"close enough that if you say my name the way you say "
        "the entity's, I will hear it and come running regardless of "
        "any promise anyone else has made. That much I will not give "
        "up, not for you, not for this man, not for anyone.\" Chibundu "
        "did not argue the term, and something in his face suggested he "
        "had not truly expected her to give up that much."
    )},
    {"type": "body", "text": (
        "Chidebe walked Amara to that furthest line himself the next "
        "morning, choosing the spot with the same careful attention he "
        "had given every other position on the field. \"From here you "
        "can see him clearly and reach him quickly,\" he told her, \"and "
        "from there, he can see you are close without needing to look "
        "for you.\" Amara thanked him plainly, and understood, standing "
        "where he had placed her, that this quiet, exacting man had "
        "spent as much care on protecting a mother's need to watch as "
        "he had on protecting the boy she was watching."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: SOMETHING ELSE WAS ALREADY LISTENING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Morning came grey and still, the kind of quiet that felt "
        "arranged rather than accidental, and Chibundu walked to the "
        "last boundary stone alone, the entity a careful distance "
        "behind him, Chidebe's men further back still, Amara at the "
        "furthest line exactly as promised. The Factor's shape resolved "
        "out of the mist well before he reached speaking distance, "
        "unhurried, unarmed, alone, exactly as he had come the first "
        "time."
    )},
    {"type": "body", "text": (
        "The entity felt every promise it had made settle into place "
        "around it like a held breath, ready to keep every one of "
        "them. And then, at the very edge of its awareness, in the "
        "same register it had felt only once before, standing at this "
        "same boundary during a parlay it had initiated and controlled "
        "entirely on its own terms, it felt the presence stir."
    )},
    {"type": "body", "text": (
        "It had not been summoned. It had not been asked. It arrived "
        "the way weather arrives, without permission and without any "
        "promise attached to it at all, and the entity understood, "
        "watching Chibundu take his first step forward alone to meet a "
        "man who wanted something from him that no one yet fully "
        "understood, that for the first time since it had agreed to "
        "stand back and let the boy have this meeting entirely on his "
        "own terms, it was no longer the only old power watching how it "
        "went."
    )},
    {"type": "body", "text": (
        "It said nothing of it to Chibundu, not out of the old habit "
        "of convenient silence it had promised to abandon, but because "
        "there was, in the space of these last few strides before the "
        "Factor came within speaking distance, no honest way left to "
        "say it that would not also break the very promise the boy had "
        "asked of it. So the entity held the knowledge alone, turning "
        "over the presence's own grief from two nights before, a "
        "hunger it had once let through a door by trusting patience "
        "too long, and hoped, with an intensity it had not let itself "
        "feel in three centuries, that whatever had drawn the presence "
        "here now was watching to protect rather than watching to "
        "decide, and that the promise it had just made a boy about "
        "trusting his own voice would still hold if a second power, "
        "older and less patient than either of them had fully "
        "reckoned with, decided that voice was not the only one that "
        "mattered here today."
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
    print("  THE DARK RISE — Episode 59: \"The Eve of Asking\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_59.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_59.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
