#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 40: "The Uninvited"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-16: Episode 40 closes the block that began with Episode
31. The trading House's agent returns to Idoro with his "clearer
invitation" — armed men rather than a written permission — and forces a
standoff Osadebe has no clean political tool to end. When the party pushes
past the field boundary toward the iroko tree line despite every refusal,
the entity, already primed by the spike of fear rolling off the village,
makes a choice it has never made before: rather than a message or a
warning, it answers with the root wall from Episode 23 turned violent for
the first time, driving the intruders back by force rather than words.
The agent retreats wounded but alive, carrying proof to his House that
something real and dangerous guards Idoro's ground — a multi-book
complication rather than a resolved threat. The episode's true hook is
smaller and closer to home: in the instant the roots struck, the vessel,
watching from the hollow, felt something of his own surge out through
them alongside the entity for the first time, not planted, not taught,
answering a threat to a mother he has never touched with the first real
act of his own will turned outward rather than inward. Book One closes on
that image, unresolved and escalating both of the entity's problems at
once — the House now has a reason to come back in force, and the entity
now has proof the boy's will can act, not just exist.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_40.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty"},
    {"type": "title_ep_name", "text": "The Uninvited"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A CLEARER INVITATION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The agent returned three days later, exactly as he had "
        "promised, and this time he did not walk Idoro's market alone. "
        "Six men came with him, armed openly in the manner of paid "
        "guards rather than soldiers, unhurried in the same way their "
        "employer was unhurried, as though violence were simply "
        "another tool a well funded House kept in careful reserve for "
        "questions that had not been answered politely enough the "
        "first time around."
    )},
    {"type": "body", "text": (
        "\"I did say I would return with a clearer invitation,\" the "
        "agent told Osadebe, who had positioned himself at the field's "
        "edge the moment word reached him, Ozoemena and two of the "
        "boundary walkers standing close behind. \"I am not here to "
        "harm your village, Captain. I am here to walk to a tree line "
        "your own council has no legal claim to forbid me from "
        "walking to. Idoro's authority ends at Idoro's fields. What "
        "lies past them belongs to no one who has ever bothered to "
        "answer for it.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Osadebe found, for the first time since arriving in Idoro, "
        "that he had no clean tool left to reach for. He could not "
        "order the crown's soldiers against a House that paid the "
        "crown's own tribute without risking a fight Eze Amadi had "
        "never authorized. He could not physically restrain six armed "
        "men with his own small party without the confrontation "
        "becoming exactly the kind of incident Ejikeme would use to "
        "argue the whole matter had been mishandled from the start. "
        "All he had was his voice, and his voice was already spent."
    )},
    {"type": "body", "text": (
        "\"I am asking you, as a captain of the crown, to wait for "
        "written word from Udo,\" he said anyway, because saying "
        "nothing felt worse than saying something that would not "
        "hold. \"Three days. That is all I am asking.\""
    )},
    {"type": "body", "text": (
        "Amara pushed through the gathered crowd before the agent "
        "could answer, placing herself beside Osadebe with the flat, "
        "unhesitating calm of a woman who had already lost more to "
        "this exact kind of unstoppable certainty than any stranger in "
        "good cloth could threaten her with twice. \"You are asking to "
        "walk toward a thing that has killed a healer in front of "
        "this whole village and spoken directly to a captain of your "
        "own crown,\" she said. \"I am not defending your right to it. "
        "I am telling you plainly, as someone who has buried enough "
        "fear about that ground for one lifetime, that whatever you "
        "find past that tree line will not care how well your House "
        "pays you.\""
    )},
    {"type": "body", "text": (
        "The agent studied her for a long moment, the first genuine "
        "flicker of hesitation Osadebe had seen cross his face since "
        "he arrived. \"You may be right,\" he said. \"My House does not "
        "pay me to avoid danger, Madam. It pays me to measure it "
        "accurately and report what I find. If I am wrong about what "
        "waits there, I will apologize to your entire village from a "
        "hospital bed. If I am right, I will have earned the only "
        "thing my employers actually sent me here for.\""
    )},
    {"type": "body", "text": (
        "\"Three days,\" the agent repeated, almost kindly, \"is three "
        "more days a rival House has to reach this ground before mine "
        "does. I am sorry, Captain. I truly am.\" He nodded once to his "
        "men, and they began walking past the last planted stone of "
        "Ozoemena's careful boundary walk, straight toward the tree "
        "line, while the whole village that had gathered to watch held "
        "its breath together for the first time since the dibia's "
        "death, Elder Maka and Adaugo standing shoulder to shoulder at "
        "the edge of the crowd, neither one willing to look away."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT ANSWERED THEM
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had felt the shape of "
        "Idoro's fear change hours before the armed men ever reached "
        "the field, a fresh, sharp spike unlike the low steady dread "
        "it had fed on for months, closer to the particular terror a "
        "village feels when violence is walking toward it rather than "
        "simply imagined. It reached toward the source out of old "
        "habit and found, for the first time, something it had never "
        "once needed to calculate against before: armed strangers "
        "closing on its own ground with clear intent to enter it."
    )},
    {"type": "body", "text": (
        "It had grown a wall of roots once already, gently, to stop a "
        "small boy from wandering too far into sunlight. It understood "
        "now, watching six armed men cross ground no human had walked "
        "uninvited in three centuries, that gentleness had never been "
        "the wall's only shape. It had simply never yet had a reason "
        "to show the other one."
    )},
    {"type": "body", "text": (
        "It weighed the choice for less time than it had weighed "
        "almost anything else this careful season, because for the "
        "first time since claiming this ground, the calculation was "
        "not complicated by patience or concealment or what a slower "
        "answer might teach it. Men with blades were minutes from a "
        "boy who trusted the entity to keep exactly this kind of "
        "danger away from him. Every other question the entity had "
        "spent weeks turning over carefully could wait behind that one."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The roots came up out of the earth without warning, faster "
        "than growth should have allowed, thick and dark and coiling, "
        "closing around ankles and driving men off their feet before a "
        "single one of them reached the tree line itself. Those "
        "watching from the field would tell it differently for years "
        "afterward, some swearing the ground itself had simply opened, "
        "others insisting they had seen shapes moving beneath the "
        "earth long before it broke. The agent fell hardest, thrown "
        "clear by a root that moved with the deliberate, targeted "
        "violence of something that had chosen exactly whom to strike "
        "and how much to hurt him without killing him outright. Two of "
        "his guards did not rise again without help. The rest "
        "scrambled backward faster than they had walked forward, "
        "dragging their fallen employer with them toward the field and "
        "away from ground that had just proven it could reach far "
        "further than anyone had ever tested."
    )},
    {"type": "body", "text": (
        "VESSEL: FIRST DIRECT PHYSICAL ACTION AGAINST HUMAN THREAT. "
        "FORCE CALIBRATED TO WOUND, NOT KILL. OUTCOME: INTRUDERS "
        "REPELLED. COST: CONCEALMENT PERMANENTLY FORFEITED."
    )},
    {"type": "body", "text": (
        "In the hollow, the boy had been watching the way he watched "
        "everything the entity allowed him to see now, and in the "
        "instant the roots struck, something moved through him that "
        "the entity had not sent and had not shaped, a hot, sudden "
        "pulse of will aimed outward through the very roots it was "
        "already using, small and untrained and entirely his own, "
        "reaching toward the danger closing on a mother he had never "
        "touched with the same fierce, unthinking speed a much older "
        "child might reach out to catch something falling."
    )},
    {"type": "body", "text": (
        "The entity felt it arrive inside its own strike the way a "
        "second hand might close over a hand already gripping a "
        "blade, not fighting for control of the motion, simply adding "
        "its own weight to it, and understood, in the same instant it "
        "watched the agent dragged bleeding back across the boundary "
        "stones, that the force which had just driven six armed men "
        "off Idoro's ground had not come from the entity alone."
    )},
    {"type": "body", "text": (
        "It turned to look at him properly for the first time since "
        "the roots fell still, and found the boy staring back at his "
        "own hands, small and shaking and entirely unhurt, with an "
        "expression the entity had never once had to teach him and "
        "could not now claim to fully understand."
    )},
    {"type": "body", "text": (
        "\"I felt them,\" the boy said, before the entity could ask "
        "anything at all. \"The men. They wanted to hurt someone. I "
        "did not think about it. I just did not want them to reach "
        "her.\" He was not crying, though something in his voice "
        "suggested he had come close, a child's plain shock at "
        "discovering a door inside himself he had never once known "
        "how to open, opened anyway, entirely on its own, the instant "
        "it mattered."
    )},
    {"type": "body", "text": (
        "The entity considered, and discarded, every careful, half "
        "true answer it might once have reached for first. \"You "
        "protected your mother,\" it told him instead, plainly, the "
        "same plainness it had promised itself days ago and only now "
        "fully understood the weight of. \"You have never met her. You "
        "still knew, without being taught, that she was worth "
        "reaching for. That is not something I gave you. I do not "
        "know where it came from. I only know it is yours.\""
    )},
    {"type": "body", "text": (
        "Somewhere past the field, a wounded man was already being "
        "carried toward a House that would want to know exactly what "
        "had just happened to him, carrying proof of Idoro's danger "
        "back to employers who would not let a beating stop them so "
        "much as sharpen their appetite for whatever had delivered it. "
        "Somewhere far beyond even the iroko roots, something far "
        "older than either of them had almost certainly felt the boy "
        "reach outward and use his will for the very first time, and "
        "the entity, watching him gather his stones back into their "
        "unfinished pattern with hands that had just struck down grown "
        "men without meaning to, understood that concealment had "
        "ended tonight in more ways than one. The boy was no longer "
        "only something the entity was shaping. He had just shown "
        "them both, and everything watching from every direction at "
        "once, that he could act."
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
    print("  THE DARK RISE — Episode 40: \"The Uninvited\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_40.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_40.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
