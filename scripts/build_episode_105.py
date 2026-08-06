#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 105: "Not a Grave"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): searching the clearing's
edges rather than its dangerous heart, the party finds a concealed
structure built into the hillside, a rest camp rather than a burial
ground. It proves the presence's people were taken, not slaughtered
where they stood, opening a new and worse question for the presence:
taken where, and by whom, across three centuries of silence.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 105
EPISODE_TITLE = "Not a Grave"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Five"},
    {"type": "title_ep_name", "text": "Not a Grave"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Osadebe kept his word about the square. They struck camp at "
        "the clearing's edge, close enough to watch the standing stone "
        "from a careful distance and far enough, he hoped, not to "
        "provoke whatever still considered that stone worth tending. "
        "Morning found all four of them awake before the light was "
        "fully up, none of them having slept well, none of them saying "
        "so, each privately grateful the others had not asked."
    )},
    {"type": "body", "text": (
        "\"If this truly was a slaughter, there should be bones,\" Ifeanyi "
        "said over the last of their dried fish, working through the "
        "problem the way he worked through a hunt, out loud, piece by "
        "piece. \"Hundreds of people do not vanish without bones "
        "somewhere, even after three centuries. Bones outlast bowls.\" "
        "It was, Osadebe realized, exactly the question that had been "
        "sitting wrong in his own chest since the clearing first opened "
        "in front of them. There had been no bones anywhere in the "
        "ruined streets."
    )},
    {"type": "body", "text": (
        "They spent the morning working the clearing's perimeter "
        "instead of its center, mapping the tree line's unnatural "
        "restraint, and it was Okonjo, circling the western slope where "
        "the ground rose toward a low hill, who found the door. Not a "
        "ruin. A door, wooden, weathered gray but whole, set into the "
        "hillside itself and half hidden behind a fall of vine that had "
        "grown across it so slowly and so evenly it looked almost "
        "deliberate."
    )},
    {"type": "body", "text": (
        "\"Osadebe,\" he called, and something in the flatness of his "
        "voice brought the others faster than shouting would have. "
        "\"This is not part of the town.\" He was right. The door sat "
        "too far up the slope, too deliberately concealed, built into "
        "the hill rather than beside it, the work of someone who had "
        "wanted this place found by no one who was not already looking "
        "for it."
    )},
    {"type": "body", "text": (
        "Osadebe tested the door with the flat of his hand before his "
        "shoulder, half expecting it to resist three centuries of "
        "swelling and rot. It gave easily and without complaint, "
        "swinging inward on a hinge "
        "someone had oiled far more recently than three hundred years "
        "ago, into a low chamber cut back into the hillside, dry and "
        "cool and carefully kept."
    )},
    {"type": "body", "text": (
        "Inside, along walls lined with shelves cut straight into the "
        "rock, sat coils of rope, sealed clay jars, a row of iron tools "
        "none of the four recognized the exact use for, and, folded "
        "with a neatness that unsettled Emenike more than any ruin had "
        "yet managed, a stack of plain traveling cloth, undyed, the "
        "kind used to bind a person's wrists without marking the skin."
    )},
    {"type": "body", "text": (
        "Osadebe lifted one of the sealed clay jars from its shelf, "
        "turning it over once in the low light before setting it back "
        "down unopened. Wax still sealed its lid, dark and unbroken, "
        "and whatever sat inside had been packed with the same "
        "unhurried care as everything else in the chamber. \"Someone "
        "meant this room to be used again,\" he said. \"Not visited. "
        "Used. There is a difference, and I do not like which one this "
        "is.\""
    )},
    {"type": "body", "text": (
        "Okonjo stood in the doorway a moment longer than the others, "
        "looking back down the slope toward the ruined square below, "
        "as if measuring the distance a person could be moved between "
        "one and the other without ever leaving sight of home. It was "
        "not far. That, more than anything else in the chamber, seemed "
        "to trouble him most."
    )},
    {"type": "body", "text": (
        "Ifeanyi counted the iron tools along the far shelf without "
        "touching them, naming what he recognized under his breath the "
        "way a hunter names a trap he has walked past before without "
        "springing it. A short chain, coiled tight. A set of stakes "
        "worn smooth at one end from handling. He stopped at the last "
        "of them and did not name it at all, only stepped back a pace "
        "and let his silence answer for him."
    )},
    {"type": "body", "text": (
        "No one spoke for a long moment. It was Emenike, in the end, "
        "who said the thing none of the others wanted to be first to "
        "say. \"This is not a grave,\" he said, quiet, one hand resting "
        "on the folded cloth without lifting it. \"This is a rest camp. "
        "Somewhere to hold people, and feed them, and keep them alive "
        "long enough to move them somewhere else.\" He was thinking, "
        "though he did not need to say this part aloud either, of a "
        "walled courtyard downriver kept for exactly the same purpose, "
        "and of how old that particular cruelty apparently was."
    )},
    {"type": "body", "text": (
        "Ifeanyi ran a hand along the shelf's edge, where the dust lay "
        "thinner than it should have after three centuries, thin "
        "enough to suggest the shelves had been dusted, deliberately, "
        "sometime within living memory. \"Someone still keeps this room "
        "ready,\" he said. \"Ready for what exactly, I do not much "
        "want to guess.\" "
        "Osadebe closed the jars one by one without opening them, not "
        "yet willing to learn what they held, and gave the order to "
        "seal the door again exactly as they had found it, disturbing "
        "nothing they did not have to disturb."
    )},
    {"type": "body", "text": (
        "\"We are very likely not the first search party to walk this bearing,\" "
        "he said, once they were back outside in the ordinary light, "
        "his voice carrying the particular calm of a man forcing "
        "himself to sound calmer than the discovery deserved. \"We may "
        "not be the last, either, if whoever built that room is still "
        "in the business it was built for.\" Okonjo asked the question "
        "that hung over all of them. Was this room built for the "
        "presence's people, three centuries ago, or was it built more "
        "recently, for someone else entirely."
    )},
    {"type": "body", "text": (
        "Emenike answered anyway, though no one had asked him directly. "
        "\"It does not matter which,\" he said, his voice steadier than "
        "his face. \"If a House built this once, or found it already "
        "built and simply kept using it, the answer is the same either "
        "way. Someone has been doing this a long time, and getting "
        "better at it, and my sister is only the most recent name on a "
        "list that started centuries before she was born.\" None of the "
        "others argued the point, because none of them could find "
        "anything true to set against it."
    )},
    {"type": "body", "text": (
        "No one had an answer. Osadebe marked the hillside carefully on "
        "his map, alongside the standing stone and the buried wall, "
        "and beneath it wrote a single line he did not read aloud to "
        "the others: whoever holds Ijeoma may not be the first House to "
        "have used this exact bearing for exactly this purpose, and the "
        "presence's people may not have been the last to disappear "
        "along it either."
    )},
    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "That night, far to the east, Chibundu felt the presence's "
        "attention sharpen on something new, a grief laid over grief "
        "rather than the same wound reopening. He sat up against the "
        "iroko's roots as the feeling built, bracing the way he had "
        "learned to brace for it now, and waited for the presence to "
        "find words for whatever had just moved through it."
    )},
    {"type": "body", "text": (
        "\"They were taken,\" it said at last, and its voice had gone "
        "strange, almost bewildered, the voice of something forced to "
        "relearn its own history after three hundred years of believing "
        "it already knew the worst of it. \"Not killed where they "
        "stood. Held. Moved. I mourned a slaughter for three centuries "
        "when I should have been asking where they were taken to, and "
        "by whom, and whether any of them lived long enough afterward "
        "to be found.\""
    )},
    {"type": "body", "text": (
        "The entity's voice came carefully, the tone of something "
        "choosing each word before it let it out. \"You mourned the "
        "grief that was in front of you,\" it said. \"No one faults a "
        "person standing in wreckage for believing the wreckage is the "
        "whole story. It rarely is, and you had no way of knowing that "
        "then.\" \"I had three hundred years to wonder,\" the presence "
        "said, sharper than Chibundu had ever heard it speak to the "
        "entity before. \"Three hundred years, and I never once let "
        "myself ask whether wondering harder might have found this "
        "room sooner.\""
    )},
    {"type": "body", "text": (
        "Chibundu pressed his palms flat against the roots beneath him, "
        "grounding himself the way he had learned to when the "
        "presence's grief threatened to become indistinguishable from "
        "his own. \"You could not have walked this bearing,\" he said. "
        "\"You told me yourself, you can barely reach past Oso's own "
        "borders even now. The room was always going to have to be "
        "found by feet, not by grief.\" It was, he realized only after "
        "saying it, the same argument the entity had been making about "
        "restraint for three centuries, offered back now in the "
        "opposite direction, toward the power that had spent those same "
        "centuries wishing it had reached further rather than less."
    )},
    {"type": "body", "text": (
        "The presence was quiet a long while. \"Your search party found "
        "in two days what I could not let myself look for in three "
        "hundred years,\" it said finally, something that was almost, "
        "though not quite, gratitude threaded through the grief. \"I do "
        "not know yet whether that makes them braver than I was, or "
        "simply luckier than the men who tried before them and never "
        "came home to tell anyone what they found.\" It let the thought "
        "sit unfinished, and outside the shrine hut the night settled "
        "over Oso the way it always did, indifferent to how much had "
        "just changed inside it."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
