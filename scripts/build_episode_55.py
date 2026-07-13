#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 55: "The Honored Guest"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-31: Episode 55 stages the summons Eze Amadi ordered at
the end of Episode 54. Chiazor, the trading House's longtime formal
sponsor at Udo, arrives believing he has been called to clarify a
simple boundary dispute. Eze Amadi and Nkiruka question him carefully,
revealing only as much as they must, and find a man who appears
genuinely unaware of Ebiere's covert operations in Idoro, his own
House's hierarchy deliberately built to keep its polished face
ignorant of its dirtier hands. Whether that ignorance is real or
rehearsed is left open. The episode closes on the detail that recasts
the whole conversation: pressed about how quickly his House could
resolve the matter to the crown's satisfaction, Chiazor lets slip that
someone senior to Ebiere, a figure his own House answers to directly,
is already travelling toward Idoro to take the matter in hand
personally, and has been for some time.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_55.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Five"},
    {"type": "title_ep_name", "text": "The Honored Guest"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A SIMPLE CLARIFICATION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chiazor arrived at the palace dressed for a pleasant morning "
        "rather than an interrogation, his cloth well cut and his "
        "manner easy, a man who had clearly spent years believing his "
        "House's name opened doors rather than drew suspicion through "
        "them. \"Your majesty honors me,\" he said, bowing with the "
        "practiced warmth of a longtime guest rather than a summoned "
        "party. \"I understand there has been some unfortunate "
        "confusion at a village boundary. I am certain we can settle "
        "it between reasonable men before it grows into anything "
        "larger than it needs to be.\""
    )},
    {"type": "body", "text": (
        "\"That is precisely why I asked you here,\" Eze Amadi said, "
        "matching the man's ease with an equal, unreadable warmth of "
        "his own. \"A confusion, as you call it, that has already cost "
        "one man his life and nearly cost a mother her son. I find "
        "myself wanting to understand it fully before I decide how "
        "reasonable a response it deserves.\""
    )},
    {"type": "body", "text": (
        "Nkiruka, seated slightly apart from the king in the manner of "
        "a counselor rather than a judge, asked the first careful "
        "question. \"Your House maintains a scholar in that region, I "
        "understand. A woman who has petitioned the local council "
        "directly for peaceful contact with whatever lives beyond "
        "Idoro's boundary. Can you tell us plainly what her mandate "
        "is, and who within your House she answers to.\""
    )},
    {"type": "body", "text": (
        "Chiazor's easy manner did not break, though something behind "
        "his eyes moved carefully, the look of a man checking his own "
        "footing before answering. \"Our House employs scholars in "
        "several regions where old stories persist about old powers,\" "
        "he said. \"Such things are, forgive me, good business. A "
        "House that understands what a place fears can trade there "
        "more safely than one that does not. I confess I do not know "
        "this particular woman's name. Our scholars report through "
        "channels that rarely reach my own desk.\""
    )},
    {"type": "body", "text": (
        "\"Her name is Ebiere,\" Eze Amadi said, watching the man's "
        "face with the same careful attention Osadebe had once turned "
        "on a captured operative at a much smaller table. \"And she has "
        "been paying a market trader in that same village for two "
        "years, gathering patrol counts, council attendance, and, most "
        "recently, the exact hour a crown patrol would stand down for "
        "a private family matter. That is not scholarship, Chiazor. "
        "That is an intelligence network operating inside my kingdom "
        "without my knowledge, wearing your House's name.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A CAREFULLY BUILT IGNORANCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chiazor's composure finally cracked, and whether the crack was "
        "genuine or simply well rehearsed was a question Eze Amadi "
        "found he could not answer with any certainty, watching it "
        "happen. \"I did not know that name,\" the man said, and his "
        "voice had lost most of its earlier ease. \"I want to believe "
        "you, majesty, and I find I cannot decide whether that "
        "willingness is honest surprise or simply the fear of a man who "
        "has just understood how little he actually knows about his "
        "own House's business.\""
    )},
    {"type": "body", "text": (
        "\"Perhaps both,\" Nkiruka said, not unkindly. \"A House built "
        "the way yours appears to be built keeps its honored sponsors "
        "clean precisely so they can say, truthfully, that they knew "
        "nothing. It is not an accident that the man dining at the "
        "king's own table is the one furthest from anything that could "
        "ever be traced back to a bribed soldier or a dead man at a "
        "boundary. That distance was built for you on purpose, whether "
        "you asked for it or not.\""
    )},
    {"type": "body", "text": (
        "Chiazor sat with that a long moment, and when he spoke again "
        "his voice had none of the practiced warmth left in it at all. "
        "\"I have represented this House at your court for eleven "
        "years,\" he said. \"I have believed, honestly, that I "
        "represented traders and surveyors and the occasional scholar "
        "of old stories. I do not know how to sit here and tell you "
        "with confidence that I have not also, unknowingly, represented "
        "whatever this woman has actually been doing in your village "
        "these past two years.\""
    )},
    {"type": "body", "text": (
        "\"Then help me understand what you do know,\" Eze Amadi said. "
        "\"How quickly can your House resolve this to my satisfaction. "
        "Recall her. Answer for the men lost at that boundary. Show me "
        "that the honored partner sitting across from me still has "
        "some authority over the hand that acted without your "
        "knowledge.\""
    )},
    {"type": "body", "text": (
        "Chiazor's answer, when it came, arrived with the particular "
        "unsteadiness of a man realizing mid sentence that he was "
        "revealing more than he had intended to. \"It is already being "
        "resolved,\" he said. \"Not by me. My House does not leave a "
        "matter of this size in the hands of a regional scholar for "
        "long once it grows large enough to reach a throne's attention. "
        "Someone senior to Ebiere, someone I answer to directly, has "
        "already been travelling toward that region for some weeks "
        "now, to take the whole matter in hand personally.\""
    )},
    {"type": "body", "text": (
        "The chamber went very still. \"For some weeks,\" Eze Amadi "
        "repeated, each word measured and quiet. \"Before the ambush at "
        "the boundary. Before your own House's complaint reached me. "
        "Someone above the woman running an informant network in my "
        "own garrisoned village was already on the road before any of "
        "us here even knew there was a matter requiring that much "
        "attention.\""
    )},
    {"type": "body", "text": (
        "Chiazor did not answer that directly, which was, by now, its "
        "own kind of answer. Nkiruka leaned toward the king once the "
        "man had been escorted out under polite guard rather than "
        "arrest, her voice low. \"Whoever is coming was already coming "
        "before Effiong ever sold a single hour,\" she said. \"Before "
        "the scholar's request was even refused. This House did not "
        "send its most senior hand in response to a failure at the "
        "boundary. It sent that hand because it had already decided, "
        "long before the failure, that Idoro's matter had grown too "
        "large to leave to patience alone.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi rose and walked to the chamber's window, looking "
        "south toward a village he had never seen and a boy he had "
        "still never met, carrying, for the first time since this whole "
        "matter began, the uncomfortable understanding that his own "
        "throne's careful, measured pace had never once controlled the "
        "true timing of any of it. \"Then send to Osadebe at once,\" he "
        "said. \"Whoever this House is sending is very likely already "
        "close. I would rather Idoro learn that from us than discover "
        "it standing at their own boundary with no warning at all.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE WARNING OUTRUNS THE THREAT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The king's rider reached Idoro in four days rather than the "
        "usual nine, changing horses at every post along the river road "
        "rather than resting them, and Osadebe read the short, urgent "
        "message twice before he trusted himself to say its contents "
        "aloud to Chidebe and Amara both. \"Someone senior within the "
        "trading House is already travelling toward this region,\" he "
        "said. \"Has been for weeks, according to their own sponsor at "
        "court. Udo does not know exactly how close, only that we "
        "should assume closer than we would like.\""
    )},
    {"type": "body", "text": (
        "Chidebe's response was immediate and practical, the response "
        "of a man grateful, for once, to have a threat he could "
        "actually prepare for. \"Then we double the watch on every "
        "approach, not only the tree line,\" he said. \"Whoever this is, "
        "I would rather my men see them coming from the river road than "
        "learn of their arrival the way we learned of the last one, "
        "standing over a body in a field we thought we had two hours "
        "to call safe.\""
    )},
    {"type": "body", "text": (
        "Amara felt the news settle over her with a colder weight than "
        "either officer's practical response seemed to carry, a "
        "mother's arithmetic running ahead of a captain's. \"Ebiere "
        "watched for weeks before she found her opening,\" she said. "
        "\"If someone above her has been traveling for weeks already, "
        "she was never the House's true ambition here. She was only "
        "ever the one sent first to learn the ground well enough that "
        "whoever came after her would not need to spend a single day "
        "guessing.\""
    )},
    {"type": "body", "text": (
        "In Oso, the entity had felt something shift at the very edges "
        "of its ordinary awareness two nights before Osadebe's rider "
        "ever arrived, a texture in the ambient dread reaching it from "
        "far beyond Idoro's fields that did not match any fear it had "
        "learned to recognize as belonging to the village, the crown, "
        "or the presence beyond its own borders. It had said nothing to "
        "Chibundu at the time, uncertain, and found itself, hearing the "
        "rider's message relayed secondhand through Amara's own unease, "
        "wishing now that it had trusted the boy with the uncertainty "
        "rather than waiting for it to resolve into something more "
        "definite."
    )},
    {"type": "body", "text": (
        "\"You felt something and did not tell me,\" Chibundu said, "
        "when the entity finally admitted it, and there was no accusal "
        "in his voice, only a tired, familiar disappointment that "
        "landed harder for how gently he said it. \"We agreed we were "
        "trying to give each other fewer half truths, not more "
        "carefully timed ones.\""
    )},
    {"type": "body", "text": (
        "\"You are right to hold me to that,\" the entity said, and "
        "meant it without the old instinct to soften the admission "
        "further. \"I felt something I could not yet name, and I chose "
        "silence rather than an uncertain warning, telling myself that "
        "was caution rather than the same old habit wearing a gentler "
        "excuse. Whatever comes toward this boundary next, I promise "
        "you will hear every uncertain thing I feel about it, named or "
        "not, as soon as I feel it.\""
    )},
    {"type": "body", "text": (
        "Chibundu accepted the promise with the same careful weight he "
        "now gave most things the entity offered him, neither fully "
        "trusting nor fully doubting it, and turned his attention back "
        "toward the tree line, toward a road neither of them could see "
        "yet but both of them now understood was already carrying "
        "someone this whole season had been quietly building toward "
        "meeting."
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
    print("  THE DARK RISE — Episode 55: \"The Honored Guest\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_55.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_55.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
