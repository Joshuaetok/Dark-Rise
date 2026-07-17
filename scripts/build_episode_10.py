#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 10: "The Verdict"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-17: Episode 10 resolves Episode 9's cliffhanger. Amara answers
Elder Maka's public demand about Kene's eyes, choosing a careful half truth: she
admits what she saw but argues Kene is a victim used as a weapon, not a returned,
wrongful child, and that the old law was never written for a case like his. In
Oso, the entity registers the village's fracturing argument as a second useful
distraction, dividing attention it might otherwise spend hunting its doors.
Elder Maka publicly accepts a compromise, a watch kept over Kene rather than an
immediate judgment, but privately resolves that the first further sign of the
entity acting through him will end the debate for good, on her own terms.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_10.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ten"},
    {"type": "title_ep_name", "text": "The Verdict"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT AMARA CHOSE TO SAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara had spent two days rehearsing lies for exactly this "
        "moment, and standing in her own compound with Elder Maka's "
        "question hanging in the air and half of Idoro pretending not to "
        "listen, she found that none of them would come to her mouth."
    )},
    {"type": "body", "text": (
        "\"His eyes turned dark,\" she said instead. \"For one instant, "
        "during the cleansing rite, while the dibia was breaking free of "
        "whatever holds him. Dark, and shining like oil on water. Then "
        "they were his own eyes again, and he cried the way any startled "
        "child cries, and I have watched him every day since and seen "
        "nothing else.\""
    )},
    {"type": "body", "text": (
        "A ripple moved through the neighbors who had stopped to watch, "
        "a held breath finally let go, and Elder Maka's face did not "
        "soften at all."
    )},
    {"type": "body", "text": (
        "\"You saw this,\" Elder Maka said, \"the same night, and told "
        "no one.\""
    )},
    {"type": "body", "text": (
        "\"I told no one because I understood exactly what would happen "
        "the moment I did,\" Amara said, and for the first time since "
        "the confrontation began, steel came into her voice instead of "
        "fear. \"You would look at my son and see the boy you buried "
        "thirty and four years ago. You would not see the difference "
        "between them. I see it every hour of every day, because it is "
        "the only thing standing between Kene and a grave.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Obi stepped forward beside his wife, close enough that his "
        "shoulder touched hers, and Amara felt the small, deliberate "
        "weight of it, a man choosing where to stand in front of "
        "witnesses. \"She has told you the truth,\" he said. \"I was "
        "there the night it happened. I held my own son while he "
        "screamed, and there was nothing in his face afterward but a "
        "frightened child who wanted his mother. Whatever you saw for "
        "that one instant was not Kene reaching for the forest. It was "
        "the forest reaching for him.\""
    )},
    {"type": "body", "text": (
        "\"Tell me the difference, then,\" Elder Maka said, unmoved by "
        "either of them, her eyes still fixed on Amara. \"Tell me "
        "plainly, in front of everyone listening, why a child who wears "
        "the same darkness in his eyes deserves a gentler law than my "
        "son did.\""
    )},
    {"type": "body", "text": (
        "\"Because your son went into Oso and came back changed,\" "
        "Amara said. \"He crossed over and something else walked home in "
        "his shape. Kene has never left this compound. Whatever reached "
        "him reached across a distance, the way it reached through the "
        "dibia to speak to me, the way it walked Zara toward the tree "
        "line in her sleep. It used my son as a weapon against a rite "
        "meant to stop it. That does not make him the thing you buried. "
        "It makes him something it is willing to hurt to protect itself. "
        "There is a difference between a knife a man swings and a knife "
        "picked up off the ground and thrown. You do not put the ground "
        "on trial.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The silence that followed had a different texture than the one "
        "before it, and Amara understood she had landed the argument "
        "somewhere it could not simply be waved away, because she had "
        "watched Elder Maka's own history often enough now to know "
        "exactly which nerve it would find."
    )},
    {"type": "body", "text": (
        "Elder Maka's returned son had chosen. Had hunted. Had killed "
        "with hands that understood exactly what they were doing. "
        "Kene had only screamed and gone still, an instrument played "
        "once by a hand that was not his own."
    )},
    {"type": "body", "text": (
        "\"Instruments can still be dangerous,\" Elder Maka said at "
        "last, quieter now, more to herself than to Amara. \"A knife "
        "thrown once can be thrown again.\""
    )},
    {"type": "body", "text": (
        "\"Then watch the hand that throws it,\" Amara said. \"Not the "
        "knife. Watch Oso. I am not asking you to trust me, Elder Maka. "
        "I am asking you to be more precise about what you are "
        "afraid of.\""
    )},
    {"type": "body", "text": (
        "One of the watching neighbors, an older man who had said "
        "nothing until now, cleared his throat and spoke into the "
        "silence, his voice unsteady with the particular courage of a "
        "man who has decided a thing must be said even though it will "
        "not be welcome. \"Elder, with respect. If we start killing "
        "children for what a spirit does through them and not for what "
        "they choose to do themselves, none of our children are safe "
        "from any of this. My daughter cried without reason for a full "
        "week after the rite. Do we watch her next.\""
    )},
    {"type": "body", "text": (
        "The murmur that followed told Amara the argument had already "
        "traveled further than the ring of neighbors standing in her "
        "own compound. Whatever happened here today, Idoro would not "
        "hear it as one woman's private grief any longer. It would hear "
        "it as a question the whole village now had to answer about "
        "itself."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY HEARD IN THE ARGUING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity followed the shape of the "
        "argument the way it followed everything that reached it out of "
        "Idoro now, as a texture of fear and anger it could taste "
        "without needing to understand every word carried inside it."
    )},
    {"type": "body", "text": (
        "It understood enough. The mother was arguing for the child's "
        "life using the very act the entity had committed against him "
        "as proof of his innocence. There was an economy to that the "
        "entity almost admired, the way a good trap sometimes becomes "
        "the very thing that springs it loose again."
    )},
    {"type": "body", "text": (
        "It did not concern itself with whether the argument succeeded. "
        "Whether the old woman spared the twin bond or severed it, the "
        "village would spend days now consumed with debating one "
        "thread while the entity's attention rested, patient and "
        "untroubled, on threads no one in Idoro had thought to argue "
        "about at all."
    )},
    {"type": "body", "text": (
        "A village divided against itself over how afraid to be of one "
        "child was a village that had stopped watching everywhere else. "
        "The entity had learned this lesson twice now, once with the "
        "dibia and once with the sleeping midwife, and a lesson learned "
        "twice was a rule it intended to keep leaning on for as long as "
        "human fear kept obliging it."
    )},
    {"type": "body", "text": (
        "It considered, briefly, whether to reach for the twin thread "
        "again now, while the argument over its last use still burned "
        "hot enough to make a second strike look like confirmation "
        "rather than coincidence. The old woman would call it proof. "
        "The mother would call it a trap. Both of them would be "
        "watching, and watched things could not be spent twice for the "
        "same coin. The entity let the thought pass unacted on, the way "
        "it let most thoughts pass now that it had learned how much "
        "more a village would hand it if only it was patient enough to "
        "wait for the offering instead of taking it by force."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the vessel pulled itself upright against a root "
        "without help for the first time, stood swaying a moment on legs "
        "no longer new to the effort, and reached one small hand toward "
        "the dark above it as though grasping for something only it "
        "could see. The entity let the reaching continue a long moment "
        "before drawing the small hand gently back down. Not yet. Soon, "
        "but not yet."
    )},

    {"type": "scene_break", "text": ""},

    # System alert block — sentence case for clean TTS; the caps run
    # property renders it all caps on the page.
    {"type": "body", "text": (
        "In Oso, the ledger voice spoke its tally."
    )},
    {"type": "system", "text": "Village attention fractured across two visible threads. Undetected threads: stable. Vessel: standing unassisted, reaching behavior observed."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE VERDICT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka took longer to answer than Amara expected, long "
        "enough that the gathered neighbors began to shift where they "
        "stood, uncertain whether they were watching a mercy or a "
        "sentence come together."
    )},
    {"type": "body", "text": (
        "\"I will not take the child from you today,\" she said finally. "
        "\"Your argument has enough truth in it that I cannot in good "
        "conscience act as though it does not. But I will not pretend a "
        "danger has become no danger simply because a clever woman found "
        "the right words for it. Two of my own people will watch this "
        "compound, quietly, from tomorrow onward. Not to punish you. To "
        "see what I am afraid you already know and will not say, which "
        "is whether this happens again.\""
    )},
    {"type": "body", "text": (
        "Amara inclined her head, giving the smallest concession the "
        "moment required, though something in her chest had gone tight "
        "and watchful at the word watch. \"If it happens again, you will "
        "see it as clearly as I did. I have no reason to hide what I "
        "cannot control.\""
    )},
    {"type": "body", "text": (
        "\"See that you remember you said that,\" Elder Maka said, and "
        "turned to go, the small crowd of neighbors parting for her the "
        "way water parts for a boat that has already decided its "
        "course."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She did not look back until she had nearly reached her own "
        "compound, and when she did, alone now, with no one left to "
        "hear the words she did not intend to speak aloud, her face "
        "settled into an expression far colder than anything she had "
        "shown Amara."
    )},
    {"type": "body", "text": (
        "She had meant every word of the mercy she had just granted. She "
        "also meant, with the same unhurried certainty that had carried "
        "her through burying her own son, that a "
        "watch was only ever the first half of a plan. If Kene's eyes "
        "darkened even once more under any roof in Idoro, she would not "
        "call another council, would not wait for another argument "
        "clever enough to stay her hand a second time. She had done this "
        "once already. She knew exactly how quickly it needed to be done "
        "the next time, and exactly how little warning she intended to "
        "give the mother she had just, for a single afternoon, allowed "
        "to win."
    )},
    {"type": "body", "text": (
        "The old man's question stayed with her longer than she wanted "
        "it to. Do we watch her next. She had no answer for him that "
        "would not sound, even to her own ear, like the beginning of "
        "something Idoro had never needed before and might not survive "
        "learning how to live with now. A village that watched its own "
        "children for signs of a darkness none of them had asked for "
        "was a village already changed, whatever verdict she handed "
        "down today or any day after it."
    )},
    {"type": "body", "text": (
        "She let herself feel that cost, once, alone, where no one "
        "could see it cross her face. Then she put it away, the same "
        "way she had put away every cost since the dawn she killed her "
        "own returned son with her own hands, and walked on."
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
    print("  THE DARK RISE — Episode 10: \"The Verdict\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_10.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_10.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
