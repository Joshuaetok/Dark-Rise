#!/usr/bin/env python3
"""
Build script for THE DARK RISE — Episode 129: "When Every Fight Became One Fight"
Uses the shared scripts/dr_build.py module.

Written 2026-08-11 (scheduled release TBD): Mfoniso and Ebiere's standoff
breaks into open combat, drawing the compound's guards inward and
emptying its outer wall at the exact moment the search party, watching
from the tree line, decides the chaos will not offer a better opening.
They breach the wall and collide with the fight before either side
understands who the other actually is. In Oso, the presence reaches
further than it ever has since Kene's rescue, toward its own lost
ground's direction, at real cost to itself.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dr_build import build_episode

EPISODE_NUM = 129
EPISODE_TITLE = "When Every Fight Became One Fight"

EPISODE_CONTENT = [
    {"type": "title_series", "text": "THE DARK RISE"},
    {"type": "title_subtitle", "text": "Book One: The Abandoned"},
    {"type": "title_ep_num", "text": "Episode One Hundred and Twenty Nine"},
    {"type": "title_ep_name", "text": "When Every Fight Became One Fight"},
    {"type": "page_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE ONE: THE COMPOUND
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Ebiere moved first, a professional's clean, economical "
        "opening strike that Mfoniso read a half breath before it "
        "landed and turned aside with her own blade, steel ringing loud "
        "enough down the corridor's stone walls that the sound alone "
        "did more damage to two seasons of careful secrecy than either "
        "woman's actual intentions ever could."
    )},
    {"type": "body", "text": (
        "Guards came at a run from every direction the corridor's echo "
        "could reach, drawn by a sound this House had never once had "
        "reason to hear inside its own walls, two of its own trained "
        "hunters meeting each other with drawn steel rather than "
        "orders."
    )},
    {"type": "body", "text": (
        "\"Stand down, both of you,\" the guard captain shouted, "
        "arriving with a dozen men behind him and no clear idea which "
        "woman he was actually meant to be protecting the compound "
        "from. Neither Mfoniso nor Ebiere gave him the satisfaction of "
        "an answer, too fully committed now to a fight that had long "
        "since stopped being about following anyone's orders at all."
    )},
    {"type": "body", "text": (
        "Ebiere pressed harder once the guard captain's shout made "
        "clear no rescue was coming from that quarter, trading "
        "professional caution for speed now that speed was the only "
        "advantage left available to her, and it took every year of "
        "Mfoniso's own harder training to keep the exchange even, two "
        "hunters of the same House meeting blade for blade with a "
        "ferocity neither of them had ever once had cause to spend on "
        "each other before tonight."
    )},
    {"type": "body", "text": (
        "\"You could still step aside,\" Ebiere said, breathing hard "
        "between exchanges, genuine rather than taunting. \"I do not "
        "actually want this fight, Mfoniso. I want the assignment "
        "finished and my own name finally clean again. Give me the "
        "door and neither of us has to find out tonight which of us "
        "would actually win this.\""
    )},
    {"type": "body", "text": (
        "\"I cannot give you what was never truly mine to give away in "
        "the first place,\" Mfoniso said, and pressed the advantage of "
        "the answer into her own next strike, forcing Ebiere back a "
        "full step toward the crowd of guards still too uncertain, "
        "even now, to actually intervene."
    )},
    {"type": "body", "text": (
        "The alarm bell began ringing somewhere behind the growing "
        "crowd, an old iron note this compound had rarely needed to "
        "sound twice in a single season, and every guard still holding "
        "an outer post heard it exactly the way an outer post's guard "
        "was trained to hear it, as an order to converge inward rather "
        "than to hold the line where he already stood."
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE TWO: THE SEARCH PARTY
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Osadebe heard the bell from the tree line and understood, "
        "faster than he wanted to admit understanding it, exactly what "
        "kind of chance a compound this distracted was about to hand "
        "three men willing to take it."
    )},
    {"type": "body", "text": (
        "\"Ifeanyi stays,\" he said, already moving, leaving no room in "
        "his own voice for the argument he could see forming on "
        "Ifeanyi's still pale face. \"You cannot run on that wound, and "
        "we cannot carry you and move fast enough to matter. Guard this "
        "camp. If we do not return by first light, you go for Adaeku's "
        "party yourself, however far behind us they still are.\""
    )},
    {"type": "body", "text": (
        "The wall's northern face, scouted at such cost only nights "
        "before, stood nearly empty for the first time since the "
        "party's watch had begun, its usual careful rotation abandoned "
        "for the compound's own inward panic. Osadebe went over first, "
        "Emenike and Okonjo close behind him, all three moving with the "
        "particular reckless speed of men who understood, without "
        "needing to say it aloud, that this chance would not offer "
        "itself twice."
    )},
    {"type": "body", "text": (
        "Okonjo said nothing about his own still tender ankle as he "
        "cleared the wall behind the other two, saving whatever breath "
        "the climb had cost him for whatever the ground beyond it "
        "still demanded. He had learned, across these past hard weeks, "
        "exactly how little patience real danger showed a man who "
        "spent his own strength worrying about an old injury before "
        "worrying about the fight actually in front of him."
    )},
    {"type": "body", "text": (
        "They found chaos rather than any clear path once they cleared "
        "the wall, guards running past them in the dark toward a "
        "commotion none of the three could yet see, torches swinging "
        "wild enough that shadows themselves seemed to be fighting "
        "somewhere just out of sight."
    )},
    {"type": "body", "text": (
        "Emenike reached the corridor's mouth first, drawn by "
        "instinct rather than any plan, and stopped hard at the sight "
        "waiting inside it, a woman he recognized instantly, blade "
        "still raised, the same face that had struck him down in "
        "Idoro's own compound and haunted every hard night since."
    )},
    {"type": "body", "text": (
        "\"Mfoniso,\" he said, the name arriving out of him half warning "
        "and half accusation, already moving to close the distance "
        "before Osadebe's own sharper hand caught his shoulder and held "
        "it."
    )},
    {"type": "body", "text": (
        "Mfoniso turned at the sound of her own name spoken by a "
        "stranger's voice, and found, for one suspended, impossible "
        "moment, three armed men she had never once expected to meet "
        "inside this particular corridor, one of them wearing a face "
        "she recognized from a very different fight, a very different "
        "wall, a lifetime ago that suddenly did not feel like a "
        "lifetime at all."
    )},
    {"type": "body", "text": (
        "\"You are the household's soldier,\" she said, understanding "
        "arriving faster than either of them had time to properly "
        "process it. \"You are here for the guest.\""
    )},
    {"type": "body", "text": (
        "\"She is my sister,\" Emenike said, blade still raised, "
        "trusting nothing about a woman who had once broken into his "
        "own home. \"Explain to me quickly why I should not finish "
        "here what I failed to finish at Idoro.\""
    )},
    {"type": "body", "text": (
        "Osadebe stepped between them without lowering his own blade "
        "from the wider chaos still gathering around all four of them, "
        "reading the corridor's whole shape the way a captain reads "
        "ground he has never once stood on before. \"We do not have "
        "time for either of your histories,\" he said. \"Guards are "
        "converging on this exact spot from every direction that bell "
        "can reach. Whatever this woman is or is not, we settle it "
        "moving, or we settle nothing at all before this whole "
        "compound arrives to settle it for us.\""
    )},
    {"type": "body", "text": (
        "\"Because I am the only reason that door still stands "
        "guarded rather than already emptied,\" Mfoniso said, flat and "
        "fast, no time left in the corridor's own gathering chaos for "
        "anything gentler than the plain, unpolished truth of it. "
        "\"Choose quickly whether you trust that fact or waste both of "
        "our remaining chances arguing about it instead.\""
    )},

    {"type": "scene_break", "text": ""},

    # ═══════════════════════════════════════════════════════════════
    # SCENE THREE: OSO
    # ═══════════════════════════════════════════════════════════════

    {"type": "body", "text": (
        "Chibundu woke gasping in the middle of that same night, "
        "though nothing in his own quiet room at Oso had actually "
        "changed, the presence's own sudden, wordless alarm flooding "
        "through him before either old power had found language "
        "enough to explain what it had just felt."
    )},
    {"type": "body", "text": (
        "\"Something is happening to them,\" the presence said, its "
        "voice already stretched thin in a way Chibundu had learned, "
        "across many hard months, to recognize as danger to the "
        "presence itself rather than merely to whoever it was reaching "
        "toward. \"The search party. The bearing. I can feel it the way "
        "I once felt Kene's own danger, distant and terrible and too "
        "far to properly reach.\""
    )},
    {"type": "body", "text": (
        "Chibundu felt it too, faintly, a secondhand echo of whatever "
        "the presence itself was feeling, distance and urgency braided "
        "together into something he had no honest word for. \"Can you "
        "tell what kind of danger,\" he asked, already knowing, from "
        "the presence's own long hesitation, that the answer would not "
        "comfort him."
    )},
    {"type": "body", "text": (
        "\"No,\" the presence admitted. \"Only that it is close to the "
        "same ground I once called home, and that something inside me "
        "recognizes the shape of it the way a body recognizes an old "
        "wound before the mind has finished remembering why it "
        "aches.\""
    )},
    {"type": "body", "text": (
        "\"Then do not reach,\" the entity said, sharp with a fear it "
        "rarely allowed itself to show. \"You are not strong enough. "
        "You were not strong enough the day you saved Kene, and you "
        "have spent everything since rebuilding only a fraction of "
        "what that day cost you.\""
    )},
    {"type": "body", "text": (
        "\"I am aware of the cost,\" the presence said, and reached "
        "anyway, further than it had ever once reached since the day "
        "it tore itself loose to save a child it had never met, past "
        "Oso's border, past the short new distance the returned "
        "fragment had only recently taught it to trust, out toward "
        "ground that had once, three centuries ago, belonged entirely "
        "to itself."
    )},
    {"type": "body", "text": (
        "It found nothing it could properly name, no clear sight of "
        "the search party or the compound holding them, only the "
        "faint, unmistakable shape of danger gathered somewhere along "
        "its own oldest bearing, and it held its reach there anyway, "
        "trembling with the effort, offering whatever thin, "
        "unfocused strength it could still spend toward men it had "
        "never met, fighting a battle it could not see, for a debt "
        "three hundred long, patient years now overdue, still "
        "unpaid, and never once, until this exact night, properly "
        "attempted at all."
    )},
    {"type": "body", "text": (
        "It let go only when its own strength gave out entirely "
        "beneath it, collapsing back into Oso's own ground with a "
        "silence that frightened Chibundu more than any scream could "
        "have. \"I do not know if it reached them,\" it said at last, "
        "faint. \"I know only that it cost more than I had left to "
        "spend, and that I would spend it again tonight, and every "
        "night after this one, without hesitation, if any of those "
        "nights ever asked the same thing of me a second time.\""
    )},
]

if __name__ == "__main__":
    build_episode(EPISODE_NUM, EPISODE_TITLE, EPISODE_CONTENT)
