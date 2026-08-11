#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 114: "The Kindness No One Will Trace"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The Factor makes his first
deniable act of conscience, folding a small, permanent change to the
eastern gate's duty roster inside a routine reshuffle no one will ever
read closely enough to notice. The Warden, still unmoved by Mfoniso's
call for caution, sets an informal deadline for Ijeoma's fate. Act Two
hook.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 114
EPISODE_TITLE = "The Kindness No One Will Trace"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Fourteen"},
    {"type": "title_ep_name", "text": "The Kindness No One Will Trace"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE FACTOR
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The duty roster was the single most boring document the "
        "Concern produced, forty names rotated across gates and "
        "corridors and storerooms in a pattern no one above the guard "
        "captain's own rank had ever once bothered to read closely, and "
        "the Factor had chosen it for exactly that reason."
    )},
    {"type": "body", "text": (
        "He had been assigned, as one of a dozen small administrative "
        "duties left to him since the Warden stripped away anything "
        "that touched the Mfoniso operation directly, the quarterly "
        "review of household staffing, a task so far beneath his "
        "former authority that he suspected it had been given to him "
        "as a quiet insult rather than genuine work. He had accepted it "
        "without complaint. A man with nothing left to do but read "
        "rosters eventually learned every gap and habit those rosters "
        "actually contained."
    )},
    {"type": "body", "text": (
        "He thought, sitting alone with the roster spread across his "
        "own desk, of the single moment weeks ago when he had passed "
        "close enough to the guest to actually see her, properly, for "
        "the first time in two full seasons of signing his own name to "
        "her keeping. He had expected, if he expected anything at all, "
        "to feel nothing new. Instead he had felt the particular, "
        "specific shame of a man who had spent two seasons treating a "
        "line in a ledger as though it could not also be a person "
        "watching the wall of her own courtyard the way a caged bird "
        "watches an open window it has never once been allowed near."
    )},
    {"type": "body", "text": (
        "That shame had not gone anywhere since. It had simply learned "
        "to sit quietly beneath his ordinary work, the way a debt sits "
        "quietly on a ledger's back page long after the front pages "
        "have moved on to other business, waiting only for an occasion "
        "patient enough to finally call it due."
    )},
    {"type": "body", "text": (
        "The change he made was small enough to be almost invisible "
        "even to himself once it was finished. The eastern gate's "
        "morning post, currently held by a single guard for the full "
        "stretch between dawn and the midmorning changeover, would now "
        "be split into two shorter watches with a formal handoff "
        "between them, a perfectly ordinary security improvement any "
        "careful captain might have proposed on his own initiative."
    )},
    {"type": "body", "text": (
        "What the change actually did, buried inside its reasonable "
        "administrative logic, was give the same guard a second, "
        "shorter absence each morning, this one official, logged, and "
        "entirely beyond question, precisely at the handoff point "
        "between his two new shorter shifts."
    )},
    {"type": "body", "text": (
        "The Factor did not know, could not have known, exactly what "
        "use such a gap might someday serve, only that a household "
        "guard willing to look away from one thing once might, given "
        "enough quiet opportunity, be willing to look away from "
        "something larger later, and that a man in his own position, "
        "stripped of every direct way to help anyone, had almost "
        "nothing left to offer except the shape of other people's "
        "opportunities."
    )},
    {"type": "body", "text": (
        "He checked his own reasoning three separate times before he "
        "was willing to submit it, turning the proposal over the way he "
        "had once, in better standing with this House, turned over a "
        "contract worth more than most men saw in a lifetime, hunting "
        "for any clause an opponent might later use against him. There "
        "was nothing in the new roster a suspicious captain could point "
        "to. There was nothing in it, on paper, but sound and sensible "
        "administration from a man everyone in this House had long "
        "since stopped expecting anything dangerous from at all, which "
        "was, he understood clearly, exactly what made it safe to "
        "attempt."
    )},
    {"type": "body", "text": (
        "He filed the revised roster through the normal channel, "
        "countersigned by the guard captain without a second glance, "
        "and told himself, walking back to his own quarters afterward, "
        "that he had done nothing more than tidy an inefficient "
        "schedule. It was, he understood even as he told himself so, "
        "the same small lie he had told himself scuffing mud smooth at "
        "the wall's weak corner. He was getting better at telling it "
        "convincingly. He was not certain that was a virtue worth being "
        "proud of."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ijeoma noticed the change on the second morning it was in "
        "effect, the way she noticed everything about this compound "
        "now, without seeming to notice anything at all. The eastern "
        "gate's guard still left his post at roughly the hour she had "
        "long since learned to expect him gone. But he returned "
        "sooner than her old counting predicted, and a second man, "
        "unfamiliar, took the post for a short stretch afterward before "
        "the first guard reclaimed it again, a formal handoff conducted "
        "in the open where any passing servant could see it happen."
    )},
    {"type": "body", "text": (
        "She did not yet understand what the change actually meant, "
        "only that it meant something, a household rarely rewrote a "
        "guard's post without a reason worth the paperwork it cost. She "
        "filed the new pattern away the same patient way she filed "
        "everything else this compound gave her without asking, "
        "unwilling to guess at its purpose before she had watched it "
        "repeat itself enough mornings to trust what it was actually "
        "showing her."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: THE WARDEN
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden summoned Mfoniso back to her study three days "
        "after their first meeting, not because anything new had "
        "changed but because the Factor's quiet administrative work, "
        "however unremarkable it looked on paper, had reminded her, "
        "reviewing the same staffing documents herself the following "
        "morning, exactly how long this House had now spent managing an "
        "asset it had not yet decided how to finally close out."
    )},
    {"type": "body", "text": (
        "\"I have given your caution three days to become something "
        "more useful than a feeling,\" the Warden said without "
        "preamble, watching Mfoniso settle into the chair across from "
        "her with the same wary stillness she had left the room in. "
        "\"I would like to know what, specifically, you intend to do "
        "with the time you asked me for.\""
    )},
    {"type": "body", "text": (
        "\"I intend to learn more about the guardian that met me at "
        "Idoro,\" Mfoniso said, choosing honesty over comfort, the "
        "strategy that had served her best with the Warden across "
        "every year of their working acquaintance. \"If it is what I "
        "now suspect it is, understanding it properly may matter more "
        "to this House's long survival than one guest's fate ever "
        "could.\""
    )},
    {"type": "body", "text": (
        "The Warden considered that for a long moment, turning it the "
        "way she turned every claim a subordinate made on her patience, "
        "weighing its actual value against its cost in time she did not "
        "particularly enjoy spending. \"That is a more interesting "
        "answer than I expected,\" she allowed finally. \"It does not, "
        "however, change the fact that a valuable, undecided asset sits "
        "in this compound eating this House's patience along with its "
        "food, and I am not a woman who enjoys watching a ledger sit "
        "open indefinitely on anyone's account, including yours.\""
    )},
    {"type": "body", "text": (
        "\"Then give me a number,\" Mfoniso said, flat, refusing to let "
        "the Warden's careful vagueness stand in for an actual answer. "
        "\"Days, not feelings. I have spent my whole career working "
        "toward numbers I could actually plan against. I would rather "
        "have one now than keep guessing at the edge of your "
        "patience.\""
    )},
    {"type": "body", "text": (
        "\"Ten days,\" the Warden said, the number arriving with the "
        "flat finality of a decision that had already been made before "
        "Mfoniso ever walked into the room, dressed up only now as a "
        "negotiation for her benefit. \"Ten days from today, you bring "
        "me a recommendation I can act on, closed account or continued "
        "asset, with reasons I can defend to people above even me if it "
        "ever comes to that. If ten days pass and you have brought me "
        "nothing better than another feeling, I will make the decision "
        "myself, and I promise you it will not be the patient one.\""
    )},
    {"type": "body", "text": (
        "\"Ten days,\" Mfoniso repeated, testing the number's weight "
        "the way she might have tested a blade's balance before "
        "trusting it to a real fight. \"And if I bring you a "
        "recommendation you do not like within those ten days.\""
    )},
    {"type": "body", "text": (
        "\"Then I will still hear it,\" the Warden said, \"because I "
        "have never once doubted your judgment on the work itself, "
        "only your speed in delivering it. What I will not do is wait "
        "an eleventh day for a recommendation I could have had on the "
        "tenth. This House has survived longer than either of us by "
        "never mistaking patience for a virtue owed indefinitely to "
        "anyone, including its own most valuable hunter.\""
    )},
    {"type": "body", "text": (
        "Mfoniso accepted the number the way she had learned, across "
        "years of hard training, to accept any hard limit she could not "
        "argue away, with a short nod and no visible flinch, though "
        "something in her chest tightened all the same at the thought "
        "of ten days being enough time to properly understand a "
        "guardian three centuries in the making."
    )},
    {"type": "body", "text": (
        "Neither woman spoke of it again that evening, but the number "
        "sat afterward in the compound's own quiet air the way a "
        "storm sits over a river before it finally breaks, unseen by "
        "the guest whose life it had just quietly begun to measure, "
        "unseen by a search party still many days out on a bearing "
        "neither woman in that study had any reason yet to fear, and "
        "unseen, most of all, by a guard now working a schedule quietly "
        "reshaped by a man neither woman in that study suspected of "
        "wanting anything at all from this House but its own eventual, "
        "long overdue conscience."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
