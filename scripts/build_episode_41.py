#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 41: "The Cost of Being Seen"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-17: Episode 41 handles the immediate aftermath of Episode
40's violence. Idoro's relationship to Amara's household shifts again,
this time into something more ambivalent than the old fear: the entity
just protected the whole village, but it did so by proving, beyond any
remaining doubt, exactly how dangerous it is. Osadebe writes the most
urgent report of his posting and sends it north before dawn, aware it
will change how Udo treats Idoro permanently. In Oso, the entity and the
vessel sit with what happened between them — the boy's guilt at having
hurt grown men mixed with a child's confusion about a power he does not
understand and cannot take back. The entity, forced by everything that
has changed to stop treating the naming question as something it can
keep deferring, tells him plainly that a name is coming, soon, though
not yet whose. The episode closes on the entity sensing, for the first
time since the parlay, that the presence beyond Oso's borders is watching
far more closely now that the boy has shown what he can do.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_41.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty One"},
    {"type": "title_ep_name", "text": "The Cost of Being Seen"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — GRATITUDE THAT LOOKS LIKE FEAR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The market was quieter than Amara had ever heard it the "
        "morning after, not the frozen silence of a village that had "
        "decided to shun her, but something stranger, a careful, "
        "watchful courtesy that would not quite meet her eyes. A "
        "woman selling yams pressed an extra one into her basket "
        "without being asked and would not take payment for it. A "
        "man who had once let his fish rot rather than trade with Obi "
        "nodded to him now from across the square, a small, "
        "unpracticed gesture that looked almost like respect and "
        "almost like fear wearing respect's clothes. Children who "
        "would once have been called inside at the sight of her now "
        "watched her pass with open, unguarded curiosity, as though "
        "she had become, overnight, someone worth studying rather than "
        "someone worth avoiding."
    )},
    {"type": "body", "text": (
        "\"They know it saved them,\" Obi said quietly, watching the "
        "same exchange. \"And they know it could just as easily have "
        "been them lying in that field instead of those strangers. I "
        "do not think Idoro has decided yet whether to build a shrine "
        "to what happened or dig a wider trench around our compound. "
        "I am not certain the village itself knows which one it is "
        "doing.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "Osadebe spent the morning writing the most careful letter of "
        "his entire posting, aware that every word he chose would "
        "shape whatever Udo decided to do next, and that for the "
        "first time since his arrival, he had no honest way to soften "
        "what he had witnessed. Six armed men struck down by something "
        "that grew out of the earth itself. A foreign House's agent "
        "carried away wounded, already halfway to becoming a story "
        "that would travel faster and further than any trader's tale "
        "ever had. He wrote it plainly, the way Amara had taught him "
        "truth traveled best in this particular village, and sealed "
        "it before he could talk himself into rounding any of its "
        "edges off."
    )},
    {"type": "body", "text": (
        "\"They will not send soldiers after reading this,\" he told "
        "Amara, handing the sealed letter to the rider waiting at "
        "first light. \"Not yet. But they will stop treating Idoro as "
        "a village to be watched from a careful distance. Whatever "
        "comes back down this road next will come faster, and it will "
        "come with more men behind it than I arrived with.\""
    )},
    {"type": "body", "text": (
        "Amara watched the rider disappear up the river road and "
        "found herself thinking, not for the first time, that every "
        "single choice made to protect her sons from one danger "
        "seemed only to summon a larger one behind it, the way pulling "
        "a single weed only revealed the deeper root beneath it, "
        "still growing, still reaching for the same soil."
    )},
    {"type": "body", "text": (
        "She found Elder Maka waiting at her own compound gate that "
        "afternoon, unannounced for the first time since the boundary "
        "walk, and braced herself out of old habit for a judgment that "
        "did not come. \"I watched those roots take those men down "
        "last night the way I once watched my own son take his father "
        "down,\" Elder Maka said, without preamble, her voice steady "
        "in a way Amara had not heard from her in a long while. \"The "
        "difference undid me more than the likeness did. My son killed "
        "out of something broken in him. Whatever moved through Oso "
        "last night killed, or nearly killed, to protect a village "
        "that has never once thanked it for anything. I do not know "
        "what to call a danger that behaves like that. I am no longer "
        "certain the old law ever had a word for it.\""
    )},
    {"type": "body", "text": (
        "It was, Amara understood, the closest thing to an apology "
        "Elder Maka had ever offered her, folded inside an observation "
        "rather than spoken plainly, and she found she no longer "
        "needed it spoken plainly to accept it. \"Maybe it never "
        "needed a word,\" she said. \"Maybe it only ever needed "
        "someone willing to keep watching long enough to see which "
        "shape it actually took.\" The two women stood together a "
        "while longer at the gate, saying nothing further, two mothers "
        "who had each buried a piece of themselves in the same old "
        "law, finding something almost like peace in simply standing "
        "in the same silence for once instead of opposite sides of it."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT HE CANNOT TAKE BACK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the boy had not touched his stones "
        "since the roots fell still, sitting instead with his knees "
        "drawn up and his hands hidden beneath them, as though hiding "
        "them from sight might undo what they had done the night "
        "before."
    )},
    {"type": "body", "text": (
        "\"I hurt them,\" he said, the first words he had offered "
        "since the entity settled beside him. \"I did not know I could "
        "do that. I did not ask to be able to do that.\" He was not "
        "crying, but his voice carried the particular flatness of a "
        "child working very hard not to, and the entity, which had "
        "shaped nearly every other feeling he had ever learned to "
        "name, found this one entirely his own to carry."
    )},
    {"type": "body", "text": (
        "A mile away, unaware any of it had happened, Kene had spent "
        "that same night asleep in his own bed, warm and ordinary and "
        "untouched by anything that moved beneath the iroko roots, "
        "and the entity, holding both boys in its attention for one "
        "brief unguarded moment, felt the full weight of everything "
        "that had once been true of both of them and was now true of "
        "only one. It did not know which twin carried the heavier "
        "inheritance. It was no longer certain the question had a "
        "single right answer."
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "\"They came to hurt your mother's village,\" the entity said. "
        "\"You stopped them. That is not the same as wanting to hurt "
        "anyone.\" It heard, even as it said this, how much the "
        "sentence resembled every careful justification it had once "
        "offered itself for the dibia, for Zara, for every thread it "
        "had ever spent without asking permission first, and did not "
        "know whether that resemblance should comfort it or trouble it "
        "further."
    )},
    {"type": "body", "text": (
        "\"Does it get easier,\" the boy asked, \"knowing you hurt "
        "someone and still believing you were right to.\""
    )},
    {"type": "body", "text": (
        "The entity considered lying to him, briefly, the way it had "
        "once considered lying about almost everything, and found the "
        "old habit no longer fit as comfortably as it once had. \"No,\" "
        "it told him. \"It only gets quieter. That is not the same "
        "thing as easier, whatever it looks like from the outside.\""
    )},
    {"type": "scene_break", "text": ""},
    {"type": "body", "text": (
        "They sat with that a long while, the boy slowly uncurling his "
        "hands from beneath his knees, turning them over in the dim "
        "light as though checking they still belonged to him, testing "
        "each finger the way he once tested the weight and shape of a "
        "new stone before deciding where it belonged in his careful "
        "arrangements. \"Will you tell me my name now,\" he asked "
        "eventually, not a demand, simply a question laid down beside "
        "all the others that night had already asked of him. \"I do "
        "not think I am only a small thing being kept safe anymore. I "
        "do not know what to call someone who is not that.\""
    )},
    {"type": "body", "text": (
        "\"Soon,\" the entity said, and meant it more fully than it "
        "had meant the same word any time before tonight. \"I am not "
        "delaying it to protect myself from the decision anymore. I am "
        "delaying it because I want it to be right, and I have not yet "
        "decided what right looks like for a boy who can do what you "
        "did tonight without being taught.\""
    )},
    {"type": "body", "text": (
        "Beneath the roots, the cold voice recorded its own promise."
    )},
    {"type": "system", "text": "Vessel: second unprompted request for identity. Entity commitment issued: name forthcoming, timeline unspecified."},
    {"type": "body", "text": (
        "He accepted this the way he accepted every unfinished answer "
        "the entity had ever given him, filing it away rather than "
        "pressing further, and fell asleep sooner than the entity "
        "expected, worn through by a night his small body had not yet "
        "learned how to carry."
    )},
    {"type": "body", "text": (
        "The entity kept watch over him longer than usual, turning "
        "its attention outward toward the borders it had crossed only "
        "twice before, and found, waiting there in the same "
        "patient stillness it had first met during the parlay, a "
        "presence that felt closer than it had ever felt before, "
        "watching without reaching, the way something might watch a "
        "student it had not taught pass a test it had not set."
    )},
    {"type": "body", "text": (
        "It did not try to speak this time, and the entity did not "
        "invite it to. There was, it understood, a particular kind of "
        "danger in mistaking silence for absence, a mistake it had "
        "made once already about this same ground and had no wish to "
        "repeat now that the cost of being wrong had grown a face and "
        "a set of small, capable hands. It settled instead for simply "
        "noting the shift, the way a careful animal notes a change in "
        "wind direction long before it can name the storm the wind is "
        "carrying."
    )},
    {"type": "body", "text": (
        "For the first time since the boy's will had moved through its "
        "own strike the night before, the entity understood that the "
        "presence beyond its borders had not merely felt that moment "
        "happen. It had been waiting for it, the way a patient buyer "
        "waits through a long negotiation for the one moment that "
        "finally proves the goods are worth what he already believed "
        "them to be, and the entity found itself, for the first time "
        "in three careful centuries, genuinely uncertain which of them "
        "the coming days were actually going to test."
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
    print("  THE DARK RISE — Episode 41: \"The Cost of Being Seen\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_41.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_41.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
