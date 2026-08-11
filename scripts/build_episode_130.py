#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 130: "The Last Order He Ever Gave"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The combined group fights
its way toward Ijeoma's barred room through a compound converging on the
alarm. The Factor, unable to fight, spends the last of his authority
instead, issuing a false stand down order that redirects a full patrol
away from the group's own route, a decisive, costly act that buys the
opening they need. Act Four closes on Ijeoma and Emenike seeing each
other for the first time in two seasons, still not clear of danger.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 130
EPISODE_TITLE = "The Last Order He Ever Gave"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Thirty"},
    {"type": "title_ep_name", "text": "The Last Order He Ever Gave"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE PUSH
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"The room is deeper in, past the second courtyard,\" Mfoniso "
        "said, already moving, trusting the strangers behind her to "
        "keep pace or be left to their own fate in a compound that no "
        "longer had any reason to be gentle with anyone it found "
        "wandering its corridors uninvited. \"Ebiere will have gone for "
        "more men rather than chase us alone. We have minutes, not "
        "longer.\""
    )},
    {"type": "body", "text": (
        "Osadebe kept the party moving in a tight formation Mfoniso "
        "had not asked for and did not need to, reading her own "
        "unfamiliar authority in this corridor the same careful way he "
        "read any battlefield he had not chosen himself. Emenike moved "
        "beside him in a silence that had nothing left in it of the "
        "suspicion he had carried into this corridor only minutes "
        "before, every scrap of his attention now spent on the "
        "distance still standing between himself and a door he had "
        "crossed half a kingdom to reach."
    )},
    {"type": "body", "text": (
        "They met the first real resistance at the second courtyard's "
        "own gate, four guards already forming a line across it on "
        "orders none of the four strangers had time to question before "
        "steel was already crossing steel again, close and desperate "
        "in ground too narrow for anyone to fight comfortably."
    )},

    {"type": "body", "text": (
        "Okonjo dropped the second guard with a strike that owed "
        "everything to the same patient training Ifeanyi had spent "
        "weeks correcting, and felt, even mid motion, the particular "
        "absence of the man who should have been fighting at his own "
        "shoulder tonight, left behind at a lonely camp with a wound "
        "this fight would have been considerably harder to survive "
        "without one more blade to share it."
    )},
    {"type": "body", "text": (
        "Mfoniso fought with an economy none of the three men had ever "
        "seen matched, each strike costing her exactly as much effort "
        "as the strike actually required and no more, and it was that "
        "same economy, rather than any raw advantage in numbers, that "
        "finally broke the gate's line open half a minute before the "
        "second patrol could arrive to close it again."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE FACTOR
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Factor reached the same courtyard's edge a breath behind "
        "them, unarmed and entirely out of any plan beyond the single "
        "desperate thought that had carried him this far, that a "
        "House this deep in chaos still listened, out of decades of "
        "trained habit, to the particular voice of a man it had never "
        "once had reason to doubt."
    )},
    {"type": "body", "text": (
        "He had spent the walk from his own quarters turning the same "
        "question over that had followed him since the night he first "
        "let a knot pass uninspected, whether a man could actually "
        "spend twenty years of careful, invisible service on a single "
        "moment and call the trade a fair one. He had never once "
        "answered the question honestly to himself before tonight. He "
        "found, closing the last distance toward a courtyard full of "
        "strangers he had never met and a woman he barely knew, that "
        "the answer had apparently been waiting for him all along, "
        "patient as a debt finally come due."
    )},
    {"type": "body", "text": (
        "A full second patrol was closing fast from the eastern "
        "corridor, six men who would reach the gate fight within "
        "seconds and end whatever chance the group still had of "
        "reaching that door alive. The Factor stepped directly into "
        "their path instead, drawing himself up into the same "
        "unhurried, absolute authority he had spent twenty years "
        "using to move ledgers rather than men."
    )},
    {"type": "body", "text": (
        "\"Stand down and redirect to the northern wall immediately,\" "
        "he said, his voice carrying the flat, practiced certainty of "
        "a man who had never once in this House's memory given an "
        "order that turned out to be wrong. \"The real breach is there, "
        "not here. This courtyard is a decoy meant to pull every man "
        "this House has away from where the actual danger is entering. "
        "Move, now, before that decoy finishes working exactly as "
        "intended.\""
    )},
    {"type": "body", "text": (
        "The patrol's own captain hesitated only a single heartbeat, "
        "twenty years of the Factor's own unblemished authority doing "
        "in that one heartbeat what no amount of shouted urgency could "
        "have managed on its own, and then the six men were moving, "
        "peeling away toward the northern wall at a dead run, chasing a "
        "breach that had already happened and emptied itself an hour "
        "ago."
    )},
    {"type": "body", "text": (
        "It could not last. The Factor knew that even as he watched "
        "them go, understood that the moment anyone compared his order "
        "against the guard captain's own contradicting report, the lie "
        "would collapse completely and take his entire career down "
        "with it in the same instant. He found, standing alone in the "
        "courtyard's own settling quiet, that the knowledge cost him "
        "far less than he had spent two long seasons assuming it "
        "would."
    )},
    {"type": "body", "text": (
        "The real guard captain found him there moments later, "
        "returning from the northern wall's own empty ground with a "
        "fury the Factor had never once seen directed at himself in "
        "twenty years of careful, invisible service. \"You sent my men "
        "chasing nothing,\" the captain said, closing the distance fast. "
        "\"Explain yourself before I explain it for you to the Warden "
        "personally.\""
    )},
    {"type": "body", "text": (
        "\"I sent them exactly where I meant to send them,\" the Factor "
        "said, and did not run, though every instinct twenty careful "
        "years had ever taught him screamed that running was still, "
        "barely, possible. \"Tell the Warden whatever you believe she "
        "needs to hear. I find I no longer have anything left to "
        "protect by lying to either of you about it.\""
    )},
    {"type": "body", "text": (
        "The captain's own restraining hand closed hard around his "
        "arm a moment later, and the Factor let himself be taken "
        "without struggle, understanding, with the same clear, "
        "unfrightened calm that had carried him through the false "
        "order itself, that whatever this House chose to do with him "
        "now, he had already spent the one thing tonight that had "
        "actually mattered."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: THE DOOR
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The courtyard cleared just long enough for the group to break "
        "through, the diversion buying exactly the handful of unwatched "
        "seconds Mfoniso had promised, and they reached the guest's "
        "barred door with no one left standing between them and it but "
        "the single guard who had not left his post in what was now "
        "four full days."
    )},
    {"type": "body", "text": (
        "He looked at the small army suddenly filling his corridor, "
        "looked longest of all at Mfoniso's own drawn blade, and stepped "
        "aside from the door without being asked, understanding, in "
        "whatever quiet way had kept him silent about a girl's failed "
        "escape and a hunter's own broken loyalty both, exactly which "
        "side of tonight's chaos he had already privately chosen."
    )},
    {"type": "body", "text": (
        "Osadebe broke the second bar himself, three hard strikes with "
        "the flat of his own blade against wood that had never once "
        "been built to withstand a determined man's full strength, and "
        "the door finally gave inward into a small, dark room where "
        "Ijeoma stood already braced against whatever new danger the "
        "night's endless noise had promised her."
    )},

    {"type": "body", "text": (
        "Brother and sister looked at each other across a threshold "
        "neither of them had truly believed, some nights, they would "
        "ever stand on either side of again."
    )},

    {"type": "body", "text": (
        "\"Emenike,\" Ijeoma said, his name arriving out of her in a "
        "voice that did not sound, even to her own ears, entirely "
        "steady."
    )},
    {"type": "body", "text": (
        "\"I told you I would come,\" Emenike said, crossing the last "
        "distance between them in three fast steps and pulling her into "
        "an embrace that carried two full seasons of everything neither "
        "of them had ever let themselves say aloud. \"I am sorry it took "
        "this long. I am sorry for every single day of it.\""
    )},
    {"type": "body", "text": (
        "Ijeoma held onto him a moment longer than either of them had "
        "any real time to spend, counting, the same private habit that "
        "had kept her alive two whole seasons, the exact number of "
        "heartbeats this reunion had actually been given, and found "
        "she did not care, for once, that the count was already "
        "running out."
    )},
    {"type": "body", "text": (
        "\"You look older,\" she said, pulling back just far enough to "
        "study his face properly, a trader's own habit of reading a "
        "person the way she once read cloth, for wear, for damage, for "
        "everything two seasons apart had actually cost him."
    )},
    {"type": "body", "text": (
        "\"So do you,\" Emenike said, and meant it as the plain, "
        "grateful truth rather than any unkindness, relief and grief "
        "tangled so completely in his own voice that he did not "
        "bother trying to separate them. \"I have a great deal to tell "
        "you. All of it can wait until we are somewhere safer than "
        "this exact doorway.\""
    )},
    {"type": "body", "text": (
        "Mfoniso, watching the reunion from the corridor's edge with "
        "her own blade still drawn, felt something she did not "
        "immediately have a name for, the particular ache of a woman "
        "who had spent her entire adult life ending exactly this kind "
        "of story for other people, standing now, for the first time, "
        "close enough to actually watch one end differently."
    )},
    {"type": "body", "text": (
        "Osadebe allowed the two of them exactly as long as the "
        "corridor's own returning noise permitted, which was not long "
        "at all, the guard captain's own furious shouting already "
        "rising somewhere behind them, closer with every passing "
        "second."
    )},
    {"type": "body", "text": (
        "\"We are not out of this House yet, not by any real measure,\" "
        "he said, gentle but immovable, already turning the party back "
        "toward whatever route out still remained open to them. \"Hold "
        "each other later, for as long as you both still need to. "
        "Right now, all five of us run together, and we run very quickly indeed.\""
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
