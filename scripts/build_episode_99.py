#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 99: "The Search They Owed Him"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-14: Episode 99 finally turns the household's attention
to the search for Ijeoma, a promise made back in Episode 88 and delayed
ever since by the confrontation, its aftermath, and the survey crisis.
Emenike, strong enough now to insist rather than merely hope, raises
the question the household has been quietly avoiding. Osadebe formally
requests crown support for the search, leveraging the same
investigation authority Eze Amadi granted in Episode 94, and receives
it. Ubani's completed survey maps, covering the country well beyond
Oso itself, give the household its first real picture of the western
ground Emenike's captors' bearing pointed toward. A small search party
is assembled: Osadebe, Emenike himself over Chidebe's hesitation, and
two soldiers, to depart within the week. The episode closes with
Chibundu carrying word of the search to the entity and the presence,
and the presence going very still at the mention of the exact bearing,
west and slightly south, unwilling yet to say why.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_99.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Nine"},
    {"type": "title_ep_name", "text": "The Search They Owed Him"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE QUESTION NO ONE HAD ASKED ALOUD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Emenike found Amara at the fire the evening the survey's dust "
        "had finally settled on the market road, standing steadier on "
        "his own feet than he had in weeks, and asked the question the "
        "whole household had let itself set quietly aside through crisis "
        "after crisis. \"When do we go looking for my sister,\" he said. "
        "\"I have not forgotten that you promised. I do not think you "
        "have forgotten either. I think everyone has simply been too "
        "afraid to be the one who says it is time.\""
    )},
    {"type": "body", "text": (
        "Amara did not flinch from the question, though the honesty of "
        "it landed with real weight. \"You are right,\" she said. \"We "
        "let the confrontation delay it, and then the recovery, and "
        "then the survey, and each delay had its own good reason, and "
        "none of those reasons were fair to Ijeoma.\" She rose from the "
        "fire with new purpose. \"That ends tonight. We plan properly, "
        "starting now.\" She did not sit back down again for the rest "
        "of that evening, moving instead between Chidebe, Osadebe, and "
        "Elder Maka with a restless energy the household had not seen "
        "from her since the days before the confrontation."
    )},
    {"type": "body", "text": (
        "Zara, sitting nearby with Adaugo, felt her own borrowed sense "
        "stir faintly at the exchange, the same uncertain flicker she "
        "had been nursing since the survey's departure, and wondered "
        "whether it was returning strongly enough yet to be trusted "
        "with something this important. \"If it comes back further "
        "before you leave,\" she told Emenike, \"I want to walk the "
        "first stretch of the road with you. Not the whole search. Just "
        "far enough to be certain I have given you everything I still "
        "have to give.\" Emenike thanked her, moved more than he showed."
    )},
    {"type": "body", "text": (
        "Adaugo, listening, thought of her own months spent waiting for "
        "someone else's rescue and found herself wanting badly to be "
        "useful to this one instead of merely hopeful about it. \"I "
        "cannot walk that far from Elder Maka's teaching yet,\" she "
        "said, half to herself, \"but I can help plan it properly. I "
        "have learned, this year, exactly how much a plan matters when "
        "someone you love is the one at risk.\""
    )},
    {"type": "body", "text": (
        "Ozoemena, hearing of it within the hour, arrived at the "
        "council fire without being summoned, unwilling to let this "
        "particular reckoning happen without him. \"I asked this house "
        "once to judge Emenike by more than his worst hour,\" he said. "
        "\"I will not now let it forget the promise it made him in "
        "return. A house that keeps its harder promises only when "
        "convenient has not truly kept them at all.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE MAPS AND THE CROWN COULD OFFER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe brought Ubani's finished survey maps to the council "
        "the following morning, spreading them across the same flat "
        "stone that had once held Chidebe's hide sketches of patrol "
        "routes, and found, for the first time, an honest picture of "
        "the country west and slightly south of Idoro rather than a "
        "guess built entirely on Emenike's secondhand account of his "
        "captors' bearing."
    )},
    {"type": "body", "text": (
        "\"It is not a map of everything,\" Osadebe said, tracing the "
        "bearing line with one finger. \"Ubani's survey stopped well "
        "short of wherever Ijeoma is actually held. But it takes us "
        "further than guesswork ever could, and I intend to use the "
        "same crown authority Eze Amadi granted for the trading House "
        "investigation to formally request soldiers and provisions for "
        "this search. This is no longer only a household's private "
        "grief. It is evidence in the crown's own inquiry.\""
    )},
    {"type": "body", "text": (
        "The request, sent by fast rider the same day, returned crown "
        "approval within a week, faster than any request Osadebe had "
        "ever sent north, a small, concrete proof of how thoroughly the "
        "crown's reckoning after his report had changed how quickly Udo "
        "now moved on Idoro's behalf."
    )},
    {"type": "body", "text": (
        "Nkiruka's name appeared at the bottom of the crown's reply "
        "alongside Eze Amadi's own seal, a personal note rather than a "
        "formal clause, reminding Osadebe to record everything the "
        "search learned of the western ground in detail, whatever its "
        "outcome. He did not know, reading it, that she was quietly "
        "hoping this search might finally answer a question her own "
        "archive had left unfinished since the border village whose "
        "record simply stopped."
    )},
    {"type": "body", "text": (
        "Amara raised the harder question the council had been "
        "circling without naming since the request first left for Udo. "
        "\"And if what we find at the end of this bearing is not Ijeoma "
        "alone,\" she said, \"but the same headquarters that has held "
        "her, and everyone else this House has ever taken.\" Osadebe "
        "had no easy answer for that. \"Then we will have found "
        "something the crown's own investigation needs far more than a "
        "single household's grief,\" he said. \"I would rather walk "
        "into that possibility prepared than pretend it away simply "
        "because it frightens us.\""
    )},
    {"type": "body", "text": (
        "Chidebe argued, as he had argued once before about a different "
        "decision, that Emenike was not yet strong enough to walk a "
        "search this uncertain, and Emenike, present for the argument "
        "this time rather than absent from it, refused the objection "
        "outright. \"I have spent two seasons letting other people "
        "decide what I was strong enough to bear,\" he said. \"I will "
        "not let it happen again over the one thing I have any right "
        "left to insist on. She is my sister. I am going.\" Chidebe, "
        "hearing the plain refusal beneath the request, did not argue "
        "further."
    )},
    {"type": "body", "text": (
        "The party took its final shape by the week's end: Osadebe "
        "leading, Emenike beside him despite every remaining ache in "
        "his side, and two soldiers Chidebe trusted enough to send this "
        "far from the garrison's usual reach, each one told plainly "
        "what the search was truly for before he agreed to volunteer, "
        "so that no man walked into uncertain country believing it was "
        "only an ordinary patrol. Amara offered Chibundu's "
        "help through the entity, a way to ask Oso's borrowed knowledge "
        "of the western country for anything it might know that Ubani's "
        "instruments could not have measured, and Elder Maka carried "
        "the request to Oso herself that same evening."
    )},
    {"type": "body", "text": (
        "Osadebe spent the last evening before departure walking the "
        "chosen route on Ubani's map a final time with the two soldiers "
        "he had selected, quiet, capable men named Ifeanyi and Okonjo "
        "who had both served through the worst of the confrontation "
        "without flinching, and satisfied himself that the party "
        "carried exactly the balance of speed and strength the "
        "uncertain ground ahead would demand. Both men studied the map "
        "in silence and asked only practical questions, about water, "
        "about ground, about what to do if the bearing failed them, "
        "which was exactly why he had chosen them."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE PRESENCE WOULD NOT YET SAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu carried Elder Maka's request to the entity that "
        "night, laying out the search's shape as plainly as she had "
        "given it to him: a small party, a rough bearing, west and "
        "slightly south, toward country none of them had ever needed "
        "to name before Emenike's sister was taken from it."
    )},
    {"type": "body", "text": (
        "Amara sat with Elder Maka through the same evening, both of "
        "them too aware of how much this search resembled every other "
        "desperate journey this family had ever sent into uncertain "
        "ground, and neither pretending the resemblance did not worry "
        "her. \"We have lost people to journeys shorter than this one,\" "
        "Amara said quietly. Elder Maka took her hand. \"We have also "
        "gained people from journeys just as uncertain,\" she said. \"I "
        "will not promise you which this one becomes. I will promise "
        "you we have earned the right, finally, to try.\""
    )},
    {"type": "body", "text": (
        "The entity considered it honestly, weighing what little it "
        "knew of ground so far beyond its own claimed boundary. \"I can "
        "offer you little,\" it admitted. \"My knowledge of that country "
        "is old and secondhand, learned from travelers rather than "
        "walked myself. But there is one among us who has reason to "
        "know that direction better than either of us.\""
    )},
    {"type": "body", "text": (
        "The presence, who had said almost nothing through the entire "
        "exchange, went very still the instant the bearing was spoken "
        "aloud a second time, a stillness Chibundu had learned, across "
        "years of knowing it, never to mistake for simple silence. "
        "\"West and slightly south,\" it repeated slowly, as though "
        "testing whether the words would feel different the second "
        "time they were said."
    )},
    {"type": "body", "text": (
        "\"You know this ground,\" Chibundu said, not quite a question. "
        "The presence did not answer immediately, and when it did, its "
        "voice carried a weight he had rarely heard from it even in "
        "its most difficult confessions. \"I know a direction,\" it "
        "said. \"Not a place. A direction I have not let myself think "
        "about in three centuries, because thinking about it never once "
        "changed what was already lost.\" It paused, and Chibundu felt, "
        "for the first time, something in the presence that resembled "
        "hope trying very hard not to be hope yet. \"I am not ready to "
        "say why. Send your search party toward that bearing. And when "
        "they draw close enough, however this ends for Emenike's "
        "sister, come and tell me exactly what ground they finally "
        "stand on.\""
    )},
    {"type": "body", "text": (
        "Chibundu did not press further, recognizing in the presence's "
        "voice the same careful, guarded hope he had once heard from "
        "Emenike himself, a man who had learned the hard way that hope "
        "spoken too soon and too loudly only made its own disappointment "
        "crueler. He carried the promise back to Elder Maka exactly as "
        "given, and said nothing yet of what he suspected it might mean, "
        "unwilling to hand the household one more uncertain thread to "
        "carry before the search had even left the compound gate."
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
                    first_line_indent=None, spacing_before=0):
    p = make_element("p")
    pPr = make_element("pPr")

    spacing_attrs = {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    }
    if spacing_before:
        spacing_attrs[f"{{{NS_WORD}}}before"] = str(spacing_before)
    spacing = make_element("spacing", spacing_attrs)
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


def make_body_paragraph(text, spacing_after=60, spacing_line=360,
                        spacing_before=0):
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=360,
                           spacing_before=spacing_before)


def make_system_paragraph(text, spacing_after=120, spacing_line=360,
                          spacing_before=0):
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line, alignment="left",
                           first_line_indent=0,
                           spacing_before=spacing_before)


def make_blank_paragraph(spacing_after=0, spacing_line=360):
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                           spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

# Vertical space (twips) inserted before the first paragraph of a new scene.
# 480 twips = 24pt: the page shows a clear scene break, but no empty
# paragraph exists for the TTS engine to turn into dead air.
SCENE_BREAK_SPACE = 480

def build_document_xml():
    document = Element(
        qn("document"),
        {f"{{{NS_MC}}}Ignorable": "w14 wp14"},
    )

    body = SubElement(document, qn("body"))

    pending_scene_break = False

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

        if typ == "scene_break":
            pending_scene_break = True
            continue

        before = SCENE_BREAK_SPACE if pending_scene_break else 0

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
            para = make_body_paragraph(text, spacing_before=before)
            pending_scene_break = False
        elif typ == "system":
            para = make_system_paragraph(text, spacing_before=before)
            pending_scene_break = False
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

# --- LINT (TTS pacing, CLAUDE.md Section 3.10) ---

def lint_content():
    """Check narration text for TTS pacing violations."""
    problems = []
    for i, item in enumerate(EPISODE_CONTENT):
        if item["type"] not in ("body", "system"):
            continue
        text = item["text"]
        if "\u2014" in text or "\u2013" in text:
            problems.append(f"  item {i}: contains a dash: {text[:60]}")
        if "  " in text:
            problems.append(f"  item {i}: double space: {text[:60]}")
        if re.search(r"\w-\w", text):
            problems.append(f"  item {i}: hyphenated word: {text[:60]}")
    return problems


def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 99: \"The Search They Owed Him\"")
    print("  Build Script")
    print("=" * 60)
    print()

    problems = lint_content()
    if problems:
        print("  LINT PROBLEMS:")
        for p in problems:
            print(p)
        print()
    else:
        print("  Lint clean: no dashes, double spaces, or hyphenated words")

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_99.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_99.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
