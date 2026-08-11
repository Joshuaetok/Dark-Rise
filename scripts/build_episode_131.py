#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 131: "When the Keeper Finally Moved"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The Warden absorbs the full
scope of the night's betrayals, Mfoniso's open break, the Factor's
sacrifice, Ijeoma's freedom, and decides she no longer trusts anyone
else's judgment enough to delegate the pursuit. The group runs for the
northern wall breach with guards closing from every direction, the
Warden herself now leading the chase for the first time in her career.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 131
EPISODE_TITLE = "When the Keeper Finally Moved"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Thirty One"},
    {"type": "title_ep_name", "text": "When the Keeper Finally Moved"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE WARDEN
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The guard captain delivered his report standing at rigid, "
        "unhappy attention, the shape of a man who understood he was "
        "about to make his own night considerably worse simply by "
        "telling the truth of it in full. Mfoniso had broken openly "
        "with the House and fought Ebiere in the second corridor. A "
        "senior administrator had issued a false order that had cost "
        "the compound its best chance of holding the northern wall. "
        "Armed strangers, at least three of them, had breached that "
        "same wall and were, as far as anyone could currently confirm, "
        "already moving toward it again with the guest in their own "
        "company."
    )},
    {"type": "body", "text": (
        "The Warden listened to the whole of it without once "
        "interrupting, the particular stillness of a keeper doing the "
        "hardest arithmetic of her career in real time, three separate "
        "betrayals arriving inside a single hour from three separate "
        "directions she had never once thought to watch closely enough "
        "together."
    )},
    {"type": "body", "text": (
        "\"Assemble every able guard at the northern wall,\" she said "
        "finally, already moving toward her own study's weapon rack for "
        "the first time in longer than she cared to remember needing "
        "it. \"I will lead them myself.\""
    )},
    {"type": "body", "text": (
        "The captain hesitated, plainly unhappy with the order despite "
        "understanding better than to argue it. \"That is not the "
        "Warden's place, tonight of all nights,\" he said carefully. "
        "\"Let me lead the pursuit. You are needed here, directing the "
        "whole of it.\""
    )},
    {"type": "body", "text": (
        "\"I trusted my most reliable hunter for ten years and she "
        "broke faith with this House in a single week,\" the Warden "
        "said, flat. \"I trusted a man I have worked beside for twenty "
        "years and he lied to my own captain's face without a moment's "
        "hesitation. I no longer trust anyone in this compound's "
        "judgment tonight except my own. That is not pride talking. It "
        "is simple, exhausted arithmetic.\""
    )},

    {"type": "body", "text": (
        "She armed herself with the same unhurried, exact care she "
        "brought to everything, a blade she had not carried into real "
        "combat in longer than the captain standing nervously beside "
        "her had served this House at all, and found, buckling it into "
        "place, that her own hands had not forgotten the weight of it "
        "the way she had half feared they might."
    )},
    {"type": "body", "text": (
        "The captain fell into step beside her rather than continue "
        "the argument he already understood he had lost. \"The "
        "strangers,\" he said, careful. \"Do we know yet who sent "
        "them.\""
    )},
    {"type": "body", "text": (
        "\"No,\" the Warden said. \"I know only that they fight with "
        "crown discipline rather than any hired mercenary's looser "
        "training, and that a House already under a crown investigation "
        "into its own court sponsor should think very carefully about "
        "what it means if crown trained men are standing tonight inside "
        "its own walls. I intend to think about that carefully once "
        "this pursuit is finished. Tonight, thinking about it changes "
        "nothing except how quickly I move.\""
    )},
    {"type": "body", "text": (
        "She paused once more before the study door, turning back "
        "toward the captain with something almost like the ghost of "
        "an explanation she did not fully owe him. \"I built this "
        "House's every careful advantage on trusting my own judgment "
        "over anyone else's comfortable assumptions,\" she said. \"I "
        "will not abandon that habit on the single night it has ever "
        "actually mattered enough to test it properly.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE GROUP
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "They ran the compound's own darkened corridors with Mfoniso "
        "leading, her knowledge of the ground the only real advantage "
        "five fugitives carried against a House that knew every "
        "shadow of it far better than they ever could."
    )},
    {"type": "body", "text": (
        "\"You are the search party,\" Ijeoma said, breathless, "
        "piecing the whole impossible shape of the night together as "
        "she ran, looking between Osadebe and Okonjo with an "
        "expression that had not fully settled yet between disbelief "
        "and something warmer. \"Someone actually sent a search "
        "party.\""
    )},
    {"type": "body", "text": (
        "\"Your household never once stopped believing you were worth "
        "finding,\" Osadebe said, not slowing his own pace to say it. "
        "\"I am sorry it took this long. I am sorrier still that we "
        "arrive with half this compound's guards now hunting all five "
        "of us together.\""
    )},
    {"type": "body", "text": (
        "Okonjo, running a half step behind, offered what he could of "
        "the missing piece Ijeoma had not yet been given time to ask "
        "for. \"There is a fourth of us,\" he said, breathless. "
        "\"Ifeanyi, wounded, waiting at a camp none of us has any "
        "honest way to reach before whatever is happening in this "
        "compound finishes happening around us. I would rather you "
        "know his name than think this party smaller than it actually "
        "is.\""
    )},
    {"type": "body", "text": (
        "Ijeoma filed the name away the same patient way she had "
        "filed every fact this compound had ever handed her, unwilling "
        "to let gratitude crowd out the counting that had kept her "
        "alive two whole seasons, even now, even mid flight, with her "
        "own brother's hand finally closed around her arm again."
    )},
    {"type": "body", "text": (
        "They reached the courtyard's edge just as the first real "
        "resistance regrouped ahead of them, six guards forming a "
        "hasty line across the shortest path to the northern wall, "
        "and it was Mfoniso, moving with the same economy she had "
        "shown in the earlier corridor, who broke the line's center "
        "before it had finished settling."
    )},
    {"type": "body", "text": (
        "\"Go,\" she said, holding the gap open with her own blade for "
        "the handful of seconds the others needed to clear it. \"I will "
        "close behind you. Do not wait for me to finish counting "
        "them.\""
    )},
    {"type": "body", "text": (
        "Emenike hesitated at the gap's edge despite himself, some old, "
        "unresolved instinct refusing to let him simply run past a "
        "woman fighting alone against six, and it was Ijeoma's own "
        "hand, closing hard around his wrist, that pulled him through "
        "before the hesitation could cost either of them anything."
    )},
    {"type": "body", "text": (
        "\"She chose this,\" Ijeoma said, breathless, reading the shape "
        "of her brother's guilt without needing it explained to her. "
        "\"Whatever she was to this House before tonight, she is "
        "choosing this now, with her eyes open. Let her have that "
        "choice. Do not spend it by getting yourself killed feeling "
        "guilty over it.\""
    )},
    {"type": "body", "text": (
        "Mfoniso rejoined them thirty seconds later, breathing hard "
        "and bleeding from a shallow cut along one forearm, having left "
        "the line behind her broken rather than beaten, four of the six "
        "guards still on their feet but no longer in any condition to "
        "give immediate chase."
    )},

    {"type": "body", "text": (
        "The wall itself came into sight a hundred desperate paces "
        "later, its own gap still standing exactly as unwatched as "
        "the earlier chaos had left it, and for one brief, aching "
        "moment the whole party believed the worst of the night might "
        "actually be behind them."
    )},

    {"type": "body", "text": (
        "It was Okonjo, glancing back once out of pure habit, who saw "
        "the torches gathering on the courtyard's far side, a "
        "disciplined, converging line of them moving with none of the "
        "earlier chaos's confusion, led at its own center by a single "
        "figure whose bearing Mfoniso recognized before anyone else in "
        "the party had time to ask who she was."
    )},
    {"type": "body", "text": (
        "\"The Warden,\" Mfoniso said, and something in her own voice, "
        "steady through every fight this night had already asked of "
        "her, went taut in a way none of the others had heard from her "
        "yet. \"She does not lead pursuits herself. She has never once, "
        "in ten years, needed to. If she is walking that line herself "
        "tonight, she has already decided none of us are meant to "
        "leave this ground alive to tell anyone what happened here.\""
    )},
    {"type": "body", "text": (
        "\"Then we do not give her the chance to finish deciding it,\" "
        "Osadebe said, already pushing the party the last hard "
        "distance toward the wall's own waiting gap, Emenike's hand "
        "never once leaving his sister's arm the whole desperate way "
        "there."
    )},
    {"type": "body", "text": (
        "Mfoniso fell into the party's rear without being asked, "
        "positioning herself between the group and the gathering "
        "torchlight with the same unhurried readiness she had carried "
        "into every fight this endless night had demanded of her, "
        "though something in the careful way she held her own blade "
        "now suggested she understood exactly what kind of fight was "
        "still coming."
    )},
    {"type": "body", "text": (
        "\"How many,\" Osadebe asked, not slowing, trusting her own "
        "practiced eye over his own less certain one."
    )},
    {"type": "body", "text": (
        "\"Enough that counting them precisely will not change what "
        "any of us do next,\" Mfoniso said. \"Get the guest through "
        "that gap. Get her brother through it beside her. Whatever "
        "happens behind you, do not turn back to see it happen.\""
    )},
    {"type": "body", "text": (
        "Ijeoma heard the shape of the offer buried inside the "
        "instruction, understood, with the same clear headed counting "
        "that had carried her through two seasons of patient captivity, "
        "exactly what Mfoniso was quietly preparing to spend on five "
        "strangers she had known for less than an hour. She did not "
        "argue it. She had learned, at real cost, that arguing a "
        "chosen sacrifice rarely honored the person choosing it."
    )},
    {"type": "body", "text": (
        "The wall's gap opened ahead of them at last, the same "
        "unwatched stretch of stone the party had crossed hours "
        "earlier in a different, quieter kind of danger, and Osadebe "
        "went through it first, checking the ground beyond with the "
        "same careful captain's instinct that had kept all four of "
        "his men alive across every hard mile since Idoro."
    )},
    {"type": "body", "text": (
        "Behind them, closer now than any of them wanted to measure "
        "honestly, the Warden's own gathered torchlight kept coming, "
        "steady and unhurried in a way that frightened Mfoniso far "
        "more, if she was being entirely honest with herself, than any "
        "purely panicked, disorganized chase ever truly could have."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
