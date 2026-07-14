#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 96: "What the Surveyors Saw"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-11: Episode 96 opens the new arc Episode 95 set in
motion. The crown survey, now named under its lead surveyor Ubani,
spends several days working steadily closer to Oso's tree line. Ubani,
a careful and observant man rather than a superstitious one, begins
noticing details that do not fit any ordinary patch of forest: no
birdsong past a certain point, wind that moves the canopy but never
quite reaches the ground, a stillness his measuring instruments cannot
account for. Chidebe and Amara try, without lying outright, to steer
his attention elsewhere, but Ubani's professional curiosity only
sharpens the more carefully it is redirected. In Oso, the entity feels
the survey's slow approach as a mounting pressure it cannot yet name
a response to, still too weak to consider showing itself even
defensively. The episode closes on Ubani informing Chidebe, politely
but immovably, that he intends to walk the boundary himself the
following morning to complete an honest map, whatever the village's
evident discomfort with the idea.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_96.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Six"},
    {"type": "title_ep_name", "text": "What the Surveyors Saw"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A MAN WHO NOTICED THINGS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ubani had surveyed river crossings, disputed farmland, and "
        "once an entire flooded district for the crown's tax rolls, and "
        "prided himself, above every other quality a surveyor could "
        "claim, on noticing exactly what his instruments told him and "
        "nothing his imagination tried to add to it. By the fourth day "
        "at Idoro, his instruments had begun telling him something he "
        "did not know how to write down."
    )},
    {"type": "body", "text": (
        "\"The birds stop,\" he told his second, a quiet young man named "
        "Ude who carried the measuring chain, \"exactly forty paces "
        "before that tree line. Not gradually. Exactly. I have marked "
        "the point three times now and it does not move.\" Ude, who had "
        "grown up two villages from Idoro and knew better than to say "
        "so aloud to a crown official, only nodded and kept his eyes on "
        "the chain."
    )},
    {"type": "body", "text": (
        "He had learned, across fifteen years of commissions, to trust "
        "the small anomalies more than the large ones, since a large "
        "strangeness usually announced itself and invited its own "
        "explanation, while a small one, repeated and consistent, "
        "almost always pointed toward something real that someone, "
        "somewhere, had gone to considerable trouble to keep hidden."
    )},
    {"type": "body", "text": (
        "Ubani noticed other things too, in the patient, cataloguing "
        "way that had made him good at his work for fifteen years. The "
        "canopy at Oso's edge moved in a wind he could feel clearly on "
        "his own skin, and yet the undergrowth beneath it stayed "
        "utterly still, as though some barrier he could not measure "
        "separated what the treetops felt from what the ground allowed. "
        "He wrote none of it into his official log yet. He wrote all of "
        "it into a private notebook he had kept, out of old habit, "
        "since his very first commission."
    )},
    {"type": "body", "text": (
        "Ude, walking the chain line behind him that evening, finally "
        "found the courage to speak what half the village would have "
        "told Ubani outright if any of them had trusted a crown "
        "official enough to try. \"That is Oso,\" he said quietly. "
        "\"Where the old law once sent children no one wanted to keep. "
        "People here do not walk it. Not from superstition alone. From "
        "respect for grief too old and too heavy to disturb.\" Ubani "
        "heard the warning in it, and filed it carefully alongside "
        "everything else he had observed, neither dismissing it nor "
        "letting it decide his work for him."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT COULD NOT BE SAID PLAINLY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka, hearing of the survey's slow creep toward the tree "
        "line from Amara that same morning, weighed the danger with the "
        "particular gravity of a woman who had spent decades guarding "
        "this exact secret from every direction it had ever threatened "
        "to leak. \"We have kept this from soldiers, from a hunter, "
        "from the crown itself for longer than either of us has been "
        "alive,\" she said. \"I did not expect the danger, when it "
        "finally came from Udo, to be simple honesty.\""
    )},
    {"type": "body", "text": (
        "Chidebe found an excuse to walk beside Ubani on the fifth "
        "morning, keeping his tone as light as the subject allowed. "
        "\"That ground past the tree line is old and troubled,\" he "
        "said. \"Idoro has kept its distance from it for generations. I "
        "would not trouble your survey with it. There is nothing there "
        "worth the crown's ink.\" Ubani listened politely, the way a "
        "careful man listens to information he has already decided not "
        "to accept without testing it himself. \"Every surveyor is told "
        "that about some patch of ground or other,\" he said. \"It is "
        "usually true. I have learned not to assume it always is.\""
    )},
    {"type": "body", "text": (
        "Amara tried a gentler approach that same afternoon, inviting "
        "Ubani to share a meal and steering the conversation toward "
        "Idoro's oldest customs, the abandonment site's place in the "
        "village's grief, the old law that had shaped so much of its "
        "history. She hoped the weight of genuine sorrow might do what "
        "Chidebe's caution had not. Ubani listened with real respect, "
        "and thanked her for trusting him with it, and did not offer, "
        "in return, any promise to leave the ground unmeasured."
    )},
    {"type": "body", "text": (
        "\"You are a mother who has buried grief in that ground her own "
        "way,\" Ubani said to her gently, when the meal had ended and "
        "the silence between them had grown honest enough to permit it. "
        "\"I do not intend to disturb what belongs to your sorrow. I "
        "intend to draw an accurate line around it, so the crown never "
        "again sends men who do not understand what they are walking "
        "toward. I would think a mother who has survived what this "
        "village has survived might want exactly that, more than she "
        "wants the ground left a mystery.\" Amara had no honest answer "
        "for him that did not risk revealing more than she dared, and "
        "so she offered none, letting the silence stand where words "
        "would only have cost her something she could not afford to "
        "spend."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the mounting pressure of the survey's "
        "attention the way a man feels a storm building before the "
        "first cloud is visible, and carried his unease straight to the "
        "entity rather than sit with it alone. \"They will not simply "
        "look away because we ask kindly,\" he said. \"Ubani wants an "
        "honest map. He believes that is worth more than a village's "
        "comfort.\" The entity, listening from a stillness that still "
        "cost it visibly to hold, offered no easy answer. \"An honest "
        "man is harder to deceive than a dishonest one,\" it said. "
        "\"That has always been the trouble with them.\""
    )},
    {"type": "body", "text": (
        "The presence, listening from further away, offered a colder "
        "practicality neither Chibundu nor the entity had yet allowed "
        "themselves to voice aloud. \"You are both treating this as a "
        "question of whether he sees something,\" it said. \"The truer "
        "question is what he does afterward, if he does. A crown "
        "surveyor who tells his masters the truth is a very different "
        "danger than a hunter who tells no one at all.\""
    )},
    {"type": "body", "text": (
        "Osadebe, brought in once Chidebe's concern reached him, "
        "considered simply ordering the survey redirected on the "
        "crown's own authority, and discarded the idea almost as "
        "quickly as he formed it. \"Ejikeme sent him to give the crown "
        "an honest account,\" he said. \"If I order him away from the "
        "one patch of ground that makes him curious, I hand him the "
        "clearest possible reason to become more curious, not less. We "
        "cannot out order a man's own good instincts. We can only hope "
        "to outlast them.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT UBANI DECIDED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ubani found Chidebe again near dusk, his private notebook "
        "still in hand, and delivered his decision with the same "
        "unhurried courtesy he had shown every day since his arrival, "
        "which made it no easier for Chidebe to hear. \"I have measured "
        "everything I can measure from outside that tree line,\" he "
        "said. \"Instruments only tell a surveyor so much. Tomorrow I "
        "intend to walk the boundary myself and see the rest with my "
        "own eyes, as I would for any ground this unusual.\""
    )},
    {"type": "body", "text": (
        "He said it without any hint of threat, the plain statement of "
        "a professional describing tomorrow's ordinary work, which made "
        "it, to Chidebe's ear, considerably harder to argue against "
        "than if the man had shown the smallest trace of malice."
    )},
    {"type": "body", "text": (
        "\"I would ask you to reconsider,\" Chidebe said, choosing each "
        "word carefully now, aware he was standing at the exact edge of "
        "how much caution he could offer without crossing into a lie "
        "outright. \"Not as an order. As a request from a man who has "
        "buried more of this village's fear than I ever wanted to.\" "
        "Ubani heard the weight in it, and did not dismiss it lightly, "
        "but did not bend either. \"I hear the request,\" he said "
        "gently. \"I am still going to walk it. A map that leaves out "
        "the one piece of ground everyone is afraid of is not an honest "
        "map at all. It is simply a shape drawn around a fear no one "
        "will name.\""
    )},
    {"type": "body", "text": (
        "Chidebe carried the news back to the compound that evening "
        "with none of the relief a completed survey should have "
        "brought, and found Amara waiting for him at the fire already "
        "reading the outcome in his face before he spoke a single word "
        "of it. \"He is going in tomorrow,\" she said, not a question. "
        "Chidebe nodded once, grim. \"At first light. I could not talk "
        "him out of it, and I could not order him out of it without "
        "making him more certain something was worth ordering him away "
        "from.\""
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt the decision settle over the household "
        "before Chibundu had finished relaying it, a slow, cold "
        "certainty moving through ground that had not been walked by an "
        "outsider's honest curiosity in three hundred years. \"Then we "
        "will learn tomorrow,\" it said quietly, \"exactly how much of "
        "us an ordinary, careful man is capable of seeing, whether we "
        "wish him to or not.\""
    )},
    {"type": "body", "text": (
        "Amara sat awake long past the rest of the compound's sleep, "
        "turning over every version of the next morning she could "
        "imagine, none of them fully within her control. She had spent "
        "seasons learning to fight a hunter who wanted her family dead. "
        "She did not yet know how to fight a good man who only wanted "
        "the truth, and found, unhappily, that the second kind of "
        "danger left her with far fewer tools than the first ever had."
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
    print("  THE DARK RISE — Episode 96: \"What the Surveyors Saw\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_96.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_96.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
