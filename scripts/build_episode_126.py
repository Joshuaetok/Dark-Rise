#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 126: "The Water She Finally Crossed"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The compound's alert since
the patrol clash has scrambled every routine Ijeoma spent months
learning, and she reads the chaos as her last real window rather than
new danger. Using a length of dock rope to cross the water that stopped
her once before, she clears the wall itself for the first time, only to
be caught in the open ground beyond it. Cliffhanger.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 126
EPISODE_TITLE = "The Water She Finally Crossed"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Six"},
    {"type": "title_ep_name", "text": "The Water She Finally Crossed"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "The compound had not settled properly in three full days, "
        "guards doubled again on top of watches already doubled once "
        "before, unfamiliar men moving through the courtyard at hours "
        "no schedule Ijeoma had ever mapped accounted for, the "
        "housemistress herself short tempered in a way two whole "
        "seasons of careful observation had never once shown Ijeoma "
        "before this week."
    )},
    {"type": "body", "text": (
        "She did not know what had actually happened to unsettle this "
        "House so completely, only that something had, and that the "
        "Factor's careful warning about a closing window now sat inside "
        "her with a weight it had not carried when he first spoke it. A "
        "House this distracted made mistakes a calmer House never "
        "would have made. It also, she suspected, made decisions about "
        "difficult guests faster than a calmer House ever would have "
        "made them."
    )},
    {"type": "body", "text": (
        "She had spent the two weeks since the Factor's visit doing "
        "the one thing her first failed climb had taught her she still "
        "needed, solving the water rather than merely reaching it. Dock "
        "duty had given her the answer eventually, watching the "
        "current pull debris past the wall's blind corner at a "
        "particular hour each evening when the river's own level "
        "dropped low enough to expose a narrow spit of submerged rock "
        "she had never once been able to see from above."
    )},
    {"type": "body", "text": (
        "She had tested the current's own pattern six separate "
        "evenings before she trusted it enough to plan around, standing "
        "at the dock's edge with an armful of laundry as excuse, "
        "watching a thrown scrap of broken wood ride the pull past the "
        "wall's blind corner and, every single evening at the same "
        "falling hour, catch briefly against something just beneath "
        "the surface before the current carried it on. Rock, she had "
        "finally decided, worn smooth and shallow enough to stand on, "
        "the river's own level dropping just far enough each evening to "
        "expose it for the length of time it took a careful woman to "
        "cross."
    )},
    {"type": "body", "text": (
        "A length of good rope, coiled small enough to hide inside a "
        "folded bolt of cloth, had taken her four separate dock shifts "
        "to steal without anyone noticing the theft. She had it now, "
        "wound tight beneath her own clothes, waiting for exactly the "
        "kind of chaotic night this House's own unsettled fear had "
        "finally handed her."
    )},
    {"type": "body", "text": (
        "She had taken it a hand span at a time, coiling a small extra "
        "loop into her own work each shift and tucking it beneath a "
        "loose fold of her own worn skirt before the day's count was "
        "ever taken, trusting that a household grown careless about "
        "counting a guest's clothing would stay careless about counting "
        "rope no one had any particular reason to inventory closely. "
        "It was, she thought, turning the coiled length over in the "
        "dark of her own small room on the third night of the "
        "compound's unsettled fear, the single most dangerous thing she "
        "had ever stolen from anyone, and also the smallest, the kind "
        "of theft that would never once show up on any ledger unless "
        "someone already knew exactly what to look for."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She moved that night the same patient way she had moved every "
        "night since the first failed climb, unhurried, unremarkable, "
        "a shape in the dark that belonged wherever it happened to be "
        "standing. The eastern gate's guard, rattled like everyone else "
        "by three days of upended routine, left his post at a ragged, "
        "distracted version of his old habitual minute, and Ijeoma "
        "used it without hesitation, crossing to the wall's bad corner "
        "before her own count had finished reaching its usual number."
    )},
    {"type": "body", "text": (
        "The climb itself felt almost familiar now, her hands finding "
        "the same broken holds they had found once before, though her "
        "heart still hammered exactly as hard as it had the first "
        "time, fear apparently uninterested in how many times a body "
        "had already survived the same danger."
    )},
    {"type": "body", "text": (
        "At the top, she did not let herself pause the way she had "
        "paused once before, crouched too long in the false safety of "
        "believing the hardest part was already finished. She fed the "
        "rope down the wall's outer face instead, anchored around the "
        "same broken stone her hands had climbed by, and lowered "
        "herself toward the water with her whole body trembling from "
        "an effort she refused to let slow her down."
    )},
    {"type": "body", "text": (
        "The submerged spit of rock held exactly where her dock "
        "counting had promised it would, cold water rising only to her "
        "knees rather than swallowing her the way the darkness had once "
        "threatened to swallow her, and for three long strides across "
        "black water she did not dare believe was actually shallow, "
        "Ijeoma crossed ground no one from this House had ever once "
        "seen a prisoner cross before."
    )},

    {"type": "body", "text": (
        "Halfway across, her foot found a gap in the submerged rock "
        "that her six careful evenings of watching had never once "
        "revealed, a sudden drop that swallowed her leg to the thigh "
        "and nearly took the rest of her with it into water she still "
        "could not read even now, this close, this committed. She held "
        "the rope with both hands and did not let the panic reach her "
        "voice, forcing her weight back onto the solid rock behind her "
        "and testing the next step twice before trusting it with her "
        "full weight."
    )},
    {"type": "body", "text": (
        "She reached the far bank with her legs numb and her whole "
        "body shaking, and stood, for one suspended moment, on ground "
        "that belonged to no House's ledger at all."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She did not allow herself to celebrate it. Two seasons of "
        "patient counting had taught her that the moment a plan finally "
        "worked was exactly the moment carelessness cost the most, and "
        "she moved immediately into the tree line beyond the water, "
        "putting distance between herself and a wall she had just, "
        "impossibly, actually cleared."
    )},
    {"type": "body", "text": (
        "It was the unfamiliar patrol, the same kind of scrambled, "
        "reassigned watch that had made her own escape possible in the "
        "first place, that found her before she had covered even a "
        "hundred careful paces, two guards walking a stretch of ground "
        "outside the wall that no schedule she had ever mapped had told "
        "her to expect anyone walking at all."
    )},
    {"type": "body", "text": (
        "She had counted, across two whole seasons of watching this "
        "House's ordinary rhythm, exactly zero patrols ever assigned to "
        "the ground beyond the wall's outer face, and she understood, "
        "hearing footsteps she had no honest way to have predicted, "
        "that the same chaos which had opened her own door out of the "
        "compound had opened an equally unpredictable door for the men "
        "now guarding it. A settled House was a House whose patterns "
        "could be learned. An unsettled one made its own rules new each "
        "night, and she had gambled everything on a version of this "
        "ground that no longer entirely existed."
    )},
    {"type": "body", "text": (
        "\"There,\" one of them called, sharp and sudden, a torch "
        "swinging toward the sound of her own too hurried breath before "
        "she had managed to freeze completely still. \"Movement, by the "
        "tree line. Someone is out here.\""
    )},
    {"type": "body", "text": (
        "Ijeoma ran."
    )},

    {"type": "body", "text": (
        "She thought, in the strange, stretched clarity that fear "
        "sometimes offered a person instead of panic, of her mother "
        "teaching her to run a market stall's full inventory count "
        "twice as fast as any of the other traders' daughters, insisting "
        "that speed without accuracy was worthless and accuracy without "
        "speed was worthless in a different way, and that a trader who "
        "mastered both together could always find her way clear of a "
        "bad bargain before it finished closing around her. She had "
        "never once imagined the lesson would matter more to her own "
        "legs than to her own hands."
    )},
    {"type": "body", "text": (
        "She did not know this ground, had never once been permitted "
        "to learn it the patient way she had learned every inch of the "
        "compound behind her, and every root and hollow she stumbled "
        "over in the dark cost her precious distance she could not "
        "afford to lose. Behind her, the shout had already become "
        "several shouts, torchlight multiplying against the tree trunks "
        "in a pattern that told her, with brutal clarity, exactly how "
        "many men had just been added to the chase."
    )},
    {"type": "body", "text": (
        "She broke from the tree line into open ground she had not "
        "expected, moonlight suddenly full and unforgiving across her "
        "own exposed shape, and heard, behind her, a voice close enough "
        "now to carry real triumph in it."
    )},
    {"type": "body", "text": (
        "\"I have her,\" the voice called, closing fast. \"She is here, "
        "in the open, she cannot outrun us across ground this bare.\""
    )},
    {"type": "body", "text": (
        "Ijeoma did not stop. She had promised herself, coiling that "
        "stolen rope one careful hand span at a time across four "
        "separate dock shifts, that she would rather be caught still "
        "running than caught having already surrendered, and she held "
        "to that promise now with everything her burning legs still "
        "had left to give them, the open ground stretching ahead of "
        "her with no cover anywhere she could see, torchlight closing "
        "from behind at a pace her own exhausted body could not "
        "possibly match for much longer."
    )},
    {"type": "body", "text": (
        "A hand closed hard around her arm from the side, someone she "
        "had not even seen approaching in the confusion of torchlight "
        "and shadow, and Ijeoma twisted against the grip with every bit "
        "of strength two seasons of patient counting had never once "
        "let her spend on anything but waiting, and felt, for one "
        "terrible, suspended instant, the whole careful plan collapse "
        "around her at the exact moment it had finally, impossibly, "
        "almost worked."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
