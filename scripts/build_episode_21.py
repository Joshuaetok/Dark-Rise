#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 21: "The Vacancy"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-28: Episode 21 opens the next arc. A week after Elder
Maka's fall, Idoro's council still has no one willing to claim her old
authority outright, until Ozoemena, a mid ranking elder known more for his
loud certainty than his wisdom, stands up at a gathering and offers
himself as the decisive hand the village has been missing. His pitch is
simple and effective: fear has been mismanaged, not misplaced, and Idoro
needs someone willing to act where Elder Maka only watched. In Oso, the
entity registers the shift in Idoro's politics with its usual patient
indifference, weighing what a new, hungrier kind of human authority might
cost or gain it. The episode closes with Ozoemena naming his first target
in front of the reassembled council: the dibia, still alive, still
silenced, and in his words, "a mouth no one has had the courage to close."
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_21.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty One"},
    {"type": "title_ep_name", "text": "The Vacancy"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE MAN WHO STOOD UP
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A week after the council stripped Elder Maka of her authority, "
        "Idoro gathered again beneath the same meeting tree, still "
        "without anyone willing to sit where she had once sat, until "
        "Ozoemena rose from among the seated elders and simply began "
        "speaking as though the silence had been waiting for him alone "
        "to fill it."
    )},
    {"type": "body", "text": (
        "He was a broad, thick necked man some ten years younger than "
        "Elder Maka had been, known across Idoro less for careful "
        "judgment than for the volume and certainty of his opinions at "
        "every gathering he had ever attended, the kind of man who "
        "mistook loudness for leadership and had, until this week, never "
        "been given the chance to prove whether the two were the same "
        "thing."
    )},
    {"type": "body", "text": (
        "\"We have spent seven days arguing over who is fit to lead "
        "us,\" he said, \"while the thing that broke Elder Maka has "
        "spent those same seven days doing whatever it pleases, "
        "unwatched, unopposed, growing bolder with every morning we "
        "waste on our own indecision. I do not claim to be wiser than "
        "she was. I claim only that I am willing to act while the rest "
        "of you are still deciding whether acting is safe.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A murmur of agreement moved through the gathered elders, "
        "tired enough after a week of fear to welcome the shape of "
        "certainty even before they had examined what it was certain "
        "about. Amara, standing at the edge of the crowd with Obi and "
        "Kene, felt the old, familiar tightening in her chest that she "
        "had learned to recognize as the first sign of a new danger "
        "finding its shape."
    )},
    {"type": "body", "text": (
        "She had seen men like Ozoemena before, in smaller disputes over "
        "land and bride price, men whose confidence grew louder in "
        "direct proportion to how little they understood of what they "
        "were being confident about. She had never before watched one of "
        "them offered the whole authority of a frightened village at "
        "once, and she found she did not know yet whether that "
        "unfamiliarity frightened her more than the certainty she did "
        "recognize in him."
    )},
    {"type": "body", "text": (
        "One of the older women near the front, the same woman who had "
        "called out in Zara's honor at the send off, spoke up now with "
        "far less warmth in her voice. \"Elder Maka spent thirty and "
        "four years learning the old rites before she ever led one. "
        "What have you spent learning, beyond how to raise your own "
        "voice above everyone else's at a gathering.\""
    )},
    {"type": "body", "text": (
        "\"I have spent this last week watching all of you argue "
        "yourselves into paralysis while a marked household went "
        "unwatched and a possessed man sat forgotten in his own hut,\" "
        "Ozoemena said, unbothered. \"Knowledge did not save Elder Maka. "
        "It only taught her exactly how afraid to be, and being afraid "
        "correctly did not stop the thing from ruining her all the "
        "same.\""
    )},
    {"type": "body", "text": (
        "\"Elder Maka watched and waited and still lost control of "
        "everything she was meant to protect,\" Ozoemena continued. "
        "\"I do not intend to watch and wait. I intend to close every "
        "door that thing has opened into this village, starting with "
        "the ones we have been too frightened to look at directly.\""
    )},
    {"type": "body", "text": (
        "No one asked him to clarify which doors he meant. No one, "
        "Amara noticed, looked toward her own compound while he spoke, "
        "and she understood, with a chill that had nothing to do with "
        "the morning air, that his restraint on that point was almost "
        "certainly deliberate, a promise saved rather than a mercy "
        "granted."
    )},
    {"type": "body", "text": (
        "She had learned, across these last difficult months, to read "
        "exactly this kind of careful omission in a speaker's words, "
        "the shape of a threat held back on purpose so it could be "
        "delivered later, privately, when it would cost the speaker "
        "less to make. Ozoemena had not forgotten her family standing "
        "at the edge of his audience. He had simply decided they were "
        "not yet worth spending in front of a crowd still deciding "
        "whether to trust him."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT A HUNGRIER AUTHORITY MIGHT COST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had felt the shape of "
        "Idoro's politics shifting for days now, a new hunger for "
        "certainty rising out of the vacuum Elder Maka's fall had left "
        "behind, and it turned its attention toward the man now "
        "claiming to fill that vacuum with the same unhurried care it "
        "gave every development that might eventually cost it something."
    )},
    {"type": "body", "text": (
        "Elder Maka had been dangerous because she understood the old "
        "rites well enough to threaten a thread directly, and cautious "
        "enough to weigh every action against a cost she had personally "
        "paid once already. This new man understood almost nothing of "
        "what he claimed to be fighting, and cared, the entity judged, "
        "rather more about being seen to fight it than about "
        "understanding what fighting it would actually require."
    )},
    {"type": "body", "text": (
        "That kind of authority was not without its uses. A leader who "
        "acted first and understood later was a leader who could be "
        "relied upon to make exactly the kind of mistake that produced "
        "rich, memorable fear, the sort that fed the entity for weeks "
        "rather than hours. It had learned patience from a careful "
        "enemy. It saw no reason yet to fear an impatient one."
    )},
    {"type": "body", "text": (
        "It considered, turning the thought over with the same "
        "unhurried attention it gave every calculation, what an "
        "impatient man might attempt against the dibia specifically. "
        "The dibia's thread was the oldest the entity had built, laid "
        "down thread by careful thread across weeks before it had ever "
        "dared risk a full sentence through that borrowed throat. A "
        "clumsy hand reaching for something built that carefully could "
        "do real damage, to the dibia's body if nothing else, and the "
        "entity found, weighing the risk honestly, that it was not "
        "entirely certain yet whether it would defend that particular "
        "door if a reckless man came for it in earnest."
    )},
    {"type": "body", "text": (
        "The dibia had served its purpose as a mouthpiece and had not "
        "been asked to serve it again in some time. A body that old, "
        "worn this thin by strain, might simply not be worth the cost "
        "of saving if saving it meant revealing more of the entity's own "
        "strength than the moment required."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel repeated his single small word to "
        "himself in the quiet hours, turning it over the way a child "
        "turns over a stone he has decided is worth keeping, and the "
        "entity, listening, found itself once again setting aside the "
        "question of what to do about it, in favor of watching what the "
        "word became next."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "NEW HUMAN AUTHORITY IDENTIFIED: HIGH AMBITION, LOW UNDERSTANDING. THREAT LEVEL: LOW, YIELD POTENTIAL: HIGH."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE FIRST NAME OZOEMENA SPOKE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By midday the council had done what it had refused to do for "
        "a full week and given Ozoemena the standing to act in the old "
        "law's name, on the condition, spoken more out of exhaustion "
        "than conviction, that he bring any serious action back before "
        "them first."
    )},
    {"type": "body", "text": (
        "He accepted the condition the way a man accepts a formality he "
        "does not intend to be bound by for long, and turned, before "
        "the gathering had even fully dispersed, to name the first "
        "target of his new authority."
    )},
    {"type": "body", "text": (
        "A handful of younger men had already begun drifting toward him "
        "before he had finished speaking, the way followers gather "
        "around any man who sounds certain enough to be worth following, "
        "and Amara watched the beginning of something that looked less "
        "like a council and more like a following, assembled in less "
        "time than it had taken Elder Maka to lose the one she had spent "
        "decades building."
    )},
    {"type": "body", "text": (
        "\"The dibia,\" he said, loud enough to carry to everyone still "
        "within earshot. \"A mouth no one has had the courage to close, "
        "sitting in his own hut all these weeks, still carrying whatever "
        "it is that speaks through him when it pleases. Elder Maka let "
        "him live because she feared what killing him might cost the "
        "village. I am not interested in what fear has already cost us. "
        "I am interested in what closing that door might finally buy "
        "us.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara felt Obi's hand find hers without either of them "
        "deciding to reach for the other, both remembering, in the same "
        "instant, the dibia's own voice breaking through mid convulsion "
        "during the cleansing rite to gasp a warning that had never "
        "finished, He is not the only door. There are others already."
    )},
    {"type": "body", "text": (
        "Whatever Ozoemena believed he understood about the thing "
        "beneath Oso, Amara understood, standing there with her "
        "husband's hand cold in hers, that he understood almost nothing "
        "at all, and that a man who acted with that much confidence "
        "atop that little knowledge was more dangerous to Idoro, in his "
        "own way, than anything Elder Maka's caution had ever cost them."
    )},
    {"type": "body", "text": (
        "\"He does not know what he is reaching for,\" Obi said quietly, "
        "once they were far enough from the crowd to speak without being "
        "overheard, his voice low and tight with the particular worry "
        "of a man who has already spent every ounce of trust he had left "
        "to give this village's leadership."
    )},
    {"type": "body", "text": (
        "\"No,\" Amara agreed. \"And a man who does not know what he is "
        "reaching for rarely stops to ask before his hand is already "
        "inside the fire.\""
    )},
    {"type": "body", "text": (
        "She looked back once at the small crowd already gathering "
        "around Ozoemena's certainty, and thought, not for the first "
        "time since Elder Maka's fall, that Idoro had traded one kind of "
        "danger for another without pausing long enough to notice it had "
        "made a trade at all."
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
    print("  THE DARK RISE — Episode 21: \"The Vacancy\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_21.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_21.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
