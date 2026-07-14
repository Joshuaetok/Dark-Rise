#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 87: "The Name the Trap Caught"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-02: Episode 87 opens exactly where Episode 86 ended.
Chidebe catches Emenike at the drop point with a fresh bark cloth
message already tucked beneath a marked stone, undeniable. Emenike does
not run and does not lie once confronted directly, confirming what
Chidebe already feared. Osadebe arrives from clearing Adaeku in time to
help walk Emenike back to the compound under guard rather than let the
confrontation happen in the open market. The household absorbs the
name with a mix of grief and vindication, Ozoemena's relief at being
cleared shadowed by sorrow for a man he considered a friend. The
episode closes on Emenike's only real defense, blurted out as he is
led away — that they have his sister, and he had no choice — a claim
that reframes him instantly from traitor to victim without yet
explaining who "they" are or what exactly was threatened.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_87.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Seven"},
    {"type": "title_ep_name", "text": "The Name the Trap Caught"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE STONE BY THE DROP POINT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Emenike crouched beside a flat, unremarkable stone at the "
        "market's edge, half hidden by a stall shuttered for the night, "
        "and lifted its corner with the ease of a man who had done this "
        "many times before. In the gap beneath it, a folded scrap of "
        "bark cloth already waited, tucked and ready, written in the "
        "same small careful hand Osadebe had described from the message "
        "Mfoniso had burned two days before."
    )},
    {"type": "body", "text": (
        "Chidebe stepped out of the dark before he had fully decided to. "
        "\"Emenike,\" he said, and his own voice sounded strange to him, "
        "too calm for what it was carrying. The soldier froze with the "
        "stone still lifted, and for one long, terrible moment neither "
        "man moved, the truth sitting plainly between them without "
        "needing to be spoken."
    )},
    {"type": "body", "text": (
        "Emenike did not run. He set the stone back down slowly, as "
        "though some part of him had been waiting years to be caught "
        "rather than seconds, and when he finally looked up, there was "
        "no defiance in his face at all, only an exhaustion so complete "
        "it looked almost like relief. \"You were not supposed to be "
        "watching me,\" he said quietly. \"Not tonight.\" Chidebe felt "
        "something in his chest give way, grief arriving ahead of anger "
        "the way it sometimes did with the worst news. \"I was supposed "
        "to be watching you every night,\" he said. \"I simply did not "
        "know it. That is the part I will have to carry, long after "
        "tonight is finished.\""
    )},
    {"type": "body", "text": (
        "For a moment neither of them moved to close the distance "
        "between them, the market silent around them except for a dog "
        "somewhere barking at nothing, and Chidebe found himself doing "
        "the strange, useless arithmetic grief always demanded, counting "
        "backward through every patrol, every shared meal, every night "
        "he had trusted this man with a watch that mattered, searching "
        "for the exact point where trust had quietly become blindness "
        "without his noticing the change."
    )},
    {"type": "body", "text": (
        "\"Is it true,\" Chidebe asked, though the folded bark cloth "
        "still resting beneath the stone had already answered him. "
        "Emenike did not try to deny it, and something in the plainness "
        "of his silence was worse than any lie could have been. \"Yes,\" "
        "he said finally. \"All of it. Every route, every watch, every "
        "word I have carried to that stone since before the third "
        "bend.\""
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the shape of the household's fear break "
        "apart into something new and sharper the instant Chidebe's "
        "hand closed around the message, and told the entity what had "
        "changed before he fully understood it himself. \"They have "
        "found him,\" he said. The entity was quiet for a long moment. "
        "\"Then the harder part begins now,\" it said. \"Catching a "
        "leak is simple, once you know where to look. Deciding what a "
        "house does with the person who was leaking it is never "
        "simple at all.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WALKING HIM HOME
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe arrived at a run, having finished confirming Adaeku's "
        "innocence and followed the sound of low voices to the market's "
        "edge, and took in the scene, the lifted stone, the message, "
        "Emenike's stillness, in a single sweeping glance that needed no "
        "explanation. \"We do not do this here,\" he said, already "
        "scanning the shuttered stalls for anyone else awake to see it. "
        "\"Whatever happens next happens behind our own gate, quietly, "
        "before the whole village decides it understands more than it "
        "does.\" He looked at Emenike once, hard, then softened it "
        "slightly before continuing. \"Whatever this is, it deserves a "
        "hearing, not a spectacle. He has earned at least that much "
        "from us, even tonight.\""
    )},
    {"type": "body", "text": (
        "They walked Emenike back through the dark streets between "
        "them, neither man binding his hands, both of them watching him "
        "closely all the same, and he came without resistance, without "
        "pleading, walking like a man already sentenced who saw no "
        "further point in delaying the verdict. The bark cloth message "
        "went into Osadebe's pouch unread, evidence rather than "
        "curiosity, to be examined properly once they were behind walls "
        "that could be trusted."
    )},
    {"type": "body", "text": (
        "They passed near Zara's hut on the way, and she stepped out at "
        "the sound of footsteps, drawn by instinct rather than any "
        "warning her muffled gift could still offer her. She looked at "
        "Emenike's face in the torchlight, at the careful distance the "
        "two soldiers kept from him without touching him, and understood "
        "immediately what she was seeing. \"Oh,\" she said quietly, one "
        "hand rising to her mouth. \"Oh, Emenike. Not you.\" He did not "
        "answer her. He simply looked at the ground and kept walking, "
        "and something in his refusal to meet her eyes told her more "
        "plainly than words could have that whatever had driven him to "
        "this, he had hated every day of it."
    )},
    {"type": "body", "text": (
        "Chidebe kept glancing sideways at him as they walked, hunting "
        "his own memory for the moment, the conversation, the single "
        "warning sign he must have missed across all the months this "
        "had apparently been happening, and found nothing. Emenike had "
        "simply done his duty exactly as well as he always had, every "
        "single day, while carrying this the entire time. That, more "
        "than the betrayal itself, was the part Chidebe knew he would "
        "carry longest."
    )},
    {"type": "body", "text": (
        "News of the walk through the gate reached the compound before "
        "the three men themselves did, the way news always outran "
        "anyone trying to carry it quietly, and by the time they arrived "
        "Amara, Obi, and Elder Maka were already waiting at the fire, "
        "faces caught somewhere between the relief of finally knowing "
        "and the fresh grief of what knowing had cost them."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE NAME COST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ozoemena heard the name before he saw the man, and the sound "
        "that left him was not triumph, though he had every reason to "
        "feel some small measure of it after days of unspoken suspicion "
        "resting on his own shoulders. It was grief, plain and "
        "immediate, for a soldier he had shared meals with, prayed "
        "beside, trusted without a second thought. \"I am glad it was "
        "not me,\" he said quietly to Amara, \"and I am sorry it was "
        "him, and I do not know how to hold both of those at once.\""
    )},
    {"type": "body", "text": (
        "Obi said little, watching Emenike with the particular quiet of "
        "a man who had spent the last several days silently suspecting "
        "nearly everyone he knew and now had to make peace with having "
        "been right about no one in particular, only right that someone "
        "existed. It brought him no satisfaction at all, only a fresh, "
        "colder version of the same fear that had kept him awake since "
        "Osadebe first said the word informant aloud. He wondered, "
        "watching Emenike's bowed head, whether a house could ever "
        "truly finish counting the cost of a single broken trust."
    )},
    {"type": "body", "text": (
        "Amara studied Emenike across the fire, searching his face for "
        "the coldness she had expected to find in someone capable of "
        "endangering a child for coin, and found instead only a man "
        "worn thin by something far heavier than greed. \"Why,\" she "
        "asked him directly, the only question that mattered now that "
        "the who had already been answered. \"You had a place here. You "
        "had our trust. What could possibly have been worth spending "
        "it on her behalf?\""
    )},
    {"type": "body", "text": (
        "Elder Maka moved to stand beside Amara, her own face carrying "
        "none of the household's anger, only the tired watchfulness of "
        "a woman who had seen betrayal born from fear far more often "
        "than from malice. \"Let him answer before we decide what kind "
        "of man he is,\" she said. \"A reason does not undo what was "
        "done. But it tells us whether we are dealing with an enemy or "
        "with someone an enemy has already finished hunting before we "
        "ever caught him.\""
    )},
    {"type": "body", "text": (
        "Osadebe, standing at the edge of the firelight with the bark "
        "cloth message still unread in his pouch, found himself agreeing "
        "with her more than he expected to. He had spent his career "
        "learning to treat traitors and threats as the same shape, and "
        "something about this particular unraveling refused to fit "
        "either shape cleanly. \"I want the reason,\" he said. \"And I "
        "want it understood that wanting the reason does not mean I "
        "have already decided to forgive whatever it explains.\""
    )},
    {"type": "body", "text": (
        "Emenike's composure, held together through the walk from the "
        "market and the long, silent minutes since, finally broke "
        "completely under the weight of the question, his voice cracking "
        "on the first word and barely holding through the rest. \"They "
        "have my sister,\" he said. \"They have had her for two "
        "seasons. I did not have a choice. I have never once had a "
        "choice in any of this, not from the very first message, and I "
        "would give anything, anything at all, for someone in this "
        "compound to believe that before they decide what to do with "
        "me.\""
    )},
    {"type": "body", "text": (
        "The fire cracked in the silence that followed, and no one "
        "moved to answer him right away. Amara looked at Obi, at Elder "
        "Maka, at Ozoemena's stricken face, and understood that the "
        "name the trap had caught was only the smallest part of what "
        "they now had to decide. Somewhere beyond Idoro's boundary, "
        "someone had known exactly which family a soldier loved enough "
        "to sell everything else for her, and Amara found herself "
        "wondering, with a cold new fear, how many other quiet debts "
        "like this one might still be waiting inside her own walls, "
        "unclaimed."
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
    print("  THE DARK RISE — Episode 87: \"The Name the Trap Caught\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_87.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_87.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
