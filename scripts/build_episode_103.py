#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 103: "Ground That Remembers Feet"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): the search party's second
day toward the presence's lost ground turns up the first unmistakable
trace of a vanished settlement, and Chibundu receives a sharper dream
fragment than any before. In Udo, Nkiruka reopens her Episode 94
archive fragment, the record that stops mid page, with new urgency now
that the search has reached the same bearing it describes.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 103
EPISODE_TITLE = "Ground That Remembers Feet"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Three"},
    {"type": "title_ep_name", "text": "Ground That Remembers Feet"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE SEARCH PARTY
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The sixth morning began the way the fifth had ended, with a "
        "silence so complete that Osadebe caught himself lowering his "
        "own voice without deciding to. They broke camp before full "
        "light, eager to close the one day the presence had promised "
        "still stood between them and whatever waited at the end of "
        "the bearing."
    )},
    {"type": "body", "text": (
        "It was Okonjo, of all of them, who found the first stone. He "
        "had stopped to reset a strap on his pack and put his hand down "
        "on what he took at first for a root, flat and hard beneath a "
        "skin of moss. It was not a root. It was worked stone, cut "
        "square by a hand and set level by a hand, laid into the earth "
        "so long ago that the ground itself had grown up around its "
        "edges like skin healing over a splinter."
    )},
    {"type": "body", "text": (
        "\"Osadebe,\" he called, and something in his voice, careful "
        "and low, brought the other three at a near run. \"Tell me "
        "this is nothing.\" Osadebe knelt and cleared moss from a "
        "second stone beside the first, then a third, and found beneath "
        "his hands the unmistakable, patient logic of a wall, laid "
        "course upon course, running away into the undergrowth in both "
        "directions."
    )},
    {"type": "body", "text": (
        "\"It is not nothing,\" Osadebe said, quiet, the words of a man "
        "revising everything he had believed about the empty country "
        "around him in the space of one sentence. \"Someone built here. "
        "Someone built here and then stopped, and the forest has spent "
        "longer covering it than any of us have been alive.\""
    )},
    {"type": "body", "text": (
        "They followed the buried wall for the better part of an hour, "
        "finding more of it the further they went, a corner here, a "
        "threshold stone there worn smooth in a shape no one could "
        "mistake for anything but a doorway. Ifeanyi walked with his "
        "head down and his shoulders drawn in, the posture of a man in "
        "a house where someone had died. \"This was a town,\" he said "
        "finally, his voice hushed the way it might have been inside a "
        "shrine. \"Not a camp. A town, with streets, and this wall "
        "held all of it in.\""
    )},
    {"type": "body", "text": (
        "Emenike said nothing for a long while, walking the doorway "
        "line with one hand trailing the buried stone the way a man "
        "might touch a scar to prove to himself it was real. He was "
        "thinking, though he did not say it aloud, that somewhere a "
        "long way south a wall just as real was holding his sister in "
        "instead of holding a town's grief out, and that the two walls "
        "did not feel as far apart from each other as the map between "
        "them suggested."
    )},
    {"type": "body", "text": (
        "Osadebe called a halt at midday, not because the light was "
        "wrong for walking but because he judged, correctly, that the "
        "four of them needed an hour to simply sit with what they had "
        "found before it changed the shape of the rest of the journey. "
        "He spread his map across his knees and began sketching the "
        "wall's run in careful strokes, adding a note in the margin he "
        "did not read aloud, that a settlement this size argued for "
        "hundreds of people once, not dozens."
    )},
    {"type": "body", "text": (
        "\"Hundreds of people do not simply vanish,\" Ifeanyi said, "
        "sitting with his back against the buried wall as though it "
        "might steady him. \"Not without someone somewhere still "
        "telling the story of where they went. Unless the story got "
        "buried along with the wall.\" Okonjo, unwrapping the last of "
        "the dried fish with careful, unhurried hands, said only that "
        "he had hunted enough abandoned villages in his life to know "
        "that silence like this one usually meant the story was too "
        "ugly for anyone left alive to want to keep telling it."
    )},
    {"type": "body", "text": (
        "Osadebe folded the map away and stood, brushing moss from his "
        "knees. \"Whatever silenced them, we are one day from standing "
        "in the middle of it,\" he said, his voice pitched level and "
        "steady for the others' sake more than his own certainty. "
        "\"Sleep while you can tonight. Tomorrow we finish what the "
        "boy's dream started.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: OSO — CHIBUNDU AND THE PRESENCE
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu slept badly that night, the way he had slept every "
        "night since the presence first named the bearing, and the "
        "dream that found him was sharper than any before it. He stood "
        "in a street he had never walked, between houses of packed "
        "earth roofed in dried leaf, and the street was full of people "
        "going about an ordinary evening, cooking fires lit, a child "
        "laughing somewhere out of sight."
    )},
    {"type": "body", "text": (
        "None of them looked at him. He understood, the way a person "
        "understands the rules of a dream without being told, that he "
        "was not truly standing among them. He was standing among what "
        "the presence remembered of them, worn soft and warm at the "
        "edges the way any old memory wears, kept safe inside "
        "something that had not let itself look at this street in "
        "three hundred years."
    )},
    {"type": "body", "text": (
        "\"This is what they took,\" the presence said, and its voice "
        "in the dream was not the low, careful thing it usually was "
        "when it spoke to him waking. It was younger. Grieving in a way "
        "that had nothing measured about it at all. \"Not a ground. Not "
        "a duty. This. An evening. A child laughing where I could hear "
        "her.\""
    )},
    {"type": "body", "text": (
        "It walked him further down the street, past a doorway where a "
        "woman sat working thread through her fingers by firelight, "
        "past two old men arguing over something that made them both "
        "laugh before the argument finished. Chibundu understood he was "
        "seeing them the way a person remembers a face they loved "
        "rather than the way a face actually looked, softened and "
        "warmed by three centuries of being turned over in the dark. "
        "None of it felt any less real for that."
    )},
    {"type": "body", "text": (
        "\"I do not know all of their names anymore,\" the presence "
        "admitted, and the admission cost it something Chibundu could "
        "feel even through the dream, a kind of wincing. \"I have kept "
        "the evening. I could not keep everything. Three hundred years "
        "is a long time to hold a street together with nothing but "
        "grief for mortar.\" The fires along the street guttered low all "
        "at once, and the dream began, gently, to end."
    )},
    {"type": "body", "text": (
        "Chibundu woke with his face wet and his heart going hard "
        "enough that he pressed a hand flat against his own chest to "
        "steady it. In the dark of the shrine hut, the entity's voice "
        "came low and unusually gentle, the tone it used only for him "
        "and only rarely. \"It has not shown anyone that street. Not "
        "me, not in three centuries of sharing this ground with it. "
        "Whatever the search party is walking toward tomorrow, it has "
        "decided you are the one it trusts to see it first.\""
    )},
    {"type": "body", "text": (
        "\"Why me,\" Chibundu asked, though some part of him already "
        "suspected the answer before he finished asking it. \"Because "
        "you asked it to stop protecting you from the truth,\" the "
        "entity said, \"and it has apparently decided to take you at "
        "your word, whatever that ends up costing either of you.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: UDO — NKIRUKA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Nkiruka had not opened the archive record in question since "
        "the day she first found it, filed where it had waited "
        "undisturbed for longer than her own tenure among the crown's "
        "keepers of old rites. She opened it again now with the "
        "courier's report from Osadebe still unrolled on the table "
        "beside her, its ink barely dry, describing a bearing the "
        "search party had reached that matched, line for line, the "
        "bearing named in the record's opening page."
    )},
    {"type": "body", "text": (
        "The record told of a border village, generations before any "
        "living memory, that had once discovered among its own people "
        "a man coerced into feeding information to hunters he feared "
        "more than he feared his own neighbors' judgment. The account "
        "described the village's response in careful, official "
        "language, and then, without warning or explanation, simply "
        "stopped. No conclusion. No note of what became of the village, "
        "the informant, or the hunters he had fed."
    )},
    {"type": "body", "text": (
        "She had read that silence before as an accident of "
        "preservation, pages lost to damp or fire or the ordinary "
        "carelessness of centuries. Tonight, with Osadebe's report in "
        "front of her and the bearing lining up too exactly to be "
        "coincidence, she found herself reading it instead as a "
        "different kind of silence. The kind a scribe leaves when the "
        "ending is not lost but unbearable to write."
    )},
    {"type": "body", "text": (
        "She checked the record's margins for a second time, the way "
        "she had checked them a dozen times before without finding "
        "anything, and this time noticed what she had always taken for "
        "an ink smear near the binding. Held close to the lamp, it "
        "resolved into a single small mark, hastily cut rather than "
        "written, a shape she recognized at once because she had seen "
        "its twin sketched fresh in Osadebe's own report from four days "
        "west. A spiral, buried in the gutter of a page no later scribe "
        "had ever thought to look at closely."
    )},
    {"type": "body", "text": (
        "Her hand went unsteady enough that she set the lamp down "
        "rather than risk it. Whoever had abandoned this record "
        "unfinished had known, or at least suspected, exactly what mark "
        "waited at the end of the story they could not bring themselves "
        "to write. That was not an accident of preservation. That was a "
        "warning, left the only way its author had dared to leave it."
    )},
    {"type": "body", "text": (
        "She did not sleep that night. By lamplight she copied every "
        "surviving word of the record twice, once for her own private "
        "study and once, though she had not yet decided whether she "
        "would ever hand it over, addressed and ready to be sent west "
        "to whichever of Osadebe's party might need to know, before the "
        "search reached whatever the first village's silence had been "
        "trying, in its own broken way, to warn them about."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
