#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 77: "The Quiet She Mistook for Peace"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-22: Episode 77 pays off the Warden's Episode 74
authorization by showing Mfoniso's second attempt in motion for the
first time: not a strike against Zara's body, but a slow, deliberate
dulling of the borrowed senses that once gave the household its only
warning against her. Zara mistakes the growing silence for rest; the
entity, keeping its post-Episode 55 vow of immediate honesty, notices
the thread has gone muffled before anyone else does and tells Chibundu
at once rather than waiting to be certain. The episode closes on
Mfoniso's own point of view, confirming in the field that her method
has already worked well enough to let her walk closer to Idoro than
she has dared since the night she lost Kene, undetected.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_77.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Seven"},
    {"type": "title_ep_name", "text": "The Quiet She Mistook for Peace"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: AN ORDINARY EVENING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara sat at the edge of Amara's compound in the last thin "
        "light of evening, mending cloth she did not truly need to "
        "mend, glad simply to have something to hold in her hands that "
        "was not another family's fear. Adaugo sat beside her on the "
        "packed earth, her own needle moving in easy, unhurried "
        "stitches, keeping the silence between them the comfortable "
        "kind rather than the watchful kind Zara had grown so tired of "
        "these past weeks."
    )},
    {"type": "body", "text": (
        "\"You are quieter tonight,\" Adaugo said, not looking up from "
        "her work. \"Quieter than usual, I mean. Even for you.\""
    )},
    {"type": "body", "text": (
        "Zara considered the observation honestly before answering, "
        "turning it over the way she had learned to turn over every "
        "strange feeling since the cold touches first began. \"I "
        "think I am,\" she said slowly. \"I have not felt anything in "
        "three days now. No cold reaching for me. No pull toward "
        "danger before anyone else in this compound has noticed it.\" "
        "She said it carefully, testing the shape of the relief before "
        "she allowed herself to trust it fully. \"I had almost "
        "forgotten what an ordinary evening felt like.\""
    )},
    {"type": "body", "text": (
        "Adaugo's needle paused for the length of one stitch. \"Is "
        "that a good thing,\" she asked, \"or does it worry you the "
        "way everything else in this family has learned to worry "
        "you?\""
    )},
    {"type": "body", "text": (
        "Zara laughed, a short, honest sound with real warmth in it, "
        "the first such sound Adaugo had heard from her in longer than "
        "either of them could easily measure. \"I have spent three "
        "seasons being the one who warns everyone else,\" she said. "
        "\"Let me have one week of believing the quiet is simply "
        "quiet, before you make me suspicious of my own rest.\""
    )},
    {"type": "body", "text": (
        "But even as she said it, something in her chest did not "
        "fully agree with her own reassurance, a small unfamiliar "
        "hollowness where the accustomed weight of watching used to "
        "sit, and she pushed the feeling down without naming it, "
        "unwilling to spend one more evening afraid of a thing she "
        "could not even point to."
    )},
    {"type": "body", "text": (
        "Across the compound, Amara watched the two of them from her "
        "own doorway, grateful for the ordinary shape of the evening "
        "even as some old, well earned caution kept her from fully "
        "resting inside it. She had learned across a whole hard season "
        "that peace in this family rarely arrived without a price "
        "attached that only announced itself later."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE ENTITY NOTICED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, Chibundu found the entity turning something over with "
        "unusual stillness when he reached the hollow that evening, "
        "its attention fixed somewhere he could not follow."
    )},
    {"type": "body", "text": (
        "\"What is it,\" he asked, recognizing the particular quality "
        "of its silence as the kind that came before something it did "
        "not yet want to say."
    )},
    {"type": "body", "text": (
        "I have been checking the threads, the entity said. The habit "
        "I built the season I learned that nothing I ever release "
        "actually disappears. And I found something in Zara's thread "
        "tonight that I do not understand."
    )},
    {"type": "body", "text": (
        "\"Found what.\""
    )},
    {"type": "body", "text": (
        "Quiet, the entity said. Not silence exactly. Muffled. The way "
        "a voice sounds through a wall rather than a voice that has "
        "simply stopped speaking. Her thread is still there. It is "
        "only harder to hear than it has ever been, and I do not know "
        "whether that is her own exhaustion finally settling into her, "
        "the way Elder Maka warned it eventually would, or something "
        "else entirely."
    )},
    {"type": "body", "text": (
        "Chibundu felt his stomach tighten around the second "
        "possibility before he had even fully let himself weigh the "
        "first. \"Something else like what.\""
    )},
    {"type": "body", "text": (
        "I do not know, the entity admitted. And I promised you "
        "honesty over comfort, so I will not pretend the not knowing "
        "troubles me less than it actually does. Whatever wears a "
        "thread down slowly enough to look like nothing more than "
        "tiredness is exactly the kind of danger neither I nor the "
        "presence has ever been built to notice quickly. We are both "
        "old enough to recognize a blow. We have far less practice "
        "recognizing a slow, patient erosion, because nothing has ever "
        "dared try one against either of us before."
    )},
    {"type": "body", "text": (
        "\"Tell Amara tonight,\" Chibundu said. \"Not tomorrow. "
        "Tonight.\""
    )},
    {"type": "body", "text": (
        "I intend to, the entity said. I have learned this season "
        "exactly what a delay costs, even a small one, even one meant "
        "kindly."
    )},
    {"type": "body", "text": (
        "It paused, weighing something further before it spoke again. "
        "There is a shape to this I do not like, it added. Mfoniso "
        "failed to take the boy through force and through a charm worn "
        "against his own skin. If this is her hand again, she has "
        "changed her method entirely, from something sudden to "
        "something so slow it asks no one to notice it happening at "
        "all. That is a harder enemy to fight than the one who came "
        "for Kene."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: A HARDER KIND OF UNDERSTANDING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu walked the boundary path to Amara's compound himself "
        "rather than wait for morning, finding Amara still awake, "
        "watching the low fire outside her hut the way she had taken "
        "to doing most evenings since Kene first drew his spiral in "
        "the dirt."
    )},
    {"type": "body", "text": (
        "He told her plainly, the way he had promised himself he "
        "always would from now on: the entity had checked its threads "
        "and found Zara's grown quiet in a way it could not explain, "
        "and did not know whether to call the change rest, or the "
        "first visible sign of something working against her too "
        "slowly to notice by itself."
    )},
    {"type": "body", "text": (
        "Amara's face did not change quickly, the particular stillness "
        "she had learned across a whole hard season of receiving news "
        "exactly this size. \"She told me herself, not an hour ago, "
        "that she has not felt the cold in three days,\" Amara said. "
        "\"She called it peace.\""
    )},
    {"type": "body", "text": (
        "\"It might be peace,\" Chibundu said. \"I do not want to take "
        "that from her over a feeling neither the entity nor I can "
        "prove is anything at all.\""
    )},
    {"type": "body", "text": (
        "\"But you do not believe it is peace,\" Amara said. It was "
        "not truly a question."
    )},
    {"type": "body", "text": (
        "\"No,\" Chibundu admitted. \"I do not.\""
    )},
    {"type": "body", "text": (
        "They found Zara still sitting with Adaugo by the last of the "
        "fire, and Amara told her plainly what the entity had noticed, "
        "watching her friend's face move from confusion, to denial, to "
        "a slower, harder kind of understanding that settled somewhere "
        "worse than fear."
    )},
    {"type": "body", "text": (
        "\"I thought I had finally earned a little quiet,\" Zara said "
        "at last, her voice smaller than either of them had heard it "
        "in a long while. \"I did not think to ask what quiet like "
        "that actually costs, until you asked me to.\""
    )},
    {"type": "body", "text": (
        "\"We do not know that it costs anything yet,\" Amara said, "
        "though the words came out gentler than she fully believed "
        "them. \"We know only that we should not have let ourselves "
        "trust it without asking first.\""
    )},
    {"type": "body", "text": (
        "Adaugo reached for Zara's hand without being asked, the same "
        "steady, unhurried gesture she had been offering through every "
        "hard evening since the council assigned her to it, and this "
        "time Zara let herself hold on rather than simply endure the "
        "comfort being offered. \"If someone has found a way to make "
        "me stop hearing danger coming,\" Zara said quietly, \"then I "
        "am no longer the alarm this family has been leaning on. I "
        "have been telling myself for weeks that resting was allowed. "
        "I did not once ask what this family loses while I do.\""
    )},
    {"type": "body", "text": (
        "Chibundu crouched beside her, meeting her eyes the way he had "
        "learned to meet difficult truths rather than soften them. "
        "\"You are not the only door this family has left,\" he said. "
        "\"You never were, even at your strongest. We watch harder now, "
        "all of us, together, rather than lean the whole weight of it "
        "onto one tired woman's hands. That much I can promise you "
        "honestly.\""
    )},
    {"type": "body", "text": (
        "Amara sent word to Chidebe before the fire burned down, asking "
        "him to double the night watch again exactly as he had after "
        "Kene, and sat with Zara a long while after the others had "
        "gone, neither of them speaking, both of them listening for a "
        "cold that no longer seemed willing to announce itself."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: WHAT MFONISO CONFIRMED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A full day's walk from Idoro's boundary, in the high ground "
        "she had claimed as her own patient vantage, Mfoniso allowed "
        "herself something close to satisfaction for the first time "
        "since the night she had failed to take the boy."
    )},
    {"type": "body", "text": (
        "The working she had begun three nights earlier, small and "
        "slow and deliberately unhurried exactly as the Warden had "
        "authorized, had done precisely what her House's oldest "
        "accounts promised it would. Not silence the woman's borrowed "
        "senses outright, which would have been noticed the instant it "
        "happened. Only dull them, one quiet night at a time, until the "
        "woman herself mistook the dulling for rest and stopped asking "
        "questions of her own comfort."
    )},
    {"type": "body", "text": (
        "Tonight she tested it properly. She walked closer to Idoro's "
        "outer fields than she had dared since the night the guardian "
        "reached across its own borders to save the boy, closer than "
        "any sane accounting of the risk should have allowed her to "
        "go, and she felt nothing answer her from the compound below. "
        "No alarm. No dropped bowl in a startled hand. No household "
        "woken mid stride by a woman who had once sensed her from half "
        "a market away."
    )},
    {"type": "body", "text": (
        "She stood in the dark a long moment, memorizing exactly how "
        "close she had come without cost, filing the distance away the "
        "same careful, unhurried way she filed everything else worth "
        "remembering. The alarm that had cost her the boy once already "
        "would not sound a second time, not soon, and not from the "
        "woman this family had come to trust to sound it."
    )},
    {"type": "body", "text": (
        "She turned back toward her camp unhurried, already composing "
        "the next patient line of her report to the Warden, and "
        "somewhere behind her, in a compound full of people who had "
        "only just begun to suspect what she had already finished "
        "proving, a woman who had spent three seasons being everyone "
        "else's warning sat wondering, for the first time in her life, "
        "whether she could still trust her own hands to tell her the "
        "truth."
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
    print("  THE DARK RISE — Episode 77: \"The Quiet She Mistook for Peace\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_77.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_77.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
