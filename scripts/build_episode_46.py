#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 46: "The Second Approach"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-22: Episode 46 shows the trading House pivoting after
Episode 40's failed show of force. Rather than a second armed party, it
sends a lone, unarmed envoy — a scholar rather than a mercenary —
requesting a formal, peaceful audience with "whatever speaks without a
body," framed as diplomacy rather than exploitation. With Chidebe's
garrison now holding the boundary and the crown newly invested in
appearances, Osadebe and Amara must decide whether allowing any contact
attempt, however civil, opens a door none of them can close again. In
Oso, Zara's compulsion deepens beyond the spiral: she wakes certain, for
the first time, that she is meant to walk to Idoro's boundary herself.
The entity, tracking both developments at once, recognizes with dawning
alarm that the presence may be building toward its own version of
Episode 30's unmediated reveal — but through a human mouth this time,
and on a timeline entirely its own, regardless of what Idoro's council or
the scholar's careful diplomacy decide. The episode closes on the entity
realizing it may not get to choose whether these two approaching moments
happen separately or collide.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_46.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Six"},
    {"type": "title_ep_name", "text": "The Second Approach"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A REQUEST WITH NO WEAPON BEHIND IT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The woman who walked into Idoro alone three weeks after the "
        "boundary carried no blade, no guards, and no visible wealth "
        "at all, only a satchel of books and a formal letter bearing "
        "the same House's mark that had sent armed men before her. "
        "Chidebe's soldiers stopped her at the field's edge as "
        "protocol required, and she waited there, patient and "
        "unbothered, until Osadebe himself came to receive her."
    )},
    {"type": "body", "text": (
        "\"I am not here to survey anything, Captain,\" she said, "
        "before he could ask. \"My House learned the hard way that "
        "force accomplishes nothing here worth the cost of sending it. "
        "I am a scholar of old contact, sent to request something far "
        "smaller and far more civil: a formal audience, arranged "
        "however your crown or this village judges safest, with "
        "whatever speaks from beyond that tree line. Nothing more. No "
        "digging, no soldiers, no second attempt at force.\""
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Amara, sent for the moment the woman's request was known, "
        "felt the particular dread of watching a door that had never "
        "fully closed being tested again from a gentler angle. \"Your "
        "House sent men to force an answer once already,\" she said. "
        "\"Now you send a woman with books instead of blades and call "
        "it a different offer. I am not certain it is as different as "
        "you would like me to believe.\""
    )},
    {"type": "body", "text": (
        "\"It is different in exactly one way that matters,\" the "
        "scholar answered, unoffended. \"The last visit assumed "
        "whatever guards this ground could simply be walked past. I am "
        "assuming the opposite. I am asking permission, from the "
        "people who actually live beside it, rather than testing "
        "whether permission is required at all. You may refuse me. My "
        "House instructed me to accept that answer gracefully if it "
        "comes, and I intend to honor that instruction whether they "
        "meant it sincerely or not.\""
    )},
    {"type": "body", "text": (
        "Osadebe found himself, against his own instinct, weighing "
        "the request honestly rather than dismissing it outright, "
        "aware that a crown now openly garrisoning this boundary would "
        "eventually have to answer for what it allowed and refused "
        "here, to Udo, to history, and to whatever historical account "
        "Nkiruka's old records might someday add this exact moment to. "
        "\"I will bring this to the council,\" he told her. \"It is not "
        "mine alone to grant or refuse. But I will tell you plainly, "
        "as I told the last envoy your House sent: whatever answer you "
        "receive, if you receive one at all, will not be one you can "
        "control the shape of.\""
    )},
    {"type": "body", "text": (
        "The council met beneath the mango tree that evening with "
        "Chidebe seated among them for the first time, invited by "
        "Amara herself on the reasoning that a man now responsible for "
        "this boundary's safety deserved a voice in what approached "
        "it. Ozoemena spoke first, plainly, the habit he had built "
        "since stepping down from real authority. \"We refused Idoro's "
        "own dibia the chance to speak plainly for years, out of "
        "fear,\" he said. \"I do not know if refusing this woman would "
        "be wisdom or simply the same fear wearing a newer excuse.\""
    )},
    {"type": "body", "text": (
        "Elder Maka, present at council now as a matter of quiet "
        "habit rather than formal restored authority, offered the "
        "counterweight. \"Every contact this village has ever allowed "
        "with that ground has cost someone something,\" she said. \"A "
        "healer's mind. A midwife's peace. My own son, thirty four "
        "years ago, though that cost came before any of us understood "
        "what we were dealing with. I am not against the request. I am "
        "against pretending civility makes the cost smaller.\""
    )},
    {"type": "body", "text": (
        "Chidebe, asked directly for his own view, gave the only "
        "answer his brief time in Idoro had earned him the right to "
        "give. \"I hold this boundary. I do not claim to understand "
        "what it holds back. If this council decides to allow the "
        "audience, my men will keep it orderly. If this council "
        "refuses, my men will turn her away without needing to be "
        "asked twice. Either way, the decision belongs to people who "
        "have lived beside this danger far longer than I have.\" The "
        "council adjourned without a final answer, Amara promising the "
        "scholar an answer by morning, though privately she already "
        "suspected the choice would not matter nearly as much as "
        "everyone at that meeting believed it would."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — TWO DOORS OPENING TOWARD THE SAME MOMENT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity felt Zara's compulsion "
        "deepen the same evening the scholar arrived, no longer "
        "content with tracing shapes in borrowed dirt. She woke before "
        "dawn certain of a single fact she could not explain, the way "
        "she had once woken certain of the road north: that she was "
        "meant to walk to Idoro's true boundary herself, soon, though "
        "not yet, the timing held by someone patient enough not to "
        "rush a decision that had waited three centuries already."
    )},
    {"type": "body", "text": (
        "The entity traced the shape of what was building with a "
        "careful, mounting unease it had not fully named until it "
        "held both threads side by side. A foreign House requesting "
        "formal, mediated contact through the crown's own channels. A "
        "presence quietly preparing a human mouth of its own for "
        "something that felt, in its slow patient shape, unmistakably "
        "similar to the entity's own choice to speak plainly at the "
        "boundary months before."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "VESSEL: PRESENCE APPEARS TO BE PREPARING AN UNMEDIATED "
        "CONTACT EVENT ANALOGOUS TO ENTITY'S OWN PRIOR BOUNDARY "
        "DISCLOSURE. TIMING RELATIVE TO SCHOLAR'S REQUEST UNKNOWN. "
        "RISK OF SIMULTANEOUS CONVERGENCE: UNCALCULATED."
    )},
    {"type": "body", "text": (
        "It found itself, for the first time since the parlay, "
        "genuinely uncertain whether to warn Amara of what it sensed "
        "building in Zara before the presence itself chose to reveal "
        "it. A warning risked exposing knowledge the entity had no "
        "honest way to explain having, deepening suspicion of exactly "
        "the kind it had spent months trying to soften. Silence risked "
        "letting Zara walk toward whatever the presence intended for "
        "her with no one around her prepared for what might actually "
        "happen when she arrived."
    )},
    {"type": "body", "text": (
        "Zara herself, unaware her own certainty was being weighed "
        "from two directions at once, spent that same evening sitting "
        "quietly apart from the rest of Amara's household, turning the "
        "conviction over the way a person turns over a decision "
        "already made rather than one still being reached. It did not "
        "feel like being pulled this time, the way the road north had "
        "once pulled her feet without permission. It felt like being "
        "told, plainly and without cruelty, about an appointment she "
        "had somehow always known was coming and simply had not been "
        "given the date for until now."
    )},
    {"type": "body", "text": (
        "She did not yet know whether to be afraid of that certainty "
        "or grateful for it, and found, turning it over one final time "
        "before sleep, that the not knowing itself had stopped feeling "
        "urgent. Whatever waited for her at that boundary, she "
        "understood without being told exactly how she understood it, "
        "was not something that intended to rush her toward it before "
        "she was ready to walk there on her own two feet."
    )},
    {"type": "body", "text": (
        "The boy, sensing its distraction the way he now sensed most "
        "of its moods without needing to be told, asked plainly what "
        "was wrong, and the entity found itself, once again, choosing "
        "the harder honesty over the easier comfort. \"Someone is "
        "getting ready to speak,\" it told him. \"Not me. Not you. The "
        "one who has been watching us both. I do not know when, and I "
        "do not know through whose mouth, but I no longer believe it "
        "will wait much longer to be heard.\""
    )},
    {"type": "body", "text": (
        "The boy absorbed this the way he absorbed every warning that "
        "carried real weight now, without panic, filing it carefully "
        "beside everything else he was learning to hold ready rather "
        "than simply fear. \"Will it be angry,\" he asked, \"that you "
        "spoke first, at the boundary with Osadebe, before it ever got "
        "the chance to.\""
    )},
    {"type": "body", "text": (
        "The entity turned the question over with more care than it "
        "had turned over almost anything since the parlay itself. \"I "
        "do not think anger is the right shape for whatever it feels,\" "
        "it said. \"Everything I have learned of it suggests patience "
        "so complete that speed itself may not register to it the way "
        "it registers to us. I spoke first because I judged it useful "
        "at the time. It may simply be choosing its own moment now "
        "because my moment has already passed and stopped mattering to "
        "its plans at all.\""
    )},
    {"type": "body", "text": (
        "\"That is worse,\" the boy said, with the plain, unflinching "
        "honesty the entity had come to rely on more than it liked to "
        "admit. \"I would rather it be angry. Angry, I could try to "
        "understand. Patient enough not to care what either of us "
        "does first is harder to imagine standing against.\""
    )},
    {"type": "body", "text": (
        "The entity had no honest answer that would soften that "
        "observation without also making it less true, and offered "
        "him none, choosing instead to simply sit with him in the "
        "particular silence they had both learned, across these last "
        "difficult weeks, was sometimes the only honest response left "
        "once every comforting word had already been spent."
    )},
    {"type": "body", "text": (
        "Watching him do it, the entity understood that whatever "
        "answer was coming, from whichever direction it finally "
        "arrived, neither of them would be facing it unprepared. That "
        "understanding offered less comfort than it should have, "
        "precisely because the entity itself no longer knew which of "
        "the two approaching moments it was actually less ready for."
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
    print("  THE DARK RISE — Episode 46: \"The Second Approach\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_46.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_46.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
