#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 51: "The Choice at the Boundary"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-27: Episode 51 opens the new ten episode block by resolving
the ambush the entity and Chibundu sensed closing at the very end of
Episode 50. The trading House's men move on the boundary through the
window Chidebe's mercy left open. Chibundu, trained across the last
several episodes to hold his will rather than only release it, acts
first, restraining rather than killing, a deliberate departure from the
entity's own lethal instinct at the same boundary in Episode 40. The
entity intervenes only once, when a single attacker breaks through
toward Amara, and kills him without hesitation. The immediate danger
ends in seconds. But the episode's real hook arrives after the fighting
stops, when a captured, half conscious operative reveals the House knew
not merely that the boundary would be undefended, but the precise two
hour window Osadebe had arranged in private, with only a handful of
people ever told the hour, none of them outside Idoro.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_51.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty One"},
    {"type": "title_ep_name", "text": "The Choice at the Boundary"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE BREAKING SILENCE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu felt the decision arrive inside him a half breath "
        "before the entity spoke a single word, felt it the way he had "
        "felt the surge at Idoro's field months before, except this "
        "time there was no wild need searching for somewhere to land, "
        "only the clean, patient readiness of something he had spent "
        "weeks learning to hold rather than release the moment it woke "
        "in him."
    )},
    {"type": "body", "text": (
        "He stepped in front of his mother without deciding to, the way "
        "his own body had already decided for him once before at a "
        "boundary very much like this one, and watched five shapes "
        "break from the dark beyond the tree line, moving low and fast "
        "and utterly without sound in a way that told him plainly these "
        "were not lost traders who had wandered into the wrong field by "
        "accident."
    )},
    {"type": "body", "text": (
        "The cold voice tallied the field even as the boy moved."
    )},
    {"type": "system", "text": "Vessel will response active. Five hostiles closing from unguarded sector. Maternal figure directly behind primary position. Lethal force not yet required."},
    {"type": "body", "text": (
        "\"Chibundu,\" Amara said, his name catching in her throat, "
        "reaching for him with the same hand that had been resting "
        "against his arm a moment before in something that had felt, "
        "impossibly, like an ordinary evening between a mother and her "
        "son. He did not let her pull him back. \"Stay behind me,\" he "
        "told her, his voice steadier than his own racing heart had any "
        "right to make it. \"I have trained for this.\""
    )},
    {"type": "body", "text": (
        "The entity felt the same choice arrive inside itself with no "
        "time left to weigh it carefully: strike now, before the five "
        "men closed the last of the distance, and prove to every "
        "watching eye, human and otherwise, exactly how far it would go "
        "to protect what it loved, or hold one more breath and let the "
        "boy it had spent weeks training answer this on his own terms "
        "first. It chose, against every instinct three centuries had "
        "carved into it, to wait."
    )},
    {"type": "body", "text": (
        "Chibundu did not reach for violence the way the entity once "
        "had at this same field's edge. He reached instead for the "
        "quieter, harder lesson Chidebe's arrival had taught him weeks "
        "before, restraint as a choice rather than an absence, and let "
        "his will move through the ground like water finding its level "
        "rather than fire finding its fuel. Roots he had not consciously "
        "grown broke the surface in a ring around the advancing men, "
        "closing fast around ankles and wrists, binding rather than "
        "piercing, holding four of the five men fast in the space of a "
        "single indrawn breath."
    )},
    {"type": "body", "text": (
        "The fifth broke free of his own falling companions and kept "
        "coming, a short blade already turning in his hand, his eyes "
        "fixed past the boy entirely on the woman standing just behind "
        "him. Chibundu felt the man's intent a half instant before the "
        "blade cleared its arc, felt his own carefully held control "
        "buckle under a fear that had nothing measured in it at all, "
        "and understood, with a child's sudden clarity, that restraint "
        "would not be fast enough to save her."
    )},
    {"type": "body", "text": (
        "The entity closed the last distance itself, a single root "
        "driving up through the dark with a speed no ordinary plant "
        "had ever moved, and there was no more careful accounting in "
        "the act than there had been at this same boundary once before. "
        "The man fell and did not rise again. The entity felt no "
        "triumph in it, only a stark, uncomplicated relief that arrived "
        "and left in the same instant, replaced immediately by the "
        "colder question of what this second death, on this same "
        "ground, would cost all of them before the night was finished."
    )},
    {"type": "body", "text": (
        "Silence came down over the field so completely that Amara "
        "could hear her own blood moving in her ears. Four men lay "
        "bound and struggling in the roots' patient grip. One did not "
        "move at all. Chibundu stood between his mother and all of it, "
        "his small chest rising and falling hard, his hands still "
        "curled at his sides though the danger they had answered was "
        "already finished."
    )},
    {"type": "body", "text": (
        "\"I did not want to kill anyone,\" he said, and his voice, "
        "when it finally came, sounded very young again, all the "
        "trained steadiness of a moment before gone out of it at once. "
        "\"I only wanted them to stop.\""
    )},
    {"type": "body", "text": (
        "\"You did,\" Amara told him, pulling him back against her, "
        "feeling him shake now that there was nothing left requiring "
        "him to hold still. \"You made them stop without becoming what "
        "they were. Whatever else happened here tonight, that part was "
        "entirely yours, and it was the harder thing to choose.\""
    )},

    {"type": "body", "text": (
        "The entity held its ring of roots steady around the four bound "
        "men and let itself, for one unhurried moment, measure the "
        "distance between this night and the last time it had killed on "
        "this same stretch of ground. It had ended a life at this "
        "boundary once before without a second thought behind it, and "
        "told itself then that the accounting balanced simply enough: a "
        "threat removed, a mother and a boy kept safe. Watching Chibundu "
        "shake now with the effort of having chosen otherwise for four "
        "men out of five, it understood, slowly and without any comfort "
        "in the understanding, that the boy had just done something "
        "harder and more costly than killing, and had done it while "
        "afraid, which the entity itself had never once had to manage."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE CAPTURED MAN KNEW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Obi reached the field at a dead run, having heard, even from "
        "the distance he had promised to keep, a sound no father could "
        "mistake for anything ordinary. He found Amara upright and "
        "shaking and whole, Chibundu pressed against her side, and four "
        "strange men bound in living roots not ten strides away, and "
        "understood in a single sweeping look that he had come too late "
        "to help and, somehow, exactly in time to matter."
    )},
    {"type": "body", "text": (
        "Chidebe arrived moments after with three of his own soldiers, "
        "drawn from the tree line's edge by the same broken quiet Obi "
        "had heard, and stopped short at the sight of the bound men, "
        "his face working through recognition, alarm, and then a "
        "harder, private understanding all in the space of a few "
        "strides. Osadebe was a step behind him, breathing hard, taking "
        "in the whole field with the flat, practiced attention of a man "
        "already composing the report this would become."
    )},
    {"type": "body", "text": (
        "\"I pulled my own patrol back,\" Chidebe said quietly, to no "
        "one in particular, though Osadebe heard it plainly enough. "
        "\"For two hours. I told myself it was mercy owed to a mother "
        "and her son. I did not once ask myself what two hours of no "
        "watching eyes might look like to someone who had been counting "
        "the days until Idoro finally offered them one.\""
    )},
    {"type": "body", "text": (
        "One of the bound men, younger than the others and bleeding "
        "from a shallow cut along his temple, stirred enough to be "
        "questioned. Osadebe crouched beside him, his voice level, "
        "offering nothing that could be mistaken for either mercy or "
        "threat. \"Who sent you to this field tonight.\""
    )},
    {"type": "body", "text": (
        "The man's eyes moved past Osadebe to the roots still coiled "
        "fast around his own wrists, and something in what he had just "
        "watched happen to his companion seemed to loosen whatever "
        "loyalty might otherwise have held his tongue still. \"We were "
        "told the ground here would be open,\" he said, his words "
        "thick and unsteady. \"Not open in the ordinary way. Open for "
        "two hours, starting at the hour the soldiers pulled back their "
        "patrol. To the hour. We were told to the hour.\""
    )},
    {"type": "body", "text": (
        "Osadebe felt something cold settle into his chest that had "
        "nothing to do with the night air. \"A patient watcher might "
        "learn a patrol's habits given enough weeks at the tree line,\" "
        "he said carefully, more to himself than to the bound man in "
        "front of him. \"A patient watcher could not learn an "
        "arrangement made in a private conversation two days ago, "
        "between four people, in a room with no window facing this "
        "field.\""
    )},
    {"type": "body", "text": (
        "\"She did not learn it from watching,\" the man said, and for "
        "the first time something like fear crossed his face, fear not "
        "of the roots or the soldiers but of having already said more "
        "than his own House would forgive. \"She said it plainly, "
        "before we ever crossed into the trees tonight. Someone inside "
        "told her the hour. Someone who already had reason to be "
        "trusted with it.\""
    )},
    {"type": "body", "text": (
        "A soldier's hand closed over the man's shoulder before he "
        "could say anything further, Chidebe's own sharp motion cutting "
        "the questioning short with the instinct of an officer who "
        "understood, too late by exactly one sentence, that some "
        "answers were better gathered somewhere other than an open "
        "field still wet with a dead man's blood. But the sentence was "
        "already spoken, already sitting in the cold night air where "
        "five people standing in this field had all heard it land."
    )},
    {"type": "body", "text": (
        "Osadebe rose slowly and turned to look at the small circle "
        "gathered around him: Amara, Obi, Chidebe, and standing quiet "
        "between them all, a boy with a name only weeks old and a "
        "mother he had almost lost twice in one night. He ran the "
        "count in his own head the way he had run it a hundred times "
        "already without ever once suspecting it would matter this "
        "much: himself, Chidebe, Amara, Obi, Zara. Five people had known "
        "the hour. Five, and not one of them standing anywhere near "
        "this House's reach."
    )},
    {"type": "body", "text": (
        "\"Unless,\" he said aloud, the word arriving before he had "
        "fully let himself finish the thought behind it, \"one of the "
        "five was never as far from their reach as I assumed.\""
    )},
    {"type": "body", "text": (
        "The entity, still holding its ring of living roots fast around "
        "four bound men, felt the same cold arithmetic settle through "
        "Chibundu beside it, the boy's relief at having survived the "
        "night already curdling into something new and unwelcome: not "
        "fear of what waited beyond the tree line, which he had just "
        "proven he could meet, but fear of a danger with no shape at "
        "all, walking somewhere inside the one place he had just been "
        "promised was safe enough to call his mother's."
    )},
    {"type": "body", "text": (
        "Amara held her son a little tighter and looked around the "
        "quiet circle of faces that had just heard the same unfinished "
        "sentence she had, Obi's, Chidebe's, Osadebe's, none of them "
        "willing yet to say the word that sentence pointed toward. She "
        "had spent a year learning to carry secrets no one else in "
        "Idoro could be trusted with. She had never once imagined "
        "needing to wonder whether that same careful circle of trust "
        "was where the danger had been standing all along."
    )},

    {"type": "scene_break", "text": ""},
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
    print("  THE DARK RISE — Episode 51: \"The Choice at the Boundary\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_51.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_51.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
