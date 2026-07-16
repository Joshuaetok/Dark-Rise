#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 98: "What They Chose to Tell Him"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-13: Episode 98 resolves the crisis Ubani's crossing
created. Amara and Elder Maka decide, after weighing every worse
alternative, to give him a true but incomplete account: Oso as the
abandonment site of the old law, ground soaked in three centuries of a
specific, particular grief that does not distinguish between a
stranger's good intentions and a stranger's curiosity. Ubani, having
felt the ground's wrongness firsthand, accepts the explanation readily
because it matches his own experience closely enough to satisfy him
without demanding he understand every detail of it. He marks Oso
excluded from the crown's official survey as consecrated, protected
ground rather than land requiring further measurement, satisfying both
his professional honesty and the household's need for secrecy. In a
closing interlude, Mfoniso, recovered and newly resourced, scouts
Idoro's defenses from a careful distance for the first time since the
confrontation, finding a doubled garrison and a crown survey crawling
over ground she once moved through freely, and begins reworking her
plans around a village that has finally learned to expect her.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_98.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety Eight"},
    {"type": "title_ep_name", "text": "What They Chose to Tell Him"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: A TRUTH SMALL ENOUGH TO GIVE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Amara brought the question to Elder Maka the same evening, "
        "framing it as plainly as she could manage after a day that had "
        "left her with no honest strength left over for careful "
        "phrasing. \"He will write something,\" she said. \"He is not a "
        "man who leaves a page blank simply because the truth "
        "frightened him. Whatever he writes, we have some small say in "
        "the shape of it, if we are willing to give him enough to stop "
        "guessing at the rest.\""
    )},
    {"type": "body", "text": (
        "Elder Maka considered the problem the way she considered every "
        "old danger dressed in new clothing, turning it over for the "
        "shape of a solution that had served the household before. "
        "\"We cannot tell him what walks that ground,\" she said. \"But "
        "we do not need to. We have a truth old enough and heavy enough "
        "to satisfy a curious man without ever naming the thing "
        "beneath it.\""
    )},
    {"type": "body", "text": (
        "\"The old law,\" Amara said slowly, understanding forming as "
        "she spoke it aloud. Elder Maka nodded. \"Every abandoned child "
        "this village ever sent to that ground is a true grief, exactly "
        "as real as any grief he has ever measured for the crown. If we "
        "give him that truth, whole and unhidden, he will have every "
        "reason to believe it is the entire truth, because it very "
        "nearly is.\""
    )},
    {"type": "body", "text": (
        "Obi, listening from the edge of the fire, voiced the one "
        "hesitation neither woman had yet spoken aloud. \"And if he asks "
        "why grief alone can do what we saw it do to him this morning,\" "
        "he said. Elder Maka met that plainly. \"Then we tell him grief "
        "old enough does not always behave the way ordinary grief "
        "does,\" she said. \"That, too, happens to be true. It is simply "
        "not the whole of the truth. A partial truth offered honestly "
        "is not the same thing as a lie, and I will not treat it as one "
        "simply because it is convenient to call it that.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT UBANI WAS TOLD
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chidebe, brought into the plan before it was carried to Ubani, "
        "raised the same worry he had carried since the survey first "
        "arrived. \"He is observant enough to notice if the account "
        "feels shaped to fit a purpose,\" he said. Elder Maka did not "
        "dismiss the concern. \"Then we will not shape it,\" she said. "
        "\"We will simply tell him the truth we are willing to give, in "
        "the same plain words we would use with each other. A shaped "
        "truth invites suspicion. An honest one, even an incomplete "
        "one, rarely does.\""
    )},
    {"type": "body", "text": (
        "They found Ubani the next morning still pale but composed "
        "again, his notebook open on his knee with nothing yet written "
        "in it, and he received Elder Maka's presence with the same "
        "attentive respect he had shown Amara throughout the whole "
        "difficult week. \"I have been waiting for someone to explain "
        "what I do not have the right words for myself,\" he told her. "
        "\"I would rather hear it from someone who actually understands "
        "it than continue guessing badly on my own.\""
    )},
    {"type": "body", "text": (
        "Elder Maka told him the old law plainly, the abandonment of "
        "children marked as cursed, the iroko tree at the boundary "
        "where each one had been laid, the generations of grief the "
        "ground had absorbed long before any living person in Idoro had "
        "been born to inherit it. She did not soften it, and did not "
        "need to; the truth was heavy enough on its own that no "
        "embellishment could have made it heavier."
    )},
    {"type": "body", "text": (
        "\"Grief that old, carried by that many mothers across that "
        "many generations, does not simply fade the way a single "
        "sorrow fades,\" she told him. \"It settles into ground the way "
        "water settles into low places, until the ground itself carries "
        "the weight of it. What you felt this morning was three "
        "centuries of that weight, meeting a stranger who did not yet "
        "know to carry it gently.\""
    )},
    {"type": "body", "text": (
        "Ubani listened without interrupting, and when she finished, "
        "sat with it a long moment before speaking again. \"That "
        "matches what I felt more closely than anything else I could "
        "have imagined,\" he said. \"I did not feel hunted. I felt "
        "grieved at, somehow, though I could not have named it that "
        "way myself.\" Elder Maka held his gaze steadily. \"Then you "
        "felt it correctly,\" she said, which was, in its own careful "
        "way, entirely true."
    )},
    {"type": "body", "text": (
        "He asked a handful of careful questions after that, about the "
        "old law's history, about whether the practice still continued, "
        "about whether the crown bore any responsibility for a custom "
        "it had never formally outlawed, and Amara and Elder Maka "
        "answered each one honestly, within the boundary of what they "
        "had already decided to give him. No question led him back "
        "toward the entity itself. He did not think to ask a question "
        "shaped that way, because nothing in the true account he had "
        "been given pointed him toward it."
    )},
    {"type": "body", "text": (
        "Ude sat quietly through the whole exchange, saying nothing, "
        "understanding better than either woman that his own careful "
        "silence about Idoro's reputation over the preceding week had "
        "already prepared Ubani to accept this deeper truth without "
        "much resistance. A frightened man handed a story that matched "
        "his own fear rarely stops to ask whether the story is complete."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT THE MAP LEFT OUT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ubani wrote his report that same afternoon, and read the "
        "finished lines aloud to Chidebe before sealing them, the same "
        "habit of transparency he had carried through every stage of "
        "his week at Idoro. He had marked Oso not as unmeasured ground "
        "requiring further survey, but as consecrated grief ground, "
        "excluded from crown development by long standing local custom "
        "the crown had no cause and no right to disturb."
    )},
    {"type": "body", "text": (
        "\"It is the honest map I promised your village,\" he said. "
        "\"An honest map does not require measuring every hidden corner "
        "of a village's grief. It requires knowing which corners belong "
        "to grief at all, and marking them accordingly.\" Chidebe read "
        "the lines twice, searching for any detail that might still "
        "invite a second visit, and found none. The account protected "
        "exactly what needed protecting, without a single word that was "
        "not, in its own careful way, true."
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt the crisis pass the way a fever "
        "finally breaks, a long tension it had held since Ubani's "
        "crossing releasing all at once. \"They gave him a true grief "
        "instead of a false peace,\" it told Chibundu, something like "
        "admiration in its thin voice. \"I have watched this family "
        "solve danger with force, with patience, with sacrifice. I had "
        "not yet watched them solve one with nothing but careful "
        "honesty. It suits them better than I expected.\""
    )},
    {"type": "body", "text": (
        "The survey packed to leave within two days, its work "
        "genuinely finished now by its own leader's honest accounting, "
        "and Amara found herself, watching them go, grateful for an "
        "outcome she had not been at all certain the household could "
        "still reach by the time Ubani first crossed the tree line. "
        "\"We kept the secret,\" she told Elder Maka quietly, \"by "
        "giving away the truth we could afford to lose.\" Elder Maka "
        "nodded once. \"That is usually how the oldest secrets survive "
        "the longest,\" she said. \"Not by hiding behind nothing. By "
        "hiding behind something true enough that no one thinks to dig "
        "past it.\""
    )},
    {"type": "body", "text": (
        "Ubani sought Amara out once more before the survey's final "
        "departure, offering her a formal, careful thanks that carried, "
        "beneath its official language, something closer to genuine "
        "respect. \"I still do not know everything I felt on that "
        "ground,\" he said. \"I have decided I do not need to. Some "
        "truths belong to the people who have carried them, and a "
        "visitor's curiosity is not always owed the whole of them.\" "
        "Amara thanked him in return, meaning it more fully than she "
        "had expected to when the survey first arrived."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # INTERLUDE: WHAT MFONISO FOUND WAITING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A ridgeline west of Idoro, fully healed now and carrying "
        "resources the Warden's mandate had finally made available to "
        "her, Mfoniso studied the village through the same patient "
        "distance she had used to study it months before, and found "
        "almost nothing about it still matched her old, careful notes."
    )},
    {"type": "body", "text": (
        "Soldiers walked the boundary in numbers she had never once "
        "counted before her defeat, patrols staggered and unpredictable "
        "in a way that told her Chidebe had learned real lessons from "
        "the last season's failures. A crew of strangers with poles and "
        "rope worked the ground near the market, crown men by their "
        "bearing, adding official eyes to a place that had once relied "
        "entirely on a frightened family's own vigilance."
    )},
    {"type": "body", "text": (
        "She had expected some of this. She had not expected quite how "
        "thoroughly a single failed night had reshaped a village she "
        "had spent three seasons learning to move through unnoticed. "
        "\"They have finally learned to expect me,\" she said quietly, "
        "to no one, folding the observation into everything else she "
        "now had to plan around. \"Which means everything I built my "
        "patience on before no longer applies.\""
    )},
    {"type": "body", "text": (
        "She did not move closer that night, content for now to watch "
        "and catalogue, rebuilding her understanding of Idoro from the "
        "ground up the way she had once built it the first time, "
        "season by patient season. The resources the Warden had given "
        "her bought her choices she had never had before. They had not "
        "yet told her which of those choices this newly cautious "
        "village would leave open to her."
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
    print("  THE DARK RISE — Episode 98: \"What They Chose to Tell Him\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_98.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_98.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
