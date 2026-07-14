#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 88: "What the Traitor Traded"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-03: Episode 88 gives Emenike's full account under a
formal council hearing rather than an accusatory interrogation. His
sister, Ijeoma, was taken from a river town two seasons ago by Ijoma
Concern agents who then contacted him directly, demanding patrol
information in exchange for her continued safety and periodic proof of
life. When Elder Maka has him describe the direction the proof-of-life
messages seem to travel from, the entity, listening through Chibundu,
realizes it roughly matches the unknown third point Elder Maka's
Episode 83 trace found running off Mfoniso's own second thread —
suggesting Ijeoma may be held at or near wherever Mfoniso herself
answers to. The household, torn between justice and mercy, does not
resolve what happens to Emenike, but does learn from him that Mfoniso
expects her next message at the stone within two nights, and that
missing a scheduled contact has never happened before in two seasons of
compliance. The episode closes on that deadline hanging over the
household, forcing a decision they are not ready to make.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_88.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eighty Eight"},
    {"type": "title_ep_name", "text": "What the Traitor Traded"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE ACCOUNT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They gave Emenike a proper hearing the next morning rather "
        "than a hurried accusation in the dark, the whole council "
        "gathered around the fire as though this were any other matter "
        "requiring Idoro's judgment. Elder Maka insisted on it plainly. "
        "\"Whatever we decide,\" she said, \"we decide it having heard "
        "the whole account, not merely the part that broke him last "
        "night.\""
    )},
    {"type": "body", "text": (
        "Emenike told it slowly, in the flat, careful voice of a man "
        "who had rehearsed never saying it aloud. His sister, Ijeoma, "
        "had gone to a river town two seasons ago to trade cloth for "
        "their aging mother and never returned. He had searched for "
        "half a season before three strangers found him instead, in the "
        "night, at his own door, and told him plainly that she was "
        "alive, and would remain so only as long as he answered every "
        "question they sent him."
    )},
    {"type": "body", "text": (
        "\"They did not ask for much, at first,\" he said. \"Small "
        "things. Who stood watch, and when. I told myself it could not "
        "matter, that a garrison's schedule was not worth a life.\" His "
        "hands, folded tightly in his lap, had not stopped shaking since "
        "he began. \"By the time I understood what they were truly "
        "building toward, I no longer had a way to stop giving it to "
        "them without losing her.\""
    )},
    {"type": "body", "text": (
        "Zara, sitting near the edge of the gathered council with Adaugo "
        "beside her, found herself thinking of her own months of "
        "carrying warnings no one else could feel, and understood "
        "something about Emenike's isolation that the rest of the "
        "council could only imagine. \"You never told anyone,\" she "
        "said quietly, not quite a question. \"Not even after two "
        "seasons.\" Emenike shook his head. \"Who could I have told,\" "
        "he said, \"who would not have simply confirmed for them that I "
        "was worth watching more closely. Silence was the only shield I "
        "had left.\""
    )},
    {"type": "body", "text": (
        "Adaugo listened without speaking, one hand unconsciously "
        "resting over the wrist that still carried its own uncut "
        "anchor, and felt a kinship in it she had not expected to feel "
        "for the man who had helped endanger her family. Both of them, "
        "she realized, had been made into a door someone else walked "
        "through without ever being asked whether they wanted the "
        "role."
    )},
    {"type": "body", "text": (
        "\"Proof she still lives comes twice a season,\" he continued, "
        "\"a token I would recognize, left near the same stone where I "
        "leave my own reports. I have never once refused a request, "
        "because I have never once been shown proof that refusing would "
        "not be the reason the proof stopped coming.\" Amara watched him "
        "say it and felt her anger, however justified, begin to bend "
        "under the plain weight of a man who had been hunted as "
        "thoroughly as any of them."
    )},
    {"type": "body", "text": (
        "\"Describe the token,\" Elder Maka said, before Amara could "
        "press further into the why of it. \"Every detail you can "
        "remember, even the ones that seem too small to matter.\" "
        "Emenike described a plaited bracelet of blue thread, one Ijeoma "
        "had worn since childhood, always left beside the stone rather "
        "than a written word, since neither side trusted the other to "
        "keep a written promise. \"It is the only proof I have ever "
        "asked for,\" he said. \"And they have never once failed to "
        "provide it, which is its own kind of cruelty, teaching a man "
        "exactly how reliable his captors can be.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE DIRECTION OF THE TOKENS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka leaned forward, something sharpening in her "
        "attention that had not been there a moment before. \"The "
        "tokens,\" she said. \"Do you know where they come from. Not "
        "who carries them to the stone. Where they begin.\" Emenike "
        "thought hard before answering, clearly trying to be exact "
        "rather than merely helpful. \"West,\" he said. \"And a little "
        "south, if the men who first threatened me were telling the "
        "truth about where they were traveling from that night. I have "
        "never had reason to doubt that part.\""
    )},
    {"type": "body", "text": (
        "In Oso, Chibundu felt the entity go still beside him the "
        "instant the words reached them both. \"West and slightly "
        "south,\" the entity said slowly. \"That is the same bearing "
        "Elder Maka's own reading found running off Mfoniso's second "
        "thread. The same unknown point neither of us could reach.\" "
        "Chibundu felt the shape of it settle into place with the cold "
        "certainty of two facts that had always belonged together. "
        "\"You believe his sister is being held wherever Mfoniso herself "
        "answers to,\" he said. It was not a question."
    )},
    {"type": "body", "text": (
        "The entity did not soften its answer. \"I believe it is "
        "possible, and I believe possible is enough to matter greatly to "
        "a man who has spent two seasons believing he was entirely "
        "alone in this.\" It paused. \"Tell them. A frightened man given "
        "a direction to hope in makes very different choices than one "
        "given none at all.\" Chibundu carried the thought back across "
        "the distance immediately, and watched, through senses he had "
        "learned to trust more than his own eyes, as Elder Maka's face "
        "changed the moment she heard it relayed."
    )},
    {"type": "body", "text": (
        "\"It is not proof,\" Elder Maka told the fire, told Emenike, "
        "told herself as much as anyone. \"A bearing is not a place. But "
        "it is the first time in two seasons anyone outside those who "
        "took her has had even that much.\" Emenike's composure, so "
        "carefully held through the whole account, finally cracked "
        "again, not from grief this time but from something closer to "
        "disbelief. \"You would help her,\" he said. \"After everything "
        "I have cost you.\" Amara answered before Elder Maka could. "
        "\"We have not decided that yet,\" she said. \"But we would not "
        "be the family this village needed if we could hear that and "
        "simply do nothing.\""
    )},
    {"type": "body", "text": (
        "Osadebe, ever the soldier even in a moment thick with feeling, "
        "brought the conversation back to what could actually be "
        "verified. \"A bearing without distance is not a rescue plan,\" "
        "he said. \"It is a direction to start walking in and hope. "
        "Before anyone speaks of finding this place, I want to know how "
        "far west and slightly south a man can travel from Idoro before "
        "he runs out of country that still answers to the crown.\" No "
        "one at the fire had an easy answer, and the gap in their "
        "knowledge sat uncomfortably alongside the hope Elder Maka's "
        "revelation had just given them."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: TWO NIGHTS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe, who had said little through the account beyond what "
        "was necessary to keep it moving, finally asked the question the "
        "rest of them had been circling without naming. \"When does she "
        "expect her next message,\" he said. Emenike's answer came fast, "
        "as though the number had been sitting behind his teeth the "
        "entire hearing, waiting to be asked for. \"Two nights,\" he "
        "said. \"She has never once gone longer without word. I do not "
        "know what happens if she does.\""
    )},
    {"type": "body", "text": (
        "Chidebe felt the weight of that land on the whole council at "
        "once. \"If the stone stays empty,\" he said slowly, working it "
        "through aloud, \"she will know something changed. She may run. "
        "She may retaliate against whatever leverage she still believes "
        "she holds.\" He looked toward Emenike, and for the first time "
        "since the market, something like sympathy crossed his face "
        "alongside the grief. \"Including his sister, if she believes "
        "his silence means he has finally been caught.\""
    )},
    {"type": "body", "text": (
        "Ozoemena spoke up then, quietly, from the edge of the circle "
        "where he had said almost nothing since the hearing began. \"I "
        "know what it is to carry a debt that eats at a person from the "
        "inside for years before anyone else sees it,\" he said. \"I do "
        "not say that to excuse what he did. I say it because I believe "
        "he deserves to be judged by people willing to remember that "
        "fear and love can make a man do things courage alone never "
        "would.\" Emenike looked at him with something close to "
        "gratitude, the first true relief that had crossed his face all "
        "morning."
    )},
    {"type": "body", "text": (
        "No one at the fire had an answer ready for that, and the "
        "silence stretched long enough that even the soldiers standing "
        "watch at its edges shifted uncomfortably in place. Amara looked "
        "around the circle, at Obi's drawn face, at Elder Maka's "
        "careful stillness, at Emenike's open, desperate hope, and "
        "understood that whatever they decided in the next two nights "
        "would shape everything that came after, for this family and "
        "for one they had not even known existed until an hour ago."
    )},
    {"type": "body", "text": (
        "\"Two nights,\" she repeated quietly, more to herself than to "
        "anyone listening, feeling the deadline settle over the compound "
        "like a weight none of them had chosen to carry and all of them "
        "now had to."
    )},
    {"type": "body", "text": (
        "Elder Maka rose slowly, gathering the folds of her wrapper "
        "around her the way she always did before delivering something "
        "she had already decided could not wait. \"We will not solve "
        "this by nightfall,\" she said, \"but we will not solve it "
        "sitting here either. Chidebe, Osadebe, I want everything either "
        "of you knows about the ground west and slightly south of us "
        "before tomorrow's light. Amara, sit with Emenike and learn "
        "every remaining detail he has, no matter how small. We have two "
        "nights to become people capable of a decision neither justice "
        "nor mercy alone can make for us.\""
    )},
    {"type": "body", "text": (
        "No one argued with her. The council broke apart slowly, each "
        "of them carrying a different piece of the same impossible "
        "weight, while Emenike remained by the fire under guard, no "
        "longer entirely a prisoner and not yet entirely anything else, "
        "watching the family he had betrayed begin, however uncertainly, "
        "to fight for the sister he loved."
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
    print("  THE DARK RISE — Episode 88: \"What the Traitor Traded\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_88.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_88.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
