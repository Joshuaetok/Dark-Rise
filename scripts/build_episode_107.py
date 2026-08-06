#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 107: "The Question She Will Not Answer by Courier"
Uses the shared scripts/dr_build.py module.

Written 2026-08-06 (scheduled release TBD): Act 1 closes. Osadebe's
written report reaches Idoro by fast courier, and the household weighs
pursuing the new lead against the risk of thinning an already stretched
garrison further. Downriver, the Warden's ciphered question finally
reaches Mfoniso, and rather than answer it by return courier, she
decides to carry her answer to the Warden in person, mirroring her
Episode 92-93 journey.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 107
EPISODE_TITLE = "The Question She Will Not Answer by Courier"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Seven"},
    {"type": "title_ep_name", "text": "The Question She Will Not Answer by Courier"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: IDORO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The courier reached Idoro at midday, dust to the knee and "
        "half asleep in the saddle, carrying a sealed report that "
        "Osadebe had trusted to no one but a rider sworn directly to "
        "Chidebe. Amara broke the seal herself in the council room, "
        "reading it once in silence before reading it again aloud, her "
        "voice steady only because she had learned, over a great many "
        "hard mornings, how to make it so."
    )},
    {"type": "body", "text": (
        "She told them all of it. The buried wall. The bowls left in "
        "place. The hillside chamber with its restraints and its "
        "still oiled hinge. The branded mark that matched, beyond any "
        "argument, the seal on every message that had ever been left "
        "for Emenike at the drop stone. When she finished, the room "
        "held a silence heavier than any it had held since the night "
        "Chidebe first walked Emenike back to the compound under "
        "suspicion."
    )},
    {"type": "body", "text": (
        "Elder Maka was the first to speak. \"Three centuries,\" she "
        "said, quiet, as if testing the weight of the number against "
        "everything she thought she had understood about Oso's grief. "
        "\"We built our whole understanding of that ground around one "
        "old law and one dibia's death. We never once asked whether "
        "the hand behind it was still working.\" Ozoemena answered her, "
        "his voice rough with the particular anger of a man who serves "
        "through labor because his own worst mistake still shapes every "
        "judgment he makes now. \"It is working,\" he said. \"It has "
        "never stopped. We simply never had a name to put to it until "
        "our own son found it wearing someone else's brand.\""
    )},
    {"type": "body", "text": (
        "Chidebe laid Osadebe's sketched map flat on the council table, "
        "the bearing marked in careful ink continuing west past the "
        "settlement toward country none of them had ever needed a name "
        "for before. \"He does not ask for reinforcement,\" Chidebe "
        "said. \"He asks only that we understand what he is walking "
        "toward, in case the report he sends next does not come from "
        "his own hand.\" The sentence sat in the room like a held "
        "breath. No one moved to fill the silence that followed it."
    )},
    {"type": "body", "text": (
        "\"Then we send what he did not ask for anyway,\" Amara said, "
        "and something in her tone left no space for argument. \"Word "
        "to Udo, today, not the slower channel Osadebe used for his own "
        "report but the fastest rider Chidebe can spare. If the crown "
        "already believes a House sponsored the coercion against "
        "Emenike, they deserve to know that House's hand reaches back "
        "three hundred years and forward into a hillside our own son is "
        "standing beside tonight.\""
    )},
    {"type": "body", "text": (
        "Obi, who had said little, finally spoke from where he sat "
        "beside her. \"And if Udo decides the answer is more soldiers "
        "on that bearing,\" he said, \"who guards Idoro while they "
        "march. We are already thinner than we were before the "
        "survey's garrison doubled and Osadebe's four men walked west "
        "with half of what we could spare.\" It was the practical fear "
        "underneath the larger one, and no less real for being smaller. "
        "Chidebe answered it plainly, the way a soldier answers a "
        "soldier's question. \"That is the crown's decision to weigh, "
        "not ours,\" he said. \"Ours is only to make certain they weigh "
        "it with every fact we have, not half of them.\""
    )},
    {"type": "body", "text": (
        "Zara, who had listened from the doorway with her arms crossed "
        "tight against her own chest, asked the question that had been "
        "sitting under everyone else's since Amara first read the "
        "report aloud. \"Does this change what Elder Maka can ask of "
        "Oso,\" she said. \"If the presence's own history is tangled up "
        "in whoever holds Ijeoma now, does it know more than it has "
        "told us. Or is it only now learning as much as we are.\" Elder "
        "Maka considered the question longer than she usually allowed "
        "herself to before answering. \"I will ask it tonight,\" she "
        "said. \"Gently. It has already given more of its own grief "
        "this week than in three centuries before it. I will not spend "
        "that generosity carelessly, even for a question this "
        "important.\""
    )},
    {"type": "body", "text": (
        "Adaugo, who had sat through the reading with her hands folded "
        "tight in her lap, spoke last, her voice smaller than her "
        "usual council presence but no less certain for it. \"When "
        "Mfoniso held me,\" she said, \"I understood for the length of "
        "one breath what it was to belong to someone else's ledger. If "
        "this House has been doing that to whole villages for three "
        "hundred years, then Ijeoma is not the only debt owed here. We "
        "are, in a sense none of us have said aloud yet, fighting on "
        "behalf of every name that hillside room ever held.\" No one "
        "argued the point. It was, Amara thought, exactly the kind of "
        "clarity her daughter had earned the hard way and should not "
        "have had to."
    )},
    {"type": "body", "text": (
        "Elder Maka rose to leave for the shrine as the council broke, "
        "then paused at the doorway and looked back at all of them, "
        "gathered around a map that had, in the space of one letter, "
        "grown far larger than the search it was drawn for. \"We should "
        "tell Osadebe's family what he has walked into, in case word "
        "must travel further before this ends,\" she said, quiet. \"Not "
        "to frighten them. Only so that no one in Idoro learns the "
        "shape of this danger secondhand, the way we very nearly "
        "learned Emenike's.\" Chidebe agreed without argument, already "
        "reaching for his own writing materials before she had finished "
        "speaking."
    )},
    {"type": "body", "text": (
        "The council broke without a full resolution, because the "
        "truth none of them said aloud was that no single meeting could "
        "resolve what the courier had actually brought them. Not a "
        "problem to be solved by dawn, but the sudden, vertiginous "
        "knowledge that the danger they had been fighting piece by "
        "piece for a hundred episodes of grief was, and had perhaps "
        "always been, a single old hand with a single old mark, patient "
        "enough to wait three centuries between one atrocity and the "
        "next."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: MFONISO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "The message reached Mfoniso on her western ridge two hours "
        "before dusk, carried by a runner she recognized by gait before "
        "she recognized his face, one of the House's oldest and most "
        "trusted lines. He said nothing beyond the courtesy required, "
        "handed her the small sealed packet, and withdrew to wait at a "
        "respectful distance while she read it, the way he always did "
        "when a message came from the Warden's own hand rather than a "
        "clerk's."
    )},
    {"type": "body", "text": (
        "She broke the seal and worked the cipher the way she had "
        "worked a hundred ciphers before it, letter folding into letter "
        "until the Warden's question sat plain in front of her, written "
        "in a hand too controlled to be anything but deliberate. Does "
        "the hunt still require the guest kept breathing, or may the "
        "House close the account."
    )},
    {"type": "body", "text": (
        "She read it twice. She had expected, if anything came at all, "
        "another order, another target, another problem shaped like all "
        "the problems she had solved for the House across a long "
        "career of solving exactly this kind of problem. She had not "
        "expected to be asked. Orders did not usually leave room for a "
        "hunter's own judgment. This one, worded exactly as it was, "
        "left nothing but room."
    )},
    {"type": "body", "text": (
        "She sat with the packet a long while, watching the last light "
        "fail over Idoro's rooftops below her, and found herself "
        "circling back, against her own discipline, to the thought she "
        "had put away days earlier on this same ridge. Her teacher's "
        "unexplained silence. The old story of the ground her lineage "
        "had once taken, told to her as triumph and lately sitting "
        "wrong in her chest however she turned it. A question about a "
        "woman's life, arriving from the same House, on the same day "
        "she had finally admitted to herself how little she trusted her "
        "own certainty about any of it."
    )},
    {"type": "body", "text": (
        "She thought, too, of the fresh spiral cut into a stone she had "
        "never seen and did not yet know existed, and of a search party "
        "she had once watched leave Idoro and dismissed as routine, and "
        "felt, without being able to name the source of the feeling, "
        "that the ground under her whole career had shifted somewhere "
        "she had not been watching closely enough to catch it moving."
    )},
    {"type": "body", "text": (
        "A courier's return message would take a season's worth of risk "
        "and compress it into a single sealed line, decided at a "
        "distance, by a woman who had never once stood in the same room "
        "as the girl whose life the line concerned. Mfoniso had written "
        "such lines before. She had never once, until this exact "
        "evening, felt the weight of what it meant to write one without "
        "looking the question in the face first."
    )},
    {"type": "body", "text": (
        "\"I will carry my own answer,\" she told the runner when she "
        "finally called him back, her voice even, giving away nothing "
        "of the hour she had just spent deciding it. \"Tell the Warden "
        "to expect me, not a reply.\" The runner did not ask why, "
        "because runners who asked why did not stay runners for the "
        "House long. He only nodded and turned back the way he had "
        "come, leaving Mfoniso alone on the ridge with a question she "
        "had chosen, for reasons she was not yet ready to examine too "
        "closely, not to answer from a distance."
    )},
    {"type": "body", "text": (
        "She broke her own vigil over Idoro that same evening, packing "
        "with the same economy she brought to everything, and did not "
        "look back at the village's lit rooftops as she turned south "
        "toward the river road. She told herself the decision was "
        "professional, that a question this weighted deserved to be "
        "answered by someone who had actually stood in the guarded "
        "courtyard and seen the girl's face rather than by ink alone. "
        "She did not examine, closely enough to notice the shape of it, "
        "why professional caution had started, these last days, to feel "
        "so much like something else entirely."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
