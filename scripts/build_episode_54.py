#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 54: "Two Reports, One Morning"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-30: Episode 54 shifts the block's attention to Udo for
the first time since Episode 45's garrison orders. The trading House's
own formal envoy at court reaches Eze Amadi first, days ahead of
Osadebe's slower courier, with a preemptive account accusing the crown's
soldiers of an unprovoked attack on a peaceful surveying party at
Idoro's boundary. Ejikeme seizes the moment to argue for appeasement.
Nkiruka and Eze Amadi are not so easily moved, but the true blow lands
only once Osadebe's own report finally arrives days later, confirming
the ambush, Effiong's bribery, and Ebiere's name. Ikwuano, tasked with
tracing that name through the crown's own trade records, delivers the
episode's hook: the House's long trusted formal ambassador at Udo has
been sponsored, for years, by the same trading concern Ebiere answers
to, meaning the crown has been dealing in good faith with the very
House now moving against Idoro.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_54.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Four"},
    {"type": "title_ep_name", "text": "Two Reports, One Morning"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE FASTER COURIER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The complaint reached Udo six full days before Osadebe's own "
        "report could hope to arrive, carried by a courier who had "
        "clearly not spared his horses, and Eze Amadi understood, "
        "reading it once in the privacy of his own chamber before ever "
        "bringing it to council, exactly what that speed was meant to "
        "purchase. Whoever wrote it first would be believed first. "
        "Whoever was believed first would shape every conversation that "
        "followed."
    )},
    {"type": "body", "text": (
        "\"A peaceful surveying party,\" Ejikeme read aloud to the "
        "assembled council the next morning, his tone carefully "
        "neutral though his eyes lingered on the king rather than the "
        "page, \"set upon without warning or provocation by crown "
        "soldiers at the Idoro boundary, one man killed outright and "
        "others taken and held against their will. The House demands "
        "an accounting, the return of its men, and assurance that no "
        "further violence will be offered to lawful traders operating "
        "within the crown's own territory.\""
    )},
    {"type": "body", "text": (
        "\"Lawful traders do not carry blades toward an unarmed woman "
        "and a child,\" Nkiruka said before Ejikeme had fully lowered "
        "the page, her voice flat with a certainty that came from "
        "having read this exact pattern before in older records. \"Nor "
        "do lawful traders send five armed men through a boundary "
        "deliberately unguarded for a private family reunion, unless "
        "they had already been told, by someone, precisely when and "
        "where to find it undefended.\""
    )},
    {"type": "body", "text": (
        "Ejikeme did not concede the point directly. \"We do not yet "
        "have Captain Osadebe's own account to weigh against theirs,\" "
        "he said instead. \"Until it arrives, we have only accusation "
        "answering accusation, and a House whose tribute has kept two "
        "provinces solvent for a decade is not a party this crown can "
        "afford to insult on the strength of rumor alone. A measured "
        "apology, offered now, costs us little and buys considerable "
        "patience while the fuller truth makes its slower way north.\""
    )},
    {"type": "body", "text": (
        "\"An apology offered before the truth arrives is not "
        "measured,\" Eze Amadi said, quiet enough that the whole "
        "chamber stilled to hear the rest of it. \"It is a wager, and "
        "I have already told this council once that I will not decide "
        "matters concerning that village on convenience alone. I will "
        "answer their complaint with patience rather than apology. "
        "Patience costs us nothing yet. Apology, offered wrongly, could "
        "cost us everything Osadebe has spent a season learning to "
        "protect.\""
    )},
    {"type": "body", "text": (
        "Nkiruka lingered after the session was formally closed, "
        "waiting until only Ejikeme remained within easy hearing before "
        "she spoke again, her voice pitched lower now, less for the "
        "council's benefit than for his alone. \"You have spent years "
        "arguing that this House's tribute is worth protecting at "
        "nearly any cost,\" she said. \"I do not think you were wrong to "
        "value the roads and soldiers that tribute has bought this "
        "kingdom. I think you have simply never once asked yourself "
        "what a trading House patient enough to buy a village trader's "
        "silence for two years might also be patient enough to buy "
        "inside these walls.\""
    )},
    {"type": "body", "text": (
        "Ejikeme did not answer at once, and when he finally did, "
        "something in his usual careful confidence had visibly "
        "thinned. \"I have built my whole argument, every season I "
        "have served this council, on the belief that a House's coin "
        "makes it predictable,\" he said. \"Predictable people do not "
        "need to be feared, only managed correctly. I find I am "
        "considerably less certain this morning that predictable and "
        "patient were ever the same quality at all.\""
    )},
    {"type": "body", "text": (
        "\"They are not,\" Nkiruka said. \"Every account in this "
        "kingdom's old records describes a presence patient enough to "
        "wait three centuries for a single door to open. I had "
        "assumed, reading them, that such patience belonged only to "
        "old, half remembered powers older than any of us. I did not "
        "expect to find the same patience wearing a trading House's "
        "seal, sitting close enough to this throne to be invited to "
        "its own table.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE NAME IN THE LEDGER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe's report arrived six days later, exactly as the king "
        "had gambled it would, and it answered the House's complaint "
        "so thoroughly that even Ejikeme read it twice before setting "
        "it down. The ambush. Chibundu's restraint and the entity's "
        "single lethal strike. Effiong's confession. Uduak's two years "
        "of quiet selling. And, written plainly in Osadebe's own steady "
        "hand, the name the trader had given up before the guards led "
        "him away: Ebiere."
    )},
    {"type": "body", "text": (
        "\"Two years,\" Eze Amadi said, reading the line a second time "
        "himself. \"This House was buying information in that village "
        "before we had ever heard its name spoken in this chamber. Our "
        "own captain arrived believing he carried the crown's first "
        "real attention into Idoro. He carried, in truth, its second.\""
    )},
    {"type": "body", "text": (
        "He turned to Ikwuano, who had said little through the whole "
        "exchange, watching the way a careful man watches a fire he "
        "suspects is not yet finished spreading. \"Find that name in "
        "our own records,\" the king told him. \"Every House trading "
        "in this kingdom answers eventually to some sponsor known to "
        "this court. I want to know whose name sits above hers before "
        "I decide how loudly to answer their complaint.\""
    )},
    {"type": "body", "text": (
        "Ikwuano did not need the full day the king had allotted him. "
        "He returned before the council had even risen for its midday "
        "recess, a single ledger page in his hand and an expression "
        "Eze Amadi had learned, across sixteen years of reports, to "
        "read as genuinely troubled rather than merely cautious. \"I "
        "found her,\" he said. \"Not under that name. Under the name of "
        "the House itself, and the House's formal sponsor at this "
        "court, the same envoy who has dined at your own table three "
        "times this past year alone.\""
    )},
    {"type": "body", "text": (
        "The chamber went very still. Ejikeme's face, for once, showed "
        "something closer to genuine alarm than calculation. \"You are "
        "telling us,\" he said slowly, \"that the House complaining of "
        "unprovoked violence against its peaceful traders is the same "
        "House this crown has been treating as an honored trading "
        "partner for years. That the woman running an informant network "
        "in a village we ourselves garrisoned answers to a man who has "
        "sat at the king's own table.\""
    )},
    {"type": "body", "text": (
        "\"I am telling you exactly that,\" Ikwuano said. \"And I am "
        "telling you further that if this House has spent two years "
        "quietly buying a market trader's silence in a village none of "
        "us thought worth watching, I have no confidence at all that "
        "two years is the limit of their patience anywhere else in "
        "this kingdom, including inside these very walls.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi sat with that for a long moment, the weight of it "
        "settling over him the way Osadebe's report had settled over "
        "the whole council a breath before, another familiar shape "
        "revealing itself to be far larger underneath than its surface "
        "had ever let on. \"Then we have learned something else besides "
        "a village's danger,\" he said finally. \"We have learned we do "
        "not yet know how deep this House's roots run into our own "
        "ground, and I would rather discover the answer slowly and on "
        "my own terms than have it handed to me the way Idoro's was, in "
        "the middle of a night already gone wrong.\""
    )},
    {"type": "body", "text": (
        "He rose, ending the session before Ejikeme could offer another "
        "argument for patience of the wrong kind. \"Summon the "
        "sponsor,\" he told Ikwuano. \"Tell him only that his House's "
        "complaint requires clarification. Give him no reason yet to "
        "believe we know as much as we do. I would like, for once, to "
        "be the one holding the fuller account when two reports finally "
        "sit across the same table from each other.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: WHAT IDORO WAITED FOR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Idoro, Osadebe's own copy of the report he had sent north "
        "sat finished on his table for six more days before any word "
        "came back from Udo at all, and he found the waiting harder "
        "than writing the report itself had been. Amara asked him once, "
        "gently, whether silence from the crown meant good news or "
        "simply slower news, and he had no honest answer to give her "
        "beyond the truth: that a throne weighing a decision this large "
        "rarely moved quickly, and that the quiet itself was not proof "
        "of anything either way."
    )},
    {"type": "body", "text": (
        "Chidebe kept the garrison at its full strength through every "
        "one of those quiet days, unwilling to risk a second stand down "
        "on anyone's account until Udo told him plainly what trust, if "
        "any, this House had left to be extended. He drilled his men "
        "harder than the season strictly required, less out of "
        "necessity than out of a captain's private need to feel he was "
        "doing something while the true decision sat entirely outside "
        "his own reach. Effiong remained confined rather than freed, "
        "awaiting whatever judgment the crown would eventually send "
        "south along with its answer, a small, unresolved weight "
        "sitting alongside the much larger one the whole village now "
        "carried."
    )},
    {"type": "body", "text": (
        "Chibundu, told of the delay by the entity, asked the same "
        "question he had been asking in different shapes for weeks. "
        "\"Does the king know about me yet. Truly know, not only that "
        "something dangerous lives in Oso.\" The entity considered its "
        "answer carefully before giving it. \"He knows a name was "
        "spoken at a boundary,\" it said. \"Whether he understands yet "
        "what that name means for a boy who has done nothing but be "
        "born and try to survive it is a very different question, and "
        "one I suspect Udo itself has not finished answering for "
        "itself.\""
    )},
    {"type": "body", "text": (
        "Chibundu turned that answer over the way he now turned over "
        "most things the entity gave him without softening, weighing "
        "the plain difference between a name spoken and a person "
        "understood. \"Then whatever the king decides,\" he said, "
        "\"he will be deciding it about someone he has never met, on "
        "the word of people who have barely met me either. I do not "
        "know yet whether that should frighten me or simply remind me "
        "that I am not the only one in this waiting who does not yet "
        "know what is coming.\""
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
    print("  THE DARK RISE — Episode 54: \"Two Reports, One Morning\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_54.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_54.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
