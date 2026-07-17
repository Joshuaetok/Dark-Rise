#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 83: "A Second Thread"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-28: Episode 83 opens on the exhausted, heavily guarded
morning after Episode 82. Elder Maka lays out a choice for the whole
household rather than deciding alone: sever Adaugo's anchor thread now
and lose their only lead on Mfoniso, or leave it open and use it,
carefully and in daylight, to trace her back. The family chooses to
trace. Elder Maka performs the reading herself, sparing Zara further
cost, with the entity and the weakened presence lending careful
support from Oso. The reading finds distance and direction, then
something no one expected: a second, thinner thread running from
Mfoniso herself toward someone or something behind her, meaning she is
not acting entirely alone or entirely by her own will. Mfoniso feels
the trace find her and severs it before Elder Maka can see who holds
the other end, then pushes west toward Idoro faster than she has
allowed herself to move all along.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_83.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Three"},
    {"type": "title_ep_name", "text": "A Second Thread"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: WHAT DAWN FOUND STILL STANDING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Dawn came up gray over the compound wall and found it still "
        "standing, still guarded, still awake. Chidebe's soldiers had "
        "not left their posts since midnight. The fire at the center of "
        "the yard had burned to a low bed of coals no one had bothered "
        "to feed. Osadebe stood at the gate exactly where Amara had last "
        "seen him, jaw tight, eyes tracking every shadow the growing "
        "light peeled back from the tree line."
    )},
    {"type": "body", "text": (
        "Zara woke first among the family, propped against the wall of "
        "Elder Maka's hut where sleep had finally taken her sometime "
        "near the third hour, still wrapped in Adaugo's borrowed shawl. "
        "She sat up slowly, testing her own body the way a woman tests a "
        "bridge she does not trust, and found herself tired in the "
        "ordinary way rather than hollowed out the way the night had "
        "left her. It was, she decided, the closest thing to good news "
        "the household had earned in days."
    )},
    {"type": "body", "text": (
        "Adaugo had not slept at all, curled between her mother and "
        "Elder Maka exactly as promised, one hand pressed over the "
        "other wrist through every hour of the night. When Elder Maka "
        "finally examined it again in daylight, gentle fingers tracing "
        "skin where nothing visible marked her, she found the same faint "
        "cold Zara had first described, patient and unhurried, waiting."
    )},
    {"type": "body", "text": (
        "\"It has not changed,\" Elder Maka said, more to herself than "
        "to the room. \"Not stronger. Not weaker. Exactly as it was "
        "before we tried to look at it.\" She sat back on her heels, "
        "weighing something she had clearly begun weighing long before "
        "she spoke a single word aloud. \"Which tells me it was never "
        "meant to hurt you, child. Only to be there. Watching is a "
        "patient cruelty. It costs the one doing it almost nothing at "
        "all.\""
    )},
    {"type": "body", "text": (
        "Amara entered with Obi a step behind her, both of them "
        "carrying the particular stillness of people who had not slept "
        "and had stopped pretending they might. \"Chidebe wants a "
        "decision before the market opens,\" Amara said. \"So does "
        "Osadebe, though he is too polite this morning to say so "
        "twice.\" She looked at Adaugo's wrist, then at Elder Maka's "
        "face, already reading the answer forming there before it was "
        "spoken."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE CHOICE ELDER MAKA WOULD NOT MAKE ALONE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka gathered them properly then, calling Chidebe and "
        "Osadebe in from the gate long enough to hear the choice laid "
        "out plainly, the way council business had always been done in "
        "Idoro even when the council itself was reduced to whoever could "
        "be found awake in one yard. \"There are two paths in front of "
        "us,\" she said, \"and I will not choose either one without "
        "every person this danger touches standing here to hear why.\""
    )},
    {"type": "body", "text": (
        "\"The first path is the one my hands know,\" she continued. "
        "\"We sever the thread. It will hurt her, the way any cutting "
        "hurts, and I cannot promise my hands still remember this "
        "particular working well enough to do it cleanly. But when it "
        "is done, whatever Mfoniso built into Adaugo's wrist stops "
        "answering. She loses her window into this house.\" She let that "
        "sit before adding the cost. \"And so do we. Once cut, we will "
        "not know where she stands again until she is close enough to "
        "see with our own eyes.\""
    )},
    {"type": "body", "text": (
        "\"The second path,\" she said, \"is the one I only understood "
        "at first light, thinking back on stories my grandmother told "
        "me of houses that learned to use what a hunter left behind "
        "rather than only removing it. A thread built to answer has to "
        "answer both ways, if the hand reaching along it is patient and "
        "steady enough to listen rather than pull. We do not sever it. "
        "We use it. Carefully, once, to learn where she stands, instead "
        "of only fearing that she does.\""
    )},
    {"type": "body", "text": (
        "Obi was the first to speak into the silence that followed. "
        "\"You are asking us to leave our daughter marked,\" he said, "
        "\"so that we can go looking for the person who marked her.\" It "
        "was not an accusation. It was, Zara thought, watching him, the "
        "sound of a father saying the true shape of a terrible choice "
        "aloud so that no one in the room could pretend it was smaller "
        "than it was."
    )},
    {"type": "body", "text": (
        "\"I am asking exactly that,\" Elder Maka said, without "
        "softening it. \"I will not pretend the risk is small. Every "
        "hour that thread stays open, Mfoniso knows exactly where "
        "Adaugo sleeps, walks, and sits. But if we cut it blind tonight, "
        "we return to exactly where we stood a season ago, waiting for "
        "her to choose the next child, learning her plans only after "
        "they have already succeeded.\" She looked at Amara last. \"You "
        "broke this thread once already, out of a mother's instinct, "
        "and I do not fault you for it. I am asking whether this house "
        "can bear to choose with its head instead, just once.\""
    )},
    {"type": "body", "text": (
        "Amara's answer took longer than anyone expected. She crossed "
        "to Adaugo, crouched in front of her, and asked the only "
        "question that mattered before any council could decide it for "
        "her. \"Do you understand what she is asking,\" Amara said "
        "gently, \"and are you willing to carry it a little longer, "
        "knowing what it might cost you.\" Adaugo did not answer quickly "
        "either, but when she did, her voice held steadier than it had "
        "at any point since the third bend. \"I have already carried it "
        "since yesterday without knowing,\" she said. \"I would rather "
        "carry it on purpose, if it means she cannot use it to surprise "
        "us again.\""
    )},
    {"type": "body", "text": (
        "Osadebe pushed off the gatepost he had been leaning against. "
        "\"Then let me say the soldier's half of this,\" he said. \"A "
        "hunter who moves fast makes mistakes a patient one never "
        "would. She told herself last night she cannot wait any longer. "
        "If we are ever going to catch her reaching for something before "
        "she is ready, it is now, while she is still deciding how much "
        "haste she can afford.\" Chidebe, beside him, said nothing, but "
        "the set of his jaw agreed for him."
    )},
    {"type": "body", "text": (
        "Elder Maka turned last to Zara, who had said nothing through "
        "the entire exchange, and asked the question everyone else had "
        "been too careful to ask aloud. \"This will not be you,\" she "
        "said. \"Not this time. Your gift is muffled, and even if it "
        "were not, I would not spend what little of you is left on "
        "this. I will carry it myself.\" Zara's relief was plain enough "
        "that no one in the yard pretended not to see it, and no one "
        "blamed her for feeling it."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE READING FOUND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They did it at midmorning, in daylight, surrounded by every "
        "soldier Chidebe could spare, nothing at all like the desperate "
        "half accident of the night before. Elder Maka knelt across "
        "from Adaugo in the center of the yard, one hand resting lightly "
        "over the girl's wrist rather than gripping it, and closed her "
        "eyes to find the old rhythm her grandmother had taught her "
        "before Amara or Obi had been born."
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the entity go taut beside him the "
        "instant Elder Maka's own thin thread opened toward it, asking, "
        "without words, for whatever strength the entity could safely "
        "lend a working this old and this careful. \"She is doing it in "
        "daylight, with witnesses, slowly,\" the entity said, something "
        "like approval in its voice. \"That is more wisdom than the "
        "night allowed anyone last time.\""
    )},
    {"type": "body", "text": (
        "The presence stirred too, weaker than it had been in days but "
        "present, watching through Chibundu's borrowed awareness rather "
        "than reaching out itself this time. \"Tell them to go "
        "carefully,\" it said. \"A thread held open on purpose behaves "
        "differently than one caught by surprise. It will not fight "
        "being seen. It will simply show them exactly as much as it "
        "wants them to know, and nothing more.\""
    )},
    {"type": "body", "text": (
        "Elder Maka's breath slowed. The yard around her seemed to fall "
        "away from her awareness one sound at a time, the soldiers, the "
        "fire, Amara's held breath, until only the thread remained, a "
        "thin cold line running out from Adaugo's wrist toward "
        "something distant and patient. She followed it the way her "
        "grandmother had once taught her to follow a scent in the dark, "
        "one careful step behind the smell rather than chasing it "
        "outright."
    )},
    {"type": "body", "text": (
        "Distance came first, vague but real, further than the third "
        "bend, further than any point Osadebe's patrols had ever dared "
        "search. Direction came second, west and slightly south, toward "
        "country none of them knew well. Then, faint beneath both, "
        "something Elder Maka had not expected to find at all. A second "
        "thread, thinner than the first, running not toward Adaugo but "
        "away from Mfoniso herself, out toward some third point Elder "
        "Maka's borrowed sense could not yet reach."
    )},
    {"type": "body", "text": (
        "She said it aloud without opening her eyes, so the whole yard "
        "heard it in the same instant she understood it herself. \"She "
        "is not alone in this the way we believed,\" Elder Maka said, "
        "her voice tight with the effort of holding the reading steady. "
        "\"Something is watching her the same way she is watching "
        "Adaugo. She carries a thread of her own, and I do not think "
        "she put it there herself.\""
    )},
    {"type": "body", "text": (
        "The words had barely left her before the cold line running "
        "through her fingers convulsed, not violently the way Zara's "
        "had, but sharply, deliberately, like a hand closing around a "
        "wrist to stop it moving further. Elder Maka's eyes snapped "
        "open, breath coming hard, the reading gone as suddenly as it "
        "had opened. \"She felt it,\" she said. \"She felt me finding "
        "her, and she pulled back before I could see who is holding the "
        "other end.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT MFONISO FELT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A day and a half west of the third bend, Mfoniso went still in "
        "the middle of tying off her pack, feeling the anchor at "
        "Adaugo's wrist stir under a touch that was not the girl's own. "
        "It moved carefully, patiently, nothing like the raw tearing she "
        "had felt two nights before. This time something was listening "
        "rather than lashing out, and that frightened her far more than "
        "the guardian's single desperate reach ever had."
    )},
    {"type": "body", "text": (
        "She severed her own attention from the thread before whatever "
        "reached for her could finish the shape of its question, an old "
        "reflex trained into her hands before she had been old enough "
        "to understand why it mattered. Her teacher's warning came back "
        "to her again, sharper this time. A guardian old enough to "
        "remember being hunted does not simply defend itself. It "
        "learns."
    )},
    {"type": "body", "text": (
        "What unsettled her more, sitting alone with her pack half "
        "closed, was the plain fact that whoever had been listening had "
        "found something on her own end of the thread that Mfoniso "
        "herself had spent years trying not to think about too closely, "
        "the second, older tie she carried to the one who had trained "
        "her, and to whoever had trained that teacher before. She had "
        "always assumed it was hers alone to know about. She no longer "
        "believed that."
    )},
    {"type": "body", "text": (
        "Mfoniso finished closing her pack with hands that did not "
        "shake, because they never did, and rose to walk west toward "
        "Idoro faster than she had allowed herself to move in weeks. "
        "Patience had cost her the element of surprise this morning. It "
        "would not also cost her the last true advantage she still held "
        "over a household that was only now learning to look back."
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
    print("  THE DARK RISE — Episode 83: \"A Second Thread\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_83.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_83.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
