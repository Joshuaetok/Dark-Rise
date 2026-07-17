#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 43: "A Different Hand"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-19: Episode 43 shows the presence beginning to use the
thread it reclaimed through Zara in Episode 42, mirroring the entity's
own early courtship of her in Episodes 14 and 15 closely enough that
Amara recognizes the shape of what is happening before anyone can name
its source — and different enough, in texture and intent, that both
women sense immediately this is not the same danger returning. Zara's
hand moves without her again, but this time she stays fully present
inside her own body the whole time, watching herself draw a shape she
does not recognize but the entity, watching from Oso, recognizes
instantly: the same spiral traced in dirt during her very first waking
intrusion, months ago, drawn now by someone else's hand wearing hers.
The entity chooses to keep watching rather than intervene, unwilling to
expose its own continued interest in a woman it deliberately let go, and
the vessel, increasingly aware of the wider world beyond Oso, asks a
question the entity has no honest way to deflect: whether Zara is in
danger, and whether the entity plans to do anything about it if she is.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_43.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Three"},
    {"type": "title_ep_name", "text": "A Different Hand"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A HAND SHE STILL RECOGNIZES AS HER OWN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara's hand moved on the third morning without her meaning "
        "it to, tracing slow, deliberate lines into the swept dirt of "
        "Amara's yard while she knelt over the washing, and this time "
        "she did not lose a single moment of watching it happen. That "
        "was the detail she kept returning to afterward, the one that "
        "frightened her more than the movement itself. She had not "
        "gone anywhere inside her own mind while it happened. She had "
        "simply sat, fully present, watching her own fingers obey "
        "someone else with the calm, unhurried patience of a hand that "
        "had done this exact motion many times before."
    )},
    {"type": "body", "text": (
        "Amara reached her side before the shape had finished forming, "
        "old memory sharpening every motion, and knelt to study the "
        "spiral traced neat and unhurried in the dirt, coil folding "
        "into coil the way water folds around a stone dropped into "
        "still current. \"This happened before,\" she said quietly. "
        "\"Months ago. Your hand moved the same way, drawing the same "
        "shape, and it was the thing in Oso reaching for you the "
        "first time.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "\"It does not feel the same,\" Zara said, and there was no "
        "hesitation in her voice at all, only the flat certainty of a "
        "woman describing a texture her own skin had already learned "
        "to tell apart. \"That first time felt urgent. Curious, almost "
        "hungry, the way a child pulls at something new to see what it "
        "does. This feels careful. Patient. Like whoever is holding my "
        "hand right now already knows exactly what they want to draw "
        "and is simply taking their time doing it properly.\""
    )},
    {"type": "body", "text": (
        "Amara sat back on her heels, the old fear rearranging itself "
        "into a shape she did not yet have language for. She had "
        "spent a year learning the particular grain of the entity's "
        "hunger, its patience, its transactional care, and this did "
        "not carry that grain at all. It felt older, somehow, and "
        "stranger for being gentler, the way a stranger's polite "
        "knock can sometimes unsettle a house more than an intruder's "
        "forced door."
    )},
    {"type": "body", "text": (
        "\"Do not tell Elder Maka yet,\" Amara said finally. \"Not "
        "until we understand what we are actually looking at. If this "
        "is the same danger wearing a gentler face, panic will only "
        "make it worse for you. And if it is something else entirely, "
        "I would rather know what before this village decides, again, "
        "that the safest answer is simply casting the frightening "
        "thing out.\""
    )},
    {"type": "body", "text": (
        "The decision did not hold past the following afternoon. "
        "Adaugo, drawn by the same instinct that had kept her watching "
        "her mother's compound since the boundary walk, noticed the "
        "faint, swept over marks still visible in the yard's dirt and "
        "asked Amara plainly what had made them, refusing the vague "
        "answer she was first offered with a directness that reminded "
        "Amara sharply of Elder Maka at her most immovable."
    )},
    {"type": "body", "text": (
        "\"My mother spent a season hiding what was happening to her "
        "own body because she believed silence would protect "
        "everyone,\" Adaugo said, when Amara finally admitted the "
        "truth. \"It protected no one. It only meant that when the "
        "truth finally came out, it came out in the worst possible way, "
        "in front of the worst possible crowd. If something new is "
        "happening to Zara, I would rather my mother hear it from you, "
        "quietly, than piece it together later from rumor the way she "
        "learned everything else that ever mattered in this village.\""
    )},
    {"type": "body", "text": (
        "Amara sent for Elder Maka that same evening, and if the "
        "older woman was hurt at being told a full day late, she did "
        "not let it show past a single measured breath before setting "
        "the feeling aside to examine the spiral itself instead, "
        "tracing its coils with one careful finger the way she once "
        "traced boundary stones, searching an old, patient memory for "
        "any shape her grandmother's stories had ever warned her "
        "granddaughter's granddaughter to recognize, passed down "
        "carefully across generations for exactly this kind of night."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — A QUESTION THE ENTITY CANNOT DEFLECT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity watched the spiral form "
        "in Amara's yard through the same faint, careful attention it "
        "had kept trained on Zara's reclaimed thread since discovering "
        "it, and recognized the shape the instant the first coil "
        "closed: the same pattern Zara's own hand had traced, "
        "unbidden, during the very first waking intrusion the entity "
        "itself had ever risked on her, months ago, back when it was "
        "still teaching itself how much a human mind could survive "
        "being asked to carry."
    )},
    {"type": "body", "text": (
        "It did not know whether the presence had chosen that "
        "particular shape deliberately, echoing the entity's own "
        "earlier work as a kind of message, or whether the spiral was "
        "simply the shape any patient, careful power reached for first "
        "when testing how far a borrowed hand could be trusted to "
        "move. Either answer troubled it. The first meant the presence "
        "wanted the entity to notice and understand exactly what was "
        "being repeated. The second meant that some part of what the "
        "entity had believed original in its own methods was, in "
        "truth, simply the oldest and most obvious approach any "
        "sufficiently old power would eventually arrive at."
    )},
    {"type": "body", "text": (
        "It thought, unwillingly, of Nkiruka's old warning read into "
        "the record at Udo, that the presence itself was never the "
        "true danger in any prior account, only what it shaped the "
        "claimed children into. The entity had assumed, hearing that "
        "warning secondhand through the boy's own dawning questions "
        "weeks ago, that the warning was aimed at itself. It "
        "considered now, watching a second power draw the same "
        "careful spiral through a borrowed hand, that the warning "
        "might never have distinguished between the two of them at "
        "all, and that whatever pattern the old records described "
        "might already be repeating itself with both of them cast in "
        "roles neither had chosen and neither fully understood yet."
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "The boy found him still watching long after the spiral in "
        "Amara's yard had gone still, and asked, with the plain, "
        "unshielded directness that had become the only way he ever "
        "asked anything that actually mattered to him, whether Zara "
        "was in danger."
    )},
    {"type": "body", "text": (
        "The entity considered the question with more care than it "
        "had given almost any other question this season, aware that "
        "whatever honesty it offered now would become the standard the "
        "boy expected from every answer after it. \"I do not know yet,\" "
        "it said. \"What is happening to her does not feel like the "
        "beginning of harm. It feels like the beginning of a lesson, "
        "the way I once taught you shapes and patterns before you "
        "could ask what they were for. I do not yet know what she is "
        "being taught, or why.\""
    )},
    {"type": "body", "text": (
        "\"Will you stop it,\" the boy asked, \"if it turns out to be "
        "harm after all.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "The cold voice weighed the question in its ledger before any "
        "answer came."
    )},
    {"type": "system", "text": "Vessel: direct question regarding entity's obligation toward third party human. No established protocol. Response requires genuine commitment rather than deflection."},
    {"type": "body", "text": (
        "The entity searched itself honestly before answering, aware "
        "that a careless yes would be a promise it might not be able "
        "to keep against something it had already learned it could "
        "not simply overpower, and that a careless no would teach the "
        "boy something about the entity's priorities it did not want "
        "him learning from a rushed, defensive answer. \"I will try,\" "
        "it said at last. \"I cannot promise I will succeed. Whatever "
        "is holding her hand right now has already proven it is more "
        "patient than I am, and patience is the one advantage I have "
        "never once had to test against something older than myself. "
        "But I will try, because you asked me to, and because she "
        "held you first, and some debts do not stop mattering just "
        "because the ones who owe them stopped counting.\""
    )},
    {"type": "body", "text": (
        "The boy accepted this the way he accepted every answer that "
        "cost the entity something real to give, filing it away beside "
        "everything else he was learning to weigh for himself, though "
        "he did not go back to his stones immediately the way he "
        "usually did once a hard question had been answered. He sat "
        "with the entity a while longer instead, quiet in a way that "
        "felt more like keeping company than needing anything further."
    )},
    {"type": "body", "text": (
        "\"You said some debts do not stop mattering,\" he said "
        "eventually. \"Does that mean I have debts too. People I owe "
        "something to, even ones I have never met.\""
    )},
    {"type": "body", "text": (
        "The entity turned the question over longer than the boy "
        "likely expected, aware that whatever it answered now would "
        "shape how he weighed every stranger he ever met afterward. "
        "\"Yes,\" it said finally. \"Your mother, for carrying you. "
        "Zara, for catching you. Even Kene, in a smaller way, for "
        "growing up carrying a little of what should have belonged to "
        "you both equally. Debts like that do not need to be paid all "
        "at once, or even paid the same way they were given. But "
        "pretending they do not exist has never once made a person "
        "lighter. It only makes the eventual reckoning heavier.\""
    )},
    {"type": "body", "text": (
        "The boy considered this with the same unhurried seriousness "
        "he gave every idea large enough to require turning over more "
        "than once, and the entity turned its own attention back "
        "toward Amara's yard, where the wind had already begun to "
        "blur the spiral's careful edges, wondering how many more "
        "patient, gentle lessons the presence intended to teach before "
        "it finally explained what any of them were actually for."
    )},

    {"type": "scene_break", "text": ""},
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
    print("  THE DARK RISE — Episode 43: \"A Different Hand\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_43.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_43.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
