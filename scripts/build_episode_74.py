#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 74: "What Mfoniso Reports"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-19: Episode 74 follows Mfoniso to a quiet river town
two days from Idoro, where she writes her own account of the failed
attempt rather than travel all the way back to the Ijoma Concern in
person, unwilling to spend the weeks such a journey would cost while
the guardian's weakened state might still be exploitable. Her report
reaches the Warden days later and forces a reassessment: the old
accounts undersold the guardian's reach badly, and the one clean
advantage left is a mortal woman whose borrowed senses gave the whole
plan away. The Warden's answer, when it comes, does not recall
Mfoniso. It gives her a new target far easier to reach than either
old power, and a great deal more dangerous to Idoro than either of
them have yet understood.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_74.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy Four"},
    {"type": "title_ep_name", "text": "What Mfoniso Reports"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A REPORT WRITTEN WITHOUT SHAME
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso took a room above a quiet river town's trading post "
        "two days from Idoro rather than begin the long journey back "
        "to the Ijoma Concern's true headquarters, unwilling to spend "
        "weeks traveling while a weakened guardian's condition might "
        "still be worth exploiting before it fully recovered. She "
        "wrote her account the same evening, in the same small, "
        "unhurried hand the Warden had used to summon her in the "
        "first place."
    )},
    {"type": "body", "text": (
        "She did not soften the failure, having learned across thirty "
        "years that a report shaped to protect its writer's pride was "
        "a report that eventually cost someone else dearly. The "
        "guardian's reach, she wrote, extends considerably further "
        "beyond its claimed ground than any account in our keeping "
        "suggested. It intervened at a distance I would have called "
        "impossible before I watched it happen in front of me. Our "
        "oldest assumptions about its limits require correction before "
        "anyone plans against it again."
    )},
    {"type": "body", "text": (
        "She wrote, too, of the one true weakness the night had "
        "actually exposed, though it was not the weakness she had "
        "walked in expecting to find. The child was never truly "
        "unguarded, she wrote. A mortal woman living in that household "
        "carries some manner of borrowed sense that reached me before "
        "either old power did. She is the reason I was seen at all. If "
        "this House intends a second attempt, she is the piece that "
        "must be addressed first, not the guardians themselves."
    )},
    {"type": "body", "text": (
        "She set down, too, the smaller obstacles this village had "
        "already built around itself without anyone here fully "
        "realizing how effective they had become: patrols rotated on "
        "no learnable schedule, a mother who now moved through her own "
        "market like a woman who expected to be watched, a captain who "
        "shared his failures with his men rather than hide them, which "
        "made every soldier under his command harder to read than "
        "soldiers usually were. None of it, alone, would have stopped "
        "her. Together, it had cost her the element she valued most."
    )},
    {"type": "body", "text": (
        "She paused once, midway through the account, at the memory "
        "of the crying child's face after the compulsion broke, and "
        "set the pen down a moment longer than the writing strictly "
        "required. She had learned, across three decades of exactly "
        "this work, to let herself feel that pause fully rather than "
        "push past it unexamined, since a hunter who stopped feeling "
        "anything at all eventually made the kind of careless mistake "
        "that got someone killed who did not need to die. She picked "
        "the pen back up once the pause had run its course, and "
        "finished the report without letting it show in a single word "
        "she chose."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE WARDEN'S REVISED ACCOUNTING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The report reached the Warden six days later, and she read "
        "it twice through in the same windowless room where she had "
        "first sent Mfoniso north, the Factor summoned to hear its "
        "contents alongside her rather than learn them secondhand. "
        "\"She was not recalled,\" the Factor said, reading the "
        "closing lines. \"She is asking permission to remain and try "
        "again.\""
    )},
    {"type": "body", "text": (
        "\"She does not need my permission to remain,\" the Warden "
        "said. \"She has never once needed it in thirty years of this "
        "work. She is telling me, plainly, what she intends to do "
        "next, and asking only whether this House will support the "
        "shape of it.\""
    )},
    {"type": "body", "text": (
        "\"The mortal woman,\" the Factor said slowly, turning the "
        "phrase over with visible discomfort. \"You are considering "
        "authorizing a move against someone whose only crime is "
        "sensing danger faster than everyone around her.\""
    )},
    {"type": "body", "text": (
        "\"I am considering the fact that this House has already lost "
        "an entire ground to a guardian we underestimated once,\" the "
        "Warden said. \"I do not intend to lose a second one because I "
        "flinched at the one weakness our own specialist has actually "
        "confirmed works. This is not cruelty. It is precisely the "
        "kind of correction Mfoniso's report was written to demand of "
        "me.\""
    )},
    {"type": "body", "text": (
        "The Factor said nothing for a long moment, weighing an "
        "objection he was no longer certain he had the standing to "
        "make, having already watched his own earlier caution overruled "
        "once this same season. \"I will not carry this decision south "
        "quietly,\" he said finally. \"I met that woman's household "
        "myself. I watched a boy answer a partnership offer in his own "
        "voice, honestly, after refusing it once already through no "
        "choice of his own. I do not believe this House gains anything "
        "lasting by teaching people like that we are willing to reach "
        "for whoever is easiest to hurt rather than whoever actually "
        "stands in our way.\""
    )},
    {"type": "body", "text": (
        "\"Your objection is noted,\" the Warden said, not unkindly. "
        "\"It is also not new. You raised nearly this same argument "
        "before I sent Mfoniso north the first time, and I did not "
        "overrule you then because I disagreed with your conscience. "
        "I overruled you because conscience alone has never once "
        "protected a House that lost everything to a guardian it "
        "underestimated. I would rather carry your objection on my own "
        "ledger than carry a second lost ground on this House's "
        "account.\""
    )},
    {"type": "body", "text": (
        "\"You speak of that lost ground as though you watched it "
        "happen yourself,\" the Factor said, studying her more closely "
        "than he had allowed himself to in years of working beneath "
        "her. \"I have never once heard you name it plainly in all my "
        "time in this House's service.\""
    )},
    {"type": "body", "text": (
        "\"I did not watch it happen,\" the Warden said. \"I inherited "
        "the account, and the guilt, and the archive, from the woman "
        "who trained me, who inherited it in turn from someone else's "
        "failure before hers. That is the true shape of this House's "
        "old records, if you read them honestly. Not a single lesson "
        "learned once. A debt passed down, generation to generation, "
        "each keeper hoping fervently they would not be the one forced "
        "to spend it.\""
    )},
    {"type": "body", "text": (
        "The Factor absorbed that, and found, turning it over, that it "
        "changed the shape of his own objection without erasing it "
        "entirely. \"Then you are not asking me to accept cruelty "
        "lightly,\" he said. \"You are asking me to accept that this "
        "House has been afraid of this exact failure for longer than "
        "either of us has been alive, and that fear has finally "
        "decided its own price is worth paying.\""
    )},
    {"type": "body", "text": (
        "\"That is closer to the truth than I usually let anyone get,\" "
        "the Warden said. \"I do not enjoy what I am about to "
        "authorize. I have simply run out of gentler options that "
        "history has not already proven insufficient.\""
    )},
    {"type": "body", "text": (
        "\"What does support look like, then,\" he asked finally, "
        "\"if not more soldiers, and not more coin.\""
    )},
    {"type": "body", "text": (
        "\"It looks like patience spent correctly this time,\" the "
        "Warden said. \"Mfoniso does not need an army. She needs time, "
        "and she needs this House to stop assuming the boy or the "
        "powers around him are the only pieces worth watching. I will "
        "give her both. I would ask you to carry one more piece of "
        "this back with you when you return south: whatever softer "
        "approach your own conscience still wants to try, try it "
        "quickly. I do not believe Mfoniso intends to wait much longer "
        "before trying hers.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A NAME NEITHER OF THEM HAD SPOKEN YET
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Alone afterward, the Warden read the closing line of "
        "Mfoniso's report a third time, the one detail she had not "
        "shared aloud even with the Factor. The mortal woman's name, "
        "she read again, is Zara. She delivered both twins into this "
        "world with her own two hands, and has been marked by both old "
        "powers ever since for exactly that reason. She is not "
        "protected the way the children are. She is, in every sense "
        "that matters to this work, simply a woman standing too close "
        "to something ancient for her own safety."
    )},
    {"type": "body", "text": (
        "The Warden set the letter down at last, and allowed herself, "
        "for the length of a single held breath, the same private "
        "unease she had not permitted herself in thirty years of "
        "sending people out to do exactly this kind of work. She had "
        "been young once too, sent out on an assignment she had not "
        "fully understood the weight of until it was already finished, "
        "and had built her whole later career on the promise that she "
        "would never again authorize a move she was not willing to "
        "have explained back to her, plainly, by whoever it eventually "
        "cost the most."
    )},
    {"type": "body", "text": (
        "She did not know yet whether that promise still held, "
        "reading the shape of what she was about to authorize. She "
        "folded the report away with the rest of her old, dangerous "
        "archive regardless, and began composing her answer, already "
        "certain of the single word Mfoniso's own patience was waiting "
        "to hear before she moved again."
    )},
    {"type": "body", "text": (
        "She wrote it plainly, without the careful hedging she "
        "usually favored in case a letter was ever intercepted by eyes "
        "it was not meant for: proceed. Take whatever time the work "
        "requires. This House will not ask you to rush a second "
        "attempt the way haste ruined the first, and it will not ask "
        "you again whether the cost is one it is willing to bear. That "
        "question has already been answered, longer ago and by more "
        "people than either of us, and I do not intend to reopen it "
        "now simply because it has finally come due in my own "
        "lifetime, in a village neither of us had ever heard of before "
        "this year."
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
    print("  THE DARK RISE — Episode 74: \"What Mfoniso Reports\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_74.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_74.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
