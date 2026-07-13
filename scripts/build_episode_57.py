#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 57: "Asking Kindly"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-02: Episode 57 delivers the arrival the presence
warned of in Episode 56. The trading House's senior figure, known
only by his title, the Factor, reaches Idoro openly and peacefully,
requesting a formal council audience rather than sending armed men.
He disowns Ebiere as a rogue agent who exceeded her mandate, offers
reparations for the ambush, and speaks with a warmth that makes every
instinct Osadebe and the council have built this season feel almost
paranoid to hold onto. Remembering the sourceless warning relayed
through Chidebe's runner, the council answers patience with patience
rather than trust. The episode closes on the Factor's real request,
delivered gently enough that refusing it will look, to anyone
watching, like the village's fear rather than its wisdom: he asks
only to meet the boy himself, to see with his own eyes that peace
between his House and Oso is possible.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_57.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Fifty Seven"},
    {"type": "title_ep_name", "text": "Asking Kindly"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: NO SOLDIERS AT ALL
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "He came alone to the last boundary stone, on foot, unarmed, "
        "in plain traveling cloth rather than any mark of his House's "
        "wealth, and waited there patiently until Chidebe's watchers "
        "noticed him rather than announcing himself the way six armed "
        "men once had. \"I am called the Factor by those I work "
        "with,\" he told Chidebe when the captain finally approached "
        "him, his voice easy and unhurried. \"I have come to speak "
        "with your council, if they will have me, about a debt my "
        "House owes this village.\""
    )},
    {"type": "body", "text": (
        "Chidebe studied him a long moment, weighing the plain "
        "unarmed figure against everything the last season had taught "
        "him to fear from this House, and found himself, uncomfortably, "
        "with no obvious reason to refuse him. \"You will be watched "
        "the whole way,\" he said, \"and you will wait for the council's "
        "answer rather than assume it.\" The Factor inclined his head, "
        "unoffended. \"I would expect nothing less, given what your "
        "village has survived because of people wearing my House's "
        "name.\""
    )},
    {"type": "body", "text": (
        "Beneath the mango tree that afternoon, he spoke to the "
        "gathered council with the unhurried warmth of a man who had "
        "clearly done this many times before, in many places, and "
        "never once needed to raise his voice to be believed. \"Ebiere "
        "exceeded every mandate my House ever gave her,\" he said. "
        "\"Bribery. An armed party sent against a private family "
        "gathering. These were never sanctioned acts, and when my "
        "House learned of them, we recalled her at once and began the "
        "long work of understanding how far her failures had already "
        "reached.\""
    )},
    {"type": "body", "text": (
        "Amara, seated near Osadebe with Chidebe's runner's warning "
        "still fresh enough to shape every word she chose, asked the "
        "question the whole circle seemed to be holding back out of "
        "politeness. \"If she exceeded her mandate so badly, why does "
        "your House still want anything at all from a boundary that has "
        "already cost you men and coin and, it seems, one agent's "
        "reputation.\""
    )},
    {"type": "body", "text": (
        "The Factor smiled, and there was nothing in the smile that "
        "read, on its surface, as anything but genuine regret. \"A fair "
        "question, and one I would ask in your place,\" he said. \"My "
        "House trades in old stories where they prove true, and few "
        "stories in my lifetime have proven truer than what watches "
        "over your Oso. We do not want to fight it. We want, if it can "
        "be arranged, to understand it well enough to never make "
        "Ebiere's mistake again.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: THE ONE REQUEST
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe listened through all of it with the flat, careful "
        "attention of a man testing every gentle word against a warning "
        "he had chosen to trust without fully knowing its source. \"You "
        "have offered reparations, an apology, and a recalled agent,\" "
        "he said. \"All of that can be accepted plainly, and I intend "
        "to recommend the council accept it. What I have not yet heard "
        "you ask for in return, and a House as patient as yours rarely "
        "comes this far without asking for something.\""
    )},
    {"type": "body", "text": (
        "\"You are direct,\" the Factor said, and something in his "
        "easy manner sharpened very slightly, not into threat but into "
        "the particular attention of a man who respects having been "
        "seen clearly. \"Very well. I ask for one thing, and I ask it "
        "gently, understanding fully that you may refuse it. I would "
        "like to meet the boy. Not to take him. Not to test him, or "
        "study him, or bring him anywhere against his will. Only to "
        "look at him with my own eyes and be able to tell my House, "
        "truthfully, that peace between us and whatever guards him is "
        "possible.\""
    )},
    {"type": "body", "text": (
        "The circle beneath the mango tree went very quiet. Elder Maka "
        "spoke first, her old caution surfacing whole and unhurried. "
        "\"A request asked gently is still a request,\" she said. "
        "\"My grandmother's stories never once described a House that "
        "announced its hunger plainly. They only ever described houses "
        "patient enough to ask for exactly the smallest thing that, "
        "once given, made every larger thing after it feel inevitable.\""
    )},
    {"type": "body", "text": (
        "\"I understand the shape of that fear,\" the Factor said, \"and "
        "I will not pretend it is an unreasonable one to hold, given "
        "what your village has already survived. I will only say this. "
        "Refusing me costs you nothing today. But somewhere, eventually, "
        "if peace is ever to be more than an accident neither side "
        "meant, someone from my House and someone from that boundary "
        "will have to look at each other without a blade or a root "
        "between them. I would simply rather that first meeting happen "
        "on my House's most patient day than on its most desperate "
        "one.\""
    )},
    {"type": "body", "text": (
        "Ozoemena, who had said little through the whole exchange, "
        "finally spoke, his voice rough with the particular caution of "
        "a man who had once mistaken his own confidence for wisdom and "
        "paid for it in front of the whole village. \"That is the most "
        "honest threat I have ever heard dressed as a kindness,\" he "
        "said. \"You are telling us plainly that this ends in a "
        "meeting eventually, one way or another, and asking only "
        "whether we would rather choose the terms or have them chosen "
        "for us.\""
    )},
    {"type": "body", "text": (
        "The Factor did not deny it. \"I would rather you thought of "
        "me as honest than as gentle,\" he said. \"Gentleness is a "
        "performance easily abandoned. Honesty, offered plainly even "
        "when it costs me the appearance of kindness, is considerably "
        "harder to fake convincingly for as long as I intend for this "
        "understanding to last.\""
    )},
    {"type": "body", "text": (
        "Osadebe felt the presence's warning settle over the whole "
        "circle the way a held breath settles before it must finally be "
        "released, patience answered by patience rather than haste "
        "answered by trust, and understood, watching this quiet, "
        "unarmed, entirely reasonable man wait calmly for their answer, "
        "exactly what kind of hunger the warning had meant. \"We will "
        "need time to decide,\" he said. \"Not because your request is "
        "unreasonable on its face. Because a reasonable request is "
        "precisely the kind we have just been warned hardest against "
        "answering quickly.\""
    )},
    {"type": "body", "text": (
        "The Factor rose, unoffended, and bowed once more, the same "
        "easy, unhurried warmth he had arrived with entirely intact. "
        "\"Take whatever time you need,\" he said. \"I have already "
        "waited a great deal longer than this to reach a conversation "
        "worth having. A few more days will cost me nothing at all.\" "
        "He left the way he had come, on foot, unarmed, unhurried, and "
        "the whole council sat afterward in a silence that felt far "
        "heavier than anything his soft, reasonable words had actually "
        "contained."
    )},
    {"type": "body", "text": (
        "Amara was the first to break it, turning to the circle rather "
        "than to any single face in it. \"I did not hear a single word "
        "from that man I could point to and call a lie,\" she said. "
        "\"That frightens me considerably more than Ebiere's silence "
        "ever did. A liar can be caught eventually. A man who has "
        "simply decided to tell you only true things, arranged to lead "
        "you exactly where he wants, may never give either of us "
        "anything solid enough to refuse him on.\""
    )},
    {"type": "body", "text": (
        "Elder Maka nodded slowly, her old caution finding new company "
        "in the thought. \"Then we do not refuse him on the strength of "
        "a lie we caught,\" she said. \"We refuse him, if we refuse him "
        "at all, on the strength of a warning we chose to trust before "
        "we ever needed proof it was true. That is a harder thing to "
        "stand on in front of a man this reasonable, and also, I "
        "suspect, the only thing sturdy enough to hold.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: THE BOY'S OWN ANSWER
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe carried the whole exchange to Oso himself that "
        "evening rather than trust it to a relayed message, standing at "
        "the boundary while the entity listened through him the way it "
        "had learned to listen through anyone willing to stand close "
        "enough and speak plainly. When he finished, the entity was "
        "quiet long enough that Osadebe wondered if it intended to "
        "answer at all."
    )},
    {"type": "body", "text": (
        "\"He asked exactly the request the presence warned us to fear "
        "most,\" the entity said finally, relaying it to Chibundu in "
        "the same breath it gave Osadebe its answer. \"Small. "
        "Reasonable. Costly only if we say yes, and somehow costly in a "
        "different way if we say no. I do not yet know which cost is "
        "smaller.\""
    )},
    {"type": "body", "text": (
        "Chibundu, listening from the hollow, felt something in himself "
        "settle before he had even finished hearing the whole account, "
        "a certainty arriving the way his hardest questions always "
        "seemed to lately, without asking his permission first. \"I "
        "want to decide this one myself,\" he said. \"Not you deciding "
        "for me and telling me after. Not Osadebe deciding for the "
        "village without asking what I think. This is my meeting to "
        "have or refuse, if it happens at all.\""
    )},
    {"type": "body", "text": (
        "The entity felt the old instinct rise again, the same one it "
        "had set aside once already this episode, wanting badly to "
        "simply refuse on his behalf and end the danger before it could "
        "properly begin. \"You are asking to weigh a decision the "
        "presence itself warned could cost an entire ground everything, "
        "if it goes wrong,\" it said. \"I am not certain wanting to "
        "decide it yourself is the same as being ready to.\""
    )},
    {"type": "body", "text": (
        "\"Maybe not,\" Chibundu said. \"But you have spent this whole "
        "season teaching me that restraint and mercy are choices I have "
        "to make myself, not ones you can make for me and simply hand "
        "over already finished. I do not see why this should be "
        "different only because the danger is quieter this time than a "
        "blade.\""
    )},
    {"type": "body", "text": (
        "The entity had no honest answer to that which did not "
        "contradict everything it had spent months teaching him, and it "
        "understood, turning the boy's own words back over itself, "
        "that this was precisely the cost of having raised him to have "
        "a will of his own rather than simply an extension of its own "
        "caution. \"Then we will bring it to the council together,\" it "
        "said at last. \"Your voice in the room, not only mine speaking "
        "for you. Whatever Idoro decides, I would rather you be the one "
        "who helped decide it than the one it was decided about.\""
    )},
    {"type": "body", "text": (
        "Osadebe, still standing at the boundary hearing only the "
        "entity's half of the exchange, felt the weight of what was "
        "being asked of him land fully for the first time: not simply "
        "whether to trust the Factor's smile, but whether an entire "
        "village was prepared to let a boy not yet a season old in any "
        "way that mattered sit at the same table where his own fate "
        "would finally be decided by more than the adults who loved "
        "him."
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
    print("  THE DARK RISE — Episode 57: \"Asking Kindly\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_57.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_57.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
