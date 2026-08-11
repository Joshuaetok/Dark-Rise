#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 111: "The Weight He Could Finally Carry"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The search party pushes west
past the lost ground into country no crown map has ever touched. A
collapsed footbridge nearly costs Okonjo his life crossing a swollen
ravine, and it is Emenike, once doubted as too fragile for this search,
who holds him from falling. The rescue deepens the four men's trust in
each other under real strain. The episode closes on a set of footprints
at their own camp's edge that belong to none of them.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 111
EPISODE_TITLE = "The Weight He Could Finally Carry"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Eleven"},
    {"type": "title_ep_name", "text": "The Weight He Could Finally Carry"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Five days past the lost ground, the country stopped pretending "
        "to be anything a crown map could ever have promised. Ubani's "
        "careful survey lines had ended long before the boundary stone, "
        "and even the rough sketches Osadebe drew fresh each evening had "
        "begun to feel less like a map and more like a private record "
        "of how far four men had walked beyond anything Idoro would "
        "recognize as the world."
    )},
    {"type": "body", "text": (
        "Rain had followed them for two days straight by then, steady "
        "rather than heavy, the kind that soaked a man through slowly "
        "enough that he stopped noticing the exact moment he had gone "
        "fully wet. It had turned the low ground to standing mud and the "
        "high ground to something worse, slick red earth that gave way "
        "under a careless boot the same way it might have given way "
        "under a careful one."
    )},
    {"type": "body", "text": (
        "They had grown, in five days of walking a country with no name "
        "any of them knew, into something closer to a single traveling "
        "creature than four separate men. Osadebe led without needing "
        "to say so, reading the ground and the light the way a captain "
        "of two decades' service read anything that might endanger the "
        "men under him. Ifeanyi walked point, silent for hours at a "
        "time, his eyes doing the work his mouth rarely bothered with. "
        "Okonjo kept the party's fragile store of dried food rationed "
        "to the day, careful in a way that had once, back in Idoro, "
        "looked a little like nervousness and now simply looked like "
        "diligence no one questioned anymore."
    )},
    {"type": "body", "text": (
        "Emenike walked last, by his own choosing rather than anyone "
        "else's insistence, the position that let him watch the other "
        "three men's backs the way none of them, out of some old "
        "courtesy none of them had ever named aloud, still let him "
        "watch theirs. He had stopped, somewhere in the last five days, "
        "thinking of himself as the search party's reason for existing "
        "and started thinking of himself as one more pair of hands the "
        "search could not afford to lose, a small shift he had not "
        "noticed happening until it had already fully happened."
    )},
    {"type": "body", "text": (
        "Ifeanyi found the ravine first, the way he had found every "
        "difficult piece of ground since they left Idoro, reading the "
        "land a full stretch ahead of where his own feet actually stood. "
        "A fallen tree spanned it, wide enough to walk if a man kept his "
        "eyes forward and his weight centered, the water beneath it "
        "swollen brown and fast with two days of rain it had not asked "
        "for and clearly did not want."
    )},
    {"type": "body", "text": (
        "\"It held my weight testing it,\" Ifeanyi said, already across "
        "and turning back to watch the others come, his voice carrying "
        "easily over the water's steady rush. \"Cross one at a time. "
        "Slow. If it moves under you, stop moving and let it settle "
        "before you take the next step.\""
    )},
    {"type": "body", "text": (
        "Osadebe weighed the crossing the way he weighed every decision "
        "that put a man's life ahead of a schedule, and found, as he "
        "usually did, that the schedule lost. There was no way around "
        "the ravine he could see without a full day's detour north, and "
        "a full day was a cost the search could not easily spend on "
        "caution alone. The log would have to be trusted, carefully, "
        "one man at a time, with the water beneath it trusted not at "
        "all."
    )},
    {"type": "body", "text": (
        "Osadebe went second, then Emenike, both crossing with the "
        "particular careful economy of men who had already learned, on "
        "worse roads than this one, exactly how much confidence a body "
        "could afford to spend on a single unproven crossing. That left "
        "Okonjo alone on the far bank with the whole party watching him "
        "come, the log's true weight already tested three times over by "
        "better balanced men than himself."
    )},
    {"type": "body", "text": (
        "He was halfway across when the wood gave way beneath him, not "
        "with any warning sound worth the name, simply a soft, final "
        "settling as the trunk's rain rotted underside finally let go of "
        "whatever strength had been holding the whole log together."
    )},
    {"type": "body", "text": (
        "Okonjo went down hard against the log's broken edge, one leg "
        "already swinging out over the water, his hands scrabbling at "
        "wet bark that offered nothing solid enough to hold."
    )},
    {"type": "body", "text": (
        "Emenike moved before anyone else had finished understanding "
        "what they were looking at, dropping flat along the log's "
        "unbroken half and driving his own arm out past the point any "
        "careful man would have called safe, closing his hand around "
        "Okonjo's wrist a breath before the current could close around "
        "the rest of him."
    )},
    {"type": "body", "text": (
        "\"I have you,\" Emenike said, his voice tight with effort but "
        "entirely steady, the words aimed less at Okonjo than at his "
        "own straining arm, a promise he intended to keep whatever it "
        "cost him to keep it. \"I have you. Do not pull away from me. "
        "Let me do the pulling.\""
    )},
    {"type": "body", "text": (
        "It took Osadebe and Ifeanyi both, flat on their own stomachs a "
        "moment later, to finally drag the two of them clear of the "
        "broken log and back onto solid ground, Okonjo coughing river "
        "water and shaking too hard at first to stand, Emenike's own arm "
        "already darkening where the strain of holding had bruised it "
        "down to the bone."
    )},
    {"type": "body", "text": (
        "No one spoke for a long moment afterward, the four of them "
        "simply breathing on the wet ground while the ravine kept "
        "running past them exactly as indifferently as it had a minute "
        "earlier, before any of this had happened at all."
    )},
    {"type": "body", "text": (
        "They made camp early that evening, well short of the distance "
        "Osadebe had hoped to cover, and no one argued the decision. "
        "Okonjo sat close to the fire with a blanket around his "
        "shoulders and a wrenched ankle already swelling, quiet in a way "
        "that had nothing to do with the cold."
    )},
    {"type": "body", "text": (
        "\"Chidebe told me once you were not strong enough for this "
        "search,\" Okonjo said finally, not looking up from the fire, "
        "his voice rough with something that was not quite embarrassment "
        "and not quite gratitude but sat close to both. \"I did not "
        "argue with him. I should have.\""
    )},
    {"type": "body", "text": (
        "Emenike turned the bruise on his own forearm over in the "
        "firelight, studying it with an odd, distant satisfaction, the "
        "look of a man weighing a cost he had decided, without much "
        "debate, was worth exactly what it cost. \"He was not entirely "
        "wrong to worry,\" he said, quiet but unhurried, testing the "
        "words as he spoke them. \"I was not strong enough for this "
        "search when he said it. I am not certain I am strong enough "
        "for it now. But strong enough was never really the question "
        "that mattered. Whether I would stop trying was.\""
    )},
    {"type": "body", "text": (
        "Osadebe, watching the exchange with the same quiet attention he "
        "gave to everything that might matter later, said nothing at "
        "all, but something in the set of his shoulders eased for the "
        "first time since the log had given way, the particular relief "
        "of a captain who had just watched his own judgment about a man "
        "prove itself correct in the worst possible circumstances."
    )},
    {"type": "body", "text": (
        "\"For what it is worth,\" Osadebe said, breaking his own "
        "silence at last, his voice carrying the particular weight of a "
        "captain who did not offer praise cheaply, \"Chidebe was wrong "
        "about one thing today, and I intend to tell him so myself when "
        "we are home to say it in person. A man does not have to be the "
        "strongest arm in a search party to be the arm it cannot afford "
        "to be without. Today proved which one you actually are, "
        "Emenike, and it was never really in doubt to the three of us "
        "walking beside you.\""
    )},
    {"type": "body", "text": (
        "Ifeanyi, practical as ever, used the fire's light to check "
        "Okonjo's ankle properly, pronounced it wrenched rather than "
        "broken, bound it tight with a strip of cloth, and declared, "
        "with the flat authority of a man who had grown up setting his "
        "own family's injuries long before any of them could afford a "
        "healer, that a full day's rest would see it fit to walk on "
        "again, if not fit to run."
    )},
    {"type": "body", "text": (
        "It was Ifeanyi, too, circling the camp's edge one last time "
        "before he judged it safe enough to finally sleep, who found the "
        "footprints."
    )},
    {"type": "body", "text": (
        "They were fresh, no more than a day old by the sharpness of "
        "their edges in the softened ground, five separate sets crossing "
        "the party's own trail at an angle that suggested purpose rather "
        "than accident, boots rather than bare feet, a party moving with "
        "the kind of discipline no ordinary traveler bothered to keep in "
        "country this far from anything worth traveling to."
    )},
    {"type": "body", "text": (
        "Osadebe crouched over them for a long time in the failing "
        "light, saying nothing, turning the same private calculation "
        "over that had kept him alive across two decades of the crown's "
        "service. Whoever had left these tracks was moving in the same "
        "direction the search party itself was moving, on ground so "
        "far from any known road that coincidence had stopped being a "
        "comfortable explanation for anything."
    )},
    {"type": "body", "text": (
        "\"Traders,\" Ifeanyi offered quietly, crouching beside him to "
        "study the same marks, though his tone carried none of the "
        "conviction the word usually deserved. \"Or hunters working "
        "this ground for something other than the four of us.\" He did "
        "not sound as though he believed either explanation himself, "
        "and Osadebe did not ask him to."
    )},
    {"type": "body", "text": (
        "What unsettled Osadebe most was not the tracks themselves but "
        "how little effort had gone into hiding them. A House that knew "
        "how to burn a maker's mark into binding cloth and vanish a "
        "settlement's whole story behind three centuries of undisturbed "
        "grass did not, in his experience, leave five days of careless "
        "footprints across open ground by accident. Either these "
        "travelers had no idea anyone might be following this bearing "
        "at all, or they had every reason to believe that whoever did "
        "follow it would never live long enough to report what they had "
        "found."
    )},
    {"type": "body", "text": (
        "He did not tell the others yet how old the second, fainter set "
        "beneath the fresh one looked, weeks rather than a single day, "
        "as though this exact stretch of forgotten ground was not merely "
        "crossed once by chance but walked, regularly, by someone who "
        "already knew precisely where it led."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
