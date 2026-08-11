#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 118: "Quiet Enough to Deny"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Eze Amadi, Nkiruka, and
Ejikeme weigh what the crown can actually do for a search party standing
outside crown jurisdiction, against a House whose court sponsor may
already be watching for exactly this kind of move. They authorize a
small, deniable detachment rather than open force, and the order travels
to Idoro, where Chidebe quietly hands the mission to Adaeku.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 118
EPISODE_TITLE = "Quiet Enough to Deny"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Eighteen"},
    {"type": "title_ep_name", "text": "Quiet Enough to Deny"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: UDO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The rider's report and Nkiruka's confession had settled a "
        "great many questions between them in a single long evening. "
        "They had settled almost nothing about what to actually do "
        "with the answer, and it was that harder question, rather than "
        "the discovery itself, that had finally brought all three of "
        "the crown's most trusted advisors back to the same table six "
        "days later, tempers shorter and patience thinner than any of "
        "them liked to admit."
    )},
    {"type": "body", "text": (
        "\"An army is the wrong tool for this problem,\" Eze Amadi "
        "said, standing over the same table where Osadebe's rider had "
        "delivered his report, tracing with one finger a bearing that "
        "led well past anything a crown map could honestly call his "
        "own ground. \"A crown army marching openly toward a foreign "
        "House's disguised headquarters is not a rescue. It is a "
        "declaration, and I have no wish to discover, only after the "
        "fact, exactly whose interests that declaration would end up "
        "serving.\""
    )},
    {"type": "body", "text": (
        "\"And yet doing nothing serves this House perfectly,\" "
        "Ejikeme said, his own patience visibly thinner than usual, "
        "the same patience that had already carried a delta survey "
        "through two refusals before finally winning approval. "
        "\"Four of our own men are standing outside a fortress with no "
        "reinforcement, no supply line, and no way to call for either "
        "if the ground turns against them. Caution is a fine policy "
        "for a court. It is a poor policy for men who may already be "
        "dying while we debate the correct word for helping them.\""
    )},
    {"type": "body", "text": (
        "Nkiruka, who had spent longer than either man in this room "
        "weighing exactly how a single hasty decision could unravel "
        "years of patient work, spoke more carefully. \"I do not "
        "disagree that they need help,\" she said. \"I disagree with "
        "sending help in a shape this House, or whoever sponsors it at "
        "this very court, would recognize as the crown's own hand the "
        "moment it appeared. Ejikeme himself asked the question that "
        "should still be sitting uncomfortably with all of us. If this "
        "House's sponsor already knows what it has been doing west of "
        "Idoro, then anything we send wearing the crown's colors "
        "arrives already expected, and expected help is very often "
        "help that walks straight into a trap someone else has had "
        "ample time to prepare.\""
    )},
    {"type": "body", "text": (
        "Ikwuano, summoned to the same table for his own quiet "
        "expertise, offered the one piece of comfort the room actually "
        "had to spend. \"My own tracing of this House's court "
        "connections has found no sign yet that its sponsor knows "
        "anything beyond the ordinary business a sponsor is meant to "
        "know,\" he said. \"That is not proof of innocence. It is only "
        "proof that if guilt exists, it has been kept carefully enough "
        "that two seasons of patient searching have not yet found its "
        "edge. I would rather we act as though it might be watching "
        "than discover too late that it was.\""
    )},
    {"type": "body", "text": (
        "The three of them sat with that for a long moment, the "
        "particular uncomfortable silence of people who all wanted the "
        "same outcome and could not yet agree on the shape that "
        "outcome should take."
    )},
    {"type": "body", "text": (
        "\"Then we send help that is not the crown's hand,\" Eze Amadi "
        "said finally, the decision arriving the way his decisions "
        "usually arrived once he had let every side of a problem "
        "finish speaking, quiet and complete rather than sudden. \"A "
        "small number. Men skilled enough to matter and few enough to "
        "pass, if anyone ever asks, as nothing more than a trading "
        "party of our own, armed the way any sensible trader arms "
        "himself on a dangerous road. If they are ever questioned, this "
        "crown will know nothing of them. I would rather protect this "
        "kingdom's wider position with a comfortable lie than protect "
        "it by leaving four good men to face that wall entirely "
        "alone.\""
    )},
    {"type": "body", "text": (
        "\"Where do such men come from,\" Ejikeme asked, \"if not from "
        "your own royal guard, which is precisely the force everyone "
        "would recognize on sight.\""
    )},
    {"type": "body", "text": (
        "\"From Idoro,\" Eze Amadi said. \"Chidebe's garrison there was "
        "doubled for exactly this kind of need, and Chidebe himself has "
        "earned enough of my trust across two seasons of difficult "
        "service to choose the right men without needing me to choose "
        "them for him. The order rides to Idoro today. What Chidebe "
        "does with it is his own careful judgment to make.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: IDORO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The crown's order reached Chidebe six days later, brief and "
        "carefully worded, authorizing a small detachment, deniable in "
        "shape and purpose, to follow the search party's last reported "
        "bearing and render whatever support it safely could without "
        "ever identifying itself as crown service."
    )},
    {"type": "body", "text": (
        "He read it twice before he called for Adaeku, and found, "
        "reading it a second time, that the choice of who to send had "
        "already made itself in his own mind somewhere between the "
        "first reading and the second."
    )},
    {"type": "body", "text": (
        "Adaeku had spent those same two seasons doing the kind of "
        "quiet, unremarked work that rarely earned a soldier much "
        "notice from anyone above him, standing his watches, keeping "
        "his own counsel, offering an opinion only on the rare "
        "occasions one was actually asked of him. He had told himself, "
        "more than once, that this was simply his own nature rather "
        "than any deliberate strategy. Standing now in front of "
        "Chidebe, summoned for reasons not yet explained to him, he "
        "began to suspect his nature had been quietly auditioning him "
        "for exactly this moment the whole time without either of them "
        "fully realizing it."
    )},
    {"type": "body", "text": (
        "\"You have never once, in two seasons under my command, drawn "
        "attention to yourself that the moment did not actually "
        "require,\" Chidebe said, when Adaeku stood before him, the "
        "same quiet soldier who had once been the only one of six "
        "informant suspects to prove, simply by having nothing at all "
        "to hide, that his own night had passed exactly as ordinary as "
        "it looked. \"That quality was worth little to me during the "
        "informant search beyond clearing your name. It may be worth a "
        "great deal now.\""
    )},
    {"type": "body", "text": (
        "\"You want me to find them,\" Adaeku said, understanding "
        "before Chidebe had finished laying the mission out in full, "
        "the particular economy of a man who had always preferred "
        "listening closely to speaking often."
    )},
    {"type": "body", "text": (
        "\"I want you to find them, and I want whoever sees you doing "
        "it to see nothing more remarkable than a small trading party "
        "moving cautiously through dangerous country,\" Chidebe said. "
        "\"You will carry no crown marking, no crown weapon that could "
        "not pass as a trader's own protection, and no name that "
        "connects you to this garrison if anyone ever asks. Choose two "
        "men you trust completely. Move fast. Osadebe's party has been "
        "gone long enough now that every day you spend deciding is "
        "another day further behind them.\""
    )},
    {"type": "body", "text": (
        "Adaeku chose his two companions before the sun had fully set "
        "that same evening, quiet, capable men from among the doubled "
        "garrison's newer arrivals, neither of them well known enough "
        "in Idoro to be missed loudly if their absence was ever "
        "noticed at all. They left before dawn the following morning, "
        "dressed and provisioned exactly as Chidebe had ordered, "
        "carrying nothing that could not be explained away as an "
        "ordinary trader's caution against an extraordinary road."
    )},
    {"type": "body", "text": (
        "Amara, told only that help was being sent and nothing of its "
        "careful, deniable shape, asked Chidebe plainly whether three "
        "men were truly enough against whatever waited at the end of "
        "that bearing."
    )},
    {"type": "body", "text": (
        "\"Enough to find them and stand beside them,\" Chidebe said, "
        "honest with her in a way his own report to Eze Amadi had "
        "carefully avoided being. \"Not enough, if it comes to it, to "
        "take a wall that size by force. I did not choose the size of "
        "this help. I chose only to make certain it was the right men "
        "carrying it.\""
    )},
    {"type": "body", "text": (
        "Amara found Adaeku herself before he left, in the last quiet "
        "hour before dawn, and pressed into his hand a small folded "
        "cloth that held nothing more valuable than dried meat and a "
        "few coins, the same practical send off she had once given "
        "Emenike's own search party at its own departure. \"I do not "
        "know you well,\" she admitted, \"but I know Chidebe chose you "
        "for a reason he trusts completely, and that is enough for me "
        "to trust it too. Bring back whoever you find out there. All "
        "of them, if it can be managed.\""
    )},
    {"type": "body", "text": (
        "\"I will do everything three careful men can do,\" Adaeku "
        "said, accepting the cloth with a small, formal bow that felt, "
        "to him, entirely inadequate to the weight of what she was "
        "actually asking. \"I cannot promise you more than that "
        "honestly, and I would rather give you an honest promise than "
        "a comfortable one.\""
    )},
    {"type": "body", "text": (
        "It was, Amara thought, watching the three of them vanish "
        "westward into a sky still more gray than blue, exactly the "
        "kind of answer that made her trust Chidebe's choice completely."
    )},
    {"type": "body", "text": (
        "Ejikeme, back in Udo, watched the three riders' departure "
        "logged in the crown's own quiet record with a satisfaction "
        "that did not fully settle his own private unease. Deniable "
        "help was still help moving on a bearing that a patient enemy, "
        "watching the right roads closely enough and for long enough, "
        "might eventually notice regardless of how carefully it was "
        "dressed. He found himself hoping, without much confidence, "
        "that whoever truly sponsored the Concern at this very court "
        "had not yet learned to watch those particular roads at all."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
