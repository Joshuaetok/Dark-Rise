#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 124: "The First Order She Ever Refused"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Mfoniso's three day deadline
arrives. Rather than delay further or offer a comfortable answer, she
refuses outright to recommend closing Ijeoma's account, and refuses in
the same breath to carry out a kill order if the Warden gives one
herself. The definitive break from the House.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 124
EPISODE_TITLE = "The First Order She Ever Refused"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Four"},
    {"type": "title_ep_name", "text": "The First Order She Ever Refused"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Mfoniso spent the last of her three days exactly as she had "
        "spent the six before them, reaching along a thread that gave "
        "her nothing back, though by the second evening she had stopped "
        "reaching for her teacher's answer and started, instead, "
        "reaching simply to feel less alone with the question she now "
        "understood only she could actually answer."
    )},
    {"type": "body", "text": (
        "She remembered, lying awake through most of that final night, "
        "a much younger version of herself asking her teacher what a "
        "hunter was actually supposed to do if a hunt ever felt wrong "
        "partway through it. Her teacher had answered without "
        "hesitation, the way she answered every question that touched "
        "the discipline she valued above almost everything else. \"A "
        "hunter finishes what she starts,\" she had said. \"Doubt is a "
        "luxury for people who have never had to live with the cost of "
        "changing their mind halfway through paying a debt.\" Mfoniso "
        "had carried that answer for fifteen years without once "
        "questioning it. She questioned it now, lying in the dark with "
        "three days shrinking toward zero, and found she no longer "
        "believed a single word of it."
    )},
    {"type": "body", "text": (
        "She thought, that last night, of every version of herself the "
        "job had ever required her to be. The careful student. The "
        "patient hunter. The steady hand the Warden had trusted for a "
        "decade to feel nothing that might slow a difficult decision "
        "down. She found, turning each version over in the dark, that "
        "she could no longer locate the exact moment any of them had "
        "agreed, on her behalf, to become a woman willing to finish a "
        "story her own teacher had never let her hear the end of "
        "simply because a ledger demanded a tidy answer by a fixed "
        "hour."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"Your three days end today,\" the Warden said, when Mfoniso "
        "was shown into the study for what both of them understood, "
        "without needing to say so aloud, was the last such meeting "
        "either of them expected to hold under these particular terms. "
        "\"Give me your recommendation.\""
    )},
    {"type": "body", "text": (
        "\"I do not recommend closing the account,\" Mfoniso said, "
        "steady, the words arriving with none of the hesitation that "
        "had marked every answer she had given across the weeks before "
        "this one. \"I will not recommend it today, and I do not "
        "believe I will ever recommend it, whatever number of days you "
        "choose to give me next.\""
    )},
    {"type": "body", "text": (
        "\"That is not the recommendation I asked for,\" the Warden "
        "said, her voice cooling several careful degrees. \"I asked for "
        "an answer, Mfoniso, not a refusal dressed up to sound like "
        "one.\""
    )},
    {"type": "body", "text": (
        "\"Then hear the refusal plainly,\" Mfoniso said, \"because I "
        "intend to give you nothing softer to hide it inside. I will "
        "not recommend Ijeoma's death. And if you decide, with or "
        "without my recommendation, that her account should close, I "
        "will not be the hand that closes it. Send someone else. I am "
        "finished being the hand this House reaches for whenever a "
        "decision proves too costly for anyone with real authority to "
        "make cleanly.\""
    )},

    {"type": "body", "text": (
        "\"You are letting a stranger's story unsettle judgment I have "
        "trusted for ten years,\" the Warden said, trying persuasion "
        "once more before she abandoned it entirely, her voice carrying "
        "something almost like genuine appeal. \"You do not know for "
        "certain the guardian at Idoro is the one your teacher's story "
        "speaks of. You are building a decision on top of a suspicion, "
        "Mfoniso, and I have never once known you to do that in ten "
        "years of watching you work.\""
    )},
    {"type": "body", "text": (
        "\"I am building a decision on top of a question I can no "
        "longer pretend does not deserve an answer,\" Mfoniso said. "
        "\"Certainty was never actually the thing I lost this week. I "
        "lost my willingness to keep working while the question sat "
        "unanswered underneath everything I was asked to do. I would "
        "rather be wrong and refuse than be right and comply, if "
        "comply means what it has meant for three centuries of this "
        "House's own careful bookkeeping.\""
    )},
    {"type": "body", "text": (
        "The silence that followed was not the same silence that had "
        "sat between them at their last meeting. That silence had "
        "carried surprise. This one carried something colder, the "
        "particular stillness of a keeper recalculating, in real time, "
        "exactly how dangerous her most reliable instrument had just "
        "become."
    )},

    {"type": "body", "text": (
        "\"You understand what you are actually saying,\" the Warden "
        "said finally, quiet now rather than sharp, which frightened "
        "Mfoniso more than sharpness would have. \"You are not simply "
        "declining an assignment. You are refusing a direct order from "
        "the House that trained you, fed you, and paid every debt your "
        "own family ever owed anyone across three generations. Hunters "
        "who refuse this House do not quietly return to their own "
        "quarters afterward and wait for a gentler assignment.\""
    )},
    {"type": "body", "text": (
        "\"I understand it completely, and I have spent every hour of "
        "the last three days weighing exactly that cost against every "
        "other cost I could think to weigh it against,\" Mfoniso said. "
        "\"I have spent "
        "three days understanding almost nothing else. I am telling "
        "you anyway, because I have finally worked out something I "
        "should have worked out long before this week cost me the "
        "chance to work it out gently. The guardian at Idoro is very "
        "possibly the same guardian my own teacher's oldest story was "
        "always too careful to name, the one who refused to run from "
        "the exact tactic I was trained to use against it. If that is "
        "true, then everything this House has asked me to do these "
        "past months has not been a new hunt at all. It has been the "
        "same old debt, still unpaid after three centuries, and I will "
        "not spend a nineteen year old girl's life finishing a payment "
        "I no longer believe this House, or my own lineage, ever had "
        "any honest right to collect.\""
    )},

    {"type": "body", "text": (
        "The Warden studied her for a long, unreadable moment, weighing "
        "a decade of trust against a single unmovable refusal, and when "
        "she finally spoke again, her voice carried the flat, final "
        "tone of a keeper closing a ledger line she had genuinely "
        "hoped, until this exact moment, she would never have to close."
    )},
    {"type": "body", "text": (
        "\"You are relieved of the guest's operation, effective "
        "immediately,\" she said. \"You are relieved, in fact, of every "
        "operation this House currently trusts you with, pending a "
        "decision I have not yet made about what your refusal costs "
        "you personally. I would advise you to remain somewhere I can "
        "find you easily in the coming days, Mfoniso. I would advise "
        "you, more urgently, not to test how far this House's patience "
        "extends toward a hunter who has just told it, to my own face, "
        "that she no longer trusts its judgment.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Mfoniso walked out of that study into a compound that already "
        "felt subtly different beneath her own feet, guards who had "
        "nodded to her without thought for a decade now glancing twice "
        "as she passed, word of a refusal this House had never once "
        "witnessed already, somehow, beginning its own quiet journey "
        "through every corridor she crossed."
    )},
    {"type": "body", "text": (
        "She passed the Factor once in that same corridor, close "
        "enough to exchange the small, meaningless nod two members of "
        "the same household exchange without thinking, and found "
        "herself wondering, for the first time, what quiet cracks of "
        "his own might already be sitting behind that carefully bored "
        "face. She had never once, in years of working near him, "
        "considered him anything more than a cautious administrator "
        "grown too soft for the Warden's harder decisions. She "
        "considered him now with something closer to kinship, two "
        "people inside the same House who had each, in their own "
        "separate quiet ways, finally run out of room to keep "
        "pretending a ledger line was only ever a number."
    )},
    {"type": "body", "text": (
        "She did not know yet what the Warden intended to do about "
        "Ijeoma now that her own steady hand had been removed from the "
        "decision. She did not know what the Warden intended to do "
        "about her, either, beyond the thin, temporary safety of being "
        "told to stay findable rather than being taken somewhere "
        "quieter immediately."
    )},
    {"type": "body", "text": (
        "She found, walking those unfamiliar corridors with every "
        "familiar certainty of her old career finally, completely "
        "gone, that she felt something closer to clarity than to fear, "
        "the particular light headed relief of a person who had spent "
        "far too long carrying a weight she had never once let herself "
        "put down and set it down, finally, without knowing yet what "
        "would be waiting for her once both her hands were finally, "
        "genuinely empty."
    )},
    {"type": "body", "text": (
        "She thought, reaching her own small quarters at last and "
        "sitting alone with the door shut behind her, of the second "
        "thread that had gone silent on the river road and never once "
        "answered since. She tried it one final time, not truly "
        "expecting anything, and felt the same familiar nothing meet "
        "her the way it had met her every night for weeks now. It "
        "occurred to her, sitting with that nothing rather than "
        "fighting it, that perhaps her teacher's silence and her own "
        "refusal tonight were not two separate failures after all, but "
        "the same debt finally coming due, quietly and at last, on "
        "both ends of a thread that had carried it, unquestioned and "
        "unexamined, for far longer than either woman holding it had "
        "ever once truly stopped long enough to seriously, honestly "
        "ask why any of it had ever begun."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
