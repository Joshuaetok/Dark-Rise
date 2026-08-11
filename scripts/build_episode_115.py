#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 115: "A Fragment of What Was Lost"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Days after the search party
disturbed the presence's lost ground and learned its people were taken
rather than killed, a fragment of the presence's own old strength finally
finds its way home through Chibundu, unbidden and unasked for. The gain
is real. So is the grief that floods the bond delivering it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 115
EPISODE_TITLE = "A Fragment of What Was Lost"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Fifteen"},
    {"type": "title_ep_name", "text": "A Fragment of What Was Lost"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "It found him in the middle of an ordinary task, mending a "
        "torn strap on his own sandal by the fire's low light, which "
        "was, Chibundu would think much later, exactly the kind of "
        "small unguarded moment old power seemed to prefer for arriving "
        "unannounced."
    )},
    {"type": "body", "text": (
        "It began as sound before it became anything else, a woman's "
        "voice singing low over something that was not quite a lullaby "
        "and not quite a work song, in a language Chibundu had never "
        "heard spoken and somehow understood completely anyway, every "
        "word arriving already translated into feeling before his mind "
        "had any chance to translate it into meaning."
    )},
    {"type": "body", "text": (
        "Then came firelight that was not his own fire, warm and "
        "orange and full of moving shadows cast by people whose faces "
        "he could almost, almost see. A child laughing somewhere close "
        "by. The particular smell of a specific evening meal cooking "
        "over specific coals, three hundred years gone and somehow "
        "still, impossibly, present enough to fill his whole chest with "
        "hunger for a meal he had never once eaten."
    )},
    {"type": "body", "text": (
        "A name arrived after the smell of the meal, unbidden, carried "
        "on the same current as everything else, a woman's name spoken "
        "in the presence's own voice, though Chibundu understood "
        "instantly it had not meant to speak it aloud at all. The name "
        "meant nothing to him. He felt, all the same, exactly what it "
        "meant to the presence, a weight so total and so specific that "
        "his own chest ached with a grief three hundred years older "
        "than his own body had any right to carry."
    )},
    {"type": "body", "text": (
        "He saw her only for a moment, a woman standing at the edge of "
        "the firelight with a child balanced on one hip, her face "
        "turned half away toward something beyond the memory's own "
        "borders, gone again before Chibundu could hold the image "
        "steady enough to keep it. He understood, without being told, "
        "that this was the specific loss the presence had spent three "
        "centuries not letting itself remember clearly, and that some "
        "part of it had just handed that exact memory to him anyway, "
        "helplessly, the way a person in the middle of drowning grabs "
        "whatever hand happens to be nearest."
    )},
    {"type": "body", "text": (
        "\"Stop,\" Chibundu managed, though he could not have said "
        "afterward whether he spoke the word aloud or only inside the "
        "place where the presence usually spoke to him. \"Whatever this "
        "is. It is too much. Stop.\""
    )},
    {"type": "body", "text": (
        "It did not stop, not because it was cruel but because, he "
        "understood even through the flood of it, it could not. This "
        "was not the presence choosing to show him something. This was "
        "something finally arriving on its own, after three centuries "
        "of being unable to reach the place it had always belonged, and "
        "arrival, once begun, was not a thing that could simply be "
        "paused politely partway through."
    )},

    {"type": "body", "text": (
        "He came back to himself on the ground, cheek pressed against "
        "packed earth still warm from the day's sun, his whole body "
        "shaking in a way that had nothing to do with cold."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "\"You are grieving something that is not your own grief,\" the "
        "entity said, close beside him though he had not heard it "
        "arrive, its usual dry, transactional tone softened into "
        "something almost gentle. \"That is the presence's memory "
        "passing through you rather than yours. It will pass. Breathe "
        "until it does.\""
    )},
    {"type": "body", "text": (
        "\"What happened,\" Chibundu asked, once breathing had become a "
        "reliable thing again rather than a labor. \"That was not a "
        "dream. That was not a vision either. That felt like something "
        "arriving, not something shown to me.\""
    )},
    {"type": "body", "text": (
        "The presence answered slowly, its own voice carrying a "
        "roughness Chibundu had never once heard in it before, the "
        "sound, he thought, of something speaking through an emotion it "
        "had not fully finished feeling yet. \"A fragment of what was "
        "taken from me has found its way home,\" it said. \"Not "
        "memory alone. Strength. A small true piece of what I was "
        "before that ground was emptied, returning now because the "
        "grief holding it away has finally learned its own correct "
        "shape.\""
    )},
    {"type": "body", "text": (
        "\"I do not understand,\" Chibundu said, though some part of "
        "him, still raw from the flood of borrowed grief, thought "
        "perhaps he understood more than he wanted to admit."
    )},
    {"type": "body", "text": (
        "\"For three centuries I mourned a slaughter,\" the presence "
        "said. \"A clean, final, comprehensible loss, terrible but "
        "finished. That grief closed around itself the way any finished "
        "grief eventually does, and closed, it seems, around a piece of "
        "my own strength along with it, sealing that piece away inside "
        "a story that was never actually true. Your search party broke "
        "the seal without meaning to, simply by proving the story "
        "wrong. What I mourn now is open, unfinished, alive with a "
        "question rather than closed around an answer. And what was "
        "sealed inside the old, false grief has apparently found, for "
        "the first time in three hundred years, a door left standing "
        "open long enough to walk back through.\""
    )},
    {"type": "body", "text": (
        "\"You said a name,\" Chibundu said quietly, once his own "
        "breathing had steadied enough to trust his voice with it. \"I "
        "do not know whose it was. I do not think you meant to say it "
        "where I could hear it.\""
    )},
    {"type": "body", "text": (
        "The presence did not answer that directly, and Chibundu, for "
        "once, did not press it, understanding without needing to be "
        "told that some doors, even opened accidentally, deserved to be "
        "closed again gently rather than pushed all the way through on "
        "the same night they first cracked open."
    )},
    {"type": "body", "text": (
        "\"Thank you,\" the presence said instead, after a long silence, "
        "\"for not asking me to explain it further tonight. There will "
        "be a night I can tell you who she was. This is not that "
        "night.\""
    )},
    {"type": "body", "text": (
        "The entity, listening with the same careful attention it gave "
        "to everything that might matter, asked the question Chibundu "
        "himself had not yet found the steadiness to ask. \"What did it "
        "cost you to receive it.\""
    )},
    {"type": "body", "text": (
        "\"Everything the boy just felt,\" the presence said, \"and I "
        "felt it with him, doubled, the way a grief is always doubled "
        "for the one who first owned it. I will not pretend that cost "
        "was small. But I have carried worse costs for smaller gains "
        "across three centuries of careful restraint, and I would carry "
        "this one again without hesitation, gladly, if it were offered "
        "to me a second time.\""
    )},
    {"type": "body", "text": (
        "It tested the fragment carefully afterward, the way a person "
        "tests a limb long unused for fear of trusting it too quickly, "
        "reaching outward through Chibundu toward the edges of Oso's own "
        "boundary and, for the first time since the night it tore "
        "itself loose from Zara to save Kene, past them, a small true "
        "distance further than it had ever managed to reach since."
    )},
    {"type": "body", "text": (
        "It was not far. A stone's throw beyond the old boundary line, "
        "no more, a reach so modest that a stranger measuring it would "
        "have called it nothing worth mentioning at all. To a power "
        "that had spent three hundred years unable to cross its own "
        "border by so much as a single extra pace, it was the first "
        "real proof, since the search party ever left Idoro, that the "
        "grief now finally shaped correctly might one day let it walk "
        "further than grief alone had ever allowed."
    )},
    {"type": "body", "text": (
        "\"Will there be more,\" Chibundu asked, still sitting where he "
        "had fallen, too shaken yet to trust his own legs to carry him "
        "back inside. \"More fragments. More of this.\""
    )},
    {"type": "body", "text": (
        "The presence was quiet for a long moment before it answered, "
        "and when it finally did, its voice had gone careful again, the "
        "old, patient caution Chibundu had learned to recognize as the "
        "shape it wore whenever it was about to tell him something true "
        "rather than something comfortable."
    )},
    {"type": "body", "text": (
        "\"I do not know,\" it said. \"That was only a fragment, small "
        "enough for one grieving night to carry. I do not yet know what "
        "receiving the whole would actually cost either of us, and I "
        "confess to you honestly that some part of me, after tonight, "
        "has already begun wondering whether I would pay it anyway, "
        "whatever the price turned out to be.\""
    )},
    {"type": "body", "text": (
        "Chibundu sat with that answer a long while after both old "
        "powers had gone quiet, turning it over the way he had learned "
        "to turn over anything either of them gave him that arrived "
        "sounding more like a warning than a comfort. He understood, "
        "sitting alone in the dark with the fire finally burned down to "
        "embers, that he had just watched something he loved grow "
        "stronger by walking straight through the worst pain it had "
        "carried in three hundred years, and that it had called the "
        "trade worthwhile without a moment's hesitation."
    )},
    {"type": "body", "text": (
        "He thought, before sleep finally found him, of the woman at "
        "the edge of the firelight, her face turned half away, gone "
        "before he could hold her steady in his own mind. He did not "
        "know her name, not truly, only the single unguarded syllable "
        "of it the presence had let slip in the middle of its own "
        "drowning. He found, turning it over one last time in the dark, "
        "that he wanted very badly to know the rest of her, and "
        "understood, with a clarity that felt older than his own years, "
        "that wanting it was exactly the kind of wanting that had "
        "already cost the presence beneath Oso more than it had ever "
        "once complained about paying."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
