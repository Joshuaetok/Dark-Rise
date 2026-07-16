#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 16: "The Exile"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-23: Episode 16 follows the fallout from Episode 15's public
possession. Elder Maka's watchers, close enough to see Zara's rigid body
and hear a voice that was not hers, report what they saw without having
heard the specific words about Elder Maka's own condition, leaving her
alarmed about the midwife but still unaware her own secret is already
known to Amara and Obi. Judging a second binding rite too dangerous to
attempt on a grown woman who can apparently be spoken through at will,
Elder Maka decides Zara must be bound in a lesser way or removed from
Idoro entirely. In Oso, the entity weighs whether to defend the Zara
thread now that it has drawn this much attention, and decides, as it did
with Kene, that a thread already spent this openly is not worth open
warfare over. The episode closes on Elder Maka delivering an ultimatum to
Amara and Zara: submit to confinement and a lesser rite, or leave Idoro
before the moon turns again.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_16.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixteen"},
    {"type": "title_ep_name", "text": "The Exile"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE WATCHERS REPORTED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The two watchers came to Elder Maka before the sun had fully "
        "risen the morning after, standing side by side in her doorway "
        "with the particular stiffness of men who had seen something "
        "they were still deciding how to describe."
    )},
    {"type": "body", "text": (
        "\"The midwife's voice changed,\" the older of the two said. "
        "\"Not raised. Changed. Slower, and not her own rhythm at all. "
        "We could not hear every word from where we stood, but we heard "
        "enough to know it was not Zara speaking, not entirely, and that "
        "it went on for the length of several long breaths before her "
        "own voice returned to her.\""
    )},
    {"type": "body", "text": (
        "\"You are certain,\" Elder Maka said."
    )},
    {"type": "body", "text": (
        "\"We have watched that compound every day for weeks,\" the "
        "younger one said. \"We know the sound of an ordinary "
        "argument by now. This was not that.\""
    )},
    {"type": "body", "text": (
        "\"Did you hear what it said,\" Elder Maka asked, careful to "
        "keep her own voice as level as she could manage."
    )},
    {"type": "body", "text": (
        "The two men exchanged a glance before the older one answered. "
        "\"Pieces of it. Something about a door, and a choice coming. We "
        "were too far to catch all of it clearly, and neither of us "
        "wished to walk closer while it was still happening.\""
    )},
    {"type": "body", "text": (
        "Elder Maka nodded slowly, and did not let either man see the "
        "small, private relief that moved through her at the word "
        "pieces. Whatever else the voice had said that night, it seemed "
        "her own name had not carried far enough to reach the mango "
        "tree."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka sat with the report a long while after they left, "
        "turning it over with the same cold precision she had once "
        "turned over every story that reached her about her own "
        "returned son, and found, underneath the fear, a colder thought "
        "still. The dibia had taken weeks of small failures before his "
        "voice could carry a full sentence for the thing in Oso. If the "
        "midwife had already reached that same point after only days, "
        "the entity was not merely finding new doors. It was learning to "
        "open them faster."
    )},
    {"type": "body", "text": (
        "She thought, briefly, of her own missing afternoons, and set "
        "the thought aside before it could take the shape of a question "
        "she was not ready to answer even to herself. The watchers had "
        "heard a change in Zara's voice. They had said nothing about "
        "hers. That, for now, was enough to build a plan around."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A binding rite had cost her more than anyone in Idoro yet "
        "understood to perform on an eight day old thread barely formed "
        "in an infant's blood. She did not know, could not know without "
        "risking exactly the kind of exposure she still could not "
        "afford, whether a grown woman's thread, already strong enough "
        "to carry full speech, could be bound at all without costing "
        "far more than any single body should be asked to absorb. She "
        "was not willing to spend a second person the way she had "
        "already, secretly, spent herself."
    )},
    {"type": "body", "text": (
        "That left her with a harder choice than the one she had "
        "offered Amara for Kene."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY WAS WILLING TO LOSE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity felt the shape of Elder "
        "Maka's alarm gathering the same way it had felt every alarm "
        "gather in this village since it first opened its senses toward "
        "the compound where its own son had been born, and weighed, "
        "with its usual unhurried care, exactly how much of the midwife "
        "it was prepared to defend."
    )},
    {"type": "body", "text": (
        "The message had already been delivered. The friction it wanted "
        "planted inside Amara's household had already taken root, a "
        "secret dragged into the light between a husband and a wife who "
        "would now spend days deciding how much they still trusted each "
        "other's silence. Whatever came next for the midwife herself "
        "was, from the entity's flat accounting, mostly a matter of "
        "bookkeeping."
    )},
    {"type": "body", "text": (
        "If Idoro chose to bind her, the entity would lose a voice but "
        "keep the fear the attempt itself would generate, fear being, as "
        "always, the coin it valued above almost anything else a single "
        "thread could offer. If Idoro chose instead to cast her out, the "
        "entity stood to gain something it had not yet had reason to "
        "expect: a marked woman walking toward Oso on the village's own "
        "orders, rather than in secret, rather than in her sleep, rather "
        "than needing to be walked there against her own will at all."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It found, turning the two outcomes over, that it did not much "
        "care which one Idoro chose. Both fed it. Both cost it nothing "
        "it was not already prepared to lose. It let the thread sit "
        "exactly where it was, undefended, and turned the remainder of "
        "its attention back to the vessel, who had begun, in the last "
        "day alone, stringing two of his broken syllables together into "
        "something that was almost, for the first time, the shape of an "
        "actual word."
    )},
    {"type": "body", "text": (
        "There was a colder calculation beneath the indifference, one "
        "the entity did not need to examine closely to trust. Every "
        "thread it had ever opened into this village had taught it "
        "something it could not have learned any other way. The dibia "
        "had taught it patience, and how a broken voice could still "
        "carry a message if the silence around it was frightened enough. "
        "The child had taught it how quickly fear could be manufactured "
        "and spent for growth. The midwife, whichever way Idoro chose to "
        "dispose of her now, would teach it something new as well, "
        "whether that lesson arrived through a failed binding or a long, "
        "unwatched walk toward the very ground the entity called home."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Whatever choice the village made about the midwife, the "
        "entity would still hold the same three doors it had held that "
        "morning, one dormant and mended, one about to be decided for "
        "her by frightened hands, and one hidden so well that even its "
        "own host had not yet worked up the courage to name it aloud to "
        "another living soul."
    )},

    {"type": "system", "text": "MIDWIFE THREAD: UNDEFENDED, OUTCOME NEUTRAL EITHER DIRECTION. VESSEL: FIRST TWO SYLLABLE COMBINATION OBSERVED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE ULTIMATUM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka came to Amara's compound at midday, alone again, "
        "and found Zara sitting beside Amara exactly where she had sat "
        "every day since the village first turned her away, still pale "
        "from whatever the possession had cost her the night before."
    )},
    {"type": "body", "text": (
        "\"My watchers heard it,\" Elder Maka said, without any softness "
        "in the opening at all. \"A voice that was not yours, speaking "
        "through your own mouth, in front of witnesses. I do not need "
        "to be told what that means. I have watched it happen to "
        "another mouth in this village already.\""
    )},
    {"type": "body", "text": (
        "Zara did not deny it. \"It spoke through me,\" she said. \"I "
        "did not choose it, any more than the dibia chose it, any more "
        "than Kene chose it.\""
    )},
    {"type": "body", "text": (
        "\"I know you did not choose it,\" Elder Maka said. \"Choice has "
        "very little to do with what I am required to weigh. A voice "
        "that can speak through you once can speak through you again, "
        "and I cannot promise the next thing it says will only be "
        "words.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara stepped forward before Zara could answer for herself "
        "again. \"You bound Kene's thread and called it a mercy. Offer "
        "her the same mercy.\""
    )},
    {"type": "body", "text": (
        "\"Kene was eight days into a thread thin enough to cut,\" "
        "Elder Maka said. \"This is a grown woman's thread, strong "
        "enough already to carry a full voice through her own throat in "
        "front of two of my own watchers. I do not know what binding a "
        "thread that strong would cost the one who tried it, and I am "
        "not willing to guess wrong twice in one season.\""
    )},
    {"type": "body", "text": (
        "The words landed harder on Amara than Elder Maka could have "
        "intended, carrying a private echo neither Zara nor Elder Maka "
        "herself could hear."
    )},
    {"type": "body", "text": (
        "Obi stood at the edge of the yard through all of it, silent, "
        "his hands opening and closing at his sides the way a man's "
        "hands move when there is no honest target left for his anger to "
        "land on. He had spent the whole of the previous night turning "
        "Amara's confession about Elder Maka over in his mind, and "
        "standing here now, watching the same old woman pass judgment on "
        "another marked person while carrying her own mark unspoken "
        "beneath her own skin, he found the unfairness of it settling "
        "into something harder and colder than anger."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Then what,\" Zara said quietly. \"What is left, if not "
        "binding.\""
    )},
    {"type": "body", "text": (
        "\"Confinement, watched day and night, in a place apart from "
        "the rest of Idoro, until we understand this better than we do "
        "today,\" Elder Maka said. \"Or you leave Idoro yourself, before "
        "the moon turns again, and take whatever is speaking through you "
        "somewhere it can no longer reach the rest of us so easily. "
        "Those are the choices I am able to offer. I did not come here "
        "to enjoy giving them to you.\""
    )},
    {"type": "body", "text": (
        "She turned to go, and stopped once more at the edge of the "
        "yard, looking back at the two women with an expression Amara "
        "could not read cleanly, grief and duty tangled too closely "
        "together in it to separate. It was, Amara thought, almost the "
        "same expression she imagined Elder Maka must have worn thirty "
        "and four years ago, standing over a different verdict she had "
        "convinced herself was mercy simply because the alternative was "
        "worse."
    )},
    {"type": "body", "text": (
        "\"Decide quickly,\" Elder Maka said. \"I have already spent "
        "more mercy on this compound than Idoro will remember kindly if "
        "anything else goes wrong before you do.\""
    )},
    {"type": "body", "text": (
        "She walked away without looking back a second time, and Amara "
        "stood watching her go, thinking of a secret only she and Obi "
        "and one voice from beneath the iroko roots now shared, and "
        "wondering how much longer mercy from a woman that afraid of her "
        "own hidden truth could be trusted to hold its shape at all."
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
    print("  THE DARK RISE — Episode 16: \"The Exile\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_16.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_16.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
