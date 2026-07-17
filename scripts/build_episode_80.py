#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 80: "What Adaugo Carried Home"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-25: Episode 80 resolves Episode 79's cliffhanger.
Osadebe reaches the third bend in time to force Mfoniso to abandon
whatever she came for, but not before she grips Adaugo's wrist and
murmurs something too fast to catch, then vanishes into the reeds
without a trace. The family finds Adaugo physically unharmed and
allows itself real relief, believing the danger passed. The episode
closes on Zara, embracing Adaugo in that relief, feeling a faint cold
thread on Adaugo's wrist exactly where the woman held her, answering
her reach the way her own gift used to before it was muffled, meaning
Mfoniso did not fail at the third bend. She got exactly what she came
for.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_80.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty"},
    {"type": "title_ep_name", "text": "What Adaugo Carried Home"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE REEDS TAKE HER BACK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe's horse came around the third bend still at a hard "
        "run, throwing dark clots of mud where the packed path gave way "
        "to riverbank, and in the last stretch before he could rein it "
        "in he saw everything the failing light would allow him to see. "
        "Adaugo stood rigid, the covered bowl broken open at her feet. "
        "The traveling woman's hand was closed gently around Adaugo's "
        "wrist, as though she had all the time left in the evening to "
        "use it."
    )},
    {"type": "body", "text": (
        "Osadebe shouted something wordless, more warning than words, "
        "and hauled the horse hard toward them. The woman did not "
        "startle. She did not even quicken. She looked up at him the "
        "way a person looks up at weather rather than danger, "
        "unhurried, already finished with whatever calculation his "
        "arrival had forced on her."
    )},
    {"type": "body", "text": (
        "\"You came faster than I allowed for,\" she said, not to "
        "Osadebe, but to Adaugo, as though continuing a private "
        "conversation the soldier had merely interrupted rather than "
        "ended. Her grip tightened once, brief and almost gentle, and "
        "she murmured something too low and too quick for Adaugo to "
        "catch more than the shape of it, three or four words folded "
        "into a single breath."
    )},
    {"type": "body", "text": (
        "Then she let go."
    )},
    {"type": "body", "text": (
        "Adaugo staggered back a full step, more from the sudden "
        "absence of that grip than from any push, and by the time she "
        "found her footing the woman was already moving, not running "
        "exactly, but covering ground with an ease that made running "
        "look clumsy by comparison, gone into the tall reeds at the "
        "river's edge before Osadebe's horse had fully closed the "
        "distance."
    )},
    {"type": "body", "text": (
        "He reached Adaugo and swung down before the animal had "
        "stopped moving, catching her by the shoulders the way a man "
        "catches something he is afraid has already fallen. \"Are you "
        "hurt,\" he said, turning her face toward what little light "
        "remained. \"Did she cut you. Mark you. Anything.\""
    )},
    {"type": "body", "text": (
        "\"No,\" Adaugo said, her voice thinner than she meant it to "
        "be. \"She only held my wrist. She said something. I could not "
        "hear it properly.\" She looked down at her own arm as though "
        "expecting to find a mark there and found only ordinary skin, "
        "unbroken, faintly cold where the woman's fingers had been and "
        "nowhere else."
    )},
    {"type": "body", "text": (
        "Osadebe left her only long enough to plunge into the reeds "
        "after the woman, sword drawn, calling ahead of himself in a "
        "voice meant to sound larger than one man alone. He found "
        "nothing. No parted grass beyond the first few strides. No "
        "print in the soft mud along the water's edge, though he stood "
        "in that same mud himself and sank to his ankle with every "
        "step. He came back out slower than he had gone in, unwilling "
        "to say aloud what the absence of any trail meant to a man who "
        "had spent his whole life reading ground for a living."
    )},
    {"type": "body", "text": (
        "He crouched beside Adaugo again once he had given up the "
        "chase, turning her wrist gently toward what little light was "
        "left. \"Two days ago I found her footprints on the high ground "
        "above your compound,\" he said, half to Adaugo, half to "
        "himself, working through something that did not sit right. "
        "\"Careless prints. A woman who did not yet know she needed to "
        "hide herself from us. Tonight she leaves none at all, in "
        "softer ground than that ridge ever was.\" He looked up toward "
        "the darkening tree line as though the answer might be written "
        "there. \"That is not a woman growing careful. That is a woman "
        "who no longer needs to run.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE SEARCH COULD NOT FIND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By the time Chidebe's soldiers reached the bend, running the "
        "last stretch on foot, there was nothing left to find but a "
        "broken bowl and a frightened girl standing very still in the "
        "near dark. They fanned out along the bank anyway, more out of "
        "duty than hope, and came back one by one with the same report. "
        "Nothing. No woman. No footprints. No sign that anyone had "
        "stood there at all beyond what Adaugo and Osadebe both swore "
        "had happened in front of them."
    )},
    {"type": "body", "text": (
        "Amara reached the bend at a dead run with Obi a stride behind "
        "her, and whatever composure either of them had managed on the "
        "way there broke completely at the sight of Adaugo alive and "
        "upright. Amara pulled her into an embrace hard enough to hurt, "
        "saying her name twice before she could manage anything else, "
        "and Adaugo let herself be held the way she had not let herself "
        "be held since she was a child small enough to be carried."
    )},
    {"type": "body", "text": (
        "Elder Maka arrived last of the family, having run the whole "
        "distance on legs that had not been asked to move that fast in "
        "years, and went to her daughter without a single word wasted "
        "on her own exhaustion. She took Adaugo's face in both hands, "
        "then her wrists, then turned her palms up to the last of the "
        "light, searching for whatever a mother's eyes might catch that "
        "a soldier's would not. She found nothing either. No mark. No "
        "burn. No thread visible to sight."
    )},
    {"type": "body", "text": (
        "\"She is whole,\" Elder Maka said finally, and the relief in "
        "her own voice surprised her, as though she had not fully "
        "believed it until she said it aloud. \"Frightened. Cold to the "
        "touch where she was held. But whole.\""
    )},
    {"type": "body", "text": (
        "Obi knelt in front of Adaugo and made her repeat, slowly, "
        "everything the woman had said, hunting for anything that might "
        "be turned into a warning for the next person she cornered. "
        "Adaugo tried three times to recover the murmured words from "
        "the moment of the grip itself and failed each time, the "
        "syllables sliding away from her the harder she reached for "
        "them, as though the sound had never fully belonged to her "
        "hearing in the first place. \"I know it was not a threat,\" "
        "she said finally, frustrated with her own memory. \"It did not "
        "sound like a threat. It sounded like she was finishing "
        "something.\" Amara asked her to try once more, gently, and "
        "Adaugo only shook her head, exhausted past the point of being "
        "useful to anyone, and Amara let it go rather than push her "
        "further that night."
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt the sharp edge of Idoro's dread begin, "
        "at last, to ease, the way a held breath eases once the danger "
        "it was held against has passed. It told Chibundu as much, "
        "relief plain even in a voice that rarely allowed itself the "
        "shape of relief. But something in the easing troubled it more "
        "than the fear had, a wrongness it could not yet put a true "
        "name to. \"She let herself be seen tonight,\" it said slowly, "
        "turning the fact over as it spoke. \"A hunter who has spent "
        "this many days unseen does not simply forget herself and get "
        "caught by a soldier on a horse. She chose to be found.\" "
        "Chibundu asked what that meant. The entity did not answer for "
        "a long moment. \"I do not think she left because she failed,\" "
        "it said at last. \"I think she left because she was "
        "finished.\""
    )},
    {"type": "body", "text": (
        "Chibundu pressed his palm flat against the cold ground of Oso, "
        "wishing, not for the first time, that whatever bound him to "
        "this place let him cross the distance to Idoro the way the "
        "presence once had, at whatever cost. \"Adaugo did nothing to "
        "deserve being used this way,\" he said. \"She only answered a "
        "kind question from a stranger.\" The entity did not try to "
        "comfort him with a smaller version of the truth, the way it "
        "sometimes had in gentler moments. \"That is exactly why it "
        "worked,\" it said quietly. \"A hunter who needs force is "
        "limited by how much force she can use unnoticed. A hunter who "
        "needs only kindness is limited by nothing at all.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE COLD THAT ANSWERED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The family began the walk home together, Adaugo held close "
        "between Amara and Elder Maka, Obi and Osadebe flanking them "
        "with drawn weapons neither expected to need again that night. "
        "Chidebe stayed behind with two of his soldiers to keep watch "
        "at the bend until full dark, in case the woman's retreat "
        "proved less final than it looked."
    )},
    {"type": "body", "text": (
        "Zara reached them on the path halfway back, having run the "
        "whole distance from Elder Maka's compound without stopping to "
        "catch the breath she needed, and did not slow until she had "
        "both arms around Adaugo, holding her the way she had once held "
        "Kene the night the presence pulled him back from the dark. "
        "\"You are here,\" Zara said into her shoulder, half question, "
        "half prayer answered. \"You are actually here.\""
    )},
    {"type": "body", "text": (
        "It was only in the holding, in the ordinary press of one "
        "frightened body against another, that Zara felt it. A cold "
        "thread, faint and fading even as she noticed it, running "
        "through the exact place on Adaugo's wrist where the woman's "
        "hand had been. Not the muffled nothing that had haunted her "
        "own senses for days. Something else. Something that answered "
        "when she reached for it, the way her own gift used to answer "
        "before it was taken from her, except this time the answer was "
        "not coming from inside herself at all."
    )},
    {"type": "body", "text": (
        "Zara went very still, her arms still locked around Adaugo, "
        "her whole body caught between finishing the embrace and "
        "pulling away from it entirely. \"Elder Maka,\" she said, her "
        "voice thin and careful, the words already trying to leave her "
        "before she had fully decided what they meant. \"Something is "
        "still here. On her. I can feel it, and it is not mine.\""
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
    print("  THE DARK RISE — Episode 80: \"What Adaugo Carried Home\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_80.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_80.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
