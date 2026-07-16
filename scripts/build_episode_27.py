#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 27: "The Empty Council"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-03: Episode 27 follows the immediate fallout from the
dibia's death. Idoro buries him, and the council that granted Ozoemena
his authority meets to decide what to do about a leader whose first real
act cost the village a life. Unlike Elder Maka, who was stripped of her
role by others, Ozoemena steps down before anyone needs to force him to,
the first real note of humility the village has seen from him. This
leaves Idoro in a position it has never faced before: no dibia, no Elder
Maka (marked and disgraced), no Ozoemena, no one left with any real claim
to lead it through what is still actively happening in Oso. In Oso, the
entity reviews the total collapse of Idoro's leadership as the cleanest
outcome the whole crisis has produced yet. Back in Idoro, out of options
and increasingly desperate, the council makes a decision that will finally
connect this village directly to the throne: they resolve to send word to
Udo asking for guidance, unaware that a report already sits waiting there
for exactly this kind of escalation.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_27.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Seven"},
    {"type": "title_ep_name", "text": "The Empty Council"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT OZOEMENA CHOSE FOR HIMSELF
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They buried the dibia two days later, in a grave dug at the "
        "edge of the compound he had served for longer than most of "
        "Idoro had been alive, and the whole village came, the same "
        "way it had come to watch him die, though the silence this time "
        "held grief instead of horror."
    )},
    {"type": "body", "text": (
        "Ozoemena stood at the very back of the gathering, apart from "
        "everyone, the cut at his temple healing into a thin scab that "
        "would leave a scar he would carry for the rest of his life, a "
        "smaller, more permanent version of the one Idoro's memory would "
        "carry about him."
    )},
    {"type": "body", "text": (
        "Adaugo stood near her mother for the first time since her own "
        "confrontation weeks earlier, not quite beside her, not quite "
        "apart, the two of them occupying the same uneasy distance that "
        "had settled between them since the truth came out. Grief, "
        "Amara noticed, watching them from across the gathering, had a "
        "way of pulling people back toward each other even when neither "
        "one had yet found the words to close the space fully."
    )},
    {"type": "body", "text": (
        "The burial itself was simple, the ground still soft enough "
        "from recent rain that the grave took shape quickly, and no one "
        "spoke the traditional words over it with any real conviction, "
        "as though even the oldest rites in Idoro's memory had been "
        "shaken loose by everything the village had watched happen to "
        "the man being buried beneath them."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The council convened that same evening, and Amara, invited "
        "this time rather than excluded, watched Ozoemena stand before "
        "them with none of the certainty that had once carried him past "
        "a whole frightened gathering in a single speech."
    )},
    {"type": "body", "text": (
        "\"I do not ask you to strip me of anything,\" he said, before "
        "any of the elders could speak first. \"I am stepping down "
        "myself, tonight, because a man who cost this village a life in "
        "his first real act of leadership has no honest claim left to "
        "keep leading it. I believed confidence could stand in for "
        "knowledge. I have learned, at a cost none of us can undo, "
        "exactly how wrong that belief was.\""
    )},
    {"type": "body", "text": (
        "No one argued with him. No one, Amara noticed, felt the need "
        "to add cruelty to a judgment he had already passed on himself "
        "more completely than the council likely would have managed on "
        "its own."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"You spoke truer tonight than you did the whole time you "
        "held this authority,\" one of the older women said, not "
        "unkindly. \"I only wish it had come a week earlier, when it "
        "might have cost us less to learn.\""
    )},
    {"type": "body", "text": (
        "\"So do I,\" Ozoemena said, and for once, no one in the room "
        "doubted that he meant it."
    )},
    {"type": "body", "text": (
        "He did not leave immediately after, lingering instead near "
        "the doorway as though uncertain whether he still had the "
        "right to be present for whatever the council decided next, and "
        "Amara found herself, watching him hesitate there, feeling "
        "something closer to pity than she had expected to feel for the "
        "man who had spent two weeks threatening her family."
    )},
    {"type": "body", "text": (
        "\"Stay,\" she said, surprising herself as much as him. \"You "
        "have paid enough tonight to have earned a voice in what comes "
        "after, even without the authority to decide it.\""
    )},
    {"type": "body", "text": (
        "He nodded, wordless, and took a seat at the very edge of the "
        "gathering, no longer the man certain his confidence could "
        "carry a whole village, but not yet entirely cast out of it "
        "either, a smaller, more uncertain shape than the one who had "
        "first risen to fill Elder Maka's empty seat two weeks earlier."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT A CLEAN COLLAPSE WAS WORTH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the iroko roots, the entity reviewed the whole shape "
        "of what these last weeks had produced with the particular "
        "satisfaction of a careful trader closing out a season's "
        "accounts and finding the balance better than expected."
    )},
    {"type": "body", "text": (
        "It had not needed to plan the sequence of it. It had only "
        "needed to be patient, to answer each new development with the "
        "smallest useful push, and let human fear finish the rest of the "
        "work on its own. Elder Maka, careful and knowledgeable, had "
        "fallen to a secret she chose to carry. Ozoemena, confident and "
        "ignorant, had fallen to a danger he refused to understand "
        "until it was already too late to matter. Between the two of "
        "them, Idoro had now exhausted every kind of leadership it knew "
        "how to produce, and had nothing left standing in the space "
        "where a dibia, an elder, and a self appointed successor had "
        "all once stood in turn."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "A village with no organizing authority at all was, in the "
        "entity's long accounting, the safest kind of village for its "
        "remaining threads to exist inside of. It turned its attention "
        "back to the vessel, whose small, unbidden reactions to distant "
        "human suffering it was still turning over, unresolved, a "
        "question it suspected it would need to answer honestly before "
        "very much more time passed."
    )},
    {"type": "body", "text": (
        "It had not counted, in any of its careful calculations across "
        "these past weeks, on the vessel's own growing sensitivity to "
        "distant human grief becoming a variable worth tracking in its "
        "own right. A tool that flinched at suffering it had never been "
        "taught to recognize as suffering was a tool developing "
        "something the entity had not deliberately planted, the same "
        "unclaimed grain it had first noticed the night the boy spoke "
        "his single unshaped word. It did not yet know whether that "
        "grain would grow into something useful, or into something that "
        "would eventually have to be pruned back by force. For now, it "
        "was simply another account left open, alongside all the others "
        "this long, patient season had left open."
    )},
    {"type": "body", "text": (
        "In the hollow, the boy sat quietly turning a smooth stone over "
        "in his small hands, an object he had found near the root wall "
        "days earlier and had not been parted from since, and the "
        "entity, watching him, found itself, not for the first time, "
        "wondering what shape a mind raised on this much careful "
        "shaping and this much unclaimed longing would eventually grow "
        "into, once shaping alone was no longer enough to contain it."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "IDORO LEADERSHIP: FULLY VACANT. NO REMAINING ORGANIZED THREAT TO ANY ACTIVE THREAD. RISK LEVEL: MINIMAL."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT THE COUNCIL DECIDED TO SEND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "With Ozoemena's seat empty and Elder Maka's name still too "
        "poisoned by revelation to speak aloud without an argument "
        "breaking out, the council sat late into the night circling the "
        "same unanswered question: who was left to lead a village that "
        "had just buried the last person who understood, even "
        "partially, what it was actually facing."
    )},
    {"type": "body", "text": (
        "\"None of us are equipped for this,\" one of the remaining "
        "elders said finally, an old man who had said little through "
        "the whole crisis and seemed to have aged years in the space of "
        "these last weeks. \"We buried our dibia. We disgraced our "
        "elder. We watched a confident fool bleed in the dirt for "
        "believing loudly was the same as knowing. I do not think Idoro "
        "has anyone left inside itself who can carry this further "
        "without costing us something we cannot afford to lose again.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The old man who had once challenged Elder Maka's judgment at "
        "Amara's compound spoke into the silence that followed. \"Then "
        "we look outside ourselves. Send word to Udo. Let the crown "
        "know what has happened here, and ask for whatever help a "
        "throne can offer a village too small to have ever troubled it "
        "before.\""
    )},
    {"type": "body", "text": (
        "A murmur of uneasy agreement moved through the gathered "
        "elders, the particular relief of frightened people finally "
        "handing a problem to someone, anyone, else. Amara said nothing, "
        "though she felt the old, familiar tightening return to her "
        "chest, the sense of a new danger finding its shape just beyond "
        "the edge of what anyone in that room could yet see clearly."
    )},
    {"type": "body", "text": (
        "\"Word travels slowly to Udo and slower still back,\" she said "
        "finally, when someone asked for her voice on the matter. \"By "
        "the time any answer reaches us, whatever is happening in Oso "
        "may already have decided the question for all of us.\""
    )},
    {"type": "body", "text": (
        "No one had an answer for that. The council sent the message "
        "anyway, because a frightened village reaching for a distant "
        "throne it barely believed would ever answer was still, in the "
        "end, easier than sitting inside its own fear with nothing left "
        "to reach for at all."
    )},
    {"type": "body", "text": (
        "Obi walked home beside her that night mostly in silence, and "
        "when he finally spoke, his voice carried the particular "
        "weariness of a man who had watched too many councils meet and "
        "too few of them settle anything for good. \"Do you think Udo "
        "will even answer,\" he asked."
    )},
    {"type": "body", "text": (
        "\"I think a throne answers whatever serves it eventually to "
        "answer,\" Amara said. \"Whether that happens before or after "
        "our son in Oso decides the rest of this for us is the only "
        "question I do not know how to guess at yet.\""
    )},
    {"type": "body", "text": (
        "They walked the rest of the way without speaking further, both "
        "of them carrying the same unspoken understanding that Idoro had "
        "just handed its fate to a distant king who did not yet know the "
        "village existed, while the true danger, patient and "
        "unhurried, continued growing exactly where it had always been "
        "growing, a mile beyond the fields neither of them could quite "
        "bring themselves to look toward anymore without feeling the "
        "old, familiar ache return, no matter how many councils met or "
        "how many messages rode north to Udo in search of an answer."
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
    print("  THE DARK RISE — Episode 27: \"The Empty Council\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_27.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_27.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
