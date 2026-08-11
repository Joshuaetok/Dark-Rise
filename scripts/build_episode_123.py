#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 123: "Whatever It Costs Us Now"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): With stealth gone after the
patrol clash, the search party debates retreat, hiding, or pushing
forward. Emenike's case, that the compound will move faster because of
today's clash rather than slower, carries the room.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 123
EPISODE_TITLE = "Whatever It Costs Us Now"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Three"},
    {"type": "title_ep_name", "text": "Whatever It Costs Us Now"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "They made proper camp for the first time in two days, a "
        "narrow hollow well back from any trail Osadebe could name with "
        "any confidence, and spent the first hour of real rest simply "
        "tending what the clash had cost them, Ifeanyi's forearm "
        "rewrapped, Osadebe's shallow cut cleaned properly at last, "
        "Okonjo's ankle bound tighter than it had been bound since the "
        "ravine."
    )},
    {"type": "body", "text": (
        "No one spoke much during that first hour, the particular "
        "quiet of men who had each spent the clash certain, at least "
        "once, that the fight might be the last thing any of them ever "
        "did. Ifeanyi worked his own bandage tighter with hands that "
        "had not fully stopped their small tremor, and Okonjo sat "
        "close to the fire with his bad leg stretched out before him, "
        "staring at nothing in particular with the flat, distant look "
        "of a man replaying a single half second over and over, "
        "searching it for the exact moment his own ankle had nearly "
        "cost him everything."
    )},
    {"type": "body", "text": (
        "It was Osadebe who finally said aloud the question all four "
        "of them had been carrying since the ravine's steep slope had "
        "finally leveled out beneath their feet. \"We have three roads "
        "open to us now, and no honest way to call any of them safe. "
        "We retreat, all the way back toward ground the crown can "
        "actually protect us on. We go still, here or somewhere "
        "quieter, and wait for whatever help Chidebe managed to send "
        "us. Or we push, faster and closer than we have dared push yet, "
        "and accept whatever that costs us for the sake of not losing "
        "the only advantage today's clash may have actually bought "
        "us.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"Retreat keeps us alive,\" Ifeanyi said first, practical as "
        "ever, laying the argument out with the same flat honesty he "
        "gave to reading any difficult ground. \"It also means we walk "
        "away from everything we have learned, with no guarantee we "
        "would ever find our way back to this exact bearing a second "
        "time, against a House that will only be better prepared for "
        "us the longer we give it to prepare.\""
    )},
    {"type": "body", "text": (
        "\"Waiting costs us nothing today,\" Okonjo offered, though even "
        "he did not sound fully persuaded by his own suggestion. "
        "\"Chidebe's help is out there somewhere on this same bearing. "
        "If we sit still and let them find us, we go in with more than "
        "four blades instead of exactly four.\""
    )},
    {"type": "body", "text": (
        "\"We do not know how many days behind us that help still is,\" "
        "Osadebe said, honest rather than dismissive. \"It could be "
        "one day. It could be six. We have no way to shorten that "
        "distance by wishing it shorter, and every day we spend "
        "waiting is a day that House spends deciding what today's "
        "clash actually means for it.\""
    )},

    {"type": "body", "text": (
        "\"I have never once, in my whole life before this search, "
        "wished harder for a decision to be made by someone other than "
        "myself,\" Okonjo admitted, quiet, still watching the fire "
        "rather than any of the other three. \"I trust Osadebe's "
        "judgment more than I trust my own tonight. I am simply "
        "grateful the choice does not rest with a man whose leg nearly "
        "failed him twice in the same season.\""
    )},
    {"type": "body", "text": (
        "\"Your leg is not the reason your judgment matters less "
        "tonight,\" Osadebe said, firm but not unkind. \"Everyone at "
        "this fire has earned a voice in what happens next. I would "
        "rather hear a doubtful voice honestly than a confident one "
        "dressed up to sound braver than it actually feels.\""
    )},
    {"type": "body", "text": (
        "Emenike had said nothing through the whole exchange, sitting "
        "apart with his own bound blade across his knees, and it was "
        "the silence itself, longer than his usual restraint, that "
        "finally drew the other three's attention toward him."
    )},

    {"type": "body", "text": (
        "\"You are all reasoning as though that House has the luxury "
        "of patience,\" he said finally, quiet but entirely certain. "
        "\"It does not. Six of their men went into that fight and not "
        "all of them walked back out of it. A House that loses men on "
        "its own ground does not sit still afterward weighing its "
        "options the careful way we are weighing ours. It moves. It "
        "tightens. It decides, fast, what to do about every liability "
        "sitting inside its own walls that it can no longer afford to "
        "leave undecided.\""
    )},
    {"type": "body", "text": (
        "\"You are describing a guess,\" Ifeanyi said, not unkindly, "
        "\"dressed carefully enough to sound like certainty.\""
    )},
    {"type": "body", "text": (
        "\"It is a guess,\" Emenike agreed, without flinching from the "
        "word. \"It is also the only guess among the three roads Osadebe "
        "laid out for us that does not require me to believe this House "
        "will simply wait, patiently, for us to be ready. I do not "
        "believe that. I have watched this exact House take two whole "
        "seasons to decide my sister was worth less trouble kept alive "
        "than killed outright, and I do not believe today's clash has "
        "made that decision easier for whoever is making it. If "
        "anything, I believe it has made the decision urgent in a way "
        "it was not urgent yesterday.\""
    )},
    {"type": "body", "text": (
        "\"And if you are wrong,\" Osadebe asked, quiet, giving the "
        "question the same weight he had given every hard question "
        "since Idoro, \"four men push forward into a wall we already "
        "know we cannot take, for the sake of urgency that turns out to "
        "have belonged only to your own fear rather than to anything "
        "real.\""
    )},
    {"type": "body", "text": (
        "\"Then we push forward carefully rather than push forward "
        "blind,\" Emenike said. \"I am not asking any of you to storm "
        "that wall tonight. I am asking that we stop treating distance "
        "as safety. We move closer. We watch harder than we have ever "
        "watched. We find whatever opening this House's own fear may "
        "hand us in the next few days, because I do not believe we have "
        "the luxury of waiting for a safer one to arrive on its own "
        "schedule.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "Osadebe let the silence stretch a long moment before he "
        "answered, weighing a captain's duty against the same debt he "
        "had privately owed Emenike since the ravine, the debt of a man "
        "whose judgment had already proven itself once when the whole "
        "party's safety depended on it."
    )},
    {"type": "body", "text": (
        "\"We push,\" he said finally, \"carefully, exactly as you have "
        "asked, and we leave a clear trail of stones behind us the way "
        "I have left them every night since Idoro, in case Adaeku's own "
        "party is closer behind us than any of us currently have reason "
        "to hope. We do not storm anything. We close the distance, we "
        "watch harder, and we find the opening Emenike believes this "
        "House's own fear is about to hand us.\""
    )},
    {"type": "body", "text": (
        "\"There is one more thing,\" Osadebe added, before any of them "
        "could rise from the fire. \"If we push forward and this goes "
        "badly, I will not have any of you dying for a guess, however "
        "well reasoned. The moment any one of us judges the risk has "
        "outgrown what a guess can justify, we say so aloud, plainly, "
        "and the whole party listens. I would rather be called overly "
        "cautious by three living men than proven right by three dead "
        "ones.\""
    )},
    {"type": "body", "text": (
        "Ifeanyi did not argue further, though the particular set of "
        "his shoulders made clear he was following orders rather than "
        "fully persuaded by them. Okonjo, still favoring the ankle that "
        "had nearly cost him his life a second time, said nothing at "
        "all, trusting Osadebe's judgment over his own uncertain one."
    )},
    {"type": "body", "text": (
        "Emenike alone looked, for the first time since the ambush that "
        "had first shown him his sister's own name on a stranger's "
        "tongue, something close to steady. \"Thank you,\" he said, "
        "quiet, meaning it for all three of them at once rather than "
        "for Osadebe alone."
    )},
    {"type": "body", "text": (
        "\"Do not thank me yet,\" Osadebe said, already turning to the "
        "night's remaining watch schedule, his voice carrying the flat, "
        "grim honesty he had carried every hard day since the ridge. "
        "\"Thank me when we actually find the opening you believe is "
        "waiting for us. Until then, all any of us have truly agreed to "
        "tonight is to walk toward danger faster than good sense would "
        "otherwise recommend, and call it a plan because the alternative "
        "felt worse.\""
    )},
    {"type": "body", "text": (
        "The fire burned lower as the night wore on, the four of them "
        "taking their watches in turn while the others slept, or tried "
        "to, each man alone for a while with whatever the day's fight "
        "had left inside him. Emenike took the last watch before dawn "
        "by his own choosing, sitting with his back against a cool "
        "stone and his sister's name turning over in his mind the way "
        "it had turned over every night since a stranger first spoke it "
        "aloud on the trail."
    )},
    {"type": "body", "text": (
        "He did not know, sitting alone in the last dark hour before "
        "the party rose to break camp, whether tonight's decision would "
        "carry them to her or bury all four of them somewhere this "
        "forgotten ground would never trouble itself to explain to "
        "anyone who came looking. He knew only that retreat had never "
        "once, from the very first morning he asked the household when "
        "it would finally search for her, felt like a road he could "
        "walk without losing something in himself he was not certain he "
        "would ever get back."
    )},
    {"type": "body", "text": (
        "When the sky finally began to gray toward morning, he woke "
        "the others quietly, one hand on each man's shoulder in turn, "
        "and said nothing more than that it was time to move, trusting "
        "the night's decision to carry its own weight without needing "
        "to be spoken again."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
