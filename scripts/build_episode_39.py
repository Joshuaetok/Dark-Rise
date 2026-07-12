#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 39: "Two Claims"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-15: Episode 39 brings the foreign trading House's interest
into Idoro itself for the first time — its agent arrives in person,
polite and well spoken, asking to see the ground nearest the forbidden
bush rather than anywhere a survey for buried wealth would normally
start, a detail that unsettles Osadebe and Amara more than an open threat
would have. In Oso, the entity, having spent a full day turning the single
answering sound from Episode 38 over without translating it, decides to
attempt what it has never once attempted: a direct parlay with whatever
waits past its own borders, offered on its own terms rather than
discovered by accident. It gets an answer, fragmented and difficult to
hold, but unmistakable in its shape — the vessel is not something the
entity holds alone. The episode closes on the entity forced to reckon,
for the first time, with the possibility that it has spent three
centuries preparing a claim on a child something else has never stopped
quietly asserting its own right to.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_39.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty Nine"},
    {"type": "title_ep_name", "text": "Two Claims"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A VISITOR WHO ASKS THE WRONG QUESTIONS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The stranger arrived on foot rather than by canoe, which "
        "Osadebe noted immediately as strange in a delta village where "
        "every serious visitor came by water, and walked the length of "
        "Idoro's market with the unhurried confidence of a man who "
        "had already decided the place could not surprise him. He wore "
        "good cloth, exactly as the headman downriver had described, "
        "and spoke the local tongue with a fluency that made his "
        "foreignness feel almost like an afterthought."
    )},
    {"type": "body", "text": (
        "He introduced himself only as an agent of a House whose name "
        "he did not offer, and asked, politely, whether anyone in the "
        "village could show him the ground nearest what he called, "
        "with careful neutrality, the old forbidden place. Not the "
        "farmland. Not the riverbank where a survey for oil or ore "
        "might sensibly begin, and where every other agent before him "
        "had always started. The ground closest to Oso itself."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Amara felt something in her chest go cold and still the "
        "moment she heard the request repeated to her, because a man "
        "hunting for buried wealth had no honest reason to care which "
        "particular field sat closest to a bush every trader in the "
        "region already knew to avoid. She thought immediately of the "
        "dibia's own warning, silenced years before it could ever "
        "finish, that Kene was not the only door. She wondered, "
        "watching this calm stranger wait patiently for an answer, "
        "whether he had come looking for a door of his own. Osadebe "
        "reached the same conclusion a half breath behind her and "
        "stepped forward before she could, his crown's seal "
        "deliberately visible against his chest."
    )},
    {"type": "body", "text": (
        "\"That ground is not open to survey,\" he told the stranger, "
        "with a calm that cost him more than it showed. \"Not for your "
        "House, and not, at present, for the crown either. I would ask "
        "what interest a trading concern has in unfarmed bush before I "
        "let you closer to it.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The stranger's smile did not waver, which Amara found, "
        "somehow, worse than if it had. \"My House trades in many "
        "things, Captain. Sometimes in oil. Sometimes in old stories "
        "that turn out, on closer inspection, to be worth more than "
        "the oil.\" He let the words settle before continuing, watching "
        "Amara's face rather than Osadebe's as he spoke. \"We have "
        "heard, from more than one mouth now, that something in this "
        "delta speaks without a body when it chooses to. My House has "
        "paid very well, in other kingdoms, for the chance to speak "
        "with things like that ourselves.\""
    )},
    {"type": "body", "text": (
        "He left without pressing further, promising only, with a "
        "courtesy that felt more like a threat than any raised voice "
        "could have managed, that he would return once he had \"a "
        "clearer invitation.\" Osadebe watched him walk back out of "
        "Idoro the same unhurried way he had walked in, and told "
        "Amara plainly that whatever this House actually wanted from "
        "the delta, it had nothing to do with soil worth digging and "
        "everything to do with the exact thing sleeping beneath the "
        "ak-pu roots."
    )},
    {"type": "body", "text": (
        "Word of the visit reached Elder Maka before the boundary "
        "walk group had finished for the day, and she surprised both "
        "Amara and Osadebe by naming the danger before either of them "
        "had fully shaped it themselves. \"My grandmother spoke once "
        "of houses that hunted spirits the way other traders hunted "
        "ivory or gold,\" she said, setting down the marker stone she "
        "had been examining. \"She called it an old trade, older than "
        "any of the roads we walk now, and said the men who practiced "
        "it were more patient and more dangerous than any army, "
        "because an army only wants your land. These men want whatever "
        "your land is afraid of.\""
    )},
    {"type": "body", "text": (
        "Amara felt the shape of the danger settle into something "
        "colder and more specific than fear of digging alone. A trading "
        "House chasing oil could be reasoned with, bribed, delayed, "
        "outlasted. A House chasing whatever spoke through the dibia "
        "and stood at the boundary and called itself still coming "
        "wanted something no council of elders, however honest its "
        "boundary stones, had any real way to defend."
    )},
    {"type": "body", "text": (
        "\"Then Udo needs to hear this before that man returns with "
        "his clearer invitation,\" Osadebe said, already turning "
        "toward his hut and the letter he would need to write before "
        "the light failed. \"Eze Amadi weighed a survey for soil "
        "carefully enough. I do not think he has yet imagined weighing "
        "one for whatever answered us at the boundary.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — SPEAKING ON ITS OWN TERMS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity had spent the day since "
        "the boy's defiance turning the single answering sound over "
        "without finding anywhere honest to set it down, until "
        "turning it over stopped being enough for the second time in "
        "as many weeks. If the presence beyond its borders had already "
        "chosen to speak once, on a night it had not been invited to, "
        "the entity decided it would rather be the one choosing the "
        "next time words passed between them."
    )},
    {"type": "body", "text": (
        "It waited until the boy slept soundly, undisturbed by any "
        "binding this time, and reached outward on its own terms "
        "rather than in the frightened, accidental rush of its first "
        "crossing, carrying the two soft syllables the boy had taught "
        "it without meaning to, offered now as a greeting rather than "
        "stumbled across as a mystery."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "The answer, when it came, did not arrive as a voice so much "
        "as a pressure shaped like meaning, the way a held hand can "
        "communicate refusal or welcome long before either word is "
        "spoken aloud. The entity had to work to hold the shape of it "
        "steady enough to understand, the effort costing it more than "
        "any single act of feeding ever had, three centuries of "
        "careful, contained hunger suddenly measured against something "
        "that did not appear to hunger at all, only to wait, patiently, "
        "the way the entity itself had once waited for a child small "
        "enough to claim."
    )},
    {"type": "body", "text": (
        "What it understood, once the pressure resolved into anything "
        "close to sense, was not a threat, and that absence of threat "
        "frightened the entity more thoroughly than open hostility "
        "would have. The presence did not want to take the boy from "
        "it, at least not yet, not by force. It communicated, in its "
        "slow, wordless way, something closer to correction. The "
        "entity had spent three centuries believing itself the sole "
        "author of the vessel's shaping, and the presence, without "
        "cruelty, informed it that this belief had never once been "
        "true."
    )},
    {"type": "body", "text": (
        "It pressed further, risking more of itself than it had "
        "risked in the earlier accidental crossing, asking as plainly "
        "as the strange wordless exchange allowed what claim the "
        "presence believed it held, and since when, and why it had "
        "waited three centuries of the entity's own tenancy on this "
        "ground before ever once making that claim known."
    )},
    {"type": "body", "text": (
        "The answer came slower this time, as though the presence "
        "were choosing carefully among things it could safely hand "
        "over and things it intended to keep. What arrived was not a "
        "story so much as the impression of a very long patience, "
        "older than the entity's own three centuries by a margin the "
        "entity could not measure, and a single clear certainty "
        "underneath all of it: the presence had not been waiting for "
        "the entity to notice it at all. It had been waiting for the "
        "boy to grow old enough to notice it himself, and the entity's "
        "sudden interest was, from where the presence stood, simply "
        "an inconvenience arriving slightly ahead of schedule."
    )},
    {"type": "body", "text": (
        "VESSEL: EXISTENCE OF A SECOND, PREEXISTING CLAIM CONFIRMED BY "
        "DIRECT CONTACT. NATURE, ORIGIN, AND INTENT OF SECOND CLAIM "
        "UNKNOWN. ENTITY'S ASSUMED EXCLUSIVITY OVER VESSEL INVALIDATED."
    )},
    {"type": "body", "text": (
        "It withdrew before the contact could deepen further, uncertain "
        "whether continuing to listen would teach it something worth "
        "the cost or simply hand the presence a clearer picture of "
        "exactly how unprepared it truly was. Sitting afterward beside "
        "the boy's small sleeping shape, arranging stones even in "
        "sleep the way he arranged everything else in his waking hours, "
        "the entity found itself facing a question it had never once "
        "needed language for before tonight."
    )},
    {"type": "body", "text": (
        "It had spent this entire careful season deciding how much of "
        "itself to give the boy honestly, weighing every word against "
        "what claim that word might stake. It had never once "
        "considered that somewhere past its own borders, something "
        "older and infinitely more patient had been making exactly "
        "the same calculation about the very same child, for exactly "
        "as long, and had simply never once felt the need to announce "
        "it until the entity itself came looking."
    )},
    {"type": "body", "text": (
        "It thought, too, of the well dressed stranger it had no way "
        "yet of knowing had walked through Idoro's market that same "
        "afternoon asking after ground closest to its roots, and felt, "
        "for the first time in three centuries of patient, contained "
        "certainty, the particular unease of a thing that had always "
        "assumed itself to be the most dangerous presence in any room "
        "it entered, discovering slowly and from more than one "
        "direction at once that this assumption may never have been "
        "entirely earned."
    )},
    {"type": "body", "text": (
        "The boy slept on, arranging some private, dreaming order "
        "among his stones, entirely unaware that in the space of a "
        "single day, two separate and much older powers had each, in "
        "their own careful way, decided he was worth reaching for "
        "before the other one could."
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
    print("  THE DARK RISE — Episode 39: \"Two Claims\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_39.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_39.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
