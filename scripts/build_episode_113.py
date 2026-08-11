#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 113: "Closer Than the Story Let Her Believe"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Mfoniso reaches the Concern's
headquarters and answers the Warden face to face, but insists on asking
her own question first, what became of the guardian ground's resettled
people, and whether the House still keeps record of where. The Warden's
answer, offered almost as an aside about the debt's four keepers, lets
Mfoniso work out for herself that her own teacher stands only two
apprenticeships removed from the hunter who took the presence's ground
three centuries ago. The old story was never as distant as she believed.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 113
EPISODE_TITLE = "Closer Than the Story Let Her Believe"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Thirteen"},
    {"type": "title_ep_name", "text": "Closer Than the Story Let Her Believe"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "She had walked the last stretch to the Concern's headquarters "
        "at a pace faster than the road strictly required, arriving "
        "with her boots caked to the ankle and her whole body carrying "
        "the particular tiredness of a woman who had slept badly every "
        "night since the river road hollow. The compound looked exactly "
        "as it always had from outside, unremarkable, disguised as "
        "ordinary trade behind walls no passing traveler would ever "
        "think to question, and she found herself studying those walls "
        "on approach with an attention she had never once spent on them "
        "before, as though they too might be hiding something she had "
        "spent her whole career failing to notice."
    )},
    {"type": "body", "text": (
        "The Warden did not rise when Mfoniso was finally shown into "
        "her private study, road dust still on her clothes and a "
        "hunter's particular stillness settled over her the way it "
        "always was after a long, uneventful walk. She simply set down "
        "the ledger she had been working and studied her most valuable "
        "field agent for a long, unhurried moment, the same way she "
        "studied anything whose value she had not yet fully decided how "
        "to weigh."
    )},
    {"type": "body", "text": (
        "\"You are later than a courier would have been,\" the Warden "
        "said, her voice giving away nothing of the weeks of private "
        "unease that comment actually cost her. \"I have spent longer "
        "than I care to admit wondering whether that delay meant you "
        "were dead, captured, or simply thinking of reasons not to "
        "answer me. I find I am relieved it was only the third.\""
    )},
    {"type": "body", "text": (
        "\"Before I answer your question,\" Mfoniso said, holding the "
        "Warden's gaze with the same steady discipline she had built "
        "her whole career on, \"I have one of my own, and I would rather "
        "ask it honestly, to your face, than carry it unasked any "
        "further. What became of the people our lineage took from its "
        "very first guardian ground. Not the polite word for it. The "
        "true one. And does this House still keep any record of where "
        "they were taken.\""
    )},
    {"type": "body", "text": (
        "The Warden's expression did not change, but something behind "
        "it did, a small recalculation Mfoniso had learned to watch for "
        "across years of reading the older woman's careful stillness. "
        "\"That is an unusual question for a hunter to bring me instead "
        "of an answer,\" the Warden said finally. \"I will assume "
        "something happened on that road worth the asking, and I will "
        "answer it, because I would rather you hear the truth from me "
        "than go looking for it somewhere less careful with you.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"They were resettled,\" the Warden said, \"exactly as you "
        "were taught. Moved to serve the House that had won their "
        "ground, most of them within a single generation absorbed so "
        "completely into that service that their children no longer "
        "remembered which ground had originally been theirs to lose. "
        "It was not mercy, whatever gentler word your own teacher chose "
        "to give you. It was simply efficient. A dead people cannot "
        "work a ledger. A resettled one can.\""
    )},
    {"type": "body", "text": (
        "\"And the records,\" Mfoniso pressed, refusing to let the "
        "answer's coldness turn her from the second half of her own "
        "question. \"Does the House still know where.\""
    )},
    {"type": "body", "text": (
        "\"Some of it,\" the Warden allowed. \"Enough of it that I "
        "could, if I judged the question worth my own time, likely find "
        "you an answer. I do not yet judge it worth my time, Mfoniso, "
        "and I would ask you to consider carefully why a hunter three "
        "hundred years removed from a single old conquest has suddenly "
        "decided its aftermath matters more to her than the living "
        "asset currently costing this House a fortune in patience.\""
    )},
    {"type": "body", "text": (
        "Mfoniso did not answer that directly, unwilling yet to hand "
        "the Warden the full shape of what had happened on the road, "
        "the slack thread, the sleepless night, the suspicion she still "
        "could not fully name even to herself. \"You spoke once of a "
        "debt inherited across four keepers before you,\" she said "
        "instead, steering the conversation onto ground she could stand "
        "on more safely. \"I did not ask, at the time, how far back that "
        "made the debt itself. I am asking now.\""
    )},
    {"type": "body", "text": (
        "\"Further than most of this House's own people realize,\" the "
        "Warden said, and there was, for just a moment, something "
        "almost like respect in the way she said it, the tone of a "
        "keeper glad to finally have someone in the room worth "
        "explaining the ledger to properly. \"The first keeper took the "
        "ground itself, using the very hunter your own training "
        "descends from. The second keeper trained the third. The third "
        "trained me. And somewhere in that same short chain, before it "
        "ever reached me, the first hunter trained an apprentice, who "
        "trained an apprentice, who is, unless I am very much mistaken "
        "about how these things are usually counted, the woman who "
        "eventually trained you.\""
    )},
    {"type": "body", "text": (
        "Mfoniso went very still. She had always understood the "
        "lineage tying her to the original conquest as something "
        "ancient, diffuse, the kind of distant inheritance a person "
        "carried the way they carried a family name whose original "
        "bearer no living person could actually picture. Two "
        "apprenticeships. Her own teacher stood only two apprenticeships "
        "removed from the hunter who had walked away with an entire "
        "guardian ground three centuries ago."
    )},
    {"type": "body", "text": (
        "That meant the story her teacher told over a cooking fire, the "
        "one guardian who ever refused to run, the story that always "
        "broke off at the same unfinished word, had not been handed "
        "down across some comfortable, blurred distance of many "
        "generations. It had passed through perhaps three sets of hands "
        "total, teacher to student to student, a chain short enough "
        "that her own teacher might well have heard the story first "
        "from someone who had stood close enough to the original "
        "failure to remember it as something closer to a wound than a "
        "legend."
    )},
    {"type": "body", "text": (
        "She thought, standing there with the Warden's careful "
        "explanation still settling over her, of every evening her "
        "teacher had ever spent correcting the smallest fault in her "
        "form, the precise angle of a blade, the exact patience a "
        "tactic demanded before it could be trusted to work. She had "
        "always understood that discipline as her teacher's own "
        "personal exacting nature. It occurred to her now, standing in "
        "the Warden's study with three centuries suddenly compressed "
        "into three sets of hands, that such discipline might instead "
        "have been passed down whole from someone who had learned, "
        "firsthand and at real cost, exactly what happened when a "
        "hunter grew careless with a guardian this old."
    )},
    {"type": "body", "text": (
        "\"You look as though I have told you something you did not "
        "want to hear,\" the Warden observed, watching her with renewed "
        "attention now, the professional curiosity of a keeper who had "
        "just watched a very controlled woman fail, briefly, to control "
        "her own face."
    )},
    {"type": "body", "text": (
        "\"You have told me something I did not expect to hear,\" "
        "Mfoniso corrected, recovering her stillness with visible "
        "effort. \"There is a difference. I will consider it carefully, "
        "and I will give you my answer on the guest before I leave this "
        "room, as I came here intending to do.\""
    )},
    {"type": "body", "text": (
        "\"My answer,\" Mfoniso said, choosing each word with the care "
        "of a woman who did not yet fully trust her own judgment in "
        "this particular room, \"is that I do not yet recommend closing "
        "the account. Not out of any sentiment toward the guest. Out of "
        "caution. Whatever moved on my own second thread that night on "
        "the road, I do not believe it was nothing, and I would rather "
        "understand what it was before this House spends an asset it "
        "cannot buy back later.\""
    )},
    {"type": "body", "text": (
        "The Warden studied her for a long moment, plainly unsatisfied "
        "with an answer that asked for more patience rather than "
        "offering a clean decision. \"Caution has already cost this "
        "House two seasons of proof runs and a fortune in careful "
        "keeping,\" she said. \"I will hear your caution today, Mfoniso, "
        "because you have earned that much from me. I will not hear it "
        "forever.\" She said nothing further on the matter, but the "
        "warning in it settled over the room clearly enough that "
        "neither woman felt any need to repeat it."
    )},
    {"type": "body", "text": (
        "She crossed the outer courtyard on her way back out, still "
        "turning the Warden's words over, and noticed, almost as an "
        "afterthought, how much heavier the guard had grown since her "
        "last visit, extra men posted at posts that had not needed them "
        "before. She did not know the tightening had nothing to do with "
        "her own delayed answer and everything to do with the Warden's "
        "private nerves. She noted it only as one more small sign that "
        "this House, like her, had quietly stopped fully trusting the "
        "very ground it stood on."
    )},
    {"type": "body", "text": (
        "She did not tell the Warden, not that day and not for many "
        "days after, that the tension she had felt go slack on the "
        "river road now sat in an entirely different light. If her "
        "teacher's own teacher had trained under the very hunter who "
        "took the presence's ground, then the guardian who met her at "
        "Idoro's wall, the one her teacher's story always broke off "
        "before naming, was no longer a distant legend Mfoniso could "
        "hold at arm's length. It was a story close enough to her own "
        "hands that she had very possibly, without ever once intending "
        "to, spent her entire career quietly finishing it."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
