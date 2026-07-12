#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 22: "The Petition"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-29: Episode 22 follows Ozoemena's first real obstacle:
he has authority but no knowledge of the old rites, and no one left in
Idoro who understands them as well as the woman he just helped remove
from power. He swallows his pride and goes to Elder Maka to demand her
knowledge, a scene thick with irony neither of them names aloud. Elder
Maka, to her own surprise, chooses honesty over spite, warning him
plainly how dangerous a clumsy rite against the dibia could be. In Oso,
the entity registers the exchange and reassesses the dibia's thread now
that real, if secondhand, knowledge might be brought against it. Back in
Idoro, Ozoemena turns his attention to Amara's household next, demanding
to see Kene for himself and question the family directly about what
really happened during the binding rite, reopening a wound the family
believed had finally closed.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_22.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Twenty Two"},
    {"type": "title_ep_name", "text": "The Petition"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: IDORO — WHAT OZOEMENA HAD TO ASK FOR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "It took Ozoemena two days to admit, even to himself, that "
        "authority alone would not be enough to do what he had promised "
        "the council he would do. He knew how to command men. He did "
        "not know a single word of the old rites well enough to use one "
        "safely, and there was only one person left in Idoro who did."
    )},
    {"type": "body", "text": (
        "He found Elder Maka exactly where Amara had found her days "
        "earlier, sitting alone in a compound going quietly to weed, and "
        "stood in her doorway with none of the certainty that had "
        "carried him through the council meeting."
    )},
    {"type": "body", "text": (
        "\"I need to know what you know,\" he said, without any "
        "greeting to soften it. \"About the dibia. About what a rite "
        "against a thread that old might cost, and how it is meant to "
        "be done properly.\""
    )},
    {"type": "body", "text": (
        "Elder Maka studied him for a long moment before answering, and "
        "something that might have been the ghost of her old authority "
        "passed briefly across her tired face. \"You took my standing "
        "in front of the whole village, and now you come to my door "
        "asking for the one thing my standing was actually worth.\""
    )},
    {"type": "body", "text": (
        "\"I did not take anything,\" Ozoemena said. \"The village took "
        "it, once it learned what you were carrying. I only stood up "
        "first.\""
    )},
    {"type": "body", "text": (
        "\"Yes,\" Elder Maka said. \"You are very good at standing up "
        "first. I have not yet decided whether that is a virtue or "
        "simply the only thing you know how to do.\""
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "She could have refused him. Some old, wounded part of her "
        "wanted to, wanted to watch him walk into the dibia's hut with "
        "nothing but confidence and come out having learned, the way "
        "she herself had once learned, exactly how much a careless rite "
        "could cost. She found, turning the temptation over, that she "
        "did not want another death added to a ledger that already held "
        "too many names she could not undo."
    )},
    {"type": "body", "text": (
        "\"The thread you want to sever was built slowly, over weeks, "
        "by something patient enough to have survived three centuries "
        "on this ground,\" she said. \"It will not come loose the way a "
        "green branch comes loose. If you go at it carelessly, you will "
        "not simply fail. You may tear something in the dibia that "
        "cannot be sewn back together, and you may draw more of the "
        "thing's attention than a man with no rites of his own to "
        "protect him can survive drawing.\""
    )},
    {"type": "body", "text": (
        "\"Then teach me the rites,\" Ozoemena said."
    )},
    {"type": "body", "text": (
        "\"I can teach you words,\" Elder Maka said. \"I cannot teach "
        "you, in the space of a few days, thirty and four years of "
        "learning when to trust them and when to walk away instead. I "
        "am telling you plainly, because no one else in this village "
        "will risk telling you at all: walk away from this one. The "
        "dibia has already paid enough. Do not make him pay for your "
        "need to prove yourself as well.\""
    )},
    {"type": "body", "text": (
        "Ozoemena's jaw tightened at that, the particular flinch of a "
        "man who has just heard the truest thing said to him in weeks "
        "and resents it precisely because it is true. \"The council did "
        "not give me authority so I could sit and do nothing, the way "
        "you sat and did nothing while the dibia's own apprentices fled "
        "this village and no one asked why.\""
    )},
    {"type": "body", "text": (
        "\"I did not do nothing,\" Elder Maka said, sharper now. \"I "
        "did what the rites I actually understood permitted me to do, "
        "and I have carried the cost of every one of those choices on "
        "my own body since, in ways you have not troubled yourself to "
        "ask about. Doing something reckless is not the same as doing "
        "something wise, whatever the difference looks like from where "
        "you are standing.\""
    )},
    {"type": "body", "text": (
        "The silence that followed held both of them a moment longer "
        "than either wanted, two people who had each spent their whole "
        "adult lives believing their own certainty was a form of "
        "protection, neither quite ready to admit how much that "
        "certainty had already cost the people around them."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: OSO — WHAT KNOWLEDGE, SECONDHAND, WAS WORTH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Beneath the ak-pu roots, the entity felt the shape of that "
        "conversation the way it felt every conversation that touched "
        "on its own threads now, a ripple moving through the fear it "
        "kept careful watch over, and weighed what it meant that real "
        "knowledge, however incomplete, was being offered to the man "
        "most likely to use it badly."
    )},
    {"type": "body", "text": (
        "Half remembered words, taught in haste by a woman still "
        "grieving her own authority, were a different danger than "
        "nothing at all. They were not, the entity judged, turning the "
        "risk over with its usual unhurried care, a danger equal to the "
        "old woman's own hands. A rite performed by someone who did not "
        "understand what he was reciting was closer to noise than to "
        "threat, more likely to injure the reciter than to touch "
        "anything the entity had actually built."
    )},
    {"type": "body", "text": (
        "It found itself, weighing the dibia's continued usefulness "
        "against the small, manageable risk of a clumsy attempt against "
        "him, still undecided which way that balance would eventually "
        "tip. There was no need to decide today. The vessel's own "
        "growth mattered more than one old, worn thread that had "
        "already given nearly everything it was ever going to give."
    )},
    {"type": "body", "text": (
        "It considered, too, the strange shape of the old woman's "
        "warning, offered freely to a man who had helped ruin her. "
        "Humans surprised it less often than they once had, after three "
        "centuries of watching the same handful of instincts repeat "
        "themselves across generation after generation, fear answered "
        "by cruelty, cruelty answered by more fear. And yet here was a "
        "woman choosing, for reasons the entity could not fully account "
        "for in its own flat arithmetic, to spend her last remaining "
        "credibility protecting the very man who had taken everything "
        "else from her. It filed the behavior away without a use for it "
        "yet, the way it filed away everything it did not immediately "
        "understand, trusting that understanding would arrive eventually "
        "if it simply kept watching long enough."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "In the hollow, the boy had begun stringing his single word "
        "into small, halting sentences, reaching for meaning the way he "
        "had once reached for balance on legs too new to trust, and the "
        "entity let the reaching continue, patient, curious in its own "
        "flat way about what shape the boy's mind would take once "
        "enough words existed inside it to build a self worth calling a "
        "self."
    )},

    {"type": "blank", "text": ""},

    {"type": "system", "text": "DIBIA THREAD: RISK REASSESSED, LOW TO MODERATE. DEFENSE DECISION: DEFERRED. VESSEL: EARLY SENTENCE FORMATION UNDERWAY."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: IDORO — WHAT OZOEMENA DEMANDED NEXT
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ozoemena left Elder Maka's compound with fewer words than he "
        "had hoped for and more doubt than he was willing to admit to "
        "carrying, and turned that doubt, as men like him often did, "
        "into a sharper need to prove himself somewhere the doubt could "
        "not follow him."
    )},
    {"type": "body", "text": (
        "He came to Amara's compound that same afternoon with two of "
        "his new followers standing close behind him, and did not "
        "bother with the courtesy of a greeting before speaking."
    )},
    {"type": "body", "text": (
        "\"I want to see the boy,\" he said. \"The one who was sealed. "
        "I want to hear, from your own mouths, exactly what happened "
        "the night Elder Maka worked that rite on him, because I intend "
        "to attempt something similar on the dibia, and I will not walk "
        "in blind the way she nearly walked in blind with you.\""
    )},
    {"type": "body", "text": (
        "Amara felt the old, familiar cold settle over her, the "
        "particular dread of watching a private wound reopened by "
        "someone with no idea how deep it had once gone. \"Kene is "
        "well,\" she said carefully. \"Whatever reached him is gone. "
        "There is nothing left to see.\""
    )},
    {"type": "body", "text": (
        "\"Then showing him to me costs you nothing,\" Ozoemena said. "
        "\"Unless there is something in the seeing you would rather I "
        "did not notice.\""
    )},
    {"type": "body", "text": (
        "Amara held his gaze without flinching, drawing on the same "
        "steadiness that had carried her through Elder Maka's own "
        "confrontation weeks earlier, though this time the ground "
        "beneath the confrontation felt less certain, a new man testing "
        "the edges of an authority he did not yet fully understand how "
        "to use. \"You may look at my son,\" she said. \"You will not "
        "touch him, and you will not speak to him as though he is proof "
        "of anything rather than a child who survived something that "
        "was done to him without his consent.\""
    )},
    {"type": "body", "text": (
        "One of Ozoemena's two followers shifted his weight, glancing "
        "toward the basket where Kene slept with the particular "
        "discomfort of a young man who had joined this cause for the "
        "certainty it promised and was only now beginning to feel the "
        "weight of what that certainty might actually require of him."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Obi stepped forward, his jaw set in the way Amara had learned "
        "to recognize as the last warning before his temper found its "
        "own voice. \"You have taken enough from this family's peace "
        "already just by standing in our yard uninvited. Ask your "
        "questions plainly, or leave.\""
    )},
    {"type": "body", "text": (
        "Ozoemena looked between them for a long moment, and something "
        "calculating moved behind his eyes, the same hunger for "
        "certainty that had carried him past a whole frightened council "
        "a week earlier. \"I will have my answers,\" he said. \"Today, "
        "gently, from a family the village still half trusts. Or later, "
        "less gently, once I have learned enough from the dibia to ask "
        "the questions a different way. The choice of which afternoon "
        "you would prefer is entirely yours.\""
    )},
    {"type": "body", "text": (
        "He left without waiting for an answer, his two followers "
        "trailing after him, and Amara stood in her own yard a long "
        "while afterward, feeling the particular exhaustion of a woman "
        "who had believed, for one brief week, that the worst of this "
        "danger had finally passed, only to learn that the shape "
        "threatening her family had simply changed hands, and grown "
        "hungrier for certainty than the last one ever was."
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
    print("  THE DARK RISE — Episode 22: \"The Petition\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_22.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_22.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
