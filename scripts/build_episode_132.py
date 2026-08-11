#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 132: "What Ten Years Finally Cost"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): At the wall's own gap,
Mfoniso stays behind to buy the others their crossing, and finds herself
facing not just the Warden's guards but the Warden herself, the woman
who trained her in part across ten years of service. The confrontation
costs both women more than either expected, and leaves Mfoniso badly
outnumbered as the episode closes.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 132
EPISODE_TITLE = "What Ten Years Finally Cost"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Thirty Two"},
    {"type": "title_ep_name", "text": "What Ten Years Finally Cost"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE GAP
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "\"I am not crossing with you,\" Mfoniso said, already turning "
        "back toward the torchlight rather than the wall's own waiting "
        "gap, her voice leaving no room for the argument she could see "
        "forming on every face still standing near her."
    )},
    {"type": "body", "text": (
        "\"You cannot hold that ground alone,\" Osadebe said, though "
        "even as he said it he understood, reading the particular set "
        "of her shoulders, that he was arguing with a decision already "
        "finished rather than one still open to persuasion."
    )},
    {"type": "body", "text": (
        "\"I do not intend to hold it,\" Mfoniso said. \"I intend to "
        "buy you the length of time it takes five tired people to "
        "cross unfamiliar ground in the dark, and then I intend to "
        "follow you through it myself. Go. Every second spent arguing "
        "with me is a second I am not spending earning you that "
        "time.\""
    )},
    {"type": "body", "text": (
        "Okonjo hesitated at the gap's own edge, his own blade still "
        "drawn, plainly weighing whether a wounded stranger's stand "
        "was truly worth leaving unaided. \"You do not owe us this,\" "
        "he said. \"None of us would think less of you for crossing "
        "with the rest of the party instead.\""
    )},
    {"type": "body", "text": (
        "\"I do not owe you anything,\" Mfoniso agreed. \"I owe it to "
        "myself, which is a different debt entirely, and the only kind "
        "I have any real interest in settling honestly tonight. Go, "
        "Okonjo. Watch that ankle on the far side. It will not forgive "
        "you a second bad landing tonight the way it forgave you the "
        "first one.\""
    )},
    {"type": "body", "text": (
        "Ijeoma caught her arm once, briefly, before Emenike could "
        "pull her onward. \"Thank you,\" she said, simple and entirely "
        "sincere, \"for choosing this, whatever it costs you.\" Mfoniso "
        "did not answer beyond a short nod, already turning fully back "
        "toward the gathering torchlight before the words could soften "
        "anything in her that tonight still needed to stay hard."
    )},
    {"type": "body", "text": (
        "Osadebe held her gaze one final moment, the practiced "
        "assessment of a man who had spent years learning exactly how "
        "much trust a stranger's face could bear, and found, somewhat "
        "to his own surprise, that he trusted this one completely. "
        "\"We will not forget this,\" he said, his voice carrying the "
        "same flat certainty he used only for orders he fully intended "
        "to keep. \"Whatever happens on the other side of that gap, we "
        "will not forget it.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE STAND
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden's own guards reached the gap first, four of them "
        "moving with the disciplined confidence of men who had trained "
        "under officers this House trusted completely, and Mfoniso met "
        "them in the narrow ground the wall's own broken stone offered "
        "her, the same economical, unhurried fighting that had carried "
        "her through every clash this endless night had already asked "
        "of her."
    )},
    {"type": "body", "text": (
        "Two went down wounded rather than dead, a discipline she held "
        "onto even now, unwilling to let tonight's necessity turn into "
        "something she would not be able to live with afterward. The "
        "other two fell back rather than press an exchange that was "
        "clearly costing them more than it was costing her, buying "
        "just enough space for Mfoniso to draw a single full breath "
        "before the Warden herself finally stepped into the torchlight."
    )},
    {"type": "body", "text": (
        "Mfoniso remembered, watching the Warden step fully into the "
        "torchlight, a much younger version of herself standing in a "
        "training yard being corrected, patiently and precisely, on "
        "the exact angle of a guard she had held wrong for a full "
        "season without anyone else noticing the flaw. The Warden had "
        "noticed within a single afternoon and spent three more "
        "correcting it, unhurried, exacting, the same careful "
        "attention she gave to a ledger line she actually valued. "
        "Mfoniso had called that attention devotion for ten years "
        "without once questioning what it actually was devotion to."
    )},
    {"type": "body", "text": (
        "\"Ten years,\" the Warden said, quiet, her own blade drawn now "
        "for the first time either of them could remember her drawing "
        "it against Mfoniso directly. \"I taught you the stance you are "
        "holding right now. I taught you to read an opponent's weight "
        "before her blade ever moves. I find I did not teach you "
        "nearly well enough, apparently, to make you loyal.\""
    )},
    {"type": "body", "text": (
        "\"You taught me to think clearly under pressure,\" Mfoniso "
        "said. \"I am doing exactly that tonight. You taught me "
        "loyalty was owed to whoever paid for it. I have simply "
        "learned, at real cost, that the debt runs the other "
        "direction too, and that this House stopped paying its own "
        "share of it long before I ever stopped paying mine.\""
    )},
    {"type": "body", "text": (
        "They met in the narrow ground between one breath and the "
        "next, ten years of shared training turned suddenly, "
        "impossibly, against itself, each woman reading the other's "
        "every feint a half second before it fully committed, because "
        "each woman had, after all, taught the other exactly how."
    )},

    {"type": "body", "text": (
        "It was the closest fight of Mfoniso's entire career, and she "
        "understood, trading blow for blow with a teacher who had "
        "never once let her win anything she had not properly earned, "
        "that she was not going to win this one cleanly either."
    )},
    {"type": "body", "text": (
        "The Warden pressed a combination Mfoniso herself had spent "
        "three whole seasons drilling into her own hands as a much "
        "younger hunter, the same patient sequence built to open a "
        "careless opponent's guard by degrees rather than force, and "
        "Mfoniso countered it only because she had spent those same "
        "three seasons quietly imagining, without ever once expecting "
        "to need the answer, exactly how she would defend against it "
        "herself."
    )},
    {"type": "body", "text": (
        "\"You practiced against me,\" the Warden said, something "
        "flickering across her own guarded face that was not quite "
        "surprise and not quite pride, \"even then.\""
    )},
    {"type": "body", "text": (
        "\"I practiced against everyone who ever taught me anything "
        "worth learning,\" Mfoniso said, pressing the answer into her "
        "own next strike. \"You taught me that too, whether you meant "
        "to or not. Trust nothing completely, not even the hand that "
        "feeds you the lesson.\""
    )},
    {"type": "body", "text": (
        "The Warden shifted her weight and tried a third combination, "
        "one Mfoniso had never drilled against because the Warden had "
        "never taught it to her directly, learned instead, Mfoniso "
        "understood in the same half second it took to react, from "
        "whichever hunter had filled her own old place in the training "
        "yard since her departure. The gap it opened was real, and "
        "small, and closed again before the Warden could press it "
        "fully, but it told Mfoniso something she had not let herself "
        "consider until that exact instant, that this House had "
        "already begun preparing for a world in which she no longer "
        "served it at all."
    )},

    {"type": "body", "text": (
        "The Warden's blade found her side in the same instant "
        "Mfoniso's own found the Warden's forearm, both wounds shallow "
        "enough to keep either woman standing, deep enough that both "
        "of them staggered back a full step to assess exactly how "
        "badly the exchange had actually cost them."
    )},
    {"type": "body", "text": (
        "\"The guest was never truly the question that mattered most "
        "here, was it,\" the Warden said, circling once, reading the "
        "distance between them with the same careful attention she "
        "gave to everything worth reading properly. \"You could have "
        "recommended her death cleanly and kept everything else. I "
        "think you know that as well as I do.\""
    )},
    {"type": "body", "text": (
        "\"I could have,\" Mfoniso agreed. \"I chose not to, and I have "
        "stopped apologizing to myself for the choice somewhere in the "
        "last few hours. That is the part of tonight I suspect will "
        "cost this House far more than one guest's life ever could "
        "have, whatever comes of the rest of it.\""
    )},
    {"type": "body", "text": (
        "\"You are better than I remembered,\" the Warden said, "
        "breathing hard, something almost like genuine respect "
        "threading through the anger in her voice. \"I am almost sorry "
        "it has come to this.\""
    )},
    {"type": "body", "text": (
        "\"Almost,\" Mfoniso agreed, matching her own labored breathing "
        "against the Warden's, \"is not the same word as sorry.\""
    )},
    {"type": "body", "text": (
        "Neither of them moved to press the exchange further in that "
        "particular breath, both women reading, with the same trained "
        "eye each had spent years sharpening in the other, exactly how "
        "little either of them had left in reserve for a second full "
        "exchange fought at that same costly speed."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "More torches were already gathering at the courtyard's far "
        "edge, a full second wave the Warden's own captain had "
        "apparently summoned the moment the first four guards fell "
        "back, and Mfoniso understood, watching the numbers stack "
        "steadily against her, that whatever ground she had bought the "
        "others was very nearly the whole of what she had left to "
        "spend."
    )},
    {"type": "body", "text": (
        "She broke from the Warden's own guard with a sharp, "
        "deliberate strike that cost her the last clean reserve of "
        "strength she had been holding back, buying herself exactly "
        "enough distance to turn for the wall's own gap rather than "
        "continue an exchange the arriving numbers had already decided "
        "the outcome of."
    )},
    {"type": "body", "text": (
        "\"This is not finished,\" the Warden called after her, not "
        "moving to follow immediately, the flat certainty of a keeper "
        "who understood exactly how this particular kind of debt "
        "eventually got collected. \"You know this House well enough "
        "to know that.\""
    )},
    {"type": "body", "text": (
        "Mfoniso did not answer, already running for a gap she was no "
        "longer entirely certain her own wounded body would clear "
        "before the second wave of torches finally closed the "
        "distance behind her."
    )},
    {"type": "body", "text": (
        "Her side burned with every stride, the wound shallow enough "
        "to keep her upright and deep enough to slow her past any pace "
        "she would have trusted an hour ago, and she counted, the same "
        "grim discipline she had trained a dozen younger hunters to "
        "rely on, exactly how many strides still separated her from "
        "ground the torches could no longer reach."
    )},
    {"type": "body", "text": (
        "Somewhere behind her, muffled by distance and her own ragged "
        "breathing, she heard the Warden's voice still directing the "
        "search, calm even now, the same unhurried authority that had "
        "once made Mfoniso feel chosen rather than merely useful. She "
        "did not let herself slow down to listen for more of it. "
        "Whatever the Warden still meant to her, tonight had already "
        "answered the only question that mattered, and running from "
        "the answer would not undo the choice that had produced it."
    )},
    {"type": "body", "text": (
        "The second wave reached the gap's own edge just as she "
        "cleared it, close enough behind her that she heard, rather "
        "than saw, the first of them scrambling over the same broken "
        "stone, and she understood, forcing her own burning legs "
        "faster through unfamiliar dark ground, that the distance she "
        "had bought herself was measured now in seconds rather than "
        "any comfortable stretch of minutes."
    )},
    {"type": "body", "text": (
        "She did not know, running blind into ground she had never "
        "once scouted for her own escape, whether the others were "
        "still close enough ahead of her to reach, or whether tonight's "
        "single closest fight of her whole career had bought them "
        "distance at a cost she alone would end up paying for it, or "
        "whether the debt, before this endless night finally ended, "
        "would prove wide enough, in the end, for all five of them "
        "still living to share its true, full weight equally between "
        "them all before this whole entire long night was finally, "
        "truly over."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
