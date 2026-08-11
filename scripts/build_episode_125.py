#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 125: "A Colder Hand to Finish It"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The Warden, distrusting
Mfoniso's refusal as evidence of compromised judgment rather than mere
disobedience, moves against Ijeoma without her. She sends for Ebiere,
the field agent publicly disowned as a rogue after the Idoro boundary
ambush but never actually cut loose, quietly reassigned to a nearby
holding ever since. Ebiere accepts the assignment as her chance to erase
the stain of a fall she never actually deserved. A second, colder threat
begins converging on Ijeoma.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 125
EPISODE_TITLE = "A Colder Hand to Finish It"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Five"},
    {"type": "title_ep_name", "text": "A Colder Hand to Finish It"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE WARDEN
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden did not sleep the night after Mfoniso's refusal "
        "either, though the sleeplessness this time carried a "
        "different shape, less fear than a kind of grim, methodical "
        "recalculation, the particular clarity of a keeper who had "
        "finally stopped hoping a difficult problem might resolve "
        "itself gently."
    )},
    {"type": "body", "text": (
        "She did not believe, turning the refusal over across that "
        "long night, that Mfoniso had simply grown soft. Softness was "
        "not the word for a hunter who had spent a decade proving "
        "herself immune to exactly the kind of sentiment the Warden had "
        "half expected, once, to eventually weaken her. What Mfoniso "
        "had actually shown her was closer to a private conviction the "
        "Warden could not fully follow and did not, in the end, need "
        "to follow in order to draw the one conclusion that actually "
        "mattered. A hunter tied by blood and training to this "
        "particular guardian's own old story could no longer be "
        "trusted to finish a hunt this same story kept quietly "
        "reaching into."
    )},
    {"type": "body", "text": (
        "She thought of the exact words Mfoniso had used, that the "
        "guardian at Idoro was very possibly the same one her own "
        "teacher's story had always protected, and found the phrase "
        "unsettling for a reason she suspected Mfoniso herself had not "
        "fully considered. If that suspicion was true, then this "
        "House's entire hunt had never truly been a hunt against a "
        "stranger at all. It had been, from its very first patient "
        "step, a hunt against something that already, somehow, knew "
        "exactly who was coming for it and why, and a keeper who sent "
        "the same compromised bloodline against an enemy that old "
        "twice in a row deserved whatever failure followed from doing "
        "so."
    )},
    {"type": "body", "text": (
        "The solution, once she allowed herself to see it plainly, was "
        "almost embarrassingly simple. She did not need another hunter "
        "trained in Mfoniso's own lineage, carrying Mfoniso's own "
        "inherited doubts. She needed someone with no old story of her "
        "own tangled anywhere near this particular guardian at all, "
        "someone who would read the guest as exactly what the ledger "
        "had always said she was, an asset whose account had simply, "
        "finally, stopped balancing."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She sent for Ebiere before the sun had fully cleared the "
        "compound's own outer wall."
    )},
    {"type": "body", "text": (
        "The rest of this House believed, as it had been carefully "
        "encouraged to believe for two full seasons now, that Ebiere "
        "had been cast out entirely after the boundary ambush's public "
        "unraveling, disowned by the Factor's own careful statement, "
        "her name spoken of only as a warning about agents who let "
        "personal ambition outrun the House's own patience. The truth, "
        "known to perhaps three people in the whole organization, was "
        "quieter and considerably more useful. Ebiere had been "
        "reassigned rather than removed, posted to a small, unglamorous "
        "holding two days downriver where a public failure could not "
        "easily follow her, and told, plainly, that her name would "
        "remain useful to this House again only when this House "
        "actually needed something it could not afford to be seen "
        "asking for directly."
    )},
    {"type": "body", "text": (
        "That day, the Warden had judged privately for some time now, "
        "had finally arrived."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: EBIERE
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ebiere read the Warden's letter twice before she allowed "
        "herself to feel anything about it, standing alone in the "
        "cramped little office she had been given at the downriver "
        "holding, a demotion she had spent two full seasons privately "
        "refusing to accept as permanent."
    )},
    {"type": "body", "text": (
        "The letter asked nothing of her that a careful reader could "
        "later use against either of them. It requested only that she "
        "make herself available, promptly, for a matter the Warden "
        "preferred to discuss in person rather than commit further to "
        "paper. Ebiere understood exactly what such careful vagueness "
        "actually meant, the same way she had understood, two seasons "
        "ago, exactly what her own public disowning had actually been "
        "bought to accomplish."
    )},
    {"type": "body", "text": (
        "She had not, in her own private accounting of that failure, "
        "ever accepted the House's official version of it. The ambush "
        "had failed because a coin greedy soldier sold its timing "
        "cheaply to anyone willing to pay for it, not because her own "
        "planning had been careless. She had paid the price for "
        "someone else's loose tongue regardless, because a House "
        "needed a name to blame publicly and her name had simply been "
        "the nearest one standing close enough to reach."
    )},
    {"type": "body", "text": (
        "She had spent those two seasons at the downriver holding "
        "doing everything asked of her with a precision she hoped, "
        "quietly, someone was still keeping track of, counting cargo, "
        "settling minor disputes among the holding's small staff, "
        "proving over and over, to an audience she could not see and "
        "was never quite certain was actually watching, that whatever "
        "had truly failed at the Idoro boundary had not been her own "
        "competence. She had grown almost, though never quite, "
        "resigned to the possibility that no one important was "
        "watching at all, and that her own careful diligence was "
        "simply the private discipline of a woman refusing to let a "
        "single unfair season define the rest of her career."
    )},
    {"type": "body", "text": (
        "She packed for the journey back that same afternoon, careful "
        "and unhurried, the particular calm of a woman who had spent "
        "two long seasons waiting for exactly this kind of summons "
        "without once allowing herself to hope for it too openly."
    )},
    {"type": "body", "text": (
        "The Warden received her that evening with none of the careful "
        "diplomacy she had spent recent weeks extending toward Mfoniso, "
        "the plain, efficient tone of a keeper speaking to an "
        "instrument rather than negotiating with a colleague. \"There is "
        "a guest,\" she said, \"whose account this House can no longer "
        "afford to leave open. I need it closed, cleanly, by someone "
        "whose judgment nothing about her own history is likely to "
        "compromise.\""
    )},
    {"type": "body", "text": (
        "\"You do not need to explain the shape of the task to me "
        "twice,\" Ebiere said, and meant it, understanding without "
        "needing the details spelled out further exactly what closing "
        "an account cleanly had always meant in this House's own "
        "careful language. \"I only need to know when you would like it "
        "finished.\""
    )},
    {"type": "body", "text": (
        "\"As soon as it can be done without drawing attention this "
        "House cannot currently afford to draw,\" the Warden said. "
        "\"There have already been strangers found too close to this "
        "ground this season, and I have no patience left to spend "
        "waiting to learn what they actually want before this "
        "particular liability finds a way to hand it to them for free. "
        "I would like this loose end closed before it becomes one more "
        "thing those strangers, whoever they finally prove to be, ever "
        "learn to use against us.\""
    )},
    {"type": "body", "text": (
        "\"May I ask what became of the hunter who held this account "
        "before me,\" Ebiere asked, careful to keep the question sounding "
        "like simple professional curiosity rather than the sharper "
        "thing actually sitting underneath it."
    )},
    {"type": "body", "text": (
        "\"She discovered a conscience,\" the Warden said, flat, \"in a "
        "matter that never should have left room for one. I do not "
        "expect you to discover the same problem. If I am wrong about "
        "that, tell me now, honestly, and save us both the trouble of "
        "learning it the harder way Mfoniso taught me to learn it.\""
    )},
    {"type": "body", "text": (
        "\"You will not be wrong about me,\" Ebiere said, and the "
        "certainty in it was not bravado, only the plain, settled fact "
        "of a woman who had already decided, long before this letter "
        "ever reached her, exactly what kind of instrument she intended "
        "to prove herself to be the next time this House found a use "
        "for her again.\""
    )},
    {"type": "body", "text": (
        "Ebiere accepted the assignment with a small, satisfied nod "
        "that carried none of the private turmoil Mfoniso had carried "
        "into this same study only days before, no old lineage tugging "
        "quietly at her conscience, no unfinished story from any "
        "teacher's careful silence complicating a task that had always, "
        "to her, been simple. A House had wronged her once, publicly "
        "and unfairly, and she intended to answer that wrong the only "
        "way this particular House had ever taught her wrongs were "
        "properly answered, by becoming, again, too useful to ever be "
        "thrown away a second time."
    )},

    {"type": "body", "text": (
        "The Warden did not tell her everything. She did not mention "
        "Mfoniso's private theory about an old guardian and an "
        "unfinished story, judging correctly that a colder hand worked "
        "more reliably when it was not handed complications it had no "
        "use for. She did not mention the strangers found on the "
        "property, only that they existed, trusting Ebiere's own "
        "professional caution to fill in whatever shape of danger the "
        "vagueness implied. What she gave her was simpler than either "
        "of those truths, and, in the Warden's own long experience, "
        "considerably more effective. A name. A location. A deadline "
        "measured now in her own patience rather than anyone else's."
    )},
    {"type": "body", "text": (
        "She left for the main compound before dawn the next morning, "
        "traveling light and unremarkable, a second, colder threat now "
        "moving steadily toward a young woman who had no idea, folding "
        "laundry in the compound's own courtyard, that the account "
        "resting quietly over her own life had just changed hands, from "
        "a hunter who had finally learned to doubt to one who had never "
        "once, in her whole career, allowed herself the luxury of "
        "doubting anything at all, a distinction that would matter far "
        "more to what happened next than any amount of her own careful, "
        "patient counting could ever hope, entirely alone and unaided, "
        "to protect her from in the days now closing in around her."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
