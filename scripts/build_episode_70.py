#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 70: "What the Night Almost Took"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-15: Episode 70 closes the ten episode block that began
with Episode 61's reckoning at the boundary. Mfoniso's wrapped charm
does not need her standing over Kene at all; it reaches for him the
way the entity once reached for Zara in Episode 8, drawing him out of
his own bed and past a distracted watch on legs that are moving
without his waking consent. Zara wakes from the compulsion's edge
before anyone else does, certain in a way she cannot explain, and
screams the household into motion. Obi gives chase on foot. But it is
the presence that reaches Kene first, extending itself beyond Oso's
ground for the first time in this whole story to break the charm's
hold directly, at a cost it does not hide from Chibundu afterward.
Mfoniso, seeing exactly what she came to learn, retreats rather than
fight a power now fully awake to her, and the block ends with a
family intact, a debt owed to a power that once failed to act in time
for someone else, and a hunter walking away with everything she
needed to plan a second attempt.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_70.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Seventy"},
    {"type": "title_ep_name", "text": "What the Night Almost Took"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: LEGS THAT WERE NOT HIS OWN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The household had gone to sleep exhausted rather than "
        "reassured, the day's alarm settling into the particular "
        "tiredness of people who had spent every waking hour since "
        "the market bracing for a danger that had not yet shown its "
        "shape. Amara had checked on Kene twice before finally letting "
        "herself lie down, and Obi had walked the compound's edge "
        "himself once more after the last patrol passed, unwilling to "
        "trust even Chidebe's doubled watch completely with the one "
        "thing that mattered most."
    )},
    {"type": "body", "text": (
        "Kene woke a little past midnight without ever fully waking "
        "at all, his small legs finding the floor and carrying him "
        "toward the compound's edge with a purpose no three year old "
        "walks with on his own, his open eyes seeing nothing of the "
        "dark hut around him and everything of a single small wrapped "
        "object waiting patient and unhurried somewhere past the "
        "stream."
    )},
    {"type": "body", "text": (
        "The soldier posted nearest the hut had turned, for perhaps "
        "the length of ten breaths, toward a sound in the far tree "
        "line that did not repeat itself, exactly long enough. Kene "
        "passed within three strides of him, silent and sure footed in "
        "a way no sleepwalking child should have been, and neither the "
        "soldier's eyes nor his own tired vigilance caught the small "
        "shape moving past him in the dark."
    )},
    {"type": "body", "text": (
        "Zara woke gasping in Amara's own compound at nearly the same "
        "moment, certain of a wrongness she could not immediately "
        "place, her whole body remembering, before her mind fully "
        "caught up to it, the exact cold weight of the thing that had "
        "twice already brushed against her in passing. This time it "
        "was not passing. This time it was working, patient and "
        "total, on someone else entirely."
    )},
    {"type": "body", "text": (
        "\"Kene,\" she said aloud, the name arriving before she "
        "understood why, and was already moving, already screaming for "
        "Obi and Amara both, by the time the rest of the thought "
        "caught up to her voice."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: A POWER THAT HAD NEVER REACHED THIS FAR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Obi found the empty bed before Zara's second scream finished "
        "leaving her throat, and was running before he had fully "
        "understood what his own eyes were telling him, barefoot "
        "through the dark toward the stream with a father's blind, "
        "total certainty of direction even though nothing yet told him "
        "which way to run. He passed the soldier still frozen in "
        "belated horror near the hut and did not stop to explain, did "
        "not stop for anything, his own breath tearing at his chest "
        "the way it had once torn at it running toward a different "
        "kind of danger years before."
    )},
    {"type": "body", "text": (
        "In Oso, the presence felt the charm's working reach across "
        "the distance the instant it fully closed around the boy, a "
        "texture it recognized immediately and completely, having "
        "carried the memory of an identical working for longer than "
        "this entire kingdom had existed in its current shape. It did "
        "not hesitate the way it once had. It did not weigh the cost "
        "first and act second, the way its own grief had taught it "
        "across three centuries of watching from adjacent ground and "
        "calling the watching caution."
    )},
    {"type": "system", "text": (
        "PRESENCE EXTENDING BEYOND CLAIMED GROUND. RANGE UNPRECEDENTED. "
        "COST UNKNOWN. INTERVENTION PROCEEDING REGARDLESS."
    )},
    {"type": "body", "text": (
        "Mfoniso felt her own working falter at the exact moment she "
        "expected it to complete, the boy's small hand already close "
        "enough to reach, and looked up to find the ordinary dark "
        "beside the stream no longer entirely ordinary at all, roots "
        "she had not planted breaking the earth in a wide, patient "
        "circle around herself and the child both, moving with none "
        "of the entity's known temper and all of an older, colder "
        "authority she recognized at once from a lifetime of hunting "
        "things exactly like it."
    )},
    {"type": "body", "text": (
        "You are further from your own ground than any account of you "
        "ever suggested you could reach, she said, not quite a "
        "question, already calculating the new shape of everything she "
        "thought she had known walking in."
    )},
    {"type": "body", "text": (
        "I have never reached this far before tonight, the presence "
        "told her, and there was no boast folded into the admission, "
        "only plain fact offered the way it now offered most things. I "
        "did not know I could, until the alternative was watching this "
        "happen to someone I have already failed to protect once "
        "before, in a place too far away for either of us to undo. I "
        "do not intend to let the distance matter more than the boy "
        "does tonight."
    )},
    {"type": "body", "text": (
        "Kene stirred, blinking, his own eyes finally opening on "
        "something other than the charm's borrowed direction, and "
        "began, in the confused, frightened way of any small child "
        "waking somewhere he does not remember walking to, to cry. The "
        "sound seemed to cost Mfoniso something she had not accounted "
        "for either, a flicker crossing her carefully composed face "
        "too quickly to name."
    )},
    {"type": "body", "text": (
        "\"You came a long way to stand in the dark and be surprised,\" "
        "the presence said, and there was no cruelty in the "
        "observation, only the plain, unhurried weight it now brought "
        "to most things. \"I would have thought a House patient enough "
        "to retain you for thirty years would have prepared you for "
        "the possibility that its own old accounts might simply be "
        "incomplete.\""
    )},
    {"type": "body", "text": (
        "\"Every account I have ever trusted described a guardian's "
        "reach ending at its own claimed ground,\" Mfoniso said, and "
        "there was no panic in her voice either, only the same "
        "careful recalculation she had brought to the market's "
        "sudden vigilance hours before. \"You have just proven that "
        "account wrong in front of me personally. I do not discard "
        "thirty years of method lightly. I also do not repeat a "
        "mistake once I have watched it fail this plainly.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT SHE CARRIED AWAY
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso did not fight the roots closing around her own "
        "working. She had built her whole long life around knowing "
        "precisely when a position had already been lost, and this one "
        "had been lost the moment a guardian proved willing to reach "
        "further than every account she had ever trusted said it "
        "could. \"You have taught me something useful tonight,\" she "
        "said, stepping back from the child without being made to, "
        "\"whether either of us wanted the lesson given.\""
    )},
    {"type": "body", "text": (
        "\"Then take the lesson and go,\" the presence said, \"and know "
        "that whatever ground I could not reach before tonight, I have "
        "reached it now, and I do not intend to forget the shape of "
        "having done it.\" Mfoniso studied the roots, the crying child, "
        "the empty dark where an old power had just proven itself "
        "considerably less contained than she had crossed a continent "
        "believing, and withdrew into the tree line without another "
        "word, unhurried even in retreat."
    )},
    {"type": "body", "text": (
        "Obi reached the stream moments later to find his son crying "
        "but whole, held gently within a loose ring of roots already "
        "beginning to withdraw back into the earth, and scooped Kene "
        "up with a sound that was not quite a sob and not quite a "
        "prayer, holding him the way he had once imagined holding a "
        "different son at a different boundary, years of fear finally "
        "breaking loose all at once."
    )},
    {"type": "body", "text": (
        "Amara arrived seconds behind him, Zara close behind her, and "
        "the small circle that gathered at the stream's edge held each "
        "other in the particular silence of people who understood, "
        "without needing to say it aloud, exactly how much closer this "
        "night had come to ending differently than the ordinary "
        "morning that would somehow still follow it."
    )},
    {"type": "body", "text": (
        "Amara looked at the last of the withdrawing roots, and spoke "
        "aloud to a power she could not see and had once promised, in "
        "anger, would answer to her. \"Thank you,\" she said simply, "
        "the anger of that earlier vow entirely absent now, replaced "
        "by something rawer and more grateful than she had expected to "
        "ever feel toward the thing that had once taken her son's own "
        "voice from him. \"Whatever this cost you, I will not forget "
        "that you paid it for him.\""
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the presence's exhaustion arrive all at "
        "once, a weariness unlike anything it had shown him before, "
        "and asked the only question that mattered. \"What did that "
        "cost you.\""
    )},
    {"type": "body", "text": (
        "More than I have spent on anything in longer than you could "
        "measure, the presence admitted. I do not yet know if I have "
        "fully paid it. I know only that I would spend the same again, "
        "without hesitating a second time, and that is a difference in "
        "myself I did not expect this season to teach me."
    )},
    {"type": "body", "text": (
        "Chibundu sat with that, and with the boy's saved, ordinary "
        "life, and understood, turning the whole long night over, that "
        "whatever the hunter had learned crossing back into Oso's dark "
        "beyond the tree line, Idoro had learned something too: that "
        "the powers guarding this ground would reach as far as they "
        "had to, at whatever cost was asked of them, rather than let "
        "the mistake that once cost a stranger everything happen twice "
        "under their own watch."
    )},
    {"type": "body", "text": (
        "By morning, word of the night had reached every corner of "
        "the village Chidebe's men could walk in an hour, Elder Maka "
        "arriving at Amara's compound before the sun had fully cleared "
        "the tree line, Ozoemena close behind her, both of them "
        "absorbing the account with the particular stillness of people "
        "measuring how much closer disaster had come than any of them "
        "had let themselves believe possible. No one suggested, even "
        "once, that the danger had passed for good. Everyone understood, "
        "without needing it said aloud, that a hunter who retreats "
        "unhurried and unharmed is a hunter who fully intends to return."
    )},
    {"type": "body", "text": (
        "Kene, held close in Amara's arms through most of that morning, "
        "remembered nothing of the night at all beyond a strange, "
        "half formed dream of cold water and a stranger's face, and "
        "asked, when he finally noticed how tightly everyone kept "
        "holding him, whether he had done something wrong. \"No,\" "
        "Amara told him, fierce and certain, pressing a kiss to the "
        "top of his head. \"You did nothing wrong at all. You were "
        "loved fiercely enough tonight that an old, tired power crossed "
        "further than it has ever crossed before, just to make sure of "
        "it.\" Whatever answer waited for that love in the days still "
        "to come, it would have to be faced daylight by daylight, the "
        "same patient way this family had learned to face everything "
        "else."
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
    print("  THE DARK RISE — Episode 70: \"What the Night Almost Took\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_70.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_70.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
