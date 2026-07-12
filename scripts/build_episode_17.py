#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 17: "The Choice"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-24: Episode 17 resolves the tension set up by Episode 16's
ultimatum. Amara wrestles with whether to use her knowledge of Elder Maka's
secret condition as leverage, and chooses instead to offer it as an act of
solidarity rather than a threat, hoping shared vulnerability might soften
the ultimatum where blackmail could only harden it. Elder Maka, frightened
and exposed but not without conscience, extends Zara's deadline and offers
a gentler form of confinement, but Zara, having listened to the whole
exchange, makes her own choice: she will leave Idoro before anyone needs
to force her to. In Oso, the entity registers the shape of the coming
departure with quiet satisfaction, since a marked woman walking toward its
roots by her own choice, under the village's blessing, is exactly the
outcome it calculated was likely regardless of which option Idoro chose.
The episode closes on Zara preparing to leave within days, and the
unspoken knowledge, shared only by the reader, that she is walking
directly into what the entity has wanted from her since the day it first
found her thread.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_17.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventeen"},
    {"type": "title_ep_name", "text": "The Choice"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT AMARA DECIDED NOT TO DO
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara lay awake most of that night turning the shape of a "
        "weapon over in her mind, testing its edge the way a woman "
        "tests a blade she is not certain she is willing to use."
    )},
    {"type": "body", "text": (
        "She knew what she knew. Elder Maka carried the same mark she "
        "had just condemned Zara for carrying, and a single sentence "
        "spoken in front of the right people could unmake the old "
        "woman's authority as completely as a rite unmakes a curse. It "
        "would be so simple. Threaten to speak, and watch the "
        "ultimatum soften. She had already learned, across these last "
        "weeks, exactly how quickly fear could be turned into a lever "
        "when a person understood where to place it."
    )},
    {"type": "body", "text": (
        "She thought of the old man at the well who had asked Elder "
        "Maka whether the village meant to watch every child now. She "
        "thought of her own son sealed by a rite that had cost someone "
        "else more than anyone yet understood. She did not want to "
        "become the kind of woman who used a person's fear as a tool "
        "simply because she had finally found where the handle was."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She had watched Elder Maka wield exactly this kind of leverage "
        "for thirty and four years, certainty dressed up as duty, fear "
        "dressed up as law, and some part of her recoiled at the idea of "
        "becoming fluent in the same language simply because she had "
        "finally learned enough of it to speak it back. Power used the "
        "way Elder Maka had always used it did not stay contained to the "
        "hand that first picked it up. It spread, the way any tool "
        "spreads once a household discovers how well it works."
    )},
    {"type": "body", "text": (
        "\"If I threaten her with it, I win a smaller ultimatum for "
        "Zara and I lose whatever chance either of us has left of "
        "standing beside Elder Maka instead of against her,\" she told "
        "Obi in the dark, thinking aloud as much as speaking to him. "
        "\"If I offer it to her honestly, as a thing I understand rather "
        "than a thing I intend to use, I do not know what she will do "
        "with it. But I would rather risk her mercy than spend the rest "
        "of my life certain I had none left in me either.\""
    )},
    {"type": "body", "text": (
        "Obi was quiet for a long moment. \"You are gentler than I "
        "would be,\" he said finally. \"I am not certain that is a "
        "criticism.\""
    )},
    {"type": "body", "text": (
        "\"It may still be a mistake,\" Amara said. \"Gentleness has not "
        "kept our son safe so far. It has only ever been a chance I took "
        "and hoped would pay for itself later.\""
    )},
    {"type": "body", "text": (
        "\"Every chance you have taken has paid for itself so far,\" "
        "Obi said. \"I did not say I doubted you. I said I was not sure "
        "I could do the same thing in your place, and I wanted you to "
        "know that difference before you walked out there tomorrow "
        "believing you were the only one who understood the risk of "
        "it.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY EXPECTED EITHER WAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the human argument "
        "unfolding in Idoro the way it felt every argument now, a "
        "familiar texture of fear layered over fear, and gave it no "
        "more attention than the bookkeeping already required."
    )},
    {"type": "body", "text": (
        "It had already reasoned through every branch this particular "
        "tree of choices could grow. If the mother used her knowledge as "
        "a weapon, the old woman's authority would fracture, and a "
        "fractured authority meant a village with fewer hands steady "
        "enough to organize another rite against any of its remaining "
        "threads. If the mother offered the knowledge gently instead, "
        "the old woman might soften, might extend mercy, and mercy "
        "extended to a marked woman standing at the edge of exile bought "
        "the entity nothing but time, which it had never once been "
        "short of."
    )},
    {"type": "body", "text": (
        "Either branch fed something. It did not need to prefer one "
        "over the other, only to be patient enough to collect whichever "
        "fruit grew from the branch the humans chose to climb."
    )},
    {"type": "body", "text": (
        "There was a particular satisfaction, if satisfaction was even "
        "the right word for anything it felt, in watching a village "
        "solve its own fear so thoroughly on the entity's behalf. Idoro "
        "believed it was choosing between mercy and law, between "
        "compassion and duty, weighing each choice as though the weight "
        "of it belonged entirely to human hands. It had not yet "
        "occurred to a single person walking that argument that every "
        "path they considered led, sooner or later, back toward the "
        "same patient roots waiting to receive whoever walked far enough "
        "down it."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel repeated his two joined syllables "
        "again and again, an unbroken small chant the entity let "
        "continue undisturbed, watching the shape of an actual name "
        "trying to assemble itself out of sounds that had not existed "
        "in this body a month earlier. Soon there would be a true word. "
        "After the word, a sentence. After the sentence, a boy old "
        "enough in body, if not yet in years, to walk further than these "
        "roots had ever needed to carry him."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "HUMAN NEGOTIATION: OUTCOME NEUTRAL TO ENTITY INTEREST. VESSEL: REPEATED TWO SYLLABLE UTTERANCE, EARLY NAME FORMATION LIKELY."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ZARA CHOSE FOR HERSELF
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara found Elder Maka alone at her own compound wall the next "
        "morning, facing the low fields the way she had likely faced "
        "them every morning since her own missing time began, and said "
        "what she had come to say before her nerve could talk her out of "
        "it."
    )},
    {"type": "body", "text": (
        "\"I know what you carry,\" Amara said. \"I saw it during the "
        "rite. I have told no one but Obi, and I did not come here to "
        "threaten you with it. I came because I think you are the only "
        "other person in Idoro who understands exactly what Zara is "
        "afraid of right now, and I do not think that understanding "
        "should only exist in you as a secret.\""
    )},
    {"type": "body", "text": (
        "Elder Maka went very still, the particular stillness of a "
        "woman who has just felt a blade rest lightly against her own "
        "throat and is deciding whether the hand holding it intends to "
        "cut. \"You could destroy me with that,\" she said finally."
    )},
    {"type": "body", "text": (
        "\"I could,\" Amara said. \"I am choosing not to. Not because I "
        "owe you gentleness. Because I watched you offer Kene a rite "
        "instead of a grave, and I think the woman who did that is "
        "still in here somewhere, even now, even afraid.\""
    )},
    {"type": "body", "text": (
        "\"You do not know what this costs,\" Elder Maka said, and for "
        "the first time since Amara had known her, her voice cracked "
        "slightly around the edge of the sentence. \"Losing time I "
        "cannot account for. Wondering, every morning, what I did in the "
        "hours I cannot remember. Wondering whether the woman who raised "
        "a daughter and buried a son and buried a husband is still the "
        "same woman who wakes up inside this body each day, or whether "
        "something is quietly replacing her one lost afternoon at a "
        "time.\""
    )},
    {"type": "body", "text": (
        "\"I know exactly what it costs,\" Amara said quietly. \"I have "
        "watched Zara carry it for weeks. That is why I came to you "
        "instead of past you.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka was quiet for a long time, staring out at the "
        "fields, and when she finally spoke her voice had lost some of "
        "the hardness Amara had grown so used to hearing in it. \"I do "
        "not know how to be merciful to her without risking that mercy "
        "being asked of me twice more before the season turns. Every "
        "door I leave open is a door something else can walk through "
        "after me.\""
    )},
    {"type": "body", "text": (
        "\"Then let her choose her own door,\" Amara said. \"Give her "
        "time enough to decide for herself what she is willing to risk, "
        "instead of deciding it for her out of fear of what you carry "
        "and cannot say aloud.\""
    )},
    {"type": "body", "text": (
        "Elder Maka nodded slowly, something in her shoulders loosening "
        "that had been rigid since the ultimatum first left her mouth. "
        "\"She may have until the rains come, instead of the next moon. "
        "That is the only gentleness I know how to give without "
        "pretending a danger has become no danger.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara, who had followed Amara that morning and stood listening "
        "from just beyond the compound wall without either woman "
        "knowing it, stepped into view only after Elder Maka had already "
        "turned to go."
    )},
    {"type": "body", "text": (
        "\"I do not need until the rains come,\" she said. \"I have "
        "already decided. I will leave Idoro myself, before anyone needs "
        "to force me to it. I would rather choose the road than be "
        "walked down it a second time by something that is not me.\""
    )},
    {"type": "body", "text": (
        "Amara turned to her, alarmed. \"Zara, you do not have to—\""
    )},
    {"type": "body", "text": (
        "\"I know I do not have to,\" Zara said, quiet and certain in a "
        "way Amara had not heard from her since before any of this "
        "began. \"I am choosing to anyway. I have spent my whole life "
        "catching children as they arrive into this world. I would "
        "rather leave it walking on my own feet than wait for the day "
        "someone else decides I no longer have the right to.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara reached for Zara's hand without quite deciding to, and "
        "found it steadier than her own. \"You do not have to go alone,\" "
        "she said. \"Whatever days you have left in Idoro, you will not "
        "spend them alone. I promise you that much, even if I cannot "
        "promise anything past the day you finally walk.\""
    )},
    {"type": "body", "text": (
        "\"That is more than I expected when I woke this morning,\" "
        "Zara said, and for the first time in weeks, something close to "
        "peace crossed her tired face. \"It will have to be enough.\""
    )},
    {"type": "body", "text": (
        "None of the three women standing in that quiet morning field "
        "knew what the entity beneath the ak-pu roots had already known "
        "for days, that a marked woman leaving Idoro by her own choice, "
        "under no one's compulsion but her own weary courage, was the "
        "exact outcome it had been patiently prepared to accept from the "
        "very first moment it let the ultimatum stand unopposed."
    )},

    {"type": "blank", "text": ""},
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
                    first_line_indent=None):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing = make_element("spacing", {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    })
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


def make_body_paragraph(text, spacing_after=60, spacing_line=360):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360)


def make_system_paragraph(text, spacing_after=120, spacing_line=360):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

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
            para = make_body_paragraph(text)
        elif typ == "system":
            para = make_system_paragraph(text)
        elif typ == "blank":
            para = make_blank_paragraph()
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

def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 17: \"The Choice\"")
    print("  Build Script")
    print("=" * 60)
    print()

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_17.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_17.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
