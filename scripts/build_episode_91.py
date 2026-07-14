#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 91: "What the Confrontation Cost"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-10-06: Episode 91 sits in the immediate aftermath of
Episode 90's climax. Zara fights through the night to keep Emenike
alive, his wound deep enough that even her steady hands cannot promise
an outcome. Chibundu spends the same hours calling into a silence in
Oso that does not answer, growing convinced something in the entity's
unprecedented direct action cost more than any of them yet understand.
Osadebe and Chidebe reconstruct the attack and realize the market
ambush's very success at drawing every soldier away was what left the
compound open, a painful tactical lesson learned at Emenike's expense.
Near dawn, the entity finally responds, weaker than Chibundu has ever
felt it, admitting it does not know whether it could do what it did
again, or what the reaching may have cost Oso's boundary itself. The
episode closes on Emenike's fever finally breaking toward survival
rather than death, and on Amara's quiet, unresolved fear that the
household bought this single night's safety with a debt still waiting
to be called due.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_91.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Ninety One"},
    {"type": "title_ep_name", "text": "What the Confrontation Cost"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE LONG NIGHT OF HANDS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara worked over Emenike through the deepest part of the "
        "night, her hands steadier than her own fear had any right to "
        "let them be, cleaning and packing a wound that refused, for the "
        "first two hours, to promise her anything at all. She had "
        "delivered both twins into this world with these same hands. "
        "She found herself praying, without quite meaning to, that they "
        "still remembered how to keep someone in it."
    )},
    {"type": "body", "text": (
        "Amara did not leave his side once, holding a cloth or a bowl "
        "or simply his hand whenever Zara's own were occupied elsewhere, "
        "and found herself, somewhere past midnight, forgiving him "
        "completely for a betrayal she had not yet decided, an hour "
        "earlier, whether she could forgive at all. A man did not throw "
        "himself in front of a spear for a family he still meant harm. "
        "Whatever else Emenike was, he had proven that much beyond "
        "argument."
    )},
    {"type": "body", "text": (
        "Elder Maka examined Adaugo twice more before allowing herself "
        "to rest, checking the wrist Mfoniso had gripped for any sign "
        "the anchor thread had changed, sharpened, or spread, and found "
        "only the same familiar cold, unchanged by everything that had "
        "just happened to it. \"It answered when she touched it "
        "directly,\" Adaugo said quietly, still shaking. \"I felt it "
        "wake up. Truly wake, not merely wait.\" Elder Maka had no easy "
        "comfort to offer that, only a promise to examine it properly "
        "once daylight and steadier hands returned to the household."
    )},
    {"type": "body", "text": (
        "Obi stood at the edge of the small circle around Emenike, "
        "unable to help with hands that had never learned Zara's craft, "
        "and found himself instead counting every choice that had led to "
        "this single terrible night, the ambush, the empty stone, the "
        "handful of soldiers left behind to guard a compound everyone "
        "had judged safe enough. \"We chose wrong,\" he said quietly, to "
        "no one in particular. \"Not maliciously. Not carelessly. We "
        "simply chose wrong, and a good man is paying for it on the "
        "ground in front of us.\""
    )},
    {"type": "body", "text": (
        "Ozoemena arrived late, roused from his own hut by the shouting, "
        "and knelt briefly beside Emenike before anyone thought to stop "
        "him, taking the wounded man's hand in both of his own. \"You "
        "foolish, brave man,\" he murmured, more to himself than to "
        "Emenike, who could not hear him. \"I asked this house to judge "
        "you by more than your worst hour. You have just shown them "
        "your best one instead.\""
    )},
    {"type": "body", "text": (
        "Kene, woken by the commotion despite every effort to keep him "
        "sleeping through it, was found by Zara sitting quietly at the "
        "edge of the yard, watching the adults work with the grave, "
        "careful stillness of a child who understood, without being "
        "told, that this was not a night for questions. She carried him "
        "back to bed herself once Emenike's bleeding had finally begun "
        "to slow, and sat with him until his own breathing settled into "
        "sleep."
    )},
    {"type": "body", "text": (
        "Chidebe and Osadebe arrived within minutes of each other, both "
        "men grim and breathless, both immediately reconstructing aloud "
        "what neither could yet forgive himself for missing. \"The "
        "ambush worked exactly as we built it,\" Osadebe said bitterly. "
        "\"It simply worked in the wrong direction. Every soldier we "
        "pulled toward that market was a soldier we pulled away from "
        "here.\" Chidebe said nothing for a long moment, staring at the "
        "blood already drying dark in the compound dirt. \"We built her "
        "a door,\" he said finally, \"and called it a trap.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE SILENCE IN OSO
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, Chibundu sat alone in the cold place beneath the roots "
        "for hours, calling into a silence that gave him nothing back, "
        "not even the faint, ambient weight the entity's presence had "
        "always left on the air even at its quietest. He had known this "
        "power for years now. He had never once, in all that time, felt "
        "it simply absent."
    )},
    {"type": "body", "text": (
        "He tried, several times, to picture what a wound to something "
        "as old and vast as the entity might even look like, and found "
        "his imagination offered him nothing useful, only the memory of "
        "Emenike's blood soaking dark into the compound dirt, as though "
        "his mind insisted on measuring an incomprehensible loss against "
        "the one loss it already understood how to fear."
    )},
    {"type": "body", "text": (
        "The presence stirred near dawn, its own strength still far "
        "from fully recovered, and offered what comfort it honestly "
        "had to give rather than the comfort Chibundu wanted to hear. "
        "\"I have never seen it act the way you describe,\" it admitted. "
        "\"Not once, in three centuries of watching it watch you. "
        "Whatever it spent tonight, it spent past whatever careful "
        "boundary kept it safe before.\" Chibundu asked the only "
        "question that mattered. \"Will it come back.\" The presence did "
        "not lie to him. \"I do not know,\" it said. \"I have been wrong "
        "about less before.\""
    )},
    {"type": "body", "text": (
        "He stayed through the last dark hours of the night rather than "
        "return to a household already stretched too thin to also carry "
        "his fear, tracing the same cold, empty ground the entity had "
        "always occupied, until, sometime near first light, something "
        "finally answered him, faint as a held breath finally let go."
    )},
    {"type": "body", "text": (
        "\"I am here,\" the entity said, and even those three words cost "
        "it visibly, thinner and further away than anything Chibundu had "
        "heard from it since the night it first named itself to him. "
        "\"I do not know if I could do that again,\" it admitted, before "
        "he could ask. \"I do not know what it cost Oso itself to let me "
        "try. I only knew, in that moment, that the cost of not trying "
        "was a price I was no longer willing to let you pay instead.\""
    )},
    {"type": "body", "text": (
        "\"You have spent three centuries telling me restraint was "
        "wisdom,\" Chibundu said, unable to keep the rawness fully out "
        "of his voice. \"I watched you throw that away in a single "
        "breath tonight.\" The entity did not defend itself. \"Wisdom "
        "and cowardice can wear the same shape from a distance,\" it "
        "said. \"I have called mine wisdom for three hundred years "
        "because I was never once tested closely enough to learn which "
        "one it actually was.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt something in his chest loosen for the first time "
        "in hours, relief and fresh fear arriving together the way they "
        "so often did lately. \"Rest,\" he told it, an order rather than "
        "a request, the first time in their long acquaintance he had "
        "ever spoken to it that way. The entity, for once, did not argue "
        "with him."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: WHAT DAWN FOUND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Emenike's fever broke a little past dawn, his breathing "
        "settling from the ragged, shallow catch it had held all night "
        "into something Zara finally allowed herself to call sleep "
        "rather than merely survival. \"He will live,\" she told Amara, "
        "exhaustion and relief fighting for control of her voice in "
        "equal measure. \"I would not have promised that three hours "
        "ago.\""
    )},
    {"type": "body", "text": (
        "Emenike stirred briefly before true sleep finally claimed him, "
        "eyes finding Amara's face through the haze of exhaustion and "
        "blood loss, and managed only a few slurred words before his "
        "strength gave out again. \"Ijeoma,\" he murmured. \"Did I lose "
        "her too, tonight.\" Amara took his hand and held it firmly "
        "until she was certain he could feel it. \"No,\" she told him. "
        "\"Nothing about tonight changes what we already promised you. "
        "Sleep. We will still be fighting for her when you wake.\""
    )},
    {"type": "body", "text": (
        "Adaugo woke once more before full morning, and found her way, "
        "unsteady, to where Emenike lay sleeping, sitting beside him "
        "without waking anyone to ask permission. \"You did not have to "
        "do that,\" she told his sleeping face quietly. \"Whatever you "
        "owed this family, you already began repaying it the moment you "
        "told us the truth. You did not have to nearly die proving it "
        "again.\" She stayed there a long while, watching him breathe, "
        "before Elder Maka gently led her back to rest."
    )},
    {"type": "body", "text": (
        "Amara sat back on her heels at the words, feeling the weight "
        "of the whole night finally settle onto her shoulders now that "
        "there was room for it to land. She looked around the compound "
        "at the drying blood, at the soldiers still walking the wall "
        "twice as carefully as they had the evening before, at Adaugo "
        "asleep at last against Elder Maka's side, and understood that "
        "surviving the night was not the same thing as having answered "
        "what the night had asked of them."
    )},
    {"type": "body", "text": (
        "Osadebe found her there as the sun cleared the tree line "
        "fully, his own face carrying the particular exhaustion of a man "
        "who had spent the night doing arithmetic he did not like the "
        "answer to. \"She will not try this again the same way,\" he "
        "said. \"Whatever met her here changed something in how she "
        "sees this house. I do not know yet whether that makes us safer "
        "or simply harder to predict.\""
    )},
    {"type": "body", "text": (
        "Amara did not have an answer for him either, only the quiet, "
        "unresolved fear she had carried since the moment the entity's "
        "reach first tore through the compound and then vanished into "
        "silence behind it. They had bought this single dawn with a "
        "debt none of them yet understood the size of, and somewhere "
        "beyond Idoro's boundary, wounded and shaken but very much "
        "alive, the woman who had opened that debt was already deciding "
        "how she meant to collect it, and how much of that reckoning "
        "would fall on people who had never asked to stand in her way."
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
    print("  THE DARK RISE — Episode 91: \"What the Confrontation Cost\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_91.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_91.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
