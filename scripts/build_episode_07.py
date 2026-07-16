#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 7: "The Second Door"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-14: Episode 7 picks up the morning after Episode 6's failed
cleansing rite. Elder Maka comes to Amara with suspicion but no proof, and
Amara chooses to lie rather than trust her, deepening the rift she privately
resolved on in Episode 5. Obi's unspoken refusal to only watch surfaces for
the first time in dialogue. In Oso, the entity treats its near exposure
during the rite as a lesson: it stops holding its other dormant threads in
reserve and begins testing the one running to Zara, the midwife whose hands
were the first to touch the vessel at birth. The episode closes on Zara
alone in her hut, feeling her own hands turn strange for a moment, with no
one else in the village aware a second door has begun to open.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_07.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seven"},
    {"type": "title_ep_name", "text": "The Second Door"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE MORNING AFTER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The morning after the cleansing rite, Idoro woke into a silence "
        "heavier than the noise that had broken it the night before."
    )},
    {"type": "body", "text": (
        "The fire pit outside the dibia's hut had burned down to gray ash. "
        "The elders who had built it stood around the cold circle arguing "
        "in low voices about whether the rite could still be finished, or "
        "whether a screaming infant had undone a working that thirty and "
        "four years of neglect had already left fragile."
    )},
    {"type": "body", "text": (
        "No one blamed Kene aloud. A child startled by smoke and chanting "
        "was an easy thing to forgive. But Amara noticed how the argument "
        "kept circling back to one question no one asked directly, why "
        "the boy had screamed at the exact moment the dibia's voice broke "
        "free, and she understood that even without proof, some part of "
        "the village's fear had already begun turning toward her own "
        "compound."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She was folding cloth in her yard, Kene asleep on a mat beside "
        "her, when Elder Maka's shadow fell across the doorway."
    )},
    {"type": "body", "text": (
        "\"You did not sleep,\" Elder Maka said. It was not a question."
    )},
    {"type": "body", "text": (
        "\"Neither did you,\" Amara answered."
    )},
    {"type": "body", "text": (
        "Elder Maka lowered herself onto the low stool across from Amara "
        "with the careful stiffness of a woman whose bones remembered "
        "every one of her years. For a long moment she only watched Kene "
        "breathe."
    )},
    {"type": "body", "text": (
        "\"He screamed at a strange hour,\" she said finally. \"I have "
        "led enough rites to know when a child cries from fright and when "
        "a child cries because something reached into him and pulled. "
        "Tell me which one I watched last night.\""
    )},
    {"type": "body", "text": (
        "Amara kept her hands moving through the cloth, folding it "
        "smaller and smaller, because if she stopped she was afraid Elder "
        "Maka would see how carefully she was choosing her next words."
    )},
    {"type": "body", "text": (
        "\"He is teething,\" Amara said. \"Zara has said so for weeks.\""
    )},
    {"type": "body", "text": (
        "\"Zara has not buried what I have buried in this village,\" "
        "Elder Maka said. \"I raised a child who came back wrong and I "
        "put him in the ground myself. I know the shape fear takes when "
        "something old is testing a door.\""
    )},
    {"type": "body", "text": (
        "The word door landed in Amara's chest like a stone dropped into "
        "still water, and she made herself breathe evenly through the "
        "widening rings of it."
    )},
    {"type": "body", "text": (
        "\"If you believe something is wrong with my son,\" Amara said, "
        "\"say it plainly. Do not circle me the way you circled the "
        "dibia with smoke.\""
    )},
    {"type": "body", "text": (
        "Elder Maka studied her for a long moment, and something in her "
        "face was almost respect. \"I am not circling you, Amara. I am "
        "asking you to remember what I told you four nights ago. I meant "
        "every word of it. For your sake, and for his, I hope I never "
        "have reason to keep that promise.\""
    )},
    {"type": "body", "text": (
        "She left without waiting for an answer. Amara sat very still "
        "after she had gone, turning the conversation over until she "
        "found the shape of what had actually happened. Elder Maka "
        "suspected. She did not know. And the space between those two "
        "things was the only room Amara had left in which to protect her "
        "son."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Obi found her there an hour later, staring at nothing, the "
        "folded cloth forgotten in her lap."
    )},
    {"type": "body", "text": (
        "\"What did she want,\" he asked."
    )},
    {"type": "body", "text": (
        "\"To remind me what she is capable of.\""
    )},
    {"type": "body", "text": (
        "Obi's jaw tightened in a way it had not before the night she "
        "told him the truth, a tightening that seemed permanent in him "
        "now. \"Then we should move faster than she does. I have been "
        "thinking. If the boy in Oso is truly ours, truly still "
        "becoming, then every day we wait is a day closer to whatever he "
        "is becoming into.\""
    )},
    {"type": "body", "text": (
        "\"We agreed. Together. Watching.\""
    )},
    {"type": "body", "text": (
        "\"I remember what I agreed to,\" Obi said, and something in the "
        "careful way he said it told Amara he had not forgotten the "
        "promise he had pointedly not made alongside it. \"I only wonder "
        "how long watching is meant to last before it becomes another "
        "word for doing nothing.\""
    )},
    {"type": "body", "text": (
        "He walked away before she could answer. Amara let him go, "
        "because she did not have an answer that would satisfy either of "
        "them yet, and because some part of her, the part that had "
        "already begun keeping a private accounting of Elder Maka's "
        "future crimes before the elder had committed any of them, "
        "understood exactly what he meant."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE SECOND THREAD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity turned the previous night "
        "over with the patience of something that had already survived "
        "every mistake a younger power could make."
    )},
    {"type": "body", "text": (
        "It had been careless. Not with the vessel, whose growth it "
        "guarded like a coal cupped against wind, but with the reach of "
        "its own hunger. It had touched the twin thread only once before "
        "last night, briefly, and had judged it safe to leave sleeping. "
        "It had been wrong. The old woman who led the rite had come close "
        "enough to smell the truth before the Kene thread gave her "
        "something louder to chase."
    )},
    {"type": "body", "text": (
        "It would not make that error again by leaving its other doors "
        "untested only because using them carried a risk of being seen."
    )},
    {"type": "body", "text": (
        "The dibia's warning, torn loose in that one unguarded second "
        "before the entity silenced him, had been true. There were "
        "others already. Not threads it had built. Threads that had "
        "always existed, thin and dormant, waiting on the far side of "
        "blood and touch, the same way the bond to Kene had waited eight "
        "days before the entity first found it."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "One of those threads ran to the woman who had pulled both sons "
        "into the world with her own two hands."
    )},
    {"type": "body", "text": (
        "The midwife. Zara."
    )},
    {"type": "body", "text": (
        "She had touched the vessel first, before Amara, before the "
        "dibia, before Oso had ever heard its name spoken in fear. Her "
        "hands had been the first hands, wet with the same blood that "
        "now ran in the boy coiled inside the iroko roots a mile beyond "
        "her hut. Blood remembered the hands that had held it, the "
        "entity had learned, the same way it remembered a mother's grief "
        "and a brother's sleeping bond. It only needed a reason to look."
    )},
    {"type": "body", "text": (
        "Last night, staring down the possibility of losing its only "
        "mouth in the village, had given it every reason it needed."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel's teeth had begun to come in "
        "overnight, small and sharp and entirely too early, another debt "
        "paid by the terror that had flooded the clearing when Kene "
        "screamed. The entity noted the growth with its usual flat "
        "attention and turned the greater part of itself toward the new "
        "thread, testing it the way a tongue tests a loose tooth, gently, "
        "to see how much it would give before it caused pain."
    )},
    {"type": "body", "text": (
        "The thread gave more than the twin bond ever had. Zara was not "
        "an infant sealed behind eight days of raw, unformed nerve. She "
        "was a grown woman who had spent thirty years with her hands in "
        "other people's blood, and blood that has been touched so many "
        "times wears a channel deep enough to travel with ease."
    )},
    {"type": "body", "text": (
        "The entity did not open the door all the way. Not yet. It only "
        "set its attention against it, softly, the way it had once set "
        "its attention against Kene in sleep, and waited to see whether "
        "anyone in Idoro would notice a second thread trembling before "
        "they had even finished mourning the first."
    )},

    {"type": "blank", "text": ""},

    # System lines
    {"type": "system", "text": "VESSEL DEVELOPMENT: EARLY DENTITION, ACCELERATED. NEW THREAD IDENTIFIED: MATERNAL BLOOD CONTACT, MIDWIFE. THREAD STATUS: TESTED, NOT YET OPENED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT ZARA FELT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "That night, Zara sat alone in her hut grinding bitter leaf into "
        "paste for a mother two compounds over who was due to deliver "
        "before the next full moon. Her hands knew the motion so well she "
        "barely needed her eyes for it, thirty years of the same grinding "
        "stone, the same practiced turn of the wrist."
    )},
    {"type": "body", "text": (
        "Halfway through the work, her hands stopped on their own."
    )},
    {"type": "body", "text": (
        "She had delivered more children than she could name "
        "individually anymore, but she remembered the twins. She "
        "remembered them the way she remembered very few births, not "
        "because of the blood or the labor, both ordinary, but because "
        "of the silence after. Amara's second son had not cried. She had "
        "waited for it, the way every midwife waits for that first "
        "outraged breath, and it had not come, and in the stretched, "
        "wrong moment before someone finally said the word abiku, she "
        "had held a living child in her hands who made no sound at all."
    )},
    {"type": "body", "text": (
        "She had not thought of that silence in days. Tonight it filled "
        "her hut so completely that the grinding stone slipped from her "
        "fingers and struck the packed earth floor without her feeling it "
        "leave her hand."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Her palms were tingling, both of them, in the exact places that "
        "had once cupped a newborn skull."
    )},
    {"type": "body", "text": (
        "Zara turned her hands over in the low lamplight and found "
        "nothing there. No mark, no wound, no reason for the sensation "
        "crawling up through her wrists like blood returning to a limb "
        "that had fallen asleep. She flexed her fingers and the tingling "
        "did not fade with the movement the way ordinary numbness should "
        "have. It deepened."
    )},
    {"type": "body", "text": (
        "She told herself it was age. She told herself it was the cold "
        "coming through the door she had left open too long. She told "
        "herself several things, one after another, the way a person "
        "tells themselves comfortable stories in the dark, and none of "
        "them stopped her from raising her hands close to her face to "
        "look again, more carefully this time, at skin she had known her "
        "entire life."
    )},
    {"type": "body", "text": (
        "For one instant, in the place where the lamplight struck her "
        "palms most directly, her skin held a faint, wrong sheen, the "
        "same reluctant shine of oil sitting on water."
    )},
    {"type": "body", "text": (
        "Then the lamp guttered in a draft that had no source, and when "
        "it steadied, her hands were only hands again, careworn and "
        "empty, exactly as they had always been."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Zara sat very still for a long time afterward, listening to her "
        "own heartbeat, telling herself she had imagined it. She picked "
        "the grinding stone back up off the floor. Her hands, when she "
        "made them work again, obeyed her perfectly."
    )},
    {"type": "body", "text": (
        "She did not know enough to be afraid yet."
    )},
    {"type": "body", "text": (
        "No one in Idoro did, except a mother a few compounds away who "
        "was already lying awake, cataloguing threats she could name, "
        "while the one thing that could have warned her stirred quietly "
        "in another woman's blood, entirely unseen."
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
    print("  THE DARK RISE — Episode 7: \"The Second Door\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_07.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_07.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
