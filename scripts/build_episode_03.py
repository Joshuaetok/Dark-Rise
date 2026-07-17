#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 3: "The First Lesson"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Written 2026-07-10: Episode 3 picks up one week after Episode 2. The entity has
sustained the child in Oso and begins teaching the vessel control and perception.
In Idoro, Amara's grief hardens into cold resolve; she begins gathering information.
The dibia is a prisoner in his own body, and the entity sends its first message
beyond the boundary.
"""

import zipfile
import os
import re
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_03.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
# Each element is a dict:
#   type: "title_page" | "heading" | "body" | "system" | "blank"
#   text: the paragraph text

EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode Three"},
    {"type": "title_ep_name", "text": "The First Lesson"},
    {"type": "page_break", "text": ""},

    # ── Episode body ──

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT ONE: OSO — ONE WEEK LATER / THE TEACHING BEGINS
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "A week passed. In Oso, the abandoned child did not die."
    )},
    {"type": "body", "text": (
        "He should have died six times over. Hunger should have taken him. "
        "Thirst should have taken him. The cold that never left the forest "
        "floor should have taken him. The creatures of the forbidden bush, "
        "the ones that came out at night, the ones without names, should "
        "have taken him."
    )},
    {"type": "body", "text": (
        "None of them did."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The entity sustained the vessel. Not with milk. Not with water. "
        "With something older than both. It fed the child on the ambient "
        "fear that saturated the soil of Oso. Centuries of terror pressed "
        "into the earth by every infant laid at the boundary before this "
        "one. Each of those small deaths had left a residue. The entity "
        "drank deep of that residue and passed it into the child like "
        "breath into a flute."
    )},
    {"type": "body", "text": (
        "The infant's body did not grow. It strengthened. The soft bones "
        "of a newborn hardened ahead of their time. The unfused plates of "
        "the skull knitted just enough to hold what was being poured "
        "inside. The eyes that had been wrong from birth became wronger "
        "still. The irises darkening toward black, the whites taking on "
        "the faintest shimmer, like oil on water."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The entity was patient. But patience had its limits. Three "
        "hundred years of sleep had been preparation. Now it was time to "
        "teach."
    )},
    {"type": "body", "text": (
        "You are not alone. You have never been alone. The rejection that "
        "put you here was the first gift. The hunger you feel is the "
        "second. Now you will learn what hunger is for."
    )},
    {"type": "body", "text": (
        "The infant could not understand words. That did not matter. The "
        "entity did not communicate in words. It communicated in images. "
        "Sensations. Truths pressed directly into the soft clay of an "
        "infant consciousness, not through ears but through the bond "
        "itself."
    )},
    {"type": "body", "text": (
        "It showed the child the village of Idoro as the entity saw it. "
        "From beneath. Strings of light connecting every living thing. The "
        "strings were food. The strings were pathways. The strings were how "
        "the entity had kept itself alive for three centuries, sipping from "
        "the edges of human fear like a man drinking dew from leaves."
    )},
    {"type": "body", "text": (
        "It showed the child the iroko tree above them. Not as a tree but "
        "as a door. A door that had stood closed for three hundred years. A "
        "door that was now opening, one hair's width at a time."
    )},
    {"type": "body", "text": (
        "It showed the child what waited on the other side of that door. "
        "The child's infant mind could not hold the full image. It was too "
        "vast. Too old. Too ravenous. But even the fragment was enough. The "
        "child's small body shuddered. The small fingers curled against the "
        "cold soil."
    )},
    {"type": "body", "text": (
        "Yes. That is what you will become. That is what we will become. "
        "Together."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In the branches of the iroko tree, a bird landed. It was the "
        "first bird to enter Oso in three hundred years. It stayed for "
        "three heartbeats. Then it fell from the branch, dead before it "
        "hit the ground."
    )},
    {"type": "body", "text": (
        "The entity had not meant to kill it. The entity was simply too "
        "much, too soon. That was the problem it had to solve. A vessel "
        "that could contain it. A body that could walk among the living "
        "without killing everything it touched."
    )},
    {"type": "body", "text": (
        "The child had to be taught control before the entity could be "
        "set loose."
    )},
    {"type": "body", "text": (
        "The first lesson had begun."
    )},

    {"type": "scene_break", "text": ""},

    # System alert block — sentence case for clean TTS; the caps run
    # property renders it all caps on the page.
    {"type": "body", "text": (
        "Inside Oso, the flat cold voice took its count."
    )},
    {"type": "system", "text": "Condition: bonding, week one. The vessel strengthens."},
    {"type": "system", "text": "Entity influence: localized. Contained within the Oso boundary."},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT TWO: IDORO — AMARA'S TRANSFORMATION / THE DIBIA'S PRISON
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Idoro, Amara had stopped speaking."
    )},
    {"type": "body", "text": (
        "It was not the silence of grief. Grief was loud. Grief wailed and "
        "tore its clothes and beat the red earth. Amara had done all of "
        "that in the first three days. Now she was doing something worse."
    )},
    {"type": "body", "text": (
        "She was watching."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She fed Kene. She bathed Kene. She held Kene when he cried. Her "
        "body performed every duty a mother's body was required to perform. "
        "But her eyes were calculating. Measuring. Storing up "
        "details like a woman building a case against an enemy who did not "
        "yet know she was an enemy."
    )},
    {"type": "body", "text": (
        "She watched Elder Maka's daily walk through the village, marking "
        "the hour the old woman passed her compound and the hour she "
        "returned. She watched the dibia's hut. No one had seen him in "
        "days. Apprentices brought food to the raffia door and took it "
        "away untouched. She watched Obi, who had become a shadow of "
        "himself. A man who went to the river but did not fish, who came "
        "home but did not speak, who slept beside her but did not touch "
        "her."
    )},
    {"type": "body", "text": (
        "She watched Kene most of all. Her living son. Her firstborn. He "
        "was healthy. He was beautiful. He was everything a mother should "
        "want."
    )},
    {"type": "body", "text": (
        "She looked at him and felt nothing."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "It was not his fault. She knew that. Part of her was still the "
        "old Amara. The woman who had laughed with Obi, who had sung to "
        "her belly during the long months of carrying, who had believed "
        "the world was hard but fair. That Amara knew this infant was "
        "innocent."
    )},
    {"type": "body", "text": (
        "But that Amara was buried now. Under the weight of what had been "
        "taken. Under the sound her second son had not made when they "
        "pulled him from her arms. Under the image of the dibia walking "
        "into the dark with her child and the old woman watching with "
        "stone eyes."
    )},
    {"type": "body", "text": (
        "The new Amara was being built from colder materials."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She began to ask questions. Quietly. Carefully. She asked Zara "
        "how many twins had been born in Idoro. Zara did not want to "
        "answer. Amara insisted."
    )},
    {"type": "body", "text": (
        "\"Four sets,\" Zara finally said. \"In my lifetime.\""
    )},
    {"type": "body", "text": (
        "\"And all were taken?\" Amara's voice stayed level, like a trader "
        "counting stock."
    )},
    {"type": "body", "text": (
        "\"All were taken,\" Zara said quietly."
    )},
    {"type": "body", "text": (
        "\"And the mothers?\" Amara asked, softer now."
    )},
    {"type": "body", "text": (
        "Zara looked away. That was answer enough."
    )},
    {"type": "body", "text": (
        "Amara filed this away. Every fact was a weapon. She did not yet "
        "know what war she was preparing for. She only knew that a war was "
        "coming, and she intended to be armed."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Three compounds away, the dibia sat in the dark of his hut and "
        "tried for the hundredth time to write what he could not speak."
    )},
    {"type": "body", "text": (
        "His hand would not obey him. The charcoal stick hovered over the "
        "dried palm leaf. His fingers trembled. Sweat dripped from his "
        "forehead onto the leaf, smearing the marks he had not yet made."
    )},
    {"type": "body", "text": (
        "He tried to write: The child is not an abiku. His hand made a "
        "mark. It was not a word. It was a shape. The same shape his blood "
        "had made in the divination water. A perfect dark circle."
    )},
    {"type": "body", "text": (
        "He tried to write: Something ancient has claimed him. His hand "
        "moved again. Another circle. Smaller. Inside the first."
    )},
    {"type": "body", "text": (
        "He tried to write: The law was wrong. His hand drew a third "
        "circle around the first two. Three rings. Like a target. Like an "
        "eye. Like a mouth."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The dibia threw the charcoal stick across the hut. It shattered "
        "against the mud wall. His apprentices flinched outside but did "
        "not enter. They had learned not to enter."
    )},
    {"type": "body", "text": (
        "He stared at the three circles on the palm leaf. He had not "
        "drawn them. Not really. Something had drawn them through him. "
        "Something that wanted him to know he was seen. Marked. Owned."
    )},
    {"type": "body", "text": (
        "He had delivered three hundred children to the boundary of Oso "
        "over forty years. He had believed, with the unshakable confidence "
        "of a man who had never been wrong, that he was serving the law. "
        "Protecting the village. Maintaining the old compact that kept the "
        "living safe from the dead."
    )},
    {"type": "body", "text": (
        "Now he understood. Every child he had left at the iroko tree had "
        "been a feeding. Not a severing. The law had not protected Idoro. "
        "The law had kept something beneath Oso alive just long enough to "
        "find the right vessel."
    )},
    {"type": "body", "text": (
        "And he had delivered that vessel himself."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "He pressed his face into his hands and wept without sound. "
        "Outside, the sun was shining. Children played in the red dirt. "
        "Women cooked over open fires. Men hauled nets from the delta "
        "waters. Idoro was having an ordinary day."
    )},
    {"type": "body", "text": (
        "Three miles away, something that used to be an infant was "
        "learning how to be a god."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════════════════
    # ACT THREE: OSO — THE FIRST MESSAGE BEYOND THE BOUNDARY / THE HOOK
    # ═══════════════════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Night fell over Oso. The entity had been teaching for seven days, "
        "and the child had absorbed more than most humans learned in a "
        "lifetime. It knew what fear tasted like. It knew that the "
        "boundary of Oso was not a wall of earth or stone. It was a wall "
        "of belief, centuries of human terror and ritual that declared "
        "nothing inside this place can leave."
    )},
    {"type": "body", "text": (
        "It knew that walls of belief could be eaten. Slowly. Patiently. "
        "From the inside out."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The child sat up."
    )},
    {"type": "body", "text": (
        "An infant of one week cannot sit up. The muscles are not formed. The "
        "spine is not ready. The brain does not yet know how to command "
        "the body into any position but lying flat."
    )},
    {"type": "body", "text": (
        "The child sat up. Its back was straight. Its head was steady. Its "
        "dark, shimmering eyes looked out at the twisted trees of Oso with "
        "an expression no infant face should be able to make. It was an "
        "expression of recognition. The entity was learning to use the "
        "body for more than breath."
    )},

    {"type": "scene_break", "text": ""},

    # System alert block — the progression
    {"type": "body", "text": (
        "The voice that owned the dark spoke, flat and exact."
    )},
    {"type": "system", "text": "Vessel status: first movement. Motor control exceeding infant norm."},
    {"type": "system", "text": "Boundary integrity: stable. Thinning at the iroko root line."},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Now. Now we send a message."
    )},
    {"type": "body", "text": (
        "The child raised one hand. The movement was slow. Deliberate. An "
        "adult gesture in an infant body. The small palm faced outward. "
        "The fingers spread. Nothing visible happened. No light. No sound. "
        "No fire from the sky."
    )},
    {"type": "body", "text": (
        "But at the boundary of Oso, three miles in every direction, "
        "every tree shivered. The cold ground warmed by a single degree. "
        "The birds that had not sung in three hundred years felt something "
        "pass through them. They opened their beaks. No sound came out."
    )},
    {"type": "body", "text": (
        "The message was not for the birds. It was not for the trees. The "
        "message was for the dibia."
    )},

    {"type": "scene_break", "text": ""},

    # ── The hook ──
    {"type": "body", "text": (
        "In his dark hut, the dibia's head snapped up. His eyes went wide. "
        "His mouth opened. Truly opened, for the first time since he had "
        "returned from Oso one week ago. The entity's grip on his voice "
        "loosened just enough. Just for a moment. Just for one word, "
        "barely a whisper, a rasp of air through a throat that had been "
        "sealed for seven days."
    )},
    {"type": "body", "text": (
        "\"Coming.\""
    )},
    {"type": "body", "text": (
        "His apprentices heard it through "
        "the raffia door. One dropped the clay pot he was carrying. It "
        "shattered on the ground. Then they ran. Not toward the hut. Away "
        "from it, into the village, into the dark, carrying nothing but "
        "the sound of their master's voice saying a word that made no "
        "sense and every sense at once."
    )},
    {"type": "body", "text": (
        "The dibia did not call them back. He could not. The grip had "
        "closed again, tighter than before. But his eyes were wet with a "
        "new quality of terror. The terror of a man who has just "
        "understood that the thing he feared was only the beginning."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "In Oso, the infant lowered its hand. The small body lay back "
        "against the softened ground where the roots cradled it. The dark "
        "eyes closed. The breathing slowed to the rhythm of an ordinary "
        "sleeping child."
    )},
    {"type": "body", "text": (
        "Tomorrow there would be another lesson. The day after that, "
        "another. And one day, not soon, but sooner than anyone in Idoro "
        "would believe, the lessons would end and the real work would "
        "begin."
    )},
    {"type": "body", "text": (
        "The child slept. The entity dreamed."
    )},
    {"type": "body", "text": (
        "And deep beneath the roots of the iroko tree, something that had "
        "been dead for three hundred years began to beat."
    )},
    {"type": "body", "text": (
        "Like a heart."
    )},

    {"type": "scene_break", "text": ""},
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
                   first_line_indent=None, spacing_before=0):
    """Create a w:p (paragraph) element.
    spacing_line=360 = 1.5 line spacing in twips (240 = single).
    spacing_after is in twips (120 twips ≈ 6pt).
    """
    p = make_element("p")

    # Paragraph properties
    pPr = make_element("pPr")

    # Spacing
    spacing_attrs = {
        f"{{{NS_WORD}}}after": str(spacing_after),
        f"{{{NS_WORD}}}line": str(spacing_line),
    }
    if spacing_before:
        spacing_attrs[f"{{{NS_WORD}}}before"] = str(spacing_before)
    spacing = make_element("spacing", spacing_attrs)
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

def make_body_paragraph(text, spacing_after=60, spacing_line=360,
                        spacing_before=0):
    """Create a body text paragraph with Georgia 12pt and first-line indent."""
    runs = [make_run(text, bold=False, font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment="left",
                          first_line_indent=360,
                           spacing_before=spacing_before)

def make_system_paragraph(text, spacing_after=120, spacing_line=360,
                          spacing_before=0):
    """Create a bold, all-caps system paragraph."""
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment="left",
                          first_line_indent=0,
                           spacing_before=spacing_before)

def make_blank_paragraph(spacing_after=0, spacing_line=360):
    """Create an empty paragraph for spacing."""
    runs = [make_run("", font_size=24)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line)


# ─── BUILD DOCUMENT XML ──────────────────────────────────────────────────────

# Vertical space (twips) inserted before the first paragraph of a new scene.
# 480 twips = 24pt: the page shows a clear scene break, but no empty
# paragraph exists for the TTS engine to turn into dead air.
SCENE_BREAK_SPACE = 480

def build_document_xml():
    """Build the word/document.xml content."""
    document = Element(
        qn("document"),
        {
            f"{{{NS_MC}}}Ignorable": "w14 wp14",
        }
    )

    body = SubElement(document, qn("body"))

    pending_scene_break = False

    for item in EPISODE_CONTENT:
        typ = item["type"]
        text = item["text"]

        if typ == "scene_break":
            pending_scene_break = True
            continue

        before = SCENE_BREAK_SPACE if pending_scene_break else 0

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
            para = make_body_paragraph(text, spacing_before=before)
            pending_scene_break = False
        elif typ == "system":
            para = make_system_paragraph(text, spacing_before=before)
            pending_scene_break = False
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

# --- LINT (TTS pacing, CLAUDE.md Section 3.10) ---

def lint_content():
    """Check narration text for TTS pacing violations."""
    problems = []
    for i, item in enumerate(EPISODE_CONTENT):
        if item["type"] not in ("body", "system"):
            continue
        text = item["text"]
        if "\u2014" in text or "\u2013" in text:
            problems.append(f"  item {i}: contains a dash: {text[:60]}")
        if "  " in text:
            problems.append(f"  item {i}: double space: {text[:60]}")
        if re.search(r"\w-\w", text):
            problems.append(f"  item {i}: hyphenated word: {text[:60]}")
    return problems


def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 3: \"The First Lesson\"")
    print("  Build Script")
    print("=" * 60)
    print()

    # Word count
    problems = lint_content()
    if problems:
        print("  LINT PROBLEMS:")
        for p in problems:
            print(p)
        print()
    else:
        print("  Lint clean: no dashes, double spaces, or hyphenated words")

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
        shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_03.docx"))
        print(f"  ✓ Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_03.docx")
    except Exception as e:
        print(f"  ⚠ Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
