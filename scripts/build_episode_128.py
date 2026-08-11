#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 128: "Between the Blade and the Door"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The Factor, drafting the
quiet paperwork Ebiere's arrival requires, learns she means to close
Ijeoma's account that same night, accelerated by the failed escape
attempt. He risks his own boldest act yet to warn Mfoniso, who is still
living inside the compound under loose watch. Mfoniso reaches the door
first and openly intervenes, breaking with the House in front of
witnesses for good. Point of no return.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 128
EPISODE_TITLE = "Between the Blade and the Door"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Eight"},
    {"type": "title_ep_name", "text": "Between the Blade and the Door"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE FACTOR
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The order reached the Factor's desk disguised, as this "
        "House's most serious orders always were, as an entirely "
        "ordinary piece of paperwork, a request to quietly amend the "
        "household's staffing ledger to remove one guest's name from "
        "tomorrow's meal count."
    )},
    {"type": "body", "text": (
        "He understood immediately what the request actually meant, "
        "the same fluent, practiced reading of this House's careful "
        "language that had once let him decode a similar request "
        "concerning a rogue field agent's disowning. A meal count "
        "amended a day ahead of need was not an accident of clerical "
        "efficiency. It was a keeper's own quiet confirmation that the "
        "guest whose name it removed would not be present to eat that "
        "meal at all."
    )},
    {"type": "body", "text": (
        "He had told himself, drafting the amendment with his own "
        "steady hand exactly as instructed, that this was simply the "
        "shape of his continuing usefulness to a House that had never "
        "once asked whether he minded being useful in exactly this "
        "way. He had told himself the same thing, more or less, every "
        "single time this House had asked something of him that a "
        "kinder man would have refused outright. He found, setting the "
        "amended ledger aside unfinished, that the sentence had "
        "finally, completely, stopped working."
    )},
    {"type": "body", "text": (
        "He confirmed the timing through a second document, a guard "
        "rotation request that placed an unfamiliar name, Ebiere's own, "
        "at the compound's inner courtyard that same night, past the "
        "hour any ordinary inspection would ever need to occupy it."
    )},
    {"type": "body", "text": (
        "He sat with both papers for a long moment, weighing a caution "
        "that had kept him safely useful to this House for twenty years "
        "against something newer, sharper, and considerably less "
        "willing to look away this time. He thought of Mfoniso's own "
        "refusal, days ago now, and of the strange, unexpected kinship "
        "he had felt passing her in that same corridor afterward. He "
        "understood, folding both documents carefully into his own "
        "coat, that he was about to spend the last of whatever careful "
        "cover two decades of quiet service had ever bought him."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: MFONISO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso had spent her days since the refusal exactly as "
        "ordered, findable, quiet, and thoroughly watched, occupying "
        "the same small guest quarters the Warden had assigned her "
        "pending a decision about her fate that seemed, with each "
        "passing day, to be arriving no faster than the answer she "
        "herself had once promised on Ijeoma's."
    )},
    {"type": "body", "text": (
        "She had used the enforced stillness, at first, to keep "
        "reaching along her own silent second thread, and had "
        "eventually, reluctantly, let even that habit fall away when "
        "days of unbroken nothing finally taught her what her own "
        "clearer judgment had already begun to suspect, that the "
        "silence was not going to break simply because she kept "
        "knocking against it. She had spent the days since instead "
        "doing something closer to waiting properly for the first time "
        "in her adult life, watching this House's ordinary rhythms move "
        "past her window the way a person watches weather she no "
        "longer has any authority to change."
    )},
    {"type": "body", "text": (
        "She had noticed Ebiere's arrival within an hour of it "
        "happening, the particular quality of attention a compound "
        "paid a face it half remembered and had been carefully "
        "instructed to stop discussing. She had not needed anyone's "
        "confirmation to guess, watching that careful, satisfied "
        "arrival from her own window, exactly what task this House had "
        "finally found worth recalling a disowned name for."
    )},
    {"type": "body", "text": (
        "The Factor found her there an hour past dark, letting himself "
        "in without knocking twice, his own carefully bored face "
        "stripped away for the first time she had ever seen it stripped."
    )},
    {"type": "body", "text": (
        "\"Tonight,\" he said, without preamble, setting both documents "
        "down before her. \"The guest's account closes tonight, by "
        "Ebiere's own hand, accelerated by whatever happened outside "
        "this compound's own walls three nights ago. I do not know "
        "every detail. I know enough to know I could not sit with this "
        "paperwork on my own desk another hour without becoming exactly "
        "the kind of quiet accomplice I have spent two seasons trying "
        "not to be anymore.\""
    )},
    {"type": "body", "text": (
        "Mfoniso did not waste a single word on questions the moment "
        "did not have time to spend answering. She was already moving "
        "before the Factor had finished speaking, out into a corridor "
        "she no longer had any official standing to walk with a blade "
        "at her hip, toward an inner courtyard she had been ordered, in "
        "every practical sense, to stay entirely away from."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She reached the guest's new, heavily barred room a handful of "
        "minutes before midnight, and found Ebiere already there, "
        "standing before the same guard who had not left his post in "
        "three days, a small, unremarkable knife held loosely, "
        "professionally, at her own side."
    )},
    {"type": "body", "text": (
        "\"Step back from that door,\" Mfoniso said, her voice carrying "
        "clean and flat down the whole length of the corridor, loud "
        "enough that the guard, two passing household staff, and a "
        "second watchman drawn by the sound all turned to see exactly "
        "who was speaking and exactly what she was interrupting."
    )},
    {"type": "body", "text": (
        "Ebiere turned, unhurried, a professional's careful assessment "
        "rather than any real alarm. \"I was told you had been relieved "
        "of every operation this House trusts to anyone,\" she said. "
        "\"I was not told you had also been relieved of the sense to "
        "know when a task no longer belongs to you.\""
    )},
    {"type": "body", "text": (
        "\"It has never belonged to you either,\" Mfoniso said, closing "
        "the distance between them with the same unhurried, deliberate "
        "control she had built her entire career on. \"You are closing "
        "an account you do not understand, against a guardian whose "
        "own history this House has been lying to itself about for "
        "three centuries. I will not stand in a corridor and watch this "
        "House repeat that lie one more time simply because it finally "
        "found a hand willing to hold the knife.\""
    )},
    {"type": "body", "text": (
        "\"Careful,\" Ebiere said, something almost like genuine "
        "curiosity entering her own flat voice, the professional's "
        "instinct to understand a threat before dismissing it. \"You "
        "are describing a private theory about an old guardian's grief "
        "as though it were a fact this whole House has already agreed "
        "to. I was given a name, a location, and an instruction. I was "
        "not given your doubts, and I do not intend to inherit them "
        "secondhand from a hunter this House has already publicly "
        "measured and found wanting.\""
    )},
    {"type": "body", "text": (
        "\"Then trust your own eyes instead of my doubts,\" Mfoniso "
        "said. \"Ask yourself honestly why a keeper who has never once "
        "explained herself to either of us suddenly needs this "
        "particular account closed tonight, in secret, rather than "
        "openly, the way this House has always closed accounts it "
        "actually stood behind.\""
    )},
    {"type": "body", "text": (
        "\"This is not your fight to finish anymore,\" Ebiere said, "
        "though her own grip on the knife had shifted, fractionally, "
        "into something readier than professional confidence alone "
        "required."
    )},
    {"type": "body", "text": (
        "\"Then make it yours to finish through me first,\" Mfoniso "
        "said, and drew her own blade in front of every witness the "
        "corridor's sudden gathered crowd could offer, a hunter of this "
        "House standing openly against another hunter of this same "
        "House, for the first time in living memory, over a single "
        "guest's single, undecided life."
    )},

    {"type": "body", "text": (
        "The guard at the door did not move to help either woman, "
        "understanding, correctly, that whichever side he chose in the "
        "next several seconds would follow him for the rest of his "
        "service to this House. The two household staff who had "
        "stopped to watch would carry the sight of it, unembellished "
        "and unforgettable, to every corner of the compound before "
        "morning."
    )},
    {"type": "body", "text": (
        "The guard at the door, forced by the moment into a choice he "
        "had spent three days praying he would never actually have to "
        "make, shifted his own weight, almost imperceptibly, half a "
        "step closer to Mfoniso's side of the corridor rather than "
        "Ebiere's. Neither woman acknowledged it. Both of them noticed "
        "it completely."
    )},
    {"type": "body", "text": (
        "\"You would truly bleed for a guest you have never once "
        "spoken to,\" Ebiere said, testing the ground between them one "
        "final time before whatever came next became unavoidable, "
        "\"over a theory neither this House nor its own Warden has ever "
        "once confirmed for you.\""
    )},
    {"type": "body", "text": (
        "\"I would bleed for the chance to finally learn whether the "
        "theory is true,\" Mfoniso said, \"rather than let this House "
        "close the one door that might ever have let me learn it "
        "honestly. That is worth more to me tonight than my own "
        "standing in a House that stopped deserving my loyalty the "
        "moment it asked me to stop asking questions.\""
    )},
    {"type": "body", "text": (
        "There was no quiet way left to undo what had already, "
        "irreversibly, been seen. Mfoniso understood that even as she "
        "held her own blade steady between Ebiere and the barred door "
        "behind her, understood that whatever happened in the next few "
        "seconds, she had just finished, in front of witnesses this "
        "House could never be talked out of remembering, the thing her "
        "quiet refusal to the Warden had only begun."
    )},
    {"type": "body", "text": (
        "Somewhere beyond this corridor, word of what had just been "
        "seen was already moving, the way it had moved after her "
        "refusal, faster and further than either woman standing here "
        "could hope to outrun it. There would be no explaining this "
        "away tomorrow as a private disagreement settled quietly "
        "between colleagues. A hunter had drawn steel against another "
        "hunter of the same House, in front of a guard and two staff "
        "who would each carry their own version of the story to "
        "whoever asked first, and Mfoniso understood, standing her "
        "ground with her own heart hammering exactly as hard as it had "
        "the day she first refused, that there was now only one "
        "direction left for either of them to walk from here."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
