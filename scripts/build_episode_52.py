#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 52: "The Circle of Trust"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-28: Episode 52 follows the morning after the ambush,
as Osadebe and Chidebe work through the five people who knew the
reunion's exact hour. Rather than let suspicion fall on Amara, Obi, or
Zara, the episode clears each of them in turn through simple, grounded
trust, then turns Chidebe's attention to his own garrison. He finds a
recently recruited soldier, Effiong, who has been quietly selling
routine patrol schedules to a middleman for coin, never knowing what
his small corruption enabled. The reveal is deliberately smaller and
more human than a grand betrayal: an ordinary bribe, not a spy planted
for this purpose. But the episode closes on the harder second question
the confession raises: the middleman Effiong sold his reports to was
never a stranger passing through. He is a trader Idoro has known and
sold to for years.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_52.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Two"},
    {"type": "title_ep_name", "text": "The Circle of Trust"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: FIVE NAMES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe had not slept, and it showed plainly in the careful, "
        "deliberate way he laid the problem out on Amara's own table "
        "the next morning, as though setting it down gently might keep "
        "it from cutting whoever picked it up next. \"Five people knew "
        "the hour,\" he said. \"I intend to account for all five before "
        "I write a single word to Udo, and I would rather do it here, "
        "plainly, than let it curdle into something worse left "
        "unspoken.\""
    )},
    {"type": "body", "text": (
        "\"Then start with me,\" Amara said, without hesitation, \"and "
        "finish quickly, so we can spend the rest of the morning on "
        "someone who actually deserves the suspicion.\" She meant it as "
        "something close to humor, though little of the night before had "
        "left room for real lightness in her yet, and Osadebe allowed "
        "himself the smallest answering measure of it before shaking his "
        "head."
    )},
    {"type": "body", "text": (
        "\"You walked into that field with your own son standing "
        "between you and five armed men,\" he said. \"No one who "
        "arranged that ambush would have built it around risking the "
        "very person they were sent to take. You are cleared before I "
        "have even finished saying so, and so is Obi, who I am reliably "
        "told ran toward the danger rather than away from any part of "
        "it.\""
    )},
    {"type": "body", "text": (
        "Obi, leaning in the doorway with Kene balanced on one hip, "
        "accepted the clearing with a short, humorless nod. \"That "
        "leaves Zara,\" he said, \"and I will not pretend I have not "
        "already turned that thought over more than once since sunrise, "
        "given everything her own hands have carried without her "
        "knowing it these past months.\""
    )},
    {"type": "body", "text": (
        "It was Amara who answered that one, quiet and certain. \"Zara "
        "has been walked by something she cannot control since before "
        "any of this began, and none of it has ever once served the "
        "trading House's purposes. Whatever reaches her reaches for its "
        "own reasons, older and stranger than a bribe. I do not believe "
        "it sold her silence to the highest House willing to pay for "
        "it, and I do not believe you believe that either, once you say "
        "it aloud.\" Obi considered this, and did not argue further."
    )},
    {"type": "body", "text": (
        "Zara herself had been standing at the edge of the compound "
        "long enough to hear most of it, and stepped forward now rather "
        "than let the conversation continue to circle around her "
        "without her voice in it. \"I have asked myself the same "
        "question every hour since I woke this morning,\" she said. "
        "\"Whether some part of me sold what I did not know I was "
        "carrying. I do not have a clean answer to offer you, only that "
        "whatever moves through me has never once asked my leave, and "
        "has never once, in all the ways it has used me, asked for a "
        "House's coin in return.\""
    )},
    {"type": "body", "text": (
        "\"That is enough for me,\" Amara said, and meant it plainly "
        "enough that no one else in the room found reason to argue the "
        "point further. Osadebe made a small mark in the private "
        "accounting he was keeping and moved on, grateful, in a "
        "morning that had offered him little else to be grateful for, "
        "that at least this part of the reckoning had cost no one "
        "their trust in each other."
    )},
    {"type": "body", "text": (
        "That left two names, and Osadebe said the harder of them "
        "himself, sparing Chidebe the discomfort of naming his own "
        "possible failure aloud first. \"Which leaves you and me, "
        "Captain. I trust my own conduct, though I understand that "
        "trust means little to anyone standing outside my own skin. "
        "What I cannot yet vouch for is every man serving under your "
        "banner, several of whom knew a patrol was being pulled back "
        "for two hours even if they were never told why.\""
    )},
    {"type": "body", "text": (
        "Chidebe's jaw tightened, not at the accusation, which he had "
        "half expected, but at the plain truth sitting underneath it. "
        "\"I gave the order myself, to men I have commanded less than a "
        "season,\" he said. \"I told myself a soldier who does not ask "
        "why can be trusted precisely because he does not ask. I did "
        "not consider, until this exact moment, that a soldier who does "
        "not ask why is also a soldier who can be bought without ever "
        "once needing to understand what he is selling.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A SMALL, ORDINARY CORRUPTION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe found what he was looking for by the middle of the "
        "afternoon, not through any clever design but through the "
        "oldest and least dignified method available to him: he asked "
        "which of his men had lately seemed to have more coin than a "
        "garrison wage could easily explain. One name surfaced twice, "
        "from two separate soldiers who had noticed and said nothing "
        "out of simple discomfort rather than loyalty. Effiong, one of "
        "the youngest men in the garrison, barely three months in "
        "Chidebe's service before the posting to Idoro."
    )},
    {"type": "body", "text": (
        "He did not deny it once Chidebe sat him down alone, which "
        "told Chidebe almost as much as the confession itself. \"I "
        "never sold anything I understood the weight of,\" Effiong "
        "said, his voice thin with the particular fear of a young man "
        "watching a mistake reveal itself as something far larger than "
        "he ever let himself believe it was. \"A trader offered coin "
        "for ordinary things. When the patrol walked. When it did not. "
        "I told myself it was no different than gossip sold at a "
        "market stall.\""
    )},
    {"type": "body", "text": (
        "\"You told a stranger for coin when thirty armed men would or "
        "would not be watching a boundary that has killed people who "
        "crossed it uninvited,\" Chidebe said, keeping his voice level "
        "through an anger that wanted very badly to be louder than "
        "this conversation could afford. \"There is a great deal of "
        "distance between that and gossip at a market stall, and I "
        "think some part of you already knew it, even if you would not "
        "let yourself look at it directly.\""
    )},
    {"type": "body", "text": (
        "Effiong did not argue the point. \"I did not know why he "
        "wanted it,\" he said instead, which was, Chidebe understood, "
        "probably true and beside the point in equal measure. \"Two "
        "days ago he asked only one thing more than usual. Not "
        "patterns this time. A single hour, the exact hour the next "
        "stand down would begin, and how long it would last. He paid "
        "three times what he ever had before for it. I told myself "
        "that was simply a generous week.\""
    )},
    {"type": "body", "text": (
        "\"And when I gave that exact order two days later,\" Chidebe "
        "said quietly, watching the last of the boy's composure finally "
        "give way, \"you understood, in that moment if no other, "
        "precisely what you had sold, and to whom.\" Effiong did not "
        "answer, which was itself the only answer left to give."
    )},
    {"type": "body", "text": (
        "Osadebe, called in once the confession was secured, asked the "
        "single question that mattered most to what came next. \"This "
        "trader who paid you. Describe him. Where do you meet him.\" "
        "Effiong's answer landed harder than his confession had, "
        "settling over the small hut with a weight neither officer had "
        "expected."
    )},
    {"type": "body", "text": (
        "\"He is no stranger passing through,\" Effiong said. \"He "
        "keeps a stall at Idoro's own market, has done for longer than "
        "I have worn this uniform. I assumed, because everyone here "
        "knew him, that whatever he wanted could not be dangerous. I "
        "see now that assumption was exactly what made him useful to "
        "whoever he answers to.\""
    )},
    {"type": "body", "text": (
        "Chidebe and Osadebe exchanged a long look that carried the "
        "whole shape of the harder problem now sitting in front of "
        "them. A bribed soldier, however costly his silence had proven, "
        "was a single ordinary failure, correctable with discipline and "
        "a harder vetting of every man who came after him. A trader "
        "Idoro had bought fish and cloth from for years, quietly "
        "carrying the trading House's coin the whole time, was "
        "something else entirely: proof the House's patience reached "
        "further into the village itself than anyone standing in this "
        "room had let themselves imagine."
    )},
    {"type": "body", "text": (
        "\"We will need his name,\" Osadebe said finally, \"and we will "
        "need it before he learns his own usefulness has just run out.\" "
        "He did not say the rest of the thought aloud, though both men "
        "in the hut with him understood it plainly enough: a village "
        "that had only just begun learning to trust its own soldiers "
        "and its own boundary again would now have to learn, once more, "
        "how much less safe an ordinary, familiar face could make "
        "everyone feel once it was known to belong, in part, to someone "
        "else."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: WHAT OSO ALREADY KNEW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, the entity had felt Idoro's fear shift overnight from "
        "the sharp, immediate terror of an attack into something "
        "slower and more corrosive, a village quietly wondering which "
        "familiar face across the market might belong, in some small "
        "hidden part, to someone else. It fed on the change without "
        "meaning to, the way it had always fed on ambient dread, and "
        "found no satisfaction in the meal at all."
    )},
    {"type": "body", "text": (
        "Chibundu, arranging his stones in a pattern that had grown "
        "steadily more deliberate over the last several weeks, asked "
        "the question plainly, the way he now asked most of his "
        "hardest ones. \"If they bought one soldier without him "
        "understanding what he sold, how many others has this House "
        "already bought the same way, in places none of us have "
        "thought to look yet.\""
    )},
    {"type": "body", "text": (
        "The entity considered the question longer than it usually let "
        "itself consider anything the boy asked, unwilling to offer "
        "another half true comfort now that it had spent so many "
        "episodes of their shared life trying to give him fewer of "
        "those rather than more. \"I do not know,\" it said finally. "
        "\"I only know that patience of the kind this House has shown "
        "does not spend itself on a single soldier and stop there. We "
        "should both expect to find more doors than the ones we have "
        "already counted.\""
    )},
    {"type": "body", "text": (
        "Chibundu absorbed this the way he had learned to absorb most "
        "hard truths lately, without flinching and without pretending "
        "it cost him nothing. \"Then we count the ones we can find,\" "
        "he said, \"and we watch harder for the ones we cannot, and we "
        "do not let either kind of door decide what tonight was "
        "allowed to mean.\" The entity, watching him say it, understood "
        "it was hearing its own hard won patience spoken back to it in "
        "a voice far younger than the one that had first learned it."
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
    print("  THE DARK RISE — Episode 52: \"The Circle of Trust\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_52.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_52.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
