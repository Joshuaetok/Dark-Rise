#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 110: "The Wrong Reason to Be Afraid"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The Warden, her patience with
Mfoniso's overdue answer running out, orders the guest's watch doubled for
reasons that have nothing to do with Episode 109's failed climb. Ijeoma
wakes to a visibly tightened compound, spends the day certain she has
been caught, and works through her fear with the same counting patience
that has kept her alive this long, concluding, without ever learning the
truth, that the eastern gate guard's continued silence is now an asset
worth banking rather than a mercy worth wasting.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 110
EPISODE_TITLE = "The Wrong Reason to Be Afraid"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Ten"},
    {"type": "title_ep_name", "text": "The Wrong Reason to Be Afraid"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE WARDEN
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The Warden had taken to counting the days since her ciphered "
        "question left for the river road the same private way she "
        "counted every debt she had ever extended, alone in her study "
        "each evening with the household long since settled for the "
        "night. Mfoniso's answer was overdue by none of the measures a "
        "courier could explain honestly, weather, distance, the ordinary "
        "hazards of a long road, and overdue by every measure the Warden "
        "trusted more than a courier's excuses. She had trained Mfoniso "
        "herself, in part, and a trained hunter did not simply forget "
        "how to answer a question put to her plainly."
    )},
    {"type": "body", "text": (
        "\"Double the watch on the guest,\" she told the household's "
        "guard captain that same morning, her voice flat in the way "
        "that had taught everyone beneath her, across many years of "
        "service, never to ask for a reason twice. The captain did not "
        "ask. He simply bowed and went to arrange it, and the Warden was "
        "left alone with the reason she had not given him, because it "
        "was not, in truth, a reason that belonged to anyone but her."
    )},
    {"type": "body", "text": (
        "The guard captain carried the order through the household with "
        "the same unhurried competence he had always shown, two more "
        "men added to the courtyard's daylight watch, one more posted "
        "for the first time in two seasons at the narrow gate behind "
        "the kitchens that led only to the well and back. None of it "
        "touched the eastern gate specifically, since nothing in the "
        "Warden's order had named any single post as the reason for the "
        "change, only the guest as a whole, and a careful captain built "
        "his watch around the whole compound rather than around a "
        "single man he had no particular cause to suspect."
    )},
    {"type": "body", "text": (
        "It was not that she suspected the guest of anything new. It "
        "was that a silence this long, from a hunter this reliable, had "
        "started to feel like the first loose thread in a working the "
        "Warden had spent two seasons believing was fully in her own "
        "hands. She did not like the feeling. She liked even less that "
        "she could not yet say, with any honesty, whether the silence "
        "meant Mfoniso was simply slow, or Mfoniso had begun, somewhere "
        "on that long southern road, to decide something the Warden had "
        "not authorized her to decide."
    )},
    {"type": "body", "text": (
        "She had canceled the bracelet proof runs already, told the "
        "Factor plainly that the guest's fate sat undecided between "
        "asset and expense. Now, waiting on an answer that refused to "
        "arrive, she found the balance tipping in her own private "
        "ledger without her quite choosing to tip it, the account "
        "looking, day by day, a little more like one that would be "
        "simpler closed than kept open indefinitely on the strength of "
        "a hunter's overdue courtesy."
    )},
    {"type": "body", "text": (
        "She thought, not for the first time that week, of the four "
        "keepers who had held this particular debt before her, each one "
        "passing the ledger on unfinished to the next, each one, she "
        "suspected, arriving eventually at exactly the private, weary "
        "arithmetic she was doing now. It was not a comforting thought. "
        "It was, she told herself, simply an old one, worn smooth by "
        "however many hands had carried it before hers, and she set it "
        "aside the way she set aside every thought that could not be "
        "spent on anything useful before nightfall."
    )},
    {"type": "body", "text": (
        "The tightened watch, she told herself, was only good sense in "
        "the meantime. A House with a valuable, undecided asset and an "
        "unaccountably silent field agent did not leave that asset "
        "lightly guarded while it waited to learn which way its own "
        "ledger would finally close. She did not think of the guest's "
        "own recent nights at all, and had no reason to. No one had "
        "told her there was anything recent to think of."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: IJEOMA
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ijeoma counted three new guards before she had even finished "
        "crossing the courtyard that morning, and felt her whole chest "
        "go cold and still in a way it had not gone since the night she "
        "climbed back down from the wall. Three new guards, a fourth "
        "posted at the kitchen door that had never held one before, and "
        "the housemistress watching her cross the yard with an "
        "expression Ijeoma could not read and did not trust herself to "
        "try reading too openly."
    )},
    {"type": "body", "text": (
        "These were not the same soldiers who had stood easy watch over "
        "her for two seasons, grown lazy and familiar with a guest who "
        "caused no trouble. These were younger men, borrowed, she "
        "guessed, from whatever posting the House kept in reserve for "
        "exactly this kind of sudden need, their spears held a fraction "
        "too upright, their eyes moving over the compound the way a "
        "person's eyes move over unfamiliar ground rather than a place "
        "they had already learned to stop truly seeing."
    )},
    {"type": "body", "text": (
        "They know, she thought, and made herself keep walking at "
        "exactly the pace she would have walked on any ordinary morning, "
        "the same discipline that had carried her back from the wall's "
        "bad corner three mornings ago. They know, and this is simply "
        "the slow, patient shape of a House deciding how to punish "
        "something before it announces the punishment aloud."
    )},
    {"type": "body", "text": (
        "She spent the whole morning at the laundry line rebuilding the "
        "same careful blankness that had gotten her this far, counting "
        "now not the guard's gap but every glance thrown her way, every "
        "pair of eyes that lingered a beat longer than the work in front "
        "of them required. By midday she had catalogued nothing that "
        "confirmed her fear and nothing that disproved it either, only a "
        "compound that felt, for the first time in two seasons, like it "
        "was actually watching her rather than simply keeping her."
    )},
    {"type": "body", "text": (
        "A new guard, young and clearly uncomfortable in a post he had "
        "only been given that morning, stopped her once near the "
        "kitchen door and asked, stiffly, why her basket looked half "
        "empty. \"Because half of what I gathered was already dry,\" "
        "she answered, keeping her voice as unremarkable as the truth "
        "actually was, and watched him decide, visibly, that the answer "
        "bored him more than it interested him. He waved her on without "
        "another word. It told her nothing about what the House knew. "
        "It told her a great deal about how thin the new watch's "
        "patience already ran, stretched over men who did not yet fully "
        "understand what they were meant to be watching for."
    )},
    {"type": "body", "text": (
        "The one thing she watched hardest, without ever once looking "
        "directly at him, was the eastern gate. If the guard had told "
        "them, she reasoned, the new watch would surely have replaced "
        "him first of anyone, the plainest and easiest confession a "
        "frightened House could make without ever admitting why it was "
        "making it. He was still there. Same post, same slouch of the "
        "shoulders, same private minute at midmorning when he stepped "
        "away from it exactly as he always had, as though nothing in "
        "the compound around him had changed at all."
    )},
    {"type": "body", "text": (
        "That, more than anything else the day offered her, was what "
        "finally let her breathe again. Not proof. She had learned two "
        "seasons ago that this House rarely handed out proof of "
        "anything to a person it had already decided to distrust. But a "
        "guard who still kept his own careless habit, unwatched, "
        "unpunished, unreplaced, was as close to proof as a woman with "
        "nothing but her own counting could reasonably ask for."
    )},
    {"type": "body", "text": (
        "She turned the fact over slowly that evening, alone in the "
        "small room that was still, despite everything, her whole "
        "world. He had seen her. He had said, by every evidence "
        "available to her, nothing at all. She had spent the last three "
        "days treating that silence as a mercy she had been lucky enough "
        "to receive, something to be grateful for and otherwise leave "
        "alone before her own gratitude drew attention to it."
    )},
    {"type": "body", "text": (
        "Sitting with the tightened compound pressing in around her on "
        "every other side, Ijeoma decided, with the same deliberate "
        "patience her mother had once used to weigh a bolt of cloth "
        "against its asking price, that luck was a poor word for what "
        "the guard had actually given her. A man did not simply forget "
        "to report what he had seen. He chose not to, every single "
        "morning since, and a choice repeated that many times in a row "
        "was not mercy. It was information, the same kind of information "
        "a trader's daughter had been trained since childhood to notice "
        "and never waste."
    )},
    {"type": "body", "text": (
        "She did not yet know what the information was worth, or "
        "whether it could ever be turned into anything more useful than "
        "a single, unrepeatable act of luck. But she began, that night, "
        "to watch him the way she had once watched the eastern gate's "
        "gap itself, patiently, without letting the watching show, "
        "counting toward an answer she was not yet ready to name aloud "
        "even to herself."
    )},
    {"type": "body", "text": (
        "She let herself think of her brother only once that whole long "
        "day, briefly, in the hour before sleep. Emenike would tell her, "
        "if he were here, that patience this careful was the same "
        "patience their mother had used to survive three bad harvests "
        "in a row without ever once letting the family go hungry in "
        "front of the neighbors. Ijeoma did not know, lying in the dark "
        "with the compound's new watch settling into its own "
        "unfamiliar rhythm outside her window, that her brother, and "
        "three other men she had never met, were walking toward her at "
        "that very hour, still many days out, but closer, every single "
        "day, than they had been the day before."
    )},
    {"type": "body", "text": (
        "She never learned, that night or any night soon after, that "
        "the guards multiplying around her had nothing to do with a "
        "climb she had already survived. The net closing slowly around "
        "the compound was not hers. It belonged to a woman two rooms "
        "away who had stopped believing, for reasons of her own, that "
        "silence from the river road could still be trusted to mean "
        "nothing. If Mfoniso's answer did not arrive soon, the watch the "
        "Warden had doubled tonight would not need Ijeoma's own secret "
        "to justify what came next."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
