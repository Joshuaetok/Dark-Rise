#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 106: "One Mission Now"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): Act 1's hook episode. A
second look inside the hillside chamber turns up a maker's mark
burned into the restraint cloth, one the party recognizes because
they have seen its twin before, on cloth used to bind captives taken
by the Concern's agents. The search for the presence's lost people and
the search for Ijeoma are, from this point, one mission.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 106
EPISODE_TITLE = "One Mission Now"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Six"},
    {"type": "title_ep_name", "text": "One Mission Now"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Osadebe could not sleep for thinking about the chamber, and so "
        "before first light he went back to it alone, against every "
        "instinct that told him to leave a place like that sealed once "
        "it was sealed. He told himself he was only confirming his own "
        "notes were accurate. He knew, walking up the slope in the gray "
        "hour before dawn, that this was not entirely true."
    )},
    {"type": "body", "text": (
        "The door opened as easily as it had the day before. Inside, by "
        "the thin light of his own small lamp, he went back to the "
        "folded stack of binding cloth that had unsettled Emenike most, "
        "and this time, instead of leaving it undisturbed, he lifted "
        "the topmost piece and turned it over in his hands."
    )},
    {"type": "body", "text": (
        "Burned into one corner, small and deliberate, was a mark. Not "
        "the spiral. Something else, a simple double curve like two "
        "waves meeting, branded into the cloth the way a trader marks "
        "goods that belong to a particular House rather than to the "
        "open market. Osadebe stared at it a long moment before the "
        "recognition landed, and when it did, it landed hard enough "
        "that he had to sit down on the chamber's stone floor to absorb "
        "it properly."
    )},
    {"type": "body", "text": (
        "He had seen that mark before. Not on old cloth in a forgotten "
        "hillside room, but fresh, on a length of binding taken off a "
        "market trader's wrist during the very first informant "
        "investigation at Idoro, seasons ago, evidence logged and filed "
        "and never fully explained, a mark none of the crown's records "
        "had matched to any known trading concern at the time."
    )},
    {"type": "body", "text": (
        "He woke the other three himself, unwilling to wait for the sun "
        "to do it for him. \"Look at this,\" he said, holding the cloth "
        "out flat so the mark caught what little light there was. "
        "\"Tell me I am wrong.\" Emenike took one look and went very "
        "still, the particular stillness of a man recognizing something "
        "he had hoped never to see again. \"You are not wrong,\" he "
        "said. \"I have seen this mark. Not on cloth. On the seal of a "
        "message left for me at the drop stone, more times than I ever "
        "wanted to count.\""
    )},
    {"type": "body", "text": (
        "Ifeanyi took the cloth from Osadebe's hands and studied it the "
        "way he studied game trails, turning it slowly, tracing the "
        "burned line with one careful finger. \"A House mark,\" he "
        "said. \"Old enough to have been used here three centuries ago, "
        "and current enough to still be sealing messages to Emenike a "
        "season past. That is not two Houses doing similar work. That "
        "is one House, doing the same work it has always done, for "
        "longer than any of us imagined possible.\""
    )},
    {"type": "body", "text": (
        "Okonjo said the thing none of them wanted to be the one to say "
        "aloud first. \"Then whoever holds Ijeoma,\" he said, \"is the "
        "same House, or the same bloodline of it, that emptied this "
        "town three hundred years ago. We did not walk toward two "
        "different mysteries on the same bearing by accident. We walked "
        "toward one mystery that has simply had three hundred years to "
        "grow larger.\""
    )},
    {"type": "body", "text": (
        "No one spoke for a while after that. The chamber's early "
        "morning cold seemed to settle deeper into all four of them at "
        "once, the particular cold of understanding a thing rather than "
        "merely fearing it, and Osadebe found himself thinking, "
        "uselessly, of every soldier at Idoro sleeping easy in the "
        "belief that the crown's doubled garrison had made the village "
        "safe from whatever this was."
    )},
    {"type": "body", "text": (
        "Osadebe sat with the cloth in his lap for a long while before "
        "he spoke again, working through the shape of what this meant "
        "for the mission he had been sent on. \"We came west to find one "
        "girl,\" he said finally. \"We may have just found the House "
        "that has been doing this to entire villages since before "
        "Idoro existed as Idoro. That is not a smaller task than the one "
        "we left home with. It is a much larger one wearing the same "
        "name.\""
    )},
    {"type": "body", "text": (
        "Emenike folded the cloth back exactly as he had found it, "
        "carefully, as if the folding itself were a kind of respect "
        "owed to whoever it had once been meant to bind. \"It does not "
        "change what I came here to do,\" he said, his voice steady in "
        "a way it had not been since the informant confession that had "
        "first cost him the household's trust. \"It only means Ijeoma "
        "was never the beginning of this, and finding her will not be "
        "the end of it either. But she is still the reason I am "
        "walking, and I am not walking any less for knowing the road is "
        "longer than I thought.\""
    )},
    {"type": "body", "text": (
        "They broke camp for the last time at the lost ground's edge "
        "that morning, Osadebe marking one final note on his map before "
        "folding it away, the bearing continuing on past the ruined "
        "settlement toward whatever lay another stretch of days beyond "
        "it. He did not yet know how many more days that would be. He "
        "knew only that the search and the rescue had stopped being two "
        "separate promises somewhere in that hillside chamber, and had "
        "become, from this morning forward, a single debt owed to both "
        "a living girl and three centuries of the dead."
    )},
    {"type": "body", "text": (
        "That night, camped a full day's walk beyond the clearing for "
        "the first time since they had found it, Emenike dreamed, "
        "though he would not remember it clearly by morning, of a boy "
        "his own age standing at the edge of a shrine hut far to the "
        "east, watching him with an expression that was neither warning "
        "nor welcome, only recognition, as if something on the other "
        "end of a thread neither of them could see had finally felt the "
        "weight of what the day had uncovered."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Downriver, on the same morning Osadebe carried a folded length "
        "of branded cloth back down a hillside six days west of "
        "everything she had ever known, Ijeoma was counting the eastern "
        "gate's gap for the ninth day in a row. It had not changed. "
        "The same guard, the same minutes, the same small, private "
        "carelessness that no one above him had ever bothered to "
        "correct."
    )},
    {"type": "body", "text": (
        "She had stopped thinking of it only as a gap and started "
        "thinking of it as a plan, though she had not yet let the word "
        "escape become part of the plan's shape in her own head, "
        "superstitious in a way she would not have admitted to her "
        "mother. Naming a thing too early, her mother always said, was "
        "how a trader lost a good price before the bargaining even "
        "started."
    )},
    {"type": "body", "text": (
        "What she needed now was not more watching. She had watched "
        "enough. What she needed was a reason to be near the eastern "
        "wall at the exact minute the gap opened, without that reason "
        "drawing a second glance from anyone else in the compound, "
        "guard or servant or the Factor himself, who had taken, these "
        "last days, to walking the courtyard's edge at odd hours in a "
        "way she had noticed but not yet understood."
    )},
    {"type": "body", "text": (
        "She found her reason two mornings later, in the laundry line "
        "strung between the kitchen and the eastern wall, close enough "
        "to the guard's post that a woman gathering dried cloth would "
        "have every excuse to be standing exactly where Ijeoma needed "
        "to stand. She asked the same servant girl who had spoken to "
        "her once before, carefully, whether the laundry work was ever "
        "given to the guest rather than only to House staff."
    )},
    {"type": "body", "text": (
        "The girl's answer came slow and thoughtful and searching, the tone of someone "
        "weighing a small kindness against a larger risk she had not "
        "been told the shape of. \"It is not "
        "forbidden,\" she said finally, quiet, glancing once toward the "
        "nearest guard before she let herself continue. \"No one has ever asked, "
        "because no one has ever really wanted to. If you truly wanted to, I could "
        "ask the housemistress for you. She likes hands that keep "
        "busy.\" Ijeoma thanked her with the same careful blankness she "
        "used for everything now, giving away nothing of how much the "
        "offer was actually worth to her."
    )},
    {"type": "body", "text": (
        "That evening, alone in the small room that had been her whole "
        "world for two seasons, Ijeoma allowed herself, for exactly as "
        "long as it took to fold one length of her own worn cloth, to "
        "imagine the moment itself. Not the escape. Just the gap. "
        "Standing at the wall's bad corner with her hands full of "
        "someone else's laundry, watching the guard walk away from his "
        "post the way he always did, and understanding, in the space "
        "between one breath and the next, that the door was finally, "
        "actually, open."
    )},
    {"type": "body", "text": (
        "She put the thought carefully away before it could grow past "
        "what was actually useful to her. A plan built on hope instead "
        "of counting was exactly "
        "the kind of careless plan that got a person caught, and she had not "
        "survived two whole seasons of patient counting only to lose everything now "
        "to a single moment of wanting too badly. Tomorrow she would ask about "
        "the laundry. Tonight, she told herself, was only for sleeping, "
        "though sleep, when it eventually came for her at last, brought "
        "her nothing at all but the same wall, the very same corner, "
        "over and over again, patient as counting."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
