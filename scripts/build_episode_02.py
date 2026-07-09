#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 2: "The Hunger Beneath"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-09: Episode 2 picks up from the Episode 1 hook — the entity has
entered the abandoned child. This episode deepens the bond between entity and
vessel, shows the aftermath in Idoro, and establishes the dibia's growing terror
that something unprecedented is unfolding in Oso.
"""

import zipfile
import os
import re
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_02.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
# Each element is a dict:
#   type: "title_page" | "heading" | "body" | "system" | "blank"
#   text: the paragraph text

EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Two"},
    {"type": "title_ep_name", "text": "The Hunger Beneath"},
    {"type": "page_break", "text": ""},

    # ── Episode body ──

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: OSO — THE FIRST NIGHT AND THE BONDING
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The ancient presence had made its choice. It did not consume the "
        "child. It entered the child. And in the deep black of that first "
        "night in Oso, the bonding began."
    )},
    {"type": "body", "text": (
        "The entity had no name. Names were for things that could be "
        "summoned, controlled, bound. This thing could not be summoned. It "
        "had been old when the first human being knelt in the delta mud and "
        "prayed to a god it did not understand. It had slept for three "
        "hundred years beneath the roots of Oso."
    )},
    {"type": "body", "text": (
        "It was done sleeping."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The infant lay in its cloth bundle at the base of the ak-pu tree. "
        "The night was cold. The child should have been shivering. It was "
        "not. The child should have been crying. It was not. The child "
        "should have been dying. It was not."
    )},
    {"type": "body", "text": (
        "Inside the small body, the presence explored its new vessel. It "
        "moved through the infant's blood like smoke through water. It "
        "traced nerves that were still forming. It pressed against soft new "
        "bones and tested their give. It was gentle, in the way a sculptor "
        "is gentle with clay. Gentleness was not kindness. Gentleness was "
        "precision."
    )},
    {"type": "body", "text": (
        "The entity tasted what this child carried. Rejection. The mother's "
        "arms that had held him only once before they were pulled away. The "
        "father who had not spoken his name because no name had been given. "
        "The old woman's law that declared him a thing and not a person. It "
        "was all imprinted in the soft clay of an infant mind — a mark "
        "deeper than any ritual scar."
    )},
    {"type": "body", "text": (
        "The entity recognized this taste. It had been rejected too. Once. "
        "Long ago. Something had cast it out. Something had buried it here. "
        "Something had hoped it would never wake."
    )},
    {"type": "body", "text": (
        "That hope had been a mistake."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The bonding was not possession. Possession was crude — one will "
        "crushing another. This was fusion. The entity did not want to "
        "erase the child. It wanted to become the child, and it wanted the "
        "child to become something new. A vessel that could walk among the "
        "living. A vessel that could speak with a human tongue. A vessel "
        "that could be overlooked and underestimated until it was too late "
        "for overlooking to matter."
    )},
    {"type": "body", "text": (
        "The entity had waited three centuries. It could wait a little "
        "longer. But it was hungry."
    )},
    {"type": "body", "text": (
        "The hunger was not for food. It was for recognition. For the taste "
        "of worship that had once been its due before men learned to fear "
        "it. The old compact had fed it on the abandoned — dozens of "
        "infants over the decades, their small lives like drops of water on "
        "parched stone. Enough to keep it from fading. Not enough to let it "
        "rise."
    )},
    {"type": "body", "text": (
        "This child was different. Marked from the womb. Rejected by the "
        "living. Offered to the dead. A sacrifice made without a blade. The "
        "old compact said: receive the cursed and consume them. This child "
        "was not merely cursed. This child was an invitation."
    )},
    {"type": "body", "text": (
        "The entity fed on that. Not on the child's life. On the rejection "
        "that had delivered him here. On the law that wrapped him in ash "
        "marked cloth and laid him on cold ground. On the mother's screams "
        "and the father's silence and the old woman's stone face. Every "
        "human cruelty was fuel — and there had been so much cruelty, over "
        "so many centuries, all of it soaked into the soil of Oso. Now that "
        "fuel had a purpose."
    )},

    {"type": "blank", "text": ""},

    # System lines
    {"type": "system", "text": "CONDITION: BONDING — THE VESSEL AND THE ANCIENT ARE BECOMING ONE."},
    {"type": "system", "text": "HOST STATUS: MARKED — THE SECOND TWIN OF IDORO — TRANSFORMATION INITIATED."},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: IDORO — THE MORNING AFTER / THE DIBIA'S TERROR
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Dawn came to Idoro. The village woke to roosters crowing, women "
        "calling across compound walls, children laughing — children who had "
        "not been taken to Oso, children born alone and safe and blessed."
    )},
    {"type": "body", "text": (
        "In Amara's hut, only one infant cried."
    )},
    {"type": "body", "text": (
        "Kene wailed for milk and Amara gave it. Her body moved through the "
        "motions. Her arms held him. Her breast fed him. But her eyes were "
        "somewhere else — on the empty space beside her on the sleeping mat, "
        "the space where the second bundle should have been. Her arms ached "
        "for the weight that was not there. Her chest knew there should be "
        "two mouths to feed."
    )},
    {"type": "body", "text": (
        "It was a physical pain. Not grief. Grief required acceptance, and "
        "Amara had not accepted anything. This was the body of a mother "
        "screaming at the absence of her child, and the scream had no sound."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Outside, Obi sat against the mud wall where he had been all night. "
        "The cuts from his fingernails had scabbed over on his palms. He did "
        "not notice. Zara the midwife found him there."
    )},
    {"type": "body", "text": (
        "\"The boy,\" she said. It was not a question."
    )},
    {"type": "body", "text": (
        "\"Gone.\" Obi's voice was flat. Like water frozen over. "
        "He had done nothing. He had fallen to his knees and he had begged, "
        "but he had not fought. He had not grabbed the dibia by the throat. "
        "He had not snatched his son and run into the delta, into the bush, "
        "into the sea. He had done nothing, and that was what the law did. "
        "It killed something in the father too."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Elder Maka came at midday with her staff of dark polished wood "
        "and the weight of sixty years of enforcing the old law. She stood "
        "in the doorway. The sun behind her made her silhouette absolute."
    )},
    {"type": "body", "text": (
        "\"The child is gone?\""
    )},
    {"type": "body", "text": (
        "\"The child is gone,\" Zara said, because Amara would not speak "
        "and Obi could not."
    )},
    {"type": "body", "text": (
        "\"Good. The law has been served. You will nurse the firstborn and "
        "forget the second. The abiku was never yours. It was a test sent "
        "by the spirits. You have passed. You will be blessed.\""
    )},
    {"type": "body", "text": (
        "Amara looked up. It was the first time her eyes had moved from the "
        "wall since dawn. She did not speak. The look said everything: I "
        "carried him. I bled for him. He was mine before your law ever "
        "touched him. And you will answer for this."
    )},
    {"type": "body", "text": (
        "Elder Maka had seen that look before, on other faces, in other "
        "huts, in other years. She had outlived every woman who had ever "
        "looked at her that way. But something in Amara's eyes made the old "
        "woman pause."
    )},
    {"type": "body", "text": (
        "She turned away first."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "Three compounds away, the dibia had not left his hut since "
        "returning from Oso. His apprentices heard him through the raffia "
        "door — the click of cowrie shells, the rattle of bone and charm, "
        "the murmur of words in a language older than any human tongue "
        "still spoken aloud."
    )},
    {"type": "body", "text": (
        "He had thrown the shells a hundred times. He had cut his palm and "
        "let the blood fall into sacred water. He had burned herbs whose "
        "smoke revealed spirits. He had done everything a man of his "
        "training could do to read the will of the other side."
    )},
    {"type": "body", "text": (
        "The other side was not answering."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "He looked at the bowl. His blood had not spread into shapes the "
        "way blood divination required. It had formed a perfect sphere — a "
        "ball of darkness suspended in the clear water. It did not move. It "
        "did not dissolve. The dibia had delivered three hundred children. "
        "He had walked to the edge of Oso more times than he could count. "
        "He had never been afraid like this."
    )},
    {"type": "body", "text": (
        "Because he understood now. The secondborn was not an abiku. An "
        "abiku was small — a spirit child that tormented a single bloodline, "
        "something that could be warded and appeased. What he had carried to "
        "Oso was not small. Something ancient and patient and vast had been "
        "waiting beneath the roots of the twisted trees. And he had "
        "delivered a vessel straight into its waiting mouth."
    )},
    {"type": "body", "text": (
        "The law had not protected the village. The law had fed it."
    )},

    {"type": "blank", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: RETURN TO OSO — THE CHILD STIRS / THE HOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, the bonding had reached its first peak. Morning sun "
        "filtered through twisted branches. The light was weak. What reached "
        "the forest floor was not sunlight. It was the memory of sunlight."
    )},
    {"type": "body", "text": (
        "The child was warm. The cold of the night had not touched him. The "
        "ground around the ak-pu tree was warmer than the ground three feet "
        "away. The roots had shifted in the night — just enough to cradle "
        "the bundle. The tree knew what slept beneath it. The tree knew what "
        "had woken."
    )},
    {"type": "body", "text": (
        "The infant opened its eyes. The irises had darkened. The whites had "
        "cleared. There was a depth in them that no infant should possess — "
        "a depth that said someone was looking out, someone who understood "
        "what looking meant. The entity was learning to see through human "
        "eyes, and it found the world intoxicating."
    )},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The child's hand moved. It was not the random flailing of an "
        "infant. It was deliberate. The small fingers uncurled. They "
        "reached toward the ak-pu tree's trunk. They pressed against the "
        "bark."
    )},
    {"type": "body", "text": (
        "The tree shuddered. A tremor ran from root to branch. Green leaves "
        "fell — healthy leaves that should not have fallen, pushed from "
        "their branches by something that was testing what a human body "
        "could channel. Not much. Not yet. The infant form was fragile. The "
        "entity had to grow the vessel slowly, let the child's body "
        "strengthen, let the child's mind expand to hold what was being "
        "poured into it."
    )},
    {"type": "body", "text": (
        "Patience. The entity had patience no living thing could comprehend. "
        "But even the ancient could count the days."
    )},

    {"type": "blank", "text": ""},

    # System line — the transformation progresses
    {"type": "system", "text": "CONDITION: BONDED — THE FIRST THRESHOLD IS CROSSED."},
    {"type": "system", "text": "VESSEL STATUS: AWAKENING — THE CHILD BEGINS TO MOVE WITH PURPOSE."},

    {"type": "blank", "text": ""},

    {"type": "body", "text": (
        "The child made a sound. Not a cry. Not a hum. Something between. A "
        "sound a newborn should not have the breath to produce — a sound "
        "that held a tone beneath the tone, like two voices learning to "
        "speak as one."
    )},
    {"type": "body", "text": (
        "The sound traveled through the soil, through the roots, through "
        "the cold ground that never warmed under any sun. It reached the "
        "edge of Oso and pressed against the boundary like a hand against a "
        "door."
    )},
    {"type": "body", "text": (
        "The boundary held."
    )},
    {"type": "body", "text": (
        "It would not hold forever."
    )},

    {"type": "blank", "text": ""},

    # ── The hook ──
    {"type": "body", "text": (
        "In Idoro, the dibia burst through the door of his hut. His "
        "apprentices fell back. They had never seen their master like this. "
        "His eyes were wild. His hands shook. The cut on his palm was still "
        "bleeding. He did not seem to see them."
    )},
    {"type": "body", "text": (
        "\"Master? What has happened?\""
    )},
    {"type": "body", "text": (
        "The dibia opened his mouth. He had to warn them. He had to tell "
        "Elder Maka. He had to undo what he had done — impossible, you "
        "could not unfeed a hunger that had starved for three hundred years "
        "— but he had to try."
    )},
    {"type": "body", "text": (
        "He said nothing."
    )},
    {"type": "body", "text": (
        "His mouth moved. His throat worked. The words were there. They "
        "would not come out. Something was stopping him. Something wanted "
        "the village to go on with its ordinary day — children playing, "
        "women cooking, men fishing — while a power older than the kingdom "
        "grew stronger three miles from their walls."
    )},
    {"type": "body", "text": (
        "The dibia's mouth closed. His eyes filled with a fear that knew "
        "it was already too late."
    )},
    {"type": "body", "text": (
        "Deep in Oso, the infant smiled again. Not the reflex of a newborn. "
        "A message."
    )},
    {"type": "body", "text": (
        "The message was simple. Patient. Terrible."
    )},
    {"type": "body", "text": (
        "It said: I am coming."
    )},

    {"type": "blank", "text": ""},
]


# ─── OOXML HELPERS ────────────────────────────────────────────────────────────

# Namespaces
NS_WORD = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_RELS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_CONTENT_TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"
NS_MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
NS_RPR = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_VT = "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"

def qn(tag):
    """Return a tag with the Word namespace."""
    return f"{{{NS_WORD}}}{tag}"

def make_element(tag, attrib=None, text=None):
    """Create an XML element with the Word namespace."""
    el = Element(qn(tag), attrib=attrib or {})
    if text is not None:
        el.text = text
    return el

def make_run(text, bold=False, font_name="Georgia", font_size=24, caps=False):
    """Create a w:r (run) element.
    font_size is in half-points: 24 = 12pt.
    """
    r = make_element("r")
    rPr = make_element("rPr")

    # Font
    rFonts = make_element("rFonts", {
        f"{{{NS_WORD}}}ascii": font_name,
        f"{{{NS_WORD}}}hAnsi": font_name,
        f"{{{NS_WORD}}}cs": font_name,
    })
    rPr.append(rFonts)

    # Size
    sz = make_element("sz", {f"{{{NS_WORD}}}val": str(font_size)})
    rPr.append(sz)
    szCs = make_element("szCs", {f"{{{NS_WORD}}}val": str(font_size)})
    rPr.append(szCs)

    # Bold
    if bold:
        b = make_element("b")
        rPr.append(b)
        bCs = make_element("bCs")
        rPr.append(bCs)

    # All caps
    if caps:
        c = make_element("caps")
        rPr.append(c)

    r.append(rPr)

    # Text
    t = make_element("t", {"xml:space": "preserve"}, text)
    r.append(t)

    return r

def make_paragraph(runs, spacing_after=120, spacing_line=360, alignment="left",
                   first_line_indent=None):
    """Create a w:p (paragraph) element.
    spacing_line=360 = 1.5 line spacing in twips (240 = single).
    spacing_after is in twips (120 twips ≈ 6pt).
    """
    p = make_element("p")

    # Paragraph properties
    pPr = make_element("pPr")

    # Spacing
    spacing = make_element("spacing", {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    })
    pPr.append(spacing)

    # Alignment
    if alignment != "left":
        jc = make_element("jc", {f"{{{NS_WORD}}}val": alignment})
        pPr.append(jc)

    # First line indent (for body paragraphs)
    if first_line_indent:
        ind = make_element("ind", {f"{{{NS_WORD}}}firstLine": str(first_line_indent)})
        pPr.append(ind)

    p.append(pPr)

    for run in runs:
        p.append(run)

    return p

def make_title_paragraph(text, font_size=32, bold=True, alignment="center",
                         spacing_after=60, spacing_line=360):
    """Create a title-style paragraph."""
    runs = [make_run(text, bold=bold, font_size=font_size)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment=alignment)

def make_body_paragraph(text, spacing_after=60, spacing_line=360):
    """Create a body text paragraph with Georgia 12pt and first-line indent."""
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment="left",
                          first_line_indent=360)  # 0.25 inch indent

def make_system_paragraph(text, spacing_after=120, spacing_line=360):
    """Create a bold, all-caps system paragraph."""
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment="left",
                          first_line_indent=0)

def make_blank_paragraph(spacing_after=0, spacing_line=360):
    """Create an empty paragraph for spacing."""
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

def build_document_xml():
    """Build the word/document.xml content."""
    document = Element(
        qn("document"),
        {
            f"{{{NS_MC}}}Ignorable": "w14 wp14",
        }
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
            # Page break before next content
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

    # Add section properties for page size and margins
    sectPr = make_element("sectPr")
    # US Letter: 12240 x 15840 twips
    pgSz = make_element("pgSz", {
        f"{{{NS_WORD}}}w": "12240",
        f"{{{NS_WORD}}}h": "15840",
    })
    sectPr.append(pgSz)
    # 1-inch margins (1440 twips)
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
    """Create the .docx ZIP package."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Build document XML
    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        + tostring(build_document_xml(), encoding="unicode")
    )

    # Content Types XML
    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType='
        '"application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType='
        '"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '</Types>'
    )

    # .rels
    rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type='
        '"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"'
        ' Target="word/document.xml"/>'
        '</Relationships>'
    )

    # word/_rels/document.xml.rels
    doc_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '</Relationships>'
    )

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml)
        zf.writestr("_rels/.rels", rels_xml)
        zf.writestr("word/document.xml", doc_xml)
        zf.writestr("word/_rels/document.xml.rels", doc_rels_xml)

    return output_path


# ─── WORD COUNT ───────────────────────────────────────────────────────────────

def count_words():
    """Count words in all body and system paragraphs."""
    total = 0
    for item in EPISODE_CONTENT:
        if item["type"] in ("body", "system"):
            total += len(item["text"].split())
    return total


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 2: \"The Hunger Beneath\"")
    print("  Build Script")
    print("=" * 60)
    print()

    # Word count
    wc = count_words()
    print(f"  Word count: {wc}")
    if wc < 1550:
        print(f"  ⚠ WARNING: Under minimum (1,550). Need {1550 - wc} more.")
    elif wc > 2150:
        print(f"  ⚠ WARNING: Over maximum (2,150). Need to cut {wc - 2150}.")
    else:
        print(f"  ✓ Word count in range (1,550–2,150)")
    print(f"  Estimated duration: {wc / 130:.1f}–{wc / 150:.1f} minutes")
    print()

    # Build .docx
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_docx(OUTPUT_FILE)
    print(f"  ✓ Created: {OUTPUT_FILE}")
    print()

    # Copy to user outputs
    try:
        os.makedirs(OUTPUT_DIR_USER, exist_ok=True)
        import shutil
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_02.docx"))
        print(f"  ✓ Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_02.docx")
    except Exception as e:
        print(f"  ⚠ Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
