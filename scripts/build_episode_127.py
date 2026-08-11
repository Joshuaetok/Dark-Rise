#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 127: "What the Chaos Cost Them Both"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Ijeoma is recaptured in the
open ground beyond the wall and returned to a far harsher confinement.
The same night's unusual torchlight and activity, unexplained to the
search party watching from a distance, reads to them as an opening
worth the risk. Splitting into two pairs to scout the walls directly for
the first time costs Ifeanyi a real wound.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 127
EPISODE_TITLE = "What the Chaos Cost Them Both"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Seven"},
    {"type": "title_ep_name", "text": "What the Chaos Cost Them Both"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The hand on her arm did not let go, no matter how hard Ijeoma "
        "twisted against it, and a second set of hands closed around "
        "her a moment later, and then a third, until the open ground "
        "that had felt, for one impossible minute, like the whole "
        "world opening back up to her, closed instead into a tight, "
        "airless circle of torchlight and shouting voices."
    )},
    {"type": "body", "text": (
        "She did not fight further once the numbers made the fighting "
        "pointless. She had learned that lesson at the wall's bad "
        "corner two seasons ago and had not needed to relearn it since. "
        "What she did instead, walked back through the same gate she "
        "had crossed a rope to escape, was count, the same patient "
        "habit that had carried her this far carrying her now through "
        "the humiliation of being marched back inside in full view of "
        "every guard this House had left standing."
    )},
    {"type": "body", "text": (
        "The room she woke to the next morning was not the small room "
        "that had been her whole world for two seasons. It was smaller "
        "still, windowless, its single door fitted overnight with a "
        "second bar no ordinary latch could have explained, and the "
        "guard posted outside it did not leave his position even once, "
        "not for a meal, not for the hour her old counting had once "
        "promised her every guard eventually needed."
    )},
    {"type": "body", "text": (
        "She allowed herself, once, sitting alone on the cold floor of "
        "a room too small to properly pace, to mourn the rope itself, "
        "four dock shifts of careful theft undone in a single failed "
        "night, and the small rock crossing she would very likely never "
        "be permitted near again. She had solved the water. She turned "
        "that fact over slowly, the one true victory the night had "
        "actually given her, and found it was not nothing, even now, "
        "even here. She had proven the wall could be beaten. She had "
        "simply not yet proven she could beat everything waiting beyond "
        "it as well."
    )},
    {"type": "body", "text": (
        "No one came to question her. No one came to explain what her "
        "capture had actually cost the House to arrange, or what it "
        "would now cost her. The silence itself felt, to a woman who "
        "had spent two seasons learning to read every small change in "
        "this compound's own weather, considerably more dangerous than "
        "any shouted threat could have been."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE SEARCH PARTY
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe saw the torches first, a sudden bloom of moving light "
        "along the compound's northern edge well past the hour any "
        "ordinary watch should have needed reinforcing, and woke the "
        "other three without a word, pointing rather than speaking "
        "until he understood exactly what he was looking at."
    )},
    {"type": "body", "text": (
        "\"Something has happened inside that wall tonight,\" he said, "
        "low. \"I do not know what. I know only that a House this "
        "distracted, chasing something of its own through its own "
        "ground, is not a House watching its outer approaches the way "
        "it was watching them yesterday.\""
    )},
    {"type": "body", "text": (
        "\"You want to move on it,\" Ifeanyi said, reading the "
        "direction of the thought before Osadebe had finished shaping "
        "it into an order."
    )},
    {"type": "body", "text": (
        "Okonjo, still favoring the ankle that had never fully "
        "recovered its old confidence, hesitated before agreeing, "
        "turning over the same math the whole party had turned over "
        "since the clash. \"Splitting cost the crown its own search "
        "party more than once in the history Chidebe used to tell "
        "around the garrison fire,\" he said. \"I would rather we agree "
        "now on exactly how close is close enough, before any of us "
        "gets curious enough to forget the number.\""
    )},
    {"type": "body", "text": (
        "\"Close enough to see. Not close enough to be seen,\" Osadebe "
        "said. \"If that line blurs even once, whoever is closest to "
        "blurring it turns back immediately, no debate, no second "
        "look. I would rather lose the chance than lose the man.\""
    )},
    {"type": "body", "text": (
        "\"I want to learn what four days of careful watching has not "
        "yet let us learn,\" Osadebe said. \"Gate positions up close. "
        "Wall construction. Whether the ground close against that "
        "outer face offers any real cover at all. We split, two and "
        "two, circle the wall's opposite faces while its attention sits "
        "elsewhere, and we do not engage anything. We watch, closer "
        "than we have ever dared watch, and we come back before this "
        "chaos settles again.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Osadebe took Emenike toward the dock side, ground they had "
        "already studied from the ridge and trusted better than "
        "anything unfamiliar. Ifeanyi and Okonjo circled instead toward "
        "the compound's northern face, the same direction the torches "
        "had first bloomed from, drawn by the same instinct that had "
        "always served Ifeanyi best, that the most interesting ground "
        "was usually the ground still actively being disturbed."
    )},
    {"type": "body", "text": (
        "They found the wall's construction exactly as guessable as "
        "Osadebe had hoped, stone footed, timber topped, nothing a "
        "patient climber could not eventually solve given real time and "
        "real darkness. What they had not counted on, moving closer "
        "than any of the party had yet risked moving, was a second, "
        "smaller patrol thrown hastily onto the northern approach that "
        "same night, three men walking a tight new circuit born of "
        "whatever chaos had already gripped this House before the "
        "party ever reached the wall, a circuit no evening of distant "
        "watching had ever once revealed."
    )},
    {"type": "body", "text": (
        "Ifeanyi read the new patrol's rhythm within a handful of "
        "minutes, the same patient skill that had once found them a "
        "supply trail's own careless gap, and judged, wrongly for the "
        "first time in longer than either of them could remember, that "
        "a gap existed here too, wide enough for two careful men to "
        "slip past unseen toward the wall's own base."
    )},
    {"type": "body", "text": (
        "The clash was short and ugly, three trained men against two "
        "who had wanted only to look and had not planned to fight at "
        "all. Okonjo dropped the first attacker with a clean, "
        "economical strike that owed everything to weeks of Ifeanyi's "
        "own patient correction. It was Ifeanyi himself who paid for "
        "the second, a blade catching him low across the ribs before he "
        "could fully turn to meet it, deep enough to steal his breath "
        "and drop him hard against the wall's own stone footing."
    )},
    {"type": "body", "text": (
        "Okonjo put the second attacker down before the man could press "
        "the advantage further, and the third broke and ran rather than "
        "face two armed strangers alone in the dark, shouting an alarm "
        "that would not stay contained for long."
    )},
    {"type": "body", "text": (
        "\"Get up,\" Okonjo said, already hauling Ifeanyi's arm over his "
        "own shoulder, his voice tight with a fear he did not have time "
        "to feel properly yet. \"Get up, we cannot be here when that "
        "shout finishes traveling.\""
    )},
    {"type": "body", "text": (
        "\"I am up,\" Ifeanyi managed, though the words cost him more "
        "than they should have, one hand pressed hard against a wound "
        "already soaking through his own shirt. \"Move. I will keep "
        "moving as long as you keep me moving with you.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They reached Osadebe and Emenike's own rally point well past "
        "the worst of the alarm's spread, Ifeanyi gray faced and "
        "leaning hard on Okonjo's shoulder, and Osadebe's face, seeing "
        "the wound properly for the first time by weak moonlight, told "
        "Ifeanyi everything he needed to know about how serious the "
        "captain judged it to be."
    )},
    {"type": "body", "text": (
        "\"Deep,\" Osadebe said, working fast and steady to bind it "
        "properly, \"but clean. No organ, by the grace of whatever was "
        "watching over you tonight. You will not be running again for "
        "some days. You will very likely live to complain about that "
        "fact at length once the fear finally lets you.\""
    )},
    {"type": "body", "text": (
        "\"We learned something tonight, at least,\" Ifeanyi managed, "
        "through gritted teeth, refusing to let the pain have the last "
        "word entirely. \"That wall is guarded closer than it was four "
        "days ago. Whatever chaos we saw tonight, it did not make this "
        "House careless. It only moved its carefulness somewhere new.\""
    )},
    {"type": "body", "text": (
        "Osadebe said nothing to that, finishing the binding in grim "
        "silence, understanding, better than any of the other three "
        "yet fully understood, that a wounded man now slowed the whole "
        "party's every future choice, and that whatever chance tonight "
        "had offered them had cost more than any of them had walked "
        "into it expecting to pay."
    )},
    {"type": "body", "text": (
        "Emenike sat close beside Ifeanyi through what remained of the "
        "night, unwilling to let the man who had once set his own "
        "ankle by firelight sit alone with a wound this serious, and "
        "found himself thinking, watching Ifeanyi's own labored "
        "breathing steady slowly toward something closer to rest, of "
        "how easily tonight could have cost the party a life instead "
        "of merely a wound. He had asked, once, for this search to move "
        "faster whatever the cost. He understood now, sitting with the "
        "actual weight of that cost bleeding through a bandage inches "
        "from his own hand, precisely how much he had actually been "
        "asking the other three men at this fire to risk on his "
        "sister's behalf."
    )},
    {"type": "body", "text": (
        "\"Do not,\" Ifeanyi murmured, eyes still closed, catching the "
        "shape of the thought without needing to see Emenike's face to "
        "read it. \"Whatever guilt you are building for yourself in "
        "that silence, set it down. I chose to read that gap the way I "
        "read it. You did not put this blade in me. This House did, "
        "and this House is the only place that particular debt belongs, "
        "whatever else you have already quietly decided, sitting here "
        "in the dark, to carry all quietly and completely alone for "
        "yourself instead.\""
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
