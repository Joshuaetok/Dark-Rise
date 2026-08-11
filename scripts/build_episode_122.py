#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 122: "The Quiet Finally Breaks"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): A Concern tracking patrol,
following the wounded courier's blood trail, finds the search party's
new position and forces an open clash. Stealth is gone for good. In the
same stretch of days, the Warden collapses Mfoniso's fourteen day
allowance into a hard, non negotiable three, unwilling to keep waiting
while her own compound feels less safe by the day. Act Three closes on
two clocks now running at once, neither side aware of the other's.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 122
EPISODE_TITLE = "The Quiet Finally Breaks"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Two"},
    {"type": "title_ep_name", "text": "The Quiet Finally Breaks"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE SEARCH PARTY
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They heard the patrol before they saw it, the deliberate, "
        "unhurried tread of men who were not merely walking but "
        "actively reading the ground the way Ifeanyi himself read it, "
        "and Osadebe understood, in the half second it took the sound "
        "to register fully, exactly what a House with trackers of its "
        "own would eventually do with a wounded man's blood trail and a "
        "missing partner."
    )},
    {"type": "body", "text": (
        "\"They followed him back out,\" Ifeanyi said, already moving "
        "them off the ridge and down toward denser cover, his voice low "
        "and fast. \"Not guessing. Tracking. Whoever is behind us has "
        "read the same ground I would have read.\""
    )},
    {"type": "body", "text": (
        "They had moved twice since the ambush, first to the hidden "
        "position Osadebe had chosen the same evening the wounded "
        "courier fled, then again the following dawn when Ifeanyi "
        "judged even that ground too close to the trail for real "
        "safety. Neither move had felt, at the time, like running. "
        "Standing now with the tracking patrol's deliberate footsteps "
        "closing behind them, Osadebe understood that running was "
        "exactly what it had always been, and that it had simply, "
        "finally, run out of new ground to spend."
    )},
    {"type": "body", "text": (
        "Six men broke from the tree line a hundred paces behind them, "
        "armed and spread in a deliberate hunting line rather than a "
        "casual patrol's loose cluster, and any hope Osadebe still "
        "carried that this might pass as a chance encounter died the "
        "moment the lead tracker raised a hand and the whole line "
        "quickened toward them without a single wasted word."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"Break for the ravine line,\" Osadebe called, already moving, "
        "\"and do not stop to fight unless the ground stops you first.\" "
        "It was, he understood even shouting it, a plan built more on "
        "hope than certainty, four men who knew this exact stretch of "
        "forgotten country only slightly better than the six men who "
        "had probably walked it a hundred times before them."
    )},
    {"type": "body", "text": (
        "The gap closed faster than any of them wanted it to. Two "
        "trackers cut the angle sharp through a stand of close set "
        "trees and came out ahead rather than behind, forcing Emenike "
        "and Okonjo to turn and meet them rather than outrun them, "
        "steel ringing against steel in a clearing far too small for "
        "four men to fight comfortably in at once."
    )},
    {"type": "body", "text": (
        "Emenike took the first man down with a wound rather than a "
        "kill, a hard cut across the sword arm that ended the fight "
        "before it truly began, and had no time at all to feel anything "
        "about the choice before the second tracker was already on him, "
        "faster and more desperate now that his own partner lay bleeding "
        "in the leaves."
    )},
    {"type": "body", "text": (
        "Okonjo's bad ankle betrayed him at the worst possible instant, "
        "buckling under a hard pivot and dropping him half a step short "
        "of where his own blade needed to be, and it was only Ifeanyi, "
        "arriving a heartbeat later at a dead run, who put the "
        "attacking tracker down before the man's own blade could finish "
        "what the ankle had started."
    )},
    {"type": "body", "text": (
        "Osadebe met the first of the remaining trackers himself, a "
        "big, confident man who fought like someone who had never once "
        "lost this particular kind of fight on ground he knew this "
        "well, and it was only two decades of the crown's own hard "
        "training that let Osadebe read the man's overconfidence for "
        "the weakness it actually was, stepping inside a wide, careless "
        "swing and ending the exchange before the man's own momentum "
        "had finished carrying him forward."
    )},
    {"type": "body", "text": (
        "Osadebe held the remaining four back almost alone for the "
        "handful of seconds it took the other three to reform, giving "
        "ground deliberately rather than losing it, reading the "
        "ravine's own edge behind him the way a captain reads the last "
        "honest option left available to him."
    )},
    {"type": "body", "text": (
        "\"Now,\" he shouted, and the four of them broke together for "
        "the ravine's steep, ugly slope, half climbing and half falling "
        "down ground no sane patrol would follow at full speed, buying "
        "distance the only way distance was left to buy."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They did not stop moving until full dark forced them to, "
        "miles from the clash and breathing too hard to speak for the "
        "first several minutes of the silence that finally caught up "
        "with them."
    )},
    {"type": "body", "text": (
        "\"Two men down, one of them badly,\" Ifeanyi said eventually, "
        "checking his own blade in the failing light with hands that "
        "had not quite finished shaking. \"They will have carried word "
        "back to that wall before this same sun sets again.\""
    )},
    {"type": "body", "text": (
        "Emenike sat apart from the other three for a long while, "
        "turning his own blade over in the dark with a stillness that "
        "worried Osadebe more than any amount of open shaking would "
        "have. \"I have never wounded a man before today,\" he said "
        "finally, not quite to anyone. \"I did not expect it to feel "
        "this much like the same fear I have carried since the ambush "
        "at Idoro. I thought fear like that belonged only to the person "
        "on the losing end of a blade.\""
    )},
    {"type": "body", "text": (
        "\"It belongs to both ends of it,\" Osadebe said, quiet, "
        "settling beside him. \"Any soldier who tells you otherwise has "
        "either never truly fought, or has spent a great deal of effort "
        "convincing himself of something that is not actually true. "
        "You did what the ground demanded and no more than that. Hold "
        "onto the second half of that fact tonight. It matters more "
        "than the first.\""
    )},
    {"type": "body", "text": (
        "\"Then the wall already knows exactly what it needs to know,\" "
        "Osadebe said, grim, binding a shallow cut of his own that none "
        "of them had noticed him taking until now. \"Four armed "
        "strangers, willing to fight rather than flee, still somewhere "
        "on this ground. Whatever quiet advantage we walked in with is "
        "finished. From here, everything we do, we do in the open, or "
        "as close to it as this country allows.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE WARDEN AND MFONISO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden had not slept properly since the courier's report, "
        "and it showed in the flat, brittle edge her voice carried when "
        "she summoned Mfoniso back to her study three days ahead of the "
        "fourteen she had promised."
    )},
    {"type": "body", "text": (
        "\"I extended your time once,\" she said, not inviting Mfoniso "
        "to sit this time, \"because I believed, then, that this House "
        "could afford the patience. I no longer believe that. Strangers "
        "are moving on ground this House considers its own, and a "
        "keeper who allows an undecided asset to sit open while her own "
        "compound grows this unsettled is a keeper who has stopped "
        "reading her own ledger honestly.\""
    )},
    {"type": "body", "text": (
        "The Warden had spent those same three sleepless nights doing "
        "the same private arithmetic she had once explained so plainly "
        "to Mfoniso across her own desk, a valuable asset weighed "
        "against the cost of keeping it, except the arithmetic no "
        "longer balanced the way it once had. Every extra guard posted "
        "against strangers on this ground was coin the ledger felt "
        "spent on fear rather than trade, and a keeper who let fear "
        "compound itself indefinitely, in her own long experience, "
        "rarely survived long enough to regret the patience that had "
        "let it grow."
    )},
    {"type": "body", "text": (
        "\"I have not yet reached my teacher,\" Mfoniso said, though "
        "she heard, even as she said it, how little the admission was "
        "going to weigh against whatever the Warden had already decided "
        "in the privacy of her own sleepless nights."
    )},
    {"type": "body", "text": (
        "\"Then you will decide without her,\" the Warden said, flat "
        "and final. \"Three days. Not fourteen, not an extension "
        "measured in whatever comfort you can still find for yourself "
        "in silence. Three days, and you bring me a recommendation this "
        "House can act on immediately, because I no longer trust this "
        "ground to give either of us the luxury of a slower answer.\""
    )},
    {"type": "body", "text": (
        "\"You extended me once out of something that looked, for a "
        "moment, almost like faith in me,\" Mfoniso said, choosing the "
        "words carefully, unwilling to let the observation sound like "
        "an accusation even though some private part of her meant it "
        "exactly that way. \"I would like to understand what changed "
        "that faith into this.\""
    )},
    {"type": "body", "text": (
        "\"Fear changed it,\" the Warden said, with a bluntness that "
        "cost her something visible to give. \"Not fear of you. Fear of "
        "a ground that no longer feels as settled as it did a season "
        "ago, and a growing suspicion that whatever is moving on it has "
        "very little patience left to spend waiting for either of us to "
        "finish deciding what we already both suspect the honest answer "
        "is.\""
    )},
    {"type": "body", "text": (
        "\"And if I still have no answer in three days,\" Mfoniso said, "
        "testing the edge of the new number the same careful way she "
        "had once tested a blade before trusting it to real work."
    )},
    {"type": "body", "text": (
        "\"Then I will close the account myself,\" the Warden said, "
        "\"without waiting for your permission to agree with me. I have "
        "given you every patient hour I intend to give you, Mfoniso. "
        "What you do with the three that remain is entirely your own "
        "affair now.\""
    )},
    {"type": "body", "text": (
        "Neither woman knew, standing in that quiet study with a hard "
        "new number settling between them, that a second clock had "
        "already started running on the very same ground, one begun in "
        "steel and blood rather than patience, ticking now toward the "
        "same compound from a direction neither careful, exhausted "
        "woman standing in that quiet study had thought, until this "
        "very hour, ever once thought to watch closely at all."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
