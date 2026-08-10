#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 108: "What Her Teacher Never Finished Telling Her"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): Mfoniso's road south to the
Concern's headquarters, threaded with a flashback to the training memory
where her teacher first told her the story of the lineage's old
conquest. In the present, without proof she could name, she senses that
something has disturbed the ground the story was always about.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 108
EPISODE_TITLE = "What Her Teacher Never Finished Telling Her"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Eight"},
    {"type": "title_ep_name", "text": "What Her Teacher Never Finished Telling Her"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "The river road south ran through country Mfoniso had traveled "
        "so many times she no longer needed to watch her own feet to "
        "know where the ground would rise or fall. Palm crowns leaned "
        "over the track at the same tired angle they always had, and the "
        "air carried the same low smell of standing water and turned "
        "earth that had greeted her on every southward walk of her "
        "career. She let her mind wander instead, which she rarely "
        "allowed herself, and it wandered, as it had every evening since "
        "the ridge, back to a training ground she had not stood on in "
        "over a decade."
    )},
    {"type": "body", "text": (
        "She had been perhaps twelve the first time her teacher told "
        "her the story properly, not the shortened version given to "
        "children too young to carry it, but the full account, over a "
        "cooking fire on a night the older woman had judged her finally "
        "ready to hear it without flinching."
    )},
    {"type": "body", "text": (
        "\"Our line did not begin as hunters of guardians,\" her "
        "teacher had said, turning a skewer of meat with the "
        "unhurried patience she brought to everything. \"We began as "
        "trackers of ordinary men, paid well by ordinary Houses for "
        "ordinary work. It was your great grandmother's grandmother who "
        "first proved a guardian ground could be taken the same way any "
        "other ground could be taken, if a hunter was patient enough to "
        "learn what the guardian loved and slow enough never to be seen "
        "reaching for it directly.\""
    )},
    {"type": "body", "text": (
        "Young Mfoniso had asked, the way any child asks a question "
        "without weighing its cost first, what had happened to the "
        "people who lived on that ground once the guardian was drawn "
        "away from it. Her teacher's face had done something then that "
        "Mfoniso, at twelve, had read as simple pride and only much "
        "later, turning the memory over on lonely roads like this one, "
        "began to suspect had actually been something closer to "
        "practiced composure."
    )},
    {"type": "body", "text": (
        "\"They were resettled,\" her teacher had said. \"Moved to "
        "serve the House that had won the ground, the way any "
        "conquered people is moved to serve the hand that conquered "
        "them. It was, for its time, considered a mercy. Better a new "
        "master than no ground at all.\" She had not elaborated further, "
        "and young Mfoniso, hungry and half asleep by then, had not "
        "thought to ask her to. It was only a story about the family "
        "business, the kind every child in every trade is told to "
        "explain why the work is theirs to inherit."
    )},
    {"type": "body", "text": (
        "Walking the river road now, a grown woman with three centuries "
        "of consequence sitting differently on her than it had at "
        "twelve, Mfoniso found herself circling the word resettled the "
        "way a tongue circles a broken tooth, unable to leave it alone "
        "precisely because touching it hurt. Resettled where. Resettled "
        "for how long. Resettled by whose hand, holding whose ledger, "
        "counting them the way the Warden's own ledgers counted "
        "Ijeoma. She had signed her own name to enough ledgers by now to "
        "know exactly how gentle a word could be made to sound when the "
        "thing it stood for was not gentle at all."
    )},
    {"type": "body", "text": (
        "There had been a second lesson, years later, that Mfoniso had "
        "not thought of in a long time and found waiting for her now "
        "with an unpleasant clarity, as though it had simply been "
        "standing in a corner of her memory all along, patient, "
        "expecting eventually to be called on."
    )},
    {"type": "body", "text": (
        "She had been sixteen, past the age of stories and into the "
        "age of practice, and her teacher had walked her through the "
        "shape of the tactic itself using nothing more than sticks laid "
        "out on packed earth, one stick for the guardian, a scatter of "
        "smaller ones for the people it loved, a single stone set apart "
        "for the hunter. \"You never move against the guardian first,\" "
        "her teacher had said, moving the stone slowly around the "
        "circle of sticks without ever touching the center one. \"You "
        "move against what it will run toward. It empties its own "
        "strength running. Then the ground is simply there for the "
        "taking, undefended, and no one ever has to test whether the "
        "guardian itself could have been beaten honestly.\""
    )},
    {"type": "body", "text": (
        "Mfoniso, sixteen and eager to be praised, had asked whether "
        "any guardian had ever seen the tactic coming and refused to "
        "run. Her teacher had smiled at that, an expression Mfoniso "
        "had once mistaken for warmth and now, walking the river road "
        "with a decade of harder knowledge behind her, recognized as "
        "something closer to respect for a worthy opponent already "
        "defeated. \"One did,\" her teacher had said. \"Once, a very "
        "long time ago. It nearly cost the lineage everything it had "
        "built. We do not speak of that one often.\" She had moved the "
        "lesson on before Mfoniso could ask which guardian, or where, "
        "or what nearly costing everything had actually looked like up "
        "close."
    )},
    {"type": "body", "text": (
        "Mfoniso understood now, with the particular sick clarity of a "
        "lesson finally landing fifteen years late, that she had spent "
        "her whole career using a tactic built from a single old "
        "victory her own teacher had never once let her examine closely "
        "enough to see the cost of. She had used it herself, against "
        "Kene, and it had failed, the guardian meeting her in the open "
        "exactly the way her teacher had once said only one guardian, "
        "long ago, ever had. She had told herself at the time that the "
        "failure was simply bad fortune, a single unlucky exception in "
        "an otherwise reliable method. Walking the river road now, that "
        "explanation felt thin in a way it never had before, worn "
        "through in exactly the place a person only notices once they "
        "have already put their full weight on it."
    )},
    {"type": "body", "text": (
        "\"We do not speak of that one often,\" she said aloud to the "
        "empty road, tasting the old sentence properly for the first "
        "time in her adult life. She wondered, and did not like how "
        "easily the wondering came to her now, whether the guardian her "
        "teacher had refused to name and the guardian that had finally "
        "met her at Idoro's compound wall were, against every reasonable "
        "probability, the very same one."
    )},
    {"type": "body", "text": (
        "Her teacher had never finished the story past that word. Not "
        "that evening, not in any of the years of training that "
        "followed it. Mfoniso had never once, until this exact walk "
        "south, thought to notice the story had an ending that had "
        "simply never been told to her, the way a house might have a "
        "room whose door no one in the family ever quite got around to "
        "opening in front of the children."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She made camp that night in a dry hollow off the road, a "
        "resting place she had used a dozen times before without "
        "incident, and it was there, settling into sleep, that the "
        "feeling first found her. Not a sound. Not a sight. A pressure "
        "at the very edge of the second thread she had carried since "
        "before she could remember carrying it, the thin, old line that "
        "ran from her back to her teacher and, through her teacher, "
        "further back than either of them had ever spoken of aloud."
    )},
    {"type": "body", "text": (
        "The pressure was not pain. It was closer to the feeling of a "
        "held breath released somewhere far away, a tension gone slack "
        "that she had never once, in all her years of carrying the "
        "thread, felt slacken before. She sat up in the dark, every "
        "instinct her training had ever given her suddenly alert to a "
        "danger she had no name for and no direction to point at. Her "
        "hand went to the knife at her hip out of pure habit before her "
        "mind caught up to the fact that no blade would help against "
        "whatever had just moved somewhere she could not see or reach."
    )},
    {"type": "body", "text": (
        "\"Something has moved,\" she said aloud, to no one, testing "
        "the shape of the thought against the empty hollow around her. "
        "\"Something old has moved, and I was not the one who moved "
        "it.\" She thought, again, of the search party she had watched "
        "leave Idoro and dismissed, of the silence from her teacher that "
        "had stretched longer than any silence before it, of a story "
        "that stopped cold at the word resettled and had never, not "
        "once in fifteen years of training, been allowed to continue "
        "past it."
    )},
    {"type": "body", "text": (
        "The hollow around her had gone fully dark by then, the fire "
        "long since burned to coals, and Mfoniso found herself listening "
        "to the ordinary night sounds of insects and settling branches "
        "the way she had once, as a much younger woman, listened for "
        "danger in every quiet place she camped. It had been a long time "
        "since an ordinary night had made her feel this unpracticed at "
        "her own trade."
    )},
    {"type": "body", "text": (
        "She did not sleep again that night, not truly, lying instead "
        "with one hand pressed flat against her own chest the way a "
        "person checks a wound they cannot see to know how badly it is "
        "still bleeding. By the time the sky began to gray toward "
        "morning, she had made a decision she did not examine too "
        "closely, the same way she had not examined, on the ridge above "
        "Idoro, why professional caution had started to feel like "
        "something else entirely."
    )},
    {"type": "body", "text": (
        "She would answer the Warden's question honestly, whatever the "
        "answer turned out to be. But she would not decide it, not "
        "fully, not until she had asked the Warden one question of her "
        "own first, a question she had never once in her career thought "
        "she would need to ask the woman who signed her wages. What, "
        "exactly, had become of the people her own lineage had once "
        "resettled, and did the House still keep any record of where."
    )},
    {"type": "body", "text": (
        "She broke camp before full light and walked on south, faster "
        "now than the road strictly required, carrying a question "
        "inside a question the way she had once, without knowing it, "
        "carried an unfinished story inside a finished one, and told "
        "herself, with less conviction than she would have liked, that "
        "she was only being thorough."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
