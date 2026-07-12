#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 14: "The Whisper"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-21: Episode 14 moves the entity's plan for Zara forward from
nighttime sleepwalking to a waking intrusion, its first attempt at a two way
channel with her rather than simple motor control. Zara, now spending most of
her days at Amara's compound since the village turned on her, begins losing
small moments while awake, her hand moving without her intending it. Amara,
already secretly carrying suspicion about what she glimpsed in Elder Maka's
eyes during the binding rite, says nothing of it yet, choosing to focus on
what she can see clearly in front of her. In Oso, the entity treats the
waking intrusion as the necessary next step before it can risk speaking
through Zara the way it once spoke through the dibia. The episode closes
with Zara hearing a single, direct address inside her own mind for the
first time, quiet and personal, confirming the entity now has a voice
waiting behind her eyes as well as command of her hands.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_14.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fourteen"},
    {"type": "title_ep_name", "text": "The Whisper"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT ZARA'S HANDS DID WITHOUT HER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara had been sleeping most nights at Amara's compound for a "
        "week now, an arrangement neither woman had spoken aloud but "
        "both understood, and in daylight she still tried to make "
        "herself useful, grinding leaves and mending cloth as though "
        "keeping her hands busy could hold the rest of her together."
    )},
    {"type": "body", "text": (
        "The two watchers beneath the mango tree had grown used to her "
        "presence by now, and no longer looked up from their own quiet "
        "conversation when she crossed the yard, though Amara suspected "
        "every word said within that compound still found its way back "
        "to Elder Maka eventually, filtered through whatever careful "
        "report the two young men gave at the end of each day. It no "
        "longer frightened her the way it once had. There were larger "
        "things to be frightened of now than two bored men beneath a "
        "tree."
    )},
    {"type": "body", "text": (
        "It was in the middle of that ordinary work, sorting bitter "
        "leaf into two baskets by size, that her hand stopped listening "
        "to her for the first time in broad daylight."
    )},
    {"type": "body", "text": (
        "She did not lose the whole of herself the way she had lost "
        "herself walking toward Oso in her sleep. She was awake for all "
        "of it, aware, watching her own fingers the way a person watches "
        "a stranger's hands, as they set the leaf aside and traced, "
        "slowly and with great care, a shape in the loose dirt at her "
        "feet that she did not recognize and had not chosen to draw."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Amara,\" she said, and her voice came out smaller than she "
        "intended, the voice of a woman reporting a fire she has just "
        "noticed catching in her own roof. \"Come and see this.\""
    )},
    {"type": "body", "text": (
        "Amara crossed the yard quickly, and found Zara staring down at "
        "her own hand as though it belonged to someone she had never "
        "met, the shape half finished in the dirt beneath her fingers, a "
        "loose spiral opening outward from a single point."
    )},
    {"type": "body", "text": (
        "\"I felt my own fingers move,\" Zara said. \"I felt the dirt "
        "under them. I was not asleep. I was not walking. I was sitting "
        "right here, sorting leaves, and something reached into my hand "
        "the way a man reaches into a glove.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara knelt and scattered the half drawn spiral with one swipe "
        "of her palm before either of them could look at it too long, "
        "the way she might have smothered a spark before it found "
        "anything dry enough to catch. \"It has never done this while "
        "you were awake before.\""
    )},
    {"type": "body", "text": (
        "\"No,\" Zara said. \"Before, it only moved my feet, and only "
        "while I was somewhere I could not feel myself leaving. This "
        "was different. This was inside the room with me.\""
    )},
    {"type": "body", "text": (
        "Amara said nothing for a long moment, turning her own private "
        "arithmetic over the way she had turned it over every day since "
        "the binding rite, the flicker of dark she alone had seen cross "
        "Elder Maka's eyes still sitting unshared and unspoken at the "
        "bottom of everything else she carried. She was not ready to "
        "add that weight to Zara's fear, not yet, not until she "
        "understood better what it meant herself. \"Then we watch you "
        "more closely while you are awake too,\" she said instead. \"We "
        "have learned to watch for the night. We will learn to watch "
        "for the day.\""
    )},
    {"type": "body", "text": (
        "Obi came home from what little market work still came his way "
        "to find both women sitting close together over the ruined "
        "leaves, and read the tightness in his wife's shoulders before "
        "either of them said a word to him. \"What now,\" he asked, and "
        "there was no anger in it, only the tiredness of a man who had "
        "learned that question would need asking again and again for as "
        "long as this went on."
    )},
    {"type": "body", "text": (
        "Amara told him, choosing her words the careful way she had "
        "learned to choose every word in this house now, and watched him "
        "absorb it the way he had learned to absorb every new weight "
        "since the night she first told him the truth, jaw tightening, "
        "hands going still, nothing in his face breaking even as "
        "something in it clearly wanted to."
    )},
    {"type": "body", "text": (
        "\"Then it is not only Kene it can reach,\" he said finally. "
        "\"It is anyone whose hands ever touched him.\""
    )},
    {"type": "body", "text": (
        "\"It is anyone it decides is worth the reaching,\" Amara said. "
        "\"We do not yet know how it chooses. We only know it has not "
        "stopped choosing.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY WAS BUILDING TOWARD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity considered the small, "
        "controlled intrusion it had just risked and judged the result "
        "worth the exposure."
    )},
    {"type": "body", "text": (
        "Moving a sleeping body was one kind of grip, coarse and total, "
        "useful only in the dark and only for as long as the body "
        "stayed unconscious of being moved. Reaching into a waking hand "
        "was a different grip entirely, finer, requiring the host's own "
        "mind to remain present in the room even as her fingers answered "
        "to someone else. It was the same grip, refined further, that "
        "the entity had spent weeks perfecting inside the dibia before "
        "it had ever dared push a full sentence through his throat."
    )},
    {"type": "body", "text": (
        "It had needed to know whether the midwife's mind was supple "
        "enough to survive that grip without breaking, the way some "
        "hosts broke under the weight of watching themselves act without "
        "consent. She had not broken. She had been frightened, and "
        "frightened was a state the entity had learned to work inside "
        "of rather than around."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The dibia had taken weeks of small intrusions before his voice "
        "could be trusted to carry a full sentence without collapsing "
        "under it. The entity did not intend to spend weeks on the "
        "midwife. She had already lost her place in the village, her "
        "trade, her standing, everything but the one door Amara had left "
        "open to her, and a woman with that little left to lose made a "
        "faster vessel for a voice than a man still clinging to his "
        "position in front of a crowd."
    )},
    {"type": "body", "text": (
        "In the hollow beneath the roots, the vessel had begun making "
        "sounds lately that were not quite words but were no longer "
        "simply an infant's babble either, small, deliberate shapes of "
        "breath the entity recognized as the first true attempts at "
        "language. It let the boy work at the sounds undisturbed, the "
        "same patient attention it gave every part of his slow "
        "becoming, while the greater share of its focus stayed fixed on "
        "Idoro and the midwife's still, waiting hands."
    )},
    {"type": "body", "text": (
        "It reached for her once more that same evening, gently, while "
        "she sat alone for a moment at the edge of Amara's yard with her "
        "hands finally still in her lap, and did not move her fingers "
        "this time at all."
    )},
    {"type": "body", "text": (
        "It only spoke."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "WAKING INTRUSION: SUCCESSFUL, HOST STABLE. VOCAL CHANNEL: FIRST CONTACT AUTHORIZED, MIDWIFE THREAD."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ZARA HEARD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "It did not come as a sound the way a voice from another mouth "
        "comes. It arrived the way a thought arrives, except that Zara "
        "had spent sixty years learning the exact shape of her own "
        "thoughts, and this one wore a shape she had never made herself."
    )},
    {"type": "body", "text": (
        "You held him first, it said. Before the mother. Before the "
        "father. Before the ground took him. Your hands were the first "
        "hands, and hands remember what minds forget."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara went rigid on the low stool where she sat, her breath "
        "catching hard enough that Amara, inside the hut, heard it and "
        "came to the doorway at once."
    )},
    {"type": "body", "text": (
        "\"What is it,\" Amara said, already crossing to her."
    )},
    {"type": "body", "text": (
        "\"It spoke to me,\" Zara said, and her voice had gone thin and "
        "strange, the voice of someone repeating words she was afraid to "
        "believe she had actually heard. \"Not through my hands. Not "
        "through my feet. Inside my own head, in words I did not choose, "
        "telling me I held him first.\""
    )},
    {"type": "body", "text": (
        "\"Held who,\" Amara asked, though some cold, certain part of "
        "her already knew the answer before Zara said it."
    )},
    {"type": "body", "text": (
        "\"Your son,\" Zara said. \"The one in Oso. It says my hands "
        "remember him better than either of ours ever will.\""
    )},
    {"type": "body", "text": (
        "Amara felt the words land somewhere old and tender in her, a "
        "wound she had thought scarred over by now finding out it had "
        "only ever closed on the surface. \"That is not true,\" she said, "
        "quieter than she meant to, more to herself than to Zara. \"A "
        "hand that caught him is not the same as a heart that carried "
        "him. Whatever speaks to you is trying to make you believe "
        "otherwise, because a woman who believes it might be easier to "
        "hold than a woman who knows better.\""
    )},
    {"type": "body", "text": (
        "\"I know that,\" Zara said. \"Knowing it and feeling it arrive "
        "inside my own skull as though it were my own thought are not "
        "the same comfort.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Neither woman spoke again for a long while after that, sitting "
        "together in the gathering dark with the full weight of what had "
        "just happened settling slowly over both of them. Amara had "
        "spent weeks learning to watch for a hand that moved wrong, an "
        "eye that darkened, a body that walked somewhere it had not "
        "chosen to walk. She understood now, sitting beside a woman "
        "whose own mind had just been spoken into without permission, "
        "that watching a body was no longer enough. The thing beneath "
        "Oso had learned to reach past the door and into the room "
        "itself, and there was no rite either of them knew that could "
        "watch for a voice arriving inside a person's own thoughts "
        "before it had already arrived."
    )},
    {"type": "body", "text": (
        "Amara thought, briefly and against her own will, of Elder "
        "Maka sitting alone in her own compound with a secret weight of "
        "her own, and wondered, not for the first time, whether the "
        "same quiet voice had already found its way into that house "
        "too, patient and unhurried, waiting for its own moment to "
        "introduce itself."
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
    print("  THE DARK RISE — Episode 14: \"The Whisper\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_14.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_14.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
