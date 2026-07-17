#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 84: "The Path No One Watched"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-29: Episode 84 turns Episode 83's rough trace (west and
slightly south) into concrete patrol coverage. Chidebe and Osadebe
organize unpredictable rotating routes across several days, but reports
trickle back describing near misses that always fall exactly where a
patrol was not standing, even after routes were deliberately changed
without notice. Osadebe begins cross referencing the misses against who
knew which schedule, and finds a pattern too precise for luck. In Oso,
Chibundu and the entity feel the household's fear beginning to turn
inward on itself for the first time, a division no direct attack has
managed to cause. The episode closes on Osadebe naming the fear
plainly in front of Chidebe and Amara — someone is telling Mfoniso
where they are not — while a brief interlude confirms from Mfoniso's
own side that the advantage is real, without yet revealing its source.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_84.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Four"},
    {"type": "title_ep_name", "text": "The Path No One Watched"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE PATROLS THEY SET
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe unrolled a strip of scraped hide across the council "
        "fire's flat stone and weighted its corners with pebbles, the "
        "closest thing Idoro had ever needed to a map of its own land. "
        "\"West and slightly south,\" he said, tracing the direction "
        "Elder Maka's reading had given them. \"That is everything we "
        "know. It is also more than we have ever known before.\""
    )},
    {"type": "body", "text": (
        "Osadebe leaned over the hide beside him, marking crossings and "
        "tree lines with a burned stick. \"We cannot simply stand every "
        "soldier we have along one line and wait,\" he said. \"She "
        "studies how trained men think. Give her a pattern and she will "
        "read it before we have finished setting it.\" He looked up at "
        "Chidebe. \"Routes that change. Timing that changes with them. "
        "No two days alike.\""
    )},
    {"type": "body", "text": (
        "Amara watched the two soldiers argue over the map with the "
        "particular patience of a mother who had learned, across many "
        "councils, that letting men finish their planning aloud saved "
        "time later. \"How many days before you can cover the whole "
        "approach,\" she asked. Chidebe did not look up from the hide. "
        "\"Three, if every man I have gives up sleeping. Longer, if I "
        "want them sharp enough to notice anything at all.\""
    )},
    {"type": "body", "text": (
        "Inside the hut, Elder Maka checked Adaugo's wrist again out of "
        "habit rather than expectation, finding the same patient cold "
        "waiting exactly where it had waited since the reading. \"It "
        "will not warn us again,\" she told Adaugo gently. \"Not soon. "
        "Whatever we learned from it, we learned already. Now it is "
        "only a thread we chose to leave open, and a thing we must live "
        "beside.\" Adaugo nodded, though her hand still drifted to the "
        "spot without her noticing."
    )},
    {"type": "body", "text": (
        "Kene found his mother at the edge of the yard while the "
        "argument over routes continued behind them, tugging her sleeve "
        "until she crouched to his level. \"Will the soldiers find the "
        "bad woman today,\" he asked, in the plain voice of a child who "
        "had learned to ask hard questions simply because no one had "
        "yet taught him to be afraid of the answers. Amara held his "
        "hand and told him the truth as gently as she knew how to tell "
        "it. \"Not today, most likely,\" she said. \"But every day they "
        "look, she has to work harder to stay hidden. That matters, "
        "even on the days it does not look like it.\""
    )},
    {"type": "body", "text": (
        "She watched his hand as she said it, the way she had watched "
        "it every day since the unbidden spiral in the dirt, and found "
        "nothing new there, only an ordinary boy's fingers curled "
        "around her own. It was, these days, the closest thing to relief "
        "she allowed herself before turning back to the map and the "
        "war it was quietly beginning to plan."
    )},
    {"type": "body", "text": (
        "By midmorning the patrols went out changed, staggered, unequal "
        "in number and hour, exactly as Osadebe had insisted. He walked "
        "the first route himself rather than send a soldier who had "
        "never seen Mfoniso's face, and Chidebe took the second, "
        "leaving only a skeleton watch on the compound wall for the "
        "first time since the third bend. It felt, Amara admitted to "
        "Obi as they watched the soldiers go, like taking a breath they "
        "had been holding since the night the presence tore itself free "
        "of Zara."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT THE PATROLS FOUND, AND DID NOT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The first day returned nothing, which Osadebe called good news "
        "and Chidebe called too soon to trust. The second day returned "
        "less than nothing: a soldier posted along the southern tree "
        "line reported a patch of grass bent the wrong direction, as "
        "though someone had passed through only hours before his watch "
        "began, in the one stretch of ground his route had not yet "
        "reached that morning."
    )},
    {"type": "body", "text": (
        "Osadebe walked the spot himself and said little, but the line "
        "of his shoulders on the way back told Chidebe more than any "
        "report would have. By the third day it had happened twice "
        "more, always the same shape, always ground that had been "
        "covered the day before and moved off the route that same "
        "morning, as though whoever left the signs knew exactly which "
        "hours belonged to open ground before the patrol itself did."
    )},
    {"type": "body", "text": (
        "That evening Osadebe sat alone with the hide map and worked "
        "backward through every route change of the last three days, "
        "matching each one against the small circle of people who had "
        "heard it spoken. The circle never grew larger than six or "
        "seven names, and it never failed to include at least one "
        "person present at all three. He stared at that overlap for a "
        "long time before he trusted himself to bring it to anyone "
        "else."
    )},
    {"type": "body", "text": (
        "\"Three times is not luck,\" Osadebe said finally, standing "
        "over Chidebe's hide map with the burned stick gone still in his "
        "hand. \"Luck misses you or it finds you. It does not know your "
        "schedule before you have finished deciding it.\" Chidebe did "
        "not argue. He simply looked at the map, at the handful of marks "
        "showing where his own routes had shifted that same morning, and "
        "said nothing for a long moment."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the shift in the household before anyone "
        "told him what had caused it, a new and unfamiliar note beneath "
        "the ordinary fear he had grown used to sensing from them. "
        "\"They are not only afraid of her anymore,\" he said to the "
        "entity. \"They are starting to be afraid of each other.\" The "
        "entity considered that with the slow gravity it gave to things "
        "it had seen before, in other households, other centuries. "
        "\"That is a wound Mfoniso does not need to strike herself,\" it "
        "said. \"A house that begins doubting its own hands has already "
        "done half her work for her.\""
    )},
    {"type": "body", "text": (
        "Chibundu turned that over uneasily. \"You believe there is "
        "someone,\" he said. \"Not simply skill, or bad luck stacked "
        "three times over.\" The entity did not answer quickly, and when "
        "it did, its caution was its own kind of answer. \"I believe a "
        "hunter this patient would rather buy one pair of eyes inside a "
        "house than out think an entire garrison from outside it. I "
        "cannot tell you who. I can tell you it would not surprise me.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE PATTERN THAT COULD NOT BE LUCK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "On the fourth morning Chidebe made a change to the noon route "
        "inside a closed meeting of exactly four people, himself, "
        "Osadebe, Amara, and the soldier who would walk it, spoken "
        "aloud only once and written nowhere. That same route was the "
        "one where a soldier found fresh signs of passage before the "
        "sun had fully cleared the tree line, hours before the change "
        "had even taken effect."
    )},
    {"type": "body", "text": (
        "Osadebe stood over the marks for a long time before he walked "
        "back to the compound, and when he did, he did not go to "
        "Chidebe first. He went to Amara, finding her at the fire with "
        "Obi, and set the fact down between them as plainly as a man "
        "sets down a weapon he no longer wants to be holding. \"Four "
        "people knew where that route would stand today,\" he said. "
        "\"Four. And she was already gone from that ground before the "
        "route existed.\""
    )},
    {"type": "body", "text": (
        "Amara went very still, the way she had learned to go still "
        "when a danger arrived too large to answer with the first "
        "feeling it produced. \"You are saying one of the four,\" she "
        "said, not quite a question, and Osadebe did not soften it into "
        "one either. \"I am saying someone is telling her where we are "
        "not,\" he said. \"I do not know who. I do not want it to be any "
        "of us. But I have chased this woman twice now and lost her "
        "twice, and I am done calling the third time luck.\""
    )},
    {"type": "body", "text": (
        "Elder Maka arrived from the hut in time to catch the shape of "
        "it rather than the whole, and she did not rush to comfort "
        "anyone the way she might once have. \"I have seen a house eat "
        "itself from suspicion before it was ever touched by the thing "
        "it feared,\" she said quietly. \"I will not pretend that cannot "
        "happen here. But I will also not let us name a face before we "
        "have found one honestly. Suspicion without proof is its own "
        "kind of poison, and it works exactly as slowly as the thing "
        "Mfoniso left on Zara.\""
    )},
    {"type": "body", "text": (
        "Chidebe arrived in time to hear the last of it, and whatever "
        "argument he might once have made against the idea did not come. "
        "He looked instead at his own hands, at the map he had drawn "
        "that morning with such care, and understood before anyone "
        "explained it further that trust, once a house begins counting "
        "who else might have known a thing, does not return simply "
        "because the counting stops. Obi said nothing at all, watching "
        "the fire, already turning over every face in Idoro he had once "
        "been certain of."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT MFONISO CARRIED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Two ridgelines west of Idoro, Mfoniso read a folded scrap of "
        "bark cloth by firelight, the ink on it small and careful, and "
        "burned it the moment she had committed its contents to memory, "
        "as she burned every message that reached her this way. It told "
        "her nothing she found surprising. It told her exactly where the "
        "morning's soldiers would not be standing, and it had reached "
        "her before those soldiers themselves had finished deciding it."
    )},
    {"type": "body", "text": (
        "She did not know the messenger's face, only the drop point "
        "outside the market where word waited for her twice a week, "
        "faithful as a tide, and she had learned long ago not to ask a "
        "useful thing too many questions about where it came from. "
        "Patience had taught her that curiosity was a luxury a hunter "
        "paid for eventually, always at the worst possible hour."
    )},
    {"type": "body", "text": (
        "What she allowed herself, walking east into the dark with the "
        "ash of the message still warm between her fingers, was a "
        "single thought she did not examine too closely. Somewhere "
        "inside that careful, guarded, grieving household, someone "
        "wanted her to succeed badly enough to risk everything for it, "
        "and had wanted it for longer than the family itself had any "
        "reason yet to suspect."
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
    print("  THE DARK RISE — Episode 84: \"The Path No One Watched\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_84.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_84.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
