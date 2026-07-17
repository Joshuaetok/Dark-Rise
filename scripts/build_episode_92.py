#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 92: "The Reckoning"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-07: Episode 92 moves from the immediate crisis into
its formal aftermath. Elder Maka finally examines Adaugo's anchor
thread in full daylight and finds it gone strangely inert, the working
apparently overloaded past repair by the entity's direct intervention,
a genuine and hard won relief. The household council formally resolves
Emenike's status, choosing conditional trust and a role in the search
for his sister over punishment, a decision Amara argues for and
Ozoemena seconds. Osadebe writes the most urgent report of his career
to Udo, telling Eze Amadi's court that Oso's guardian has now acted
directly for the first time in three centuries. The episode closes on
Mfoniso, recovering alone beyond Idoro's boundary, deciding that a
setback this significant cannot be explained in a message left under a
stone, and setting out on the long journey to deliver her account to
the Warden in person for the first time in her career.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_92.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Two"},
    {"type": "title_ep_name", "text": "The Reckoning"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: WHAT DAYLIGHT FOUND ON HER WRIST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka examined Adaugo's wrist properly at last once the "
        "household had slept, eaten, and steadied itself enough to make "
        "her hands trustworthy again, expecting to find the anchor "
        "thread changed in some way she would need new caution to "
        "understand. What she found instead surprised her far more. "
        "Nothing answered her touch at all."
    )},
    {"type": "body", "text": (
        "\"It is quiet,\" she said slowly, testing the working from "
        "three different angles before she trusted the result enough to "
        "say it aloud. \"Not hidden. Not waiting. Quiet, the way a fire "
        "goes quiet once it has burned through everything it had left "
        "to burn.\" Adaugo flexed her fingers, watching her own wrist as "
        "though it belonged to someone else. \"You believe it is "
        "finished,\" she said. \"I believe whatever the entity's reach "
        "did to Mfoniso, it did something to this working too,\" Elder "
        "Maka said. \"Overloaded past whatever careful shape she built "
        "it to hold. I will not swear to it. But for the first time "
        "since the third bend, I do not feel her watching through it.\""
    )},
    {"type": "body", "text": (
        "Amara watched the examination from a few careful paces away, "
        "having learned across many crises exactly how much room Elder "
        "Maka needed to work without an anxious mother crowding her "
        "elbow. \"What if you are wrong,\" she asked, once Elder Maka "
        "sat back from the wrist at last. \"What if it is only resting, "
        "the way she once let it rest before.\" Elder Maka did not "
        "pretend the fear was foolish. \"Then we will learn that too,\" "
        "she said, \"and we will meet it again, the way we have met "
        "everything else. But I do not think a working built to answer "
        "questions can survive the answering being torn out of it by "
        "force. I think it broke tonight, the same way its maker very "
        "nearly did.\""
    )},
    {"type": "body", "text": (
        "Obi crouched to look at his daughter's wrist himself, though he "
        "had no gift for reading workings and knew it, simply needing "
        "to see the ordinary skin there with his own eyes. \"It looks "
        "like a wrist again,\" he said, and the small, helpless "
        "gratitude in his voice said more than a longer sentence could "
        "have. Adaugo laughed for the first time since the attack, "
        "short and startled by her own laughter. \"It has always looked "
        "like a wrist, Baba,\" she said. \"That was rather the problem.\""
    )},
    {"type": "body", "text": (
        "Kene wandered over to examine the fuss himself, tugging at "
        "Adaugo's sleeve until she lifted him to see. \"Is the cold gone "
        "now,\" he asked, remembering, in the plain way children "
        "remember frightening things precisely, every detail adults "
        "hoped they had missed. \"I think so,\" Adaugo told him, and "
        "found she meant it."
    )},
    {"type": "body", "text": (
        "The relief that moved through the compound at the news was "
        "quiet rather than celebratory, the particular relief of people "
        "too tired and too recently frightened to trust good news "
        "completely. Zara, checking on Emenike between his lengthening "
        "stretches of true sleep, allowed herself a small, cautious "
        "smile at hearing it. \"One thread closed,\" she said. \"After "
        "everything, I will take it.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE COUNCIL DECIDED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The full council gathered that afternoon, Emenike present on a "
        "mat near the fire rather than confined anywhere else, too weak "
        "to sit fully upright but present all the same, because Amara "
        "had insisted a man be allowed to hear his own judgment rather "
        "than have it delivered to him afterward like a sentence handed "
        "down in absence."
    )},
    {"type": "body", "text": (
        "\"He was coerced,\" Amara said, opening the matter plainly. "
        "\"He confessed before we forced it from him. He bled protecting "
        "a child who is not his own blood. I do not believe justice and "
        "mercy are opposites here. I believe, in this case, they are "
        "asking for the same thing.\" Ozoemena seconded her without "
        "hesitation, and even Osadebe, who had argued hardest for "
        "caution weeks earlier, found he had nothing left to argue "
        "against."
    )},
    {"type": "body", "text": (
        "Chidebe spoke last, and spoke to Emenike directly rather than "
        "about him. \"I trained you,\" he said. \"I watched you become "
        "the soldier every other man measured himself against, and I "
        "did not see what was being done to you underneath all of it. "
        "That failure is mine as much as the silence you kept was "
        "yours.\" Emenike, still weak, managed only a small shake of his "
        "head. \"You could not have seen what I made certain no one "
        "saw,\" he said. \"Do not carry a blame that belongs to me "
        "alone.\""
    )},
    {"type": "body", "text": (
        "The council's decision, when it came, held no ceremony beyond "
        "its own plainness. Emenike would remain a soldier of Idoro, "
        "watched for a season as any wound of trust required watching, "
        "and would be given every resource the household could spare to "
        "help find his sister, once he was strong enough to walk beside "
        "the search rather than merely wait for its result. \"You are "
        "not forgiven because you suffered enough to earn it,\" Elder "
        "Maka told him gently. \"You are forgiven because this house has "
        "decided fear should not be the only thing that shapes a man's "
        "whole future.\" Emenike wept quietly at that, the first tears "
        "anyone in the household had seen from him since his exposure, "
        "and no one thought less of him for it."
    )},
    {"type": "body", "text": (
        "Osadebe spent the rest of the day composing the report he had "
        "been dreading since the moment the entity first reached, "
        "choosing each word with the same care he had once given a "
        "false patrol route, knowing this one detail could not be "
        "softened without lying to a crown that had trusted him to "
        "report the truth exactly as it happened. Oso's guardian, "
        "silent and careful for three centuries, had finally acted "
        "directly. Udo needed to know it, whatever the council decided "
        "to make of it."
    )},
    {"type": "body", "text": (
        "He read the finished report aloud to Amara before sealing it, "
        "a habit he had kept since the very first urgent letter he had "
        "ever sent north, trusting her ear for a phrase that might land "
        "wrong in a distant court more than his own. She listened in "
        "silence until the final line, then nodded once. \"It is "
        "honest,\" she said. \"That is the only thing I ever ask of "
        "your reports. Whatever Udo decides to do with honesty is not "
        "something either of us can control from here.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO CONTINUED: A SEASON OF WATCHING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe added his own name beneath Chidebe's on the report's "
        "closing line, formalizing the season of watching Emenike would "
        "carry alongside his reinstatement, not as a punishment "
        "disguised in gentler language but as the honest shape trust "
        "took when it had to be rebuilt rather than simply assumed. "
        "\"A season is not forever,\" he told Emenike plainly. \"It is "
        "simply long enough for both of us to learn whether today's "
        "faith was earned or merely hoped for.\" Emenike accepted the "
        "terms without complaint, grateful for a shape to the trust he "
        "had to rebuild rather than an unspoken, shapeless doubt that "
        "might never fully lift."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE LONG WALK TO THE WARDEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Two days west of Idoro, Mfoniso tended her own wounds alone in "
        "a hollow she trusted, hands steady out of long habit even as "
        "the rest of her still had not fully stopped shaking. She had "
        "survived worse cuts than the ones she carried now. She had "
        "never once, in a long and careful career, survived being "
        "chased off ground she had entered fully intending to control."
    )},
    {"type": "body", "text": (
        "She considered, as she always did after a failure, writing it "
        "down in the flat, honest language her House expected of her "
        "and leaving it at the nearest safe drop for the Warden to find "
        "in her own time. This time the thought did not settle. A "
        "guardian that had broken three centuries of restraint to meet "
        "her in the open was not news that survived being folded into a "
        "few careful lines of bark cloth."
    )},
    {"type": "body", "text": (
        "\"She needs to hear this from my mouth,\" Mfoniso said aloud, "
        "testing the thought the way she tested every decision that "
        "mattered, and found it held. Not because she feared being "
        "disbelieved. Because a threat of this size, delivered secondhand, "
        "would be weighed by someone who had not felt the cold of it "
        "closing around her own throat, and weighed wrong."
    )},
    {"type": "body", "text": (
        "It would cost her the better part of two weeks, ground she "
        "could ill afford to lose against a household that would only "
        "grow more prepared with every day she was absent. She weighed "
        "that cost against the alternative, a report the Warden could "
        "read once and set aside among a hundred other careful, distant "
        "documents, and found the choice was not actually close at all. "
        "Some warnings had to be carried in a living voice or they were "
        "not truly carried at all."
    )},
    {"type": "body", "text": (
        "She finished binding her wounds, checked the small collection "
        "of tools that had carried her across three seasons of this "
        "hunt, and turned her steps away from Idoro entirely for the "
        "first time since she had accepted this assignment, toward the "
        "long river road and the disguised trading post at its end, "
        "where the Warden kept the House's oldest and most dangerous "
        "secrets, and would now have to make room for one more."
    )},
    {"type": "body", "text": (
        "She did not look back toward Idoro as she walked, a discipline "
        "learned so long ago she no longer had to choose it consciously, "
        "but some small, unfamiliar part of her carried the shape of "
        "that cold reach with her anyway, the first thing in her long "
        "career she had ever failed to leave fully behind on the ground "
        "where it happened."
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
    print("  THE DARK RISE — Episode 92: \"The Reckoning\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_92.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_92.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
