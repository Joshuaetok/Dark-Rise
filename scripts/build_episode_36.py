#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 36: "The Answering Dark"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-12: Episode 36 follows Osadebe's promised trip upriver from
Episode 35. He wins back one town's trade with his own word, but at the
larger river town learns a foreign trading House has already sent an agent
asking pointed questions about "the delta village the crown sends soldiers
to" — the first concrete move of the Oji Delta oil exploitation backdrop
(Section 7 item 4) into the active plot, a new outside interest with its
own agenda that has nothing to do with abiku law or old fear. In Oso, still
unsettled by the untraceable word from Episode 35, the entity risks
something it has not risked in three centuries: reaching its own senses
outward past the edges of Oso itself, into ground it has never explored,
searching for the source of the pressure it felt. It costs it a moment of
real vulnerability, its attention pulled thin enough that its hold on the
vessel briefly slackens. The episode ends on the entity, withdrawing, at
the exact instant something answers back — not randomly, but deliberately,
proof after three hundred years of assumed solitude that it has never
actually been alone out there.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_36.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Six"},
    {"type": "title_ep_name", "text": "The Answering Dark"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE RIVER ROAD — A NEW KIND OF INTEREST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The nearer town believed him. Osadebe stood in its market "
        "square with the crown's own seal hanging plain against his "
        "chest and told the assembled traders exactly what he had told "
        "Amara he would tell them, the smallest true version of "
        "everything, and watched relief loosen the shoulders of men who "
        "had simply wanted a reason not to be afraid of a village that "
        "had never once cheated them on a trade. Two canoes agreed, "
        "before he had even finished speaking, to resume the Idoro run "
        "by the next full moon."
    )},
    {"type": "body", "text": (
        "The larger town, two days further downriver, did not go so "
        "easily. Osadebe found its headman polite but distracted, "
        "answering questions with half his attention already elsewhere, "
        "and it took the better part of an afternoon before the man "
        "admitted why. A trading House had sent its own agent through "
        "three days earlier, a quiet, well dressed foreigner asking "
        "careful questions about a delta village the crown had "
        "apparently found worth sending soldiers to watch, and what, "
        "exactly, might be worth watching so closely in a village that "
        "small."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"He did not ask about your old law,\" the headman said, "
        "turning a carved trade token over in his fingers without "
        "looking at it. \"He asked about the ground. Whether Idoro's "
        "land had ever been surveyed. Whether anyone had found anything "
        "beneath it worth digging for. I told him I did not know, which "
        "was true, and he thanked me and left north toward the delta "
        "concessions without buying so much as a length of cloth.\""
    )},
    {"type": "body", "text": (
        "Osadebe asked, carefully, whether the agent had given a name "
        "or a House. The headman shrugged, unconcerned in the way of a "
        "man for whom foreign traders passing through were simply "
        "weather, unremarkable unless they bought or sold something. "
        "\"He wore good cloth and spoke our tongue better than most of "
        "his kind bother to learn. That is all I noticed. Men like that "
        "come through twice a season asking about one delta village or "
        "another. I did not think this one worth remembering until you "
        "arrived asking the same questions from the other direction.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe rode the rest of the way back to Idoro turning that "
        "single detail over more carefully than he had turned over "
        "almost anything since the boundary itself. Every fear he had "
        "carried out of Oso had been a fear about what the entity "
        "wanted. It had not once occurred to him, until a stranger's "
        "polite questions about surveyed ground, that other men might "
        "be circling Idoro for reasons that had nothing to do with the "
        "presence beneath the ak-pu roots at all, and everything to do "
        "with whatever the delta's soil and water were quietly worth to "
        "houses that had never heard the word abiku spoken."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "He told Amara everything that evening, watching her weigh the "
        "new danger against the ones she already carried with the tired "
        "precision of a woman adding one more name to a list already "
        "too long to hold comfortably in her head. \"An old law, a "
        "buried presence, and now foreign eyes on our ground besides,\" "
        "she said. \"Idoro has survived a great deal these last months. "
        "I would like, for once, for something to threaten us that I "
        "actually understand how to fight.\""
    )},
    {"type": "body", "text": (
        "\"I will send word to Udo,\" Osadebe told her. \"Eze Amadi "
        "will want to know a trading House has taken an interest before "
        "that interest becomes anything more than questions asked "
        "politely at a market.\" He did not say, because he did not "
        "yet know how true it might become, that a kingdom already "
        "wrestling with an ancient presence at its border might not "
        "have the appetite left to also fight for a delta village's "
        "soil against men who paid the crown's own tribute."
    )},
    {"type": "body", "text": (
        "Obi listened from the doorway with Kene asleep against his "
        "shoulder, and found the fear this new threat carried strangely "
        "shaped compared to every other fear this last year had taught "
        "him. Oso wanted his second son and had wanted him from before "
        "the boy could crawl. Whatever this quiet, well dressed "
        "stranger wanted, it wanted nothing to do with either of his "
        "sons at all, only the dirt beneath the whole village, and Obi "
        "was not certain yet which kind of hunger frightened him more, "
        "the one that had a face and a season, or the one that simply "
        "priced everything it looked at."
    )},
    {"type": "body", "text": (
        "Ozoemena, told the news the next morning while hauling water "
        "for the compound as he now did most mornings, set his jars "
        "down slowly and said nothing for a long while. \"I spent my "
        "one turn at leading this village fighting an enemy I could "
        "see and still lost badly,\" he finally said. \"I do not envy "
        "whoever has to lead it against one that only sends polite men "
        "asking about dirt.\" He picked the jars back up and carried "
        "them the rest of the way without being asked twice, and Amara "
        "found she trusted his plain unease more than she would have "
        "trusted any confident promise from the man he used to be."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE FAR EDGE OF ITS OWN DARK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity had spent three days "
        "turning the boy's untraceable word over without finding "
        "anywhere to set it down, until turning it over stopped being "
        "enough, and it made a decision it had not made once in three "
        "hundred years of careful, contained patience. It would reach "
        "for the source itself, rather than wait for the source to "
        "reach for the boy again."
    )},
    {"type": "body", "text": (
        "It had always known the exact borders of its own territory, "
        "the ground its roots claimed and the ground beyond that "
        "belonged to nothing it had ever needed to name. It had fed "
        "there, grown there, waited there, and never once, in all that "
        "waiting, sent any part of itself past the edge of what it "
        "already understood. Doing so now meant loosening its grip on "
        "everything closer to keep, including, for however many "
        "careful minutes this took, the boy sleeping among his stones."
    )},
    {"type": "body", "text": (
        "It weighed the risk the way it weighed every risk, coldly and "
        "without hurry, and found, for once, that the calculation would "
        "not resolve cleanly. Three centuries of caution argued for "
        "waiting the pressure out the way it had waited out every other "
        "threat that never fully arrived. But the boy's small, "
        "unbothered certainty kept returning to it, the way he had said "
        "the word as though it already belonged to something, and the "
        "entity understood that a mystery left uninvestigated inside a "
        "vessel it could not fully see into was a danger of a different "
        "order than anything it had faced from outside itself before."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "It went anyway. Its attention thinned and stretched the way a "
        "single voice thins when asked to fill a hall built for a "
        "hundred, spreading out past the last root it had ever grown, "
        "into ground that smelled of nothing living, dark that had "
        "never once held a fire or a footstep, silence so total it felt "
        "less like an absence of sound than like something actively "
        "holding its breath."
    )},
    {"type": "body", "text": (
        "For a long while there was nothing. No pressure, no pulse, "
        "no answer to the two soft syllables it carried out with it "
        "like a question it did not fully know how to ask. It moved "
        "further than it had planned to, drawn on by the same "
        "stubborn certainty that had once made it press a dormant "
        "thread it barely understood rather than leave a question "
        "unanswered, and the ground it crossed grew stranger with every "
        "reach, roots that were not its own roots, cold that did not "
        "behave like the cold of soil or water or night, as though the "
        "dark itself had simply decided, this far out, that it no "
        "longer needed to explain itself to anything passing through."
    )},
    {"type": "body", "text": (
        "The entity began, cautiously, to consider that three "
        "centuries of assumed company at the edges of its own dark had "
        "been nothing more than an old habit of fear it had never "
        "bothered to test, the way a man raised to fear a particular "
        "shadow might never think to check whether anything actually "
        "cast it. It allowed itself, for one unguarded instant, "
        "something close to relief."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Then, far back in Oso, closer to the boy than the entity's "
        "own reaching attention currently was, something small and "
        "unwatched cried out. Not the boy's voice. A startled, wordless "
        "sound, brief and quickly swallowed, the exact sound something "
        "makes when it wakes suddenly to find itself alone in the dark "
        "and does not yet know why."
    )},
    {"type": "body", "text": (
        "The entity snapped its attention home so fast the silence it "
        "left behind in that far, unclaimed ground seemed, for one "
        "unbearable instant, to close around the space where it had "
        "just been standing, the way water closes over a hand pulled "
        "quickly out of a river."
    )},
    {"type": "body", "text": (
        "The boy was exactly where he had been left, stones "
        "undisturbed, breathing even, entirely unaware anything had "
        "happened at all. Whatever had cried out had not been him. The "
        "entity searched the hollow twice, found nothing to explain the "
        "sound, and understood, with a certainty that settled into it "
        "colder than any fear it had felt in three hundred years, that "
        "the sound had not come from anything it had ever claimed."
    )},
    {"type": "body", "text": (
        "It had reached out looking for whatever answered the boy's "
        "stolen word. What it found instead, in the last instant before "
        "it fled home, was proof that something out past the edge of "
        "its own dark had heard it reaching, and had, deliberately, "
        "reached back."
    )},
    {"type": "body", "text": (
        "It sat with the boy the rest of that night in a stillness "
        "that had nothing gentle in it, cataloguing everything it now "
        "knew and everything it still did not. The cry had not come "
        "from inside its own claimed ground, which meant whatever made "
        "it lived close enough to be startled by a presence it had "
        "clearly never expected to feel reaching toward it. That the "
        "sound had been startled, rather than hostile, offered the "
        "entity no comfort at all. Three centuries had taught it that "
        "the things most worth fearing were rarely the ones that "
        "announced themselves with anger."
    )},
    {"type": "body", "text": (
        "For the first time since it had claimed this ground and the "
        "child sleeping on it, the entity found itself wondering "
        "whether patience, its oldest and most trusted weapon, had "
        "simply never been tested against anything patient enough to "
        "wait it out in return."
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
    print("  THE DARK RISE — Episode 36: \"The Answering Dark\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_36.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_36.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
