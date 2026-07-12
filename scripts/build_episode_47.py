#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 47: "The Name It Chose"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-23: Episode 47 is the payoff this whole block has been
building toward. Idoro's council refuses the trading House scholar's
request for formal contact, choosing protection over any managed channel
— and the scholar accepts gracefully but warns her House will "hear one
way or another" regardless. That same morning, Zara's certainty resolves
into action: she tells Amara plainly that today is the day, and Amara
walks her to the boundary rather than let her go alone, an echo of
walking Osadebe there in Episode 30. At the tree line, the presence
speaks through Zara directly for the first time, in front of Amara and
the entity both, brief and unmediated the way the entity once addressed
the crown. It does not explain itself. It does not threaten. It does one
thing only: it gives the vessel a name, seizing the choice the entity had
spent seven episodes deliberately, carefully refusing to make alone. The
episode closes on the entity, watching from Oso, forced to reckon in real
time with a decision it no longer has any say in at all.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_47.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Seven"},
    {"type": "title_ep_name", "text": "The Name It Chose"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A REFUSAL, AND A MORNING THAT WAS ALREADY DECIDED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The council's answer came at first light, delivered by Amara "
        "herself to the scholar waiting patiently at the field's "
        "edge. \"We will not arrange the audience you asked for,\" she "
        "said. \"Not out of disrespect for the manner you asked in, "
        "which was more honest than the last visit your House sent. "
        "But this village has paid enough for other people's curiosity "
        "about that ground. We are done being the doorway other "
        "people's questions walk through.\""
    )},
    {"type": "body", "text": (
        "The scholar accepted it exactly as she had promised she "
        "would, without argument, gathering her books with the same "
        "unhurried care she had shown arriving. \"I understand,\" she "
        "said. \"I will tell you honestly, since honesty is the only "
        "coin I came here spending: my House will learn what it wants "
        "to know one way or another, whether through a door you open "
        "for us or one that simply opens on its own eventually. I "
        "would have preferred the first. I suspect the second is more "
        "likely now.\" She left the way she came, alone and unarmed, "
        "and Amara watched her go with the uneasy sense of having won "
        "an argument that had not actually settled anything."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Zara found her within the hour, dressed and ready in a way "
        "that needed no explanation once Amara saw her face. \"Today,\" "
        "Zara said simply. \"I do not know how I know. I only know "
        "that if I wait past today, I will have missed whatever this "
        "was always going to be.\""
    )},
    {"type": "body", "text": (
        "Amara did not argue, and did not let her walk alone either, "
        "matching her stride step for step down the same path she had "
        "once walked with Osadebe months before, toward the same tree "
        "line, carrying the same particular fear of a boundary about "
        "to be crossed in a way no one present could fully control."
    )},
    {"type": "body", "text": (
        "She left word with Obi before she went, brief and unable to "
        "explain more than she understood herself, and found him "
        "standing in the doorway with Kene balanced on one hip, "
        "watching her go with the particular helpless patience of a "
        "man who had learned, across a difficult year, that some "
        "mornings could not be talked out of happening. \"Come back,\" "
        "was all he said, and she promised him she would, though the "
        "promise felt smaller than the moment deserved, a single small "
        "true thing offered against a morning that had already decided "
        "to be larger than either of them."
    )},
    {"type": "body", "text": (
        "Kene reached for her as she turned to go, a small, ordinary "
        "gesture that meant nothing more than a toddler's fleeting "
        "want, and Amara felt the whole enormous weight of everything "
        "she had never been able to give her other son settle over her "
        "shoulders one more time before she made herself walk away from "
        "the one she could still hold."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE BOUNDARY — A NAME NEITHER OF THEM CHOSE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The entity felt them approaching long before they reached "
        "the last stone, and felt, alongside them, the presence "
        "gathering itself at the very edge of what the entity could "
        "still perceive clearly, patient and enormous and utterly "
        "unhurried, the way a held breath gathers itself in the "
        "instant just before it is finally released."
    )},
    {"type": "body", "text": (
        "It considered, one final time, whether to intervene, to "
        "place itself bodily between Zara and whatever was coming the "
        "way it had once placed roots between Idoro and six armed "
        "men. Every instinct three centuries deep argued for exactly "
        "that, a door closing before anything unknown could walk "
        "through it. It chose, instead, to do nothing, understanding "
        "with a clarity that offered no comfort at all that force had "
        "never once been the right answer to a power this patient, and "
        "that the only thing left to offer, after everything else it "
        "had already tried, was simply witness."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Zara stopped at the last stone without needing to be told, "
        "and her eyes, when she turned toward the tree line, had "
        "already stopped being entirely her own. The voice that came "
        "from her mouth was quiet, unhurried, carrying none of the "
        "hunger the entity's own borrowed voices had once carried "
        "through the dibia, none of the urgency it had carried through "
        "Zara herself in earlier days. It simply spoke, the way "
        "something speaks when it has already decided exactly what it "
        "intends to say and has felt no need to rehearse it."
    )},
    {"type": "body", "text": (
        "\"I have watched him since before the one who raised him "
        "understood what it was raising,\" it said, through a mouth "
        "that trembled slightly but did not fight the words leaving "
        "it. \"I have been patient because patience has always served "
        "me better than haste. I am no longer certain patience alone "
        "still serves either of us, now that he has learned to reach "
        "for himself.\""
    )},
    {"type": "body", "text": (
        "Amara stood frozen beside her, unable to look away, close "
        "enough to see the strain the words cost the body carrying "
        "them and too afraid to reach for Zara while the voice still "
        "held her. It turned, unmistakably, toward something it "
        "clearly believed was listening from the dark behind the tree "
        "line. \"You have given him truth, these last weeks, when "
        "concealment would have been easier. I did not expect that "
        "from you. It changes how much longer I am willing to simply "
        "watch. He asked for a name. You have not given him one. I "
        "will not wait for either of you to finish deciding whether he "
        "deserves it.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "VESSEL: UNMEDIATED CONTACT EVENT IN PROGRESS. PRESENCE "
        "ADDRESSING ENTITY DIRECTLY THROUGH THIRD PARTY HOST. NAMING "
        "ACTION IMMINENT. ENTITY UNABLE TO INTERVENE WITHOUT RISKING "
        "HARM TO HOST."
    )},
    {"type": "body", "text": (
        "\"His name is Chibundu,\" the voice said, plain and final, "
        "the way a single stone is set into ground already prepared "
        "for it. \"The one whom the presence carries. It is not the "
        "name his village would have given him on the eighth day. It "
        "is the name that is actually true. I did not choose it to "
        "wound either of you. I chose it because pretending he is "
        "still nameless has already cost him more than either of you "
        "seem willing to admit.\""
    )},
    {"type": "body", "text": (
        "Zara's knees buckled the instant the voice released her, and "
        "Amara caught her before she reached the ground, holding her "
        "upright with hands that would not stop shaking long after the "
        "tree line had gone silent again. Neither woman spoke on the "
        "walk back, Amara's mind turning over a single word that did "
        "not yet feel real enough to say aloud, as though saying it "
        "too soon might somehow make it truer than either of them was "
        "ready for."
    )},
    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity sat a long while with a "
        "name it had not chosen, had not been asked about, and could "
        "not now unhear, understanding with total clarity that "
        "whatever it had believed about its own authority over this "
        "one small life had just been settled by someone else "
        "entirely, in less time than it took to speak four careful "
        "words."
    )},
    {"type": "body", "text": (
        "The boy was waiting when it finally turned its attention back "
        "toward the hollow, sitting very still among his stones in a "
        "way that told the entity he had felt some part of what had "
        "just happened, even without understanding the shape of it "
        "fully. \"Something changed,\" he said. \"I do not know what. It "
        "feels like a door opened somewhere I cannot see.\""
    )},
    {"type": "body", "text": (
        "The entity considered, one final time, softening what it was "
        "about to say, and found, as it had found so often these last "
        "weeks, that softening it would only cost more than simply "
        "saying it plainly. \"You have a name now,\" it told him. \"It "
        "was not given by me. It came from the one who has been "
        "watching us both, spoken through Zara at the boundary, in "
        "front of your mother.\""
    )},
    {"type": "body", "text": (
        "The boy went very still, the particular stillness he saved "
        "for things too large to react to all at once. \"What is it,\" "
        "he asked, and his voice, small and careful, carried none of "
        "the fear the entity had braced itself to hear."
    )},
    {"type": "body", "text": (
        "\"Chibundu,\" the entity said. \"The one whom the presence "
        "carries.\""
    )},
    {"type": "body", "text": (
        "The boy said it back once, quietly, testing its shape the "
        "way he once tested every new stone before deciding where it "
        "belonged, and something in his small face settled that the "
        "entity had not seen settle in weeks, a boy trying on the "
        "first true weight he had ever been allowed to carry that was "
        "entirely, unmistakably his own."
    )},
    {"type": "body", "text": (
        "\"Are you angry,\" Chibundu asked, watching the entity's "
        "stillness with the same careful attention he gave everything "
        "he had learned to read in it. \"That it was not you who gave "
        "it to me.\""
    )},
    {"type": "body", "text": (
        "The entity turned the question over honestly before "
        "answering, aware that whatever it said now would settle "
        "permanently into the shape of a memory neither of them would "
        "ever be able to fully set back down. \"I do not know yet what "
        "I feel,\" it admitted. \"I have spent three centuries certain "
        "that patience always eventually wins. Tonight I watched "
        "something patient enough to out wait even me. I think, "
        "somewhere underneath everything else, I am relieved the "
        "waiting is finally over. I think I am also afraid of exactly "
        "how little that relief actually changes about what comes "
        "next.\""
    )},
    {"type": "body", "text": (
        "Chibundu considered this with the same unhurried seriousness "
        "he gave every truth large enough to require turning over more "
        "than once, and went back to his stones without needing "
        "anything further said, arranging them now, for the first "
        "time, around a single smooth center stone as though the "
        "whole careful pattern had finally found the name it had "
        "always been quietly waiting to organize itself around."
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
    print("  THE DARK RISE — Episode 47: \"The Name It Chose\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_47.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_47.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
