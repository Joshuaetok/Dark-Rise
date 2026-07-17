#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 30: "The Warning"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-06: Episode 30 closes the ten episode block that began
with Ozoemena's rise. Amara and Obi walk Osadebe to the edge of Oso at
dawn, and the entity, now aware that a representative of the crown
itself is standing at its boundary, makes a deliberate choice: rather
than remain hidden or strike as it once struck at Idoro, it reveals
itself just enough to be unmistakable, speaking directly to all three of
them without borrowing a single mouth to do it, a demonstration of reach
it has never risked showing an outsider before. Its message is short,
almost identical to the first words it ever spoke through the dibia
back in Episode 2, but aimed now, for the first time, past the village
entirely and toward the throne that sent a man to measure it. The
episode, and this block, ends with Osadebe riding back toward Udo
carrying something far heavier than a report, and Amara understanding
that whatever quiet window of time she believed she still had left has
just been closed by the one voice with the power to close it.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_30.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty"},
    {"type": "title_ep_name", "text": "The Warning"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — THE WALK AT FIRST LIGHT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Obi insisted on coming, and Amara did not argue with him the "
        "way she might once have, understanding, without needing it "
        "explained, that he had earned the right to stand at that "
        "boundary as much as she had."
    )},
    {"type": "body", "text": (
        "The three of them walked the bush path in the gray hour before "
        "sunrise, Osadebe silent and watchful beside them, his two "
        "remaining men left behind at the edge of the village on his own "
        "instruction, a decision Amara noted with something like "
        "respect. A careful man did not bring more witnesses than the "
        "moment required."
    )},
    {"type": "body", "text": (
        "\"You have walked this path before,\" Osadebe said, somewhere "
        "past the last of the cassava fields."
    )},
    {"type": "body", "text": (
        "\"Never this far,\" Amara said. \"I have stood at the edge of "
        "my own courage more times than I can count since my son was "
        "carried down this path. I have never once found the nerve to "
        "walk past it.\""
    )},
    {"type": "body", "text": (
        "Obi walked slightly ahead of both of them, his own steps "
        "slower and more deliberate than usual, and Amara understood, "
        "watching him, that he was measuring this walk against every "
        "night he had once imagined making it alone, back before she "
        "had talked him out of exactly this kind of reckless approach "
        "in the earliest days of their grief. There was a strange "
        "symmetry in finally walking it together, invited this time, "
        "escorted by a stranger with the whole weight of a distant "
        "throne standing somewhere behind him."
    )},
    {"type": "body", "text": (
        "\"I dreamed of this path for a long while,\" Obi said quietly, "
        "not quite to either of them. \"In the dreams I always reached "
        "the tree line. I never once dreamed what waited past it.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The tree line came into view as the sky began to pale, the "
        "iroko saplings standing in their strange, deliberate ring "
        "exactly as Zara had once described them, and beyond the "
        "saplings, the older growth, dark even in the strengthening "
        "light, close and patient in a way no ordinary forest had ever "
        "felt to Amara."
    )},
    {"type": "body", "text": (
        "Osadebe stopped a full body length before the boundary itself, "
        "the trained stillness of a man taking the measure of ground he "
        "did not yet trust, and said nothing for a long moment, simply "
        "looking."
    )},
    {"type": "body", "text": (
        "The birds had gone quiet somewhere behind them, Amara "
        "realized, in the last stretch of the path, the ordinary "
        "morning chorus of the fields fading into a stillness that felt "
        "deliberate rather than simply early, as though the whole of "
        "Oso had drawn a slow breath and was holding it, waiting to see "
        "what these three visitors intended to do with the last few "
        "steps left between them and the tree line."
    )},
    {"type": "body", "text": (
        "\"You feel it too,\" Osadebe said, and it was not a question. "
        "\"I have stood at the edge of battlefields that did not feel "
        "this attentive.\""
    )},
    {"type": "body", "text": (
        "\"I feel it every time I let myself come close enough,\" Amara "
        "said. \"It has never once felt like an accident.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY DECIDED TO SHOW
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had felt the three of them "
        "coming since they first left the village behind, and had spent "
        "the whole of their approach weighing, with the same "
        "unhurried care it gave every decision that might cost it "
        "something, exactly how much of itself this particular morning "
        "was worth revealing."
    )},
    {"type": "body", "text": (
        "A stranger this careful, sent by a throne this distant, was "
        "not a threat to be struck down the way it had struck down a "
        "reckless villager's overreach. Striking at a king's own "
        "captain risked inviting exactly the kind of attention its "
        "three centuries of patience had always been built to avoid. "
        "But allowing him to leave with nothing more than a frightened "
        "village's secondhand story, easily dismissed by a court that "
        "had never needed to believe in anything beyond its own ledgers, "
        "would waste an opportunity the entity had not expected to be "
        "offered so soon."
    )},
    {"type": "body", "text": (
        "It decided, in the last few careful steps before the three of "
        "them reached the boundary, to be believed rather than merely "
        "suspected. A message understood clearly by a frightened "
        "captain would travel further, and land harder, than any "
        "rumor his own uncertain report could ever carry on its own."
    )},
    {"type": "body", "text": (
        "There was a colder calculation folded inside the simpler one, "
        "one it did not trouble itself to soften even to its own "
        "reasoning. A distant throne convinced of a genuine, patient "
        "danger would move carefully, would send careful men to ask "
        "careful questions rather than armies to burn a forest it did "
        "not understand. Fear handled correctly did not always need to "
        "provoke violence. Sometimes the more useful fear was the kind "
        "that convinced a powerful hand to keep its distance rather "
        "than the kind that provoked it into striking blindly. The "
        "entity had already spent one door's worth of exposure teaching "
        "Idoro that lesson. It saw no reason not to spend a second, "
        "larger lesson teaching the same thing to the throne behind it."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "It did not reach for a mouth to borrow. There was no one "
        "standing at that boundary it needed to wear like a glove to "
        "be heard. It simply let its voice arrive, directly, into all "
        "three of them at once, the same low, wordless register it had "
        "used with the vessel since his first day of hearing anything "
        "at all, given shape and volume enough, for the first time, to "
        "be received by minds it had never touched before."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In Oso, the cold voice recorded the first sending."
    )},
    {"type": "system", "text": "Direct unmediated contact: authorized, three simultaneous recipients. First use of this capability outside the vessel bond."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE BOUNDARY — WHAT ALL THREE OF THEM HEARD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The words arrived without a sound to carry them, the way a "
        "held breath arrives in a suddenly still room, and all three of "
        "them stopped at once, Osadebe's hand dropping instinctively "
        "toward a blade he must have known, even as he reached for it, "
        "would do nothing against what he was actually facing."
    )},
    {"type": "body", "text": (
        "I know why you have come, the voice said, addressed to no "
        "single one of them and to all three at once. Tell your king "
        "I have not forgotten the word I first sent into his kingdom. I "
        "am still coming. I have simply learned, since I first said so, "
        "how much better the coming goes when it is not rushed."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Then it was gone, as completely and suddenly as it had "
        "arrived, the ordinary birdsong of the waking forest rushing "
        "back in to fill the silence it left behind, and the three of "
        "them stood at the edge of the tree line for a long moment, "
        "none of them quite trusting their own legs to carry them "
        "either forward or back."
    )},
    {"type": "body", "text": (
        "\"That,\" Osadebe said finally, his voice not quite steady, "
        "\"is not a story I will need to embellish for anyone at Udo to "
        "believe it.\""
    )},
    {"type": "body", "text": (
        "He turned to look at Amara, something new in his expression "
        "that had not been there the evening before, a soldier's "
        "practical calm reasserting itself even now, already "
        "reorganizing what he had just witnessed into the shape a "
        "report would need to carry it faithfully. \"You have lived "
        "beside this for months,\" he said. \"I do not know whether to "
        "call that courage or simply the absence of any other choice.\""
    )},
    {"type": "body", "text": (
        "\"Both, most days,\" Amara said. \"I stopped trying to "
        "separate them a long time ago.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "He turned to leave within the hour, riding north with his two "
        "remaining men and a report that would need no exaggeration to "
        "earn a king's full attention, and Amara watched him go with the "
        "same tightening in her chest she had carried since the message "
        "first left for Udo weeks earlier, now finally given its true "
        "shape."
    )},
    {"type": "body", "text": (
        "Before he mounted, he turned back once more. \"Whatever comes "
        "of my report,\" he said, \"I do not believe the crown will "
        "forget this village again the way it forgot it for so long "
        "before. That may be a mercy, in time. I am not yet certain it "
        "will feel like one to you before it does.\""
    )},
    {"type": "body", "text": (
        "Amara had no answer ready for that, and let him go without "
        "one, watching the small party shrink along the river road "
        "until the bend in the path finally swallowed them from view."
    )},
    {"type": "body", "text": (
        "Whatever quiet window she had believed herself still standing "
        "inside, some private stretch of time in which she alone "
        "carried the full weight of her son's existence, had just been "
        "closed by a voice that had chosen, after three hundred years "
        "of patient silence toward every throne that had ever risen and "
        "fallen along this river, to finally speak to one of them "
        "directly."
    )},
    {"type": "body", "text": (
        "It had not done so by accident. Amara understood that much "
        "with a certainty that settled cold and permanent beneath "
        "everything else she felt standing at that boundary. Whatever "
        "was growing beneath the iroko roots had just decided, for "
        "reasons only it fully understood, that the time for staying "
        "unseen by the wider world had finally come to an end."
    )},
    {"type": "body", "text": (
        "She thought of her son, somewhere behind that tree line, "
        "growing into whatever shape three centuries of patience and a "
        "few short months of careful shaping had decided to make of "
        "him, and understood that whatever came next, for Idoro, for "
        "Udo, for a throne that had only just learned her village's "
        "name, would no longer be decided in secret, in the quiet, "
        "private margins where she had fought every one of her battles "
        "so far. The margins had just closed. Whatever came next would "
        "happen in the open, in front of a kingdom finally watching, "
        "whether any of them were ready for that or not."
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
    print("  THE DARK RISE — Episode 30: \"The Warning\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_30.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_30.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
