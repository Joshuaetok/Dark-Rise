#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 120: "A Name From a Stranger's Mouth"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): The search party intercepts
two couriers on a supply trail leading from the compound, gaining the
first hard confirmation that a young woman prisoner, closely watched in
the inner courtyard, matches Ijeoma exactly. The interception is not
clean: the second courier breaks free wounded and flees back toward the
compound, leaving a trace the party cannot undo.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 120
EPISODE_TITLE = "A Name From a Stranger's Mouth"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty"},
    {"type": "title_ep_name", "text": "A Name From a Stranger's Mouth"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "Four days of patient watching had taught the search party the "
        "compound's outer rhythm well enough to set a clock by it, and "
        "it was that same patient watching that finally showed them "
        "the trail, a narrow supply path running north from the "
        "compound's rear gate to a smaller landing further up the "
        "river, walked twice a week by no more than two men carrying "
        "goods too modest to need a larger escort."
    )},
    {"type": "body", "text": (
        "\"Two men, unwatched by the main garrison the moment they "
        "clear the tree line,\" Ifeanyi said, having tracked the "
        "pattern for three full trips before he trusted it enough to "
        "report it. \"If we are ever going to learn something more "
        "useful than a wall's own outline, this is the closest thing to "
        "an open door this House has shown us yet.\""
    )},
    {"type": "body", "text": (
        "Osadebe weighed the risk with the same careful arithmetic he "
        "had weighed every decision since the ridge, and found, this "
        "time, that the arithmetic finally tipped toward action. "
        "\"Weeks of watching a wall have told us it is guarded,\" he "
        "said. \"They have told us nothing about who is actually behind "
        "it. I would rather risk this trail once, carefully, than "
        "watch that wall for another month learning nothing more than "
        "its own shadow.\""
    )},

    {"type": "body", "text": (
        "Emenike had said little during the days of pure watching, "
        "content, or appearing content, to let Osadebe's careful "
        "patience set the pace the way it had set every pace since "
        "Idoro. But Ifeanyi's report changed something in him visibly, "
        "a stillness settling over him that the other three had learned "
        "by now to read as the particular quiet of a man holding "
        "himself on a very short leash rather than the quiet of a man "
        "at ease."
    )},
    {"type": "body", "text": (
        "\"I will not ask to lead it,\" Emenike said that same evening, "
        "before Osadebe had finished laying out the plan in full. \"I "
        "know my own judgment is not the steadiest thing in this camp "
        "where she is concerned. I am only asking to be there when "
        "whatever we learn is finally said aloud.\" Osadebe granted it "
        "without argument, understanding, better than most captains "
        "would have, exactly what two seasons of waiting had cost the "
        "man asking."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They took the trail two mornings later, well back from the "
        "compound's own tree line, Emenike and Okonjo positioned to "
        "close the path behind the couriers while Osadebe and Ifeanyi "
        "waited ahead where the trail narrowed between two close set "
        "boulders, ground chosen precisely because it left a man no "
        "room to run in any direction but forward, into waiting hands."
    )},
    {"type": "body", "text": (
        "The waiting itself was the hardest part, each man alone with "
        "his own particular version of the same fear, that the pattern "
        "which had held true for three careful trips would choose this "
        "one morning to break for reasons no amount of patient watching "
        "could have predicted. The forest around them held its ordinary "
        "morning sounds, birds, insects, the far off murmur of the "
        "river, and gave away nothing at all about what was coming up "
        "the trail toward them."
    )},
    {"type": "body", "text": (
        "The two couriers came exactly on schedule, unhurried, "
        "talking quietly between themselves about nothing more "
        "dangerous than the coming rains, and were three steps into the "
        "narrow ground before either of them understood the trail had "
        "already closed around them."
    )},
    {"type": "body", "text": (
        "The first went down fast and quiet, Osadebe's forearm across "
        "his throat before he had finished drawing the breath to shout, "
        "wrestled to the ground and bound before his own surprise had "
        "fully cleared from his face."
    )},
    {"type": "body", "text": (
        "The second broke the wrong way, twisting free of Ifeanyi's "
        "first grab and driving hard for the tree line rather than "
        "toward the boulders, a small belt knife already flashing in "
        "his free hand. Ifeanyi caught him a heartbeat later, the knife "
        "opening a shallow line across his own forearm before he "
        "finally wrestled the man's wrist still, and it was in that same "
        "brief, ugly struggle that the courier tore loose again, "
        "bleeding freely from a cut of his own now, and ran."
    )},
    {"type": "body", "text": (
        "Osadebe made the call before any of the others could finish "
        "forming the question themselves. \"Let him go,\" he said, flat "
        "and immediate, watching the fleeing man vanish back toward the "
        "compound's tree line with a wound that would slow him but not "
        "stop him. \"Chasing him costs us the one we already hold, and "
        "costs us any chance this stays quiet a moment longer than it "
        "already has.\""
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They questioned the one they kept a full ridge away from the "
        "trail, in a hollow chosen for how completely it swallowed "
        "sound, the man bound, gagged only until questioning actually "
        "began, and visibly certain he was about to die."
    )},
    {"type": "body", "text": (
        "\"We are not going to kill you,\" Osadebe told him, plainly, "
        "the same flat honesty he had used on frightened men before, "
        "\"provided you answer honestly and quickly. I am looking for a "
        "young woman, held inside that compound against her will, taken "
        "from a river town two seasons past. Tell me she is there, and "
        "tell me where, and this ends for you with nothing worse than a "
        "very long, very cold walk home once we are finished.\""
    )},
    {"type": "body", "text": (
        "The courier, a hired hand rather than a trained House man by "
        "every visible sign of him, talked fast and readily once the "
        "gag came free, the words tumbling over each other in his "
        "hurry to be believed. \"There is a guest,\" he said. \"That is "
        "the only word any of us are ever told to use for her. Held in "
        "the inner courtyard, past the second wall, watched closer than "
        "anyone else kept on this whole property. Young. Quiet. I have "
        "seen her twice from a distance carrying laundry, never once up "
        "close.\""
    )},
    {"type": "body", "text": (
        "\"Does she have a name,\" Emenike asked, his voice tight "
        "enough that Osadebe glanced at him once, a silent instruction "
        "to hold steady rather than let two seasons of waiting spill "
        "out sideways into the interrogation and ruin it."
    )},
    {"type": "body", "text": (
        "\"I have heard one of the housemistress's girls say it once,\" "
        "the courier admitted. \"Ijeoma. I do not know if it is true. I "
        "only know it is the name that is said quietly, when the guards "
        "who watch her think no one else is listening.\""
    )},
    {"type": "body", "text": (
        "Emenike did not speak again for a long moment afterward, and "
        "when he finally did, his voice had gone rough in a way none of "
        "the other three had heard from him since the night at the "
        "ravine. \"That is her,\" he said. \"That is my sister's name.\""
    )},
    {"type": "body", "text": (
        "He knelt then, closer to the bound man than Osadebe would "
        "ordinarily have allowed, and asked the one question none of "
        "the interrogation's careful planning had accounted for. \"Is "
        "she well. Not held, not watched, not any of the words your "
        "House uses for a person it owns. Is she actually well.\""
    )},
    {"type": "body", "text": (
        "The courier, frightened enough to be honest even where honesty "
        "cost him nothing further to give, answered as carefully as his "
        "own limited knowledge allowed. \"She walks steady. She works "
        "the laundry line without complaint anyone has ever reported. I "
        "cannot tell you what sits behind a stranger's eyes from two "
        "seasons of distant glances, only that nothing about how she "
        "carries herself looks broken to me.\" It was not everything "
        "Emenike had hoped to hear. It was, visibly, more than he had "
        "allowed himself to expect."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "They bound the courier securely to a tree well off the trail "
        "rather than kill him or free him, gagged again and left with "
        "water within reach of a working chin, a decision Osadebe made "
        "and did not ask anyone else to vote on. It bought them time. It "
        "did not buy them safety."
    )},
    {"type": "body", "text": (
        "\"The second man is already back inside that wall,\" Ifeanyi "
        "said, binding his own shallow wound with the same rough "
        "competence he had used on Okonjo's ankle, once the party had "
        "put real distance between themselves and the trail. \"Wounded, "
        "frightened, and missing his partner. However this House reads "
        "that story, it will not read it as an accident.\""
    )},
    {"type": "body", "text": (
        "\"No,\" Osadebe agreed, already moving them toward a new "
        "hidden position further from the ridge than their old one, the "
        "grim calculation of a captain recalculating everything he had "
        "assumed safe only that morning. \"We have our confirmation. We "
        "no longer have the luxury of being invisible while we decide "
        "what to do with it. From here, every hour we spend watching "
        "that wall is an hour that wall may already be watching back.\""
    )},
    {"type": "body", "text": (
        "Okonjo, still favoring the ankle that had never fully "
        "recovered its old confidence, asked the question the whole "
        "party had been quietly circling since the wounded courier "
        "vanished into the tree line. \"How long do you think we "
        "actually have.\""
    )},
    {"type": "body", "text": (
        "\"Less than we had this morning,\" Osadebe said, honest rather "
        "than comforting, the same honesty he had offered the bound "
        "courier not an hour earlier. \"A day, if this House is slow to "
        "believe its own frightened man. Half that, if it is not. We "
        "move now, and we move as though whatever time we still have is "
        "already spending itself whether we use it well or not.\""
    )},
    {"type": "body", "text": (
        "Emenike walked the last stretch to their new camp in silence, "
        "carrying the courier's few honest words about his sister the "
        "way a person carries something too fragile to hold with both "
        "hands at once, grateful for them and terrified, in equal "
        "measure, of everything they had not been able to promise him."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
