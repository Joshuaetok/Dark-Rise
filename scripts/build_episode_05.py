#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 5: "The Cost of the Law"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-12: Episode 5 continues directly from Episode 4's hook. Elder
Maka tells Amara the truth she has carried for thirty four years: the same
dibia once carried her own child to Oso, that child came back wrong, and she
killed it herself before it could kill again. Meanwhile in Oso, the village's
fresh terror feeds the entity harder than any ambient dread before it, and
the vessel's body surges through a grotesque growth spurt. The episode ends
with Elder Maka's vow to Amara: if her son comes back wrong, she will end him
too, and Amara's silence in response is its own answer.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_05.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Five"},
    {"type": "title_ep_name", "text": "The Cost of the Law"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE ELDER'S CONFESSION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara sat because the old woman's voice left no room to stand. "
        "The night pressed close around them, thick with woodsmoke and the "
        "sour tang of fear that had settled over Idoro like a fog that "
        "would not lift."
    )},
    {"type": "body", "text": (
        "Elder Maka lowered herself onto the bench outside the dibia's "
        "hut with the slow care of a much older woman, though Amara had "
        "never once seen her move that way in daylight. In the dark, "
        "stripped of the audience that usually watched her every step, "
        "she looked less like a priestess and more like someone carrying "
        "a weight she had never once set down."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"Thirty and four years ago,\" Elder Maka said, \"I was not an "
        "elder. I was a young wife with a swollen belly and a husband who "
        "sang to it every evening, whether or not the child inside could "
        "hear him.\""
    )},
    {"type": "body", "text": (
        "Amara said nothing. She had learned, these past weeks, that "
        "silence pulled truth out of people faster than questions did."
    )},
    {"type": "body", "text": (
        "\"I carried twins,\" Elder Maka went on. \"The same as you. One "
        "came into the world crying the way a child should. The other "
        "came into the world with eyes that had already seen too much. "
        "The law was the law then as it is the law now. I did not fight "
        "it. I believed, the way you once believed, that fighting it "
        "would only make the grief longer.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"The same man who carried your son to the boundary of Oso "
        "carried mine,\" she said. \"He was younger then. So was I. His "
        "hands did not shake yet.\""
    )},
    {"type": "body", "text": (
        "Amara's breath caught. She thought of the dibia's trembling "
        "hands not an hour ago, the charcoal circles on the palm leaf, "
        "the wrong voice wearing his mouth. \"He has carried children into "
        "that forest for forty years,\" she said slowly. \"Yours was one "
        "of the first.\""
    )},
    {"type": "body", "text": (
        "She tried to picture him young. A younger dibia with steady "
        "hands, walking a different young mother's child into the same "
        "dark trees, and could not manage it. In her mind his hands had "
        "always shaken. In her mind the forest had always been waiting."
    )},
    {"type": "body", "text": (
        "\"Mine was among the first I know of,\" Elder Maka said. \"There "
        "may have been others before either of us were born to care.\""
    )},
    {"type": "body", "text": (
        "\"And the other twin,\" Amara asked. \"The one you kept.\""
    )},
    {"type": "body", "text": (
        "\"She grinds millet three compounds from mine,\" Elder Maka "
        "said. \"She has never once asked why her mother became a "
        "priestess who enforces the old law more harshly than any elder "
        "before her. She thinks it is devotion. She has no idea it is "
        "penance.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"For seven years I mourned him the way a mother is permitted "
        "to mourn a child the law has taken. Quietly. Alone. In the space "
        "between chores, where no one could see it and call it "
        "weakness.\""
    )},
    {"type": "body", "text": (
        "\"Then, in the eighth year, he came back.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The words landed in the dark like a stone dropped into still "
        "water. Amara felt the ripple of them move through her own chest."
    )},
    {"type": "body", "text": (
        "\"He walked out of the trees at the edge of Oso on a morning "
        "no different from any other,\" Elder Maka said. \"Taller than "
        "a boy of eight years should have been. Stronger than any boy "
        "raised on millet and river fish. He smiled at me the way he "
        "used to smile before I gave him away, and for one whole day I "
        "let myself believe the law had been merciful after all. That "
        "the forest had simply kept him safe and grown him well and sent "
        "him home.\""
    )},
    {"type": "body", "text": (
        "\"I was a fool for one whole day.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka's voice did not break. That was somehow worse than "
        "if it had. \"By the second night, animals in the compound would "
        "not go near him. By the third, he had stopped eating food and "
        "started watching the rest of us the way a hunter watches "
        "something he has already decided to kill. On the fourth night, "
        "he killed my husband in his sleep, and two men who came running "
        "at the sound, and he was smiling the entire time it happened, "
        "the same smile he gave me at the tree line.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"I do not know if it was the same hunger that speaks through "
        "our dibia now,\" she said. \"Perhaps it was only a small piece "
        "of it, testing how far its reach could travel in a single "
        "returned child. I do not know. I know only what walked out of "
        "the trees wearing my son's face, and I know what I had to do "
        "to stop it wearing that face any longer.\""
    )},
    {"type": "body", "text": (
        "She did not say the words. She did not need to. Amara understood "
        "them from the flatness in the old woman's eyes, the particular "
        "stillness of someone who had done an unspeakable thing once and "
        "had spent every year since making sure she would never have to "
        "explain it to anyone."
    )},

    {"type": "blank", "text": ""},

    # System line
    {"type": "system", "text": "HISTORICAL RECORD: SECOND KNOWN INCIDENT OF RETURN. OUTCOME: THREE DEAD. VESSEL DESTROYED BY THE ELDER HERSELF."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — THE HUNGER SPIKE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three miles away, beneath the ak-pu tree, the entity drank."
    )},
    {"type": "body", "text": (
        "It had fed on ambient dread for three centuries, sipping the "
        "way a man sips dew from leaves when there is no river near. What "
        "poured toward it now was nothing like dew. It was a flood."
    )},
    {"type": "body", "text": (
        "A whole village lay awake behind barred doors. Guards stood "
        "rigid outside a hut where something had spoken with a stranger's "
        "voice. An old woman relived a grief she had buried for thirty "
        "and four years. Every one of those fears rose off Idoro like "
        "heat off the delta at midday, and the entity opened itself to "
        "all of it at once."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The vessel's body could not hold the feeding quietly."
    )},
    {"type": "body", "text": (
        "Bone lengthened with a sound like green wood bending. The soft, "
        "unfinished plates of a newborn skull fused entirely in the space "
        "of a single night, and beneath the new bone, something in the "
        "shape of the child's face reorganized itself into an "
        "expression an infant's muscles were never built to make. Fat "
        "burned away. Sinew corded along small limbs that had been "
        "boneless a week ago."
    )},
    {"type": "body", "text": (
        "By the time the feeding slowed toward dawn, the thing lying in "
        "the hollow beneath the ak-pu roots no longer looked like an "
        "infant at all. It looked like a child of perhaps one year, "
        "though it had drawn its first breath only eight days before."
    )},
    {"type": "body", "text": (
        "The roots themselves had thickened overnight, breaking through "
        "soil that had not moved in three centuries. They coiled loosely "
        "around the child's new limbs the way a mother's arms might, or "
        "the way a snake's coils might, and it was no longer possible to "
        "tell, looking at the shape of it in the dark, which the roots "
        "meant to be."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Fear feeds faster than lessons, the entity thought, and there "
        "was something close to amusement in the thought, if amusement "
        "was a thing this old hunger still remembered how to feel. Your "
        "own terror is building the very thing you fear. You have always "
        "been feeding me. Tonight you have simply learned to do it "
        "faster."
    )},
    {"type": "body", "text": (
        "The vessel's eyes opened. They were no longer the eyes of "
        "something learning to see. They were the eyes of something that "
        "had already decided what it was looking for."
    )},

    {"type": "blank", "text": ""},

    # System lines
    {"type": "system", "text": "VESSEL AGE: EIGHT DAYS. APPARENT DEVELOPMENT: APPROXIMATELY ONE YEAR AND ACCELERATING."},
    {"type": "system", "text": "FEEDING SOURCE: VILLAGE WIDE TERROR, FIRST OF ITS SCALE. GROWTH RATE: NO LONGER LINEAR."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE VOW / THE HOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"What happened to him,\" Amara asked quietly. \"After.\""
    )},
    {"type": "body", "text": (
        "Elder Maka looked at her for a long moment before she answered, "
        "as though weighing whether Amara had earned the last and worst "
        "part of the story."
    )},
    {"type": "body", "text": (
        "\"I ended him myself,\" she said. \"With my own hands, before "
        "the sun rose on the fifth day, before he could kill a fourth "
        "person or a fifth or however many it would have taken before "
        "someone braver than me found the courage to do what needed "
        "doing. I did not wait for the men. I did not wait for a "
        "blessing. I did it myself so that no one else would carry what "
        "I already knew I would carry for the rest of my life.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara's hands had curled into fists in her lap without her "
        "noticing. \"You are telling me this so I will be afraid of my "
        "own son.\""
    )},
    {"type": "body", "text": (
        "\"I am telling you this,\" Elder Maka said, \"so that you "
        "understand what I am, and what I will do, if the day ever comes "
        "that your son walks out of those trees wearing a smile that "
        "does not belong to him.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She reached out and took Amara's clenched hand in both of hers. "
        "Her grip was dry, and warm, and utterly without mercy."
    )},
    {"type": "body", "text": (
        "\"If he comes back wrong, Amara, I will end him too. Not out of "
        "hatred. Out of the same mercy I could not find the courage to "
        "show my own son quickly enough. I will not hesitate a second "
        "time. I owe the dead that much.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara did not answer. She looked instead at the dark line of "
        "the horizon where, three miles off, something waited beneath a "
        "tree that had learned to lean toward the village it was slowly "
        "learning to devour."
    )},
    {"type": "body", "text": (
        "Her silence was its own answer. Elder Maka heard it, and "
        "something in her face went sad in a way it had not been sad "
        "since she started speaking."
    )},
    {"type": "body", "text": (
        "\"I prayed you would say something else,\" the old woman "
        "whispered. \"But prayers have never once stopped this law. Not "
        "in thirty and four years. I do not expect them to start with "
        "you.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka rose from the bench, her joints protesting the "
        "long stillness, and straightened her wrapper with the brisk, "
        "practiced motion of a woman putting her mask back on. By the "
        "time she turned to walk back toward her own compound, the "
        "grief in her face had vanished so completely that Amara could "
        "almost believe she had imagined the whole confession."
    )},
    {"type": "body", "text": (
        "Almost."
    )},
    {"type": "body", "text": (
        "Amara sat alone outside the dibia's hut long after the old "
        "woman's footsteps had faded, turning one thought over and over "
        "until it wore smooth. Elder Maka had made her vow believing it "
        "was a warning. Amara had heard it as something else entirely. A "
        "map of exactly how much time she had, and exactly who would be "
        "waiting with a blade when that time ran out."
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
    print("  THE DARK RISE — Episode 5: \"The Cost of the Law\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_05.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_05.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
