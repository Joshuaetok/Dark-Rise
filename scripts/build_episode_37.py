#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 37: "The Dream Before the Word"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-13: Episode 37 brings Osadebe's report of the foreign
trading House to Udo, where Ejikeme, sidelined since Episode 31, sees an
opportunity rather than a threat: if the crown moves first to survey and
negotiate Idoro's land itself, it can secure tribute before an outside
House claims the ground unilaterally, framed as protecting the village
from worse. Eze Amadi is troubled by the shape of an argument that sounds
like protection but functions like a land grab, and defers a decision
rather than accept or refuse Ejikeme outright, keeping the moral question
open. In Oso, the entity questions the vessel carefully about the
untraceable word from Episode 35, trying to learn its source without
revealing its own unease, and discovers something worse than a stray
word: the boy describes a recurring dream of a cold, root laced dark he
has never been shown, a place the entity itself only just visited in
Episode 36. The episode ends on the entity's realization that whatever
answered its reach did not just hear it coming — it has been reaching the
boy directly, quietly, for longer than the entity has known to look.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_37.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Seven"},
    {"type": "title_ep_name", "text": "The Dream Before the Word"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: UDO — A DIFFERENT KIND OF APPETITE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ejikeme had waited a long while for a piece of news he could "
        "use, and when Osadebe's letter reached the council chamber "
        "describing a trading House's agent asking after Idoro's "
        "buried worth, he read it twice before anyone else in the room "
        "had finished it once, already turning the shape of an "
        "argument over in his mind the way a trader turns over a coin "
        "to check it is not counterfeit."
    )},
    {"type": "body", "text": (
        "\"This is not a threat to be feared,\" he told Eze Amadi, "
        "once the letter had been read aloud in full. \"It is a "
        "warning of a threat we can still get ahead of. If a House has "
        "already sent a man to look at Idoro's ground, others will "
        "follow before the season turns. Better the crown surveys that "
        "land first, on the crown's own terms, and sets whatever "
        "tribute is owed before a foreign House decides the terms for "
        "us.\""
    )},
    {"type": "body", "text": (
        "Nkiruka, seated near the back of the chamber where the "
        "keeper of old rites was rarely asked to speak on matters of "
        "trade, spoke anyway. \"I have read what happened to three "
        "other kingdoms that let foreign appetite decide the timing of "
        "their own decisions,\" she said. \"None of them regretted "
        "moving carefully. Several regretted moving at all. I would "
        "want to know a great deal more about what actually sits "
        "beneath that soil before I called any survey, crown ordered "
        "or otherwise, a small thing.\""
    )},
    {"type": "body", "text": (
        "Ejikeme inclined his head toward her politely without "
        "conceding a single point. \"I do not disagree that caution "
        "has its place. I am only observing that caution has a cost "
        "too, and that cost falls hardest on the people who cannot "
        "afford to wait and see which foreign House moves first.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Eze Amadi turned the proposal over slower than Ejikeme "
        "clearly wanted him to. \"You are describing this as "
        "protection,\" he said finally. \"Explain to me how it differs, "
        "in its actual shape, from simply taking Idoro's ground before "
        "someone else can. A survey ordered by the crown still ends "
        "with men digging into soil that village has never offered.\""
    )},
    {"type": "body", "text": (
        "\"It differs,\" Ejikeme said, \"in who profits, and in whether "
        "the people living on that ground still have a crown that "
        "answers to them afterward, or only a House that answers to "
        "no one. I am not asking you to take anything from Idoro that "
        "will not be taken regardless. I am asking you to decide "
        "whether it is taken by us, imperfectly, or by strangers, "
        "completely.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "It was, Eze Amadi thought, the most honest argument Ejikeme "
        "had ever made in this chamber, which somehow made it harder "
        "to dismiss than his usual careful evasions had ever been. He "
        "thought of Osadebe's own report from months earlier, of a "
        "village that had already lost a healer, an elder's authority, "
        "and a season's peace to a danger it had never asked for. He "
        "did not much like the idea of adding a survey crew to that "
        "same list of things Idoro never asked for, whatever careful "
        "language Ejikeme wrapped around it."
    )},
    {"type": "body", "text": (
        "\"I will not authorize a survey while a captain of mine still "
        "sits in that village learning whether its own dead are done "
        "rising,\" he said at last. \"But I will not pretend your "
        "argument has no weight either. Send nothing yet. Prepare "
        "everything. If the day comes that I decide Idoro's ground must "
        "be looked at, I would rather it be looked at by men who answer "
        "to me than men who answer to profit alone.\""
    )},
    {"type": "body", "text": (
        "Ejikeme bowed and left satisfied with half of what he had "
        "come for, which experience had taught him was usually enough "
        "to build the other half on later, while Eze Amadi sat alone "
        "afterward turning over a question that troubled him more than "
        "he had let show: how many decisions framed as protecting a "
        "village eventually looked, from that village's side of the "
        "river, exactly like the thing they claimed to be preventing."
    )},
    {"type": "body", "text": (
        "Ikwuano lingered after the others had gone, as he often did, "
        "content to be the last quiet presence in an emptying room. "
        "\"You did not refuse him,\" he observed, not quite a "
        "question. \"You did not accept him either,\" Eze Amadi "
        "answered, \"and I find I am no longer certain that leaving a "
        "decision unmade is the same mercy toward Idoro that it once "
        "felt like when it was only Osadebe's watching and reporting "
        "waiting on my word. A village can only be told to wait so "
        "many times before waiting itself becomes the harm.\""
    )},
    {"type": "body", "text": (
        "He thought again, as he had more than once since Nkiruka "
        "first warned him, of a grandmother's half remembered story "
        "about a marked child carried into a forbidden bush, and "
        "wondered whether every one of the three prior kingdoms in her "
        "old records had believed, right up until the moment they "
        "acted, that they still had time to decide carefully rather "
        "than decide at all."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE PLACE HE HAD ALREADY SEEN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity approached the boy with a "
        "gentleness it had to work harder than usual to sound "
        "unforced, asking him again, carefully, where the soft word "
        "from days before had come from, careful not to let its own "
        "unease bleed into a question it needed him to answer honestly "
        "rather than defensively."
    )},
    {"type": "body", "text": (
        "The boy considered it with the same unhurried patience he "
        "gave every question that actually interested him, turning a "
        "stone over twice before answering. \"I told you. It was "
        "already there.\" He paused, searching for something harder to "
        "say than the word itself had ever been. \"Like the cold place "
        "I keep going to when I sleep. I did not learn that either. I "
        "just go there.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The entity went very still, the particular stillness it had "
        "not needed to hide from him in weeks. \"Tell me about the cold "
        "place,\" it said, and heard, even in its own voice, an "
        "urgency it usually spent great care keeping out of anything "
        "it said to him."
    )},
    {"type": "body", "text": (
        "The boy described it plainly, the way he described anything "
        "he had not yet learned to be afraid of. Roots that were not "
        "the ak-pu roots, thicker and darker and older, tangled close "
        "enough to block out whatever light existed anywhere near that "
        "place. A silence that felt, he said, like something holding "
        "its breath on purpose. He went there most nights now, he told "
        "the entity, though he could never remember choosing to, and "
        "he always woke again before anything in the dark noticed him "
        "standing there."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Every detail matched the ground the entity had crossed two "
        "nights earlier and fled the instant something in it had "
        "cried out, matched closely enough that there was no comfort "
        "left in calling it coincidence. The entity had assumed, "
        "reaching out past its own borders for the first time in three "
        "centuries, that it was the one doing the discovering, a "
        "cautious visitor testing ground that had never before been "
        "walked."
    )},
    {"type": "body", "text": (
        "\"How long,\" it asked him, working to keep the question "
        "sounding like curiosity rather than the alarm actually moving "
        "through it, \"have you been going there.\""
    )},
    {"type": "body", "text": (
        "The boy shrugged, the small unconcerned gesture of a child "
        "asked to measure something he had never once thought "
        "required measuring. \"A long time,\" he said. \"Longer than "
        "the word. I think the word came from there too. I just did "
        "not know the two things were the same thing until you asked "
        "about the word and I remembered where I had actually heard "
        "it.\" He said it the way he said everything lately, without "
        "weight, without understanding yet that he had just told the "
        "entity its own careful season of teaching had been running "
        "alongside a second, older lesson it had never once been "
        "invited to observe."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The entity asked, as gently as it could shape the question, "
        "whether the cold place had ever frightened him. The boy "
        "thought about it with real seriousness this time, the same "
        "seriousness he had given the question of his own name. \"No,\" "
        "he said. \"It waits the way you wait. I did not know that was "
        "strange until just now, watching your face try not to look "
        "strange about it.\""
    )},
    {"type": "body", "text": (
        "VESSEL: RECURRING UNCONSCIOUS PRESENCE IN UNCLAIMED GROUND, "
        "ORIGIN AND DURATION UNKNOWN. NOT INITIATED OR DIRECTED BY "
        "ENTITY. FIRST INSTANCE PREDATES EPISODE THIRTY SIX CONTACT."
    )},
    {"type": "body", "text": (
        "It understood now, turning the boy's plain, unafraid "
        "description over against its own single startled encounter "
        "in that same dark, that it had not discovered anything at "
        "all. It had simply followed a path the boy had already been "
        "walking, unwitnessed and unclaimed, for longer than the "
        "entity had thought to look for it, into ground where "
        "something had clearly grown used enough to his presence to "
        "be startled, not by him, but by the entity trailing in "
        "behind him for the very first time."
    )},
    {"type": "body", "text": (
        "\"Does it feel like Mama's voice,\" the entity asked, choosing "
        "the only comparison it trusted him to answer honestly, \"or "
        "like mine.\""
    )},
    {"type": "body", "text": (
        "The boy thought about it longer than the entity wanted him "
        "to. \"Neither,\" he said finally, going back to his stones as "
        "though he had not just handed the entity the coldest answer "
        "it had received since it first claimed him. \"It does not "
        "talk yet. But I think it knows my name already. I think it "
        "has known it longer than you have.\""
    )},
    {"type": "body", "text": (
        "He said it plainly, without cruelty, the way a much older "
        "child might correct an adult on a small, harmless point of "
        "fact, and went on stacking his stones as though the sentence "
        "he had just spoken carried no more weight than the weather."
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
    print("  THE DARK RISE — Episode 37: \"The Dream Before the Word\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_37.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_37.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
