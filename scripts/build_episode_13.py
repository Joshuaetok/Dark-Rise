#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 13: "The Weight"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-20: Episode 13 turns to Elder Maka in the days after the
binding rite, showing the private cost of what she absorbed from Kene's
severed thread. She loses small stretches of time without explanation, and
cannot tell anyone what she suspects is happening to her without exposing
herself to the exact law she has spent thirty four years enforcing without
mercy. Her surviving daughter, named here for the first time as Adaugo,
notices her mother is not herself but is given no explanation. In Oso, the
entity registers the new thread running through Idoro's most dangerous
enemy and treats it as a high value, high risk asset, choosing to observe
rather than act, unlike its more aggressive handling of the midwife's
thread. The episode closes on Adaugo catching her mother's eyes flicker
dark for one instant while helping her up from a stumble, not understanding
what she has seen, and letting it go.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_13.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirteen"},
    {"type": "title_ep_name", "text": "The Weight"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT ELDER MAKA COULD NOT EXPLAIN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The first time it happened, Elder Maka told herself it was "
        "nothing more than age. She was grinding camwood in her own "
        "yard, the pestle rising and falling in a rhythm her hands had "
        "known for longer than most of Idoro had been alive, and then "
        "the light had changed, and the bowl before her was full instead "
        "of half empty, and she could not account for the missing time "
        "between one thought and the next."
    )},
    {"type": "body", "text": (
        "She checked the sun. It had moved further than a moment's "
        "distraction should have allowed."
    )},
    {"type": "body", "text": (
        "She sat with the bowl in her lap for a long while afterward, "
        "listening to her own household move around her, the ordinary "
        "sounds of a goat shifting its tether and a pot settling on the "
        "fire, and told herself an old woman's mind wanders sometimes "
        "the way an old woman's knees ache sometimes, without meaning "
        "anything beyond the plain fact of years spent. She had told "
        "younger women this exact comfort more than once, standing over "
        "their own small fears. It sounded thinner now, offered only to "
        "herself, than it ever had offered to someone else."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The second time, three days later, she found herself standing "
        "at the low wall behind her compound, facing the direction of "
        "Oso across the sloping fields, with no memory of having risen "
        "from her stool to walk there. Her feet were bare. She did not "
        "remember removing her sandals either."
    )},
    {"type": "body", "text": (
        "She stood very still for a long moment, listening to her own "
        "heartbeat, and thought of Zara's bleeding feet on the bush "
        "path, and understood, with a clarity that frightened her more "
        "than the missing time itself, exactly what she was looking at "
        "in herself."
    )},
    {"type": "body", "text": (
        "She had sat across from that same midwife only days earlier "
        "and heard her describe this precise sensation, the walk begun "
        "without a beginning, the waking without a memory of having "
        "slept badly enough to explain it, and she had listened with the "
        "cool, measuring attention of a woman gathering evidence rather "
        "than the frightened attention of a woman recognizing her own "
        "future. She understood now that she had simply not yet known "
        "which one she was."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "There was no one she could tell. That was the shape of the "
        "trap she had built with her own hands three days earlier, "
        "chanting over a sleeping child while she chose, deliberately, "
        "to carry his severed weight into her own blood rather than let "
        "it scatter. She had spent thirty and four years teaching Idoro "
        "that a marked person was a danger to be watched, contained, "
        "and if necessary ended before the danger matured. She could not "
        "now walk into her own council and confess that the danger had "
        "found a new home inside the woman who enforced the law against "
        "it."
    )},
    {"type": "body", "text": (
        "She thought, once, of going to Amara. The thought did not "
        "survive long. Amara had every reason in the world to use such "
        "a confession as a weapon, and Elder Maka, of all people in "
        "Idoro, understood exactly how sharp a weapon like that could "
        "be made."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Her daughter found her sitting alone that evening, staring at "
        "nothing, a cold cup of palm wine untouched at her elbow."
    )},
    {"type": "body", "text": (
        "\"Mother,\" Adaugo said, setting down the basket of millet she "
        "had been grinding nearby, her voice carrying the particular "
        "worry of a grown daughter who has watched her mother be "
        "unbreakable for as long as she can remember and does not know "
        "what to do with the sight of a crack. \"You have not been "
        "yourself since the night you went to Amara's compound. What "
        "happened there.\""
    )},
    {"type": "body", "text": (
        "\"I performed a rite,\" Elder Maka said. \"Rites take a toll. "
        "I am old, and the toll is heavier than it once was. That is "
        "all this is.\""
    )},
    {"type": "body", "text": (
        "Adaugo did not look convinced, but she had also spent her "
        "whole life learning not to push at doors her mother had closed, "
        "and after a moment she only nodded, and picked her basket back "
        "up, and let the lie stand between them the way so many lies had "
        "stood between them for thirty and four years without either "
        "woman naming a single one of them aloud."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY WAS PATIENT ENOUGH NOT TO TOUCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had felt the new thread "
        "settle into existence the instant Elder Maka chose to carry it, "
        "a thin, unexpected gift dropped directly into its reach by the "
        "one woman in Idoro who had never once intended to give it "
        "anything."
    )},
    {"type": "body", "text": (
        "It considered this thread more carefully than it had considered "
        "either of the others."
    )},
    {"type": "body", "text": (
        "The dibia's thread had been built slowly, over days, with the "
        "entity's own patient effort behind every strand of it. The "
        "midwife's thread had opened almost by accident, a blood memory "
        "waiting to be noticed. This thread was neither. It sat inside a "
        "woman who had killed a vessel of the entity's own kind with her "
        "own hands once already, who understood the old rites better "
        "than anyone else living, and who would recognize the shape of "
        "being reached for far sooner than either the dibia or the "
        "midwife ever had."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A careless hand here could lose the thread entirely, sealed as "
        "swiftly and cleanly as Kene's had just been sealed, by the same "
        "woman, using knowledge the entity had no way of predicting in "
        "advance. A patient hand, though, might hold something no other "
        "thread in Idoro could offer. Not a distraction. Not a "
        "messenger. An enforcer, turned slowly enough that she never "
        "noticed the turning, could someday stand at the very center of "
        "the village's fear and point it wherever the entity found most "
        "useful."
    )},
    {"type": "body", "text": (
        "It did not reach for her yet. It only watched, the way it had "
        "learned to watch everything worth having, and let the small, "
        "unexplained absences it had not even caused directly, only "
        "inherited, do their own slow work on a woman already terrified "
        "of what she had chosen to carry."
    )},
    {"type": "body", "text": (
        "There was an irony in this thread the entity almost enjoyed, in "
        "whatever manner something without a face could be said to "
        "enjoy anything. The old woman had spent her whole life sorting "
        "the marked from the unmarked, certain of which side of that "
        "line she stood on. She would spend whatever time remained to "
        "her now discovering that lines drawn by fear were never as "
        "fixed as the people who drew them liked to believe, and the "
        "entity intended to let her discover it slowly, one missing "
        "afternoon at a time, rather than all at once in a single strike "
        "she might yet find a way to survive."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Three doors now stood open into Idoro in one shape or another, "
        "and the entity, counting them the way a careful trader counts "
        "coin rather than the way a hungry animal counts prey, found "
        "itself, for the first time since it had claimed the vessel "
        "beneath these roots, in the curious position of having more "
        "than it yet knew how to spend."
    )},

    {"type": "system", "text": "THIRD THREAD CONFIRMED: HIGH VALUE, HIGH RISK. ACTIVATION WITHHELD PENDING FURTHER OBSERVATION. HOST IDENTIFIED AS PRIMARY LAW ENFORCER, VILLAGE OF IDORO."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ADAUGO SAW AND DID NOT UNDERSTAND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka tried, that night, to do the one thing she still "
        "knew how to do for herself. She traced a small ring of "
        "protective ash around her own sleeping mat, murmuring half "
        "remembered words she had not spoken since long before her "
        "husband died, words meant to keep a restless spirit from "
        "finding the sleeper inside the ring."
    )},
    {"type": "body", "text": (
        "She did not know if the words still held any power at all, "
        "spoken alone by an old woman with no dibia left to trust and no "
        "one to stand witness. She traced the ring anyway, because doing "
        "something felt less unbearable than doing nothing, and lay down "
        "inside it, and did not sleep for a long while."
    )},
    {"type": "body", "text": (
        "She thought, staring up into the dark thatch above her, of "
        "every mother she had ever stood over with a verdict already "
        "decided before the woman finished pleading her child's case. "
        "She had believed, every single time, that she was protecting "
        "Idoro from a danger she alone had the courage to name plainly. "
        "It had never once occurred to her, in thirty and four years of "
        "believing that, that the danger might someday choose to enter "
        "through the very door built to keep it out."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the morning, rising stiffly from a night that had given her "
        "little rest, her foot caught the edge of her own sleeping mat "
        "and she stumbled, and Adaugo, passing by with a bundle of "
        "firewood, dropped it at once and caught her mother's arm before "
        "she could fall."
    )},
    {"type": "body", "text": (
        "\"Careful,\" Adaugo said, steadying her, and for one instant, "
        "close enough to see it clearly, close enough that there could "
        "be no mistaking it for a trick of the early light, she looked "
        "into her mother's eyes and saw them, briefly, turn dark and "
        "faintly shining, the way oil shines on water left too long "
        "undisturbed."
    )},
    {"type": "body", "text": (
        "Then Elder Maka blinked, and straightened, and her eyes were "
        "only her own eyes again, tired and old and entirely familiar, "
        "and Adaugo told herself, the way anyone tells themselves "
        "something too strange to hold onto in the ordinary light of "
        "morning, that she had imagined it, a shadow, a trick of sleep "
        "still clinging to her own eyes rather than her mother's."
    )},
    {"type": "body", "text": (
        "She picked her firewood back up and said nothing, and neither "
        "of them ever knew, standing together in that ordinary morning "
        "light, that Idoro now held a third pair of eyes capable of "
        "turning dark without warning, and that the only person besides "
        "Elder Maka herself who had just seen it happen did not yet "
        "understand what she had seen, or how soon that understanding "
        "might come looking for her anyway, whether she was ready for "
        "it or not."
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
    print("  THE DARK RISE — Episode 13: \"The Weight\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_13.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_13.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
