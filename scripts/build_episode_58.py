#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 58: "A Seat at the Boundary"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-03: Episode 58 delivers the milestone the last several
episodes have been building toward: rather than decide the Factor's
request without him, Idoro's council walks to the boundary itself so
Chibundu can speak for his own fate directly. For Elder Maka, it is
the first time she has seen him in person, and the encounter unsettles
her in a way she does not expect, a calm, careful, entirely unlike
her own returned son standing in front of her. The council agrees,
under tight conditions, to allow a single controlled meeting with the
Factor. The episode closes on the news that undercuts everything his
patience seemed to promise: Chidebe's watch reports the Factor has
already moved his camp measurably closer to the boundary overnight,
before any answer was ever given him.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_58.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Eight"},
    {"type": "title_ep_name", "text": "A Seat at the Boundary"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE COUNCIL WALKS TO HIM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "No council in Idoro's memory had ever walked its full circle "
        "out to the boundary rather than summon whoever it needed to "
        "speak before it, and the procession that formed the next "
        "morning felt, to nearly everyone in it, like the crossing of a "
        "line as significant as any the old law had ever drawn. Amara "
        "walked at its front beside Osadebe. Ozoemena walked near the "
        "back, quiet in the particular way he had learned to be quiet "
        "since his own fall. Elder Maka walked apart from both, her "
        "steps slower than the rest, carrying a weight none of them "
        "could fully see."
    )},
    {"type": "body", "text": (
        "Chibundu was waiting at the last stone when they arrived, "
        "standing rather than hidden among the roots the way he might "
        "once have been, and Amara felt her own chest tighten watching "
        "the whole council take him in for the first time as a person "
        "rather than a name argued over beneath a mango tree. He was "
        "not what any rumor had prepared them for. He looked, more than "
        "anything, simply like a boy trying very hard to stand still "
        "under the weight of being looked at by so many strangers at "
        "once."
    )},
    {"type": "body", "text": (
        "Elder Maka stopped several strides back from where the rest "
        "of the circle gathered, and Chibundu, sensing the particular "
        "shape of her stillness, spoke to her directly before anyone "
        "else could open the council properly. \"You are the one who "
        "lost a son to this same ground,\" he said, gently, not as an "
        "accusation but as a fact he had clearly turned over carefully "
        "before choosing to name it aloud. \"I am not him. I know that "
        "does not undo what he cost you. I only wanted you to hear it "
        "from me before we spoke of anything else.\""
    )},
    {"type": "body", "text": (
        "Something in Elder Maka's face moved that none of the "
        "watching council had ever seen it do, not in judgment, not in "
        "grief exactly, but in a kind of stunned, careful recognition. "
        "\"My son screamed before he ever spoke a kind word to anyone "
        "again,\" she said quietly. \"You are the first thing to come "
        "back out of that ground in my lifetime who spoke a kind word "
        "first. I do not yet know what to do with that. I did not "
        "expect, coming here, to need to know.\""
    )},
    {"type": "body", "text": (
        "Adaugo, standing close enough to her mother now that no one "
        "in the council thought to remark on the distance anymore, "
        "studied Chibundu with an attention that had none of Elder "
        "Maka's old dread in it, only a careful, searching curiosity. "
        "\"You knew to say that before anyone told you it needed "
        "saying,\" she said. \"That is not something the stories about "
        "you ever mentioned.\" Chibundu met her look steadily. \"The "
        "entity taught me a great deal,\" he said, \"but it did not "
        "teach me that. I have simply had a great deal of time lately "
        "to think about what I would want to hear, if I were standing "
        "where she is standing.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE BOY'S OWN CONDITIONS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe opened the council properly once the whole circle had "
        "settled, addressing Chibundu directly rather than the entity "
        "beside him. \"You asked to help decide this yourself,\" he "
        "said. \"Then tell us plainly. Do you want to meet this man.\""
    )},
    {"type": "body", "text": (
        "\"Yes,\" Chibundu said, and the plainness of it seemed to "
        "surprise even Amara, who had expected fear or refusal rather "
        "than a clear, considered want. \"Not because I trust him. "
        "Because I am tired of being a story other people argue over "
        "without ever once asking what I think the story should be. If "
        "this House is going to decide something about me eventually, "
        "I would rather be in the room, or the field, when it happens, "
        "than learn about it after, the way I have learned about most "
        "things concerning my own life.\""
    )},
    {"type": "body", "text": (
        "Ozoemena, listening from the circle's edge, spoke the "
        "question others seemed reluctant to ask directly. \"And what "
        "would you want, if the council agrees. What terms would make "
        "this safe enough to risk.\""
    )},
    {"type": "body", "text": (
        "Chibundu answered as though he had already turned the "
        "question over many times before anyone else asked it aloud. "
        "\"He comes to the boundary, not past it. The entity stays "
        "close enough to act, though not standing between us the whole "
        "time, since I do not want this to look like something I need "
        "protecting from rather than something I chose. A fixed span, "
        "counted the way my mother's reunion was counted. And Chidebe's "
        "men watching from a distance they cannot close quickly enough "
        "to matter, but close enough to see everything.\""
    )},
    {"type": "body", "text": (
        "Amara felt a fierce, complicated pride move through her "
        "hearing him lay out terms with the same careful precision "
        "Osadebe himself might have used, and understood, watching the "
        "council absorb it, that whatever else this season had cost "
        "her son, it had also built something in him no one, not even "
        "the entity, had fully planned for."
    )},
    {"type": "body", "text": (
        "The entity spoke for the first time since the council had "
        "arrived, its voice carrying through the air the way it had "
        "learned to make itself heard without borrowing anyone's mouth. "
        "\"I will honor every term he has set,\" it said, \"including "
        "the one he did not say aloud, which is that I am to trust him "
        "enough not to hover close enough to make the meeting look like "
        "his cage rather than his choice. I have spent three centuries "
        "learning patience. I did not expect the hardest use of it yet "
        "would be standing still while he faces something alone that I "
        "am fully capable of ending myself.\""
    )},
    {"type": "body", "text": (
        "Chidebe, who had said little through the whole exchange, "
        "offered the one condition that belonged properly to him rather "
        "than to Chibundu or the entity. \"My men hold the wider "
        "ground,\" he said. \"Not to control what happens between the "
        "boy and this Factor, but so that whatever answer today "
        "produces, good or bad, does not have to travel back to Idoro "
        "through rumor before the truth of it does.\" No one in the "
        "circle found reason to object."
    )},
    {"type": "body", "text": (
        "The council's vote, when Osadebe finally called for it, came "
        "quickly and with less argument than anyone had expected. Elder "
        "Maka was the last to speak before it was cast, her voice "
        "steadier than it had been all morning. \"I came here prepared "
        "to see a danger,\" she said. \"I find I am voting instead for "
        "a boy who has just shown more restraint than most grown men in "
        "this circle have managed all season. Let him have his meeting, "
        "on his own terms, and let us finally be a village that trusts "
        "someone's judgment about his own life before fear has the "
        "chance to decide it for him.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A PATIENCE THAT DID NOT WAIT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The council's satisfaction lasted only as long as it took "
        "Chidebe's runner to reach them, breathless from having run the "
        "whole distance rather than trust the news to a walk. \"The "
        "Factor's camp,\" he said. \"It stood two full days from here "
        "when he first arrived. My watchers report it now stands less "
        "than half a day's walk from this very boundary, moved sometime "
        "in the night, before any of us had given him an answer to "
        "anything.\""
    )},
    {"type": "body", "text": (
        "Osadebe felt the whole morning's fragile relief drain out of "
        "him at once. \"He told us a few more days would cost him "
        "nothing,\" he said slowly. \"He did not say those days would "
        "be spent standing still.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt the entity go taut beside him, the same "
        "particular stillness it wore whenever a calculation it had "
        "trusted turned out to have been missing a piece all along, and "
        "understood, watching the council's faces shift from cautious "
        "hope back into the older, more familiar shape of alarm, that "
        "whatever kind of patience the Factor had shown them at the "
        "mango tree, it had never once meant standing still."
    )},
    {"type": "body", "text": (
        "\"He gave us days to decide and spent the nights closing the "
        "distance those days were supposed to buy him,\" Osadebe said, "
        "turning the arithmetic over aloud the way he had turned over "
        "every other unwelcome fact this season had handed him. \"Either "
        "he never intended to wait for our answer at all, or he wanted "
        "to be close enough to receive it the instant it came, "
        "regardless of what that answer turned out to be.\""
    )},
    {"type": "body", "text": (
        "Elder Maka's earlier certainty had not entirely left her, but "
        "it had grown a harder edge around it. \"Perhaps both can be "
        "true,\" she said. \"A patient man does not need to choose "
        "between courtesy and readiness. He can offer one while "
        "quietly arranging the other, and call the whole of it "
        "patience regardless of which part was ever meant kindly.\""
    )},
    {"type": "body", "text": (
        "Chibundu turned the news over the way he had learned to turn "
        "over every hard thing this season had handed him, refusing to "
        "let the fear in it simply decide his answer for him. \"Then we "
        "do not change the terms because he moved early,\" he said. "
        "\"We hold them exactly as we set them, and we let him learn, "
        "meeting me on my own ground under my own conditions, that "
        "moving closer in the dark does not actually buy him anything "
        "he did not already have a right to ask for honestly in the "
        "daylight.\""
    )},
    {"type": "body", "text": (
        "The entity felt something steady itself in the boy beside it, "
        "a calm that did not come from an absence of fear but from a "
        "decision made in spite of it, and understood, watching the "
        "council disperse to carry the news back to a village that "
        "would sleep very little that night, that whatever the "
        "following days brought, Chibundu intended to meet them "
        "standing rather than braced."
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
                    first_line_indent=None, spacing_before=0):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing_attrs = {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    }
    if spacing_before:
        spacing_attrs[f"{{{NS_WORD}}}before"] = str(spacing_before)
    spacing = make_element("spacing", spacing_attrs)
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


def make_body_paragraph(text, spacing_after=60, spacing_line=360,
                        spacing_before=0):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360,
                           spacing_before=spacing_before)


def make_system_paragraph(text, spacing_after=120, spacing_line=360,
                          spacing_before=0):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0,
                           spacing_before=spacing_before)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

# Vertical space (twips) inserted before the first paragraph of a new scene.
# 480 twips = 24pt: the page shows a clear scene break, but no empty
# paragraph exists for the TTS engine to turn into dead air.
SCENE_BREAK_SPACE = 480

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    pending_scene_break = False

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

        if typ == "scene_break":
            pending_scene_break = True
            continue

        before = SCENE_BREAK_SPACE if pending_scene_break else 0

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
            para = make_body_paragraph(text, spacing_before=before)
            pending_scene_break = False
        elif typ == "system":
            para = make_system_paragraph(text, spacing_before=before)
            pending_scene_break = False
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

# --- LINT (TTS pacing, CLAUDE.md Section 3.10) ---

def lint_content():
    """Check narration text for TTS pacing violations."""
    problems = []
    for i, item in enumerate(EPISODE_CONTENT):
        if item["type"] not in ("body", "system"):
            continue
        text = item["text"]
        if "\u2014" in text or "\u2013" in text:
            problems.append(f"  item {i}: contains a dash: {text[:60]}")
        if "  " in text:
            problems.append(f"  item {i}: double space: {text[:60]}")
        if re.search(r"\w-\w", text):
            problems.append(f"  item {i}: hyphenated word: {text[:60]}")
    return problems


def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 58: \"A Seat at the Boundary\"")
    print("  Build Script")
    print("=" * 60)
    print()

    problems = lint_content()
    if problems:
        print("  LINT PROBLEMS:")
        for p in problems:
            print(p)
        print()
    else:
        print("  Lint clean: no dashes, double spaces, or hyphenated words")

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_58.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_58.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
