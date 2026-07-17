#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 29: "The Investigation"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-05: Episode 29 brings Captain Osadebe into Idoro itself.
He begins with the village's remaining council, and finds, unexpectedly,
that Ozoemena, humbled by everything Episodes 25 and 26 cost him, gives
him the most honest account anyone in the village offers, along with a
pointed recommendation: speak to Amara, who has seen more of this than
anyone still living in Idoro. In Oso, the entity registers a new,
unfamiliar flavor in the village's fear, careful and investigative rather
than purely afraid, and does not yet grasp its source. The episode's
center is the long conversation between Osadebe and Amara, in which she
must decide, for the first time, how much of the full truth to hand to
an outsider who actually holds the power and resources to act on it. She
tells him enough to convince a careful man this is not simple
superstition, though she withholds the rest for now. The episode ends
with Osadebe asking to be taken to the edge of Oso himself.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_29.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Nine"},
    {"type": "title_ep_name", "text": "The Investigation"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT OZOEMENA FINALLY TOLD THE TRUTH ABOUT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe reached Idoro on the seventh day of travel, and found "
        "a village that watched his small party approach with the "
        "particular wariness of people who had learned, recently and "
        "expensively, that strangers arriving with confidence rarely "
        "left without costing someone something."
    )},
    {"type": "body", "text": (
        "He had learned, across a dozen provinces and twice as many "
        "smaller disputes, that a village's first answer to a stranger "
        "asking careful questions was almost never its truest one. The "
        "first answer was always the answer a frightened place gave to "
        "protect itself, polished smooth by however many times it had "
        "already been repeated among neighbors before an outsider ever "
        "arrived to hear it. He had come prepared to spend days peeling "
        "that answer back layer by layer."
    )},
    {"type": "body", "text": (
        "He began, as he always began, with whoever the village itself "
        "pointed him toward, and found himself, within the hour, "
        "sitting across from a broad, quiet man with a healing scar at "
        "his temple, introduced to him only as the one who had held "
        "authority here until three weeks ago."
    )},
    {"type": "body", "text": (
        "\"Tell me what happened,\" Osadebe said, the same opening he "
        "had used in a dozen villages before this one, and watched "
        "Ozoemena consider the question for a long moment before "
        "answering it in full, without a single attempt to soften his "
        "own part in it."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"I believed confidence could stand in for knowledge I did "
        "not have,\" Ozoemena said. \"It cost a man his life, and it "
        "cost me the authority I had spent two weeks fighting to keep. "
        "I am telling you this plainly because I have already learned, "
        "at the worst possible price, what happens when a man in my "
        "position tells a story softer than the truth deserves.\""
    )},
    {"type": "body", "text": (
        "Osadebe found himself genuinely surprised, an uncommon feeling "
        "after twelve years of hearing frightened men in fallen "
        "positions reach reflexively for whatever version of events "
        "cost them the least. \"Most men in your position spend their "
        "first hour with me explaining why none of it was truly their "
        "doing.\""
    )},
    {"type": "body", "text": (
        "\"Most men in my position have not yet watched a corpse strike "
        "them across the face for their own arrogance,\" Ozoemena said. "
        "\"It clarifies a man's relationship with honesty rather "
        "quickly.\""
    )},
    {"type": "body", "text": (
        "He went on, unprompted, filling in details Osadebe had not "
        "yet asked for, the borrowed rite, Elder Maka's warning ignored, "
        "the exact words the entity had spoken through the dying dibia "
        "before it struck him down. Osadebe wrote almost nothing of it "
        "on the small tablet he carried, trusting instead to the "
        "particular memory a careful investigator trains across years "
        "of interviews, the kind that holds a man's exact phrasing "
        "longer and more faithfully than ink ever could."
    )},
    {"type": "body", "text": (
        "\"You believe it spoke,\" Osadebe said. \"Not merely that the "
        "dibia's body moved strangely, or that fear shaped what the "
        "crowd believed they heard. You believe words were actually "
        "spoken, with intent behind them.\""
    )},
    {"type": "body", "text": (
        "\"I do not believe it,\" Ozoemena said. \"I watched it happen "
        "an arm's length from my own face. Belief is for things a man "
        "has not yet seen with his own eyes.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"Who in this village actually understands what you were "
        "reaching for,\" Osadebe asked."
    )},
    {"type": "body", "text": (
        "\"Amara,\" Ozoemena said, without hesitation. \"She has seen "
        "more of this, up close, than anyone left alive in Idoro. I "
        "spent two weeks refusing to believe that made her worth "
        "listening to instead of a threat worth watching. Do not make "
        "the same mistake I made. Whatever she tells you, believe it "
        "before you believe anyone else in this village, myself "
        "included.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY COULD NOT YET NAME
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity tasted a new thread moving "
        "through Idoro's fear that afternoon, unfamiliar enough that it "
        "took a long moment to place what made the flavor of it "
        "different from everything the village had produced before."
    )},
    {"type": "body", "text": (
        "This fear was not the sharp, concentrated dread of a rite "
        "gone wrong, nor the low, constant hum of a village shunning a "
        "marked household. It was careful. Measured. The particular "
        "fear of people being asked precise questions by someone who "
        "clearly intended to remember every answer, rather than the "
        "shapeless fear of people simply waiting for the next disaster "
        "to arrive."
    )},
    {"type": "body", "text": (
        "It did not yet have enough of the thread to understand its "
        "source, only enough to note that something in Idoro's texture "
        "had shifted again, a new variable added to an accounting it "
        "had believed, only days earlier, was as settled as it was "
        "ever going to get."
    )},
    {"type": "body", "text": (
        "It considered, briefly, extending a thread toward whatever "
        "was producing this new flavor of fear, the way it had once "
        "extended itself toward the dibia and toward Zara before him, "
        "and decided against it just as quickly. It had learned, "
        "across every thread it had built and every thread it had "
        "spent, that a new presence entering a village unannounced was "
        "worth understanding fully before it was worth touching at all. "
        "Better to watch this stranger's shape a while longer than to "
        "reach for him blind and discover, too late, that he had come "
        "carrying more than careful questions."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel added another small stone to his "
        "shifting arrangement, entirely undisturbed by whatever new "
        "thing was moving a mile away in the village he had once tried, "
        "and failed, to walk toward."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The ledger voice marked the new flavor of fear, curious and "
        "cold."
    )},
    {"type": "system", "text": "New fear variant detected: measured, investigative. Source unidentified. Monitoring."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT AMARA DECIDED TO TELL HIM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe found Amara in her own yard, and something in the way "
        "she watched him approach, measuring rather than fearing, told "
        "him before either of them spoke a single word that Ozoemena's "
        "recommendation had been exactly right."
    )},
    {"type": "body", "text": (
        "\"The crown sent you,\" she said, not quite a question."
    )},
    {"type": "body", "text": (
        "\"The crown sent me to learn the truth,\" Osadebe said. \"Not "
        "to decide it in advance. I have heard three different "
        "versions of what happened in this village already today, and "
        "I was told, by the man most responsible for the worst of it, "
        "that you were the only person likely to give me a fourth "
        "worth trusting.\""
    )},
    {"type": "body", "text": (
        "Amara studied him a long while, weighing the particular "
        "arithmetic she had weighed so many times these last months, "
        "how much truth a stranger deserved against how much danger the "
        "truth might invite. Something about his stillness, the same "
        "careful patience she had learned to recognize in people "
        "actually worth trusting, tipped the balance further than she "
        "expected it to."
    )},
    {"type": "body", "text": (
        "Obi came to stand beside her partway through the silence, "
        "sensing without needing to be told that this conversation "
        "belonged to a different weight class than the ones that had "
        "come before it, and Osadebe, watching them settle together, "
        "waited without pressing, the particular patience of a man who "
        "understood that the truths worth having were rarely the ones "
        "extracted by force."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She told him most of it. The twins. The abandonment forced by "
        "the old law. The presence that had claimed her second son in "
        "Oso and kept him alive, growing him far faster than any "
        "ordinary child grows, teaching him to reach into the village "
        "through blood and memory and, eventually, through willing "
        "human mouths. She told him about the dibia, about Zara, about "
        "the binding rite that had saved Kene at a cost she still did "
        "not fully understand herself. She did not tell him about Elder "
        "Maka's condition, or the exact shape of what she still "
        "privately suspected about her own son's growing will. Some "
        "truths, she had learned, were not yet hers to spend on behalf "
        "of people who had trusted her with them."
    )},
    {"type": "body", "text": (
        "She watched his face carefully as she spoke, looking for the "
        "particular flicker she had learned to expect from anyone "
        "hearing this story for the first time, the moment disbelief "
        "either hardened into dismissal or softened, reluctantly, into "
        "something closer to belief. Osadebe's face gave her very "
        "little to read either way, the trained stillness of a man who "
        "had spent twelve years learning not to let his own reaction "
        "shape a witness's next words before he had heard all of them."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Osadebe listened to the whole of it without once interrupting, "
        "the same careful stillness he had given Ozoemena, and when she "
        "finished, he sat with it a long moment before speaking again."
    )},
    {"type": "body", "text": (
        "\"I was warned, before I left Udo, not to let disbelief blind "
        "me to what was standing directly in front of me,\" he said. "
        "\"I did not expect, riding south, to need that warning quite "
        "this literally.\""
    )},
    {"type": "body", "text": (
        "\"You do not have to believe all of it today,\" Amara said. "
        "\"You only have to decide whether you believe enough of it to "
        "look further before you decide anything at all.\""
    )},
    {"type": "body", "text": (
        "\"I have decided that much already,\" Osadebe said. \"Take me "
        "to the edge of it. Whatever is out there, I did not ride seven "
        "days to write a report based only on what a village is willing "
        "to say about it from a safe distance.\""
    )},
    {"type": "body", "text": (
        "Amara felt the old, familiar tightening return to her chest, "
        "the sense of a new danger and a new possibility arriving in "
        "the same breath, indistinguishable from each other until time "
        "revealed which one it actually was. She had spent months "
        "protecting the truth of her son from a village that wanted him "
        "dead. She did not yet know what it would mean to hand the same "
        "truth, carefully measured, to a stranger who might finally have "
        "the power to do something about it."
    )},
    {"type": "body", "text": (
        "\"Tomorrow,\" she said. \"At first light. I will not walk that "
        "path in the dark for anyone, captain or not.\""
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
    print("  THE DARK RISE — Episode 29: \"The Investigation\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_29.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_29.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
