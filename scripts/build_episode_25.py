#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 25: "The Gathering"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-01: Episode 25 brings Ozoemena's threat from Episodes 21
and 22 to its breaking point. Stung by Elder Maka's warning and needing to
rebuild the authority his standoff with Amara cost him in front of his own
followers, he sets a date to perform a rite against the dibia in public,
using the half remembered words Elder Maka gave him. Amara, despite every
reason to let him walk into the danger he has been threatening her family
with, tries once to warn him plainly, and is refused. In Oso, the entity,
having weighed the dibia thread's dwindling usefulness across two prior
episodes, finally decides: rather than let a clumsy human rite simply
fail or succeed quietly, it will make the attempt itself into an example
memorable enough to discourage anyone from trying again for a long while.
The episode ends with the crowd gathered, the rite beginning, and the
first small, wrong sign already visible in the dibia's convulsing body.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_25.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Five"},
    {"type": "title_ep_name", "text": "The Gathering"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT AMARA TRIED TO SAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ozoemena set the date three days after his visit to Amara's "
        "compound, announcing it to his gathered followers the way a "
        "man announces something he has already decided cannot be "
        "undone without costing him more than proceeding will."
    )},
    {"type": "body", "text": (
        "Word reached Amara by midday, carried by a neighbor still "
        "loyal enough to warn her even now. She stood in her own yard "
        "turning the news over, and found, to her own surprise, that "
        "some old, stubborn part of her wanted to walk straight to "
        "Ozoemena's compound and stop him, despite everything he had "
        "threatened her family with only days earlier."
    )},
    {"type": "body", "text": (
        "\"Why,\" Obi asked, when she told him where she intended to "
        "go. \"He has given us nothing but threats since the day he "
        "rose. Let him walk into whatever Elder Maka warned him about. "
        "It costs us nothing.\""
    )},
    {"type": "body", "text": (
        "\"It costs the dibia everything, if this goes as badly as "
        "Elder Maka fears,\" Amara said. \"And it may cost the whole "
        "village more than any of them understand yet. I am not going "
        "to save Ozoemena. I am going because someone in that crowd "
        "deserves to hear the truth before it happens instead of after.\""
    )},
    {"type": "body", "text": (
        "Obi studied her for a long moment, the particular look he had "
        "learned to give her across these last difficult months, equal "
        "parts worry and a grudging kind of admiration for a woman who "
        "kept finding new ways to spend her own safety on people who had "
        "given her every reason not to bother. \"You are a better person "
        "than this village deserves,\" he said finally. \"I mean that as "
        "a compliment and a complaint in equal measure.\""
    )},
    {"type": "body", "text": (
        "\"I am not doing it for the village,\" Amara said. \"I am "
        "doing it because I do not want to spend the rest of my life "
        "wondering whether I could have stopped something and chose "
        "silence instead. I have carried enough of that particular "
        "weight already, and I do not intend to add to it needlessly.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She found him surrounded by his followers, rehearsing the "
        "words Elder Maka had given him with the particular confidence "
        "of a man who had convinced himself that confidence alone could "
        "close the gap between knowledge and understanding."
    )},
    {"type": "body", "text": (
        "\"Do not do this,\" Amara said, without preamble. \"I have "
        "seen what this thing does to people who reach for it "
        "carelessly. I watched it happen to Elder Maka. I do not want "
        "to watch it happen to you, whatever you have threatened my "
        "family with.\""
    )},
    {"type": "body", "text": (
        "Ozoemena turned to her, and something in his face was almost "
        "amused. \"You come to warn me now, after refusing me every "
        "answer I asked for honestly. Forgive me if I do not trust the "
        "sudden concern of a woman who has spent this whole crisis "
        "protecting her own family's secrets first.\""
    )},
    {"type": "body", "text": (
        "\"Believe whatever motive makes it easiest to ignore me,\" "
        "Amara said. \"But do not say, after, that no one told you "
        "plainly what you were reaching for.\""
    )},
    {"type": "body", "text": (
        "He did not answer that, and his silence told her everything "
        "she needed to know about whether the warning had landed "
        "anywhere it could still do some good."
    )},
    {"type": "body", "text": (
        "One of his younger followers, the same one who had shifted "
        "uneasily in Amara's yard days earlier, looked between them "
        "with open uncertainty on his face. \"Elder Maka warned him too, "
        "did she not,\" he said quietly, more to himself than to anyone "
        "listening. \"And now this woman is warning him as well. Two "
        "people who understand this thing better than the rest of us, "
        "both saying the same thing.\""
    )},
    {"type": "body", "text": (
        "\"Two people who have already lost their nerve,\" Ozoemena "
        "said, sharper than he needed to be, and the young man fell "
        "silent, though Amara noted, walking away, that the silence had "
        "the particular texture of a doubt swallowed rather than a doubt "
        "resolved."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE DECISION THE ENTITY FINALLY MADE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the date settle into "
        "place the way it felt every decision Idoro made about its "
        "threads now, and turned, at last, to the question it had left "
        "open across two full episodes of careful observation."
    )},
    {"type": "body", "text": (
        "Whether the dibia's thread was still worth defending."
    )},
    {"type": "body", "text": (
        "The thread itself had given almost nothing new in weeks. Its "
        "value as a mouthpiece had been spent long ago, its usefulness "
        "as a hidden door mostly exhausted the moment Ozoemena named it "
        "in front of the whole council. There was little left to lose "
        "by letting it go quietly, and the entity had genuinely "
        "considered, across those two episodes of watching, simply "
        "allowing the rite to succeed or fail on its own clumsy terms "
        "without spending any further effort on the outcome."
    )},
    {"type": "body", "text": (
        "It found, weighing the decision a final time, that quiet "
        "indifference was not, after all, the most valuable use of this "
        "particular moment."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A man had gathered a crowd to watch him prove himself against "
        "something he did not understand. That crowd would carry "
        "whatever happened next to every household in Idoro before the "
        "sun set, the way every public spectacle in this village had "
        "carried itself across every compound since the cleansing rite "
        "first taught the entity how efficiently fear traveled when it "
        "had witnesses. A quiet failure taught no one anything. A loud "
        "one, timed and shaped correctly, could teach an entire village "
        "to fear reaching for the entity's threads for a generation, "
        "and fear that deep, planted once and well, required almost no "
        "further tending to keep feeding it for years."
    )},
    {"type": "body", "text": (
        "It would not simply let the rite fail. It would make it "
        "unforgettable."
    )},
    {"type": "body", "text": (
        "There was a particular satisfaction in the decision, if "
        "satisfaction was still the right word for anything a presence "
        "without a face could be said to feel. Three centuries of "
        "patience had taught it that a village's fear, once planted deep "
        "enough at its root, needed almost no tending afterward to keep "
        "bearing fruit for years. Elder Maka's fall had taught Idoro to "
        "distrust its own authority. The dibia's ruin, timed correctly, "
        "would teach it something even more useful: that reaching for "
        "the entity directly, with any hand less careful than the one "
        "that had already paid dearly to learn caution, was a mistake no "
        "one survived making twice."
    )},
    {"type": "body", "text": (
        "In the hollow, the vessel sat very still through all of this "
        "calculating, some new, wordless awareness in him reaching "
        "toward the coming violence the way he had once reached toward "
        "the crowd's fear at Zara's send off, and the entity, noticing "
        "the reaching, did not trouble itself yet to decide what that "
        "particular sensitivity in him might eventually mean."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "DIBIA THREAD: DEFENSE AUTHORIZED. OBJECTIVE: MAXIMUM MEMORABLE YIELD, NOT SURVIVAL OF THE THREAD ITSELF."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT BEGAN AT DUSK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By dusk, nearly the whole of Idoro had gathered around the "
        "dibia's hut, drawn by the same mixture of dread and morbid "
        "curiosity that had once brought them out for Elder Maka's "
        "cleansing rite and again for Zara's aborted departure, each "
        "gathering larger than the last, as though the village could "
        "not stop assembling to watch itself absorb one more wound."
    )},
    {"type": "body", "text": (
        "Ozoemena stood at the center of it with the borrowed words "
        "clutched in one hand on a scrap of cloth, his followers "
        "arranged behind him in a rough approximation of the authority "
        "Elder Maka had once commanded without needing to arrange "
        "anything at all."
    )},
    {"type": "body", "text": (
        "The dibia himself sat propped upright near the fire, thinner "
        "than Amara remembered him, his grayed hair gone nearly white "
        "now, his eyes tracking the gathering crowd with an awareness "
        "that seemed, for the first time in longer than anyone could "
        "recall, almost entirely his own."
    )},
    {"type": "body", "text": (
        "Amara found a place near the front, close enough to see "
        "clearly, though she had told herself she would not stay for "
        "the whole of it, only long enough to know whether her warning "
        "had been worth the walking. Obi stood beside her, silent, his "
        "arms crossed in the particular stillness of a man watching "
        "something he had already decided he would not be able to stop "
        "no matter how loudly his own doubts argued for trying."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Ozoemena began the words Elder Maka had taught him, halting at "
        "first, then finding a rougher confidence as the crowd's "
        "silence pressed in around him, demanding he sound like a man "
        "who deserved to be standing where he stood."
    )},
    {"type": "body", "text": (
        "The dibia's body seized on the fourth line."
    )},
    {"type": "body", "text": (
        "Not the small tremor Amara remembered from the cleansing rite "
        "months earlier. A full, violent convulsion, his spine arching "
        "hard enough that the two men holding him staggered under the "
        "sudden weight of it, and his mouth opened on a sound that was "
        "not yet a word, not yet a scream, but the unmistakable, rising "
        "shape of something about to become both at once."
    )},
    {"type": "body", "text": (
        "Ozoemena faltered mid word, the borrowed confidence draining "
        "visibly from his face as the fire beside them guttered without "
        "any wind to explain it, and for one brief, unguarded instant "
        "Amara saw the same look cross his features that she had once "
        "seen cross Elder Maka's during the cleansing rite, a man "
        "realizing, an entire breath too late, exactly how far past his "
        "own understanding he had just reached, and exactly how little "
        "that realization was now going to be able to help him."
    )},
    {"type": "body", "text": (
        "The crowd's low murmur died all at once into a silence thick "
        "enough to feel, every eye in Idoro fixed on the dibia's "
        "arching body, waiting, breath held, to learn what kind of "
        "night this was about to become before any of them had the "
        "chance to decide whether to run from it."
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
    print("  THE DARK RISE — Episode 25: \"The Gathering\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_25.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_25.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
