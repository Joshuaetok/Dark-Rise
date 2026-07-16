#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 24: "The Report"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-31: Episode 24 follows the river agent, named here for the
first time as Nduka, on the final leg of his journey to Udo, where he
delivers his report not to the throne directly but to Ikwuano, keeper of
the crown's scattered intelligence along the trade roads, whose daily
work is deciding which of a hundred small strange stories are worth a
king's attention. Ikwuano judges the pattern in Nduka's report, a voice
speaking through two different mouths weeks apart, breaking a village
matriarch's authority in a single morning, unusual enough to carry
forward. Eze Amadi, introduced here for the first time on page, hears it
amid a dozen other petty provincial matters, weary and pragmatic, and
very nearly dismisses it before an old, half remembered piece of his own
family's history gives him pause. He earmarks it for a quiet follow up
rather than immediate action, unaware of how much more than a province's
worth of superstition is actually stirring in the Oji Delta.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_24.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Four"},
    {"type": "title_ep_name", "text": "The Report"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE RIVER ROAD — WHAT NDUKA CARRIED TO UDO
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Udo announced itself long before its walls did, the river "
        "road thickening with traffic the closer it drew to the "
        "capital, carts and cattle and traders all funneling toward the "
        "same gates Nduka had passed through a dozen times before "
        "without ever once carrying a report he thought worth losing "
        "sleep over."
    )},
    {"type": "body", "text": (
        "This one had cost him sleep for three nights running."
    )},
    {"type": "body", "text": (
        "Udo itself was larger than any three villages Nduka had ever "
        "passed through combined, its market sprawling in every "
        "direction from the palace walls like roots spreading from a "
        "trunk too broad for any one man to put his arms around. Traders "
        "here spoke of grain prices and bride wealth and the coming "
        "planting season, ordinary concerns for ordinary lives, entirely "
        "unaware that a hundred miles south a village had spent a single "
        "morning tearing apart the woman who ruled it. Nduka found the "
        "distance between those two worlds unsettling in a way he could "
        "not quite name, the way it always unsettled him to carry "
        "something heavy into a place too busy to notice the weight of "
        "it."
    )},
    {"type": "body", "text": (
        "He did not go to the palace itself. Men of his standing did "
        "not simply walk up to a throne and speak. He went instead to a "
        "modest compound near the eastern market, where a quiet, "
        "unhurried man named Ikwuano kept a room full of scrolls no one "
        "outside the palace's inner circle knew existed, each one a "
        "small strange thread gathered from somewhere along the "
        "kingdom's edges and sorted, patiently, into what mattered and "
        "what did not."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Ikwuano listened to the whole of Nduka's report without "
        "interrupting once, a habit that had served him well across "
        "twenty years of separating a kingdom's genuine dangers from its "
        "endless supply of frightened village gossip, and when Nduka "
        "finished, he sat turning the details over with the same care "
        "he gave to reports of unrest or unpaid tribute."
    )},
    {"type": "body", "text": (
        "\"A voice, twice, in two different mouths,\" Ikwuano said. "
        "\"Weeks apart. The first time through a healer, saying only "
        "one word. The second time through a midwife, breaking an "
        "elder who had ruled unquestioned for thirty and four years.\""
    )},
    {"type": "body", "text": (
        "\"That is the whole of it,\" Nduka said. \"I have heard a "
        "hundred curses blamed for a hundred droughts on that road. I "
        "have never heard the same voice claimed twice, in two "
        "different bodies, weeks apart, by people who had no reason to "
        "agree on their story beforehand.\""
    )},
    {"type": "body", "text": (
        "\"No,\" Ikwuano agreed slowly. \"That is not the usual shape "
        "of a village's fear. That is the shape of a pattern.\""
    )},
    {"type": "body", "text": (
        "He rose and crossed to the shelves lining the far wall, where "
        "scrolls sat sorted by province in a system only he fully "
        "understood, and found the thin, mostly empty roll that "
        "represented everything the crown had ever bothered to record "
        "about the Oji Delta. It held almost nothing. A handful of tax "
        "notations. A brief mention, two generations old, of a dispute "
        "over fishing rights along the river's mouth. Nothing that had "
        "ever once suggested the delta held anything worth a careful "
        "man's attention."
    )},
    {"type": "body", "text": (
        "\"Tell me about the village itself,\" Ikwuano said. \"Not the "
        "voice. The place. How large. How it feeds itself. Who leads it "
        "now that this Elder Maka no longer can. Voices come and go in "
        "every frightened province I have ever recorded. What I want to "
        "know is whether the ground beneath the voice is stable enough "
        "to still be standing if the crown ever needs it to be.\""
    )},
    {"type": "body", "text": (
        "Nduka told him what little he knew, gathered secondhand from "
        "traders who had passed through more recently than he had, of a "
        "loud, ambitious man named Ozoemena filling the space Elder "
        "Maka had left, of a household marked by rumor that the new "
        "leader seemed determined to test. Ikwuano listened to all of "
        "it with the same unhurried care, adding each detail to the "
        "thin scroll in a careful hand, building, thread by thread, "
        "the first real record the crown had ever kept of a village "
        "most of Udo had never once had reason to name aloud."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT NEITHER OF THEM COULD YET IMAGINE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A hundred miles south, in the delta neither Nduka nor Ikwuano "
        "had ever set foot in themselves, the entity beneath the "
        "iroko roots had no awareness at all that its name, or the "
        "absence of one, had just been spoken for the first time inside "
        "a room within sight of the throne of Ijendu."
    )},
    {"type": "body", "text": (
        "It would not have cared, had it known. Udo was a word without "
        "weight to something that measured its patience in centuries "
        "rather than seasons, a kingdom's throne no more urgent to it "
        "than a single villager's frightened whisper. It had learned, "
        "across three hundred years, that human power moved slowly even "
        "when it moved at all, and that whatever attention a delta "
        "village's unrest eventually earned from a distant capital would "
        "arrive long after the entity had finished whatever it meant to "
        "finish."
    )},
    {"type": "body", "text": (
        "In the hollow, the boy slept off the exhaustion of his first "
        "real tears, small and still and utterly unaware that two men "
        "in a room a hundred miles away had just spent an hour deciding "
        "whether his existence was worth a king's passing attention."
    )},
    {"type": "body", "text": (
        "The entity turned the greater share of its attention, as it "
        "always did in the quiet hours, to the slow work of shaping the "
        "vessel rather than to any question of what distant men in a "
        "distant capital might eventually decide to do about a village "
        "they had never seen. Three centuries of patience had taught it "
        "which threats deserved urgency and which deserved only "
        "watching. A king's idle curiosity, filtered through a "
        "cautious servant's careful hand, belonged, for now, entirely "
        "to the second category."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "EXTERNAL AWARENESS: NONE. RISK ASSESSMENT: NEGLIGIBLE, DISTANT HUMAN AUTHORITY MOVES SLOWLY."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: UDO — WHAT THE EZE ALMOST DISMISSED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ikwuano carried the report to Eze Amadi three days later, "
        "folded into a longer list of the kingdom's smaller troubles, a "
        "disputed well in one province, a tax dispute in another, a "
        "delta village called Idoro where an old law enforcer had "
        "apparently been ruined by a voice speaking through two "
        "different mouths."
    )},
    {"type": "body", "text": (
        "Eze Amadi was a broad shouldered man made heavier by years of "
        "sitting through exactly this kind of morning, listening to a "
        "kingdom's worth of small emergencies with the particular "
        "weariness of a ruler who had long ago learned that most "
        "emergencies solved themselves before he ever needed to spend "
        "real attention on them."
    )},
    {"type": "body", "text": (
        "\"A voice through two mouths,\" he repeated, only half "
        "listening, already reaching for the next scroll in the "
        "morning's pile. \"Every province in this kingdom has a story "
        "like that once a season. Spirits, curses, an abiku come back "
        "wrong. It is what frightened people tell each other instead of "
        "admitting a sickness has no explanation they can bear to sit "
        "with.\""
    )},
    {"type": "body", "text": (
        "\"Perhaps,\" Ikwuano said, and did not press further, because "
        "twenty years of service had taught him exactly how far to push "
        "a tired king before the pushing cost him more than the report "
        "was worth."
    )},
    {"type": "body", "text": (
        "He had learned, across those same twenty years, that the "
        "surest way to lose a king's trust was to insist too hard on "
        "any single report among the dozens that crossed this chamber "
        "every week. Better to plant a small seed and let it find its "
        "own room to grow, the way he had planted a hundred smaller "
        "seeds before this one, most of which had come to nothing, a "
        "handful of which had eventually mattered more than anyone in "
        "this room could have guessed on the morning they were first "
        "spoken aloud."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Eze Amadi's hand paused over the next scroll, and something "
        "old and half buried stirred behind his eyes, a memory of his "
        "own grandmother's voice, decades gone now, telling a much "
        "younger version of him a story about a childhood friend's "
        "brother, a marked child once carried into a forbidden bush and "
        "never spoken of again by a family that could not bear the "
        "shame of it."
    )},
    {"type": "body", "text": (
        "He had not thought of that story in twenty years. He was not "
        "certain why it surfaced now, over a report he had every reason "
        "to dismiss as one more frightened province inventing monsters "
        "to explain its own bad luck."
    )},
    {"type": "body", "text": (
        "His grandmother had never said what became of that marked "
        "child, or the family that carried him away. She had only ever "
        "said, in the particular hushed voice old women used for "
        "stories they half believed themselves, that some doors, once "
        "opened, did not stay quiet simply because a family wanted them "
        "to. Eze Amadi had grown into a man who ruled by ledgers and "
        "treaties and the slow, patient management of other men's "
        "ambitions. He did not consider himself superstitious. He found, "
        "turning Ikwuano's report over a second time, that he also did "
        "not consider himself quite willing to dismiss it outright, and "
        "was not entirely sure which of those two truths troubled him "
        "more."
    )},
    {"type": "body", "text": (
        "\"Keep the report,\" he said finally. \"Do not send anyone "
        "yet. But if this village troubles the road again, I want to "
        "know before the next season's taxes are due, not after, and I "
        "want to know it from you directly, not filtered through a "
        "clerk who thinks it beneath his time.\""
    )},
    {"type": "body", "text": (
        "Ikwuano bowed and withdrew, carrying the scroll back to the "
        "quiet room where it would wait, patiently, for a second sign "
        "the way every other small strange thing the kingdom sent him "
        "waited, never once suspecting that the second sign was already "
        "closer than either of them believed possible, gathering itself "
        "even now beneath a forest neither man had ever heard named."
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
    print("  THE DARK RISE — Episode 24: \"The Report\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_24.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_24.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
