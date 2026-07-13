#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 68: "The Watcher at the Tree Line"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-13: Episode 68 delivers the warning Chibundu and the
entity resolved to give at the end of Episode 67. Amara, Obi, and
Chidebe absorb the true shape of the danger — that it will come for
whoever matters most to them rather than for Chibundu directly — and
begin quietly restructuring the family's most predictable habits. The
episode's second half leaves Idoro for the first time to show the
specialist's arrival near Oso directly: patient, unhurried, and
entirely unannounced, observing the boundary for a full day before
ever being sensed by either old power. Where the entity and the
presence have spent this whole season assuming Amara stands at the
center of the danger, the specialist's own quiet accounting settles
somewhere else — on the ordinary, unwatched toddler nobody has
thought yet to guard as carefully as they guard everyone else.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_68.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Eight"},
    {"type": "title_ep_name", "text": "The Watcher at the Tree Line"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A DIFFERENT KIND OF READY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The entity told Amara itself, exactly as it had promised "
        "Chibundu it would, standing at her own compound rather than "
        "at the boundary, its voice carrying the particular weight of "
        "an apology it had not fully earned the right to offer yet. "
        "\"I failed to recognize a danger already aimed at you once "
        "before,\" it said. \"I will not compound that failure by "
        "softening what I now understand it might try again.\""
    )},
    {"type": "body", "text": (
        "Amara listened to the whole account without once "
        "interrupting, her hands folded tightly in her lap the way "
        "they had been at the boundary council weeks before, and when "
        "the entity finished, she asked the only question that "
        "actually mattered to her. \"What do we do differently "
        "starting tonight.\""
    )},
    {"type": "body", "text": (
        "\"You stop being predictable,\" Chidebe said, before the "
        "entity could answer, his soldier's mind already several steps "
        "ahead of the conversation. \"No fixed hour for anything that "
        "matters. No routine simple enough for a patient watcher to "
        "learn from a distance. I will rotate my men's patrols on no "
        "pattern at all, even one only I can predict, and I want your "
        "own household doing the same with anything resembling a "
        "schedule.\""
    )},
    {"type": "body", "text": (
        "Obi, holding Kene against his shoulder through the whole "
        "conversation, asked the question underneath all of it that no "
        "one had yet said aloud. \"You keep saying whoever matters most "
        "to us,\" he said. \"Say plainly what you mean. Do you mean "
        "Amara. Do you mean Kene. Do you mean all of us at once.\""
    )},
    {"type": "body", "text": (
        "\"I do not know yet,\" the entity admitted, and the honesty of "
        "it landed harder in the small room than a comforting lie "
        "would have. \"That is precisely what frightens me most about "
        "this danger. It will choose whoever offers it the clearest "
        "opening, and I cannot promise you which of you that will "
        "turn out to be.\""
    )},
    {"type": "body", "text": (
        "Chibundu, standing at Amara's side rather than leaving the "
        "entity to speak for him, added the part he had insisted on "
        "carrying himself. \"I do not want either of you treating Kene "
        "as though he is somehow safer than the rest of us simply "
        "because his own thread was cut years ago,\" he said. \"The "
        "presence was clear that this hunter chooses whoever offers "
        "the easiest opening, not whoever carries the most power. A "
        "boy no one thinks to guard as carefully might be exactly that "
        "kind of opening.\""
    )},
    {"type": "body", "text": (
        "Amara felt the specific shape of that fear land somewhere "
        "deeper than the others had, a mother's arithmetic running "
        "ahead of everyone else's caution. \"He is a child,\" she said. "
        "\"He plays at the edge of the compound. He follows the other "
        "children to the stream. I cannot keep him inside a guarded "
        "circle every hour of every day without also taking from him "
        "the ordinary life we have fought this hard to let him keep.\""
    )},
    {"type": "body", "text": (
        "\"No one is asking you to cage him,\" Chidebe said. \"I am "
        "asking you to let me post a man near enough to the stream and "
        "the compound's edge that he could reach Kene in the time it "
        "takes to draw one breath, rotated often enough that no watcher "
        "could learn his habits either. It costs the boy very little. "
        "It costs this family considerably less than the alternative.\""
    )},
    {"type": "body", "text": (
        "Amara looked at Obi, and some silent argument passed between "
        "them the way it had across two children and a whole difficult "
        "season, before she nodded, slowly, her agreement costing her "
        "something visible even as she gave it. \"Do it,\" she said. "
        "\"But I want to choose which of your men it is myself. If my "
        "son is going to have a shadow he does not know is there, I "
        "would like to have looked the man in the eye first.\" Chidebe "
        "accepted the condition without argument, recognizing in it "
        "the same hard won caution this whole family had been forced "
        "to learn one danger at a time."
    )},
    {"type": "body", "text": (
        "Obi, still holding Kene, pressed his lips briefly to the "
        "boy's head, the small, ordinary gesture of a father who had "
        "just heard, in careful adult language, exactly how thin the "
        "line protecting his son's ordinary life had suddenly become. "
        "\"He does not need to know any of this,\" he said. \"Not yet. "
        "Let him keep his stream and his games a while longer, even if "
        "we cannot let him keep them entirely unwatched.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A FULL DAY, UNFELT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The specialist reached the high ground overlooking Oso's "
        "outer tree line two full days before either old power sensed "
        "anything at all, having learned across a lifetime of this "
        "exact work that the last stretch of any approach mattered more "
        "than all the ones before it combined. They carried little "
        "beyond what a common traveler might carry, plain cloth worn "
        "soft from years of walking rather than any mark of the Ijoma "
        "Concern's coin, and settled into the tree line's shadow with "
        "the unhurried stillness of someone who had long ago stopped "
        "measuring this kind of work in days at all."
    )},
    {"type": "body", "text": (
        "They did not cross the boundary. They did not test it, or "
        "call to it, or announce themselves in any way a watching power "
        "might have noticed. They simply sat, and watched, and let the "
        "ground reveal itself at its own unhurried pace, the way it "
        "always eventually did for anyone patient enough to stop "
        "demanding it reveal itself on a schedule."
    )},
    {"type": "body", "text": (
        "They watched Idoro's ordinary rhythms first, the fields "
        "worked at dawn, the market opening at its usual hour, the "
        "soldiers' patrols moving with a discipline that told them "
        "plainly this garrison, at least, had been well trained. Twice "
        "that first day the patrol pattern changed without warning, "
        "and the specialist noted the change with something almost "
        "like respect, filing away the fact that whoever commanded "
        "this garrison had learned, recently and well, exactly the "
        "kind of watching a patient enemy relies on most."
    )},
    {"type": "body", "text": (
        "They watched the compound nearest the fields longest of all, "
        "marking the comings and goings of a woman, a man, and two "
        "young children with the same patient, unhurried attention a "
        "farmer gives a field he intends to harvest only once "
        "conditions are exactly right."
    )},
    {"type": "body", "text": (
        "Every account the specialist had ever been given about this "
        "particular ground pointed toward the mother as the guardians' "
        "most obvious weakness, the woman both powers had already once "
        "nearly lost at this very boundary. The specialist did not "
        "dismiss that account. They simply noted, watching a full day "
        "longer than the account alone would have required, that the "
        "mother moved through Idoro now with a wariness that had "
        "clearly been taught to her recently and taught well. Guarded "
        "prey, however valuable, was rarely the most efficient prey."
    )},
    {"type": "body", "text": (
        "The younger child was not guarded that way at all. He was "
        "watched, certainly, loved plainly, but moved through the "
        "compound and its nearby paths with the unguarded ease of a "
        "boy no one had ever told needed protecting from anything "
        "larger than an ordinary fall. No soldier walked at his side. "
        "No old power's attention seemed to rest on him the way it so "
        "visibly rested on the boy across the boundary, or on the "
        "mother who had learned, however belatedly, to watch her own "
        "shadow."
    )},
    {"type": "body", "text": (
        "The specialist rose at last, unhurried, having seen enough to "
        "settle the only question that had ever truly mattered to this "
        "particular work: not which target the guardians expected to "
        "be threatened, but which one they had not yet thought to "
        "protect at all. They began, without any further ceremony, to "
        "plan the patient, ordinary way they would make the second "
        "child's existence matter to them both."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: AN ORDINARY AFTERNOON AT THE STREAM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "That same afternoon, unaware of anything watching from the "
        "high ground beyond the tree line, Kene ran ahead of the "
        "soldier Chidebe had posted near the stream, laughing at some "
        "private game only he and the other children understood, and "
        "the soldier, new enough to his rotation that he had not yet "
        "learned exactly how far a small boy could get in the time it "
        "took to blink, let the distance between them stretch a few "
        "strides further than Chidebe would have allowed."
    )},
    {"type": "body", "text": (
        "Nothing happened. Kene splashed at the water's edge, called "
        "back to the other children, and returned when his own hunger "
        "decided the game had run long enough, exactly the ordinary "
        "afternoon any toddler in Idoro might have had on any other "
        "day in the village's long, unremarkable history. But the gap "
        "had opened, however briefly, closing again only because "
        "nothing yet had reason to test it, a small, unremarked proof "
        "of exactly the kind of ordinary opening a patient enough "
        "watcher would need only once."
    )},
    {"type": "body", "text": (
        "The soldier reported the lapse to Chidebe himself that "
        "evening, unprompted and plainly, the way this whole garrison "
        "had learned across a season to report its own failures rather "
        "than bury them. Chidebe did not punish him for it. He "
        "thanked him for the honesty, adjusted the rotation once more, "
        "and carried the small, ordinary fact into his own private "
        "accounting of everything this family still had left to guard "
        "against a danger that had not yet shown either of them its "
        "face, and hoped, without any real way of knowing, that "
        "honesty offered quickly enough might yet prove to be its own "
        "kind of defense against a patience neither of them could see "
        "coming."
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
    print("  THE DARK RISE — Episode 68: \"The Watcher at the Tree Line\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_68.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_68.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
