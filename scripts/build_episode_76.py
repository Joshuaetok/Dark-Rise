#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 76: "What the Presence Left in Him"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-21: Episode 76 pays off a fear the story has been
quietly building since Episode 70: that the presence's direct,
unprecedented touch on Kene to break Mfoniso's compulsion may not
have been as clean as everyone hoped. Amara finds Kene tracing an
unbidden spiral in the dirt, unprompted, in the exact shape Zara once
traced under both old powers' touch. Chibundu carries the discovery
to the presence, which admits, honestly and with visible discomfort,
that it cannot be certain its intervention left nothing behind. The
episode ends without a clean resolution, Amara facing the possibility
that both her sons may now carry some thread into a world she has
spent this entire season trying to keep at least one of them free of.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_76.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Six"},
    {"type": "title_ep_name", "text": "What the Presence Left in Him"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A SHAPE IN THE DIRT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara found Kene crouched at the compound's edge in the quiet "
        "hour before the evening meal, tracing something into the soft "
        "dirt with one finger, slow and careful and entirely unbothered "
        "by her approach. She recognized the shape before she "
        "consciously understood why it frightened her: a spiral, drawn "
        "from the outside in, the same unhurried pattern she had once "
        "watched Zara's own hand trace without her permission, twice, "
        "in two different seasons. Around them the compound went on "
        "with its ordinary evening noises, wood smoke and a neighbor's "
        "voice and somewhere the small clatter of a cooking pot, all of "
        "it suddenly very far away."
    )},
    {"type": "body", "text": (
        "\"Where did you learn that,\" she asked, keeping her voice "
        "carefully light, unwilling to frighten him before she "
        "understood what she was looking at."
    )},
    {"type": "body", "text": (
        "Kene looked up at her with the plain, unclouded honesty he "
        "brought to most things. \"I did not learn it,\" he said. \"My "
        "hand just wanted to. It felt like remembering something "
        "rather than making it up.\" He looked back down at the "
        "spiral, tracing it once more from the outside in, and Amara "
        "felt the whole of her carefully rebuilt calm since the stream "
        "threaten to come apart at once."
    )},
    {"type": "body", "text": (
        "\"Does your hand feel strange when it does that,\" she asked, "
        "keeping her voice gentle, crouching down to his level the "
        "same way she had once knelt to answer his question about "
        "having a brother. Kene considered this seriously, the way he "
        "considered most questions put to him plainly. \"A little "
        "cold,\" he said. \"Not bad cold. Just cold, like water in the "
        "morning before the sun warms it.\" He did not seem frightened "
        "by the answer at all, which frightened Amara considerably "
        "more than fear would have."
    )},
    {"type": "body", "text": (
        "She called Obi over without raising her voice, unwilling to "
        "startle Kene into hiding a truth that badly needed to stay in "
        "the open, and watched her husband's face move through the "
        "same recognition hers had, the particular dread of a parent "
        "seeing an old fear return wearing a new, smaller shape. \"Not "
        "again,\" Obi said quietly, more plea than statement. \"We "
        "already gave one door to this whole story. I do not know how "
        "to survive believing we have given it two.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: AN HONEST ANSWER SHE DID NOT WANT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu carried the account to the presence himself that "
        "same evening, unwilling to let his mother sit with the fear "
        "even one night longer than she had to, walking the boundary "
        "path with a heaviness he had not felt since the night he "
        "first learned what his own name had cost the people who gave "
        "it to him. \"Tell me plainly,\" he said, reaching the cold "
        "place at last. \"Did you leave something in him, the night "
        "you broke Mfoniso's charm.\""
    )},
    {"type": "body", "text": (
        "I did not intend to, the presence said, and the honesty of "
        "the admission cost it visibly, weakened as it still was. I "
        "reached for him the way I have never reached for anyone "
        "before, faster and rougher than the careful way I once "
        "touched Zara. I was thinking only of breaking the charm's "
        "hold. I was not thinking, in that instant, of what my own "
        "touch might leave behind on ground I had never touched at "
        "all before that night."
    )},
    {"type": "body", "text": (
        "\"Can you be certain,\" Chibundu asked, \"one way or the "
        "other.\""
    )},
    {"type": "body", "text": (
        "No, the presence said. I would like to tell you I can. I "
        "have learned, across this whole season, that a false "
        "certainty offered to spare your family a night's fear costs "
        "considerably more than an honest uncertainty offered "
        "immediately. I do not know if what your brother is tracing in "
        "the dirt is memory, or residue, or simply a child's hand "
        "mimicking a shape he half glimpsed in a moment of terror he "
        "does not otherwise remember."
    )},
    {"type": "body", "text": (
        "The entity, listening, felt the old, familiar dread of a "
        "choice with no clean answer settle over it. \"If there is a "
        "thread,\" it said, \"Elder Maka's rite once severed one "
        "before, at a cost she still carries quietly to this day. I do "
        "not know whether attempting the same rite on a thread this "
        "new and this poorly understood would sever it cleanly, or "
        "simply teach us the same hard lesson twice.\""
    )},
    {"type": "body", "text": (
        "\"And if we do nothing,\" Chibundu asked. \"What does a "
        "thread like that become, left alone, on a boy who has spent "
        "his whole life believing he was the one brother the old world "
        "left untouched.\""
    )},
    {"type": "body", "text": (
        "I do not know that either, the presence admitted. It may "
        "fade on its own, a residue with no root left to feed it, the "
        "way a bruise fades once the blow that caused it is finished "
        "causing harm. It may also deepen, slowly, the way every "
        "thread in this story has ever deepened once it was given time "
        "and attention to grow. I would rather tell you honestly that "
        "I do not know which, than promise you a comfort I have no "
        "real grounds to offer."
    )},
    {"type": "body", "text": (
        "The entity turned the whole dilemma over a final time before "
        "offering the only counsel it felt confident giving. \"Then we "
        "watch, carefully, the way we have learned to watch "
        "everything else this season,\" it said. \"We do not cut "
        "something we do not understand simply because cutting feels "
        "like action. We have already paid once for a rite performed "
        "in haste. I would rather Kene's fate be decided slowly and "
        "correctly than quickly and wrongly.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: BOTH SONS, NOW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu returned to Amara with the whole uncertain account, "
        "unwilling to soften it the way half the truths in this family "
        "had once been softened before costing everyone more for the "
        "delay. Amara listened in a silence that deepened with every "
        "sentence, and when he finished, sat with her hands folded "
        "tightly in her lap, the same stillness she had once brought "
        "to Elder Maka's hardest questions."
    )},
    {"type": "body", "text": (
        "\"I spent a year believing I had one son the old world had "
        "claimed and one son it had left alone,\" she said finally. \"I "
        "do not know how to hold the possibility that it may have "
        "reached for both of them now, in two entirely different "
        "ways, neither of which either of us chose or asked for.\""
    )},
    {"type": "body", "text": (
        "\"We do not act on uncertainty alone,\" Chibundu said, "
        "careful and steady in a way that surprised even him to hear "
        "himself manage. \"We watch. We wait for something clearer "
        "than a spiral drawn once in the dirt. And if it becomes "
        "something more than that, we face it together, honestly, the "
        "same way this family has faced everything else this "
        "season.\""
    )},
    {"type": "body", "text": (
        "\"I do not want him to grow up the way I did,\" Chibundu "
        "added, quieter now, the words costing him something plainly "
        "to say aloud. \"Raised by an old power instead of the mother "
        "who wanted him. If there is any way to keep whatever this is "
        "small enough that he never has to learn it the hard way, the "
        "way I did, I would spend a great deal to make certain of "
        "it.\""
    )},
    {"type": "body", "text": (
        "Amara felt that promise land somewhere raw when Chibundu "
        "finally repeated it to her, understanding for the first time "
        "how much of her older son's own hard won steadiness had been "
        "built directly out of a determination that his brother never "
        "have to build the same thing the same painful way."
    )},
    {"type": "body", "text": (
        "Amara sought out Elder Maka before the night was finished, "
        "unwilling to let the one woman in Idoro who had actually "
        "performed a severing rite go another day without knowing what "
        "might be growing in the second son she had once helped save "
        "from a different thread entirely. Elder Maka listened without "
        "interrupting, her face carrying the particular stillness she "
        "now reserved for anything touching the old, dangerous edges "
        "of this family's story."
    )},
    {"type": "body", "text": (
        "\"I severed Kene's first thread when it was already fully "
        "grown and clearly dangerous,\" she said finally. \"I have "
        "never once attempted to cut something this new, this "
        "uncertain. I do not know if my own hands still remember how, "
        "or whether they ever truly knew how to do this safely at "
        "all. I paid a cost the last time that none of you fully "
        "understood until long after it was already spent.\""
    )},
    {"type": "body", "text": (
        "\"I am not asking you to cut anything tonight,\" Amara said, "
        "her voice steadier than she fully felt. "
        "\"I am asking you to help me understand what watching for "
        "should actually look like, so I am not simply waiting, "
        "helplessly, for my son's hand to draw something worse than a "
        "spiral one morning, unable to tell an ordinary child's habit "
        "from the first quiet sign of something older settling into "
        "him.\""
    )},
    {"type": "body", "text": (
        "Elder Maka considered that request seriously, the way she "
        "considered most things asked of her plainly now rather than "
        "demanded of her in fear. \"Watch his sleep,\" she said. "
        "\"Watch what his hands do when his mind is not directing "
        "them. Watch whether the cold he described grows sharper or "
        "fades. I cannot promise you those signs will tell us enough "
        "in time. I can promise you they are the only honest signs "
        "either of us actually has to watch for.\""
    )},
    {"type": "body", "text": (
        "Amara found Kene later that evening, sleeping soundly, one "
        "small hand curled loosely at his side, and sat with him a "
        "long while, watching for a shape in his dreaming fingers she "
        "hoped, more than she had hoped for almost anything else this "
        "season, she would never actually see them trace again, "
        "whatever quiet, unfinished shape this newest fear eventually "
        "decided to take."
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
    print("  THE DARK RISE — Episode 76: \"What the Presence Left in Him\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_76.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_76.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
