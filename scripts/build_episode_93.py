#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 93: "What the Concern Decides"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-08: Episode 93 follows Mfoniso to the Ijoma Concern's
disguised headquarters downriver, where she delivers her account to the
Warden in person for the first time in her career. The Factor, present
for the report, argues her account finally proves what he has warned
of since Episode 64: that this guardian cannot be safely provoked, and
pushes to abandon the operation entirely. The Warden refuses, revealing
the House's stake in this hunt is older and more personal than simple
business calculation, an inherited debt passed down through generations
of keepers since the guardian ground was lost three centuries ago. Over
the Factor's final, most forceful objection yet, she authorizes
resources beyond anything committed so far, effectively removing the
Factor from further say in the operation. The episode closes with
Mfoniso, escorted past a heavily guarded inner courtyard on her way out,
catching the briefest glimpse of a young woman she recognizes from
Emenike's description, confirming without question that Ijeoma is held
at this same headquarters.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_93.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Three"},
    {"type": "title_ep_name", "text": "What the Concern Decides"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE ACCOUNT GIVEN IN PERSON
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The disguised trading post received Mfoniso the way it "
        "received every arrival, with quiet, practiced indifference on "
        "its surface and careful watchfulness beneath it, guards who did "
        "not announce themselves stationed at every approach a stranger "
        "might use. She had visited twice before in ten years of "
        "service. She had never once come carrying wounds she could not "
        "fully explain even to herself."
    )},
    {"type": "body", "text": (
        "The post's ordinary business continued around her arrival "
        "exactly as it always did, sacks of trade goods stacked against "
        "walls that concealed rooms no honest ledger ever recorded, "
        "clerks moving between them with the unhurried competence of "
        "people who had long since stopped finding anything about this "
        "place remarkable. Mfoniso had always found that ordinariness "
        "useful cover. Tonight it felt, for the first time, faintly "
        "obscene, set against everything she had just survived."
    )},
    {"type": "body", "text": (
        "She had walked the long river road for the better part of two "
        "weeks, resting only as much as her wounds demanded and no "
        "more, turning the account over in her mind at every stop until "
        "she trusted herself to deliver it plainly rather than shaped by "
        "the fear still living somewhere beneath her ribs. A hunter who "
        "let fear choose her words, her teacher had always said, had "
        "already lost twice, once to the danger and once to her own "
        "account of it."
    )},
    {"type": "body", "text": (
        "The Warden received her in the same narrow, windowless room "
        "where the House's oldest ledgers were kept, and listened to the "
        "full account without interrupting once, her face giving away "
        "nothing until Mfoniso reached the part her own memory still "
        "struggled to hold steady, the cold closing around her throat, "
        "undisguised, meeting her directly. Only then did the Warden's "
        "composure crack, briefly, into something that looked almost "
        "like recognition."
    )},
    {"type": "body", "text": (
        "\"Describe exactly what it felt like,\" the Warden said, her "
        "voice tight in a way Mfoniso had never heard from her before. "
        "\"Not what you saw. What it felt like.\" Mfoniso obliged, "
        "choosing her words with the same care she gave everything, and "
        "watched the Warden's knuckles whiten around the edge of her own "
        "ledger as she listened."
    )},
    {"type": "body", "text": (
        "\"You have heard something like this before,\" Mfoniso said "
        "carefully, once the account was fully told, reading the "
        "Warden's stillness for what it plainly was. The Warden did not "
        "deny it. \"I have read of it,\" she said. \"In accounts old "
        "enough that I once doubted whether the keepers who wrote them "
        "were exaggerating out of shame for what they had lost. I no "
        "longer doubt it. You have just confirmed, in your own body, "
        "every word I was taught to half disbelieve.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE FACTOR HAD ALWAYS WARNED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Factor was summoned before the account had even finished, "
        "arriving with the particular grimness of a man who suspected "
        "what he was about to hear before he heard it. He listened to "
        "the account's end standing rather than seated, and when he "
        "finally spoke, his voice carried none of the caution he had "
        "used twice before to soften the same warning."
    )},
    {"type": "body", "text": (
        "\"I told you at the very beginning this guardian had already "
        "cost a prior House every hand it sent against it,\" he said. "
        "\"I told you again after the boundary ambush. I am done telling "
        "you gently. This is no longer a hunt we can afford to continue, "
        "and if we do not end it ourselves tonight, it will end itself "
        "at a cost none of us have the stomach to pay.\""
    )},
    {"type": "body", "text": (
        "Mfoniso said nothing, watching the two of them the way she "
        "watched any confrontation she had not yet decided how to weigh, "
        "aware that whatever was settled in this narrow room would shape "
        "every day of the hunt still ahead of her far more than any "
        "single choice she herself might make in the field."
    )},
    {"type": "body", "text": (
        "The Warden let his words settle fully into the small room "
        "before she answered, and when she did, it was with a stillness "
        "that unsettled Mfoniso more than any raised voice could have. "
        "\"You believe this proves you were right to counsel retreat,\" "
        "she said. \"You are mistaken. It proves the debt is exactly as "
        "large as I have always believed it to be.\""
    )},
    {"type": "body", "text": (
        "The Warden's answer, when it came, held no anger, only a "
        "certainty that unsettled Mfoniso more than anger would have. "
        "\"It stopped being a choice for me the day I was named keeper,\" "
        "she said. \"I do not ask you to understand it as honor. I only "
        "ask you to understand that it will be finished, with or without "
        "your approval of the reasons.\""
    )},
    {"type": "body", "text": (
        "She rose and crossed to the oldest shelf in the room, drawing "
        "down a ledger so worn its cover had gone soft as cloth, and set "
        "it open between them. \"Four keepers before me held this "
        "office,\" she said. \"Each one inherited the same unfinished "
        "account, the same guardian ground taken from a House that could "
        "never win it back. I did not choose this debt. I was born into "
        "it, the way Mfoniso's own craft was handed down to her rather "
        "than invented. I will not be the keeper who lets it go "
        "unfinished simply because it has finally begun to cost what it "
        "was always going to cost.\""
    )},
    {"type": "body", "text": (
        "\"You speak of a debt,\" the Factor said, quieter now but no "
        "less pointed. \"I speak of living people this House still "
        "employs, still sends into danger on the strength of a grudge "
        "none of them chose to inherit. Mfoniso did not ask to be born "
        "into her family's craft any more than you asked to be born "
        "into this office. At what point does an inherited debt stop "
        "being honor and become simply cruelty passed downward because "
        "no one above ever had to pay it themselves?\""
    )},
    {"type": "body", "text": (
        "The Factor's protest, when it came, was his sharpest yet, "
        "invoking the House's dwindling patience, its exposure if the "
        "crown ever traced the operation fully back to its true "
        "sponsors, the plain arithmetic of resources spent against "
        "results returned. The Warden heard all of it and set it aside "
        "with a single, final decision. \"You will be relieved of any "
        "further say in this operation,\" she told him. \"Your caution "
        "has been noted three times now. It will not be needed a "
        "fourth.\""
    )},
    {"type": "body", "text": (
        "She turned to Mfoniso before the Factor had finished absorbing "
        "the blow. \"You will have resources beyond anything committed "
        "to this hunt so far,\" she said. \"Whatever this guardian has "
        "become, it will meet a House that has waited three centuries "
        "and has no intention of waiting a fourth.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE COURTYARD HELD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso left the narrow room with resources she had not asked "
        "for and a mandate heavier than any she had carried before, and "
        "found herself, for the first time in a long career built on "
        "certainty, unsure whether the Warden's conviction comforted her "
        "or frightened her more than the guardian's cold reach had."
    )},
    {"type": "body", "text": (
        "A junior agent led Mfoniso out through the trading post's inner "
        "grounds rather than the way she had entered, a shortcut meant "
        "to spare her wounded body the longer walk around the compound's "
        "outer wall, and the route carried her briefly past a heavily "
        "guarded courtyard she had never had reason to see on her "
        "previous visits."
    )},
    {"type": "body", "text": (
        "She slowed without meaning to, catching, through a gap in the "
        "guarded gate, a single glimpse of a young woman sitting alone "
        "against the far wall, thin, watchful, and unmistakably alive, "
        "her wrists marked with the plain rope burns of someone who had "
        "long since stopped fighting a captivity she could not win "
        "against."
    )},
    {"type": "body", "text": (
        "Mfoniso had never seen Emenike's sister's face. She had never "
        "needed to; the token had always been enough. But something in "
        "the shape of the young woman's watchfulness, the particular "
        "way she held herself apart from the guards around her, matched "
        "every careful detail Mfoniso had absorbed without meaning to "
        "across two seasons of carrying proof of her survival back to a "
        "soldier who loved her."
    )},
    {"type": "body", "text": (
        "She thought, unwillingly, of Emenike's face at their very "
        "first meeting years of messages ago, before she had ever known "
        "his name properly, the specific desperate stillness of a man "
        "who had already decided he would do anything asked of him "
        "rather than risk this exact woman's safety. She had used that "
        "stillness for two seasons without once picturing what stood on "
        "the other end of it."
    )},
    {"type": "body", "text": (
        "It was not guilt, precisely, that moved through her as she was "
        "led past the gate. Mfoniso had made her peace, long ago, with "
        "the costs her craft required of people who had never chosen to "
        "stand near her hunts. It was something closer to a held breath, "
        "the recognition that a fact this useful, once known, could not "
        "simply be unknown again, whatever she eventually decided to do "
        "with it."
    )},
    {"type": "body", "text": (
        "She said nothing of the courtyard to the junior agent walking "
        "beside her, and nothing of it, for now, to herself either "
        "beyond the bare fact of having seen it, filed carefully "
        "alongside every other piece of knowledge a careful hunter "
        "learned to hold close and spend only when the moment finally "
        "asked for it."
    )},
    {"type": "body", "text": (
        "The junior agent noticed her slowing and moved to hurry her "
        "along, offering nothing by way of explanation, and Mfoniso let "
        "herself be led without comment, filing the discovery away "
        "exactly as she filed every other useful fact she was not yet "
        "certain what to do with. Idoro's soldier's leverage had been "
        "here all along, inside the very walls that had just promised "
        "her a war without end."
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
    print("  THE DARK RISE — Episode 93: \"What the Concern Decides\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_93.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_93.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
