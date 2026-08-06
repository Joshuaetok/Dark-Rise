#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 102: "The Shape of Waiting"
Uses the shared scripts/dr_build.py module (see that file for the OOXML
machinery). This script only defines episode content.

Written 2026-08-06 (scheduled release TBD): opens the Episodes 102-140
arc. Three quiet, watching threads advance in parallel: the search
party, a day into the two the presence promised, finds an old path
gone suddenly unwalked; Ijeoma, for the first time, studies the guard
rotation with intent to act rather than only to endure; Mfoniso, still
rebuilding her read of a transformed Idoro from her western ridge, is
unsettled by her own teacher's unexplained silence. The episode closes
cold: the Warden's ciphered question is one day from reaching Mfoniso's
hand, and she has no idea it is coming.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 102
EPISODE_TITLE = "The Shape of Waiting"

EPISODE_CONTENT = [
    # ── Title page ──
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Two"},
    {"type": "title_ep_name", "text": "The Shape of Waiting"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE SEARCH PARTY
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Five mornings past the fallen stone, the bush stopped sounding "
        "like bush. Osadebe noticed it first as an absence. The birds "
        "that should have argued over first light simply did not, and "
        "by midmorning even Okonjo, who whistled without meaning to "
        "whenever he walked, had gone quiet without being told to."
    )},
    {"type": "body", "text": (
        "They followed the bearing the presence had given through "
        "Chibundu's dream, west and then slightly south, a line so "
        "exact it felt less like a direction and more like a debt "
        "finally being called in. The ground under their feet had long "
        "since stopped resembling any trail a map would bother to draw. "
        "Even the trees here grew with a stillness that had nothing to "
        "do with the absence of wind."
    )},
    {"type": "body", "text": (
        "Ifeanyi crouched at a bend where nothing should have made him "
        "crouch. He ran two fingers along a low ridge of packed earth "
        "that any of the others would have walked straight across "
        "without seeing it. \"This was a path once,\" he said, low, the "
        "voice of a hunter reading a language he only half remembered. "
        "\"Feet made this. Not animals. Feet, over and over, for a long "
        "time. And then all at once, it stopped being walked, the way a "
        "market empties the hour everyone hears the same bad news.\""
    )},
    {"type": "body", "text": (
        "Osadebe crouched beside him and found nothing his own eyes "
        "could confirm, only grass grown thick and even where a true "
        "path usually wore itself thin. \"How long ago,\" he asked, his "
        "voice carrying the calm of a man who had learned not to want "
        "an answer too badly before he heard it. \"Longer than I have a "
        "number for,\" Ifeanyi said, flat, unwilling to guess at what "
        "he could not measure. \"This ground is not empty, Captain. It "
        "is only old.\""
    )},
    {"type": "body", "text": (
        "Emenike walked a few steps behind them with one hand pressed "
        "lightly against the healing wound at his side, more habit now "
        "than pain. He had stopped asking how much further an hour ago, "
        "because the answer never changed the walking, only the "
        "waiting inside it. Somewhere past this bent, quiet ground was "
        "a bearing that might end at his sister, or might end at "
        "nothing that had anything to do with her at all, and he had "
        "trained himself these five days not to let his face choose "
        "between those two outcomes in front of the others."
    )},
    {"type": "body", "text": (
        "\"Two days,\" Osadebe said anyway, his voice pitched to sound "
        "more certain than he felt, answering the question Emenike had "
        "not asked aloud. \"That is what the boy's dream gave us. One "
        "day gone already. If the ground keeps its word, we sleep "
        "inside whatever this bearing is pointing at by tomorrow "
        "night.\" Okonjo, walking drag behind them with the water "
        "skins, said only that he hoped whatever it was had shade, his "
        "voice dry with the particular humor of a soldier too tired to "
        "be afraid yet."
    )},
    {"type": "body", "text": (
        "They pressed on. An hour past the ridge, the old path Ifeanyi "
        "had found split without warning into two, one line bending "
        "north around a stand of trees too evenly spaced to be an "
        "accident, the other continuing straight along the bearing the "
        "presence had given. Ifeanyi looked a long moment at the "
        "northern branch and said nothing at all, which unsettled "
        "Osadebe more than anything he might have said."
    )},
    {"type": "body", "text": (
        "Osadebe marked both branches on his map anyway, the straight "
        "one in a firm hand and the other in a lighter one, a question "
        "he was choosing to carry rather than answer today. Whatever "
        "waited up that northern line could keep. The bearing they had "
        "been given only pointed one way, and for now that was the "
        "only debt any of them had the right to collect."
    )},
    {"type": "body", "text": (
        "They made camp early that night, not from tiredness but from "
        "the plain sense that walking blind into the last hour of "
        "light was a poor way to meet whatever tomorrow's ground held. "
        "Okonjo rationed the dried fish without being asked, a small "
        "kindness none of them commented on, and Osadebe sat a long "
        "while with his map open on his knee, tracing the straight "
        "line south and west with one finger as if repetition might "
        "make the last two days shorter than they were."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "In the walled courtyard downriver, Ijeoma had spent two "
        "seasons learning to count without looking like she was "
        "counting. Guards. Meals. The exact number of steps between the "
        "well and the kitchen door. It had become a kind of prayer, "
        "private and useless, the only power a locked person kept when "
        "every other kind had been taken from her."
    )},
    {"type": "body", "text": (
        "Her mother had taught her to count cloth the same patient way, "
        "years ago in a life that felt borrowed from someone else now. "
        "Thread count told you what a bolt of cloth was worth before "
        "you ever touched it. Ijeoma had simply never expected to spend "
        "two seasons applying that same patience to a wall instead of "
        "a market stall."
    )},
    {"type": "body", "text": (
        "Today she counted something new. Not the guards themselves, "
        "but the gap between them, the particular minute each morning "
        "when the man at the eastern gate left his post to relieve "
        "himself against the outer wall and did not return for the "
        "length of time it took her to recite, in her head, every cloth "
        "pattern her mother had ever taught her to name by touch alone."
    )},
    {"type": "body", "text": (
        "She had never watched for the gap before. Watching for it "
        "changed the shape of the whole courtyard, turned it from a "
        "place she endured into a place she was, for the first time in "
        "two seasons, actually reading."
    )},
    {"type": "body", "text": (
        "A servant girl passed close by with a basket of wet laundry, "
        "glancing at Ijeoma the way the House staff always did, careful "
        "and brief, the look of people who had been told not to speak "
        "to the guest but had never been told why. \"You are up early,\" "
        "the girl said, her voice pitched soft and neutral, testing "
        "whether a conversation was allowed today. \"I sleep badly,\" "
        "Ijeoma answered, just as evenly. \"The wall keeps its own "
        "hours, and mine follow it now.\" It was true enough to pass, "
        "and vague enough to mean nothing to anyone listening."
    )},
    {"type": "body", "text": (
        "The girl moved on without slowing. Ijeoma watched the eastern "
        "gate for one more count, confirming what she already "
        "suspected, that the gap was not an accident of one lazy "
        "morning but a habit, worn into the guard the way a path wears "
        "itself into ground that is walked the same way often enough."
    )},
    {"type": "body", "text": (
        "A habit was a door."
    )},
    {"type": "body", "text": (
        "She had not decided yet what she meant to do with a door. But "
        "she had found one, and for the first time since the last "
        "bracelet went untaken, that felt like more than waiting."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: MFONISO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Mfoniso had chosen her vantage with a hunter's patience, high "
        "enough on the western ridge to see three of Idoro's four "
        "approach roads without being seen from any of them. She had "
        "held the position four days now, rebuilding, patrol by "
        "patrol, the picture of a village that no longer matched "
        "anything she had studied before her wounds sent her home to "
        "heal."
    )},
    {"type": "body", "text": (
        "The garrison had not shrunk back down since the crown's "
        "survey left. If anything it had settled into its new size the "
        "way a scar settles into skin, permanent rather than "
        "temporary, and the patrols moved on a rotation she had not yet "
        "found the seam in. She respected the change even as it cost "
        "her. Whoever had rebuilt Idoro's defenses had done it like "
        "someone who expected to be tested again."
    )},
    {"type": "body", "text": (
        "Four days ago, before she had fully rebuilt her picture of "
        "the village, she had watched a small band leave Idoro by its "
        "eastern road at dawn, soldiers by their bearing, walking "
        "rather than riding, and had filed it without much weight as "
        "another rotation folded into the garrison's new routine. She "
        "had not troubled to count them again since. It did not occur "
        "to her, watching Idoro's much larger patrols now, that four "
        "men on foot might matter more than forty kept on schedule."
    )},
    {"type": "body", "text": (
        "What unsettled her more than the garrison was the silence on "
        "her own side of the line. Her teacher had not answered her in "
        "longer than she could remember going without word, not since "
        "before the confrontation that had sent her home wounded and "
        "shaken. She told herself it meant nothing. Teachers went "
        "quiet. Old hunters kept their own counsel, and hers had never "
        "been a woman who explained herself twice."
    )},
    {"type": "body", "text": (
        "But Mfoniso had spent her whole training learning to read "
        "absence the way other people read speech, and the absence on "
        "that particular line had a shape to it now that she did not "
        "like. It reminded her, uncomfortably, of the stillness Ifeanyi "
        "would have recognized without needing to be told what it "
        "meant. Somewhere beyond her own reach, something had shifted, "
        "and no one had told her what."
    )},
    {"type": "body", "text": (
        "She thought, not for the first time, of the stories her "
        "teacher used to tell about the ground their lineage had once "
        "taken, three centuries back, before either of them had a name "
        "for what they carried. Her teacher had always told it as a "
        "triumph. Lately, alone on a ridge with too much silence to "
        "fill, Mfoniso found herself wondering what the story sounded "
        "like from the other side of it, and disliked how easily the "
        "question came to her now."
    )},
    {"type": "body", "text": (
        "She put the thought away the way she put away every thought "
        "that did not serve the work in front of her, and returned to "
        "her count of Idoro's patrols. Discipline was the only thing "
        "her teacher had ever given her that she trusted without "
        "reservation now, and discipline said the silence was not her "
        "business until it became one."
    )},
    {"type": "body", "text": (
        "She did not yet know that a message addressed to her in the "
        "House's oldest cipher was already a single day's ride "
        "downriver, sealed and moving, carrying a question the Warden "
        "had written with a small brass weight still holding the "
        "ledger page open on her desk."
    )},
    {"type": "body", "text": (
        "Mfoniso watched Idoro's eastern road empty into evening and "
        "turned her attention back to counting patrols, unaware that "
        "somewhere behind her, a decision about a woman she had once "
        "glimpsed in a guarded courtyard was already traveling toward "
        "her hand."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
