#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 81: "The Thread That Answered Back"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-26: Episode 81 opens on Zara's alarm from Episode 80's
final line. Elder Maka confirms it herself, barely, before it fades
past finding again. Rather than wait for a slow overland consultation,
Zara offers to be a conduit for the presence, using her existing blood
thread bond to let it examine what Mfoniso left on Adaugo directly,
despite the cost this arc has already established such reaching takes
from her. The presence identifies the working as an anchor rather than
a muffler, built to always know where Adaugo is rather than to blind
anyone watching over her, meaning Mfoniso no longer needs to stand
inside Idoro to know what the household is doing. The episode closes
mid reading, the working reacting to being examined, as if something
on the other end has just noticed it is being watched back.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_81.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty One"},
    {"type": "title_ep_name", "text": "The Thread That Answered Back"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: WHAT ELDER MAKA COULD BARELY CATCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka stopped walking so abruptly that Obi nearly ran "
        "into her from behind. She turned back to Zara and Adaugo, her "
        "own exhaustion forgotten, and did not waste breath asking "
        "whether Zara was certain. Everything the last two days had "
        "taught her said a claim like that, spoken in a voice that "
        "careful, was not the kind of thing a tired woman imagined."
    )},
    {"type": "body", "text": (
        "\"Show me where,\" she said, already crossing back to them. "
        "Zara guided her hand to the exact place on Adaugo's wrist, and "
        "Elder Maka closed her eyes the way she had not allowed herself "
        "to since the binding rite that first bound her to the entity, "
        "reaching past what her fingers could feel toward whatever lay "
        "beneath them."
    )},
    {"type": "body", "text": (
        "For a long moment she found nothing, and the old doubt crept "
        "in uninvited, the fear that grief and running and the day's "
        "terror had simply worn Zara's judgment thin. Then, right at "
        "the edge of losing her concentration entirely, she caught it. "
        "A thread of cold so faint it was barely a thread at all, "
        "there and gone again before she could close her hand around "
        "it, like trying to hold water that had already decided to be "
        "steam."
    )},
    {"type": "body", "text": (
        "Elder Maka opened her eyes slowly, and the look on her face "
        "told the others everything before she found the words for it. "
        "\"She is right,\" she said. \"Something was placed on you "
        "tonight, Adaugo, and it is already retreating from anyone who "
        "tries to look at it directly. By morning I do not believe "
        "either of us will be able to find it at all.\""
    )},
    {"type": "body", "text": (
        "Amara's hand went to her own throat. \"Then we do not have "
        "until morning,\" she said. \"Whatever this is, we look at it "
        "now, while it can still be looked at.\""
    )},
    {"type": "body", "text": (
        "Adaugo had gone very quiet, staring at her own wrist as though "
        "it belonged to someone else. \"I let her hold me,\" she said, "
        "so softly that Amara had to lean in to catch it. \"I stood "
        "there and let her, because I did not understand yet what she "
        "was.\" Elder Maka took her daughter's face in both hands again, "
        "firmer this time. \"You did not let her do anything,\" she "
        "said. \"She took the chance the moment gave her, the same way "
        "she took the words you never meant as a gift. That is on her "
        "hands, not yours.\" Adaugo nodded, but her eyes stayed fixed on "
        "the wrist a moment longer, as though she could will herself to "
        "feel whatever Zara had felt there and understand it for "
        "herself."
    )},
    {"type": "body", "text": (
        "Obi asked the question none of them had wanted to say aloud "
        "first. \"Do we cut it. The way you tried to cut Kene's.\" Elder "
        "Maka's silence answered before her words did. \"I was not "
        "confident in my own hands with Kene's thread, and that one "
        "was left by a power that loves this family,\" she said. \"I "
        "will not cut blind at something a hunter placed on purpose. A "
        "wrong cut could seal it in deeper than it already sits, or "
        "worse, tell her exactly when we found it.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT ZARA OFFERED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"There is another way,\" Zara said, and something in how "
        "quickly she said it told Amara she had already decided before "
        "anyone could argue her out of it. \"The presence has reached "
        "through me before, to speak, to warn, to carry Chibundu's name "
        "to this family when nothing else could. If I offer myself as "
        "the door again, it will not need days to reach Oso and back. "
        "It can look at what is on Adaugo tonight, through me, while "
        "there is still something left to see.\""
    )},
    {"type": "body", "text": (
        "Amara's first word was no. Her second was Zara's name, low "
        "and pleading, every week of gathering exhaustion rising behind "
        "her eyes at once. \"You are already worn to nothing,\" she "
        "said. \"We do not know what a working like this costs the one "
        "who carries it into you.\""
    )},
    {"type": "body", "text": (
        "\"I know exactly what it costs,\" Zara said, quieter now, not "
        "unkindly. \"I have been paying pieces of it for days already, "
        "whether I open the door or not. The difference tonight is "
        "that if I open it on purpose, something might finally come "
        "back through and tell us what we are fighting.\" She took "
        "Adaugo's hand in her own free one. \"She stood in that woman's "
        "grip for me. I can stand in this for her.\""
    )},
    {"type": "body", "text": (
        "Elder Maka looked at Amara for a long moment, then nodded once, "
        "slow and reluctant. \"We stay close,\" she said. \"If it "
        "becomes too much, we pull her back, whatever the presence "
        "still wants to see.\" Amara did not argue further. She had "
        "learned, across every crisis since the first one, that Zara's "
        "courage was not the kind that bent for being loved."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT OSO FELT LEAVE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, the entity felt the presence gather itself the way a "
        "man gathers his strength before lifting something he already "
        "suspects is too heavy for him. It said nothing to Chibundu at "
        "first, only watched, old caution warring with the newer "
        "habit of honesty the two of them had built between themselves "
        "since the household first learned to trust them both."
    )},
    {"type": "body", "text": (
        "\"It is reaching for the girl again,\" the entity said finally, "
        "unable to keep the worry fully out of its voice. \"Through "
        "Zara, the way it always has. But it has not fully recovered "
        "from what the boy cost it, and it means to spend more of "
        "itself tonight regardless.\" Chibundu asked whether it could "
        "be stopped. The entity was quiet for a moment before answering. "
        "\"I do not believe either of us has ever successfully told it "
        "no when a child of this family is the one in danger,\" it "
        "said. \"I am not certain we should try.\" Chibundu felt the "
        "truth of that settle over him uneasily, a fear for one power "
        "sitting right alongside his fear for two people he loved who "
        "were nowhere near Oso at all."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE THREAD THAT ANSWERED BACK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They settled in the swept dirt of Amara's compound by lamp "
        "light, Adaugo seated with her wrist held out, Zara kneeling "
        "beside her with both hands wrapped loosely around the same "
        "arm, a bridge built of nothing but old trust and older blood. "
        "Zara closed her eyes and let the muffled quiet inside herself "
        "fall away on purpose for the first time since it had first "
        "frightened her, opening the door instead of fighting to keep "
        "it shut."
    )},
    {"type": "body", "text": (
        "The presence's attention arrived the way it always did through "
        "her, cold and vast and careful with its own strength, moving "
        "through Zara toward Adaugo's wrist like water finding the "
        "lowest point in a room. Zara felt it settle, felt it study, "
        "and after a silence long enough to make Amara's hands curl "
        "into fists, Zara spoke again, though the voice underneath her "
        "own had gone strange and slow."
    )},
    {"type": "body", "text": (
        "\"It is not what was done to me,\" Zara said, the presence "
        "choosing her own remembered words to explain itself. \"Mine "
        "was built to blind the watcher. This was built to be found. "
        "An anchor, not a blindfold. Wherever this girl goes, whoever "
        "holds this thread will always know exactly where.\" A pause, "
        "the words slowing further, as though the presence were "
        "turning the shape of the working over one more time to be "
        "certain. \"She does not need to stand inside your walls "
        "anymore. She has already left something standing there for "
        "her.\""
    )},
    {"type": "body", "text": (
        "Elder Maka's breath left her all at once. Obi's hand went "
        "instinctively to Adaugo's shoulder, as though he could shield "
        "her from a thing already inside her skin. Amara said nothing "
        "at all, watching Zara's face for any sign of how much longer "
        "this could safely go on."
    )},
    {"type": "body", "text": (
        "\"Every patrol Chidebe moves,\" Elder Maka said slowly, "
        "working through the shape of it herself now. \"Every hour we "
        "choose to keep her close instead of sending her elsewhere. "
        "Every place we believe is safe because we chose it in secret.\" "
        "She looked at Adaugo with something close to grief. \"None of "
        "it has been secret since the moment that woman let go of your "
        "wrist.\" Zara's borrowed voice answered before anyone else "
        "could. \"Not everything,\" it said. \"Only where she stands. "
        "Not what is said near her, not yet. But a place is a "
        "beginning most hunters would consider more than enough.\""
    )},
    {"type": "body", "text": (
        "Then the thread moved."
    )},
    {"type": "body", "text": (
        "Zara's whole body went rigid, her hands tightening hard enough "
        "around Adaugo's wrist to leave marks of her own. \"It felt "
        "that,\" she said, and her own voice broke through the "
        "presence's borrowed calm for just a moment, raw with a fear "
        "that belonged entirely to her. \"Elder Maka, it felt us "
        "looking. It is answering back.\" Her back arched as though "
        "something had reached through the open door from the far side "
        "of it, and the lamp beside them guttered low without a breath "
        "of wind in the compound to explain why."
    )},
    {"type": "body", "text": (
        "Elder Maka lunged forward and seized Zara by both shoulders, "
        "shouting her name once, sharp enough to carry over whatever "
        "was happening behind Zara's closed eyes. Amara was already "
        "moving too, reaching for Adaugo's arm to break the bridge "
        "between them, some instinct older than any of her council "
        "training screaming that whatever had just noticed them looking "
        "was no longer content to simply be found."
    )},
    {"type": "body", "text": (
        "Zara's mouth opened, and for one terrible moment no sound came "
        "out of it at all, her whole frame shaking under the weight of "
        "something none of them could see and only one of them could "
        "feel."
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
    print("  THE DARK RISE — Episode 81: \"The Thread That Answered Back\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_81.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_81.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
