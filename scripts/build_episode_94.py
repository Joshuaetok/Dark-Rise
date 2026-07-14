#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 94: "The Crown's Reckoning"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-09: Episode 94 follows Osadebe's Episode 92 report to
Udo, where Eze Amadi's council absorbs the full picture for the first
time: an inside informant coerced through his own sister, Oso's
guardian breaking three centuries of restraint, and mounting evidence
that a trading House is operating directly against the crown's own
subjects. Nkiruka finds a troubling precedent in the crown's old
archive, a prior informant scandal in a border village that ended in
tragedy when the crown moved too slowly. Ejikeme, humbled since Episode
65, no longer argues for a survey of Idoro's land on trade grounds
alone but reframes it as protective mapping the crown owes a village
that has absorbed three seasons of danger largely alone. Eze Amadi
authorizes a formal crown investigation into trading House sabotage of
crown subjects, doubles Idoro's permanent garrison, and grants
Ejikeme's survey at last, overruling his own past caution now that the
danger has proven itself undeniable. The episode closes on Nkiruka's
private unease: the old precedent she found ends not with the crown
arriving in time, but with the record simply stopping, unfinished.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_94.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Four"},
    {"type": "title_ep_name", "text": "The Crown's Reckoning"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: WHAT THE REPORT CARRIED NORTH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe's report reached Udo carried by a rider who had barely "
        "stopped to sleep, and Eze Amadi's council convened within the "
        "hour of its arrival rather than waiting for the customary "
        "morning session, a break in protocol that told the assembled "
        "advisors more about the report's weight than any single line "
        "of it had yet been read aloud."
    )},
    {"type": "body", "text": (
        "Nkiruka read it first, as she always did, her trained eye "
        "moving fast over the careful, unsoftened language Osadebe had "
        "chosen, and went very still at the paragraph describing the "
        "entity's direct intervention. \"In three hundred years of "
        "records,\" she said, mostly to herself, \"I have never once "
        "read of Oso's guardian acting rather than merely warning. Not "
        "once.\""
    )},
    {"type": "body", "text": (
        "Ejikeme, seated near the door as he always positioned himself "
        "in council, found his own hands unsteady as the report was "
        "read aloud in full, remembering with fresh discomfort every "
        "argument he had once made about grain routes and river tolls "
        "while a village he had barely troubled to picture on a map "
        "absorbed danger of a size he had never once imagined possible."
    )},
    {"type": "body", "text": (
        "Eze Amadi took the report from her hands and read the same "
        "paragraph twice before setting it down. \"And the informant,\" "
        "he said. \"A crown soldier, coerced through his own sister, "
        "feeding movements to a hired killer for two seasons inside my "
        "own garrison.\" He looked around the gathered council. \"I want "
        "to know how many other villages under my protection carry a "
        "wound exactly like this one that no one has yet found reason "
        "to report.\""
    )},
    {"type": "body", "text": (
        "Nkiruka answered honestly rather than reassuringly, which was "
        "the only kind of answer Eze Amadi had ever truly wanted from "
        "her. \"I cannot tell you the number,\" she said. \"I can tell "
        "you that Idoro is the first village that has ever had the "
        "means to catch a leak this well hidden, because it is the only "
        "village under your crown that carries two old powers willing "
        "to notice on its behalf. Any other village suffering the same "
        "wound may simply not know it yet.\" The thought settled over "
        "the council with real weight, and no one moved to soften it."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE COUNCIL ARGUED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ejikeme spoke next, and spoke differently than he had at any "
        "council session since the boundary ambush first brought this "
        "danger to Udo's attention. \"I have asked twice for a survey of "
        "Idoro's land,\" he said, \"and both times I asked it as a man "
        "protecting the crown's trade interests. I ask a third time as "
        "something else now. That village has absorbed three seasons of "
        "danger largely on its own resources, and we do not even "
        "possess an honest map of the ground it is defending.\""
    )},
    {"type": "body", "text": (
        "\"You have changed your reasons,\" Nkiruka observed, not "
        "unkindly. Ejikeme did not deny it. \"I have watched a village "
        "nearly lose a child, then a soldier, then very nearly a "
        "guardian power itself, while I argued about grain routes and "
        "river tolls,\" he said. \"A man can be humbled by that without "
        "losing every practical thought he ever had. I still believe "
        "the crown needs that map. I no longer believe protecting trade "
        "is the only reason worth wanting it.\""
    )},
    {"type": "body", "text": (
        "Nkiruka pressed him gently, testing the sincerity of the "
        "change rather than doubting it outright. \"And if the survey "
        "finds ground worth exploiting alongside ground worth "
        "protecting,\" she said, \"will the crown be able to tell the "
        "difference once the surveyors are already standing on it.\" "
        "Ejikeme did not have a clean answer for that, and to his "
        "credit did not pretend to. \"I do not know,\" he admitted. \"I "
        "only know that refusing to look has protected no one so far, "
        "least of all Idoro.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi weighed the matter for a long moment, the whole "
        "council waiting on his answer with the particular stillness "
        "reserved for decisions that would outlast the meeting itself. "
        "\"There is a second matter beneath the first,\" he said "
        "finally. \"A trading House, operating inside my kingdom, has "
        "now coerced a crown soldier into sabotage. That is no longer a "
        "danger to one village. That is an act against the crown "
        "itself, and I will not treat it as anything smaller than that.\""
    )},
    {"type": "body", "text": (
        "He gave his decisions in the order he had weighed them, each "
        "one landing with the finality of a man who had already spent "
        "every doubt he intended to spend on the matter. A formal crown "
        "investigation into which trading House had sponsored the "
        "informant's coercion, with authority to examine ledgers and "
        "movements no House would otherwise open to scrutiny. A doubling "
        "of Idoro's permanent garrison, drawn from Udo's own reserves "
        "rather than requested piecemeal as danger arose. And, at last, "
        "Ejikeme's survey, granted not as a trade measure but as a "
        "crown obligation to a village that had earned better protection "
        "than distance and good luck had so far provided it."
    )},
    {"type": "body", "text": (
        "\"I refused this request twice because I judged the cost too "
        "high for a benefit I could not yet see clearly,\" Eze Amadi "
        "said, looking at Ejikeme. \"I was wrong to weigh it only in "
        "trade. I will not make that mistake again simply because this "
        "time the cost is easier to name.\""
    )},
    {"type": "body", "text": (
        "Nkiruka raised the one caution she felt duty bound to raise "
        "before the council dispersed to carry out its new decisions. "
        "\"A doubled garrison and a formal investigation will not stay "
        "quiet for long,\" she said. \"Whichever House sponsored this "
        "informant will learn the crown is looking, and a hunter who "
        "has already shown she prefers striking before she is fully "
        "ready may not wait for us to finish looking before she acts "
        "again.\" Eze Amadi accepted the warning without flinching from "
        "it. \"Then we move as quickly as the danger allows,\" he said, "
        "\"and we accept that moving at all carries a risk that standing "
        "still has already proven carries a worse one.\""
    )},
    {"type": "body", "text": (
        "The council session ended with assignments rather than further "
        "debate, Ejikeme dispatched to begin the survey's preparations "
        "within the week, Nkiruka tasked with quietly tracing every "
        "trading House with river access near Idoro's delta, and a "
        "formal writ drawn up authorizing the garrison's expansion under "
        "Chidebe's continued command. Eze Amadi kept Osadebe's original "
        "report on the table long after the others had filed out, "
        "reading its closing lines a third time in the emptied room."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE RECORD DID NOT FINISH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Nkiruka remained in the archive long after the council had "
        "dispersed to carry out its new decisions, chasing a memory the "
        "report had stirred loose, a dimly recalled account from deep in "
        "the crown's older records of a border village that had "
        "discovered, generations ago, a coerced informant inside its "
        "own watch."
    )},
    {"type": "body", "text": (
        "She began, as she always began, with the index her own hands "
        "had built across years of careful cataloguing, searching for "
        "any prior mention of a coerced informant inside a crown "
        "garrison, a category so specific she half expected to find "
        "nothing at all. The single entry that answered her search was "
        "older than she had guessed, its reference number belonging to "
        "a section of the archive she had not opened in a decade."
    )},
    {"type": "body", "text": (
        "She found it near midnight, in a section of the archive so "
        "rarely consulted its bindings had gone brittle, and read it "
        "twice to be certain she had understood it correctly the first "
        "time. The village had discovered its informant. It had moved, "
        "as Idoro had moved, to close the leak and set a trap of its "
        "own."
    )},
    {"type": "body", "text": (
        "The record did not describe what happened next. It simply "
        "stopped, mid account, the remaining pages of that section lost "
        "or deliberately removed sometime in the centuries since, "
        "leaving no resolution at all, neither triumph nor tragedy, only "
        "silence where an ending should have been."
    )},
    {"type": "body", "text": (
        "She checked the surrounding pages twice, hunting for a cross "
        "reference, a later addendum, anything a careful keeper might "
        "have added once the matter finally resolved, and found nothing "
        "of the kind anywhere in that section of the archive. Whatever "
        "had happened to that border village, no one afterward had "
        "thought it worth the ink to finish recording it, or someone had "
        "made certain it never got the chance."
    )},
    {"type": "body", "text": (
        "Nkiruka sat with that unfinished record for a long time before "
        "she allowed herself to close the book, turning over the "
        "uncomfortable possibility that a missing ending was not always "
        "an accident of poor archiving, and wondering, with a chill she "
        "did not share with anyone that night, whether Idoro's own "
        "account was being written toward a similar silence."
    )},
    {"type": "body", "text": (
        "She considered, briefly, carrying the discovery to Eze Amadi "
        "that same night, and set the thought aside until she had "
        "something more useful to offer him than an old fear with no "
        "shape to it yet. A king who had just committed a garrison, an "
        "investigation, and a survey to Idoro's defense did not need a "
        "keeper of records adding a nameless dread on top of decisions "
        "already made. He needed, when the time came, an answer she did "
        "not yet have."
    )},
    {"type": "body", "text": (
        "She closed the brittle old book carefully, marked the section "
        "for her own private return rather than the council's shared "
        "index, and sat a while longer in the archive's silence, "
        "listening to it the way she imagined a village listened for a "
        "danger it could not yet name, hoping this time the record would "
        "not simply stop before it was finished."
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
    print("  THE DARK RISE — Episode 94: \"The Crown's Reckoning\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_94.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_94.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
