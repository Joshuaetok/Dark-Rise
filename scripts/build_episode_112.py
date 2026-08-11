#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 112: "What the Record Was Trying to Say"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Idoro's fast rider reaches
Udo with formal word of Episode 106's discovery, the same House lineage
holding Ijeoma emptied the presence's lost ground three centuries ago.
Nkiruka, hearing it land beside her own private archive fragment (the
border village record that stops mid page, marked with the same spiral),
finally understands the pattern rather than a single old mystery, and
decides she can no longer keep it from Eze Amadi.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 112
EPISODE_TITLE = "What the Record Was Trying to Say"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twelve"},
    {"type": "title_ep_name", "text": "What the Record Was Trying to Say"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "The rider Amara had sent reached Udo on the ninth day, dust "
        "colored and hoarse, having changed horses twice along a road "
        "he had ridden faster than any message out of Idoro had ever "
        "traveled before. He was brought before Eze Amadi still half "
        "unsteady on his own feet, and delivered the household's report "
        "in the plain, unpolished language of a man who had been told to "
        "get every word right and had spent nine days rehearsing them "
        "rather than risk forgetting a single one."
    )},
    {"type": "body", "text": (
        "The search party had found more than a search party's ordinary "
        "luck. A hillside chamber built for holding people rather than "
        "burying them. A House maker's mark burned into its binding "
        "cloth, the same mark, by Emenike's own recognition, used on "
        "messages left for him at the drop stone two seasons running. "
        "Whatever power or grief haunted Oso's forbidden bush and "
        "whatever House had taken Ijeoma from her family were not, as "
        "the crown's own investigation had assumed since Episode ninety "
        "four, two separate threats sharing a single unlucky bearing. "
        "They were one lineage, one hunger, at work on the same ground "
        "for at least as long as anyone in Idoro had ever kept count."
    )},
    {"type": "body", "text": (
        "He had ridden through two full nights without proper sleep, "
        "trusting each fresh horse to carry him a little further than "
        "the last one had managed, and stopping only long enough at "
        "each posting station to confirm the words in his head still "
        "matched the words Amara had made him repeat back to her three "
        "times before he was allowed to leave Idoro's own gate. He "
        "delivered them now standing, refusing the seat he was offered, "
        "as though sitting down before the message was fully given "
        "might somehow let some part of it slip away from him."
    )},
    {"type": "body", "text": (
        "\"Say that again,\" Eze Amadi said, quiet, when the rider "
        "finished, his voice carrying none of the sharpness he usually "
        "kept in reserve for reports that disappointed him, only the "
        "flat, focused attention of a king recalculating, in real time, "
        "exactly how large the trouble on his western edge had actually "
        "grown."
    )},
    {"type": "body", "text": (
        "Nkiruka stood at the edge of the receiving hall through the "
        "whole of it, as she always did when a report touched anything "
        "the crown's old rites and records might have a bearing on, and "
        "felt the report land inside her with a weight the rider "
        "himself could not have understood he was delivering."
    )},
    {"type": "body", "text": (
        "Ejikeme, present for what he had assumed would be an ordinary "
        "update on his own delta survey, asked the one question the "
        "room's stunned quiet had left unspoken. \"If this is truly one "
        "lineage's work rather than two threats sharing a bearing, does "
        "that not mean whoever sponsors this House at court already "
        "knows exactly what their own trading partner has been doing "
        "west of Idoro all along.\" No one in the hall had an answer for "
        "him, and Eze Amadi did not pretend to invent one."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She had served the crown's archive for close to twenty years "
        "by then, long enough to have learned that a keeper's worst "
        "failures were rarely the records lost to fire or flood or "
        "simple neglect. They were the records kept perfectly intact, "
        "correctly filed, and never once read closely enough by anyone "
        "with the authority to act on what they actually said. She had "
        "told herself, across the weeks she sat on her own copied "
        "pages, that she was being careful rather than negligent. "
        "Standing in that receiving hall tonight, she was no longer "
        "certain the difference between the two was as wide as she had "
        "wanted it to be."
    )},
    {"type": "body", "text": (
        "She did not go directly to her own archive room that evening. "
        "She made herself walk the long way first, past the kitchens "
        "and the empty training yard, giving her own racing thoughts "
        "time to settle into something she could trust before she let "
        "them anywhere near the record she had been sitting on since "
        "Episode ninety four."
    )},
    {"type": "body", "text": (
        "The record itself had not changed since she copied it out in "
        "full some weeks ago, a border village decades past, a coerced "
        "informant discovered exactly as Idoro's own had been, an "
        "account that simply stopped, mid page, pages lost or removed, "
        "and a small spiral mark hidden in the gutter that matched, "
        "precisely, the mark the search party had now found burned into "
        "the hillside chamber's own binding cloth."
    )},
    {"type": "body", "text": (
        "What had changed was everything around it. A single "
        "unresolved record from decades past could be filed away, "
        "uncomfortably, as an old mystery no one living had the power to "
        "solve. A single unresolved record that shared its exact mark "
        "with a hillside chamber currently being searched by four crown "
        "soldiers on the far side of nowhere was not a mystery anymore. "
        "It was a pattern, and patterns, in Nkiruka's long experience "
        "with the crown's old records, existed because whatever made "
        "them had done the same thing more than once and expected, "
        "reasonably, to keep doing it."
    )},
    {"type": "body", "text": (
        "She sat with her own copied pages spread across the low table "
        "in her archive room for a long while, tracing the spiral mark "
        "in the gutter with one finger the way she might once have "
        "traced a scar to learn its shape. The account did not simply "
        "stop because pages had been lost to time or damp or careless "
        "handling. She understood that now with a certainty she could "
        "not have defended in front of a skeptical court but trusted "
        "completely in her own private judgment. It stopped because "
        "whoever wrote it had been stopped, and whoever stopped them had "
        "left the mark behind, deliberately, the way a hunter marks "
        "ground it considers already settled."
    )},
    {"type": "body", "text": (
        "The dread that settled over her afterward was not the "
        "abstract, academic unease she had carried these past weeks, "
        "the private worry of a keeper sitting on an inconvenient old "
        "document. It was sharper than that now, and specific. Four "
        "living men, one of them a boy she had watched Osadebe train "
        "personally, were walking, at this exact hour, across ground "
        "that this same mark had already claimed at least once before "
        "and very possibly many times before that, entirely unaware "
        "that the last person known to have stood where they now stood "
        "had never finished telling anyone what she found there."
    )},
    {"type": "body", "text": (
        "\"I have kept something from you,\" Nkiruka told Eze Amadi "
        "directly, finding him still awake in his private study long "
        "past the hour any of his household would have expected him to "
        "be, her voice steadier than she had any right to expect it to "
        "sound. \"Not out of disloyalty. Out of caution, which I now "
        "believe was the wrong instinct entirely, and I would rather "
        "confess that to you tonight than let caution cost anyone else "
        "what it may already have cost a border village whose name I "
        "do not even know.\""
    )},
    {"type": "body", "text": (
        "Eze Amadi did not interrupt her once through the whole of it, "
        "the record's discovery, the mark in its gutter, its unfinished "
        "final page, the exact match to what Osadebe's rider had just "
        "carried nine hard days to reach him. When she finished, he sat "
        "silent for a long moment, turning the shape of what she had "
        "given him over with the same care she had once watched him "
        "give to Osadebe's very first report of a curse child's cry "
        "carrying across Idoro, a lifetime of the kingdom's business "
        "ago now, though it had been, in truth, only a handful of "
        "years."
    )},
    {"type": "body", "text": (
        "\"You will copy that record a second time,\" he said finally, "
        "\"and this copy rides west with the next courier we can spare, "
        "however long it takes to reach them. If Osadebe's party is "
        "walking ground this lineage has already emptied once, I would "
        "rather they walk it warned late than not warned at all. Send "
        "your fastest rider again, the same one if his own strength "
        "allows it, and tell him plainly what he is carrying this time "
        "before he leaves my gate.\" He said it the way a man says the "
        "harder of two available truths aloud, once, so that no one in "
        "the room could later claim he had chosen otherwise."
    )},
    {"type": "body", "text": (
        "\"There is one more thing you should know before I go,\" "
        "Nkiruka added, pausing at the study door rather than leaving "
        "it unsaid. \"Ejikeme asked tonight whether this House's court "
        "sponsor already knows what it has been doing west of Idoro. I "
        "do not know the answer. But I know now that I would rather we "
        "ask that question loudly and be wrong than keep sitting on it "
        "quietly and be right.\" Eze Amadi's silence, this time, was "
        "agreement rather than deliberation."
    )},
    {"type": "body", "text": (
        "Nkiruka bowed and withdrew to begin the copying immediately, "
        "grateful, more than she let herself show, that the king's first "
        "instinct had been the search party's safety and not his own "
        "wounded trust in a keeper who had waited this long to speak."
    )},
    {"type": "body", "text": (
        "She did not let herself say aloud, to Eze Amadi or to anyone, "
        "the second thought sitting beneath the first, that a courier "
        "however fast could not outrun ground the search party had "
        "already been walking for days, and that whatever unfinished "
        "warning her record actually carried might reach the four men "
        "who needed it only after they had already found, for "
        "themselves, and at whatever cost that finding demanded of "
        "them, exactly what it had been trying, all this time, "
        "patiently and in vain, to say."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
