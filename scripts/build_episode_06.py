#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 6: "The Cleansing"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-13: Episode 6 picks up four days after Episode 5. Amara tells
Obi the truth, reactivating him from his grief-stupor into fear and purpose.
Elder Maka leads the village in a cleansing rite meant to sever whatever
controls the dibia. The entity, recognizing the rite as a threat to its only
foothold in the village, strikes the dormant twin thread to Kene as a
distraction at the ritual's climax, shattering the village's focus and
saving its hold on the dibia. Amara alone sees Kene's eyes darken for an
instant before returning to normal, and understands the entity now has more
than one door into Idoro.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_06.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Six"},
    {"type": "title_ep_name", "text": "The Cleansing"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT AMARA TELLS OBI
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Four days after Elder Maka's confession, Idoro prepared for the "
        "cleansing rite the way a village prepares for a storm it cannot "
        "see yet, only smell coming."
    )},
    {"type": "body", "text": (
        "Women swept compounds that were already swept clean. Men "
        "sharpened tools that did not need sharpening. Near the dibia's "
        "hut, three elders built a fire pit and laid out bundles of "
        "bitter leaf and camwood powder, preparing for a ritual none of "
        "them had performed in thirty and four years and few of them "
        "remembered correctly."
    )},
    {"type": "body", "text": (
        "The story the apprentices had carried out of the village had not "
        "stayed small. It had grown teeth in the retelling, passed from "
        "compound to compound until half of Idoro believed the dibia was "
        "possessed outright and the other half believed something worse, "
        "that whatever had taken him was already loose and simply "
        "wearing his face until it found a better one. Mothers kept their "
        "children closer than usual that week. No one said the word "
        "abiku aloud, but it sat behind every glance thrown toward Oso."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In her own compound, Amara watched Obi mend a fishing net he had "
        "not used since the night their sons were born. His hands moved "
        "through the motions without any purpose behind them, the way a "
        "man moves when stillness has become more frightening than work."
    )},
    {"type": "body", "text": (
        "She sat across from him and said, \"I need to tell you "
        "something, and I need you to hear all of it before you speak.\""
    )},
    {"type": "body", "text": (
        "Obi's hands stopped."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She told him carefully, choosing each word the way a woman "
        "crosses a river on stones she has not tested. Their son was "
        "alive. Something old and patient had claimed him in Oso and was "
        "not letting go. It spoke through the dibia now, had spoken "
        "through him directly to her, had called her by name. Elder Maka "
        "had buried a version of this same horror thirty and four years "
        "ago and had vowed, only days past, to kill their son herself if "
        "he ever came home wearing the wrong face."
    )},
    {"type": "body", "text": (
        "She did not tell him about the place beside their son the "
        "voice had offered her. Some stones on the river were not meant "
        "to be tested yet."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Obi was silent for so long that Amara thought he had not "
        "understood. Then he stood, and the net fell from his hands "
        "unnoticed, and something moved behind his eyes that had not "
        "moved there since the night the dibia carried their son into "
        "the dark."
    )},
    {"type": "body", "text": (
        "\"He is alive,\" Obi said, as though testing whether the words "
        "would hold his weight."
    )},
    {"type": "body", "text": (
        "\"He is alive and he is becoming something none of us have a "
        "name for,\" Amara said. \"Do not mistake one truth for a "
        "kinder one than it is.\""
    )},
    {"type": "body", "text": (
        "\"Then I will go to him. Tonight. I will walk into that forest "
        "and I will—\""
    )},
    {"type": "body", "text": (
        "\"You will die there and he will still be alone,\" Amara said, "
        "sharper than she meant to. \"Whatever waits in Oso did not "
        "spare our son so a grieving father could wander in and be "
        "forgiven for it. If we move, we move together, and we move "
        "when it costs us less than everything.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Obi's jaw worked. For the first time in weeks, grief and anger "
        "shared his face instead of grief alone, and Amara understood, "
        "watching him, that she had not only given her husband a "
        "terrible truth. She had given him back a reason to stand."
    )},
    {"type": "body", "text": (
        "\"Tonight's rite,\" he said finally. \"We will be there. "
        "Together. Watching.\""
    )},
    {"type": "body", "text": (
        "\"Together,\" Amara agreed. \"And watching. Nothing more, "
        "until I say otherwise.\""
    )},
    {"type": "body", "text": (
        "He did not promise it. She noticed that he did not promise it, "
        "and filed the omission away with everything else she was "
        "learning to carry."
    )},
    {"type": "body", "text": (
        "Later, while Obi slept the first deep sleep she had seen in him "
        "since the birth, Amara stood over Kene's basket and watched him "
        "breathe. He had been fussier lately, waking at odd hours with a "
        "thin restless cry that settled the moment she lifted him, and "
        "Zara had blamed teething and moved on. Amara was no longer sure "
        "she believed in such a simple explanation for anything. She "
        "pressed two fingers lightly to his chest, felt his heart beating "
        "fast and even beneath them, and made herself put the thought "
        "away before it could take root."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE ENTITY PREPARES ITS ANSWER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, the entity tasted the village's intentions long before "
        "the fire pit was finished."
    )},
    {"type": "body", "text": (
        "This fear had a different shape than the fear it usually fed "
        "on. Ordinary dread was soft and formless, easy to drink. This "
        "was fear with a point sharpened on one end, aimed with purpose "
        "at a single target. The elders meant to reach into the dibia's "
        "hut tonight and cut whatever thread connected him to the "
        "forest."
    )},
    {"type": "body", "text": (
        "The entity considered this the way a spider considers a hand "
        "reaching toward its web from across a room. There was time to "
        "prepare. There was no reason to be afraid, and every reason to "
        "be ready."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Losing the dibia would not unmake the entity. It had survived "
        "three centuries without a single mouth to speak through. But "
        "the dibia was its only window into Idoro, its only hand able to "
        "touch the village directly, and a spider does not surrender a "
        "web simply because a hand is reaching for it."
    )},
    {"type": "body", "text": (
        "In the hollow beneath the iroko roots, the vessel pushed itself "
        "upright on legs that had not existed in that shape a week "
        "earlier, wavered, and took one small stumbling step before the "
        "roots caught him. It was the first step any part of this body "
        "had ever taken. The entity noted it with the same flat "
        "attention it gave everything useful."
    )},
    {"type": "body", "text": (
        "It let the vessel try again. And again. Each attempt taught the "
        "small collapsing legs something they would need later, and the "
        "entity was patient in the way only something that had already "
        "outlasted a village's grandfathers could be patient. Growth "
        "bought with fear was still growth. It did not care what paid for "
        "the meal, only that the meal arrived, and Idoro had been feeding "
        "it richly since the night it first spoke through the dibia's "
        "mouth."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "If the elders' rite reached far enough to threaten its hold "
        "tonight, the entity would need to break their attention "
        "entirely, all at once, before their combined will finished what "
        "it started. It had one thread ready for exactly that purpose. A "
        "thread it had touched once, briefly, and then left alone "
        "because it was too raw, too likely to be noticed."
    )},
    {"type": "body", "text": (
        "Not yet, it had told itself, eight days ago."
    )},
    {"type": "body", "text": (
        "Tonight might not leave room for later."
    )},

    {"type": "blank", "text": ""},

    # System lines
    {"type": "system", "text": "THREAT DETECTED: RITE INTENT TO SEVER CONTROL OF THE DIBIA. VESSEL MOTOR CONTROL: FIRST INDEPENDENT STEP TAKEN."},
    {"type": "system", "text": "CONTINGENCY PREPARED: TWIN THREAD, HELD IN RESERVE, NOW ARMED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE RITE / THE HOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By dusk, most of Idoro had gathered in a loose, uneasy ring "
        "around the fire pit outside the dibia's hut. Amara stood beside "
        "Obi at the edge of the crowd, Kene asleep against her shoulder, "
        "wrapped against the evening chill."
    )},
    {"type": "body", "text": (
        "No one spoke above a murmur. Even the children, sensing "
        "something in their parents' stillness, had stopped their usual "
        "running between the compounds and stood pressed against legs "
        "and skirts, watching the fire pit with the wide unblinking eyes "
        "of animals that smell a predator before they see it."
    )},
    {"type": "body", "text": (
        "The elders brought the dibia out into the firelight. He could "
        "barely stand on his own. Two men held him upright by the arms "
        "while Elder Maka circled him three times with a bundle of "
        "burning bitter leaf, chanting words in a register Amara had "
        "never heard her use, older and rougher than any prayer spoken "
        "at a naming or a burial."
    )},
    {"type": "body", "text": (
        "The smoke rolled low across the ground and did not rise the "
        "way smoke should rise. It pooled instead, thick and reluctant, "
        "as though something did not want to let it go."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The dibia's body began to shake."
    )},
    {"type": "body", "text": (
        "Not the small constant tremor Amara had seen in his hands "
        "before. This was a full body convulsion, his spine arching, his "
        "throat working against something that did not want to let him "
        "speak. Elder Maka's chant rose louder, sharper, and for one "
        "astonishing moment the dibia's own voice broke through, raw and "
        "real."
    )},
    {"type": "body", "text": (
        "\"The child,\" he gasped, eyes wild and clear for the first "
        "time in weeks. \"He is not the only door. There are others "
        "already—\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "He never finished it."
    )},
    {"type": "body", "text": (
        "Against Amara's shoulder, Kene went rigid."
    )},
    {"type": "body", "text": (
        "It happened too fast for anyone but her to notice at first. His "
        "small body arched backward, a thin, terrible sound tearing out "
        "of him that no sleeping infant should have been able to make, "
        "and then he screamed, a full waking scream that cut through the "
        "chanting and the crackle of the fire and every other sound in "
        "the clearing at once."
    )},
    {"type": "body", "text": (
        "The rite shattered instantly. Elder Maka's chant died in her "
        "throat. Every head turned toward Amara and the screaming child "
        "in her arms. The two men holding the dibia loosened their grip "
        "without meaning to, and the dibia sagged between them, whatever "
        "had almost broken through in him swallowed back down into "
        "silence."
    )},

    {"type": "blank", "text": ""},

    # System line
    {"type": "system", "text": "DISTRACTION SUCCESSFUL. RITE INTERRUPTED. CONTROL OF THE DIBIA REMAINS INTACT."},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara pulled Kene against her chest, her whole body flooding "
        "with the animal panic of a mother whose child is in danger, and "
        "for one instant, before his eyelids fluttered and his scream "
        "dissolved into ordinary frightened sobbing, she looked directly "
        "into his open eyes."
    )},
    {"type": "body", "text": (
        "They were dark. Not brown. Not the warm color they had been "
        "every day since his birth. Dark, and faintly shining, the way "
        "oil shines on water in poor light."
    )},
    {"type": "body", "text": (
        "Then his eyes closed, and opened again, and they were only "
        "Kene's eyes, brown and frightened and entirely his own, and he "
        "was crying the ordinary crying of a startled child and nothing "
        "more."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "No one else had seen it. Obi was already reaching for his son, "
        "murmuring comfort. The elders were arguing over whether the "
        "rite could be resumed. Villagers were already turning the "
        "moment into a story about a startled baby and a poorly timed "
        "cry."
    )},
    {"type": "body", "text": (
        "Amara alone understood what had actually happened. The entity "
        "beneath Oso had just answered a question none of them had "
        "thought to ask. It did not have only one door into Idoro."
    )},
    {"type": "body", "text": (
        "It had at least two. And it had just proven, in front of the "
        "entire village, that it could open either one whenever it "
        "chose."
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
    print("  THE DARK RISE — Episode 6: \"The Cleansing\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_06.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_06.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
