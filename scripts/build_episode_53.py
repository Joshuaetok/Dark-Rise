#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 53: "The Trader's Price"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-29: Episode 53 follows Chidebe, Osadebe, and Ozoemena
as they move quickly on the market trader Effiong named, before word
of his exposure can reach him first. They find him trying to leave
his own stall behind under the cover of an ordinary afternoon errand,
carrying a small sealed letter he has not yet had the chance to
deliver or destroy. Confronted with Effiong's confession, he admits
he has been selling small, seemingly harmless observations to the
trading House for two years, far longer than Osadebe's own posting to
Idoro, meaning the House's interest in the village predates even the
foreign agent's first visit in Episode 36. He gives up the name behind
the scholar's polite title, and the episode closes on the far more
unsettling thing he says once that name is spoken: he is not the only
one the House has bought in Idoro.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_53.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Three"},
    {"type": "title_ep_name", "text": "The Trader's Price"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE STALL LEFT HALF PACKED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ozoemena reached the market ahead of the two officers, having "
        "spent enough seasons walking Idoro's paths at every hour to "
        "know its shortest ones better than either soldier, and found "
        "the trader's stall already half stripped of its usual goods, "
        "cloth and dried fish left in careless piles rather than the "
        "careful rows the man had always kept them in. \"Something has "
        "already spooked him,\" he called back, low and urgent, when "
        "Chidebe and Osadebe caught up. \"He does not leave a stall "
        "looking like this unless he means never to return to it.\""
    )},
    {"type": "body", "text": (
        "They found him two paths further on, walking fast but not "
        "running, a small bundle under one arm and a folded letter "
        "pressed flat against his ribs beneath his tunic, as though he "
        "had convinced himself that walking calmly through his own "
        "familiar streets would draw less notice than any hurry could. "
        "He stopped the moment he saw Chidebe's uniform, and something "
        "in his face gave way at once, the particular collapse of a man "
        "realizing the calculation he had been running in his head for "
        "the last hour had already failed."
    )},
    {"type": "body", "text": (
        "\"Uduak,\" Ozoemena said, and there was no anger in the name "
        "yet, only a plain, heavy disappointment that seemed to cost "
        "him more than shouting would have. \"I have bought fish from "
        "your hands more mornings than I can count. Tell me now, "
        "before these two decide for you how this conversation is "
        "going to go, exactly what you have been carrying out of this "
        "village besides fish.\""
    )},
    {"type": "body", "text": (
        "Uduak's hand moved instinctively toward the letter at his "
        "ribs, and Chidebe closed the distance before the motion could "
        "become anything more than instinct, taking the folded paper "
        "without force, the way a man takes something already given up "
        "rather than something fought over. He broke the plain, "
        "unmarked seal and read in silence for a long moment before "
        "handing it wordlessly to Osadebe."
    )},
    {"type": "body", "text": (
        "\"A weekly accounting,\" Osadebe said, scanning it once, twice, "
        "his voice flattening into the careful neutrality he used when "
        "he did not yet trust himself to sound as troubled as he felt. "
        "\"Patrol counts. Which elders still meet under the mango tree "
        "and which have stopped attending. Nothing that reads, on its "
        "own, like a single dangerous fact. Only useful, patient people "
        "collecting useful, patient pieces, the way a slow fire is "
        "built one dry branch at a time.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: TWO YEARS OF DRY BRANCHES
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Uduak did not wait to be asked twice before the whole shape "
        "of it came out of him at once, the confession of a man who had "
        "clearly rehearsed denying it and found, faced finally with the "
        "letter in Osadebe's hand, that he no longer had the will to "
        "attempt the performance. \"Two years,\" he said. \"It began "
        "two years ago, long before any of you arrived, long before "
        "there was an entity or a captain or a name spoken at any "
        "boundary. A quiet man asked small questions at my stall and "
        "paid well for small answers. I told myself there was no harm "
        "in it. I still believed that, mostly, until last night.\""
    )},
    {"type": "body", "text": (
        "Osadebe felt the ground of his own understanding shift under "
        "the plain arithmetic of it. \"Two years,\" he repeated. \"That "
        "places this House's interest in Idoro before the dibia's "
        "death, before Ozoemena's rise and fall, before even the first "
        "trader carried word of Zara's departure north. Whatever drew "
        "them here first, it was never the entity revealing itself at "
        "the boundary. That came later. Something about this village "
        "was already worth watching before any of us understood there "
        "was anything here worth watching at all.\""
    )},
    {"type": "body", "text": (
        "\"I do not know what it was they wanted at first,\" Uduak "
        "said. \"I was never told, and I made certain never to ask, "
        "since the not asking was worth almost as much to me as the "
        "coin itself. It was only these last months, once the boy at "
        "the boundary became something spoken of openly, that the "
        "questions changed. Sharper. More urgent. Whether the crown had "
        "posted new soldiers. Whether a woman named Amara still kept a "
        "compound near the fields. When a stand down might next be "
        "arranged, and how long it might last.\""
    )},
    {"type": "body", "text": (
        "Chidebe's expression had not moved through most of the "
        "confession, but it moved now, a controlled, private fury "
        "settling into the line of his jaw. \"You sold the hour that "
        "nearly cost a woman her life and her son his freedom,\" he "
        "said, \"and you are telling me you did it without ever once "
        "asking who it was for, or what it would be used to do.\""
    )},
    {"type": "body", "text": (
        "\"I am telling you the truth, which is the only thing left I "
        "have to offer any of you,\" Uduak said, and something in his "
        "voice cracked at last, the calm collapsing into something "
        "closer to fear. \"The one who pays me calls herself a scholar "
        "to your council. To me, across two years of quiet meetings at "
        "the river landing, she has only ever given one name. Ebiere. "
        "I do not know if it is true. I only know it is the name I "
        "have and the only one I can give you.\""
    )},
    {"type": "body", "text": (
        "Osadebe wrote the name down at once, plain and careful, the "
        "first solid thread this whole tangled season had offered him "
        "to pull on. \"You will come with us,\" he told Uduak, \"and you "
        "will tell every part of this again, slowly, to the council, "
        "and to whoever Udo sends once this reaches them. It may be the "
        "only thing that buys you any mercy left to ask for.\""
    )},
    {"type": "body", "text": (
        "Uduak did not resist being led. But as they turned him toward "
        "the council path, he said the one thing none of them had "
        "thought yet to ask, and it landed harder in the quiet market "
        "than the letter's contents had. \"You should know,\" he said, "
        "\"before you decide you have found the whole of it. I am not "
        "the only one Ebiere pays in this village. I was only ever the "
        "one who happened to speak too plainly to a frightened boy "
        "with more coin than sense.\""
    )},
    {"type": "body", "text": (
        "Ozoemena went very still at that, the disappointment on his "
        "face hardening into something colder, and Osadebe felt the "
        "morning's small, hard won relief drain out of him at once, "
        "replaced by the far larger and far less answerable question "
        "of exactly how many familiar faces in Idoro belonged, in some "
        "quiet part, to someone else entirely."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE COUNCIL HEARS IT TWICE
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "By the time the sun stood directly overhead, Uduak had told "
        "the whole of it a second time beneath the mango tree, this "
        "time to the full gathered council, Amara summoned from her own "
        "compound the moment word reached her that the matter touched "
        "her family directly. She listened without interrupting, her "
        "hands folded tightly in her lap, and said nothing at all until "
        "the name Ebiere was spoken aloud for the second time that day."
    )},
    {"type": "body", "text": (
        "\"I met a woman who called herself that,\" Amara said quietly, "
        "\"though she gave a different name to this council when she "
        "asked leave to speak with Chibundu across the boundary. A "
        "scholar's name, gentle and unthreatening. It seems now she "
        "keeps as many names as she keeps purposes, and shows this "
        "village only whichever one serves her on a given day.\""
    )},
    {"type": "body", "text": (
        "Elder Maka, seated closer to the circle's center than she had "
        "sat in many months, spoke next, her voice carrying the weight "
        "of an old memory finally finding its match. \"My grandmother "
        "told stories of houses that hunted spirits with the same "
        "patience they hunted gold,\" she said. \"She always said the "
        "surest sign of one was not the soldiers they eventually sent, "
        "but the years they spent first, quietly, buying small pieces "
        "of a place before anyone there understood there was a larger "
        "picture being assembled. Two years of small questions is not "
        "carelessness. It is exactly the patience she warned was worst "
        "to face.\""
    )},
    {"type": "body", "text": (
        "Adaugo, standing near her mother's side for the first time in "
        "a council session rather than merely watching from its edge, "
        "asked the question plainly that several others in the circle "
        "had clearly been holding back out of caution. \"If she has "
        "bought more than one mouth in this village, how do any of us "
        "know which mouths are still hers, and which have only just "
        "been cleared of suspicion because no one has thought yet to "
        "look at them closely enough.\""
    )},
    {"type": "body", "text": (
        "No one in the circle answered that at once, the silence itself "
        "an admission of how little any of them could honestly promise "
        "in response. Ozoemena finally broke it, his voice rougher than "
        "usual. \"We watch harder,\" he said, \"the same as we did after "
        "the boundary walk, the same as we will keep doing until this "
        "House understands that Idoro has stopped being an easy place "
        "to buy quietly. It cost us something to learn that lesson "
        "twice already. I do not intend to let it cost us a third "
        "time.\""
    )},
    {"type": "body", "text": (
        "Osadebe closed the session by setting down, plainly, what "
        "would happen next. Uduak would be held, not harmed, until "
        "Udo's own judgment could be sought on him. The name Ebiere "
        "would travel north in his next report, alongside everything "
        "Effiong and the ambush had already taught him. And the "
        "council, for its own part, would need to decide how much "
        "longer it could afford to treat its own market, its own "
        "familiar faces, as ground already safe simply because it had "
        "always felt that way before."
    )},
    {"type": "body", "text": (
        "Amara walked home from the council that evening turning "
        "Uduak's last warning over in her mind, unable to shake the "
        "particular cold of it. It was one thing to fear an army "
        "crossing a boundary stone. It was another thing entirely to "
        "wonder, buying cloth or fish at her own familiar market the "
        "next morning, whose hand was passing it to her, and what that "
        "hand might already have sold about the son she had only just "
        "been given back."
    )},
    {"type": "body", "text": (
        "In Oso, the entity felt her unease reach it faintly across the "
        "distance the way it now felt most of Idoro's larger currents "
        "without needing to search for them, and found itself, for the "
        "first time in this long season, wishing it could offer her "
        "more than patience in return. Two years, it thought, turning "
        "the number over the way Osadebe had. Two years was longer "
        "than the entity itself had known the boy existed. Whatever "
        "this House wanted from Idoro, it had wanted it before "
        "Chibundu ever drew his first breath, and that fact alone told "
        "the entity the ambush at the boundary had never been the "
        "beginning of anything. It had only been the first move either "
        "side had let the other one see."
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
    print("  THE DARK RISE — Episode 53: \"The Trader's Price\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_53.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_53.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
