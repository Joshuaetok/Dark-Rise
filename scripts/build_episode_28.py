#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 28: "The Second Sign"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-04: Episode 28 brings Idoro's formal message to Udo,
arriving at Ikwuano's door as exactly the second sign Eze Amadi told him
to watch for in Episode 24. Rather than file it away with the rest of
the kingdom's small strange stories, Ikwuano brings it directly to the
king himself, as instructed. Eze Amadi, faced now with a village that has
lost its diviner, its law enforcer, and its self appointed successor in
the span of a single season, decides the report has crossed from
provincial curiosity into something worth a trained eye. He appoints
Osadebe, a quiet, capable captain of his personal service, to travel to
the Oji Delta and learn the truth of Idoro before the crown commits to
anything larger. In Oso, life continues entirely unaware that the
kingdom has finally decided to look south. The episode ends with Osadebe
setting out on the road, carrying instructions that reveal, more than
anything he has been told outright, how uncertain the king himself
remains about what is actually waiting for his captain at the end of it.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_28.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Eight"},
    {"type": "title_ep_name", "text": "The Second Sign"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: UDO — WHAT IKWUANO CARRIED WITHOUT WAITING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The message from Idoro reached Ikwuano's quiet room eleven "
        "days after the council sent it, delayed by rain that had "
        "swollen the river road into something barely passable, and he "
        "read it twice through before he allowed himself to feel the "
        "particular satisfaction of a man whose patience has finally "
        "been rewarded."
    )},
    {"type": "body", "text": (
        "A dibia dead in front of the whole village. An elder disgraced "
        "and stripped of her authority. A second man risen to fill her "
        "place and fallen from it within a season, having cost the "
        "village a life in the attempt. Idoro's own council, out of "
        "options, asking the crown directly for guidance it had never "
        "once needed to ask for before."
    )},
    {"type": "body", "text": (
        "This was not a clerk's kind of report. Ikwuano did not sit on "
        "it, did not fold it into a longer list of smaller troubles the "
        "way he had folded the first one. He carried it straight to the "
        "palace himself, exactly as he had been instructed."
    )},
    {"type": "body", "text": (
        "He spent the walk from his quiet room to the palace gates "
        "turning the message over once more, comparing it against the "
        "thin scroll he had already built on the Oji Delta, adding "
        "detail to detail the way he had built every genuine file in "
        "his twenty years of service, patiently, until the shape of "
        "something worth a king's real attention finally became "
        "impossible to mistake for anything smaller. He had learned, "
        "across those same twenty years, that the reports which turned "
        "out to matter most rarely announced themselves loudly at "
        "first. They arrived quietly, in pieces, and only revealed "
        "their true size once enough pieces had gathered in the same "
        "hand to be counted together."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Eze Amadi read the message standing, which was, Ikwuano had "
        "learned across twenty years of service, always a worse sign "
        "than the king reading anything seated."
    )},
    {"type": "body", "text": (
        "\"Three authorities lost in a single season,\" the king said "
        "slowly. \"In a village of that size, that is not misfortune. "
        "That is a pattern finishing what the first report only began "
        "describing.\""
    )},
    {"type": "body", "text": (
        "\"That was my reading as well,\" Ikwuano said. \"I did not "
        "wish to be the one to reach it first, given how the last "
        "report was received.\""
    )},
    {"type": "body", "text": (
        "\"You were right to bring it exactly as I asked,\" Eze Amadi "
        "said. \"I have spent eleven days since that first report "
        "telling myself I imagined the weight of it. I no longer have "
        "that comfort available to me.\""
    )},
    {"type": "body", "text": (
        "He set the message down on the low table beside him and stood "
        "a while longer in silence, the particular stillness of a ruler "
        "weighing a decision that would cost something no matter which "
        "way he turned it. \"If I send soldiers, I announce to my own "
        "court that I believe a spirit story from a delta village "
        "important enough to warrant them, and I invite every rival "
        "with an interest in my judgment to whisper about it for a "
        "season. If I send no one, and this pattern is real, I have "
        "chosen comfort over the lives of people who have already lost "
        "three leaders trying to manage it alone.\""
    )},
    {"type": "body", "text": (
        "\"There is a third path,\" Ikwuano said carefully. \"Send one "
        "man. Quiet. Capable of judging the truth of a thing without "
        "needing an army at his back to feel safe doing it. If he finds "
        "nothing, you have spent almost nothing to learn it. If he "
        "finds something, you will at least know its shape before you "
        "decide how heavily to answer it.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi considered this for a long moment, and something in "
        "his face suggested he had already been leaning toward exactly "
        "this answer before Ikwuano ever offered it, the way a king "
        "often needs to hear his own private conclusion spoken aloud by "
        "someone else before he can fully trust it as a decision rather "
        "than a fear."
    )},
    {"type": "body", "text": (
        "\"Send for Osadebe,\" he said. \"Quietly. I do not want this "
        "discussed beyond this room until he is already on the road, "
        "well past anyone at court who might think to talk him out of "
        "going, or worse, ride ahead of him with warning.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT REMAINED ENTIRELY UNAWARE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A hundred miles south, beneath the iroko roots, the entity "
        "spent that same morning exactly the way it had spent every "
        "morning since the dibia's death, tending the one thread that "
        "still mattered to it more than any question of thrones or "
        "councils or distant kings finally choosing to look toward a "
        "delta they had never once troubled themselves over before."
    )},
    {"type": "body", "text": (
        "The vessel had begun, in these last quiet days, sorting his "
        "small collection of found objects into an order only he "
        "seemed to understand, the smooth stone from the root wall "
        "placed always at the center, smaller stones and broken bits of "
        "bark arranged around it in patterns that shifted slightly each "
        "time he returned to them, an early, wordless kind of thinking "
        "the entity found itself watching with something closer to "
        "genuine curiosity than mere supervision."
    )},
    {"type": "body", "text": (
        "It did not yet know, and would not have cared greatly even if "
        "it had known, that a captain of the crown's own service was, "
        "at that same hour, being summoned to a private audience a "
        "hundred miles north to receive instructions that would "
        "eventually carry him within sight of these very roots. Its "
        "patience had outlasted kingdoms once already, in the centuries "
        "before this one. It saw no reason yet to believe this kingdom "
        "would prove any more urgent a concern than the others had "
        "been."
    )},
    {"type": "body", "text": (
        "It had watched, across three centuries, empires rise along "
        "this river and empires quietly recede from it again, borders "
        "redrawn, thrones inherited and lost, every one of those "
        "changes arriving at the edge of Oso eventually as nothing more "
        "than a faint, secondhand tremor in the ambient fear it fed on, "
        "never once as a direct threat requiring its attention. It had "
        "no reason yet to believe this particular king's curiosity "
        "would prove any different, and every reason, drawn from three "
        "hundred years of evidence, to expect that whatever Idoro had "
        "just set in motion would arrive far too slowly and far too "
        "gently to matter before the entity had already finished "
        "whatever it intended to finish."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "EXTERNAL AWARENESS: UNCHANGED, NONE. VESSEL: SELF DIRECTED ORGANIZATION OF PHYSICAL OBJECTS, EARLY SYMBOLIC BEHAVIOR OBSERVED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: UDO — WHAT OSADEBE WAS TOLD, AND NOT TOLD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe had served the crown for twelve years, long enough to "
        "have stopped being surprised by most of what a private summons "
        "to the king's own chamber could mean, and stood at attention "
        "while Eze Amadi laid the whole strange shape of Idoro's report "
        "out before him without softening a single detail."
    )},
    {"type": "body", "text": (
        "\"I want the truth of this village,\" the king said. \"Not the "
        "story it tells itself, and not the story its fear has already "
        "shaped for it. Go, watch, ask careful questions of careful "
        "people, and bring back only what you can stand behind with "
        "your own eyes as witness, nothing borrowed secondhand from "
        "frightened tongues eager to tell you whatever they believe you "
        "wish to hear.\""
    )},
    {"type": "body", "text": (
        "Osadebe listened without interrupting, the particular "
        "stillness of a man who had learned long ago that a soldier who "
        "spoke too soon in front of a king rarely got the chance to "
        "speak twice. He was neither young nor old, built more like a "
        "man who had spent his years walking long distances than "
        "fighting short violent ones, and Eze Amadi had chosen him for "
        "precisely that reputation, a captain who investigated before "
        "he ever drew a blade."
    )},
    {"type": "body", "text": (
        "\"And if what I find matches the story rather than "
        "contradicting it,\" Osadebe asked, choosing the question "
        "carefully, the way a soldier learns to choose every question "
        "he asks a king."
    )},
    {"type": "body", "text": (
        "Eze Amadi was quiet for a long moment, and something old and "
        "half buried moved behind his eyes, the same shadow Ikwuano had "
        "noticed cross his face during the first report, weeks earlier."
    )},
    {"type": "body", "text": (
        "\"Then you will have found something I hoped, without "
        "entirely admitting it to myself, that we would not need to "
        "find,\" the king said. \"Go carefully, Osadebe. Do not let "
        "superstition cloud what you report to me. But do not let your "
        "own certainty that such things cannot be real blind you to "
        "what is standing directly in front of you, either. I have "
        "learned, these last weeks, that both mistakes are equally "
        "easy to make.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Osadebe left within the day, a small, unremarkable party of "
        "no more than four men riding south along the same river road "
        "Nduka had once carried a trader's story down, deliberately "
        "modest so as to draw no more attention than a routine tax "
        "circuit might, and told himself, the way any careful man tells "
        "himself before a task he does not yet understand the size of, "
        "that he was riding toward nothing more than a frightened "
        "village and an overworked imagination."
    )},
    {"type": "body", "text": (
        "He did not yet know how completely the king's last warning "
        "would come to matter, or how little his own careful certainty "
        "would end up preparing him for whatever was actually waiting "
        "at the end of that road."
    )},
    {"type": "body", "text": (
        "Behind him, Udo settled back into its ordinary business, "
        "traders and treaties and the slow, patient management of a "
        "kingdom's thousand smaller concerns, entirely unaware that one "
        "quiet captain now carried, in a single small satchel of "
        "instructions, the first thread the crown had ever spun toward "
        "the ancient, hungry thing waiting patiently at the edge of a "
        "forest most of the court could not have found on a map."
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
    print("  THE DARK RISE — Episode 28: \"The Second Sign\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_28.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_28.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
