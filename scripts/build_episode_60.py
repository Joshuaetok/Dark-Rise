#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 60: "A Voice Not His Own"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-05: Episode 60 closes the ten episode block that began
with Episode 51's ambush. At the boundary, the Factor lays out his
House's true offer: not capture, not simple peace, but partnership,
Chibundu and the entity as guardians whose blessing would legitimize
his House's extraction of Oso's ground, in exchange for wealth,
protection, and an end to all further aggression against Idoro. It is
a seductive, morally grey argument built on a real truth: someone will
eventually come for this ground, guardian or not, and the Factor
offers to be the version of that hunger Idoro can actually survive.
Chibundu, weighing an offer that could end his family's danger
forever, begins to answer on his own terms exactly as he insisted on
doing — and mid word, for the first time in his life, his own voice is
taken from him. The presence, which stirred uninvited at the end of
Episode 59, seizes him directly rather than Zara, refusing the offer
before he can, and the block ends on the exact violation of his own
hard won agency that this entire block was quietly building toward,
witnessed by a Factor who now understands there are two old powers at
this boundary, not one.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_60.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty"},
    {"type": "title_ep_name", "text": "A Voice Not His Own"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE TRUE OFFER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"You set your own terms for this meeting,\" the Factor said, "
        "once the pleasantries had passed and the watching distances "
        "had settled into their places. \"I respect that more than I "
        "can easily explain. Most grown men I deal with never learn to "
        "ask for exactly what safety requires and no more. You arrived "
        "at it before your first year of life was finished.\""
    )},
    {"type": "body", "text": (
        "\"You did not walk this far to admire my manners,\" Chibundu "
        "said, and felt, saying it, the same steady readiness he had "
        "practiced the night before settle into place beneath the "
        "words. \"Tell me plainly what you actually want, the way you "
        "asked me to be plain with you.\""
    )},
    {"type": "body", "text": (
        "The Factor considered him a long moment before answering, the "
        "unhurried consideration of a man deciding how much truth a "
        "listener has actually earned. \"I have walked this delta for "
        "twenty years in my House's service,\" he said. \"I have seen "
        "villages upriver from here poisoned slowly by men who took "
        "what was under their soil and gave nothing honest back for "
        "it, and I will not insult you by pretending my own House's "
        "hands are entirely clean of that history. I am not here "
        "offering you a stranger's kindness. I am here offering you the "
        "chance to make the next hunger that reaches this ground "
        "answerable to someone, rather than answerable to no one at "
        "all, the way every hunger before it has been.\""
    )},
    {"type": "body", "text": (
        "The Factor's easy warmth did not vanish, but something behind "
        "it sharpened into the true shape it had been wearing all "
        "along. \"My House does not want to fight what guards you,\" he "
        "said. \"We have learned, at considerable cost in other places, "
        "that fighting an old, patient power is the single most "
        "expensive mistake a House can make. We want, instead, to work "
        "beside it. This ground, and the ground surrounding it, holds "
        "wealth beneath the soil that has drawn eyes to this delta for "
        "longer than your village has kept its old law. Someone will "
        "come for it eventually. I am offering you the chance to decide "
        "what kind of someone that turns out to be.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT PEACE WOULD COST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"You want to dig here,\" Chibundu said slowly, turning the "
        "offer over the way he turned over every hard thing now, "
        "refusing to let its size decide his answer before he had "
        "finished understanding its shape. \"And you want me, and "
        "whatever guards me, to stand over the digging and make it safe "
        "for you to do it.\""
    )},
    {"type": "body", "text": (
        "\"I want your blessing on it,\" the Factor said. \"Nothing more "
        "dramatic than that. In exchange, my House ends every "
        "hostility against Idoro permanently, in writing, witnessed by "
        "the crown itself if your council prefers it that way. Wealth "
        "flows to your village rather than only out of this ground. "
        "Your mother's family wants for nothing, ever again, and no "
        "soldier or scholar or Factor ever needs to darken this "
        "boundary uninvited again in your lifetime. I am not asking "
        "you to become a weapon. I am asking you to become the reason "
        "no one else's weapon ever has to be used here.\""
    )},
    {"type": "body", "text": (
        "\"You told the council you would rather be answerable for a "
        "hunger than let it come unanswerable,\" Chibundu said slowly. "
        "\"You did not say whether the villages you already poisoned "
        "upriver were given that same choice, or whether it was simply "
        "made for them by someone who decided, the way you are asking "
        "me to decide now, that they would thank you for it "
        "eventually.\""
    )},
    {"type": "body", "text": (
        "The Factor's easy composure did not break, but something in "
        "his eyes acknowledged the hit landing true. \"They were not "
        "given that choice,\" he said. \"That is precisely why I have "
        "walked here alone and unarmed to offer it to you instead of "
        "simply taking what my House wants the way it was taken "
        "upriver. I am not asking you to trust that my House has "
        "changed its nature. I am asking you to be the reason it "
        "cannot behave the same way here that it behaved there.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt the whole weight of it land in him at once, an "
        "offer built cleverly enough to be almost entirely true, a "
        "peace that would cost Idoro nothing it could immediately see "
        "and would cost only the ground itself, quietly, the way the "
        "Oji Delta had already been costing other villages for longer "
        "than his own life had existed. He thought of Amara waiting at "
        "the furthest line. He thought of Kene, and of a danger that "
        "could simply, finally, stop."
    )},
    {"type": "body", "text": (
        "\"I want to hear the terms in full,\" he began, weighing each "
        "word with the same careful precision he had used to set every "
        "condition of this very meeting, \"before I tell you whether "
        "there is any version of this I could...\""
    )},
    {"type": "body", "text": (
        "Far away, beneath Oso, the ledger voice registered the "
        "seizure."
    )},
    {"type": "system", "text": "Vessel vocal control interrupted. Source: unidentified, external, non entity. Entity intervention protocol not triggered. No name spoken."},
    {"type": "body", "text": (
        "The word died in his own throat, and what came out instead "
        "was not his voice shaping his own next thought. It arrived "
        "whole, calm, and utterly unhurried, in a register Chibundu "
        "recognized with a lurch of pure horror as belonging to the "
        "cold place rather than to himself. \"No,\" his own mouth said, "
        "without his permission, without his will anywhere inside the "
        "shaping of it. \"There is no version of this he accepts. I "
        "have watched this exact offer made once before, in another "
        "place, by a hunger wearing a gentler face than yours. I did "
        "not stop it in time then. I will not make that mistake "
        "twice.\""
    )},
    {"type": "body", "text": (
        "The entity felt every part of its own held stillness shatter "
        "at once, three centuries of careful restraint colliding "
        "headlong with a promise it had made only the night before, "
        "unable to move without breaking a vow to a boy whose own "
        "voice had just been taken from him by something the vow had "
        "never once accounted for. It had promised to wait for its own "
        "name. No one had ever thought to promise anything against "
        "this."
    )},
    {"type": "body", "text": (
        "Chibundu felt his own mouth close again, his own breath "
        "return to him, and understood, in the sudden, ringing silence "
        "that followed, that for the first time since he had learned "
        "to want anything at all, a choice that belonged entirely to "
        "him had been made by someone else's voice, wearing his own "
        "throat as its instrument, exactly the way the presence had "
        "once worn Zara's."
    )},
    {"type": "body", "text": (
        "The Factor did not move, did not reach for anything, only "
        "studied the boy in front of him with an attention that had "
        "sharpened past warmth entirely now into something closer to "
        "genuine, delighted alarm. \"That,\" he said quietly, \"was not "
        "the same voice that greeted me. I came prepared to bargain "
        "with one old power standing behind this boundary. I find I "
        "have just been answered by a second, and I confess, watching "
        "you struggle to reclaim your own mouth in front of me, that I "
        "no longer know which of you my House should actually be "
        "afraid of.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: WHAT THE FAR LINE SAW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "From Chidebe's furthest line, Amara had heard none of the "
        "words, only watched the shape of her son's posture change in "
        "a way that reached her before any sound could have, a "
        "wrongness in how suddenly still he went, the particular "
        "stillness of a puppet finding its strings pulled by a hand "
        "that was not its own. \"Something is wrong,\" she said aloud, "
        "already moving before she had finished deciding to, and felt "
        "Osadebe's hand close firm on her arm."
    )},
    {"type": "body", "text": (
        "\"He did not say your name,\" Osadebe said, his own voice "
        "tight with the effort of holding a line he had promised to "
        "hold. \"Whatever this is, it was not the danger any of us "
        "planned for, and running blind into it will not help him "
        "reclaim whatever has just been taken.\" Amara stopped, every "
        "instinct in her screaming to close the distance regardless, "
        "and held herself at the line through sheer, furious will "
        "alone."
    )},
    {"type": "body", "text": (
        "The entity felt its own three centuries of careful patience "
        "arrive at the one test it had never once rehearsed for: not "
        "a blade, not an army, not even the Factor's soft, reasonable "
        "voice, but something reaching directly into the boy it had "
        "raised and closing its hand around the one thing the entity "
        "had spent this entire season teaching him to hold for "
        "himself. It took one step forward, the promise it had made "
        "the night before straining against a danger that promise had "
        "never been built to answer, uncertain, for the first time in "
        "three hundred years, whether keeping its word or breaking it "
        "was the greater failure it was about to commit."
    )},
    {"type": "body", "text": (
        "Chibundu felt his own hands come back to him first, curling "
        "and uncurling at his sides the way they had the very first "
        "night he had ever fought for control of them, and understood, "
        "testing his own throat with a small, private sound only he "
        "could hear, that he could not yet be certain the voice that "
        "answered the Factor was finished speaking through him. He had "
        "asked, the night before, to be the only one standing where "
        "the Factor could see him. Something older than either of them "
        "had just proven, in front of a watching stranger and a "
        "watching kingdom, that the boundary he thought he stood at "
        "alone had never once been his to hold by himself."
    )},
    {"type": "body", "text": (
        "The Factor watched him test his own voice with the same "
        "patient, calculating interest he had brought to every word of "
        "the meeting, already reshaping, behind his still perfectly "
        "composed face, everything he would carry back to his House "
        "about what this boundary actually guarded. Behind them all, "
        "held at the furthest line by nothing but her own will and a "
        "captain's steady hand, Amara watched her son's shoulders shake "
        "once, twice, and understood, unable to hear a single word that "
        "had passed between him and the stranger facing him, that "
        "whatever answer this meeting produced, it had cost him "
        "something none of them had thought to prepare him for."
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
    print("  THE DARK RISE — Episode 60: \"A Voice Not His Own\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_60.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_60.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
