#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 101: "What She Is Worth"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-16 (scheduled release 2026-10-16): the villain-side
hostage-clock episode. With Emenike exposed, the Warden cancels the
bracelet proof runs — proof of Ijeoma's life no longer purchases
anything — and weighs, in pure ledger terms, whether the House should
keep feeding a hostage who is now only a witness. The Factor, stripped
of the operation but still holding the commerce ledgers, passes the
guarded courtyard for the first time and begins, quietly, to crack.
Ijeoma herself, introduced properly for the first time, deduces from
the overdue taking exactly what it means and stops waiting. Four days
west, the search party finds a toppled boundary stone carved with a
spiral, laid face down the way you lay down the dead; that night
Chibundu dreams the stone standing, and the presence confirms its
people cut it — the lost ground lies two days ahead of the search.
The episode closes cold: the Warden writes one ciphered question to
Mfoniso — does the hunt still require the guest kept breathing, or
may the House close the account.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_101.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and One"},
    {"type": "title_ep_name", "text": "What She Is Worth"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════
    # ACT ONE: THE LINE IN THE LEDGER
    # ═══════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Far downriver from Idoro, where the delta widened into brackish "
        "water, there was a trading post built to look like warehouses and "
        "a modest dock. Past its loading floors, past three doors no tax "
        "collector had ever been invited through, a lamp burned in a room "
        "lined with ledgers. The Warden sat beneath it, working through "
        "the season's accounts. Rain moved on the roof with a sound like "
        "grain poured slowly from hand to hand. She turned the pages the "
        "way she did everything, without hurry and without mercy. Then one "
        "line stopped her."
    )},
    {"type": "body", "text": (
        "The entry was written in a clerk's careful hand. Keeping of the "
        "guest. Six guards in rotation. A cook. A walled courtyard that "
        "produced nothing and earned nothing. The House had paid that cost "
        "every month for two seasons, and every month the payment had "
        "bought the same thing. A young woman's heartbeat, held in reserve "
        "against her brother's obedience. The Warden set a small brass "
        "weight on the page so it would not turn, and sent for the Factor."
    )},
    {"type": "body", "text": (
        "He came correctly, and he came cold. Since the night she had "
        "taken the operation out of his hands, the Factor gave her exactly "
        "what duty required and not one word more. He stood before the "
        "desk like a man visiting a grave he had not chosen. \"You sent "
        "for me.\" \"The guest,\" the Warden said. \"Her keeping still "
        "sits in your ledgers. Commerce, not operation. I want the line "
        "moved to mine.\" \"Then move it,\" he said. \"You did not need "
        "me standing here to watch you write.\""
    )},
    {"type": "body", "text": (
        "\"I needed you here because there are things I would rather you "
        "heard plainly,\" she said. \"The proof runs are ended. There "
        "will be no more takings of the bracelet. No more journeys to that "
        "stone.\" The Factor did not move. \"The girl's brother has been "
        "discovered. You know this. Proof of her life was a tool for "
        "persuading him, and there is no one left to persuade. From "
        "tonight the House will not spend a single day of any man's "
        "travel pretending otherwise.\""
    )},
    {"type": "body", "text": (
        "\"And the girl,\" the Factor said. It was not quite a question. "
        "The Warden folded her hands. \"The House keeps what it might "
        "still spend,\" she said. \"It does not keep what it can only "
        "feed. Which of those she is, I have not yet decided.\" She said "
        "it the way she would have priced a shipment of cloth, and that "
        "was the thing the Factor found he could not put down afterward. "
        "Not cruelty. Cruelty would at least have looked at what it was "
        "doing."
    )},
    {"type": "body", "text": (
        "\"She has seen faces,\" he said carefully. \"Yours among them, "
        "by now. A guest can be returned one day, with the right words, "
        "and become nothing worse than a story about a House no one can "
        "find. A body is a different kind of entry. Bodies do not close "
        "accounts. They open them.\" \"I know what bodies do,\" the "
        "Warden said. \"I have not moved the line yet. That is all the "
        "assurance you should read into this evening.\""
    )},
    {"type": "body", "text": (
        "She dismissed him through the inner grounds, because the rain "
        "had flooded the outer walk. That was how the Factor came to "
        "pass, for the first time, within sight of the guarded courtyard. "
        "He saw a young woman sitting very straight in the wet dusk with "
        "her back against the far wall, watching the sky the way "
        "prisoners watch anything that cannot be taken from them. He had "
        "signed the cost of her keeping every season for two seasons. He "
        "understood, standing in the rain, that he had signed it without "
        "once reading the line as a person. The Factor walked on. But he "
        "walked slower."
    )},

    # ═══════════════════════════════════════════════════════════════════════
    # ACT TWO: THE FIFTH TAKING
    # ═══════════════════════════════════════════════════════════════════════

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the courtyard, Ijeoma was counting. She counted everything. "
        "It was how a cloth trader's daughter was raised. Count the "
        "bolts, count the cowries, count the knots in a stranger's smile "
        "before you trust it. She was nineteen years old, small like her "
        "mother and quick handed like her mother, and she had spent two "
        "seasons learning this courtyard until she could walk it blind. "
        "Six guards, in three watches of two. A cook who hummed when the "
        "food was short and was silent when it was not. Forty one paces "
        "of wall."
    )},
    {"type": "body", "text": (
        "Above her left wrist she wore a plaited bracelet of blue thread. "
        "Her mother had woven it when Ijeoma was a child too small to "
        "keep still, and she had worn it so long that the color lived now "
        "mostly in the deep places of the plait. Twice each season since "
        "her taking, a courier had untied it and carried it away, and "
        "weeks later it had come back to her smelling of river mud and "
        "other people's hands. She hated the taking more than she hated "
        "the walls. And she lived for it. While the bracelet traveled, "
        "one thing was still true. Somewhere upriver, her brother was "
        "alive, and worth persuading."
    )},
    {"type": "body", "text": (
        "The fifth taking was late. Not a market day late. A full turning "
        "of the moon late, by her count, and her count was never wrong. "
        "She had asked no one. Asking teaches your keepers exactly which "
        "door to close on you, and she had not survived two seasons in "
        "this courtyard by handing anyone a map of her fears. She sat "
        "with her back against the wall, turned the bracelet slowly on "
        "her wrist, and worked the problem the way a weaver works a knot. "
        "Not by pulling. By understanding."
    )},
    {"type": "body", "text": (
        "If they no longer sent proof of her life, then proof of her life "
        "no longer purchased anything. There were only two ways that "
        "became true. Either Emenike had been caught. Or Emenike was "
        "dead. Her hands went still on the bracelet. She made herself "
        "finish the thought, because the thought did not care whether she "
        "finished it. Either way, the House was no longer keeping a "
        "lever. It was keeping a witness. And nobody feeds a witness "
        "forever."
    )},
    {"type": "body", "text": (
        "The evening guard change came. She watched it without seeming to "
        "watch, the way she had watched it for two seasons, and for the "
        "first time she watched it differently. Which man checked the "
        "gate bar with his hands, and which man only looked at it. Which "
        "watch ended in full darkness. Where the cook set the water jars "
        "at night, and how far that was from the wall's one bad corner, "
        "where forty years of rain had rounded the top course of mud "
        "brick like an old tooth. Ijeoma turned the bracelet on her wrist "
        "one last time, the way her mother tied off a finished thread. "
        "She was done waiting to learn her worth from other people's "
        "ledgers."
    )},

    # ═══════════════════════════════════════════════════════════════════════
    # ACT THREE: THE STONE THAT LIES ON ITS FACE
    # ═══════════════════════════════════════════════════════════════════════

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Four days west of Idoro, the search party walked out of the last "
        "country that had a name. Osadebe kept them to a soldier's pace, "
        "steady and unheroic, and sketched each evening by firelight "
        "where Ubani's borrowed maps ended and his own began. The land "
        "had been changing under them all day. Ifeanyi said it first, "
        "because Ifeanyi had grown up hunting. The game trails bent. Not "
        "around water. Not around rock. Around nothing at all. Wide, "
        "respectful curves through open ground, as if every animal for a "
        "hundred years had agreed there was something in the middle of "
        "this country not worth crossing."
    )},
    {"type": "body", "text": (
        "Okonjo found the stone an hour before dusk. He nearly walked "
        "past it, one more gray shape half swallowed by grass, and then "
        "he saw that the shape was too regular for the country around it, "
        "and called the others. It lay face down, waist high if it had "
        "ever stood, its edges worked by tools and softened by centuries. "
        "It took two of them with a spear haft to lever it over. Cut deep "
        "into the old gray face beneath, filled with earth and still "
        "unmistakable, was a spiral."
    )},
    {"type": "body", "text": (
        "Emenike crouched close but touched nothing. He had seen enough, "
        "these last two seasons, to know that some marks are letters in a "
        "language where reading aloud is not free. Osadebe copied the "
        "spiral onto his evening map, exactly, curve for curve. Then he "
        "studied the stone itself for a long while. \"Stones fall,\" he "
        "said at last. \"When they fall, they fall onto their sides. "
        "This one is lying on its face, with its mark pressed into the "
        "earth.\" He looked along the line the stone must once have "
        "faced, west and slightly south, to where the grass ran out of "
        "names entirely. \"It did not fall. It was laid down. The way "
        "you lay down the dead.\""
    )},
    {"type": "body", "text": (
        "They made camp within sight of it, because no one wanted to say "
        "aloud that camping out of sight of it felt worse. Osadebe took "
        "the first watch himself and added one line beneath his sketch, "
        "for the report he owed Udo if any of them came home to deliver "
        "reports. A boundary stone marks the beginning of something, he "
        "wrote. Someone wanted this one to forget what."
    )},
    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "That night, in Oso, Chibundu dreamed the stone standing up. It "
        "stood in the dream as it must once have stood, newly cut, the "
        "spiral sharp and filled with red ochre, and beyond it the land "
        "was not empty at all. There was a hedge of living green, and "
        "smoke rising from cooking fires, and the sound of unseen people "
        "laughing somewhere behind the leaves, ordinary as water. Then "
        "the dream ended. Not the way dreams end. The way a story ends "
        "when the one telling it cannot make themselves go on."
    )},
    {"type": "body", "text": (
        "He woke in the dark among the iroko's roots with his heart "
        "loud, and the presence was already there, wrapped around the "
        "edges of him, trembling like a struck drum skin."
    )},
    {"type": "body", "text": (
        "Through the bond, the cold exact voice spoke what the dream "
        "had shown."
    )},
    {"type": "system", "text": "The bond reports: boundary mark found and recognized. The lost ground is lost no longer. It lies two days ahead of the search."},
    {"type": "body", "text": (
        "\"My people cut that stone,\" the presence said, and its voice "
        "was not like itself. \"It was the easternmost mark of my "
        "ground. Children used to race each other out to it, slap the "
        "spiral, and race home before their mothers noticed they were "
        "gone.\" Chibundu held very still, the way you hold still for a "
        "wounded thing. \"And it is lying on its face,\" he said. "
        "\"Yes.\" \"Why.\" The presence was silent for a long moment. "
        "\"Because that is what the ones who hunt us do when they take a "
        "ground,\" it said. \"They lay its marks face down, so the land "
        "forgets its own name. So that even if a guardian's people ever "
        "came searching, nothing would be left standing that knew them.\""
    )},
    {"type": "body", "text": (
        "From deeper in Oso, the entity spoke, quiet as roots moving. "
        "\"Two days,\" it said. \"Then the searchers will stand on "
        "what is left of you, old friend, and all three of us will learn "
        "what three centuries did to it.\" Chibundu pressed his palm "
        "flat against the cold earth, and did not promise the presence "
        "that what they found would be bearable, because it had asked "
        "him once already to stop protecting it from the truth."
    )},
    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Far downriver, in the room lined with ledgers, the Warden had "
        "not gone to bed either. She wrote a single message in the "
        "House's oldest cipher and sealed it for the fastest courier "
        "line the House owned, the one whose existence was itself a "
        "secret worth killing for. It was addressed to the hunter. It "
        "asked one question. Does the hunt still require the guest kept "
        "breathing, or may the House close the account?"
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
    print("  THE DARK RISE — Episode 101: \"What She Is Worth\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_101.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_101.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
