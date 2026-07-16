#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 19: "The Unraveling"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-26: Episode 19 shows the human cost of Episode 18's public
exposure. Idoro's elders strip Elder Maka of her authority within the day,
unable to trust a woman marked by the very thing she has spent thirty four
years condemning others for carrying. Adaugo, learning in the same
afternoon both that she had a brother and that her mother is marked,
cannot bring herself to stay in her mother's compound. Amid the chaos,
Zara's departure, the reason the crowd gathered in the first place, happens
almost unnoticed, Amara walking with her as far as the village boundary to
keep her promise. In Oso, the entity reviews the day's yield with something
close to satisfaction, having turned one afternoon's calculated cruelty
into a leaderless, destabilized village far more vulnerable than the one
it woke to that morning. The episode closes on a passing trader, having
witnessed enough of the day's chaos from the road, already carrying the
story north, toward villages that have never once heard Idoro's name
spoken with dread.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_19.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Nineteen"},
    {"type": "title_ep_name", "text": "The Unraveling"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT THE COUNCIL DECIDED BY NIGHTFALL
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The elders convened before the sun had finished setting, a "
        "hurried, frightened council held by torchlight because no one "
        "present was willing to wait until morning to settle a question "
        "that had already answered itself in front of the whole "
        "village."
    )},
    {"type": "body", "text": (
        "Amara was not permitted inside the meeting, but she did not "
        "need to be. The shape of it reached her anyway, carried out in "
        "fragments by neighbors too shaken to keep their voices low. "
        "Elder Maka would no longer speak for the old law. A woman "
        "marked by the very thing the law existed to guard against "
        "could not be trusted to judge who else deserved to be spared "
        "or condemned by it."
    )},
    {"type": "body", "text": (
        "No one suggested she be bound, or exiled, or ended the way she "
        "had once ended her own returned son. The council was too "
        "frightened to agree on anything beyond the one thing they could "
        "all agree on at once, that she could no longer be the one who "
        "decided such questions for anyone else. It was, Amara thought, "
        "listening to the fragments pass from mouth to mouth, its own "
        "kind of mercy, thin and reluctant, offered by people too "
        "unsettled to manage anything crueler that night."
    )},
    {"type": "body", "text": (
        "No one stood forward to take her place either, at least not "
        "yet. The two watchers who had guarded Amara's compound for "
        "weeks stood outside the meeting hut with nothing left to guard "
        "and nowhere clear to report, and when Amara passed them on her "
        "way home, neither man met her eyes, as though the whole village "
        "had discovered, in a single afternoon, that it did not entirely "
        "know what it was supposed to be afraid of anymore."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Adaugo found her mother afterward sitting alone in the "
        "compound that no longer held any authority at all, and stood "
        "in the doorway for a long time before she trusted herself to "
        "speak."
    )},
    {"type": "body", "text": (
        "\"You had a son before me,\" Adaugo said. \"You buried him with "
        "your own hands and never told me. And you have been carrying "
        "the same darkness that took him for weeks now, and you let me "
        "believe you were only tired.\""
    )},
    {"type": "body", "text": (
        "\"I was trying to protect you from both truths at once,\" "
        "Elder Maka said, and for the first time in longer than either "
        "of them could remember, her voice held no authority in it at "
        "all, only an old woman's exhaustion."
    )},
    {"type": "body", "text": (
        "\"You protected yourself,\" Adaugo said. \"You have spent my "
        "whole life telling this village exactly how much mercy the "
        "marked deserve. I do not know how to sit in this house tonight "
        "and pretend I have not just learned the answer.\""
    )},
    {"type": "body", "text": (
        "\"I was afraid,\" Elder Maka said, so quietly Adaugo almost did "
        "not hear it. \"Every day since I chose to carry it, I was "
        "afraid, and I told myself the fear was proof I could still be "
        "trusted with it, because a woman too comfortable with a "
        "darkness like this one is a woman already lost to it. I do not "
        "know if that was wisdom or only another way of lying to "
        "myself.\""
    )},
    {"type": "body", "text": (
        "\"It does not matter which,\" Adaugo said. \"Either way I have "
        "spent my whole life believing you were the one person in Idoro "
        "who could not be reached by any of this. I do not know how to "
        "stop believing that overnight simply because it would be "
        "convenient for both of us.\""
    )},
    {"type": "body", "text": (
        "She left before her mother could answer, and Elder Maka let "
        "her go, because she had already spent the last true authority "
        "she had over anyone, and she was not certain, sitting alone in "
        "the dark that followed, that she had any right left to call her "
        "own daughter back."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY COUNTED AS PROFIT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity reviewed the day's yield "
        "with the same unhurried satisfaction a careful trader takes in "
        "counting a harvest larger than expected."
    )},
    {"type": "body", "text": (
        "It had spent one secret, held in reserve for exactly the right "
        "morning, and received in return a village with no one left "
        "standing at its center willing to organize another rite, "
        "another cleansing, another binding. The old woman had been the "
        "only person in Idoro who understood the shape of the old "
        "rites well enough to threaten any of its remaining doors. "
        "Without her, the dibia's silenced thread sat entirely "
        "unguarded, and whatever thin defenses the village had scraped "
        "together against its reach were now leaderless, argued over by "
        "elders too frightened of each other's judgment to agree on "
        "anything beyond removing the one woman who had ever come close "
        "to hurting it."
    )},
    {"type": "body", "text": (
        "It let itself consider, briefly, whether the dibia's own "
        "condition had shifted at all in the noise of the day. He had "
        "not been present at the crowd's gathering, kept apart in his "
        "hut by villagers too consumed with their own fear to remember "
        "the first door the entity had ever opened into this village. "
        "That, too, the entity noted with quiet approval. A door "
        "forgotten was a door that required no defense at all to keep."
    )},
    {"type": "body", "text": (
        "It weighed, too, the strange new softness in its own reasoning "
        "that had crept in somewhere across these last weeks, a "
        "willingness to let outcomes fall where they fell rather than "
        "forcing every one of them by hand. It had not been built this "
        "way once. Three centuries earlier, newly bound to the ground it "
        "still called home, it had reached for everything within its "
        "grasp at once, indiscriminate, hungry in the crude way young "
        "things are hungry. Patience had been learned, slowly, the same "
        "way the vessel now learned to shape sound into something "
        "closer to language. It found, turning the comparison over, that "
        "it did not dislike what it had become in the learning."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel had begun, for the first time, to "
        "reach toward the entity's own attention rather than simply "
        "receiving it, small fingers closing around the nearest root the "
        "way an older child reaches for a hand it has learned to trust. "
        "The entity let the boy hold on. There was no harm in it now, "
        "and there was, if the entity allowed itself something close to "
        "anticipation, a use coming soon enough for a vessel that had "
        "finally learned to reach back."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "VILLAGE LEADERSHIP: DESTABILIZED, NO ORGANIZING AUTHORITY REMAINING. REMAINING THREADS: UNDEFENDED. VESSEL: FIRST RECIPROCAL CONTACT OBSERVED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE DEPARTURE NO ONE WATCHED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By the time Zara finally left, the path that had been crowded "
        "with witnesses that morning stood almost empty, every person "
        "who might have watched her go instead pulled into their own "
        "compounds arguing over what to do about an old woman who no "
        "longer ruled them."
    )},
    {"type": "body", "text": (
        "It struck Amara, walking beside her toward the boundary of "
        "Idoro's fields, that the entity had managed, in a single "
        "morning, to erase the one goodbye Zara had actually earned "
        "after thirty years of service, folding it quietly into a larger "
        "story that was no longer about her at all."
    )},
    {"type": "body", "text": (
        "\"I am sorry,\" Amara said. \"You deserved better than to be "
        "forgotten in the middle of your own leaving.\""
    )},
    {"type": "body", "text": (
        "\"I do not think I minded, in the end,\" Zara said. \"A quiet "
        "leaving is easier to carry than a loud one. Let the village "
        "spend its grief on Elder Maka tonight. I have had enough of "
        "being the thing it spends its fear on.\""
    )},
    {"type": "body", "text": (
        "\"Where will you go,\" Amara asked, though she suspected there "
        "was no honest answer waiting behind the question, only "
        "directions and the hope that one of them proved kinder than "
        "the rest."
    )},
    {"type": "body", "text": (
        "\"Wherever a midwife's hands are still worth more than the "
        "story attached to them,\" Zara said. \"There are other rivers. "
        "Other villages that have never heard the word abiku spoken the "
        "way Idoro speaks it. I intend to find one of them before I "
        "decide what the rest of my life is meant to look like.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "They stopped together at the last of the cassava fields, where "
        "the path narrowed and the bush beyond it grew close and "
        "unfamiliar, and Amara embraced her once, tightly, the way a "
        "woman embraces someone she does not expect to see again in this "
        "life."
    )},
    {"type": "body", "text": (
        "\"Walk carefully,\" Amara said. \"And if anything reaches for "
        "you out there, remember you are still the woman who caught half "
        "this village in her own two hands. That is not nothing, "
        "whatever else has been taken from you.\""
    )},
    {"type": "body", "text": (
        "Zara nodded, and turned, and walked on alone down a path Amara "
        "did not follow any further, and did not look back, the same "
        "way a woman does not look back at a door she has already "
        "decided to close behind her."
    )},
    {"type": "body", "text": (
        "Amara stood at the edge of the cassava field a long while "
        "after Zara had disappeared around the first bend, watching the "
        "empty path the way a person watches a wound to see whether it "
        "has truly stopped bleeding, before finally turning back toward "
        "a village that no longer looked, to her, quite like the one she "
        "had grown up trusting."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Neither of them noticed the trader resting his cart at the "
        "crossroads a little further down that same path, a stranger to "
        "Idoro passing through toward the river markets, who had heard "
        "enough of the day's shouting carried on the wind to piece "
        "together a story worth telling at his next stop. He did not "
        "know the names Amara or Zara or Elder Maka. He knew only that a "
        "village called Idoro had spent one single morning tearing "
        "apart the woman who ruled it, over something that spoke through "
        "another woman's mouth in front of the whole gathered crowd."
    )},
    {"type": "body", "text": (
        "It was, he decided, turning his cart back onto the northward "
        "road, exactly the kind of story that traveled well, the kind "
        "that grew a little larger and a little stranger at every fire "
        "it was told beside, long before it ever reached anyone who "
        "might have known what to do with the truth of it."
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
    print("  THE DARK RISE — Episode 19: \"The Unraveling\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_19.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_19.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
