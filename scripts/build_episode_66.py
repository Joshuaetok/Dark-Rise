#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 66: "The Ordinary Days Between"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-09-11: Episode 66 slows down deliberately, giving the
village's quieter threads room to breathe before the next escalation.
Kene, old enough now to notice the shape of what adults do not say
aloud, asks Amara and Obi a question about a brother he has never
been told he has. Elder Maka begins formally teaching Adaugo the old
rites and stories rather than simply repairing the distance between
them, a first real step toward naming a successor for knowledge that
nearly died with her. The episode closes on Zara, seeking out Elder
Maka rather than Amara this time, describing a second occurrence of
the cold, unfamiliar touch first felt in Episode 63, stronger now than
before — a quiet, human confirmation, unknown to either woman, that
whatever the presence and the entity have been dreading is no longer
merely approaching. It is getting close.
"""

import zipfile
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_66.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Sixty Six"},
    {"type": "title_ep_name", "text": "The Ordinary Days Between"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: THE QUESTION KENE FINALLY ASKED
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Kene had taken to standing at the edge of the compound in "
        "the evenings, watching the path toward the fields the way "
        "children watch for something they cannot yet name, and it was "
        "there that he finally asked the question Amara had been "
        "quietly dreading since the day he first learned to string "
        "more than two words together. \"Mama,\" he said, \"do I have a "
        "brother.\""
    )},
    {"type": "body", "text": (
        "Amara knelt to meet him at his own height, the way she had "
        "learned across two children now that some questions deserved "
        "a level gaze rather than one looking down. \"Why do you ask "
        "that,\" she said, gently, buying herself a moment to find the "
        "shape of an answer she had rehearsed in her head a hundred "
        "times without ever quite finishing it."
    )},
    {"type": "body", "text": (
        "\"The women at the well go quiet when I am near,\" Kene said, "
        "with the plain, unclouded observation of a child who notices "
        "everything and understands the significance of very little "
        "of it yet. \"And you and Papa look at the path some evenings "
        "the way you look at me when you think I am not watching. I "
        "thought maybe it meant someone else was supposed to be "
        "standing here too.\""
    )},
    {"type": "body", "text": (
        "Obi, listening from the doorway, stepped out to stand beside "
        "them both rather than let Amara carry the moment alone. \"You "
        "do have a brother,\" he said, before Amara could decide how "
        "much softening the truth required. \"His name is Chibundu. He "
        "does not live with us the way you live with us, and the "
        "reasons for that are complicated enough that we will explain "
        "them to you properly when you are old enough to hold the whole "
        "of it. But you asked a true question, and you deserve a true "
        "answer at least that large.\""
    )},
    {"type": "body", "text": (
        "Kene turned the name over with the same serious concentration "
        "he gave anything new, testing its shape in his mouth once, "
        "quietly, before looking back up at them both. \"Chibundu,\" he "
        "repeated, careful with each syllable the way he was careful "
        "with every new word lately, determined to own it properly "
        "before setting it down. \"Will I meet him,\" he asked, and "
        "Amara felt something in her chest ache at how simply he asked "
        "it, as though meeting a brother were the most natural thing "
        "in the world rather than a question that had already cost "
        "this family a year of grief to even begin answering."
    )},
    {"type": "body", "text": (
        "\"Is he bigger than me,\" Kene asked next, the practical "
        "curiosity of a small child already outpacing whatever solemn "
        "weight the adults around him were still carrying, and Obi "
        "found himself laughing, once, softly, grateful for a question "
        "small enough to actually answer without flinching. \"He is "
        "older than you by only a handful of minutes,\" he said, \"but "
        "he has had to grow faster than any child should have to. In "
        "some ways, yes. He is bigger.\""
    )},
    {"type": "body", "text": (
        "\"I hope so,\" Amara told him, honestly, unwilling to promise "
        "a timeline she did not control. \"I hope so very much. Until "
        "then, I want you to know that having a brother you have not "
        "met yet is nothing to be afraid of, and nothing to be ashamed "
        "of either, no matter what the women at the well go quiet "
        "about.\" Kene accepted this the way children accept most "
        "answers offered plainly, folding it away to be taken back out "
        "and examined again later, and returned to watching the path "
        "without further questions that evening."
    )},
    {"type": "body", "text": (
        "Later, once Kene had finally been coaxed to sleep, Obi found "
        "Amara still sitting at the doorway watching the same empty "
        "path their son had been watching earlier. \"He will ask "
        "harder questions eventually,\" he said. \"Whether it is fair "
        "that Chibundu carries what he carries and Kene does not. "
        "Whether it is fair that one brother was chosen and the other "
        "was left behind entirely by whatever the old law decided that "
        "night.\" Amara nodded slowly. \"Then we will answer those too,\" "
        "she said, \"the same way we answered this one. Plainly, and "
        "before he has to go looking for the answer somewhere less "
        "kind than his own parents.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: WHAT ELDER MAKA CHOSE TO PASS DOWN
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Elder Maka called Adaugo to her compound the next morning "
        "with a purpose she had not carried in longer than either of "
        "them could easily measure, setting out, on the mat between "
        "them, the small collection of carved markers and dried leaves "
        "she had once used to teach rites to no one but herself. \"I am "
        "going to teach you what my grandmother taught me,\" she said, "
        "\"properly, from the beginning, rather than in the frightened "
        "pieces I have handed you across arguments these past several "
        "seasons.\""
    )},
    {"type": "body", "text": (
        "Adaugo looked at the markers with an expression that mixed "
        "surprise and something warier underneath it. \"You have spent "
        "my whole life keeping this from me,\" she said. \"Why now.\""
    )},
    {"type": "body", "text": (
        "\"Because I nearly lost the chance to give it to you at all, "
        "several times over, and because this village has just spent a "
        "season learning that knowledge kept too closely guarded costs "
        "more than knowledge shared carefully,\" Elder Maka said. \"I "
        "do not know how many years I have left to teach you properly. "
        "I would rather begin today than assume tomorrow is promised to "
        "either of us.\""
    )},
    {"type": "body", "text": (
        "They worked through the morning slowly, Elder Maka naming "
        "each marker's old purpose, correcting Adaugo's grip on the "
        "carved stones with the same patient attention she had once "
        "given the boundary walk's disputed markers, and for the first "
        "time in longer than either of them could remember, the "
        "silence between them felt companionable rather than wounded."
    )},
    {"type": "body", "text": (
        "She showed Adaugo the marker for a binding rite next, the "
        "same knowledge she had once used, incompletely, to sever "
        "Kene's twin thread at the cost of a secret she carried alone "
        "for a season afterward. \"This one nearly killed me the last "
        "time I used it,\" she said plainly, no longer willing to teach "
        "half a history the way she had once been forced to live it. "
        "\"I want you to know exactly what it costs before you ever "
        "consider reaching for it yourself.\""
    )},
    {"type": "body", "text": (
        "Adaugo studied the marker with new weight in her hands, "
        "understanding for the first time in concrete terms what her "
        "mother had actually paid to save a stranger's son. \"You never "
        "told me it could cost this much,\" she said."
    )},
    {"type": "body", "text": (
        "\"I did not tell you many things it took this village nearly "
        "losing itself to finally pry out of me,\" Elder Maka said. \"I "
        "am not proud of how long that took. I am only glad I still "
        "have the chance to do this part differently.\""
    )},
    {"type": "body", "text": (
        "\"Will I ever use any of this,\" Adaugo asked eventually, "
        "turning one of the older stones over in her hands. \"The "
        "council settles most things now without needing a priestess "
        "at all.\""
    )},
    {"type": "body", "text": (
        "\"I hope you never need to,\" Elder Maka said. \"I hoped that "
        "for myself too, once, and I was wrong more than once in ways "
        "that cost people dearly. I would rather you carry knowledge "
        "you never have to use than need it someday and find your "
        "mother took it to her grave rather than risk teaching it to "
        "you sooner.\""
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # CODA: A SECOND COLD TOUCH
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Zara found Elder Maka rather than Amara that evening, an "
        "instinct she did not fully examine before acting on it, only "
        "trusting that the woman who had once carried a thread of her "
        "own without anyone's help might understand this particular "
        "fear better than a mother already carrying enough of her own. "
        "\"It touched me again,\" she said, without preamble. \"The cold "
        "one. Stronger this time.\""
    )},
    {"type": "body", "text": (
        "Elder Maka set down the marker still in her hand and gave "
        "Zara her full, undivided attention, the same stillness she "
        "had once brought to hearing Amara's hardest confessions. "
        "\"Describe it to me exactly,\" she said. \"Not the fear of it. "
        "The shape.\""
    )},
    {"type": "body", "text": (
        "\"It does not linger the way the entity's touch does, or "
        "settle in patiently the way the presence's does,\" Zara said. "
        "\"It arrives all at once, cold and total, tests something in "
        "me for the space of a single held breath, and leaves again "
        "before I can even finish being afraid of it. Tonight it "
        "stayed perhaps twice as long as it did the first time.\""
    )},
    {"type": "body", "text": (
        "Elder Maka absorbed that in a long, careful silence, turning "
        "it over against every old story her grandmother had ever "
        "given her, and found, at the end of that turning, nothing "
        "that matched it cleanly. \"I do not know what tests a person "
        "twice as long the second time as the first,\" she said finally, "
        "\"except a thing deciding, patiently, exactly how close it has "
        "already come.\""
    )},
    {"type": "body", "text": (
        "\"Should I be afraid,\" Zara asked, and Elder Maka, who had "
        "spent this whole season learning what honesty actually cost "
        "compared to comfortable silence, did not soften the answer "
        "she gave her."
    )},
    {"type": "body", "text": (
        "\"I do not know yet,\" she said. \"I know that this village "
        "has survived every danger so far by refusing to let a fear "
        "sit quietly in only one person's chest. I will carry this to "
        "the council myself in the morning, and you will not carry it "
        "alone one hour longer than tonight.\" Zara nodded, some of "
        "the night's cold finally loosening its grip on her shoulders, "
        "and the two women sat together a while longer, saying "
        "nothing further, letting the ordinary dark of the compound "
        "hold them both until the fear felt, for a little while at "
        "least, small enough to bear."
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
    print("  THE DARK RISE — Episode 66: \"The Ordinary Days Between\"")
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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_66.docx"))
        print(f"  Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_66.docx")
    except Exception as e:
        print(f"  Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
