#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 116: "A Fortress Wearing a Market's Face"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The search party finally
sights the Concern's disguised headquarters from a wooded ridge, and
finds it far larger and far better guarded than anything four crown
soldiers prepared for. No Section 3.5 violations: story-time is tracked
only in-world (days, seasons), never as spoken episode numbers.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 116
EPISODE_TITLE = "A Fortress Wearing a Market's Face"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Sixteen"},
    {"type": "title_ep_name", "text": "A Fortress Wearing a Market's Face"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "They had walked three more days since the footprints, "
        "watching the older, fainter trail beneath the fresh one grow "
        "steadily busier rather than fainter, more crossings, more "
        "signs of regular traffic, until even Okonjo, who had wanted "
        "badly to believe in traders or ordinary hunters, stopped "
        "offering either explanation aloud. Osadebe had begun leaving a "
        "small cairn of stones at each night's camp, an old habit from "
        "his earliest years of crown service, in case a courier ever "
        "did manage to catch up to a party this far past any road worth "
        "the name. None of them expected one to."
    )},
    {"type": "body", "text": (
        "Ifeanyi smelled the river before any of them saw it, a change "
        "in the air thick and green and faintly rotten in the way only "
        "slow water ever managed, and called the party to a careful "
        "halt a full afternoon's walk short of wherever that smell was "
        "actually coming from. They had learned, across many hard days "
        "on this bearing, to trust his nose over their own eyes."
    )},
    {"type": "body", "text": (
        "They approached the last stretch at dusk the following "
        "evening, moving slow and low along a wooded ridge that "
        "Osadebe judged, correctly, would give them a clear look down "
        "onto whatever waited below without putting any of them in "
        "open ground first. It was Okonjo, still favoring the ankle he "
        "had wrenched at the ravine, who reached the ridge's edge "
        "first, and it was Okonjo whose sharp, indrawn breath told the "
        "other three, before any of them had actually seen it "
        "themselves, that they had finally found what they had walked "
        "this far to find."
    )},
    {"type": "body", "text": (
        "Below them, spread across a wide bend in the river, sat "
        "something built to look, at a careless glance, like nothing "
        "more than an ordinary trading post. Warehouses. A modest "
        "wooden dock crowded with river craft. Sacks of rice and palm "
        "produce stacked in the open the way any honest merchant "
        "stacked his goods for a passing buyer to see and trust."
    )},
    {"type": "body", "text": (
        "A careless glance, though, was not the kind of glance four "
        "trained crown soldiers were in the habit of giving anything."
    )},
    {"type": "body", "text": (
        "Osadebe counted the outer wall first, a proper defensive wall "
        "rather than a merchant's simple fence, stone footed and timber "
        "topped, running the compound's full perimeter with a "
        "discipline no honest trading post would ever have troubled "
        "itself to build. He counted guard positions next, more than "
        "twice what the largest legitimate warehouse he had ever "
        "personally overseen in Udo would have employed, spaced along "
        "the wall at intervals that spoke of a captain who understood "
        "sightlines and coverage the way a crown officer understood "
        "them, not the way a merchant's hired watchman ever bothered "
        "to."
    )},
    {"type": "body", "text": (
        "Sound reached them too, carried up the ridge on the same "
        "evening air that brought the river smell, voices calling "
        "ordinary instructions across a loading dock, the creak of a "
        "laden cart, a dog barking somewhere behind the outer wall at "
        "nothing any of them could see. It was, Emenike thought, "
        "listening to it, the precise sound of an ordinary evening "
        "going on exactly as ordinary evenings always did, in a place "
        "that was very plainly not ordinary at all, and the mismatch "
        "between the two unsettled him more than open hostility would "
        "have."
    )},
    {"type": "body", "text": (
        "\"That is not a trading post,\" Emenike said quietly, the "
        "words coming out flatter than he meant them to, the sound of a "
        "man arriving at a conclusion he had been half expecting for "
        "two full seasons and still was not entirely prepared to hear "
        "confirmed aloud. \"That is a fortress wearing a market's "
        "face.\""
    )},
    {"type": "body", "text": (
        "No one argued with him. Ifeanyi, counting patrol patterns with "
        "the same patient attention he gave to reading any difficult "
        "ground, noted a rotation of paired guards walking the wall's "
        "full circuit on a schedule tight enough that no single gap "
        "along its length stayed unwatched for more than a few careful "
        "minutes at a stretch."
    )},
    {"type": "body", "text": (
        "\"Four of us,\" Osadebe said, half to himself, doing the same "
        "grim arithmetic every man on that ridge was already doing in "
        "his own head. \"Against a wall that size, a garrison that "
        "size, and however many more men we cannot see from here inside "
        "it. This is not a search party's problem anymore. This is a "
        "crown army's problem, and I do not have a crown army with "
        "me.\""
    )},
    {"type": "body", "text": (
        "Okonjo, still half breathless from the climb and the sight "
        "both, asked the question none of the other three had quite let "
        "themselves ask aloud yet. \"Is she in there. Is that where "
        "Ijeoma actually is.\""
    )},
    {"type": "body", "text": (
        "\"I do not know,\" Osadebe admitted, and found, saying it, "
        "that the honesty cost him more than he expected it to. \"I "
        "know only that this is the bearing, and that this is the "
        "kind of place that bearing was always going to lead us "
        "toward, sooner or later. Whether she is inside this exact "
        "wall or another one further on, I cannot promise any of you. "
        "I can promise you we are not walking away from it without "
        "finding out.\""
    )},
    {"type": "body", "text": (
        "They watched the compound for the better part of an hour "
        "before full dark finally forced them back from the ridge's "
        "open edge, cataloguing everything Osadebe's careful sketching "
        "hand could capture by the fading light, gate positions, the "
        "dock's own separate watch, a second, smaller wall visible "
        "toward the compound's inner heart that suggested whatever sat "
        "behind it mattered more to this House than warehouses full of "
        "rice ever could."
    )},
    {"type": "body", "text": (
        "Emenike stared longest at that inner wall, unable to look away "
        "from it even after Osadebe finally called them back into the "
        "trees, some old, worn instinct in him insisting, without any "
        "proof he could point to, that whatever this House valued "
        "enough to wall twice over was exactly the thing he had walked "
        "this whole impossible distance to find."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They made a cold camp well back from the ridge that night, no "
        "fire, no risk of smoke against a sky this close to a garrison "
        "that size, and ate what little remained of their dried "
        "stores in a silence none of them seemed inclined to break."
    )},
    {"type": "body", "text": (
        "\"We cannot take that compound,\" Ifeanyi said finally, "
        "stating the plain fact none of them had wanted to be the first "
        "to say. \"Not four of us. Not without help we do not have and "
        "cannot reach in any useful time.\""
    )},
    {"type": "body", "text": (
        "\"No,\" Osadebe agreed, quiet, turning his own sketched map "
        "over in the dark though there was no longer enough light left "
        "to actually read it by. \"We cannot take it. We can watch it. "
        "We can learn it, the way we have learned every hard piece of "
        "ground between here and Idoro, patiently, one careful day at a "
        "time, until we know it well enough that whoever eventually "
        "comes to take it will not be walking in blind the way we very "
        "nearly did tonight.\""
    )},
    {"type": "body", "text": (
        "\"And if help never comes,\" Okonjo asked, the question "
        "landing heavier in the dark than it might have in daylight."
    )},
    {"type": "body", "text": (
        "\"Then we will already know that wall better than anyone who "
        "ever built it,\" Emenike said, before Osadebe could answer for "
        "him, his voice steadier than it had any right to be after what "
        "they had just seen. \"I have spent two seasons being told to "
        "wait for someone else to decide my sister's fate for me. I did "
        "not walk this far to start waiting again now that I can "
        "finally see the wall she is behind. Watch it. Learn it. I will "
        "do both for as many days as it takes. But I would rather die "
        "learning that wall than go home having never truly looked at "
        "it.\""
    )},
    {"type": "body", "text": (
        "Osadebe let the words sit in the dark for a long moment before "
        "he answered them, weighing a captain's duty to caution against "
        "a debt he privately felt he owed this particular soldier after "
        "the ravine. \"No one is dying learning a wall,\" he said "
        "finally, firm but not unkind. \"We watch. We learn. We do not "
        "cross that wall alone, whatever it costs any of us to wait. "
        "That is not caution for its own sake, Emenike. That is the "
        "only plan that actually gets your sister out alive instead of "
        "getting the rest of us killed beside her.\""
    )},
    {"type": "body", "text": (
        "Osadebe did not answer that one directly, and none of the "
        "other three pressed him to. Privately, turning the day's whole "
        "impossible sight over in his own mind long after the others "
        "had finally gone quiet, he found himself doing arithmetic he "
        "had not let himself do since the ravine, counting exactly how "
        "many days a rider would need to reach Udo from this exact "
        "stretch of forgotten ground, and exactly how many more days "
        "any help the crown chose to send would then need to find its "
        "way back out here again, over ground this hard, this far from "
        "any road a crown messenger could actually trust. The sum, "
        "however patiently he turned it, never once came out small."
    )},
    {"type": "body", "text": (
        "They lay down at last in the cold and the dark within sight "
        "of a wall none of them had prepared for, four men who had "
        "walked further from everything they knew than any of them had "
        "ever walked before, watching a fortress that wore a market's "
        "face and gave away nothing at all, that first long night, "
        "about what it actually kept behind it."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
