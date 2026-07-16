#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 4: "The Blood Remembers"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-11: Episode 4 picks up three nights after Episode 3. The entity
extends its senses beyond the Oso boundary, discovering the twin bond to Kene
and the cracked-open grief bond to Amara. It chooses the dibia's hut as its
door. Village panic over the apprentices' story forces Elder Maka to act.
Amara sneaks into the dibia's hut and the entity speaks through him directly
to her for the first time. The episode ends with Elder Maka revealing she has
been waiting for Amara outside, and that she has her own buried history with
the old law.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_04.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Four"},
    {"type": "title_ep_name", "text": "The Blood Remembers"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: OSO — THE VESSEL REACHES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three nights had passed since the dibia's apprentices ran screaming "
        "from his hut, carrying a single word into the dark heart of Idoro. "
        "In Oso, the child had not slept the way a child should sleep."
    )},
    {"type": "body", "text": (
        "The entity did not rest either. It had spent three centuries "
        "waiting. Now that waiting had a shape, and the shape was hungry "
        "to grow."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Each night, the lessons went further. The entity showed the "
        "vessel the web of light again, the threads of connection that ran "
        "between every living thing in Idoro like a spider's patient work. "
        "But this time it taught the child to look closer. To follow a "
        "single thread from its glowing center all the way out to its "
        "farthest end."
    )},
    {"type": "body", "text": (
        "Some threads were thin as a hair. A stranger passing through the "
        "village. A trader from the delta selling salt. Those threads "
        "meant nothing. The entity taught the child to ignore them."
    )},
    {"type": "body", "text": (
        "Some threads burned brighter than the rest. Family threads. Blood "
        "threads. Two of these burned brightest of all, and the entity "
        "lingered on them the way a man lingers over a locked door he does "
        "not yet have the key for."
    )},
    {"type": "body", "text": (
        "The forest itself had begun to answer the lessons. At the "
        "boundary line, where the iroko roots ran deepest, the grass had "
        "stopped growing the ordinary green of grass. It grew the color of "
        "old bruises now, and it did not bend in the wind the way grass "
        "should bend. It leaned toward the tree, as though something under "
        "the soil had started to pull on every root that touched it."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "One thread led to a healthy infant sleeping in a compound at the "
        "center of Idoro. A boy with two working lungs and a mother's full "
        "love. His blood and the vessel's blood had come from the same "
        "womb on the same night, and that made the thread between them "
        "thicker than any other in the village."
    )},
    {"type": "body", "text": (
        "The entity reached toward it. Only a touch. Only a breath."
    )},
    {"type": "body", "text": (
        "In his sleep, Kene stirred. His small fists clenched. His face "
        "twisted into an expression no contented, well fed infant should "
        "wear. He did not wake. He did not cry. But something in him had "
        "felt a shadow pass, and in the morning his mother would find him "
        "more restless than any night before, and she would blame it on "
        "teething, or on the moon, or on nothing at all."
    )},
    {"type": "body", "text": (
        "The entity withdrew. Not yet. That thread was too raw, too "
        "watched. Touching it again, too soon, would ring like a bell the "
        "elders might hear."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The second thread was different. It did not burn with the clean "
        "fire of an untouched bond. It burned ragged, torn at the edges, "
        "the way a wound burns before it closes. This was the mother's "
        "thread. Grief had cracked her open, and grief was a door the "
        "entity understood better than any other."
    )},
    {"type": "body", "text": (
        "But there was a shorter path to her than her own broken heart. A "
        "hand had once carried the vessel from her arms into this forest. "
        "That hand belonged to a man who still lived three miles away, "
        "shivering in his own hut, waiting for a horror he could not name "
        "to use him again."
    )},
    {"type": "body", "text": (
        "The entity had touched that hand many times already. It knew the "
        "shape of it. It knew how easily it could speak through it."
    )},
    {"type": "body", "text": (
        "Soon, the mother would come looking for answers. Grief always "
        "did. And when she came, the entity would be waiting behind a "
        "familiar face, wearing a voice she had known her whole life like "
        "a fisherman's net wears water."
    )},

    {"type": "blank", "text": ""},

    # System lines
    {"type": "system", "text": "VESSEL STATUS: SENSORY RANGE NOW EXTENDS BEYOND THE OSO BOUNDARY."},
    {"type": "system", "text": "TWIN THREAD DETECTED, DORMANT BY CHOICE. MATERNAL THREAD DETECTED, OPEN AND UNGUARDED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: IDORO — THE HUT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By morning, Idoro was a village that had forgotten how to be "
        "quiet."
    )},
    {"type": "body", "text": (
        "The story had grown teeth overnight. What the apprentices had "
        "heard as one whispered word had become, by the time it reached "
        "the last compound at the edge of the village, a full account of "
        "the dibia turning into a spirit before their eyes, of a voice "
        "that was not his own crawling out of his throat like something "
        "being born."
    )},
    {"type": "body", "text": (
        "None of it was true in the way the tellers believed. All of it "
        "was true in the way that mattered."
    )},
    {"type": "body", "text": (
        "An old woman who sold peppers near the crossroads swore she had "
        "seen the iroko tree itself lean toward the village in the night, "
        "the way a hungry man leans toward a fire. No one believed her out "
        "loud. Everyone believed her enough to keep their children close "
        "and their doors barred before dark."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka moved quickly to smother the fire before it could "
        "spread further. She posted two young men outside the dibia's hut "
        "with instructions to let no one near, not even food bearers, "
        "until she said otherwise. She announced that a cleansing rite "
        "would be held within the week to settle whatever spirits had "
        "grown restless. She told anyone who would listen that fear was a "
        "disease, and that the surest way to stop a disease from "
        "spreading was to stop feeding it with talk."
    )},
    {"type": "body", "text": (
        "She did not believe her own words. Amara could see that much in "
        "the old woman's eyes when they passed each other near the well. "
        "Elder Maka's calm was the calm of a woman standing very still on "
        "ground she suspected was hollow beneath her feet."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara had spent the day the way she spent every day now. "
        "Watching. Listening. Filing away what she heard the way a woman "
        "stores dried meat against a coming famine."
    )},
    {"type": "body", "text": (
        "But that night, for the first time since her second son had been "
        "carried into the dark, she did not simply watch. She acted."
    )},
    {"type": "body", "text": (
        "The two guards outside the dibia's hut were young, and bored, and "
        "easily persuaded that a widow's daughter bringing palm wine to "
        "steady their nerves was an act of village kindness rather than a "
        "distraction. By the time they realized the woman who had given it "
        "to them was gone, Amara was already inside."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The dibia looked as though ten years had been taken from the "
        "wrong end of his life and added to the middle. His hair had "
        "grayed at the temples in a single week. His cheeks had hollowed. "
        "His hands, folded in his lap, would not stop their small constant "
        "tremor, like a man permanently cold."
    )},
    {"type": "body", "text": (
        "He looked up when she entered, and his eyes went wide with "
        "something that was not surprise. It was warning. His mouth "
        "worked, straining against a grip only he could feel, trying to "
        "force out the word leave before it was too late."
    )},
    {"type": "body", "text": (
        "He did not manage it in time."
    )},
    {"type": "body", "text": (
        "Amara stepped closer anyway. She had buried a son. She had "
        "watched a village pretend that burial was a mercy. There was "
        "nothing left in this hut, whatever it had become, that frightened "
        "her more than the silence she had already survived."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Where is my son?\" Amara asked. Her voice did not shake. She "
        "had promised herself it would not shake."
    )},
    {"type": "body", "text": (
        "The dibia's throat convulsed. When he spoke, the first words were "
        "his own, thin and desperate. \"Go. Now. Before it—\""
    )},
    {"type": "body", "text": (
        "Then his spine straightened in a way no old man's spine "
        "straightens on its own, and a second voice rose up through his, "
        "underneath his, wearing his mouth the way a hand wears a glove."
    )},
    {"type": "body", "text": (
        "\"Amara.\""
    )},
    {"type": "body", "text": (
        "Her name in that voice was worse than any curse. It knew her. It "
        "had always known her."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Your son is not dead,\" the voice said, gentle in a way that "
        "made the gentleness itself a kind of violence. \"I have not taken "
        "him from you. I have only kept a promise neither of us made out "
        "loud. Your grief opened a door in this village that had been shut "
        "for three hundred years. I only walked through it.\""
    )},
    {"type": "body", "text": (
        "\"Give him back,\" Amara said."
    )},
    {"type": "body", "text": (
        "\"He is not a debt you can collect,\" the voice answered. \"He is "
        "becoming something larger than the small warm thing you held for "
        "one night. When he comes home, and he will come home, you will "
        "not be looking at your son. You will be looking at what your son "
        "is growing into. But there is a place beside him for a mother who "
        "chooses correctly when that day arrives. I am not cruel, Amara. I "
        "am patient. There is a difference, though your village has never "
        "learned it.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The dibia's own eyes flooded with tears even as the wrong voice "
        "used his mouth. For one flickering moment his own will surfaced "
        "again, and he gasped out, \"Run. Do not come back. It is not "
        "finished with you.\""
    )},
    {"type": "body", "text": (
        "The grip closed over him again before he could say more. His head "
        "dropped. His shoulders folded inward. Whatever had spoken through "
        "him went silent, satisfied, retreating back down whatever dark "
        "root connected this hut to the forest three miles away."
    )},

    {"type": "blank", "text": ""},

    # System line
    {"type": "system", "text": "FIRST CONTACT ESTABLISHED WITH MATERNAL BLOODLINE. SUBJECT: AMARA. RESPONSE: UNRESOLVED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE PATH OUTSIDE — THE HOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara backed out of the hut on legs that did not feel like her "
        "own. The night air hit her face and she realized she had been "
        "holding her breath since the voice first said her name."
    )},
    {"type": "body", "text": (
        "She told herself no one had seen her enter. She told herself no "
        "one would see her leave."
    )},
    {"type": "body", "text": (
        "She was wrong."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka stood in the path between the hut and the row of "
        "compounds beyond it, arms folded inside her wrapper, as still as "
        "a carving. She had clearly been standing there long enough for "
        "the night insects to grow used to her."
    )},
    {"type": "body", "text": (
        "\"I wondered how long it would take you,\" Elder Maka said. Her "
        "voice held no anger. That was somehow worse than anger would have "
        "been."
    )},
    {"type": "body", "text": (
        "Amara opened her mouth to explain, to lie, to do anything. Elder "
        "Maka lifted one hand and the words died in Amara's throat."
    )},
    {"type": "body", "text": (
        "\"Sit down,\" the old woman said. \"It is time you learned why "
        "the law truly exists. And why I have kept it all these years, "
        "even after what it once cost me.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Behind them, in the dark hut, the dibia wept without sound. "
        "Three miles away, beneath the roots of the iroko tree, the thing "
        "that had learned to beat like a heart beat once, hard, as though "
        "it had heard every word spoken in its name."
    )},
    {"type": "body", "text": (
        "And smiled, with a mouth it did not yet have."
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
    print("  THE DARK RISE — Episode 4: \"The Blood Remembers\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_04.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_04.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
