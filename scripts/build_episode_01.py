#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 1: "Born to Die"
Creates a properly formatted .docx file using only Python stdlib (no external deps).

Rewritten 2026-07-05: All character and place names optimized for AI voice-over
pronunciation — no consonant clusters, clear open-syllable patterns throughout.

Updated 2026-07-06: Pocket FM AI audio compliance pass — all hyphens removed
(firstborn, secondborn, spirit child, iyi uwa, close cut), numbers converted to
word form (Episode One), end markers removed from narration body per Section 2.5.

Updated 2026-07-17: TTS pacing restructure. Related sentences merged into full
paragraphs (a paragraph break reads as a long pause in AI narration; standalone
lines are now reserved for genuine dramatic peaks). Empty spacer paragraphs
replaced with scene_break markers that add spacing_before to the next paragraph
instead of emitting an empty paragraph. All em dashes removed from narration.
Dialogue lines carry tone cues before or beside the quote so the AI voice can
match the speaker's emotion.
"""

import zipfile
import os
import re
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

# ─── CONSTANTS ───────────────────────────────────────────────────────────────
OUTPUT_DIR = "/data/data/com.termux/files/home/dark-rise/episodes"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "The_Dark_Rise_Episode_01.docx")
OUTPUT_DIR_USER = "/mnt/user-data/outputs"

# ─── EPISODE CONTENT ─────────────────────────────────────────────────────────
# Each element is a dict:
#   type: "title_page" | "heading" | "body" | "system" | "scene_break" | "page_break"
#   text: the paragraph text
#
# Pacing rules (2026-07-17):
#   - One paragraph = one connected beat. TTS pauses longest at paragraph
#     breaks, so a standalone one-line paragraph is a deliberate dramatic
#     pause — use sparingly, only at peaks.
#   - "scene_break" emits no paragraph. It adds vertical space before the
#     next paragraph so the page shows the break but the voice does not
#     inherit stacked silences.
#   - Every dialogue paragraph carries a tone cue (whispered, cracked,
#     flat, dry) placed before or immediately beside the quote.

EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One"},
    {"type": "title_ep_name", "text": "Born to Die"},
    {"type": "page_break", "text": ""},

    # ── Scene one: the birth ──
    {"type": "body", "text": (
        "The night the twins were born, the moon hid its face."
    )},
    {"type": "body", "text": (
        "Amara's screams cut through the village of Idoro like a dull blade. "
        "Slow, ragged, wrong. She had been in labor since sunrise, and now it "
        "was deep night. The oil lamps in her hut burned low and threw shadows "
        "against the mud walls. Shadows that moved when they should not have "
        "moved."
    )},
    {"type": "body", "text": (
        "Zara the midwife pressed a damp cloth to Amara's forehead. Her old "
        "hands were steady. Her eyes were not."
    )},
    {"type": "body", "text": (
        "\"Push,\" Zara urged, her voice low and fierce. \"Again.\""
    )},
    {"type": "body", "text": (
        "Amara's back arched. Outside the hut, her husband Obi could hear "
        "everything. Every cry. Every silence between cries. Custom barred him "
        "from entering, and the silences were worse."
    )},
    {"type": "body", "text": (
        "Inside, the first child came. A boy with strong lungs. He wailed "
        "into the night and the sound was clean and good and alive. Zara "
        "lifted him, tied off the cord, and wrapped him in soft cloth the "
        "color of sunrise. A firstborn son. Amara wept with relief."
    )},
    {"type": "body", "text": (
        "Then she screamed again. Zara looked down, and her blood went cold."
    )},
    {"type": "body", "text": (
        "There was a second child."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene two: the dibia ──
    {"type": "body", "text": (
        "The dibia arrived before the second cord was cut. He was an old man. "
        "No one remembered his true name. They called him Dibia. He wore a "
        "necklace of cowrie shells and small bones that clicked when he "
        "walked. In forty years of prophecies, he had never run to a birth "
        "before this one."
    )},
    {"type": "body", "text": (
        "He pushed through the curtain and stopped."
    )},
    {"type": "body", "text": (
        "Zara held the second twin up. A boy. Smaller than his brother. His "
        "chest moved with breath, but he did not cry."
    )},
    {"type": "body", "text": (
        "His eyes were open."
    )},
    {"type": "body", "text": (
        "Newborns do not open their eyes. Not like that. Not looking at you. "
        "Not looking through you. Not with a stillness that made Zara's "
        "stomach knot like wet rope."
    )},
    {"type": "body", "text": (
        "\"Twins,\" Zara whispered, and the word landed like a stone in "
        "still water."
    )},
    {"type": "body", "text": (
        "In the Kingdom of Ijendu, twins were not a double blessing. They were "
        "a sign. A rupture in the natural order. The old law said: when two are "
        "born together, one belongs to the living and one belongs to the "
        "spirits. An abiku. A spirit child. A thing that would die and return, "
        "die and return, tormenting its bloodline until the family was ash."
    )},
    {"type": "body", "text": (
        "The law said the secondborn was the abiku. The law said the "
        "secondborn must be taken to the forbidden bush. The law said the "
        "secondborn must not return."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene three: Elder Maka's ruling ──
    {"type": "body", "text": (
        "Elder Maka came with the morning. She was the oldest woman in Idoro. "
        "She had enforced the old law for sixty years, and her face was a map "
        "of rulings she could not take back. Her wrappa was the deep red of "
        "dried blood. The morning sun caught the grey in her hair and made it "
        "look like a crown of iron."
    )},
    {"type": "body", "text": (
        "Amara held both boys against her chest. She would not look up."
    )},
    {"type": "body", "text": (
        "\"How many?\" Elder Maka asked. Her voice gave away nothing at all."
    )},
    {"type": "body", "text": (
        "\"Two,\" the dibia answered, choosing each word with care. \"Both "
        "male. The first cried strong. The second did not cry at all.\""
    )},
    {"type": "body", "text": (
        "Elder Maka went very quiet. \"The second opened his eyes?\""
    )},
    {"type": "body", "text": (
        "\"Before I cut the cord, Elder.\" The old man's voice began to "
        "shake. \"He opened his eyes and looked at me. I have delivered three "
        "hundred children. None of them looked at me like that.\""
    )},
    {"type": "body", "text": (
        "Elder Maka closed her eyes. When she opened them, something in her "
        "face had turned to stone. \"The law is clear,\" she said, and the "
        "words fell like a gate coming down."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene four: Obi pleads ──
    {"type": "body", "text": (
        "Outside the hut, Obi fell to his knees. He had been a strong man "
        "once. A fisherman who could wrestle a tarpon from the delta waters "
        "with his bare hands. He had survived storms that swallowed boats "
        "whole. Now his hands hung at his sides like dead things."
    )},
    {"type": "body", "text": (
        "\"Please.\" His voice cracked open into begging. \"She carried them "
        "both. She bled for them both. She nearly died bringing them into "
        "this world. You cannot ask her to give one back.\""
    )},
    {"type": "body", "text": (
        "Elder Maka did not look at him. She kept her eyes on the infant "
        "whose eyes were still open. Still watching."
    )},
    {"type": "body", "text": (
        "\"The law does not bleed,\" she said. \"The law does not love. The "
        "law protects the living from what the spirits send to test us.\" She "
        "turned to face Obi now, and her voice was not cruel. Cruelty would "
        "have been easier to bear. Her voice was sad. Sad and immovable. "
        "\"You know what happens to families who keep an abiku. You have "
        "seen.\""
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene five: what everyone had seen ──
    {"type": "body", "text": (
        "Everyone in Idoro had seen."
    )},
    {"type": "body", "text": (
        "There had been a family, three villages over, five years ago. They "
        "kept their abiku. They named her. They loved her. They defied the old "
        "law and Elder Maka herself. For three years, the thing wore the face "
        "of their daughter."
    )},
    {"type": "body", "text": (
        "Then the fever came. It took every child in the compound, one by "
        "one. Four small graves in four days. Then it took the parents. Then "
        "the grandparents. Then the house burned, and no one could remember "
        "who lit the fire."
    )},
    {"type": "body", "text": (
        "The old law was cruel. But the old law was old for a reason."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene six: the naming ──
    {"type": "body", "text": (
        "They named the firstborn Kene. It means thanksgiving. It meant: "
        "thank the spirits this one is ours to keep. Thank the spirits we "
        "only have to lose one. Thank the spirits for letting grief be "
        "partial."
    )},
    {"type": "body", "text": (
        "They did not name the secondborn."
    )},
    {"type": "body", "text": (
        "At dusk, the dibia wrapped the second twin in a cloth marked with "
        "ash and palm oil. Lines and circles. Symbols of severing. Symbols of "
        "returning what belonged to the other side. The child still had not "
        "cried, and his eyes were still open."
    )},
    {"type": "body", "text": (
        "He watched everything. The faces of the people who had already "
        "decided he was not a person. His stillness was not animal. His stillness was not human. "
        "It was the stillness of something waiting."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene seven: the taking ──
    {"type": "body", "text": (
        "Amara was held back by two village women. She fought them. She bit "
        "one hard enough to draw blood. She screamed words that had no shape, "
        "sounds that came from somewhere before language."
    )},
    {"type": "body", "text": (
        "Obi stood ten feet away. His face was wet. His fists were clenched "
        "so tight that blood dripped from his knuckles into the red earth."
    )},
    {"type": "body", "text": (
        "\"The child will not suffer,\" the dibia said. His voice was too "
        "smooth, like a thing recited many times. \"Oso takes quickly.\""
    )},
    {"type": "body", "text": (
        "This was a lie and everyone knew it."
    )},
    {"type": "body", "text": (
        "Oso was the forbidden bush. Three miles past the village boundary. "
        "A place where trees grew twisted, where roots broke through the soil "
        "like the fingers of buried things. A place where birds did not sing "
        "and the ground was always cold, even under a burning noon sun. "
        "Hunters walked the long way around it. Children learned its "
        "boundaries before they learned the names of their own grandparents."
    )},
    {"type": "body", "text": (
        "Abandoned infants did not die quickly there. They died slowly. From "
        "hunger. From thirst. From the cold. From whatever else lived in "
        "that place."
    )},
    {"type": "body", "text": (
        "The dibia began to walk. Amara's screams followed him for a mile "
        "before the forest swallowed them."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene eight: the boundary of Oso ──
    {"type": "body", "text": (
        "Oso was dark when the dibia reached its edge. The sky was the color "
        "of a bruise. The trees at the boundary leaned inward, branches "
        "interlaced like fingers woven in prayer. Or in warning."
    )},
    {"type": "body", "text": (
        "The dibia stopped."
    )},
    {"type": "body", "text": (
        "No one entered Oso. Not the dibia. Not Elder Maka. Not the "
        "Eze himself. The law said you left the child at the boundary. You "
        "did not step inside. What happened after that was between the child "
        "and whatever lived in the dark."
    )},
    {"type": "body", "text": (
        "He laid the bundle at the base of an iroko tree. The cloth was "
        "white, and in the fading light it glowed like a small ghost."
    )},
    {"type": "body", "text": (
        "The dibia turned. He walked away. He did not look back."
    )},
    {"type": "body", "text": (
        "If he had, he would have seen the bundle move."
    )},

    {"type": "scene_break", "text": ""},

    # ── Scene nine: the presence ──
    {"type": "body", "text": (
        "The child lay still. The forest was silent. Not the silence of "
        "night. Not the silence of sleep. The silence of a held breath. No "
        "insects sang. No wind stirred the leaves. The air was thick and "
        "still and waiting."
    )},
    {"type": "body", "text": (
        "Then the ground breathed."
    )},
    {"type": "body", "text": (
        "It was not a sound. It was a sensation. A slow exhale from beneath "
        "the roots. From beneath the soil. From beneath the bones of things "
        "that had died here long before the first village was built, before "
        "the first king was crowned."
    )},
    {"type": "body", "text": (
        "Something stirred. It had no shape. It had no name. It had been here "
        "since before the Kingdom of Ijendu had a name, since before the "
        "first human heart beat on this continent."
    )},
    {"type": "body", "text": (
        "It was old. It was patient. And it was hungry."
    )},
    {"type": "body", "text": (
        "The bundle twitched, and the infant inside made its first sound. Not "
        "a cry. A hum. Low and steady, like a plucked string held too long."
    )},
    {"type": "body", "text": (
        "The presence drew closer. It wrapped around the child like smoke, "
        "like water, like something that was neither. It tasted the life in "
        "the small body. It could have taken it. Should have taken it."
    )},
    {"type": "body", "text": (
        "That was the old compact. The forest gave nothing back. It received "
        "the cursed, the abandoned, the unwanted, and kept them. Dozens. "
        "Scores. More than anyone in Idoro remembered."
    )},
    {"type": "body", "text": (
        "But this child was different. This child had been marked from the "
        "womb. Rejected by the living. Offered to the dead before its first "
        "breath. That was a kind of sacrifice. That was a kind of invitation."
    )},
    {"type": "body", "text": (
        "The presence paused."
    )},
    {"type": "body", "text": (
        "It made a choice that would take three hundred years to unravel."
    )},

    {"type": "scene_break", "text": ""},

    # System alert block — herald, clipped alert lines, exit.
    # Text is sentence case for clean TTS; the caps run property renders it
    # all caps on the page. The paragraph pauses around these lines are a
    # feature here, not a bug — the voice should land each one separately.
    {"type": "body", "text": (
        "And then, for the first time in three centuries, a voice spoke "
        "inside Oso. It did not come from a mouth. It was flat and cold "
        "and exact, like something counting what it owned."
    )},
    {"type": "system", "text": "Condition: bound. The old compact is sealed."},
    {"type": "system", "text": "Host status: marked. The abandoned child of Idoro."},
    {"type": "system", "text": "Entity status: awakening. Three hundred years of silence. Broken."},
    {"type": "body", "text": (
        "Then the voice was gone, and the forest seemed to breathe again."
    )},
    {"type": "body", "text": (
        "The child's eyes were still open. They were no longer the eyes of a "
        "newborn. They were something else entirely."
    )},

    {"type": "scene_break", "text": ""},

    # ── Cut to the palace ──
    {"type": "body", "text": (
        "Three hundred miles away, Eze Amadi sat on the ancient throne of "
        "the Kingdom of Ijendu and heard nothing of this."
    )},
    {"type": "body", "text": (
        "The throne room was carved from white stone. Tapestries on the "
        "walls showed the conquests of dead kings. Men on "
        "horseback. Men with spears. Men kneeling. The colors had faded but "
        "the message had not."
    )},
    {"type": "body", "text": (
        "Courtiers moved in careful patterns around the dais. These were "
        "people who had survived decades in the palace. They did not survive "
        "by accident."
    )},
    {"type": "body", "text": (
        "Eze Amadi was sixty years old. He had ruled for twenty of them. His "
        "beard was grey and close cut. His robes were purple and gold. His "
        "eyes were the kind of tired that sleep could not fix."
    )},
    {"type": "body", "text": (
        "A messenger knelt before the dais."
    )},
    {"type": "body", "text": (
        "\"Rise,\" the Eze said, in the weary tone of a man performing a "
        "duty. \"Speak.\""
    )},
    {"type": "body", "text": (
        "The messenger's words came out in a nervous rush. \"Eze, the delta "
        "villages report strange signs. Fishermen near Idoro say the waters "
        "have gone still. No current. No fish. Elders say the trees in Oso "
        "have begun to grow toward each other. As if bowing to something at "
        "the center.\""
    )},
    {"type": "body", "text": (
        "The Eze's expression did not change. \"Fishermen talk,\" he said, "
        "dry as harmattan dust. \"Elders see omens in every change of "
        "weather. Is there anything real to report?\""
    )},
    {"type": "body", "text": (
        "The messenger hesitated. He had more to say. Something about a "
        "midwife who had stopped speaking. Something about a mother who had "
        "not stopped screaming. Something about a dibia who had locked "
        "himself in his hut. But he said none of "
        "this. You did not bring rumors to the throne. You brought facts. And "
        "facts could get you killed."
    )},
    {"type": "body", "text": (
        "\"No, Eze. Nothing real,\" the messenger said, and hated himself "
        "quietly for saying it."
    )},
    {"type": "body", "text": (
        "Eze Amadi waved a hand. The gesture said: this audience is over. "
        "The gesture said: the Kingdom has real problems. Trade disputes. "
        "Nobles who would put a knife in his back for the throne. He did not "
        "have time for ghost stories from fishing villages."
    )},
    {"type": "body", "text": (
        "The messenger backed away, his sandals making small sounds on the "
        "stone."
    )},
    {"type": "body", "text": (
        "The Eze did not know it, but he had just dismissed the only warning "
        "he would ever receive."
    )},

    {"type": "scene_break", "text": ""},

    # ── Return to Oso — the hook ──
    {"type": "body", "text": (
        "Far to the south, night had fully claimed the forbidden bush. The "
        "infant lay at the base of the iroko tree. The white cloth was soaked "
        "with dew. The air was cold."
    )},
    {"type": "body", "text": (
        "The presence had made its choice."
    )},
    {"type": "body", "text": (
        "It did not consume the child. It entered the child. Slowly. "
        "Deliberately. Like water finding its way through cracked stone. The "
        "infant's small body shuddered once. Then twice. Then stilled."
    )},
    {"type": "body", "text": (
        "When the child's eyes opened again, they were different. They held "
        "light that did not come from the moon. They held a darkness that did "
        "not come from the night. Something ancient and patient and terrible "
        "had found a vessel."
    )},
    {"type": "body", "text": (
        "And the child smiled."
    )},
    {"type": "body", "text": (
        "Newborns do not smile. This one did."
    )},
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
    spacing_after / spacing_before are in twips (120 twips ≈ 6pt).
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
                          first_line_indent=360,  # 0.25 inch indent
                          spacing_before=spacing_before)

def make_system_paragraph(text, spacing_after=120, spacing_line=360,
                          spacing_before=0):
    """Create a bold, all-caps system paragraph."""
    runs = [make_run(text, bold=True, font_size=24, caps=True)]
    return make_paragraph(runs, spacing_after=spacing_after,
                          spacing_line=spacing_line, alignment="left",
                          first_line_indent=0, spacing_before=spacing_before)


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


# ─── LINT ─────────────────────────────────────────────────────────────────────

def lint_content():
    """Check narration text for TTS pacing violations."""
    problems = []
    for i, item in enumerate(EPISODE_CONTENT):
        if item["type"] not in ("body", "system"):
            continue
        text = item["text"]
        if "—" in text or "–" in text:
            problems.append(f"  item {i}: contains a dash: {text[:60]}")
        if "  " in text:
            problems.append(f"  item {i}: double space: {text[:60]}")
        if re.search(r"\w-\w", text):
            problems.append(f"  item {i}: hyphenated word: {text[:60]}")
    return problems


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  THE DARK RISE — Episode 1: \"Born to Die\"")
    print("  Build Script (TTS pacing restructure, 2026-07-17)")
    print("=" * 60)
    print()

    # Lint
    problems = lint_content()
    if problems:
        print("  ⚠ LINT PROBLEMS:")
        for p in problems:
            print(p)
        print()
    else:
        print("  ✓ Lint clean: no dashes, double spaces, or hyphenated words")

    # Word count
    wc = count_words()
    print(f"  Word count: {wc}")
    if wc < 1550:
        print(f"  ⚠ WARNING: Under minimum (1,550). Need {1550 - wc} more.")
    elif wc > 2150:
        print(f"  ⚠ WARNING: Over maximum (2,150). Need to cut {wc - 2150}.")
    else:
        print(f"  ✓ Word count in range (1,550–2,150)")
    print(f"  Estimated duration: {wc / 150:.1f}–{wc / 130:.1f} minutes")

    # Paragraph stats
    bodies = [x for x in EPISODE_CONTENT if x["type"] == "body"]
    print(f"  Body paragraphs: {len(bodies)}")
    print()

    # Build .docx
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    build_docx(OUTPUT_FILE)
    print(f"  ✓ Created: {OUTPUT_FILE}")
    print()

    # Copy to user outputs
    if os.path.exists(OUTPUT_DIR_USER) or True:  # try anyway
        try:
            os.makedirs(OUTPUT_DIR_USER, exist_ok=True)
            import shutil
            shutil.copy(OUTPUT_FILE, os.path.join(OUTPUT_DIR_USER, "The_Dark_Rise_Episode_01.docx"))
            print(f"  ✓ Copied to: {OUTPUT_DIR_USER}/The_Dark_Rise_Episode_01.docx")
        except Exception as e:
            print(f"  ⚠ Could not copy to {OUTPUT_DIR_USER}: {e}")
    print()

    print("  Done.")
    return wc


if __name__ == "__main__":
    main()
