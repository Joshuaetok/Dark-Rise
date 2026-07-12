#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 23: "The Edge of Oso"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-30: Episode 23 turns fully to Oso for the first time in
several episodes. The vessel, now walking steadily and stringing small
sentences together, makes his first real attempt at independent will: he
walks away from the ak-pu roots entirely, toward the direction some
instinct tells him leads to the word he has been repeating since Episode
20. The entity, curious about exactly how far this new independence
might carry him, lets him go further than it has ever allowed before,
right up to the edge of Oso itself, before finally stopping him with a
gentle but absolute use of its power. The exchange that follows is the
first real conversation between them, the boy asking a question the
entity cannot answer honestly without costing itself something, and
answering instead with a careful, partial truth. In Idoro, a brief
grounding scene shows Amara and Obi still absorbing Ozoemena's threat
from Episode 22, unaware that a mile away, in Oso, their son has just
taken his first steps toward finding them.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_23.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Three"},
    {"type": "title_ep_name", "text": "The Edge of Oso"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A HOUSEHOLD STILL BRACING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara had not slept well since Ozoemena's visit, turning his "
        "threat over each night the way she had once turned over Elder "
        "Maka's, searching for the shape of the danger before it found "
        "her first."
    )},
    {"type": "body", "text": (
        "\"He will not attempt the dibia soon,\" Obi said, more to "
        "reassure himself than her. \"Elder Maka's warning will have "
        "shaken him, whatever he lets the others see on his face.\""
    )},
    {"type": "body", "text": (
        "\"He will attempt it eventually,\" Amara said. \"Men like him "
        "do not absorb warnings. They store them away as reasons to "
        "prove the warning wrong. I have watched enough of them in my "
        "life to know the shape of it before it happens.\""
    )},
    {"type": "body", "text": (
        "Kene slept on undisturbed in his basket nearby, growing the "
        "ordinary way ordinary children grow, and Amara found herself, "
        "not for the first time, grateful for a kind of peace that had "
        "cost so much to buy that she could not quite let herself trust "
        "it yet."
    )},
    {"type": "body", "text": (
        "She watched him a long while that evening, the small rise and "
        "fall of his chest, the ordinary softness of a sleeping child "
        "with nothing hidden left in him for anyone to find, and let "
        "herself feel, for just a few minutes, the particular grief she "
        "rarely allowed herself the space to feel at all. Somewhere "
        "beyond the fields, in a forest she had never once let herself "
        "walk toward, her other son was growing too, shaped by hands "
        "that were not hers, learning a world she had no part in "
        "teaching him. She did not know if he was loved, in whatever way "
        "the thing that claimed him understood loving. She only knew he "
        "was alive, and that the knowing had never once stopped aching."
    )},
    {"type": "body", "text": (
        "Obi found her still sitting there when he came to bank the "
        "fire for the night, and did not ask what she was thinking "
        "about. Some griefs did not need to be spoken aloud between two "
        "people who had already carried them together this long."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — HOW FAR HE WALKED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In the hollow beneath the ak-pu roots, the boy woke before the "
        "entity expected him to, and did not wait, the way he had "
        "always waited before, for the day's shapes and sounds to be "
        "offered to him. He stood, steadier on his legs than he had ever "
        "been, and walked."
    )},
    {"type": "body", "text": (
        "Not in circles around the hollow, the way he had practiced "
        "walking every day since he first stood unassisted. Outward. "
        "Toward the thin gray light that marked the tree line, small "
        "bare feet finding their way across roots and packed earth with "
        "a purpose the entity had not placed in him and had not seen "
        "coming."
    )},
    {"type": "body", "text": (
        "\"Mama,\" he said, quietly, to no one, the way a person "
        "repeats an instruction to keep from losing hold of it, and "
        "kept walking."
    )},
    {"type": "body", "text": (
        "He did not know, in any way he had words yet to hold, what "
        "the word actually meant, or why some blind, wordless part of "
        "him had decided that walking in this particular direction, and "
        "not any other, was the same thing as reaching whatever the word "
        "pointed toward. He only knew the pull of it, steady and "
        "certain in a way almost nothing else in his short life had yet "
        "been certain, and his small feet obeyed the pull before the "
        "rest of him had finished deciding to follow it."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The entity could have stopped him at the first root. A single "
        "thought would have been enough, the same small adjustment it "
        "had once considered and declined to make when the word first "
        "surfaced. It found itself, instead, curious enough to let the "
        "small experiment continue, wanting to know, with the same "
        "patient attention it gave everything it had not yet fully "
        "understood, exactly how far an unshaped want could carry a body "
        "before the body's own limits caught up to it."
    )},
    {"type": "body", "text": (
        "He walked further than he ever had. Past the hollow's usual "
        "boundary, past the ring of younger ak-pu saplings that marked "
        "the edge of the entity's oldest and surest reach, out toward "
        "the thinning trees where the forest's dark gave slowly onto "
        "ordinary daylight and, beyond that, though neither of them "
        "could see it yet, the sloping fields that led toward Idoro "
        "itself."
    )},
    {"type": "body", "text": (
        "He stumbled twice on ground his small feet had never learned "
        "the shape of, and picked himself back up both times without "
        "crying, the same stubborn small motion the entity remembered "
        "from his first attempts at standing months of growth ago, and "
        "kept walking, one word carrying him further than any lesson "
        "the entity had ever poured into him."
    )},
    {"type": "body", "text": (
        "The entity followed the whole of the small journey without "
        "once revealing itself, weighing, as it walked its own patient "
        "attention alongside him, exactly how much of this stubbornness "
        "had been shaped by its own careful teaching and how much of it "
        "had simply always been waiting inside the boy, ready to surface "
        "the moment he found a want large enough to need it. It had "
        "built his hunger. It had built his fear. It had not, so far as "
        "it could tell, built this particular refusal to stay where he "
        "was placed, and the not knowing sat strangely against three "
        "centuries of otherwise near total certainty about everything "
        "growing beneath these roots."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "VESSEL: UNPROMPTED DIRECTIONAL MOVEMENT TOWARD BOUNDARY. DISTANCE EXCEEDS ALL PRIOR OBSERVED RANGE. INTERVENTION PENDING."},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The entity let him reach the very edge of the old growth, "
        "close enough that the ordinary sun fell fully across his face "
        "for the first time in his short, strange life, before it "
        "finally moved."
    )},
    {"type": "body", "text": (
        "It did not frighten him. It reached through the roots nearest "
        "his feet, gently, and let them rise just enough to bar the "
        "path forward without ever touching him directly, a wall grown "
        "rather than a hand laid on him. The boy stopped, confused, and "
        "pushed once against the barrier with both small hands before "
        "understanding, in the wordless way understanding still mostly "
        "arrived for him, that this door, unlike every other shape in "
        "his short life, would not open simply because he wanted it to."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: OSO — THE FIRST QUESTION HE ASKED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"Mama,\" he said again, and this time there was a different "
        "shape in it, not practice, not comfort, but something closer "
        "to a question, small and raw and aimed, for the first time, "
        "directly at the presence he had always felt nearest to him."
    )},
    {"type": "body", "text": (
        "The entity considered its answer carefully, aware, in a way it "
        "had not needed to be aware with any other thread it had ever "
        "built, that whatever it said now would become part of the "
        "shape this particular mind carried forward for the rest of a "
        "very long life."
    )},
    {"type": "body", "text": (
        "\"Not yet,\" it said, using the low, wordless register it had "
        "always used to speak directly into him, the closest thing to a "
        "voice it had ever needed with this one thread. \"You are not "
        "ready for her yet, and she is not ready for you. When you are "
        "both ready, the door will open on its own. Until then, walking "
        "toward it before its time will only hurt you both.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It was not the whole truth. The whole truth was longer, "
        "colder, and involved a village that would very likely kill him "
        "on sight if he arrived as he was now, half formed and unable "
        "yet to explain himself in any language Idoro would recognize as "
        "innocent. The entity judged, weighing the boy's small, "
        "stricken face against the value of that fuller truth, that a "
        "kinder incompleteness would serve them both better tonight."
    )},
    {"type": "body", "text": (
        "There was a colder truth beneath even that one, a truth the "
        "entity did not offer him at all. That it had its own reasons "
        "for keeping the door closed a while longer, reasons that had "
        "very little to do with the boy's safety and a great deal to do "
        "with how much more useful an unfinished vessel remained here, "
        "beneath these roots, than a finished one loose in a world the "
        "entity could not yet fully control from a distance. It did not "
        "examine too closely whether withholding that reason from him "
        "counted as the same kind of lie Amara had once told her own "
        "husband, or something worse."
    )},
    {"type": "body", "text": (
        "The boy sat down hard in the dirt at the base of the new root "
        "wall, and cried, the first real tears the entity had ever felt "
        "move through him, and did not fight when the roots curled "
        "gently around his small shoulders and drew him back, unhurried, "
        "toward the hollow he had tried to leave."
    )},
    {"type": "body", "text": (
        "The entity held him through the worst of it, patient in the "
        "particular way it had learned patience across three centuries "
        "of watching everything it touched eventually want something it "
        "could not yet have, and found, once the crying had finally "
        "worn itself down into an exhausted, hiccuping sleep, that it "
        "was already turning over the same question it had first asked "
        "itself the night the boy spoke his single unshaped word."
    )},
    {"type": "body", "text": (
        "It had built empires of patience out of far less promising "
        "material than this. It told itself that now, holding a "
        "sleeping child who had just walked further from it, in every "
        "sense that mattered, than any thread it had ever tended before, "
        "and found the telling did not settle the unease nearly as "
        "completely as it once would have."
    )},
    {"type": "body", "text": (
        "How much longer could a door this determined to open be kept "
        "closed by patience alone, and what, exactly, would be waiting "
        "on the other side of it by the time patience finally ran out."
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
    print("  THE DARK RISE — Episode 23: \"The Edge of Oso\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_23.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_23.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
