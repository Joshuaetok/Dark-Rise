#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 31: "The Skeptic"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-08-07: Episode 31 follows Osadebe back to Udo, where he
delivers the account Eze Amadi asked him for: not a village's frightened
story, but a thing he witnessed directly, addressed to him by name. The
king convenes a small council to weigh the report, and Osadebe's account
runs immediately into Ejikeme, the crown's overseer of delta trade
concessions, whose livelihood depends on foreign trading Houses believing
the Oji Delta is a stable, unremarkable place to keep doing business. In
Oso, the entity continues its patient work entirely unaware of the exact
shape of the argument now unfolding a hundred miles north on its behalf.
The episode ends with Eze Amadi refusing to let the matter be quietly
buried, though not yet certain himself what doing otherwise will actually
require of his throne.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_31.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Thirty One"},
    {"type": "title_ep_name", "text": "The Skeptic"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: UDO — WHAT OSADEBE STOOD BEHIND
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe reached Udo nine days after leaving Idoro, and asked "
        "for an audience before he had even finished washing the road "
        "from his hands, a breach of ordinary court manners that told "
        "Ikwuano, receiving him at the gate, everything he needed to "
        "know about how the journey had gone."
    )},
    {"type": "body", "text": (
        "\"You were told to bring back only what you could stand "
        "behind with your own eyes,\" Ikwuano said, walking beside him "
        "toward the throne room. \"I have rarely seen a man look less "
        "eager to have succeeded at his task.\""
    )},
    {"type": "body", "text": (
        "\"I stand behind every word of it,\" Osadebe said. \"That is "
        "precisely the trouble.\""
    )},
    {"type": "body", "text": (
        "Ikwuano studied him a moment longer, the particular careful "
        "attention of a man who had spent twenty years learning to read "
        "exactly how much weight a report carried before it was ever "
        "spoken aloud. \"You have not slept properly since Idoro,\" he "
        "said. It was not a question."
    )},
    {"type": "body", "text": (
        "\"I have not slept properly since I stood at the edge of that "
        "forest,\" Osadebe said. \"I do not expect that to change soon. "
        "A man does not easily rest once he has learned that something "
        "he cannot fight knows his purpose before he has spoken it "
        "aloud.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Eze Amadi received him with only a handful of trusted "
        "advisors present, exactly as he had promised, and listened to "
        "the whole account without once interrupting, his face giving "
        "away less than Osadebe had hoped it might."
    )},
    {"type": "body", "text": (
        "\"It addressed you by nothing more specific than your "
        "purpose,\" the king said when Osadebe finished. \"Not your "
        "name.\""
    )},
    {"type": "body", "text": (
        "\"It did not need my name,\" Osadebe said. \"It knew why I "
        "had come before I ever spoke a word of it aloud, and it "
        "answered a question I had not yet found the courage to ask "
        "out loud myself. I have interrogated enough frightened men to "
        "know the difference between a story rehearsed for my benefit "
        "and a thing that simply happened in front of me. This was the "
        "second kind.\""
    )},
    {"type": "body", "text": (
        "He described the rest of it carefully, in the same measured "
        "voice he used to give any report, though Ikwuano noted the "
        "small tremor that entered his hands each time he came near the "
        "moment of the voice itself. The mother who had lived beside "
        "this for months without once breaking. The father who had "
        "once dreamed of walking that same path alone and never once "
        "imagined what waited past the tree line. The words themselves, "
        "delivered without any mouth to carry them, arriving instead "
        "the way a held breath arrives in a suddenly still room."
    )},
    {"type": "body", "text": (
        "\"You are certain it addressed the throne specifically,\" one "
        "of the other advisors asked, an older woman who oversaw the "
        "kingdom's western garrisons and had said little until now. "
        "\"Not merely you, as its messenger.\""
    )},
    {"type": "body", "text": (
        "\"It told me to tell my king,\" Osadebe said. \"I have served "
        "twelve years without once needing to guess at the meaning of "
        "an instruction that plain.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT THE ENTITY DID NOT YET KNOW IT HAD STARTED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity had already set the "
        "morning's message aside as spent, the way it set aside every "
        "act once its intended effect had been released into the "
        "world, and turned its full attention back to the slower, more "
        "patient work of the vessel's continuing growth."
    )},
    {"type": "body", "text": (
        "It did not trouble itself imagining the argument its own "
        "words might currently be starting a hundred miles north. Three "
        "centuries of patience had taught it that the shape of a "
        "message, once released, belonged to whoever received it, to "
        "carry and argue over and eventually act on however their own "
        "fear or ambition decided. It had done its part. Whatever grew "
        "from the seed now belonged to a garden it could not see and "
        "did not, for the moment, need to."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The vessel had begun, in these last days, repeating small "
        "phrases back to the entity unprompted, testing the shape of "
        "sentences the way he had once tested the shape of single "
        "words, and the entity found itself, watching this new "
        "development, once again setting aside the deeper question of "
        "how much of the boy's growing voice was still entirely its own "
        "to author."
    )},
    {"type": "body", "text": (
        "There was a kind of freedom in having finally spoken plainly "
        "to the wider world, one the entity had not fully anticipated "
        "when it made the choice at the boundary. For months it had "
        "spent its patience carefully, spreading its reach through "
        "Idoro one thread at a time, always weighing exposure against "
        "gain, always calculating how much of itself a single village "
        "could be allowed to glimpse before the glimpsing became a "
        "danger. That calculation had just changed shape entirely. The "
        "wider world already knew something of it now, whatever shape "
        "that knowledge eventually took at a distant throne. There was "
        "less left to protect by staying hidden, and, it found, "
        "turning the strange lightness of that thought over, perhaps a "
        "little more room now to simply attend to the one thing it had "
        "always cared about protecting more than its own secrecy."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "MESSAGE DELIVERY: COMPLETE, EFFECT UNKNOWN AND UNMONITORED. VESSEL: EARLY SENTENCE REPETITION, INCREASING FREQUENCY."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: UDO — WHAT EJIKEME ARGUED FOR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ejikeme, overseer of the crown's trade concessions along the "
        "delta, had said nothing through the whole of Osadebe's "
        "account, and Amadi's gaze finally settled on him with the "
        "particular patience of a king who already suspected what his "
        "silence had been building toward."
    )},
    {"type": "body", "text": (
        "\"Speak plainly,\" the king said. \"You have clearly been "
        "holding something back since the captain began.\""
    )},
    {"type": "body", "text": (
        "\"Plainly, then,\" Ejikeme said. \"The foreign Houses trading "
        "palm oil out of that delta send three ships a season through "
        "waters they already consider more trouble than they are worth. "
        "If word travels that the crown itself now believes a spirit "
        "speaks through village mouths and threatens royal captains at "
        "forest boundaries, those same Houses will find quieter rivers "
        "to trade along instead, and the tribute this kingdom collects "
        "from that trade will not travel with them out of courtesy.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "\"You would have me silence a captain's honest report to "
        "protect a trade agreement,\" Eze Amadi said, his voice flat "
        "enough that Ejikeme shifted where he stood."
    )},
    {"type": "body", "text": (
        "\"I would have you remember that this kingdom's granaries and "
        "this kingdom's soldiers are both paid for, in no small part, "
        "by tribute those same ships carry north every season,\" "
        "Ejikeme said, pressing further despite the king's tone, the "
        "particular stubbornness of a man who had built his entire "
        "position on being the one voice at court willing to say the "
        "unpopular arithmetic aloud. \"A story that frightens away that "
        "trade does not only cost the treasury. It costs every soldier "
        "whose wages depend on it, every road built with it, every "
        "season this throne has managed to keep its provinces fed "
        "without asking them to starve for want of coin.\""
    )},
    {"type": "body", "text": (
        "\"I would have you weigh a captain's single unwitnessed "
        "encounter against the certain cost of frightening away trade "
        "this kingdom already depends on,\" Ejikeme said. \"I do not "
        "call that silencing. I call it governing.\""
    )},
    {"type": "body", "text": (
        "\"He was not alone when it spoke,\" Osadebe said, sharper than "
        "he had spoken all morning. \"A mother and her husband stood "
        "beside me and heard every word I heard. I did not imagine a "
        "voice that three separate minds received at once.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The room fell silent, Ejikeme's argument suddenly thinner than "
        "it had sounded a moment earlier, and Eze Amadi rose from his "
        "seat with the air of a man who had already made his decision "
        "before the argument finished, and simply wished to let both "
        "sides finish speaking first."
    )},
    {"type": "body", "text": (
        "\"I will not bury a captain's honest witness to protect a "
        "season's tribute,\" the king said. \"Whatever this is, it has "
        "now spoken directly to the crown's own service. I cannot "
        "unhear that simply because hearing it costs me something to "
        "act on. Ejikeme, your concern for the Houses is noted, and I "
        "will not dismiss it lightly either. But this matter will be "
        "decided on what is true, not on what is convenient, and I have "
        "not yet decided what is true enough to act on plainly, nor "
        "what acting on it will ultimately require of any of us in this "
        "room.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "He dismissed the council without announcing what came next, "
        "and Osadebe left the chamber uncertain whether he had just "
        "watched a king protect the truth, or only postpone the moment "
        "when protecting it would cost far more than any of them in "
        "that room yet understood."
    )},
    {"type": "body", "text": (
        "Ejikeme lingered a moment longer than the others, and caught "
        "Osadebe's arm gently before he could follow the rest of the "
        "council out. \"I do not doubt what you saw, captain,\" he said, "
        "quieter now, all the performance gone out of his voice. \"I "
        "doubt only whether this kingdom can afford the truth of it "
        "handled carelessly. There is a difference between believing a "
        "thing and being wise about how loudly the believing is "
        "allowed to travel.\""
    )},
    {"type": "body", "text": (
        "\"That difference has already cost one village its dibia, its "
        "elder, and its peace,\" Osadebe said. \"I am not eager to learn "
        "what it costs a kingdom that decides to manage the truth "
        "instead of simply facing it.\""
    )},
    {"type": "body", "text": (
        "He left Ejikeme standing alone in the emptied chamber, and did "
        "not look back to see what expression the man wore once no one "
        "else remained to watch him wear it, or to guess at what a man "
        "that practiced at protecting his own interests might quietly "
        "decide to do next, now that the king's decision had not gone "
        "entirely his way."
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
    print("  THE DARK RISE — Episode 31: \"The Skeptic\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_31.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_31.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
