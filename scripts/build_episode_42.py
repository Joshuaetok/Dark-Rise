#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 42: "The Thread Not Cut"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-18: Episode 42 finally pays off Zara's departure from
Episode 19 — she walks back into Idoro after weeks away, unable to
explain why beyond a pull she could not resist, uncannily similar to the
sleepwalking compulsion that first exposed her to the entity in Episode
8. Amara keeps her old promise and takes her in without hesitation. In
Oso, the entity, newly vigilant since Episode 41's revelation that the
presence beyond its borders had been watching, does something it has not
done in a long while: checks on the old threads it once built and then
abandoned. It finds the dibia's thread permanently dark and Elder Maka's
thread quiet but present, exactly as expected. Zara's thread, which the
entity itself judged not worth defending back in Episode 16 and left
entirely undefended, is not where it should be. Something else has been
walking it. The episode closes on the entity's realization that Zara did
not simply choose to come back — she was called back, by the one power
that had a use for a door the entity itself had thrown away.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_42.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Forty Two"},
    {"type": "title_ep_name", "text": "The Thread Not Cut"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — A PULL SHE COULD NOT NAME
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara walked back into Idoro at dusk, thinner than Amara "
        "remembered her, her feet bare and cracked from a road she "
        "would later admit she could not fully account for, and stood "
        "at the edge of the compound the way a woman stands at a door "
        "she is no longer certain she has the right to knock on."
    )},
    {"type": "body", "text": (
        "Amara reached her before a single word passed between them, "
        "pulling her into an embrace that answered every question "
        "either of them might have tried to ask first, and only once "
        "Zara had been fed and settled beside the fire did she manage "
        "to explain, haltingly, why she had returned to the one "
        "village that had asked her to leave it."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "\"I found a village three rivers north that needed a "
        "midwife and did not ask why my old one no longer wanted me,\" "
        "she said. \"I was building something there. A life, almost. "
        "Then four nights ago I woke on the river road already two "
        "days walking, with no memory of leaving my new bed, and I "
        "knew, the way I knew that first night with Obi, that my feet "
        "had made a decision my mind had no part in.\""
    )},
    {"type": "body", "text": (
        "Amara felt the old fear return with a familiarity that "
        "frightened her more than a new fear would have. \"You "
        "thought that was finished,\" she said. \"We all thought it "
        "was finished, once you crossed the fields and the entity let "
        "you go without a fight.\""
    )},
    {"type": "body", "text": (
        "\"So did I,\" Zara said. \"But whatever moved my feet this "
        "time did not feel like what moved them then. That first time "
        "felt like something reaching into a house and taking what it "
        "wanted. This time felt like something opening a door it had "
        "left unlocked on purpose, a long time ago, and only now "
        "deciding to walk back through it.\""
    )},
    {"type": "body", "text": (
        "She described the walk itself the way a person describes a "
        "dream already fading, certain of the shape of it but unable "
        "to hold the edges steady. No fear, she said, which was itself "
        "the strangest part. No sense of being taken against her will, "
        "only a growing, patient certainty with every step that "
        "Idoro was where she was supposed to be standing, as though "
        "someone had simply reminded her of a plan she had agreed to "
        "long before she had any memory of agreeing to it."
    )},
    {"type": "body", "text": (
        "\"I do not feel afraid of it,\" she admitted, and looked "
        "almost ashamed to say so aloud. \"I know I should. Everything "
        "that has happened in this village since I left should make me "
        "afraid of it. But whatever brought me back did not feel angry, "
        "or hungry, the way people describe the thing in Oso feeling. "
        "It felt almost patient. Almost kind. I do not know what to do "
        "with a fear that refuses to feel like fear.\""
    )},
    {"type": "body", "text": (
        "Amara held her promise from months before without needing to "
        "be reminded of it, and told Zara plainly she would not spend "
        "another night of this alone, whatever door had opened inside "
        "her. But she carried the distinction Zara had drawn back to "
        "her own sleeping mat that night and turned it over long after "
        "the compound had gone quiet, unable to shake the sense that a "
        "difference this precise was not something an ordinary woman "
        "would have felt unless it was actually, carefully, true."
    )},
    {"type": "body", "text": (
        "Kene found her the next morning before anyone had thought to "
        "keep the two of them apart, tugging at the hem of her wrap "
        "with the unguarded curiosity of a child meeting a stranger who "
        "somehow did not feel like one, and Zara knelt to meet him at "
        "his own height, her hands finding the same careful, "
        "practiced steadiness they had used to catch him into the "
        "world in the first place. \"The last time I held you, you "
        "were smaller than a loaf of bread,\" she told him, and found "
        "herself unexpectedly undone by the ordinary miracle of a boy "
        "who had simply been allowed to grow, running now on legs she "
        "had once cupped in one palm."
    )},
    {"type": "body", "text": (
        "Obi watched the two of them from the doorway with a warmth "
        "he had not expected to feel this soon after the fear of the "
        "night before, and told Amara quietly that whatever pulled "
        "Zara back to Idoro, some part of him was simply glad to see "
        "her safe under their roof again rather than wandering some "
        "unknown road alone. \"We can be glad and afraid at the same "
        "time,\" Amara said. \"I have had a great deal of practice at "
        "exactly that this last year.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — AN INVENTORY OF OLD DOORS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity had spent the days since "
        "sensing the presence's closer attention doing something it "
        "had not done carefully in a long while: taking stock of every "
        "thread it had ever built into Idoro, the way a careful trader "
        "counts his stores after learning a rival has been seen near "
        "his warehouse."
    )},
    {"type": "body", "text": (
        "The dibia's old thread was exactly where it should be, "
        "permanently dark, spent and closed since the night it had "
        "used that thread to strike Ozoemena down. Elder Maka's thread "
        "sat quiet and present, watched but undisturbed, precisely as "
        "the entity had left it since deciding, weeks ago, that "
        "patient observation served it better than any direct reach."
    )},
    {"type": "blank", "text": ""},
    {"type": "body", "text": (
        "Zara's thread was not where it should have been."
    )},
    {"type": "body", "text": (
        "The entity had judged that thread not worth defending long "
        "ago, back when Elder Maka's ultimatum first forced the "
        "question, and had let it go entirely undefended when Zara "
        "chose exile over confinement, confident an abandoned door "
        "left no lock worth picking. It searched for the thread now "
        "the way a man searches a familiar room for a key he left on "
        "a particular nail, and found, instead of the faint, dormant "
        "connection it expected, something warmer, more recently "
        "handled, worn smooth in a way three weeks of neglect should "
        "never have produced on its own."
    )},
    {"type": "body", "text": (
        "VESSEL: THIRD PARTY ACCESS DETECTED ON PREVIOUSLY ABANDONED "
        "THREAD. ENTITY DID NOT INITIATE. ORIGIN CONSISTENT WITH "
        "PRESENCE CONTACTED DURING PARLAY. PURPOSE UNKNOWN."
    )},
    {"type": "body", "text": (
        "It traced the warmth as carefully as it dared, unwilling to "
        "risk a second unplanned crossing so soon after the first two "
        "had each cost it more than it expected, and found, at the "
        "very edge of what it could safely follow, the unmistakable "
        "shape of the same patient pressure it had met during the "
        "parlay, resting inside a door the entity itself had thrown "
        "away as worthless."
    )},
    {"type": "body", "text": (
        "It weighed, briefly, whether to sever the thread outright now "
        "that it had found where the presence's attention had settled, "
        "and discarded the idea almost as quickly as it arrived. "
        "Cutting a door the presence was actively using would announce, "
        "as plainly as any words, that the entity had noticed and had "
        "chosen confrontation over patience, a message it was not yet "
        "prepared to send while it still understood so little of what "
        "the presence actually wanted from a woman who had touched the "
        "vessel exactly once, briefly, at his very first breath."
    )},
    {"type": "body", "text": (
        "It settled instead for watching, the same careful patience it "
        "had once spent three centuries perfecting before a single "
        "child gave it anything worth spending that patience on, and "
        "found the watching harder now than it had ever been before, "
        "because for the first time the entity was not the only "
        "patient thing paying attention to this particular door."
    )},
    {"type": "body", "text": (
        "It understood, turning the discovery over with a coldness "
        "that had nothing to do with the season, that Zara had not "
        "walked back into Idoro on legs that simply remembered an old "
        "compulsion. She had been called, deliberately, by the one "
        "power patient enough to notice a door the entity had left "
        "hanging open behind it and careful enough to wait three "
        "centuries of the entity's own tenancy before finally deciding "
        "the door was worth walking through."
    )},
    {"type": "body", "text": (
        "The entity did not yet know what the presence wanted with a "
        "midwife who had touched the vessel only once, at his very "
        "first breath, a connection so old and so faint the entity "
        "itself had stopped counting it as meaningful months ago. It "
        "understood only that the presence had counted it still, and "
        "had reached through it, into the heart of Idoro itself, "
        "without needing the entity's permission, its knowledge, or "
        "its help at all."
    )},
    {"type": "body", "text": (
        "It thought of every thread it had ever judged not worth "
        "defending, every door it had let fall shut because keeping it "
        "open cost more than the entity believed it was owed, and felt "
        "the full, uncomfortable weight of a possibility it had never "
        "once considered across three centuries of careful bookkeeping: "
        "that nothing it had ever discarded had actually disappeared. "
        "It had simply been left lying in the open, waiting for "
        "someone more patient than the entity had ever needed to be to "
        "come along and pick it back up."
    )},
    {"type": "body", "text": (
        "The boy slept on, unaware that a woman who had once held him "
        "wet and screaming into the world had just walked three "
        "rivers back toward him for reasons neither she nor the entity "
        "yet understood, and the entity found itself, for the second "
        "time in as many weeks, keeping watch over a danger it could "
        "not name, could not measure, and could not yet decide whether "
        "to fear or simply, carefully, learn from."
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
    print("  THE DARK RISE — Episode 42: \"The Thread Not Cut\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_42.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_42.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
