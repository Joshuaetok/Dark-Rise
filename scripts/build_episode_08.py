#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 8: "The Sleepwalker"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-15: Episode 8 picks up days after Episode 7. Obi, no longer
willing to only watch, sneaks out at night to see Oso for himself, and finds
Zara already on the bush path ahead of him, walking in an unseeing trance
toward the ak-pu tree. He wakes her at the very edge of the boundary before
she crosses it. Neither of them understands what happened. The entity,
watching through the thread it opened in Episode 7, treats the interruption
as a successful test: it now knows it can move an adult body at will, and
that it will not always need to let her stop. Obi confesses his broken
promise to Amara, who now carries a second secret alongside her own from
Episode 6, deepening both her isolation and the quiet strain between them.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_08.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Eight"},
    {"type": "title_ep_name", "text": "The Sleepwalker"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT OBI DECIDED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Three nights after Elder Maka's visit, Obi lay beside his "
        "sleeping wife and listened to her breathe until he was certain "
        "she would not wake, and then he rose, and dressed, and took down "
        "the machete he had not touched since before the twins were "
        "born."
    )},
    {"type": "body", "text": (
        "He told himself he was not breaking anything. He had promised "
        "to watch, together, and Amara was asleep and could not watch "
        "with him tonight, and a man could not be blamed for watching "
        "alone when the woman he had promised to watch beside him was "
        "unavailable. It was a thin argument and he knew it was thin even "
        "as he built it, but a thin argument was still enough to carry "
        "him out through the compound gate and onto the path that led, "
        "eventually, everywhere in Idoro led, toward Oso."
    )},
    {"type": "body", "text": (
        "He did not intend to cross the boundary. He told himself this "
        "twice more before he had gone even a hundred paces, which was "
        "itself a kind of warning he chose not to hear. He only wanted "
        "to see the ak-pu tree from close enough to know it was a real "
        "tree, rooted in real ground, and not the shapeless dread it had "
        "become in every telling since the dibia's apprentices ran."
    )},
    {"type": "body", "text": (
        "Idoro at that hour belonged to no one. The compounds sat dark "
        "and shuttered, cook fires banked to embers, dogs curled too "
        "deep in sleep even to lift their heads at his passing. Obi had "
        "walked this ground his whole life and had never once felt it "
        "watch him back the way it seemed to now, every silent doorway a "
        "held breath, every shadow a question about what kind of man "
        "left his wife sleeping to go looking for a monster."
    )},
    {"type": "body", "text": (
        "He told himself he only needed to see it once, with his own "
        "eyes, to know the shape of the thing that had swallowed his "
        "son whole and given something else back in his place. A man "
        "could not fight what he had only heard described in a "
        "frightened woman's whisper. He needed the weight of it. Then he "
        "would turn around, and he would tell Amara everything, and the "
        "promise he had not quite made would finally be worth something."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The moon was high and thin. The bush path narrowed the further "
        "he walked, hemmed by grass gone silver and stiff in the cold "
        "night air, and Obi kept the machete loose in his hand without "
        "quite admitting to himself what he expected to use it against."
    )},
    {"type": "body", "text": (
        "He was perhaps halfway to the tree line when he saw the figure "
        "ahead of him on the path."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE PATH — WHAT MOVED HER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "It was a woman, walking steadily, without a lamp, without "
        "hesitation, in a direction no one walked alone at that hour "
        "unless something had gone very wrong in their life or their "
        "mind. Obi's first thought was fear for himself, that he had been "
        "seen leaving his own compound and someone had followed to catch "
        "him at it. His second thought, when he came close enough to "
        "make out her shape against the pale grass, was worse."
    )},
    {"type": "body", "text": (
        "It was Zara."
    )},
    {"type": "body", "text": (
        "She had gone to sleep hours earlier the way she had gone to "
        "sleep every night since the strange tingling in her palms, "
        "telling herself firmly that a tired mind invents its own "
        "ghosts, and had drifted under with the grinding stone still "
        "unfinished beside her mat. She had not felt herself rise. She "
        "had not felt her feet find the door, or the packed earth beyond "
        "it, or the long cooling grass of the bush path. Whatever part of "
        "her carried her forward that night, it was not the part that "
        "dreamed."
    )},
    {"type": "body", "text": (
        "She wore only her sleeping wrap, her feet bare on ground that "
        "should have made any waking person wince and slow. She did not "
        "slow. She did not look toward him when he called her name, "
        "quietly at first and then louder, and it was the not looking "
        "that frightened Obi more than anything else about her, because "
        "her eyes were open, fixed ahead on the dark line of trees, and "
        "they were simply not seeing him at all."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow beneath the ak-pu roots, the entity felt the "
        "woman's feet cross ground it had marked in its own attention the "
        "moment it first touched her thread, and understood, with the "
        "flat satisfaction of an experiment concluding cleanly, exactly "
        "how much of her it could move."
    )},
    {"type": "body", "text": (
        "It had not commanded her the way it had once reached for "
        "Kene, a single sharp strike meant to be seen and to distract. "
        "This had been slower, gentler, a hand laid over her sleeping "
        "will the way a rider lays a hand over a horse's neck before "
        "ever touching the reins. It had walked her out of her own hut, "
        "down her own path, closer to Oso than any grown woman in Idoro "
        "had come without an escort of elders and fire in longer than "
        "the entity had bothered to count."
    )},
    {"type": "body", "text": (
        "She would have reached the tree line herself within a hundred "
        "more paces. The entity had intended to let her arrive, to feel "
        "what her hands remembered when they touched ak-pu bark again "
        "after all these years, and to see what that memory might loosen "
        "in her the way memory had loosened something in the dibia."
    )},
    {"type": "body", "text": (
        "The man's voice, calling her name from behind, was not part of "
        "the entity's plan. It considered, for one cold instant, holding "
        "its grip on her regardless, forcing her those last hundred "
        "paces despite him. It decided against it. A woman found "
        "wandering alone toward the forbidden bush could be explained "
        "away as grief, or sleep sickness, or a mind unraveling under the "
        "village's fear. A woman dragged there visibly against a "
        "struggling man's grip could not be explained at all, and the "
        "entity had already spent one door's worth of exposure buying "
        "silence during the cleansing rite. It was not ready to spend a "
        "second."
    )},
    {"type": "body", "text": (
        "It let her go. Gently, the way it had taken her, so that the "
        "release itself would look like nothing more than a woman waking "
        "startled from a walk she could not explain."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "SECOND THREAD CONFIRMED VIABLE. FULL MOTOR CONTROL ACHIEVABLE AT RANGE. WITHDRAWAL EXECUTED, UNDETECTED BY THIRD PARTY BEYOND THE HOST."},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Obi reached her three strides before the first line of ak-pu "
        "saplings and caught her arm, and the moment his hand closed "
        "around it, Zara's whole body seized as though she had been "
        "dropped from a height into her own skin."
    )},
    {"type": "body", "text": (
        "She gasped, staggered, and would have fallen if he had not "
        "held her upright. Her eyes, wild now and finally, finally "
        "seeing him, went from his face to the trees ahead and back "
        "again, and Obi watched understanding arrive in her like cold "
        "water finding a crack in a wall."
    )},
    {"type": "body", "text": (
        "\"How did I come here,\" she said, and her voice shook so badly "
        "the words barely held together. \"I was in my hut. I was "
        "grinding leaf for tomorrow. I was in my hut.\""
    )},
    {"type": "body", "text": (
        "\"You were walking,\" Obi said. \"Straight toward it. You did "
        "not hear me until I touched you.\""
    )},
    {"type": "body", "text": (
        "Zara looked down at her own bare, bleeding feet as though they "
        "belonged to someone else, and Obi understood that whatever "
        "answer she needed, he did not have it to give her."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — THE CONFESSION
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "He walked her home in silence, her arm gripped tight in his, "
        "both of them casting glances back at the tree line more than "
        "once, as though it might have grown legs of its own to follow."
    )},
    {"type": "body", "text": (
        "At her door, Zara found enough of her voice to say what duty "
        "demanded of her. \"I must tell Elder Maka. Whatever this is, "
        "she must know.\""
    )},
    {"type": "body", "text": (
        "\"Tell her tomorrow,\" Obi said. \"Not tonight, half out of your "
        "mind and barefoot in blood. Let it wait until you can say it "
        "plainly, and let me speak to my wife first.\""
    )},
    {"type": "body", "text": (
        "Zara studied him, and something passed behind her eyes that "
        "told Obi she had already guessed more than he had said aloud. "
        "\"Your wife already knows something is wrong in that forest that "
        "the rest of us have not been told.\""
    )},
    {"type": "body", "text": (
        "He did not answer that, and his silence was answer enough. She "
        "nodded once, wearily, and let him go."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Amara was awake when he returned, sitting up in the dark with "
        "the particular stillness of a woman who had already imagined "
        "every reason her husband might be missing from their bed and "
        "liked none of them."
    )},
    {"type": "body", "text": (
        "He told her all of it. The broken promise. The path. Zara's "
        "bare feet and unseeing eyes and the hundred paces that would "
        "have ended at the tree line if he had walked ten breaths "
        "slower."
    )},
    {"type": "body", "text": (
        "Amara listened without interrupting, and when he finished, she "
        "sat with her hands pressed flat against her knees for a long "
        "moment, doing the same silent arithmetic she had done alone "
        "since the night of the cleansing rite, only now with a second "
        "number added to the sum."
    )},
    {"type": "body", "text": (
        "\"You should have woken me,\" she said finally. Not about the "
        "broken promise. About what came after it."
    )},
    {"type": "body", "text": (
        "\"I know,\" Obi said. \"I am telling you now.\""
    )},
    {"type": "body", "text": (
        "\"Yes,\" Amara said. \"You are.\" And she let the small mercy "
        "of that be enough for tonight, even as she kept, silent and "
        "unshared, the older secret still folded behind her ribs, the "
        "one about her own son's eyes turning dark in firelight while "
        "the whole village looked the wrong way."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Neither of them slept again before dawn. Neither of them knew "
        "yet that beneath the ak-pu roots, the entity had already filed "
        "away everything it needed from the night's failed experiment, "
        "and had begun, with the patience of something that measured "
        "time in centuries rather than hours, considering exactly which "
        "night it would choose not to let the woman stop."
    )},

    {"type": "blank", "text": ""},
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
    print("  THE DARK RISE — Episode 8: \"The Sleepwalker\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_08.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_08.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
