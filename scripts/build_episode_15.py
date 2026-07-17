#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 15: "The Message"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-22: Episode 15 escalates the entity's contact with Zara from
a private, internal voice to full vocal possession, mirroring how it once
spoke through the dibia in Episode 4 but choosing, this time, to speak in
front of both Amara and Obi at once rather than to Amara alone. The message
it delivers is deliberately unsettling on two fronts: it reveals, for the
first time to anyone but Amara, that it knows about the weight Elder Maka
secretly carries from the binding rite, and it signals that the vessel in
Oso is nearing a readiness it has not named plainly before. In Oso, the
entity's reasoning is shown to be calculated rather than impulsive, a
controlled widening of its audience meant to test how much pressure Amara
can bear before she breaks in one direction or another. The episode closes
with Amara reeling from the knowledge that the entity now holds Elder
Maka's secret as a card it can play whenever it chooses.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_15.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifteen"},
    {"type": "title_ep_name", "text": "The Message"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT ZARA FELT COMING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three evenings after the voice first spoke inside her, Zara "
        "learned to recognize the pressure that came before it, a "
        "tightening behind her own eyes like the air going still before "
        "a storm breaks, and she had just enough warning that evening "
        "to set down the bowl in her hands before her own throat stopped "
        "answering to her."
    )},
    {"type": "body", "text": (
        "\"Amara,\" she managed to say, and then could not say anything "
        "else in her own voice at all."
    )},
    {"type": "body", "text": (
        "It had come twice more since that first night at the edge of "
        "the yard, always the same quiet arrival inside her own "
        "thoughts, always careful, almost courteous, the way a visitor "
        "who intends to stay a long while is careful not to frighten the "
        "household on the first evening. She had told Amara each time, "
        "the way she had promised to, and each time the two of them had "
        "sat afterward turning the words over for whatever use they "
        "might hold. Neither of them had expected the voice to want a "
        "larger room than the inside of Zara's own skull."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi was there that evening too, mending a net in the last of "
        "the daylight, and both of them turned at the strangled sound of "
        "Zara's name catching in her own mouth. They watched her "
        "shoulders go rigid, her chin lift at an angle no tired woman "
        "lifts her own chin, and when she spoke again the words came out "
        "in her own voice but shaped by a rhythm that had never once "
        "belonged to her, slower, older, each word set down like a stone "
        "placed with care rather than spoken in a hurry."
    )},
    {"type": "body", "text": (
        "\"Amara,\" the voice said, using Zara's mouth the way a hand "
        "uses a glove. \"You have grown careful. Careful is not the "
        "same as safe. I have let you believe otherwise for longer than "
        "I needed to.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi rose halfway to his feet, the net forgotten, one hand "
        "moving instinctively toward Zara as though he could pull her "
        "back out of her own body by the shoulder. Amara caught his arm "
        "and held it. \"Do not touch her,\" she said, low and urgent. "
        "\"We do not know what that would do to either of them.\""
    )},
    {"type": "body", "text": (
        "\"Wise,\" the voice agreed, and something that was not quite a "
        "smile moved across Zara's borrowed face. \"You have learned "
        "more caution in a month than most mothers learn in a lifetime. "
        "It is why I have chosen to speak through her tonight, and not "
        "simply into her, the way I have on other nights. A whisper "
        "convinces one woman. A voice convinces a household.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHY IT CHOSE TWO WITNESSES INSTEAD OF ONE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity held the small, controlled "
        "portion of itself that spoke through the midwife with the same "
        "steady attention it gave every working it had ever spun out "
        "across this village, watching the reaction it produced the way "
        "a fisherman watches the first give of a line."
    )},
    {"type": "body", "text": (
        "Speaking to Amara alone, through the dibia, had won it "
        "information and little else. She had absorbed the words, "
        "weighed them, and kept her own counsel, exactly as a woman who "
        "trusted no one but herself would be expected to do. A message "
        "delivered in front of a second witness could not be quietly "
        "filed away and reconsidered alone in the dark. It would need to "
        "be discussed, argued over, carried between two people who did "
        "not always agree on how much danger was too much danger to "
        "risk."
    )},
    {"type": "body", "text": (
        "That friction was worth more to the entity than any single "
        "fact it could have delivered in private. A household arguing "
        "with itself over how to answer a threat was a household too "
        "occupied to notice everything else moving quietly around it."
    )},
    {"type": "body", "text": (
        "There was a risk in it too, and the entity did not pretend "
        "otherwise to itself. A second witness meant a second memory of "
        "exactly how the voice had sounded, a second account that could "
        "be carried to the old woman, or worse, to the council, and "
        "compared against whatever the dibia's silenced testimony might "
        "someday manage to add to it. The entity weighed that risk "
        "against the value of the friction it would buy and judged the "
        "trade worth making. It had made harder trades than this one "
        "and survived every single one of them for three centuries."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "It had also, carefully, chosen exactly what to reveal and what "
        "to withhold. The old woman's secret was worth more unspent than "
        "spent, a card the entity intended to hold rather than throw "
        "down all at once. Tonight it would only prove that the card "
        "existed. Amara would spend the rest of the night imagining "
        "every way it might be played, which was, in its own way, a far "
        "more effective use of the fact than playing it outright ever "
        "could have been."
    )},
    {"type": "body", "text": (
        "In the hollow, the vessel had begun repeating a single sound "
        "over and over, an early, imperfect shape of a word, and the "
        "entity let a thin thread of its attention rest there even while "
        "the greater part of it spoke through borrowed lips a mile away. "
        "Soon, it thought, in the same unhurried register it thought "
        "everything in. Not yet, but close enough now to begin letting "
        "the village feel the shape of soon arriving."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In Oso, the ledger voice took stock of what the day had "
        "bought."
    )},
    {"type": "system", "text": "Vocal possession: full, multi witness. Strategic disclosure: partial. Third thread leverage held in reserve. Vessel: early vocalization, repeating single syllable."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT THE VOICE CHOSE TO SAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"You sealed one door,\" the voice continued, Zara's borrowed "
        "mouth shaping words with none of the midwife's own warmth left "
        "in them. \"You should be proud. It was cleverly done, and "
        "cost the old woman more than either of you understands yet.\""
    )},
    {"type": "body", "text": (
        "Amara went very still. \"What do you mean, cost her.\""
    )},
    {"type": "body", "text": (
        "\"I mean that a thread cut loose from a child too young to "
        "carry the whole of it must come to rest somewhere,\" the voice "
        "said. \"She chose to be that somewhere. She has not told you. "
        "She has not told her daughter. She sits alone every night now, "
        "counting the hours she cannot account for, and calls it the "
        "cost of age. You, of all the people in this village, should "
        "recognize that particular shape of lie. You have worn it "
        "yourself.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi looked between his wife and the possessed woman standing "
        "in their yard, confusion and dawning horror moving across his "
        "face in equal measure. \"What is it talking about,\" he said. "
        "\"Amara. What does it mean.\""
    )},
    {"type": "body", "text": (
        "Amara did not answer him. She could not, not yet, not with the "
        "voice still watching her through Zara's borrowed eyes, patient "
        "and pleased with itself in a way that made her want to be sick. "
        "It had just handed her, in front of her own husband, "
        "confirmation of the very thing she had been carrying alone "
        "since the binding rite, and stripped away, in the same breath, "
        "any comfortable illusion that the knowledge was hers to control "
        "the timing of."
    )},
    {"type": "body", "text": (
        "\"Why tell us this,\" Amara said instead, her voice steadier "
        "than she felt. \"What do you gain from it.\""
    )},
    {"type": "body", "text": (
        "\"Nothing, tonight,\" the voice said. \"Tonight I only wanted "
        "you to know that I see further into this village than the "
        "walls you have built around your own fear. Soon there will be "
        "a choice in front of you that matters far more than one old "
        "woman's secret. When it comes, remember that I told you the "
        "truth first, even when the truth cost me nothing to withhold.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Zara's body sagged all at once, the borrowed rhythm draining "
        "out of her the way water drains from an overturned jar, and she "
        "caught herself against the compound wall with both hands, "
        "gasping, herself again and utterly spent by whatever the "
        "speaking had cost her to carry."
    )},
    {"type": "body", "text": (
        "Obi turned to his wife the instant Zara's own voice returned to "
        "her, and this time he would not be put off. \"Amara. Tell me "
        "what it meant. Now.\""
    )},
    {"type": "body", "text": (
        "Amara looked at him, and then at Zara, shaking and pale against "
        "the wall, and understood that the last private thing she had "
        "been carrying alone had just been taken out of her hands "
        "entirely, by the one voice in Idoro with no reason at all to "
        "keep her secrets safe."
    )},
    {"type": "body", "text": (
        "\"Elder Maka is marked too,\" she said, and the words felt like "
        "setting down a stone she had carried so long her arms had "
        "forgotten how to move without its weight. \"I saw it during "
        "the rite. I did not tell you. I did not tell anyone. And now "
        "the only other person who knows for certain is the thing that "
        "put it there.\""
    )},
    {"type": "body", "text": (
        "Obi said nothing for a long moment, absorbing this final weight "
        "the way he had absorbed every weight before it since the truth "
        "first found him, and when he finally spoke his voice was quiet "
        "in a way Amara had not heard from him since the night he "
        "confessed his own broken promise. \"How many more of these are "
        "you carrying alone,\" he asked. \"How many more nights have you "
        "decided, on your own, what I am strong enough to be told.\""
    )},
    {"type": "body", "text": (
        "\"As many as it took to keep all of us alive one more day,\" "
        "Amara said, and found, to her own surprise, that she had no "
        "apology left in her for it, only a tiredness so complete it "
        "felt almost like peace. \"I will not apologize for the "
        "carrying. I will only tell you, now, everything I know, and "
        "let you decide what to do with the weight of it same as I have "
        "had to.\""
    )},
    {"type": "body", "text": (
        "Zara, still leaning against the compound wall and only half "
        "recovered, looked at the two of them and understood, better "
        "than either of them yet did, that the voice had not only "
        "delivered a message that night. It had tested exactly how much "
        "truth this household could survive at once, and left before "
        "anyone could tell whether it had found the breaking point or "
        "only come close to it."
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
    print("  THE DARK RISE — Episode 15: \"The Message\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_15.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_15.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
