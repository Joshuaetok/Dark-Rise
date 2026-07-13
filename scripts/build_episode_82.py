#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 82: "The Same Hand"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-27: Episode 82 resolves Episode 81's cliffhanger. Amara
breaks the bridge between Zara and Adaugo by force, and the presence
tears itself backward out of the anchor thread hard enough to drop
Zara into Elder Maka's arms, gasping but alive, at a further cost the
presence again cannot fully explain. In the half second before it
disengaged, the presence recognized the shape of the craft behind the
working, the same signature technique used by the hunter who took its
guardian ground centuries ago, meaning Mfoniso is not simply skilled,
she was trained in or descended from that same lineage. Adaugo's
anchor thread remains active and uncut, too costly to touch again
tonight. The episode closes on Mfoniso herself, unsettled to have felt
something reach back along her own working for the first time in her
career, and deciding patience has just become a luxury she can no
longer afford.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_82.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Two"},
    {"type": "title_ep_name", "text": "The Same Hand"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE SEVERING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara's hand closed around Adaugo's wrist and wrenched it free "
        "of Zara's grip before her own mind had finished deciding to "
        "move, breaking the bridge the way a mother breaks anything "
        "standing between her child and danger, without asking whether "
        "it was the right thing to break. For one terrible heartbeat "
        "nothing changed. Zara's back stayed arched, her mouth still "
        "open around a sound that refused to come."
    )},
    {"type": "body", "text": (
        "Then the presence tore itself backward through her all at "
        "once, a force Zara felt in her own spine like a rope pulled "
        "taut and cut in the same instant, and she dropped flat against "
        "Elder Maka's arms, gasping the way a woman gasps when pulled "
        "up too fast from water far deeper than she meant to swim in."
    )},
    {"type": "body", "text": (
        "\"Zara.\" Elder Maka held her upright, searching her face for "
        "whatever had been left behind. \"Zara, look at me.\" It took "
        "three long breaths before Zara's eyes found her, glassy and "
        "unfocused, and three more before the words in them belonged "
        "fully to Zara again rather than to whatever had been speaking "
        "through her a moment before."
    )},
    {"type": "body", "text": (
        "\"I am here,\" Zara managed finally, her voice raw, as though "
        "she had been the one shouting rather than the one gone silent. "
        "\"It let go. It let go of me before it let go of whatever it "
        "was reaching for.\" She pressed a shaking hand to her own chest, "
        "checking, the way a person checks themselves for a wound after "
        "surviving a fall they should not have survived."
    )},
    {"type": "body", "text": (
        "Obi crouched beside her, steadying her shoulder, while Amara "
        "held Adaugo close on the other side, both girls trembling in a "
        "circle none of them had chosen to stand inside. \"What did you "
        "feel,\" Amara asked, gentler than the fear in her own voice "
        "should have allowed. \"At the end. Before we pulled you free.\""
    )},
    {"type": "body", "text": (
        "\"Not me,\" Zara said. \"It. Something reached along the "
        "thread toward the presence itself, not toward me, not toward "
        "Adaugo. Like it recognized what was looking at it and did not "
        "like being recognized.\" She shook her head slowly, still "
        "catching her breath. \"I do not think it was trying to hurt "
        "me. I think I was simply standing in the doorway when two much "
        "older things noticed each other.\""
    )},
    {"type": "body", "text": (
        "Adaugo pulled her knees up to her chest and pressed her "
        "forehead against them, unable to look at either of the women "
        "who had nearly paid for her carelessness with something worse "
        "than fear. \"You should not have done that for me,\" she said, "
        "muffled, to Zara. \"Not when you are already carrying so "
        "little strength to spare.\" Zara reached over despite her own "
        "trembling hands and took Adaugo's chin, lifting it gently until "
        "their eyes met. \"I did not do it for you instead of myself,\" "
        "she said. \"I did it because you are already family, and "
        "family is the only thing worth spending what little I have "
        "left on.\" It was the first time either of them had said the "
        "word aloud between them, and it settled over the compound with "
        "a quiet weight neither fear nor exhaustion could touch."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE PRESENCE RECOGNIZED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, the entity felt the presence return the way a person "
        "returns from a plunge into cold water, all at once and shaking "
        "with it, and for the first time in their long uneasy "
        "acquaintance, the entity reached toward it without being asked. "
        "\"You are hurt,\" it said, not a question. The presence did not "
        "deny it. It simply did not yet have the strength to answer in "
        "anything but fragments."
    )},
    {"type": "body", "text": (
        "Chibundu felt the exchange rather than heard it, the way he "
        "had learned to feel the weather of both powers' moods long "
        "before either explained itself in words. \"What happened,\" he "
        "asked, unwilling to wait for the fragments to become a full "
        "sentence on their own. \"Tell me now, not once you have decided "
        "how gently to say it.\""
    )},
    {"type": "body", "text": (
        "The presence answered slowly, each word costing it visibly. "
        "\"I know that craft,\" it said. \"Not the woman's face. Not her "
        "name. The shape of the working itself, the exact manner in "
        "which it was tied to close around a wrist and left to wait. I "
        "have felt hands work this way only once before, three "
        "centuries ago, on the night my own guardian ground was taken "
        "from me.\""
    )},
    {"type": "body", "text": (
        "Chibundu went very still. \"You are certain,\" he said, though "
        "he already knew the answer from the way the presence had said "
        "it, without its usual careful hedging. \"You are certain this "
        "is the same hand.\""
    )},
    {"type": "body", "text": (
        "\"Not the same hand,\" the presence said. \"That hunter is "
        "centuries dead, if hunters like that die the way ordinary "
        "people do. But no one invents a working this precise alone, "
        "and no one teaches it carelessly. Mfoniso did not stumble onto "
        "this method. She was given it, by someone who learned it from "
        "someone who learned it from whoever took my ground from me. "
        "She is not merely skilled, Chibundu. She is an inheritance.\""
    )},
    {"type": "body", "text": (
        "The entity absorbed that in silence, turning over three "
        "centuries of caution in the space of a breath. \"That changes "
        "what we are facing,\" it said finally. \"A skilled hunter can "
        "be outthought. A tradition passed down and refined across "
        "generations has already accounted for everything a guardian "
        "and its family are likely to try.\" It paused. \"Including, "
        "perhaps, tonight.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT COULD NOT BE FINISHED TONIGHT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Back in the compound, Elder Maka helped Zara to a seat near "
        "the fire and would not let her rise again until she had eaten "
        "something and drunk twice as much water as she claimed to "
        "want. Adaugo sat pressed against her mother's side, one hand "
        "wrapped protectively over the wrist that still carried, "
        "invisible and untouchable, whatever Mfoniso had left there."
    )},
    {"type": "body", "text": (
        "\"We cannot try again tonight,\" Elder Maka said, and no one in "
        "the compound argued with her. \"Not the reading. Not a "
        "severing. Whatever nearly happened in that doorway, we are not "
        "prepared to face it a second time before dawn.\" She looked at "
        "Adaugo with the particular grief of a mother who cannot yet "
        "promise the danger is over. \"You will sleep between your "
        "mother and me tonight, and every soldier Chidebe can spare will "
        "stand within call of this compound until first light.\""
    )},
    {"type": "body", "text": (
        "Amara sent word to Chidebe before the sentence had fully "
        "finished leaving Elder Maka's mouth, and within the hour the "
        "compound wall carried more watching eyes than it had held "
        "since the night Kene was nearly taken from his own bed. "
        "Osadebe arrived still smelling of river mud, refusing the rest "
        "Chidebe offered him, and took up a post at the gate himself "
        "rather than hand the watch to a soldier who had not seen the "
        "woman's face. \"I have chased her once tonight and lost her "
        "once tonight,\" he said, when Amara tried to send him to sleep. "
        "\"I will not add losing this house to the same evening.\""
    )},
    {"type": "body", "text": (
        "Chidebe walked the wall himself twice before settling, counting "
        "his men aloud under his breath the way he counted them before "
        "every crisis this family had survived, as though the number "
        "itself might hold steadier than his own nerves. No one spoke "
        "of sleep for themselves. They spoke instead, in low voices "
        "around the fire, of what an anchor thread might cost them by "
        "morning, and whether a working built to be found could ever "
        "truly be cut free of the girl who now carried it."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT MFONISO FELT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A full night's walk from the third bend, Mfoniso sat very "
        "still beside a fire she had not lit for warmth, one hand "
        "pressed flat against her own chest where the thread's distant "
        "end lived quietly inside her, always. She had felt hundreds of "
        "anchors answer their holders over the long years of her craft. "
        "She had never once, in all that time, felt one reach back."
    )},
    {"type": "body", "text": (
        "It had lasted less than a breath, a cold pressure against the "
        "thread as though something enormous and old had leaned close "
        "to look directly at her through it, and then it was gone as "
        "suddenly as it had come, leaving only the ordinary hum of a "
        "working doing exactly what it was built to do. She did not "
        "believe it was an accident. Nothing about that family had been "
        "accidental in weeks."
    )},
    {"type": "body", "text": (
        "She thought, briefly and without wanting to, of the warning "
        "her own teacher had given her only once, years ago, about the "
        "handful of guardians old enough to remember being hunted "
        "before. Most guardians reacted to a threat the way a struck "
        "animal reacts, all instinct and no memory. A guardian that "
        "recognized the shape of an old wound reopening was a different "
        "animal entirely, one her teacher had refused to describe in "
        "more detail than a single sentence. It remembers what was done "
        "to it, her teacher had said, and it will not forgive being "
        "reminded twice."
    )},
    {"type": "body", "text": (
        "Mfoniso rose and began breaking camp, unhurried in her hands "
        "even as something unfamiliar moved beneath her calm. Patience "
        "had carried her this far without a single wasted step, and "
        "patience was the one thing every teacher she had ever studied "
        "under agreed was worth more than speed. But a guardian that had "
        "just proven it could reach back along her own working was no "
        "longer a danger she could afford to watch from a comfortable "
        "distance. \"Not tonight,\" she said quietly, to no one, folding "
        "the last of her things into her pack. \"But soon. Sooner than I "
        "had planned to move.\""
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
    print("  THE DARK RISE — Episode 82: \"The Same Hand\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_82.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_82.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
