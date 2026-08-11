#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 119: "The First Crack in Her"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Midway through the ten days
the Warden allowed her, Mfoniso has spent every spare hour testing her
second thread for any sign her teacher still answers, and has produced
no real recommendation on Ijeoma's fate to show for it. The Warden
presses her for progress and, for the first time in years of working
together, sees Mfoniso's composure slip.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 119
EPISODE_TITLE = "The First Crack in Her"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Nineteen"},
    {"type": "title_ep_name", "text": "The First Crack in Her"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Mfoniso had spent six of her ten allotted days doing "
        "something she had never once, in her whole career, allowed "
        "herself to do before a hunt's conclusion. She had stopped "
        "hunting the guest entirely and started, instead, hunting for "
        "her own teacher, reaching along the thin, old thread between "
        "them every evening with a patience that felt less like "
        "professional discipline now and more like something closer to "
        "prayer."
    )},
    {"type": "body", "text": (
        "The ritual was always the same. She would sit alone, usually "
        "in the last hour before sleep, and turn her attention inward "
        "along the thin old line the way she might have turned a key "
        "in a lock she had opened a thousand times before without ever "
        "once needing to think about the motion. Some nights she "
        "reached for an hour. Some nights she reached until her own "
        "eyes grew too heavy to keep the attempt honest any longer. "
        "Every night, without exception, the line gave back the same "
        "flat, patient nothing, neither warm nor cold, simply present "
        "and unanswering, like a door that had not been locked against "
        "her so much as quietly, permanently vacated."
    )},
    {"type": "body", "text": (
        "The thread answered nothing. It had answered nothing since "
        "the night on the river road hollow when the tension along it "
        "first went slack, and six days of careful, repeated reaching "
        "had taught her only the shape of that silence, unbroken, "
        "unchanged, giving away nothing about whether it meant her "
        "teacher was simply occupied elsewhere, deliberately withholding "
        "contact, or no longer able to answer at all."
    )},
    {"type": "body", "text": (
        "She had told herself, each of those six evenings, that the "
        "search cost her nothing she was not willing to spend, an hour "
        "here, a restless night there. She understood, walking to the "
        "Warden's study for the check in she had known was coming since "
        "the number ten was first spoken aloud, that the search had in "
        "fact cost her a great deal more than that. It had cost her the "
        "clear, uncluttered attention a decision like this one actually "
        "required."
    )},

    {"type": "body", "text": (
        "She remembered, walking the last stretch of corridor toward "
        "the Warden's door, a much smaller version of herself asking "
        "her teacher once why the thread between them had to exist at "
        "all, when other trades passed their skills down through "
        "nothing more mysterious than patient instruction. Her teacher "
        "had only smiled, the particular smile Mfoniso had spent a "
        "lifetime reading as warmth and had only recently begun "
        "rereading as something closer to practiced composure. \"Some "
        "debts,\" she had said, \"are better carried where they can be "
        "felt rather than merely remembered.\" Mfoniso had not "
        "understood the answer then. She was beginning, six silent "
        "days later, to understand it rather better than she wanted "
        "to."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"Six days,\" the Warden said, not unkindly, watching Mfoniso "
        "settle into the same chair she had occupied at their first "
        "meeting. \"I am not asking for your final answer. I am asking "
        "what you have actually learned in the time I gave you, because "
        "a woman who has learned nothing in six days rarely learns "
        "anything useful in the four that remain to her either.\""
    )},
    {"type": "body", "text": (
        "\"I have learned that the guardian at Idoro is very likely the "
        "same one my own teacher's story always broke off before "
        "naming,\" Mfoniso said, choosing the true answer over the "
        "convenient one, the way she had trained herself to do across "
        "every year of honest service to this House. \"I have not yet "
        "learned what that fact should actually change about my "
        "recommendation on the guest.\""
    )},
    {"type": "body", "text": (
        "\"Then learn it faster,\" the Warden said, an edge entering her "
        "voice that had not been there a moment before. \"I did not "
        "give you ten days to conduct a private study of your own "
        "family history, Mfoniso. I gave you ten days to tell me "
        "whether a valuable, difficult asset is worth this House's "
        "continued patience. Those are not the same question, and I "
        "would like to understand why you appear to have spent six "
        "days answering only the one I did not actually ask you.\""
    )},
    {"type": "body", "text": (
        "Mfoniso opened her mouth to answer with the same practiced "
        "composure she had carried into every difficult conversation of "
        "her adult life, and found, for the first time she could "
        "clearly remember, that the composure simply was not there to "
        "reach for."
    )},
    {"type": "body", "text": (
        "\"Because I cannot reach my teacher,\" she said instead, the "
        "words arriving raw and unrehearsed in a voice that did not "
        "sound, even to her own ears, entirely like her own. \"I have "
        "carried a thread to her since before I could properly walk, "
        "and for six days now it has answered me with nothing at all, "
        "and I do not know whether that means she is simply busy, or "
        "deliberately silent, or gone in some way I have never once had "
        "to imagine before now. I am sorry. That is not an answer that "
        "helps this House's ledger. It is the true reason I have not "
        "given you a better one.\""
    )},

    {"type": "body", "text": (
        "The silence that followed lasted longer than either woman "
        "seemed comfortable letting it last, the two of them sitting "
        "with an honesty neither had quite planned to let into the "
        "room, until the fire in the corner brazier finally settled "
        "with a small, quiet shift of its own coals, as though even it "
        "had grown tired of waiting for one of them to speak first."
    )},

    {"type": "body", "text": (
        "The Warden studied her for a long moment with an attention "
        "Mfoniso had felt directed at her many times before, but never "
        "once quite like this, not the professional assessment of a "
        "keeper weighing a hunter's usefulness but something closer to "
        "simple, startled observation, the look of a person noticing, "
        "for the first time, a crack in a wall she had genuinely "
        "believed load bearing enough to trust without inspection."
    )},
    {"type": "body", "text": (
        "\"I have known you nearly ten years,\" the Warden said finally, "
        "her voice quieter now, stripped of the edge it had carried a "
        "moment ago. \"In all that time I do not believe I have ever "
        "once heard you say the words I am sorry to me about your own "
        "work. You have made mistakes in ten years. You have never "
        "apologized for one before today.\""
    )},
    {"type": "body", "text": (
        "\"I am not certain it was a mistake,\" Mfoniso said, recovering "
        "her voice if not entirely her composure. \"I am certain it has "
        "cost me time I promised you, and that the two things are not "
        "the same, and that I owe you the honesty of telling you which "
        "one has actually happened here.\""
    )},
    {"type": "body", "text": (
        "\"And if the silence does not break in four days either,\" the "
        "Warden asked, the question landing more gently than Mfoniso "
        "had braced herself to receive it. \"What then.\""
    )},
    {"type": "body", "text": (
        "\"Then I will give you a recommendation built on my own "
        "judgment alone, without whatever answer I had hoped she might "
        "still be able to give me,\" Mfoniso said. \"I would have "
        "preferred her counsel. I have made harder decisions than this "
        "one without it before, and I will not pretend to you now that "
        "I cannot manage it again.\""
    )},
    {"type": "body", "text": (
        "\"Four days,\" the Warden said, standing to signal the meeting "
        "had reached its natural end, though something in the careful "
        "way she said it suggested the number had cost her more "
        "certainty to repeat than it had the first time she named it. "
        "\"Find your teacher, or find your answer without her. I no "
        "longer particularly care which. I care only that four days "
        "from now, you walk back into this room and give me one.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Alone afterward, the Warden sat a long while with a question "
        "she had not asked Mfoniso directly, turning it over with the "
        "same careful attention she gave to any ledger entry that had "
        "suddenly, unexpectedly, stopped balancing the way it always "
        "used to. She had built ten years of trust on the certainty "
        "that Mfoniso was the single most reliable instrument this "
        "House possessed, steady where other hunters grew reckless, "
        "controlled where others let feeling cloud their judgment."
    )},
    {"type": "body", "text": (
        "She did not yet believe that certainty was wrong. She "
        "believed, sitting with the memory of an apology she had never "
        "once heard before today, that it might no longer be as simple "
        "as it had always looked, and a keeper who had survived this "
        "long by trusting her own ledgers over her own comfortable "
        "assumptions found herself, for the first time in a very long "
        "while, quietly beginning to prepare for the possibility that "
        "her most reliable instrument might not answer the way she had "
        "always assumed it would."
    )},
    {"type": "body", "text": (
        "She thought of the delta ambush, three years past now, when "
        "Mfoniso had walked out of a burning warehouse with a wound "
        "that should have killed a less disciplined woman and had "
        "still, somehow, delivered her full report before allowing "
        "anyone to so much as look at the injury. She thought of a "
        "dozen smaller moments since, each one confirming the same "
        "quiet truth, that Mfoniso simply did not break under pressure "
        "the way other hunters eventually did. Sitting with today's "
        "apology still fresh in her memory, the Warden found she could "
        "no longer say with total confidence whether that truth had "
        "ever actually been tested by anything that mattered to "
        "Mfoniso personally, rather than merely anything that had, "
        "until this very afternoon, only ever mattered to this House "
        "and the careful, unfeeling ledgers it had always kept so very "
        "faithfully indeed, year after year."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
