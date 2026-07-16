#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 18: "The Reveal"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-25: Episode 18 is the climax of the Zara arc. On the
morning of her departure from Idoro, a small crowd gathers to see her off,
enough witnesses that the entity, calculating that her usefulness as a
private thread is ending the moment she leaves its reach on foot, decides
the value of holding Elder Maka's secret in reserve has run out. It seizes
Zara fully and publicly for the first time, in front of the whole
gathered crowd rather than only Amara's household, and spends the
leverage it has held since Episode 15: it exposes Elder Maka's own hidden
condition to the entire village, turning grief and duty in one instant
into panic and open suspicion of the very woman who has enforced Idoro's
law for thirty four years. The episode closes with the crowd's fear
turning on Elder Maka in real time, and the entity's flat calculation
proven correct that a single public act could do more damage to the
village's order than weeks of private threats ever managed.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_18.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighteen"},
    {"type": "title_ep_name", "text": "The Reveal"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE MORNING ZARA MEANT TO LEAVE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "More people came to see Zara off than Amara expected, given "
        "everything the village had done to her in the weeks before. "
        "Some came out of the old respect thirty years of careful hands "
        "had earned her. Some came, Amara suspected, simply to be "
        "certain with their own eyes that whatever frightened them was "
        "truly leaving."
    )},
    {"type": "body", "text": (
        "Zara stood at the edge of the compound with a single bundle "
        "over one shoulder, everything she had chosen to carry out of a "
        "life she had spent thirty years building, and managed something "
        "close to a smile for the small crowd that had gathered along "
        "the path, Obi beside her, Amara close on her other side, Elder "
        "Maka standing a little apart with her two watchers and her "
        "daughter Adaugo, who had come without quite understanding why "
        "her mother's face had looked so tired all week."
    )},
    {"type": "body", "text": (
        "\"I did not think this many of you would come,\" Zara said, "
        "her voice a little unsteady."
    )},
    {"type": "body", "text": (
        "\"You delivered half of Idoro,\" an older woman near the front "
        "called out. \"Half of Idoro remembers it, whatever the rest of "
        "us have let ourselves forget lately.\""
    )},
    {"type": "body", "text": (
        "A few others murmured agreement, small nods passing through "
        "the crowd like a current finding its own direction, and for a "
        "moment the morning felt almost like what it should have been "
        "all along, a village honoring a woman who had spent her whole "
        "life catching its children as they arrived, rather than casting "
        "her out for a fear none of them had chosen for her."
    )},
    {"type": "body", "text": (
        "Amara watched the gathering with a knot in her stomach she "
        "could not quite place, some old animal sense telling her that a "
        "morning this large, this witnessed, was exactly the kind of "
        "morning the entity had spent weeks patiently waiting for, "
        "though she could not have said why the thought arrived just "
        "then, of all the mornings it might have chosen to."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY DECIDED TO SPEND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity watched the gathering "
        "crowd assemble through Zara's own eyes, counting witnesses the "
        "way it had once counted the pair standing beneath a mango tree, "
        "except that this count ran into the dozens rather than the "
        "twos and threes it had risked before."
    )},
    {"type": "body", "text": (
        "It had held the old woman's secret in reserve for exactly this "
        "kind of moment, though it had not known, when it first decided "
        "to hold rather than spend, precisely which morning would prove "
        "to be the right one. The midwife was walking out of its reach "
        "on her own two feet within the hour, whatever remained unspent "
        "in that particular thread about to become unusable currency the "
        "instant she crossed the boundary of Idoro's fields. A held card "
        "not played before the game ended was worth exactly nothing."
    )},
    {"type": "body", "text": (
        "There would not be a larger crowd than this one for a long "
        "while, and there would certainly never again be a moment where "
        "spending the secret cost the entity anything at all, since the "
        "vessel it had spent it through was already leaving and could "
        "not be punished for having carried the words."
    )},
    {"type": "body", "text": (
        "There was value beyond the secret itself in choosing this "
        "particular morning. Every person gathered along that path had "
        "come believing they understood the shape of the danger facing "
        "Idoro, a marked woman being sent away so the village could "
        "return to feeling safe. The entity intended to correct that "
        "belief in the most public way available to it, and to correct "
        "it so thoroughly that no quiet council afterward could soften "
        "what every witness had heard with their own ears."
    )},
    {"type": "body", "text": (
        "A rumor could be managed. A hundred people's shared memory of "
        "a single morning could not be managed nearly so easily, and the "
        "entity had learned, across weeks of watching this village try "
        "and fail to contain its own fear, that unmanageable fear was "
        "worth more to it than any quiet arrangement Amara or Elder Maka "
        "might otherwise have found a way to broker between themselves."
    )},
    {"type": "body", "text": (
        "In the hollow, far beneath all of this, the vessel had gone "
        "still and listening, some new awareness in him reaching toward "
        "the gathering fear the way a plant turns its leaves toward "
        "light it has not yet learned to name. The entity let him feel "
        "it. There was no harm now in letting the boy taste what was "
        "coming, so long as the tasting stayed exactly that, and nothing "
        "more, for a little while longer."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It reached into her fully, all at once, with none of the "
        "careful gentleness it had used in Amara's yard. This was not a "
        "conversation it intended to have quietly."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "FULL PUBLIC POSSESSION AUTHORIZED. WITNESS COUNT: MAXIMAL AVAILABLE. RESERVED LEVERAGE: ELDER MAKA SECOND THREAD, TO BE SPENT IN FULL."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT THE WHOLE VILLAGE SAW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara's body went rigid so suddenly that the bundle slid from "
        "her shoulder and struck the ground, and every conversation "
        "along the path died at once as her head lifted at an angle no "
        "grieving, tired woman lifts her own head."
    )},
    {"type": "body", "text": (
        "\"Good,\" the voice said, using her mouth, carrying further and "
        "louder than it had ever dared carry before, reaching every "
        "single person gathered along that path at once. \"So many of "
        "you, come to watch a woman leave the only home she has known. "
        "None of you came to ask why she is truly leaving.\""
    )},
    {"type": "body", "text": (
        "The crowd recoiled as one body, mothers pulling children back "
        "by the shoulder, men reaching for tools they had not thought to "
        "carry as weapons an hour ago. Elder Maka stepped forward, her "
        "face gone the color of old ash. \"Enough,\" she said, though her "
        "voice carried none of its usual command. \"Whatever you are, "
        "you have taken enough from this village already.\""
    )},
    {"type": "body", "text": (
        "\"I have taken almost nothing from this village that it did "
        "not offer me first, out of its own fear,\" the voice said, and "
        "turned Zara's borrowed eyes directly on Elder Maka with a "
        "patience that felt, to everyone watching, far worse than any "
        "anger could have. \"You, of everyone standing here, should "
        "understand that better than most. You have been offering me "
        "something of your own for weeks now, old woman, and telling no "
        "one.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"That is a lie,\" Elder Maka said, but her voice cracked in "
        "the middle of the word lie, and every person close enough to "
        "hear the crack understood, before she had said another word, "
        "that it was not."
    )},
    {"type": "body", "text": (
        "A murmur ran through the crowd, confusion first, then "
        "something sharper as the voice continued, unhurried, cruel in "
        "its patience."
    )},
    {"type": "body", "text": (
        "\"She bound a thread out of a sleeping child's blood and could "
        "not bear to let it scatter loose, so she took it into her own "
        "body instead. She has lost hours of her own life to it every "
        "week since. She has lied to her own daughter's face about it. "
        "She stands here now, ready to send another marked woman out "
        "into exile, while carrying the very same mark herself, hidden "
        "beneath robes and thirty and four years of practiced authority.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The silence that followed broke all at once into noise, "
        "dozens of voices rising together, Adaugo's cry of \"Mother, is "
        "this true,\" cutting through the rest of it sharp enough that "
        "even the entity, watching through Zara's stolen eyes, seemed to "
        "pause and consider the sound worth savoring before it let the "
        "moment continue."
    )},
    {"type": "body", "text": (
        "Elder Maka did not answer her daughter. She could not, not "
        "with every eye in Idoro suddenly fixed on her instead of on the "
        "woman she had just finished exiling, and in the space of her "
        "silence, the crowd's fear finished the work the voice had "
        "started, turning from the possessed midwife entirely and "
        "settling instead, hot and sudden, onto the one woman in Idoro "
        "who had spent her whole life telling everyone else exactly how "
        "afraid they ought to be."
    )},
    {"type": "body", "text": (
        "\"She sent my sister's boy to the elders' council for less than "
        "this,\" someone shouted from further back, and the voice was "
        "swallowed almost at once by others rising to join it, old "
        "grievances long buried under thirty and four years of unquestioned "
        "authority finding, all at once, a reason to surface. The two "
        "watchers beneath the mango tree looked at each other and then "
        "at the woman they had been posted to obey for weeks, and neither "
        "of them moved to defend her."
    )},
    {"type": "body", "text": (
        "\"You would have killed Kene without a second council if this "
        "one had not argued you out of it,\" Obi said, low and furious, "
        "his arm still around Zara's shaking shoulders. \"And you have "
        "been carrying the same darkness the whole time you stood over "
        "us deciding whether our son deserved to live.\""
    )},
    {"type": "body", "text": (
        "Elder Maka opened her mouth to answer him, or perhaps to answer "
        "all of them at once, and found, for the first time in thirty "
        "and four years of standing in front of a frightened crowd, that "
        "she did not have a single word left that any of them were "
        "willing to believe."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara's body sagged the instant the voice released her, "
        "collapsing into Obi's waiting arms, spent and shaking and "
        "utterly unaware of what had just been spoken through her own "
        "mouth. But the crowd was no longer looking at Zara at all."
    )},
    {"type": "body", "text": (
        "They were looking at Elder Maka, and for the first time in "
        "thirty and four years, Idoro looked at her the way it had once "
        "looked at every marked mother she had ever stood in judgment "
        "over."
    )},
    {"type": "body", "text": (
        "Amara stood very still in the middle of it, Zara's weight half "
        "leaning against her, and felt something she had not expected to "
        "feel amid all that noise, a thin, unwelcome thread of pity for "
        "the very woman she had spent weeks learning to fear. Elder Maka "
        "had asked for exactly this kind of mercy once, quietly, in a "
        "field at dawn, and Amara had given it to her without hesitation. "
        "The entity had just proven, in front of the whole village, "
        "precisely how little that private mercy was worth once it "
        "decided the moment had come to spend what it had been holding "
        "in reserve all along."
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
    print("  THE DARK RISE — Episode 18: \"The Reveal\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_18.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_18.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
