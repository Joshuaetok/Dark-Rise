#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 121: "The Warning He Could Not Take Back"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The compound reacts to the
wounded courier's report by doubling every watch on the property. The
Factor, fearing the tightening will close whatever narrow window Ijeoma
still has, risks the most dangerous act of his quiet redemption yet: a
handful of words spoken directly to her, oblique enough to survive
scrutiny, real enough to matter.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 121
EPISODE_TITLE = "The Warning He Could Not Take Back"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty One"},
    {"type": "title_ep_name", "text": "The Warning He Could Not Take Back"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "The wounded courier reached the compound's rear gate a full "
        "hour before dusk, bleeding through a hastily wrapped forearm "
        "and short of breath from a run he had clearly not expected to "
        "make, and the story he carried spread through the household "
        "faster than any formal order could have spread it, ambushed on "
        "the supply trail, his partner taken, strangers waiting in "
        "ground no stranger should have known well enough to wait in."
    )},
    {"type": "body", "text": (
        "The guard captain doubled every watch on the property before "
        "full dark, a blunt, immediate response that needed no "
        "elaborate reasoning to justify itself, and by the following "
        "morning the whole compound moved differently, guards walking "
        "closer together, gates checked twice where once had always "
        "been enough, an atmosphere the Factor recognized instantly "
        "from thirty years of reading exactly this kind of fear inside "
        "exactly this kind of House."
    )},
    {"type": "body", "text": (
        "The Warden received the guard captain's report standing, "
        "unwilling to sit through news this raw, and asked only two "
        "questions before dismissing him to his own urgent work. How "
        "many strangers, and how well armed. The captain could answer "
        "neither with any certainty, and the Warden's face, by every "
        "account that reached the Factor secondhand within the hour, "
        "had gone the particular still, flat color of a keeper doing "
        "arithmetic she did not like the shape of."
    )},
    {"type": "body", "text": (
        "He spent that whole morning turning a private calculation over "
        "that frightened him more than the strangers on the trail ever "
        "could. A House that felt threatened from outside its walls did "
        "not, in his long experience, grow more patient with the "
        "uncertain assets it already kept inside them. It grew faster, "
        "harsher, quicker to close accounts it could no longer afford "
        "the luxury of leaving open. The Warden's own fourteen day "
        "deadline had felt, a week ago, like distant weather. Watching "
        "the compound's guards tighten around him now, it felt like "
        "weather that had already arrived."
    )},
    {"type": "body", "text": (
        "He had seen this exact pattern once before, years ago, in a "
        "sister House downriver that lost two warehouses to a rival "
        "trader's private grievance and answered the loss by quietly "
        "disposing of every liability its own frightened leadership "
        "could no longer justify feeding. He had called it sound "
        "business at the time, in the careless way a younger man calls "
        "anything sound business when the liability in question is "
        "still only a line in someone else's ledger. He no longer had "
        "that comfortable distance left to hide behind."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "He arranged his reason to visit the guest's small room the "
        "way he arranged every careful thing now, inside the shape of "
        "an ordinary duty no one would think twice about. A senior "
        "review of the household's security procedures, prompted "
        "naturally by the previous day's attack, would obviously "
        "include a personal check of exactly where and how the "
        "compound's one truly irreplaceable guest was being kept. He "
        "requested the housemistress's key with a steadiness that cost "
        "him more than it should have to hold."
    )},
    {"type": "body", "text": (
        "Ijeoma stood when he entered, the same careful blankness "
        "settling over her face that she wore for every stranger who "
        "had ever crossed her threshold, though something in her eyes "
        "sharpened slightly at the sight of a face she recognized from "
        "the dock rather than a guard's unfamiliar one."
    )},
    {"type": "body", "text": (
        "\"A security review,\" he said, for the benefit of the guard "
        "waiting just outside the open door, his voice pitched to carry "
        "exactly as far as it needed to and no further. \"Nothing more. "
        "I will only be a moment.\" He crossed to the small window, "
        "testing its shutter with exaggerated care, buying himself the "
        "handful of seconds his own courage needed to actually use."
    )},
    {"type": "body", "text": (
        "\"Guards are doubled from tonight,\" he said, quiet, his back "
        "still turned toward the door and the shutter still held in his "
        "own hands as though testing it truly were the whole of his "
        "purpose here. \"Trouble has found this ground from outside its "
        "walls, and a House that fears what it cannot yet name rarely "
        "grows kinder toward what it can.\""
    )},
    {"type": "body", "text": (
        "The guard at the door shifted his weight once, an ordinary "
        "soldier's small restlessness rather than any particular "
        "suspicion, and both of them heard it, and both of them let a "
        "full breath pass in silence before either dared speak again, "
        "each privately counting the same distance between the "
        "doorway and the window and finding, with some relief, that "
        "the sound had not carried further than an idle guard's own "
        "boredom."
    )},
    {"type": "body", "text": (
        "Ijeoma said nothing, understanding immediately that whatever "
        "this actually was, it was not the idle courtesy it was "
        "dressed as, and understanding, a beat later, that saying so "
        "aloud would be the single most dangerous thing either of them "
        "could do in this room."
    )},
    {"type": "body", "text": (
        "\"I do not know your circumstances,\" the Factor continued, "
        "still not turning, still testing a shutter that had needed no "
        "testing at all. \"I do not ask to know them. I know only that "
        "whatever choice you have been patiently waiting to make, I "
        "would not wait much longer to make it. This House does not "
        "grow more generous with time. It only ever grows shorter with "
        "it.\""
    )},
    {"type": "body", "text": (
        "He latched the shutter, finally, and turned to face her fully "
        "for the first time since entering, the two of them standing "
        "close enough now that neither the guard at the door nor "
        "anyone passing beyond it could have read anything from their "
        "faces except the ordinary blankness of an inspection concluded "
        "without incident."
    )},
    {"type": "body", "text": (
        "\"Thank you for your patience with the review,\" he said, "
        "louder now, the words aimed plainly past her toward the door. "
        "\"The window latch is sound. I will note it in the report.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "He walked away from that small room afterward with his pulse "
        "loud enough in his own ears that he half expected the guard "
        "outside to hear it too, and did not allow himself to exhale "
        "properly until he had put two full corridors between himself "
        "and the door he had just closed behind him."
    )},
    {"type": "body", "text": (
        "He had broken no law that any careful reading of his own "
        "conduct could name outright. He had said nothing a suspicious "
        "listener could not explain away as an overseer's idle "
        "observation about the household's mood. He understood, all "
        "the same, walking those two corridors with his hands not "
        "quite steady at his sides, that he had just crossed a "
        "distance far greater than a roster's quiet edit or a knot left "
        "unreported. He had spoken to her directly, deliberately, with "
        "intent she could not possibly mistake for anything but what it "
        "actually was."
    )},

    {"type": "body", "text": (
        "There was no scuffing this mistake smooth afterward, no ledger "
        "line to quietly misfile. If she ever repeated a single word of "
        "it to the wrong ear, willingly or under pressure this House "
        "knew well how to apply, his own account would close far faster "
        "than hers ever had."
    )},

    {"type": "body", "text": (
        "He thought, walking those last corridors back toward his own "
        "quarters, of the ledger line he had once refused to read as a "
        "person, and of every quiet season since that he had spent "
        "half convincing himself that scuffed mud and canceled bracelet "
        "runs were the whole of what conscience could reasonably ask of "
        "a man in his position. He understood now, hands finally "
        "steadying at his sides, that conscience had never once been "
        "satisfied with those small, deniable gestures. It had only "
        "been patient, waiting for him to run out of smaller ways to "
        "avoid the larger one."
    )},
    {"type": "body", "text": (
        "He did not know, closing his own door behind him at last, "
        "whether what he had just done would save her, cost her, or "
        "change nothing at all beyond the private relief of having "
        "finally said something true out loud instead of merely "
        "thinking it. He found, turning the uncertainty over one last "
        "time before forcing himself back to the ordinary business of "
        "the day, that he could live with any of those outcomes far "
        "more easily than he could have lived with silence."
    )},
    {"type": "body", "text": (
        "Ijeoma, alone again behind her own closed door, sat a long "
        "while turning the visit over with the same patient counting "
        "she turned over everything now, unable to decide whether she "
        "had just been given a warning, a test, or something closer to "
        "an apology arriving three years too late to matter. She "
        "decided, in the end, that it did not matter which. A man with "
        "nothing to gain from lying to her had told her, plainly enough "
        "to act on, that her own window was closing faster than she had "
        "let herself believe. She would be a fool, this House had "
        "already taught her at real cost, to spend that warning on "
        "wondering about the stranger who gave it rather than on what "
        "she meant to do with the time he had just handed her."
    )},
    {"type": "body", "text": (
        "She thought of the wall's bad corner, of the black water she "
        "still could not read, of the guard whose careless habit had "
        "held steady across every doubled watch since. She thought of "
        "the knot traveling somewhere downriver toward hands she could "
        "not choose. None of it, laid out honestly, added up yet to "
        "anything she could call a real plan. It added up, for the "
        "first time in two long seasons of patient counting, to "
        "something that finally felt like urgency rather than waiting, "
        "and she found, sitting alone with the compound's new watch "
        "settling into its harsher rhythm outside her window, that she "
        "trusted the feeling far more than she trusted the stranger who "
        "had handed it to her."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
