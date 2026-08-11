#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 109: "The Wall She Almost Cleared"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Ijeoma's first real escape
attempt. She clears her holding room and the compound's eastern wall
itself, only to find the far side is water she cannot read in the dark,
and retreats rather than gamble blind. The eastern gate's guard sees her
return and says nothing. The Factor finds the evidence at dawn and
scuffs it smooth. First thread of an inside ally; the Factor's second
small act of conscience.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 109
EPISODE_TITLE = "The Wall She Almost Cleared"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Nine"},
    {"type": "title_ep_name", "text": "The Wall She Almost Cleared"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"The laundry line is yours from today,\" the housemistress had "
        "said, brisk but not unkind, the first time in two seasons she "
        "had spoken to Ijeoma directly rather than around her. Ijeoma "
        "had thanked her with the same careful blankness she used for "
        "everything now, and had spent every one of the three days since "
        "doing exactly what the work asked of her and nothing more, "
        "patient in front of anyone watching, counting in the part of "
        "her mind no one else could see."
    )},
    {"type": "body", "text": (
        "She chose the fourth night. No moon, the sky low with cloud "
        "that swallowed even the compound's own torchlight past a few "
        "paces. Rain earlier had softened the packed earth by the "
        "eastern wall, and from her window she had watched the household "
        "staff hurry the last of the drying cloth in before the weather "
        "turned, leaving the line strung bare and the ground beneath it "
        "churned soft enough to hold no clear print by morning."
    )},
    {"type": "body", "text": (
        "Getting out of the small room that had been her whole world "
        "for two seasons took less courage than she had expected and "
        "more patience than she had planned for. The door was never "
        "locked from outside, only watched, and the watching, across "
        "nine days of counting, thinned to almost nothing in the hour "
        "after the household's evening meal, when even guards grew "
        "hungry for their own supper."
    )},
    {"type": "body", "text": (
        "She moved through the compound the way she had once moved "
        "through her mother's crowded market stalls as a girl, "
        "unhurried, unremarkable, a person clearly going somewhere "
        "ordinary. Past the kitchen's banked coals, past the well, "
        "silent and black, to the laundry line, where she gathered an "
        "armful of cloth she had already folded once that morning and "
        "carried it toward the eastern wall as though the hour made "
        "perfect sense."
    )},
    {"type": "body", "text": (
        "The eastern gate's guard left his post at the expected minute, "
        "the same private carelessness that had never once, in over two "
        "weeks of watching, failed her. Ijeoma did not look toward the "
        "gap he left behind. Her mother had taught her that too, that a "
        "person who looks too hard at an open door tells everyone nearby "
        "exactly where the door is."
    )},
    {"type": "body", "text": (
        "The wall's bad corner waited exactly where her counting had "
        "promised, a stretch where the mud brick had been patched twice "
        "by hands less careful than the House usually paid for, broken "
        "into hand holds a patient climber could find by feel alone in "
        "the dark. She set the folded cloth down at its base, wiped her "
        "palms once against her own skirt, and began to climb."
    )},
    {"type": "body", "text": (
        "It took longer than she had let herself imagine. Her hands "
        "found each hold the way her feet had once found each stone "
        "crossing a flooded market road, tested before trusted, weight "
        "shifted only when she was certain. Twice her foot slipped "
        "against wet brick and twice she held, breath caught, waiting "
        "to learn whether the small sound had reached anyone at all. It "
        "had not."
    )},
    {"type": "body", "text": (
        "She reached the top of the wall with her arms shaking and her "
        "breath loud in her own ears, and for one long moment, crouched "
        "low against the wet brick with the whole dark compound spread "
        "small and sleeping behind her, Ijeoma let herself believe it "
        "might actually be this simple."
    )},
    {"type": "body", "text": (
        "Then she looked down the far side, and understood at once why "
        "no one had ever bothered building a second guard post at this "
        "particular corner of the wall."
    )},
    {"type": "body", "text": (
        "The ground she had pictured, ordinary ground she could drop to "
        "and run across in the dark, was not there. Below her the wall "
        "fell away into black water, a moat or drainage cut she had "
        "never once seen from inside the compound, its surface unreadable "
        "in the darkness, its depth and its floor a complete unknown to "
        "a woman who had spent her whole life on dry market roads. She "
        "could not tell, crouched there with her heart loud in her "
        "chest, whether the water stood knee deep or higher than she "
        "was tall, whether its bed was mud or stone, whether anything "
        "with teeth called it home."
    )},
    {"type": "body", "text": (
        "A trader's daughter did not spend two whole seasons of patient "
        "counting only to throw the whole careful sum away on a single "
        "blind guess in the dark. Ijeoma had told herself that exact "
        "sentence once before, folding cloth in her own small room, and "
        "she made herself believe it again now, crouched on top of a "
        "wall with freedom close enough to smell and no way to measure "
        "the cost of reaching for it. She would not jump blind into "
        "water she could not read."
    )},
    {"type": "body", "text": (
        "Climbing down was slower than climbing up had been, every hold "
        "tested twice instead of once, her whole body aching with the "
        "effort of not simply letting go and trusting the fall. By the "
        "time her feet found the churned earth at the wall's base again, "
        "the sky to the east had begun, very faintly, to gray."
    )},
    {"type": "body", "text": (
        "She was three steps from the laundry line, the folded cloth "
        "back in her arms as though it had never left them, when she "
        "saw him. The eastern gate's guard, back at his post ahead of "
        "when her counting said he should have been, stood very still "
        "in the gray half light with his eyes already on her."
    )},
    {"type": "body", "text": (
        "Neither of them spoke. Ijeoma made herself walk the last three "
        "steps at exactly the pace she would have walked them on any "
        "ordinary morning, and set the cloth down on the line as though "
        "laundry, and only laundry, had ever been her purpose there. The "
        "guard's gaze followed her the whole distance and gave away "
        "nothing at all, not alarm, not suspicion, nothing Ijeoma could "
        "read with any of the two seasons of patience she had spent "
        "learning to read this House."
    )},
    {"type": "body", "text": (
        "She walked back to her small room with her spine straight and "
        "her hands steady, and did not allow herself to shake until the "
        "door had closed behind her. Then she sat on the floor with her "
        "back against the wall she had just failed to clear, and let "
        "the shaking come, and understood, with a clarity that felt "
        "almost like grief, that she had learned two things tonight "
        "instead of one. The wall could be climbed."
    )},
    {"type": "body", "text": (
        "And someone had watched her climb it, and said, so far, "
        "nothing at all."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE FACTOR
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Factor had taken, these last weeks, to walking the "
        "courtyard's edge in the hour before the household properly "
        "woke, a habit he had never examined closely enough to name, "
        "and it was in that hour, on that particular morning, that he "
        "noticed the mud."
    )},
    {"type": "body", "text": (
        "Not much of it. A smear against the wall's patched corner that "
        "had no honest reason to be there, laundry set down at an angle "
        "no tired servant would have chosen, ground churned in a "
        "pattern that told a plain story to anyone who had spent forty "
        "years learning to read what disturbed ground actually meant. "
        "He had signed enough transport manifests in his career to read "
        "a trail the way another man read a face."
    )},
    {"type": "body", "text": (
        "He stood over it for a long moment, turning the small, cold "
        "weight of a decision he had not yet fully made. He could "
        "report it to the guard captain within the hour and let the "
        "House's usual machinery close whatever gap had opened here. Or "
        "he could do nothing, the way he had already begun, in small "
        "ways he still could not name properly even to himself, to do "
        "nothing about a great many things this House asked of him."
    )},
    {"type": "body", "text": (
        "He scuffed the mud smooth with the side of his own sandal, "
        "unhurried, the gesture of a man tidying a courtyard rather than "
        "erasing evidence, and walked on toward the kitchen as though he "
        "had seen nothing worth his attention at all. It was the second "
        "time in one season he had chosen silence over the ledger. He "
        "did not yet know it would not be the last."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: THE GUARD
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The guard did not sleep well that day, lying on his mat in the "
        "men's quarters with the sun already high and hot against the "
        "roof above him, turning over the same three steps of Ijeoma's "
        "walk back to the laundry line until they wore smooth in his "
        "mind the way a much handled coin wears smooth."
    )},
    {"type": "body", "text": (
        "He told himself, the way he had told himself every morning for "
        "eleven days now, that a man who reported every small thing "
        "kept his post longer than a man who did not, and that this had "
        "been a small thing, a servant out early, nothing worth the "
        "guard captain's time. It was, he understood even as he told "
        "himself so, the first lie he had allowed himself in three "
        "years of honest service to this House."
    )},
    {"type": "body", "text": (
        "He had a sister once. He did not let the rest of that thought "
        "finish forming, not even alone, not even now, and turned his "
        "face to the wall instead and made himself, at last, close his "
        "eyes."
    )},
    {"type": "body", "text": (
        "Downriver and upriver both, no one yet knew what he had chosen "
        "not to report. Not the Warden, tallying a ledger that still "
        "listed Ijeoma as an asset undecided. Not Mfoniso, somewhere on "
        "the river road south, the very gate this guard had failed to "
        "watch growing a little closer with every mile she walked. Not "
        "the search party, pressing west past ground already emptied "
        "once by hunters, now hunting the same House that had emptied "
        "it. Only a girl who had learned to count everything knew that "
        "this particular wall, and this particular man, could both be "
        "climbed."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
