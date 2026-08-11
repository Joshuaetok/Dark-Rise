#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 117: "A Knot Her Mother Taught Her"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Ijeoma completes her map of
the compound's full guard rotation, old gap and new, and finally acts on
a plan that has nothing to do with the wall itself: hiding a small,
distinctive trade knot inside an outgoing cloth bundle, a signal only
someone from her own home market would ever recognize as meaning
something. The Factor's dock inspection nearly catches her hand in the
act, the closest near miss yet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 117
EPISODE_TITLE = "A Knot Her Mother Taught Her"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Seventeen"},
    {"type": "title_ep_name", "text": "A Knot Her Mother Taught Her"},
    {"type": "page_break", "text": ""},

    {"type": "body", "text": (
        "It took Ijeoma eleven more days to finish what she privately "
        "thought of as her map, though nothing about it existed on "
        "paper, every gate and gap and rotation held instead in the "
        "same patient, wordless place where she had once kept every "
        "thread count her mother ever taught her. The eastern gate's "
        "old habitual absence. The newer, second gap the schedule "
        "change had quietly added to it, still unexplained but "
        "reliable as sunrise across every morning she had watched it "
        "since. A shorter, thinner gap at the dock during the "
        "midday cargo count, when the two guards assigned to watch the "
        "loading crews traded places without ever quite watching the "
        "handoff itself."
    )},
    {"type": "body", "text": (
        "She built the map slowly and out loud only inside her own "
        "head, the way she had once built a whole cloth trader's "
        "ledger from memory alone during a season her mother's eyes "
        "had gone too weak to trust with ink. A morning here, marking "
        "which guard yawned through the last quarter of his watch. An "
        "evening there, noting which post grew careless the moment "
        "supper's smell reached it from the kitchens. She trusted "
        "nothing until she had watched it repeat at least three times, "
        "and trusted it fully only once it had repeated five."
    )},
    {"type": "body", "text": (
        "Knowing the gaps had never once, by itself, been the same "
        "thing as knowing what to do with them. The wall had already "
        "taught her that lesson at real cost, a lesson written now in "
        "the memory of black water she still could not read and would "
        "not risk blind a second time. What she needed was not another "
        "way over a wall she already knew could not be trusted. What "
        "she needed was a way to be found by someone who was not "
        "already trapped inside this compound with her."
    )},
    {"type": "body", "text": (
        "The idea arrived, when it finally arrived, from the most "
        "ordinary place imaginable, the dock's weekly cargo count, "
        "where House goods bound for genuine river markets were bundled "
        "and tied by House hands under a watch too thin and too bored "
        "to look closely at any single bundle twice."
    )},
    {"type": "body", "text": (
        "Her mother had taught her, long before any of this, a small "
        "private trade signature every serious cloth family along their "
        "stretch of river kept and guarded the way a name is guarded, a "
        "particular double knot tied into the corner selvedge of any "
        "bolt worth standing behind, invisible to a careless buyer and "
        "instantly readable to any trader who had ever done honest "
        "business with that family before. It meant, to the right "
        "eyes, this cloth was handled by someone who knows exactly what "
        "she is doing. It could mean, tied where it had no honest "
        "reason to exist, something else entirely to the one particular "
        "kind of stranger who might ever recognize it."
    )},
    {"type": "body", "text": (
        "She requested dock duty for the first time in two seasons, "
        "framing it to the housemistress as simple restlessness, a "
        "guest grown tired of laundry alone and looking for lighter "
        "variety in her days. The request was granted without much "
        "thought, exactly as she had counted on it being, one more "
        "small unremarkable favor extended to a guest no one had ever "
        "quite decided was worth watching closely."
    )},

    {"type": "body", "text": (
        "Her first two days at the dock were spent doing nothing more "
        "dangerous than actual work, hauling and stacking and counting "
        "alongside House hands who barely looked at her twice, a "
        "guest's presence among them explained away by the "
        "housemistress in a single indifferent sentence that seemed to "
        "satisfy everyone's curiosity completely. One older dockhand, "
        "missing two fingers on his left hand from some accident he "
        "never explained, showed her without being asked how to fold a "
        "bolt properly for river transport, and Ijeoma let him teach "
        "her, grateful for a task that gave her hands something honest "
        "to do while her eyes did the real work of learning the whole "
        "loading rhythm by heart."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "She found her moment on the third day of dock duty, a bundle "
        "of finished cloth already counted and half wrapped, the two "
        "watching guards mid handoff at exactly the thin, unwatched "
        "instant her weeks of counting had promised her. Her hands "
        "moved before she let herself think too hard about moving them, "
        "the double knot tied fast into a corner fold where a careless "
        "eye would read it as nothing more than a trader's ordinary "
        "habit."
    )},
    {"type": "body", "text": (
        "She was still smoothing the bundle's outer wrap flat, her "
        "pulse loud enough in her own ears to nearly drown the dock's "
        "ordinary noise, when the Factor arrived to conduct his own "
        "weekly inspection of the cargo ledger."
    )},
    {"type": "body", "text": (
        "He had never once, in two seasons, paid the dock's cargo count "
        "any real attention beyond the numbers themselves, but today, "
        "for reasons Ijeoma could not have guessed and would not have "
        "believed if she had, he stopped directly beside the very "
        "bundle her hands had only just left, lifting its corner to "
        "check the count against his own ledger the way any careful "
        "overseer might."
    )},
    {"type": "body", "text": (
        "His thumb passed directly over the knot."
    )},
    {"type": "body", "text": (
        "Every careful lesson her mother had ever given her about "
        "keeping a trader's face still under pressure, the one that "
        "gave nothing away to a buyer trying to guess how badly she "
        "wanted a sale, rose up in her all at once, and she found "
        "herself grateful, in the strange sideways way fear sometimes "
        "made a person grateful for the smallest things, that two "
        "seasons of practiced blankness had given her a face this "
        "House had long since stopped bothering to read closely."
    )},
    {"type": "body", "text": (
        "Ijeoma did not move. Did not breathe, or thought afterward she "
        "had not, though her own body must have kept doing both without "
        "her permission the way a body always did. She watched the "
        "Factor's face for any flicker of recognition, any small "
        "tightening that would tell her the knot had been seen for what "
        "it actually was rather than what it pretended to be, and found "
        "nothing there she could read with any certainty at all."
    )},
    {"type": "body", "text": (
        "\"Count is correct,\" the Factor said at last, to no one in "
        "particular, setting the bundle back down exactly as he had "
        "found it and moving on to the next without a backward glance. "
        "His voice carried nothing but the flat, bored competence of a "
        "man doing a duty he had done a thousand times before and "
        "expected to do a thousand times again."
    )},
    {"type": "body", "text": (
        "Ijeoma finished her own work in a fog she did not fully "
        "surface from until the whole shipment had been loaded and the "
        "boat carrying it was already pulling away from the dock into "
        "the river's slow brown current, her one small, unrepeatable "
        "chance now traveling somewhere she could no longer see, toward "
        "eyes she could not choose and a fate she could not control."
    )},

    {"type": "scene_break", "text": ""},

    {"type": "body", "text": (
        "The Factor, for his own part, walked the rest of his "
        "inspection with the same flat competence he had shown at the "
        "bundle, and did not let himself think about the knot again "
        "until he was alone in his own quarters that evening, turning "
        "the memory of it over with the particular unease of a man who "
        "had spent a lifetime reading cloth for a living and knew "
        "exactly what an unnecessary double knot in a corner selvedge "
        "usually meant."
    )},
    {"type": "body", "text": (
        "He had seen it. He had understood, in the half second his "
        "thumb rested over it, precisely what it was and precisely "
        "whose careful hands must have tied it, and he had said, aloud, "
        "in front of two watching guards, that the count was correct, "
        "and moved on."
    )},
    {"type": "body", "text": (
        "It was the closest he had come yet to being caught in the act "
        "of his own quiet treason, and the strangest part, sitting with "
        "it now in the private dark of his own room, was how little "
        "afraid the moment had actually made him feel. He had expected, "
        "if he ever came this close to discovery, some sharp jolt of "
        "self preservation warning him back from the edge. Instead he "
        "had felt something closer to relief, the relief of a man "
        "finally doing, in some small unauthorized way, the one thing "
        "his own conscience had been demanding of him since he first "
        "truly saw her standing at that wall."
    )},
    {"type": "body", "text": (
        "Ijeoma, alone in her own small room that same night, sat for a "
        "long while with her back against the wall she had once failed "
        "to clear, turning the whole day over the way she turned "
        "everything over now before allowing herself to trust it. She "
        "did not know, and had no way of finding out, whether the "
        "Factor's flat, bored sentence had been genuine or performed. "
        "She knew only that the boat was gone, the knot traveling with "
        "it, and that she had done the one thing two seasons of patient "
        "counting had never quite let her attempt before tonight, "
        "reached, however faintly and however unlikely to ever be "
        "answered, beyond this compound's own walls toward a world that "
        "still did not know to look for her."
    )},
    {"type": "body", "text": (
        "He did not know where the boat was bound, or which of its "
        "several stops downriver might someday put that bundle into "
        "hands that understood what its knot actually said. He found, "
        "turning the uncertainty over one last time before sleep "
        "finally took him, that he did not need to know. He had done "
        "what a person in his position could do. What happened to that "
        "small, single knot now belonged to the river, and to whatever "
        "stranger's hands eventually untied it."
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
