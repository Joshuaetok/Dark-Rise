#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 12: "The Binding"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-19: Episode 12 follows Elder Maka's private vow from Episode
10 to its logical next step, but not the one she originally intended. Rather
than wait for a second sign and act alone, she comes to Amara with a
different offer: a binding rite, drawn from fragments of the old law she
half remembers from her own son's case, meant to dampen the twin thread
without harming Kene. Amara agrees, judging a rite she can watch is safer
than a silence she cannot. In Oso, the entity weighs the cost of defending
a thread it has already spent most of its value from and chooses to let it
go, husbanding its strength for Zara instead. The rite works, but only
because Elder Maka takes a fragment of the severed darkness into herself
rather than let it scatter loose, a private, hidden cost she tells no one,
including Amara. The episode closes on Elder Maka alone afterward, feeling
the first faint, unfamiliar weight of a thread now running through her
own blood.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_12.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twelve"},
    {"type": "title_ep_name", "text": "The Binding"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT ELDER MAKA OFFERED INSTEAD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka came to Amara's compound three days after the well "
        "had taught Amara what silence could look like, and this time "
        "she came alone, without her watchers, without the crowd of "
        "neighbors who had gathered the last time she stood in this "
        "yard."
    )},
    {"type": "body", "text": (
        "\"I did not come to take your son,\" she said, before Amara "
        "could ask. \"I came to offer you a choice I did not have when "
        "my own child was young enough to still be saved. There is a "
        "rite. Older than the cleansing we tried on the dibia, and "
        "smaller, meant for exactly this, a thread that has not yet "
        "chosen its shape. It will not sever what runs in his blood. It "
        "may dampen it, enough that whatever reached him once will find "
        "the reaching much harder the next time.\""
    )},
    {"type": "body", "text": (
        "Amara studied her for a long moment, remembering the rite that "
        "had already failed once in this village, the smoke that had "
        "pooled low and wrong, the dibia's body arching against a "
        "grip that would not let him finish his warning. \"The last rite "
        "you led nearly cost the dibia his life and gave the thing in "
        "Oso a second door instead of closing the first one.\""
    )},
    {"type": "body", "text": (
        "\"The last rite was aimed at severing a bond fully grown and "
        "long guarded,\" Elder Maka said. \"This is smaller. A thread "
        "eight days old the night it was first touched, still thinner "
        "than a hair. I would rather try to cut a thin thing while it is "
        "still thin than wait for it to become a rope I cannot cut at "
        "all.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara thought of the watchers beneath the mango tree, of the "
        "private vow she had guessed at but never heard spoken aloud, "
        "that Elder Maka would not wait for a council or an argument a "
        "second time. A rite she could watch, could stand inside of, "
        "could stop with her own hands if it turned toward harm, was a "
        "kind of danger she at least understood the shape of. A silence "
        "in which Elder Maka decided alone, in the dark, exactly when "
        "enough was enough, was not."
    )},
    {"type": "body", "text": (
        "\"I will not hand you my son to work on unwatched,\" Amara "
        "said. \"But I will stand beside you while you try. If I see "
        "anything I do not trust, I will end it myself, and you will "
        "let me.\""
    )},
    {"type": "body", "text": (
        "\"That is the only way I intended to offer it,\" Elder Maka "
        "said, and for the first time since the night of her confession, "
        "something almost like relief crossed her face, the relief of a "
        "woman who has been carrying a private plan alone and has just "
        "been handed a witness she did not know she wanted."
    )},
    {"type": "body", "text": (
        "Obi, when Amara told him that evening, took longer to agree "
        "than Amara had. \"She buried her own son with a rite like this "
        "one behind her,\" he said. \"Forgive me for not trusting a "
        "woman's steady hand simply because she has held the knife "
        "before.\""
    )},
    {"type": "body", "text": (
        "\"I do not trust her hand either,\" Amara said. \"I trust that "
        "I will be standing close enough to stop it if it slips. That is "
        "the only trust either of us can afford anymore.\""
    )},
    {"type": "body", "text": (
        "He did not argue further, though she saw the argument sitting "
        "unfinished behind his eyes for the rest of that night, the way "
        "every hard choice in their household now seemed to sit unfinished "
        "somewhere, waiting for a day calm enough to be resolved that "
        "never quite arrived."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY DECIDED WAS WORTH KEEPING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the shape of the "
        "coming rite the moment the two women agreed to it, the same "
        "way it had felt the cleansing rite gathering weeks earlier, "
        "and turned the question over with none of the urgency a "
        "younger power might have brought to it."
    )},
    {"type": "body", "text": (
        "The twin thread had already given it everything it was ever "
        "likely to give. One clean distraction, spent at exactly the "
        "moment it mattered most, purchased at the cost of being seen "
        "by the one woman sharp enough to understand what she had seen. "
        "Every day since, the thread had sat watched, guarded, "
        "surrounded now by two men beneath a mango tree and a mother who "
        "would notice the smallest flicker in her son's eyes before the "
        "flicker had finished happening."
    )},
    {"type": "body", "text": (
        "A door that expensive to use again was barely a door at all. "
        "It was closer to a debt, one the entity had already been "
        "paid in full."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "It considered, briefly, defending the thread anyway, purely to "
        "deny the old woman the satisfaction of a rite that worked where "
        "her first one had failed. Pride was a thing the entity had felt "
        "before, in smaller measures, across three centuries of watching "
        "villages rise and fall around its roots. It set the impulse "
        "aside. Pride had never once fed it. Patience had fed it every "
        "single day since it first opened its senses toward Idoro."
    )},
    {"type": "body", "text": (
        "Better to let the twin thread go quietly, and let the two "
        "women believe they had won something significant, while the "
        "entity turned the whole of its strength toward the door that "
        "had grown lonelier and softer with every day Idoro spent "
        "shunning the woman who carried it."
    )},
    {"type": "body", "text": (
        "There was even a use in letting them win this one. A village "
        "that believed it had found a working defense against the "
        "entity's reach would grow careless in exactly the places that "
        "defense had never touched. Let them celebrate a sealed thread "
        "in an infant's blood. They would not think to look nearly as "
        "closely at a grown woman's, not after tonight, not once the "
        "story of the successful rite had traveled the length of "
        "Idoro and settled everyone's fear a little too soon."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "TWIN THREAD: VALUE EXHAUSTED, DEFENSE NOT WARRANTED. RESOURCE REALLOCATION: MIDWIFE THREAD, PRIORITY RAISED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE COST ELDER MAKA DID NOT SHARE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They performed the rite at dusk, in Amara's own yard, with "
        "only Obi and the two watchers as witnesses, camwood powder "
        "traced in a narrow ring around Kene's sleeping mat and a low "
        "fire burning bitter leaf at each of the four points Elder Maka "
        "marked with her own hands."
    )},
    {"type": "body", "text": (
        "She chanted in the same old register she had used at the "
        "cleansing rite, rougher and older than any prayer Amara had "
        "ever heard spoken over a naming, but softer now, more careful, "
        "the voice of a woman handling something she had once handled "
        "too roughly and had spent thirty and four years learning to "
        "hold differently."
    )},
    {"type": "body", "text": (
        "Kene stirred in his sleep partway through the chant, a small "
        "frown crossing his face, and Amara's whole body went rigid, "
        "ready to end the rite the instant it turned toward harm the way "
        "she had promised. But he only turned onto his side and settled "
        "again, and the chant continued, and the smoke from the bitter "
        "leaf rose, this time, straight and clean into the evening air "
        "instead of pooling low and reluctant across the ground."
    )},
    {"type": "body", "text": (
        "The two watchers stood at the edge of the camwood ring with "
        "their hands on the hilts of tools they did not otherwise carry, "
        "unsure what threat they had been posted to guard against and "
        "unwilling to admit it, and Obi stood close enough to Amara that "
        "their shoulders touched, the two of them watching the small, "
        "rising figure of the chant the way parents watch anything that "
        "might, without warning, become a thing they cannot undo."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara felt the moment the thread gave way before she understood "
        "what she was feeling, a faint loosening in the air over her "
        "son's basket, like a held breath finally released after being "
        "held so long no one remembered it was being held at all."
    )},
    {"type": "body", "text": (
        "Elder Maka's chant broke off. She swayed once, catching herself "
        "against the nearest fire point with a hand that trembled far "
        "more than her age alone could explain, and for one instant, so "
        "brief that only Amara, trained now by weeks of watching for "
        "exactly this, thought to look closely enough to catch it, Elder "
        "Maka's eyes went dark and faintly oil sheened, the same wrong "
        "shine Kene's had carried during the cleansing rite."
    )},
    {"type": "body", "text": (
        "Then it was gone, and Elder Maka straightened, breathing hard "
        "but steady, and the rite was finished, and Kene slept on "
        "undisturbed, his small body no longer carrying whatever thin "
        "thread the entity had touched eight days into his life."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"It is done,\" Elder Maka said, and did not explain the "
        "trembling in her hand, and Amara, exhausted with relief and "
        "still uncertain what she had actually seen, did not press her "
        "for an answer she was not sure she wanted yet."
    )},
    {"type": "body", "text": (
        "Elder Maka walked home alone in the dark, as she always did, "
        "and did not tell Amara, and would not tell anyone, that binding "
        "a thread loose from a child too young to bear the whole weight "
        "of its own severing had required somewhere for that weight to "
        "go, and that she had chosen, deliberately, to let it come to "
        "rest in the one body in Idoro old enough and hard enough, she "
        "had believed, to carry it without being changed by it."
    )},
    {"type": "body", "text": (
        "She sat alone in her own compound long after the fires had "
        "burned down, flexing one hand slowly in the dark, feeling for "
        "the first time in thirty and four years a thin, unfamiliar "
        "thread running somewhere beneath her own skin, and understood, "
        "with a coldness that had nothing to do with the night air, "
        "exactly what she had just done to herself in order to spare "
        "someone else's son."
    )},
    {"type": "body", "text": (
        "She told herself it was a small price, thinner than the thread "
        "she had just cut from Kene, easily carried by a woman who had "
        "already carried far heavier things and lived. She told herself "
        "this several times, the way a person tells themselves anything "
        "they need to be true before they have any proof of it, and "
        "beneath the telling, quieter than she wanted it to be, a doubt "
        "sat waiting that no amount of telling had ever quite managed "
        "to silence, the same doubt that had waited beneath every "
        "certainty she had carried since the dawn she buried her own "
        "returned son."
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
    print("  THE DARK RISE — Episode 12: \"The Binding\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_12.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_12.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
