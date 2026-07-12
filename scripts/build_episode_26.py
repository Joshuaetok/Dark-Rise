#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 26: "The Toll"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-02: Episode 26 delivers the disaster Episode 25 built
toward. The entity, having decided to spend the dibia's thread as an
unforgettable lesson rather than preserve it, speaks through his dying
body one final time in front of the entire gathered village, delivers a
message aimed squarely at Ozoemena, and then uses the dibia's body to
strike him down before the thread finally, permanently, goes silent. The
dibia dies in front of the crowd he served for decades, the first named
adjacent casualty of this long crisis, and Ozoemena is left visibly,
physically marked by his own overreach. In Oso, the entity reviews the
outcome with cold satisfaction, treating the death as the closing of an
account long overdue rather than a loss. The episode ends with Idoro
staring at a dead man and a wounded leader, understanding, all at once,
that fear born of overconfidence had just cost them something no rite of
Elder Maka's ever had: a life.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_26.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Six"},
    {"type": "title_ep_name", "text": "The Toll"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE DIBIA SAID LAST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The dibia's convulsion did not break the way it had broken "
        "during the cleansing rite months earlier, into a scream and "
        "then a slump and then silence. It rose instead, steady and "
        "terrible, until the sound tearing out of his throat resolved "
        "itself into words that were unmistakably not his own."
    )},
    {"type": "body", "text": (
        "\"You wished to prove yourself against a door you do not "
        "understand,\" the voice said, using the dibia's ruined body "
        "the way a hand uses a glove it no longer intends to return. "
        "\"I will not waste the lesson on half measures the way the "
        "last one did.\""
    )},
    {"type": "body", "text": (
        "The two men holding the dibia upright staggered as his body "
        "arched further than a spine should have been able to bend, and "
        "let go, stumbling backward, unwilling to keep their hands on "
        "something that no longer felt like a man at all."
    )},
    {"type": "body", "text": (
        "The fire beside them guttered low and strange, the flames "
        "bending sideways though no wind moved through the gathered "
        "crowd, and somewhere near the back a child began crying, "
        "sharp and frightened, the sound of someone too young to "
        "understand what was happening but old enough to feel the fear "
        "spreading through every adult body pressed close around them."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Ozoemena froze where he stood, the scrap of borrowed words "
        "still clutched forgotten in one hand, and for one long moment "
        "the entire crowd watched him fail to move at all, the "
        "certainty that had carried him past a whole frightened council "
        "nowhere to be found in his face."
    )},
    {"type": "body", "text": (
        "\"This body has carried me faithfully for a very long while,\" the "
        "voice continued, almost gentle now, which somehow made it "
        "worse. \"It has grown too thin and too tired to carry much "
        "longer regardless of what any of you attempt tonight. I only "
        "regret that you will remember tonight as the reason, rather "
        "than simply the occasion.\""
    )},
    {"type": "body", "text": (
        "Amara, near the front of the crowd, felt Obi's hand close hard "
        "around her arm, both of them understanding, in the same "
        "terrible instant, that whatever restraint the entity had shown "
        "in every prior encounter, that restraint had just been spent "
        "in full. This was not a warning shaped to frighten without "
        "harming. This was something else entirely, something that had "
        "decided the cost of harm was worth whatever it purchased."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The dibia's body lunged before anyone in the crowd understood "
        "it was capable of lunging, closing the distance to Ozoemena "
        "faster than an old, wasted man's legs should have carried him, "
        "and struck him once across the face and chest with a strength "
        "that sent him sprawling into the dirt, gasping, a thin line of "
        "blood already welling at his temple."
    )},
    {"type": "body", "text": (
        "Then the dibia collapsed where he stood, all at once, the way "
        "a rope goes slack the instant the weight it was holding is "
        "finally released, and did not move again. A wasted, worn body "
        "that had carried this village's fear on its own tired back for "
        "years finally set the weight down for good."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY COUNTED AS PAID IN FULL
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the thread go dark "
        "the instant the dibia's body stopped, a small, final "
        "extinguishing it registered with the same flat attention it "
        "gave every other closed account across three centuries of "
        "closing them."
    )},
    {"type": "body", "text": (
        "The dibia had served it longer and more completely than any "
        "other thread it had ever built, carrying the very first words "
        "it had spoken to Amara, bearing the strain of that service "
        "until his own hair had gone white and his body had worn down "
        "to almost nothing beneath it. There was no ceremony in the "
        "entity's accounting for that service now that it had ended. A "
        "tool spent past its use was simply a tool set down, however "
        "long it had been carried."
    )},
    {"type": "body", "text": (
        "It found the outcome fully worth what little it had spent to "
        "produce it. A death, witnessed by the whole of Idoro at once, "
        "delivered at the exact moment its new leader had gambled his "
        "authority on understanding a danger he plainly did not, would "
        "teach this village a lesson far more durable than any rumor "
        "or private warning ever could have. Fear built on a corpse "
        "outlasted fear built on a story every time."
    )},
    {"type": "body", "text": (
        "It considered, turning the dibia's long service over one "
        "final time, whether it owed the thread anything beyond the "
        "flat accounting it had just performed. Three centuries of "
        "watching mortal things end had taught it that grief was a "
        "luxury built for creatures who expected their attachments to "
        "outlast a single lifetime. It did not expect that, had never "
        "expected it, and found no reason tonight to begin expecting it "
        "now, however long the thread had served."
    )},
    {"type": "body", "text": (
        "And yet it lingered a moment longer than the accounting "
        "strictly required, turning the dibia's final years over once "
        "more, the fear he had carried without ever once breaking "
        "entirely, the single sentence he had managed to gasp free "
        "during the cleansing rite despite everything holding his voice "
        "down. It had cost the man everything he had. The entity noted, "
        "somewhere beneath its own flat arithmetic, that this was not "
        "nothing, even if it changed nothing about what came next."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel had gone rigid at the exact moment "
        "the thread closed, some new, unbidden awareness in him "
        "flinching at a death he had no words yet to name, and the "
        "entity, feeling that flinch ripple through its own careful "
        "shaping of him, found itself once again facing the same "
        "unanswered question it had been circling since the boy's first "
        "unshaped word: how much of what grew in him was still entirely "
        "its own to direct."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It would not be the last account this crisis closed before it "
        "was finished. The entity had learned long ago that a lesson "
        "this expensive rarely stayed contained to the single household "
        "or the single body it was spent on."
    )},

    {"type": "system", "text": "DIBIA THREAD: TERMINATED. OBJECTIVE ACHIEVED: MAXIMUM MEMORABLE YIELD. VESSEL: UNPROMPTED EMOTIONAL RESPONSE TO HOST DEATH, ORIGIN UNCLEAR."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT THE CROWD UNDERSTOOD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "No one moved for a long, terrible moment after the dibia fell "
        "still, the whole crowd held in the particular paralysis of "
        "people who have just watched something happen that their minds "
        "have not yet agreed to believe."
    )},
    {"type": "body", "text": (
        "Amara reached Ozoemena before his own followers did, some old "
        "instinct from her years tending Kene through fevers moving her "
        "forward before her fear had finished catching up with her. The "
        "cut at his temple was shallow but bleeding freely, and his eyes, "
        "when they finally focused on her, held none of the certainty "
        "she had grown so used to seeing there."
    )},
    {"type": "body", "text": (
        "\"I told you,\" she said, quietly, not unkindly, pressing a "
        "fold of cloth against the wound. \"I did not want to be right "
        "about this.\""
    )},
    {"type": "body", "text": (
        "Ozoemena did not answer at first, his eyes fixed on the "
        "dibia's still body a few feet away, and when he finally spoke "
        "his voice had none of the certainty that had carried him "
        "through every gathering since Elder Maka's fall. \"I did not "
        "think it would answer at all,\" he said. \"I thought, if "
        "anything, it would simply fail to come, the way half the old "
        "rites fail when the one performing them does not fully believe "
        "in them.\""
    )},
    {"type": "body", "text": (
        "\"You believed enough to gather half the village to watch,\" "
        "Amara said. \"Whatever doubt you are only discovering now "
        "would have served you and this whole village far better a "
        "week ago, before it cost anyone their life.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Behind her, the crowd's silence was already breaking apart "
        "into something sharper, a woman weeping openly for the man who "
        "had once helped deliver two of her own children, an old man "
        "muttering that this was worse, far worse, than anything Elder "
        "Maka had ever brought down on the village in thirty and four "
        "years of harsh judgment. Elder Maka had broken a woman's "
        "authority in a single public morning. Ozoemena, in less than "
        "two weeks of holding power he had never earned the knowledge "
        "to wield safely, had broken a man's life entirely."
    )},
    {"type": "body", "text": (
        "\"He is dead,\" one of Ozoemena's own young followers said, "
        "staring down at the dibia's still body as though the fact of it "
        "had only just finished arriving in him. \"You told us this "
        "would prove something. It only proved we should have listened "
        "when we were warned.\""
    )},
    {"type": "body", "text": (
        "The same young man who had voiced his doubt in Amara's yard "
        "days earlier stepped back from Ozoemena's side entirely now, "
        "putting distance between himself and the man he had followed "
        "into this disaster, and two others drifted after him, the "
        "small following Ozoemena had gathered in less than a week "
        "already beginning to come apart in front of everyone watching."
    )},
    {"type": "body", "text": (
        "Ozoemena said nothing, blood still running from the cut Amara "
        "pressed against, and for the first time since he had risen to "
        "fill the space Elder Maka's fall had left behind, Idoro looked "
        "at him the way it had once looked at her: not with the "
        "certainty of a village trusting its own protector, but with the "
        "cold, measuring silence of a village beginning to count exactly "
        "what his protection had already cost it."
    )},
    {"type": "body", "text": (
        "Someone eventually came forward to cover the dibia's body with "
        "a length of cloth, and someone else began the low, mournful "
        "sound that would carry through Idoro for the rest of the night "
        "and into the funeral rites to come, but no one moved to comfort "
        "Ozoemena where he sat bleeding in the dirt, and Amara, still "
        "kneeling beside him with the cloth pressed to his wound, "
        "understood that this particular silence would follow him far "
        "longer than the cut ever would."
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
    print("  THE DARK RISE — Episode 26: \"The Toll\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_26.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_26.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
