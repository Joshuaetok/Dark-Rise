#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 104: "What Grief Left Standing"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): the search party reaches
the presence's lost guardian ground itself. The ruin is preserved
wrong, warped by three centuries of grief bound into the land, and the
presence's reaction through Chibundu is the episode's emotional core.
The hook: a second spiral mark, cut into a standing stone at the
settlement's heart, far fresher than three centuries old.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 104
EPISODE_TITLE = "What Grief Left Standing"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Four"},
    {"type": "title_ep_name", "text": "What Grief Left Standing"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE SEARCH PARTY REACHES THE GROUND
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They came out of the tree line an hour past dawn, and Osadebe "
        "stopped walking before his mind had finished telling his feet "
        "why. Ahead of them, where the buried wall's line should have "
        "led into more forest, the forest simply was not there. In its "
        "place stood a wide clearing ringed by trees that had grown "
        "for three centuries without ever once encroaching on the open "
        "ground at their center, as though something had drawn a line "
        "the roots themselves knew better than to cross."
    )},
    {"type": "body", "text": (
        "Inside the clearing, a settlement stood in ruin, but wrongly, "
        "the way a body looks wrong laid out for burial in clothes "
        "still too clean for the grave. Walls that should have "
        "collapsed under three hundred years of rain stood at waist "
        "height, edges softened but unmistakably square. Roof frames "
        "long since stripped of their thatch still held their shape in "
        "packed earth, as if the houses had simply stopped being lived "
        "in one evening and had been waiting, patient and undecayed, "
        "ever since."
    )},
    {"type": "body", "text": (
        "\"Nothing here has finished falling down,\" Ifeanyi said, his "
        "voice gone thin, standing at the clearing's edge like a man "
        "asked to enter a room where someone had died recently rather "
        "than long ago. \"Three hundred years, and it looks like it "
        "happened last season.\" Okonjo did not answer him. He was "
        "staring at the ground itself, where grass grew in the streets "
        "but stopped short, always, of the doorways, as though even "
        "the grass understood which thresholds it was and was not "
        "permitted to cross."
    )},
    {"type": "body", "text": (
        "Emenike walked in first, before Osadebe could stop him, "
        "drawn by something he could not have named if asked. The "
        "silence inside the clearing was total in a way no bush "
        "silence had ever been, no birds, no insects, not even the "
        "small sounds of wind through leaves, as though sound itself "
        "had learned, generations ago, to stay outside the tree line "
        "with everything else that still belonged to the living world."
    )},
    {"type": "body", "text": (
        "Osadebe followed, then Ifeanyi, then Okonjo last, each of them "
        "moving the way soldiers move through a place they have been "
        "trained to respect and have never been trained for. They "
        "found what had once been a central square, wide and open, "
        "with the remains of a great meeting stone at its heart, and it "
        "was there, at the square's edge, that Osadebe's boot struck "
        "something that rang instead of thudding."
    )},
    {"type": "body", "text": (
        "He knelt and cleared three centuries of leaf litter from a "
        "standing stone, waist high, carved on its visible face with a "
        "spiral identical to the one they had copied from the fallen "
        "boundary marker days before. But this one was different in a "
        "way that emptied his stomach the moment he understood it. The "
        "cut lines were sharp edged. Clean. Not worn soft by weather "
        "the way three hundred years should have worn them."
    )},
    {"type": "body", "text": (
        "\"This was cut recently,\" Osadebe said, and heard his own "
        "voice come out steadier than he felt. \"Not this season, "
        "maybe not this year, but recently. Someone has stood in this "
        "square and cut this mark long after whatever happened here "
        "was already three centuries finished.\" Emenike crouched "
        "beside him, one hand hovering over the fresh cut without "
        "touching it, the same caution he had learned at the first "
        "stone. \"Someone still comes here,\" he said, low. \"Someone "
        "still tends it.\""
    )},
    {"type": "body", "text": (
        "Ifeanyi drifted toward the nearest standing wall while the "
        "other three studied the stone, and what he found there brought "
        "him back at a half run, his soldier's discipline for once "
        "losing to something closer to a boy's fear. Inside the "
        "doorway, on a shelf of packed earth that should have crumbled "
        "into the floor a hundred years ago, sat three clay bowls, "
        "unbroken, arranged as neatly as if a hand had set them down "
        "that same morning and simply forgotten to return for them."
    )},
    {"type": "body", "text": (
        "None of them touched the bowls. Okonjo said what all four "
        "were thinking without any of them wanting to be the one to "
        "say it first, that a house does not keep its bowls in place "
        "for three centuries by accident, that something in this "
        "clearing had been holding the whole settlement exactly as it "
        "fell, the way a hand holds a wound closed rather than letting "
        "it heal wrong."
    )},
    {"type": "body", "text": (
        "Osadebe called them together at the square's edge as the sun "
        "climbed toward midday. \"We do not camp inside tonight,\" he "
        "said, and no one argued the point. \"Whatever kept those "
        "bowls in place, whoever cut that mark, this ground does not "
        "belong to travelers passing through, and I would rather insult "
        "it from outside its walls than risk sleeping inside them.\" "
        "They spent the rest of the day working the clearing's edges "
        "instead, mapping what they could without crossing further into "
        "the square than the standing stone, and by evening Osadebe's "
        "sketch had grown into the most careful, most reluctant page in "
        "his entire journal."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: OSO — THE PRESENCE'S GRIEF
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In Oso, Chibundu felt it before he understood it, a pressure "
        "behind his ribs like grief arriving in someone else's body "
        "first and his own only after. He sat down hard against the "
        "iroko's roots, and the entity's voice reached him at once, "
        "urgent in a way it rarely allowed itself to be. \"Stay where "
        "you are. Whatever is happening, it is not happening to you.\""
    )},
    {"type": "body", "text": (
        "\"Then whose is it,\" Chibundu managed, though some part of "
        "him already knew. The answer came not from the entity but "
        "from the presence itself, and its voice, when it finally "
        "spoke, was barely a voice at all, more like something being "
        "held together by will alone. \"They are standing in my "
        "square,\" it said. \"After three hundred years of no one "
        "standing in my square, four living men are standing in it, "
        "and I do not know whether I have been waiting for this or "
        "dreading it, and I find I no longer have the strength to tell "
        "the two apart.\""
    )},
    {"type": "body", "text": (
        "Chibundu pressed both hands flat against the ground the way "
        "he had learned to when the presence's feeling threatened to "
        "overwhelm his own, and asked the only question that felt like "
        "it mattered. \"The mark they found. The fresh one. Do you know "
        "who cut it?\" The presence was quiet long enough that Chibundu "
        "thought it might not answer at all. \"No,\" it finally said. "
        "\"I have not been able to watch my own ground closely enough, "
        "for centuries, to know who still visits it. That failure "
        "belongs to me as much as anything else that happened here.\""
    )},
    {"type": "body", "text": (
        "The entity's voice returned, gentler now, aimed as much at the "
        "presence as at Chibundu. \"You did not fail by surviving what "
        "you could not stop,\" it said. \"I have told myself something "
        "close to that for three hundred years, about the dibia, about "
        "every death since I chose restraint over reaching. It is a "
        "lie that gets easier to tell and no truer for the practice.\" "
        "It was, Chibundu realized, the closest either power had ever "
        "come to comforting the other rather than merely coexisting "
        "with it."
    )},
    {"type": "body", "text": (
        "Chibundu asked, carefully, the question he had been circling "
        "since the pressure first hit his chest. \"What happened here. "
        "Not everything. Just enough that I understand what they are "
        "standing in the middle of.\" The presence took a long time to "
        "answer, long enough that Chibundu began to think it would "
        "refuse, the way it had refused for three centuries before he "
        "asked it to stop protecting him from the truth."
    )},
    {"type": "body", "text": (
        "\"It was fast,\" it said finally. \"Faster than grief usually "
        "allows itself to be understood while it is happening. One "
        "evening the street was full, the way I showed you. By the "
        "next evening it was not, and I was somewhere else entirely, "
        "spent past any strength I had, unable to reach my own square "
        "in time to do anything but arrive after and find it already "
        "quiet.\" It did not say the word taken again. It did not need "
        "to."
    )},
    {"type": "body", "text": (
        "\"You were somewhere else,\" Chibundu repeated, hearing the "
        "shape of an old wound in the words before he understood their "
        "meaning fully. \"They drew you away first.\" \"Yes,\" the "
        "presence said, and something in the single word carried more "
        "weight than anything else it had told him all morning. \"The "
        "same shape of trick your Mfoniso used against Kene. Take what "
        "a guardian will run toward, and the guardian empties its own "
        "ground running.\" The entity was silent at that, and Chibundu "
        "understood, without being told, that it was thinking of its "
        "own three centuries of choosing not to run toward anything at "
        "all."
    )},
    {"type": "body", "text": (
        "\"Tell them to be careful,\" the presence said at last, its "
        "voice steadying by degrees the way a person's does after "
        "weeping. \"If someone still tends that ground, someone still "
        "has reason to. And reasons three centuries old rarely turn out "
        "to be gentle ones.\" Chibundu promised he would find a way, "
        "though he had no idea yet how a warning shaped this vaguely "
        "was supposed to reach four men six days west with no way for "
        "him to speak to them directly except through whatever thin "
        "thread of dream still connected him to Emenike's sleeping "
        "mind."
    )},
    {"type": "body", "text": (
        "He lay back against the iroko's roots as the sun climbed "
        "higher outside the shrine hut, and for a long while neither "
        "power spoke again, the entity and the presence each holding "
        "their own private version of the same old grief, and Chibundu "
        "caught between them, learning, not for the first time, that "
        "some kinds of comfort could only ever be offered, never "
        "actually delivered in time to matter."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
