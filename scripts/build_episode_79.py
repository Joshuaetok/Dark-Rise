#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 79: "The Third Bend in the River"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-24: Episode 79 turns Episode 78's quiet dread into a
race against the clock. Adaugo, during a rites lesson with Elder Maka,
mentions the friendly traveler who questioned her at the grinding
stone, and Elder Maka recognizes too late exactly what was being
gathered. By the time the danger is named, Adaugo has already left for
her ordinary, unguarded evening walk to see Zara. The episode closes
mid stride, at the third bend in the river path, with Adaugo finding
the same traveling woman waiting for her, calm and no longer
performing ordinary curiosity, as the light fails.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_79.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Nine"},
    {"type": "title_ep_name", "text": "The Third Bend in the River"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A DETAIL TOLD TOO LATE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Adaugo knelt across from Elder Maka in the swept dirt of the "
        "family compound, repeating the binding words her mother had "
        "been teaching her properly for a full season now, careful "
        "lessons finally beginning to settle into something resembling "
        "memory rather than mimicry. She stumbled twice over "
        "the same line, laughed at herself, and mentioned, almost as an "
        "afterthought between one attempt and the next, the pleasant "
        "traveling woman who had asked her so many questions at the "
        "grinding stone the day before."
    )},
    {"type": "body", "text": (
        "Elder Maka's hands went still over the small clay bowl between "
        "them. \"What questions,\" she asked, keeping her voice even "
        "with an effort Adaugo did not notice."
    )},
    {"type": "body", "text": (
        "\"Whether Zara was resting somewhere close. Whether she had "
        "been sent away.\" Adaugo shrugged, reaching for the next line "
        "of the rite. \"I told her Zara was at Amara's compound, past "
        "the third bend. She asked whether I walked there alone in the "
        "evenings. I did not think anything of it. Travelers ask "
        "questions. It is what makes them travelers.\""
    )},
    {"type": "body", "text": (
        "Elder Maka felt the whole shape of the danger she had "
        "described to Amara only a day earlier settle into place at "
        "once, cold and complete. A working that requires nearness, "
        "repeated across many nights. A hand patient enough to ask its "
        "questions gently, in the open market, in broad daylight, "
        "rather than steal the answers by force. \"Describe her to me,\" "
        "she said, already rising. \"Everything you remember. Quickly.\""
    )},
    {"type": "body", "text": (
        "Adaugo's easy expression faltered as she watched her mother's "
        "face change. \"An ordinary woman,\" she said slowly, groping "
        "now for details she had not thought worth keeping. \"Plain "
        "cloth. A traveler's pack. Nothing about her that I would "
        "know again in a crowd, except that she asked more than she "
        "answered, now that I think of it properly.\""
    )},
    {"type": "body", "text": (
        "\"When did you tell her you visit Zara,\" Elder Maka asked, "
        "already knowing the answer would be the one she feared most."
    )},
    {"type": "body", "text": (
        "\"Most evenings,\" Adaugo said. \"A little before the last "
        "light. The same as always.\" She looked toward the sun, "
        "already low over the compound wall, and understood, a "
        "heartbeat behind her mother, exactly what hour it currently "
        "was."
    )},
    {"type": "body", "text": (
        "Elder Maka pressed one hand flat against her own chest, "
        "steadying a fear that had not moved through her body this "
        "fast since the night she absorbed Kene's severed thread. Her "
        "grandmother's old warning surfaced whole, a line she had not "
        "spoken aloud in years. A patient house does not ask for what "
        "it wants directly. It asks for small, harmless things, from "
        "small, harmless people, until it has been handed everything it "
        "needed without a single door ever being forced. \"You did "
        "nothing wrong,\" she told Adaugo, gripping her daughter's "
        "shoulders. \"A kind stranger asking kind questions is not a "
        "sin. But we must move now, and we must move faster than fear "
        "will let either of us think clearly.\""
    )},
    {"type": "body", "text": (
        "Adaugo's own fear had caught up to her fully by then, her "
        "hands trembling around the half finished binding bowl. \"I "
        "will run for her myself,\" she said, already rising."
    )},
    {"type": "body", "text": (
        "\"No,\" Elder Maka said, sharper than she meant to. \"If this "
        "is what I believe it is, you are the one thing she has already "
        "learned enough about to use. Stay here. Let those who can "
        "still move safely go.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT ZARA COULD NOT FEEL
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "At Amara's compound, Zara sat waiting for Adaugo the way she "
        "waited every evening now, the small pleasure of a familiar "
        "visit the closest thing to normal her days had held since the "
        "quiet first frightened her. When the appointed hour came and "
        "went without the sound of Adaugo's sandals on the path, she "
        "told "
        "herself it meant nothing, that Elder Maka had likely kept her "
        "daughter longer than usual over some stubborn line of the "
        "rite."
    )},
    {"type": "body", "text": (
        "But the old habit of listening for danger, worn down as it "
        "was, still reached for something anyway, out of a lifetime's "
        "instinct rather than any real gift left to answer it. Zara "
        "closed her eyes and reached the way she used to reach without "
        "thinking, toward the river path, toward the third bend, toward "
        "whatever Adaugo might be walking into, and felt only the same "
        "muffled nothing that had frightened her at the tree line two "
        "days earlier."
    )},
    {"type": "body", "text": (
        "\"I cannot tell if something is wrong,\" she said aloud to no "
        "one, rising to her feet anyway, her whole body certain in a "
        "way her senses no longer were. \"I do not know if that is fear "
        "talking, or the last honest thing I have left trying to reach "
        "me through a door someone else has already shut.\" She was "
        "already moving toward the gate when she heard the commotion "
        "rising from Elder Maka's compound, and broke into a run "
        "without waiting to learn why."
    )},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE RACE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka ran for Amara's compound faster than her own body "
        "had moved in years, arriving breathless and already speaking "
        "before she had fully crossed the threshold. \"Adaugo told the "
        "traveler everything,\" she said. \"The path, the hour, that "
        "she walks it alone. She left for Zara's already, before I "
        "understood what I was hearing.\""
    )},
    {"type": "body", "text": (
        "Amara's face drained of color in a way Chibundu would later "
        "say he felt echo faintly all the way to Oso. \"How long ago,\" "
        "she demanded, already moving toward the gate."
    )},
    {"type": "body", "text": (
        "\"Long enough that walking will not catch her,\" Elder Maka "
        "said. \"We must run, or send someone who can outrun her "
        "start.\""
    )},
    {"type": "body", "text": (
        "Chidebe, summoned by the noise, was already redirecting two "
        "of his soldiers toward the river path before Amara finished "
        "explaining, his earlier frustration at having too much ground "
        "and too few men now sharpened into something close to fury at "
        "himself. \"We watched the boundary and the tree line,\" he "
        "said, half to himself, half to no one. \"We never once thought "
        "to watch the path everyone in Idoro considers too ordinary to "
        "fear.\""
    )},
    {"type": "body", "text": (
        "Osadebe took the fastest horse in the garrison's small string "
        "and rode for the river without waiting to be told, calling "
        "back only that he would reach the third bend well ahead of "
        "any soldier on foot. Amara ran behind him anyway, unwilling to "
        "trust her daughter's safety to distance and speed alone, Obi "
        "close beside her, neither one saying what they both now feared "
        "plainly."
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt Idoro's ambient dread spike sharply "
        "and without warning, a fear too sudden and too specific to be "
        "the village's usual low hum of worry. It reached toward the "
        "feeling instinctively and found only distance between itself "
        "and whatever had caused it, the same helpless gap it had "
        "learned to hate since the night it could not be the one to "
        "reach Kene in time. Something is happening, it told Chibundu, "
        "and I cannot tell you what, only that it is close to Zara and "
        "moving faster than any of them can outrun."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE THIRD BEND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Adaugo walked the river path the same unhurried way she "
        "walked it every evening, a small covered bowl of food balanced "
        "against her hip for Zara, humming the same tune under her "
        "breath that she had hummed at the grinding stone the morning "
        "before. The light was going fast now, the low gold of late "
        "afternoon already curdling toward the gray that came before "
        "true dark, and she quickened her pace only slightly, out of "
        "habit rather than any particular unease."
    )},
    {"type": "body", "text": (
        "It was the quiet that finally caught her attention, the way "
        "quiet always eventually catches the attention of anyone who "
        "has walked the same path enough times to know its ordinary "
        "noise by heart. The birds that usually settled loudly into the "
        "reeds ahead of the third bend had already gone silent. No "
        "insects called from the tall grass. Even the river itself "
        "seemed to be running with less voice than it should have, as "
        "though the whole evening were holding something back."
    )},
    {"type": "body", "text": (
        "Adaugo slowed without deciding to, the covered bowl suddenly "
        "heavier against her hip than it had been a moment before, and "
        "rounded the third bend into the last of the failing light."
    )},
    {"type": "body", "text": (
        "The traveling woman from the market was already there, "
        "standing exactly in the center of the path, not admiring "
        "stones now, not asking gentle questions about healers resting "
        "somewhere close. She stood perfectly still, watching Adaugo "
        "approach with an unhurried patience that had nothing ordinary "
        "left in it at all."
    )},
    {"type": "body", "text": (
        "\"You walk this path most evenings,\" the woman said, her "
        "voice carrying easily across the quiet she had somehow made of "
        "the whole riverbank. \"A little before the last light. The "
        "same as always. You told me so yourself.\""
    )},
    {"type": "body", "text": (
        "Adaugo's feet stopped moving before her mind had finished "
        "understanding why they should, the covered bowl slipping "
        "slightly in her grip, her mother's unfinished warning arriving "
        "in her memory a full breath too late to have done her any "
        "good at all. \"Who are you,\" she managed, proud of how little "
        "her voice shook even as the rest of her had already begun to."
    )},
    {"type": "body", "text": (
        "\"Someone who has waited a long while to meet the woman Zara "
        "has grown to love best,\" the traveler said, taking one "
        "unhurried step closer, her hand drifting, almost gently, "
        "toward something small and wrapped at her own hip. \"You have "
        "no reason to be afraid of me yet. I have not decided what I "
        "need from you. That decision belongs to whoever comes running "
        "down this path in the next few moments, and how much they are "
        "willing to trade to keep you standing exactly where you are.\""
    )},
    {"type": "body", "text": (
        "Somewhere behind Adaugo, faint but closing, she heard what "
        "might have been footsteps on the packed river path, or might "
        "have been only her own heartbeat finally loud enough to hear. "
        "The traveling woman tilted her head toward the sound with the "
        "same unhurried patience she had spent two whole days building, "
        "and smiled at Adaugo as though the two of them now shared a "
        "secret neither had asked for."
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
    print("  THE DARK RISE — Episode 79: \"The Third Bend in the River\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_79.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_79.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
