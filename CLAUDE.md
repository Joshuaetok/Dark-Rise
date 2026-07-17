# CLAUDE.md — THE DARK RISE
### Project bible & operating instructions for every episode

This file is the single source of truth for **The Dark Rise**, a 1000-episode
Pocket FM audio drama. Read this file in full before writing any episode.
Never contradict it. When an episode adds a new permanent fact (a death, a
power gained, a title changed), **update this file in the same commit** as
that episode.

**This file was split on 2026-07-13** after the Living Name Registry and
Changelog grew past the 150,000 character working-memory limit at Episode 78.
Nothing was lost — the full, unabridged episode-by-episode history through
Episode 78 (registry) and, for the changelog, every episode older than
Section 11's active window (see `ARCHIVE.md`'s changelog header for its
current range) now lives in `ARCHIVE.md` in this same repo. This file keeps only what's needed to write the next episode
without contradiction: each character's *current status*, and the
changelog's active arc (last ~15 episodes). See Section 5 and Section 11
below for the maintenance rule that keeps it that way going forward.

---

## 1. WHAT THIS STORY IS

- Genre: dark supernatural rise-to-power drama, in the tradition of
  *Vampire System*-style Pocket FM serials — hidden power, a marked outcast,
  slow accumulation of strength, court intrigue, betrayal, vengeance.
- Setting: a fully fictional West African-inspired world. **No real countries,
  leaders, or historical figures are named anywhere in the story.** Real
  Nigerian history (see Section 7) is the emotional and structural skeleton,
  never the surface. If a plot beat maps directly onto a real assassination,
  election, or execution, it must be fictionalized in every detail — names,
  dates, exact methods, dialogue — before it goes in an episode.
- Names: African names throughout (people, places, titles). Names should
  sound authentic (drawn from real Igbo/Yoruba-style phonetics and naming
  logic) but must not be copied from existing novels, real public figures, or
  overused clichés (avoid reusing names like Okonkwo, Ikemefuna, Chukwu,
  Adaeze, Ngozi, Chinedu as-is — invent adjacent, fresher names in the same
  spirit). See Section 5 for the living name registry.
- Audio-first prose: every sentence must work read aloud, cold, with no
  visual aid. Short sentences. Concrete images. Minimal subordinate clauses.
  No sentence should require re-reading to parse. **All rules in Section 3
  (Pocket FM AI Audio Guidelines) apply to every sentence — read that section
  before drafting.**
- Target audience: men and women, young adults and up. The show title ("The
  Dark Rise") is already set; any future arc subtitles must be concise,
  evocative, and genre-resonant (see Pocket FM titling guidance in Section 3).

---

## 2. STORYTELLING CRAFT PRINCIPLES

Every episode must be built on these fundamentals. They are the scaffolding
beneath every scene, every line of dialogue, every hook.

### 2.1 The Plot Is a Blueprint
- Think of the plot as a treasure-hunt blueprint. Every scene must advance
  the listener toward the treasure — or deeper into the trap. Nothing is
  random. If a scene does not move the story forward, cut it.
- The audience should always feel the story knows where it is going, even
  when the characters do not.

### 2.2 Three-Act Structure (Per Episode)
Every episode, no matter how short, has a beginning, a middle, and an end:
- **Beginning (Setup):** Establish where we are, who is present, and what is
  at stake — within the first 90 seconds of narration. The listener must
  know whose eyes they are seeing through and why they should care.
- **Middle (Rising Action / Conflict):** The challenge deepens. The
  character faces an obstacle, makes a choice, or discovers something that
  changes the situation. Tension rises. This is the engine of the episode.
- **End (Climax + Hook):** The immediate conflict reaches a peak — then the
  episode cuts away, leaving the listener desperate for the next one. Never
  end on a resolved, comfortable beat (see Section 4 for hook requirements).

### 2.3 Conflict Is the Engine
- Without conflict, there is no story — only description. Every episode
  needs a problem.
- Conflict enters when a challenge disrupts the character's life. It can be
  external (an enemy, a law, a betrayal) or internal (fear, doubt, a
  terrible choice) — but it must be present in every episode.
- A looming challenge — one the character can see coming but cannot yet
  stop — is one of the most powerful hooks in serial fiction. Use it.

### 2.4 Character Basics
- Introduce every named character with enough detail that the listener can
  picture them and understand their immediate role. A physical detail, a
  status marker, a telling action — these do more work than a paragraph of
  description.
- Every character wants something. The listener should know or sense what
  that is within the character's first scene. A character whose desires are
  unclear is a character the audience will ignore.

### 2.5 Story Threads — Main Plot and Subplots
- The main plot is the central spine of the series: the protagonist's rise
  from abandoned curse-child to ruler.
- Subplots are connected events and supporting threads that develop
  alongside the main plot. Over time, these threads must weave into and
  become part of the main plot — nothing should feel like filler.
- Track every open thread. If you introduce a question, a mystery, or a
  promise, you must eventually pay it off. The Pocket FM audience listens
  daily and remembers.

---

## 3. POCKET FM AI AUDIO GUIDELINES — NON-NEGOTIABLE

Chapters are converted into audio episodes through AI voice technology.
Every sentence must be written for clean AI narration. These rules are
non-negotiable — violations produce awkward, unlistenable audio.

### 3.1 Typing Precision
- **Zero tolerance for typos.** AI reads literally — it cannot identify or
  correct mistakes. "Radhel" typed instead of "Rachel" will be spoken as
  "Radhel." Proofread every line before committing.
- **No stammer or stutter words.** "b-b-baby" or "wh-what" kill AI flow.
  Write smooth, coherent speech every time.

### 3.2 Full Words — No Abbreviations
- **Write complete words only.** AI narration requires full forms for
  natural cadence.
  - "Doctor" not "Dr." (AI reads "Dr." as "Doctor" with an awkward pause)
  - "Mister" not "Mr."
  - Spell out all titles, honorifics, and common short forms.
- This applies to everything: "versus" not "vs.", "Saint" not "St.", and so
  on.

### 3.3 Numbers as Words
- **Write all numbers in word form.** AI misinterprets digit strings.
  - "ten thousand" not "10,000"
  - "fifty thousand dollars" not "$50,000"
  - "call nine one one" not "call 911"
  - "one point seven million" not "1.7 million"
  - "thirty thousand" not "30K"
- When a numeric comma IS used, always English format: "281,000."

### 3.4 Punctuation Rules
- **No clustered punctuation.** Never use !!!, ...., ?!, ****, or any
  multi-mark grouping. One exclamation point. One question mark. An ellipsis
  is three dots, once — not six, not twelve.
- **No hyphens.** Write compound terms without hyphens for cleaner AI flow.
  "well known" not "well-known." "newly built" not "newly-built."

### 3.5 No Episode Metadata in Body Text
- **Episode numbers and titles stay out of the narration body.** They belong
  in the file name and title page only. The AI reads everything in the body
  aloud — if it speaks "Episode Two: The Return" mid-story, immersion breaks.

### 3.6 Sensory Description — No Onomatopoeia
- **Never use sound-effect words.** No "tch tch," "tsk tsk," "bang," "boom,"
  "slam," "haha," "crash," etc. as standalone effects. Instead, write full
  descriptive sentences:
  - ✗ "Bang! The door slammed shut."
  - ✓ "The door slammed shut with a heavy crash that echoed through the
    empty hall."
  - ✗ "Haha, very funny."
  - ✓ "She laughed, a short sharp sound with no warmth in it."

### 3.7 Heteronym Awareness
- **Minimize heteronyms** — words spelled identically but pronounced
  differently by meaning. Example: "residential address" vs. "she addressed
  him." When a heteronym is unavoidable, ensure the surrounding context
  forces the intended pronunciation.

### 3.8 No Repetitive Echo Phrases
- **Avoid echo words.** "Yes yes," "okay okay," "no no no" — these read as
  stuttering redundancy in AI narration. Write each beat once, cleanly.

### 3.9 License Plates and Letter Sequences
- **Insert spaces between individual letters** when referencing license
  plates or letter codes: "Y U N four five seven eight" not "YUN 4578."
  This ensures the AI pronounces each character distinctly.

### 3.10 Paragraph Pacing and Dialogue Tone (added 2026-07-17, piloted on Episode 1)
TTS engines pause longest at paragraph breaks — noticeably longer than at a
period. Structure paragraphs for the ear:
- **One paragraph = one connected beat.** Group related sentences into
  paragraphs of roughly two to five sentences. Do not give every sentence
  its own paragraph — that inserts a long pause after each line and makes
  the narration sound halting.
- **A standalone one-line paragraph is a deliberate dramatic pause.** Use
  it only at genuine peaks (a reveal, a hook, a gut punch) — a handful per
  episode, no more.
- **Never emit empty paragraphs for scene breaks.** Empty paragraphs become
  stacked silence in narration. Build scripts must mark scene breaks by
  adding vertical spacing (spacing before) on the next paragraph instead
  (see `scripts/build_episode_01.py`, the `scene_break` type).
- **No em dashes or en dashes in narration** — they read as another hard
  pause. This extends Section 3.4's hyphen ban to all dashes. Use a period,
  a comma, or a rewrite.
- **Every dialogue line carries a tone cue** placed before or immediately
  beside the quote, so the AI voice can color the line: "Zara urged, her
  voice low and fierce," "his voice cracked open into begging," "he said,
  dry as harmattan dust." Never leave a bare unattributed quote — the
  listener cannot see paragraph placement, and the voice cannot infer tone
  it was never given.
- Build scripts should lint for dashes, double spaces, and hyphenated
  words before building (see `lint_content()` in the Episode 1 script).

---

## 4. EPISODE FORMAT — NON-NEGOTIABLE

- **Length: 11–15 minutes of narration per episode.** At a spoken pace of
  130–150 words/minute, that means a **target word count of 1,550–2,150
  words**, aiming for the 1,700–1,900 sweet spot. Always run the word count
  after drafting (see Section 10 — Build & Verify Checklist) and adjust before
  finalizing. Never ship an episode outside the 11–15 minute range.
- **One episode = one .docx file**, titled `The_Dark_Rise_Episode_##.docx`,
  formatted per Section 9.
- **Every episode ends on a hook.** No exceptions. The last line must do one
  of: reveal a threat, reveal a betrayal, reveal a hidden truth, cut away at
  the worst possible moment, or drop a piece of information that recontextualizes
  what just happened. Never end on a resolved, comfortable beat.
- **Every episode must escalate at least one of:** danger, intimacy/trust,
  or stakes. If an episode doesn't move at least one of these forward, it
  needs another pass.
- **Emotional turn required.** Every episode should make the listener feel
  something specific and nameable (grief, dread, triumph, betrayal, tenderness)
  — not just "things happened." Suspense without an emotional anchor goes flat
  over 1000 episodes.
- **Daily publishing cadence.** Pocket FM audiences expect fresh content every
  day. Use the schedule-ahead feature to maintain a consistent daily release
  rhythm. Never miss a day if you can avoid it.

---

## 5. LIVING NAME REGISTRY

**This section holds each character's CURRENT STATUS ONLY — not a
history.** Full episode-by-episode detail through Episode 78 lives in
`ARCHIVE.md`; recent episodes' detail is still recoverable from Section 11's
changelog below (see that section's header for the exact current window).

**Maintenance rule (read this before editing):**
- When an episode changes a character's status, **replace** the relevant
  sentence(s) in their entry — do not append a new "In Episode N..."
  clause on top of the old one. This section must stay a snapshot, not a
  log.
- Permanent facts (deaths, true names revealed, titles changed, powers
  gained) stay inline forever, briefly.
- Anything that's just "what happened" belongs in Section 11's changelog,
  not here. If you're ever tempted to write "In Episode 40, then in
  Episode 41, then in Episode 45..." inside a registry entry, stop — that
  history already exists in the changelog and in `ARCHIVE.md`. Write only
  the current state that results from it.
- Never introduce a new name without checking it isn't already used for
  something else, and never silently rename something already established.

### People

| Name | Role | Current status (as of Episode 101) |
|---|---|---|
| Amara | Mother of the twins | Alive, Idoro, full council seat. Knows the entity, the presence, Chibundu's identity, and Elder Maka's condition — no secrets left within the household. Current thread: sent the search party off with a plain, direct plea for Emenike to come home either way, having claimed him as more than a soldier to this house (Ep100). |
| Obi | Father of the twins | Alive, Idoro. Fully present and active partner to Amara in every crisis since Episode 6. Current thread: sat quietly with the recovering Emenike, who declined an early end to his season of watching, preferring trust earned slowly to trust granted out of pity (Ep95). |
| Zara | Village midwife | Alive, living mostly at Amara's compound. Delivered both twins; carries a dormant blood thread the presence (not the entity) has used to reach her since her Episode 42 return. Her borrowed sense of danger has been the family's best early warning system since Episode 69. Current thread: walked the first stretch of road with the search party as promised, her flickering gift finding nothing to warn of; turned back at the old boundary stone (Ep100). |
| Adaugo | Elder Maka's surviving daughter | Alive, Idoro. Fully reconciled with her mother since Episode 66. The anchor thread Mfoniso planted on her wrist (Ep80) appears permanently inert since Ep90. Current thread: not yet able to travel far from her training, offered instead to help plan the search for Ijeoma properly, drawing on her own months of once waiting for rescue (Ep99). |
| Elder Maka | Elder priestess | Alive, Idoro, restored to a respected advisory council seat (not sole authority over the old law, stripped Ep19). Secretly carries her own thin thread to the entity since the Episode 12 binding rite (now openly known to the household and village). Current thread: blessed the search party's departure with an old protective rite and gave Emenike a plaited cord to carry (Ep100). |
| Ozoemena | Mid ranking Idoro elder | Alive, Idoro. Humbled, trusted council member who serves through labor since his own disastrous rite killed the dibia (Ep26). Current thread: held the household to its promise to search for Ijeoma, arguing a harder promise kept only when convenient has not truly been kept at all (Ep99). |
| Kene | Surviving firstborn twin | Alive, toddler, Idoro. Original twin thread to the entity severed (Ep12); knows he has a brother (told Ep66); survived Mfoniso's first abduction attempt (Ep70), saved when the presence reached beyond Oso's ground for the first time. Began tracing an unbidden spiral in the dirt (Ep76) — the same shape both old powers have used on Zara — raising fear the presence's rescue left a second, uncut thread in him. Current thread: the spiral tracing has gone still rather than resolved; Kene reports it "does not feel like it wants me to" today, unresolved per Elder Maka's assessment (Ep95). Family continues watching rather than attempting a severing rite. |
| Chibundu | Abandoned secondborn twin / protagonist ("the one whom the presence carries") | Alive, Oso. Named by the presence through Zara (Ep47); reunited with Amara (Ep50); survived a trading House ambush at that reunion; has twice refused the trading House's partnership offer (once in his own voice, once when the presence seized his voice to refuse it for him, Ep60-61) and extracted a narrower promise from the presence (it will not take his voice again except to save his life). Current thread: dreamed the toppled boundary stone as it stood three centuries ago — upright, ochre filled, living ground beyond it — the same night the search party found it; woke to the presence's confirmation and now knows the party is two days from the lost ground. Deliberately did not promise the presence the answer would be bearable, honoring its request to stop being protected from the truth (Ep101). |
| Eze Amadi | King, Kingdom of Ijendu, throned at Udo | Alive, Udo. Aware of the entity and, since Ep65, the presence as a second distinct power. Has permanently assigned Osadebe to Idoro and stationed Chidebe's garrison there. Current thread: absorbed Osadebe's report of the entity's direct action and the coerced informant, and authorized a formal crown investigation into trading House sabotage, a doubled permanent garrison for Idoro, and Ejikeme's long refused land survey, reframed as crown obligation rather than trade measure (Ep94). |
| Nduka | Crown river-road intelligence agent | Alive. Minor, not currently active — carried the first report of Idoro's unraveling to Udo (Ep24). |
| Nkiruka | Keeper of the crown's old rites and records, Udo | Alive. Holds the crown's only historical archive on prior encounters with old powers. Revised her reading (Ep65) to recognize two separate powers rather than one growing bolder. Found a centuries old record of a border village that discovered a coerced informant exactly as Idoro did, whose account then stops mid record with no resolution (Ep94); still kept private from Eze Amadi. Current thread: personally endorsed Osadebe's Ijeoma search request alongside Eze Amadi's seal, privately hoping it might answer what her own unfinished archive record could not (Ep99). |
| Ejikeme | Overseer of the crown's delta trade concessions, Udo | Alive. Won authorization for the crown survey of Idoro's land he had twice been refused (Ep94), granted as crown protective obligation rather than a trade measure, though he could not promise Nkiruka the crown would keep that distinction once exploitable ground was found. Dispatched to begin survey preparations within the week. |
| Osadebe | Captain of Eze Amadi's personal service, permanently assigned to Idoro | Alive. The crown's primary eyewitness and liaison to Idoro. Leads the Ijeoma search party (himself, Emenike, Ifeanyi, Okonjo), sketching fresh maps each evening past the edge of Ubani's survey. Current thread: four days west, the party found a centuries old boundary stone laid deliberately face down with a spiral cut into its buried face; he copied the mark exactly onto his map, judged the stone was laid down rather than fallen ("the way you lay down the dead"), and noted its facing line runs west and slightly south (Ep101). |
| Chidebe | Captain, commands the crown garrison at Idoro | Alive. Disciplined, trusted by Osadebe. Current thread: argued Emenike was not yet strong enough for the Ijeoma search and was overruled by Emenike's own flat refusal to be protected from the one thing he still has a right to insist on (Ep99). |
| Ikwuano | Keeper of the crown's scattered intelligence reports, Udo | Alive. Traced the trading House's court sponsor and confirmed its interest in Idoro predates its public approach by years. Not currently central to the active plot thread. |
| *(unnamed dibia)* | Village diviner/healer; carried the secondborn to Oso | **Deceased (Episode 26).** Was the entity's first mouthpiece; killed when Ozoemena's borrowed rite against him failed and the entity struck him down mid final message. |
| *(unnamed entity)* | Ancient presence beneath Oso, bonded to Chibundu | Active, still badly weakened but mending. Three centuries old, patient and transactional; broke three centuries of pure restraint to act directly against Mfoniso (Ep90). Current thread: named plainly to the presence that in two days the searchers will stand on what is left of its ground, "and all three of us will learn what three centuries did to it" (Ep101). |
| *(unnamed presence)* | Older power beyond Oso's outer borders, reaches Chibundu through dreams and has spoken through Zara | Active. Named Chibundu (Ep47). Once lost a guardian ground centuries ago to a hunter using the exact tactic Mfoniso now uses (take the people the guardian loves, wait, strike slowly) — revealed Ep67. Broke its three century habit of never overspending its strength to save Kene directly (Ep70), at a cost it still hadn't finished paying as of Ep72-73; further spent by tearing itself out of Zara in Ep82. **Major reveal (Ep100):** confirmed under Chibundu's direct pressure that its own lost guardian ground lay exactly along the bearing west and slightly south of Oso — the same bearing the Ijeoma search now travels. Current thread: the search party found its ground's easternmost boundary stone, laid face down by the hunters' custom "so the land forgets its own name"; through Chibundu's dream it confirmed the stone and that the lost ground now lies two days ahead of the search — the closest it has come in three centuries to learning what became of its people (Ep101). |
| Uduak | Market trader, former trading House informant | Alive, held pending Udo's judgment since his confession (Ep53). Not currently active in the plot. |
| the Warden | Ijoma Concern's keeper of old and dangerous knowledge | Active. Authorized Mfoniso's second attempt, against Zara directly (Ep74), overruling the Factor's objection. Revealed the guardian ground debt is inherited across four keepers before her rather than her own personal grievance; permanently relieved the Factor of any further say in the operation and committed resources beyond anything spent on the hunt so far (Ep93). Current thread: canceled the bracelet proof runs outright (no one left to persuade), took the guest's ledger line from the Factor, left Ijeoma's fate explicitly undecided between asset and expense, and sent a ciphered query to Mfoniso asking whether the hunt still requires the guest kept breathing or the House may close the account (Ep101). |
| Mfoniso | Ijoma Concern's retained guardian hunter | Active — the story's current antagonist. Failed to abduct Kene (Ep70) when the presence intervened directly; pivoted to a slow, undetectable working against Zara's borrowed senses instead, confirmed succeeding by Ep77-78. Confirmed as trained in or descended from the same hunting lineage that took the presence's guardian ground three centuries ago (Ep82); revealed to be carrying her own second thread to whoever trained her (Ep83). Breached Idoro's compound directly, seized Adaugo, and struck down Emenike, then fled wounded and shaken when the entity met her in the open for the first time (Ep90). Delivered her account to the Warden in person and received resources beyond anything committed so far, plus confirmation of Ijeoma's location at the Concern's headquarters (Ep93). Current thread: fully healed, resumed scouting Idoro from a distance and found it transformed — a far larger garrison and staggered patrols (the survey crew she observed has since departed, Ep98) — forcing her to rebuild her understanding of the village from the ground up before deciding her next move. A ciphered query from the Warden — whether the hunt still requires Ijeoma kept breathing — is en route to her; she has not yet received it, and does not know the Warden is asking (Ep101). |
| Chiazor | Trading House's formal sponsor at Udo | Alive. Revealed a senior House figure was already traveling toward Idoro before the ambush. Not currently central to the active plot. |
| the Factor | Senior trading House figure, Ebiere's direct superior | Alive, permanently removed from any further say in the Mfoniso operation. Objected three times now (Ep64, Ep74, Ep93) to escalating the hunt against Oso's guardian, each time overruled; his final, sharpest objection after learning of the entity's direct intervention led the Warden to relieve him of authority over the operation entirely (Ep93). Current thread: surrendered the guest's ledger line to the Warden, argued in pure cost terms against killing Ijeoma (bodies open accounts rather than close them), and passed within sight of her for the first time — recognizing he had signed two seasons of her keeping without once reading the line as a person; the first private crack in his loyalty to the House (Ep101). |
| Ebiere | Trading House field agent who orchestrated the boundary ambush | Whereabouts unknown since Ep53; publicly disowned by the Factor as a rogue agent. |
| Effiong | Young crown soldier who sold patrol schedules for coin, enabling the ambush | Confessed (Ep52). Not currently active in the plot. |
| *(unnamed)* | Elder Maka's returned son | Deceased. Her own abandoned twin, returned wrong at age eight, killed three people including her husband; she killed him herself. Origin of her severity toward the old law. |
| Emenike | Soldier in Chidebe's garrison at Idoro | Alive, on the road with the Ijeoma search party, three days west of Idoro. Served under Chidebe since before the boundary ambush (Ep51); confirmed as Mfoniso's informant (Ep87), coerced for two seasons by threats against his sister, Ijeoma. Threw himself between Mfoniso and Adaugo during her direct attack on the compound (Ep90). Carries Elder Maka's protective cord and Amara's plea to come home either way. Current thread: four days out, present at the boundary stone discovery; crouched close but touched nothing, having learned some marks are not free to read aloud (Ep101). Does not know Mfoniso confirmed Ijeoma's location (Ep93), that the Warden has stopped the bracelet proof runs and is asking Mfoniso whether Ijeoma still needs keeping alive (Ep101), nor that the presence's lost guardian ground lies two days ahead of him. |
| Ijeoma | Emenike's younger sister | Alive, confirmed held at the Ijoma Concern's disguised headquarters downriver, seen briefly by Mfoniso in a heavily guarded inner courtyard (Ep93), confirming the bearing (west, slightly south) reported in Ep88. Taken from a river town by the Concern's agents two seasons ago while trading cloth for their mother; held as leverage to coerce Emenike's cooperation as an informant. Introduced in her own viewpoint for the first time (Ep101): nineteen, a cloth trader's daughter who counts everything, watchful and deliberate. Current thread: deduced from the overdue fifth bracelet taking that proof of her life no longer purchases anything (her brother caught or dead), concluded the House is now keeping a witness rather than a lever, and quietly began studying guards, watches, and the wall's one bad corner — done waiting (Ep101). Does not know a search party is four days out, nor that the Warden has asked Mfoniso whether she still needs keeping alive. Idoro's household does not yet know her exact location has been confirmed. |
| Adaeku | Soldier in Chidebe's garrison at Idoro, quietest of the six informant suspects | Alive. Cleared in practice, if not yet formally: paired with Emenike on the same false route, but his own night proved ordinary — a plain meal alone and sleep, watched the whole while by Osadebe (Ep86). |
| Ubani | Lead surveyor, crown survey party at Idoro (Ep94's authorized survey) | Alive, survey work concluded. Careful, observant, professionally honest; fifteen years' experience surveying disputed and unusual ground. Walked Oso's boundary alone (Ep97) and encountered an overwhelming, formless dread with no concrete cause he could name. Current thread: accepted Elder Maka's true but incomplete account of Oso as the old law's abandonment ground and grief-soaked site; marked it consecrated ground excluded from crown development in his official report, protecting the household's deeper secret without ever being told it, and departed Idoro with genuine respect for what he chose not to dig further into (Ep98). |
| Ude | Ubani's second on the crown survey, carries the measuring chain | Alive. Grew up two villages from Idoro; knows Oso's reputation but is cautious about saying so to a crown official. Warned Ubani gently that the ground is tied to old grief, not merely superstition (Ep96), which helped prepare him to accept Elder Maka's account without much resistance (Ep98). |
| Ifeanyi | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Grew up hunting; first to read the land's wrongness — game trails bending in wide curves around nothing (Ep101). |
| Okonjo | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Found the toppled spiral boundary stone an hour before dusk on the fourth day west (Ep101). |

### Places
| Name | What it is |
|---|---|
| Kingdom of Ijendu | The nation; ruled by an Eze from the capital |
| Udo | Capital city, seat of the throne |
| Oji Delta | Oil-rich, foreign-exploited delta region |
| Idoro | Village where the story begins, in the Oji Delta |
| Oso | The "forbidden bush" where cursed children are abandoned |
| iroko tree | Ancient tree at the boundary of Oso; where abandoned children are laid. **Renamed from "ak-pu" on 2026-07-16** (post-Episode-100 maintenance pass): the old spelling was hyphenated (violating Section 3.4) and unreliable in TTS. All episode files, build scripts, and ARCHIVE.md were updated in the same commit. Never write "ak-pu" again. |
| the Ijoma Concern | Foreign trading House operating through Ebiere, the Factor, and Chiazor; true headquarters revealed in Episode 64 as a disguised trading post several days downriver, kept off the crown's tax records |

### Titles / Concepts
| Term | Meaning in-story |
|---|---|
| Eze | King/ruler |
| Abiku | A child believed to be a spirit that dies and returns to torment its family — the in-world explanation for what the protagonist is believed to be |
| Dibia | Traditional healer/diviner who communes with spirits |

**Rule:** any new named character, village, or title must be added to this
table before or immediately after the episode that introduces them.

### 5.1 AUDIO CONFUSABLE-NAME RULES (mandatory — this is a TTS show)

Names that read fine on the page can be near-identical spoken aloud. These
rules exist because of collisions already present in the cast. Check every
new name against this list for *sound*, not just spelling.

- **Ijeoma vs. the Ijoma Concern:** one soft vowel apart in narration, and
  they are victim and captor in the same arc. In episode narration, always
  call the trading House **"the Concern"** (or "the House" in dialogue).
  The full name "Ijoma Concern" must never appear in any episode that also
  names Ijeoma. It has only ever been spoken on-page in Episodes 64, 68,
  and 74 — keep it that rare.
- **Amara vs. Eze Amadi:** never write bare "Amadi" in any scene that
  contains Amara. The king is always "Eze Amadi" (his existing pattern —
  bare "Amadi" has appeared only twice, Episodes 31-32, in crown-only
  scenes).
- **Chibundu vs. Chidebe (vs. Chiazor):** the protagonist and the garrison
  captain have never shared a scene; when their storylines converge,
  re-anchor with role tags ("the captain," "the boy") every few lines
  rather than alternating bare names.
- **Adaugo vs. Adaeku:** near-identical aloud. Adaeku is retired from
  active use; if he must reappear, always tag him ("Adaeku, the quiet
  one").

### 5.2 WHO KNOWS WHAT — dramatic irony ledger (as of Episode 101)

Update this table whenever knowledge changes hands. It protects continuity
(no character may act on a fact this table says they lack) and marks where
the suspense lives.

| Fact | Who knows | Who does NOT know |
|---|---|---|
| The captor House's name ("the Ijoma Concern") | The Concern's own people; the narration (Eps 64, 68, 74 only) | **The household and the crown have never heard the name.** They say "the trading House" / "the House." The crown's Ep94 investigation into which House sponsored the coercion is still unresolved. |
| Ijeoma's exact location (the Concern's headquarters, confirmed Ep93) | Mfoniso only — she told no one, holding it as leverage | The Warden, the household, the crown, and **Emenike**, who searches on a bearing alone |
| The presence's lost guardian ground lies along the search bearing (Ep100), two days ahead of the party (Ep101) | The presence, the entity, Chibundu | Everyone else — the search party found the ground's boundary stone (Ep101) but has no idea what it marks or that Oso knows |
| The bracelet proof runs are canceled (Ep101) | The Warden, the Factor; Ijeoma has independently deduced it from the overdue taking | The household, the crown, and Emenike, who does not know his sister's proof of life has stopped mattering to the House |
| The Warden's ciphered question — does the hunt still need Ijeoma alive, or may the House close the account (Ep101) | The Warden only; the message is in transit | Mfoniso has not yet received it; no one in Idoro or Udo suspects a clock is now running on Ijeoma's life |
| Ijeoma is planning her own escape (Ep101) | Ijeoma only | Everyone — including the search party coming for her and the House holding her |
| The Factor's loyalty has begun to crack (Ep101) | The Factor only (and the audience) | The Warden believes his objections are still merely professional |
| Mfoniso's lineage tie to the hunter who took the presence's ground (Ep82) and her second thread to her teacher (Ep83) | The household and both powers | Mfoniso does not know they know |
| The search party's true purpose and departure (Ep99-100) | The household, the crown | Mfoniso — unless a future episode decides she saw them leave from her western ridgeline (Ep98); **decide this deliberately, on the page, before she next acts** |
| Nkiruka's archive record that stops mid-page (Ep94) | Nkiruka only | Eze Amadi and everyone else |
| Elder Maka's thin thread to the entity; Chibundu's identity; the presence's existence | The whole household (no secrets left inside it since ~Ep66) | The wider village knows Oso is feared ground, not what lives there; Ubani chose not to learn (Ep98) |

---

## 6. THE POWER SYSTEM

- The power binding the protagonist is **not** a generic floating game-menu.
  It is framed through real Igbo/Yoruba cosmology (abiku/ogbanje spirit-child
  belief and dibia divination) filtered through something ancient and hungry that
  has claimed him. System-style status/condition lines (as used in Episode 1)
  are permitted sparingly, for cold, clinical contrast against the warmth of
  the human scenes — never overused. Cap at 1–3 short system-style lines per
  episode, and only when something genuinely changes (a new ability, a new
  threat detected, a level/condition shift).
- The entity in Oso should stay ambiguous and unsettling for as long as
  possible. It is not simply "good" or "evil" — it is patient, transactional,
  and has its own agenda. Do not rush to explain it fully; every reveal about
  its nature should cost the protagonist something.
- Power growth must be earned through story events (grief, injustice, near-death,
  betrayal, sacrifice) — never handed over for free. Trauma is the currency
  of this system, mirroring the real history the story is built on.

---

## 7. HISTORICAL SKELETON (INTERNAL REFERENCE — NEVER SURFACE DIRECTLY)

Use these as structural/emotional templates for future arcs. Always
fictionalize completely — different names, different specific details,
different order of events if needed for pacing. The audience should never be
able to point to one episode and name the real event it's based on; they
should only feel that it rings true.

1. **A self-made ruler undone by a rigged summit** (Jaja of Opobo parallel) —
   a merchant-king lured into a trap under false promise of negotiation,
   exiled, dies before reaching home.
2. **Twin-killing law** (in progress, Episodes 1+) — the old law, the Evil-Forest
   equivalent (Oso), the abiku belief.
3. **Colonial-era segregation** (not literal apartheid) — reserved
   districts, unequal status between colonizers/administrators and locals —
   available as a mid-series arc about a divided city.
4. **Oil exploitation of the delta** — ongoing backdrop (Oji Delta),
   foreign Houses draining wealth while poisoning the people who live there.
5. **A truth-telling scribe killed by a cursed/trapped parcel** (Dele Giwa
   parallel) — a journalist or court scribe who exposes the crown's secrets,
   killed by a boobytrapped object days after being questioned by palace
   security.
6. **An elder executed for defying foreign exploitation despite international
   pleas, causing a total severing of foreign ties** (Ken Saro-Wiwa/Ogoni
   parallel) — a nonviolent activist-elder hanged despite outside kingdoms
   intervening; the aftermath permanently isolates the crown from allies.
7. **An elected leader annulled and imprisoned until death** (MKO Abiola
   parallel) — a leader who wins a free and fair succession contest, is
   denied the throne by the military/palace guard, dies in custody weeks
   before a promised release.
8. **A reformist ruler killed by his own guard amid heavy foreign interest in
   his fall** (Murtala Mohammed parallel) — ambiguous whether outside powers
   orchestrated it or merely wanted him gone; keep this ambiguity, don't
   resolve it definitively.
9. **An outspoken prisoner who becomes the eventual ruler** (Obasanjo
   parallel) — likely endpoint for the protagonist's arc: imprisoned for
   defiance, released after the old regime falls, ascends to the throne.

Suggested rough order across the 1000 episodes: (2) runs from Episode 1;
weave in (4) as constant backdrop; build toward (5), (6), (7), (8) as major
mid-to-late arcs; (1) can surface as a flashback/legend told to the
protagonist; (9) is the long-term destination for the finale arc. Adjust
freely for pacing — this is scaffolding, not a rigid outline.

---

## 8. LITERARY/CULTURAL TEXTURE TO DRAW ON

(Researched from Chinua Achebe's novels and Igbo/Yoruba folklore — used for
authentic texture, never quoted or copied.)

- **Things Fall Apart**: the Evil Forest / twin-abandonment custom (our
  Oso), the concept of *chi* (personal guardian spirit/fate — useful
  framing for "why do I have this power"), the *osu* outcast caste (useful
  for how a village might treat someone marked as cursed), the Week of Peace
  (a sacred truce period that can be dramatically violated later), a beloved
  ward sacrificed on an oracle's word by the very man who raised him as a son
  (powerful template for a future betrayal/sacrifice arc — do not copy the
  specific character or scene, use the shape of it).
- **Ogbanje/Abiku belief**: spirit-child dies and returns to torment its
  family; a *dibia* works to break the cycle through ritual and divination.
  This is our core supernatural mechanic (see Section 6).
- **A Man of the People / Anthills of the Savannah**: Achebe himself used a
  fictional stand-in country ("Kangan") to tell Nigeria's political story —
  validates our approach. Useful character templates: a dictator known only
  by title, a newspaper editor critical of the regime who is eventually
  killed by it, a palace official torn between loyalty and conscience.
- Use these as **flavor and structure**, never as text to lift. Everything
  must be reworded and reimagined in our own world.

---

## 9. DOCUMENT FORMAT

- US Letter page size, 1-inch margins, body font Georgia 12pt, 1.5 line
  spacing.
- Title page elements: series title (THE DARK RISE), book/arc subtitle,
  episode number, episode title.
- Bold, all-caps for any in-world "system" status lines.
- Per Section 3.5, episode numbers and titles must not appear in the
  narration body — they belong in the file name and title page only.
  The story ends on its hook, with no spoken "End of Episode" marker.

---

## 10. BUILD & VERIFY CHECKLIST (every episode, no skipping)

1. Draft the episode in a Node/docx script (see prior build scripts as
   template).
2. Run word count check:
   ```
   pandoc -t plain The_Dark_Rise_Episode_##.docx | wc -w
   ```
   Confirm word count falls in **1,550–2,150 words** (11–15 min at
   130–150 wpm). Adjust and rebuild if outside range.
3. Convert to PDF and rasterize 1–2 pages to visually confirm formatting
   before delivery.
4. Update Section 5 (Living Name Registry) with any new names/status changes
   — **replace** the affected character's current-status sentence(s), don't
   append a new history clause (see Section 5's maintenance rule).
5. Update the CHANGELOG (Section 11) with a one-line summary of the episode.
   If Section 11 has grown past ~20 entries, cut the oldest entries out and
   append them, unedited, to `ARCHIVE.md` under "ARCHIVED CHANGELOG" before
   adding the new one — keep Section 11 to roughly the most recent 15-20
   episodes.
6. Copy final .docx to `/mnt/user-data/outputs/` and deliver via
   `present_files`.
7. Commit and push to GitHub (see Section 12) — **do this at the end of
   every episode, without being asked.**

---

## 11. CHANGELOG

Keep a running one-line-per-episode log here so continuity can be checked
at a glance without rereading everything. **This section holds only the
active arc — roughly the most recent 15-20 episodes.** Everything older
is archived verbatim in `ARCHIVE.md` under "ARCHIVED CHANGELOG" (see that
header for its current range, Episodes 1-86 as of this writing); when this
section grows past ~20 entries, move the oldest ones there following the
same pattern (see Section 10, step 5).

**Note on dates:** the parenthetical dates on episode entries are the
scheduled Pocket FM release dates (per Section 4's schedule-ahead cadence),
not writing dates. Writing/commit dates live in git history and are weeks
to months earlier.

- **CLAUDE.md archive split (2026-07-13):** CLAUDE.md exceeded the
  150,000 character working-memory limit at Episode 78. Split the Living
  Name Registry and Changelog's older history out into `ARCHIVE.md`
  (lossless, verbatim). Section 5 now holds current-status-only entries per
  character with a maintenance rule against re-appending history; Section 11
  now holds only the active arc. Nothing was deleted — see `ARCHIVE.md`
  for the full archived record (registry history through Episode 78;
  archived changelog per its own header, growing as this section is
  trimmed).
- **Episode 87 — "The Name the Trap Caught" (2026-10-02):** Chidebe
  catches Emenike at the drop point with a fresh message already left
  for Mfoniso; Emenike does not run or lie once confronted, confirming
  the betrayal outright. Osadebe arrives from clearing Adaeku and the
  three walk back to the compound quietly rather than risk a public
  scene, passing Zara, who recognizes Emenike immediately and grieves
  before knowing his reason. The household absorbs the name with grief
  more than triumph; Ozoemena, cleared at last, mourns a friend rather
  than celebrating his own vindication, and Elder Maka counsels hearing
  Emenike's reason before judging him. Pressed by Amara, Emenike breaks
  down and confesses that the people holding his sister have forced his
  cooperation for two seasons, from the very first message. (On the page
  he never names his captors — "They have my sister" — and the household
  has still never heard the name "Ijoma Concern"; see Section 5.2.) The
  episode closes on Amara's cold new fear — not relief that the leak is
  found, but dread over how many other quiet debts like his might still
  be hidden inside Idoro's walls.
- **Episode 88 — "What the Traitor Traded" (2026-10-03):** A formal
  council hearing gives Emenike's full account: his sister Ijeoma was
  taken from a river town two seasons ago, and Ijoma Concern agents
  have coerced his cooperation since, proving her survival twice a
  season with a blue thread bracelet she has worn since childhood.
  When Elder Maka has him describe her captors' bearing, west and
  slightly south, the entity recognizes it as matching Elder Maka's own
  Episode 83 trace of Mfoniso's unknown second thread, suggesting
  Ijeoma may be held wherever Mfoniso herself answers to. Zara and
  Adaugo each recognize a version of their own isolation in Emenike's
  ordeal; Ozoemena speaks in his defense, asking the household to judge
  fear and love rather than simple malice. Osadebe tempers the hope
  with practicality, and the episode closes on the deadline Emenike
  reveals: Mfoniso expects contact at the drop stone within two nights,
  the longest silence would ever plausibly go unpunished, forcing a
  decision the household is not yet ready to make.
- **Episode 89 — "A Trap With No Leak Left" (2026-10-04):** The
  council rejects forging a message in Emenike's hand as too risky and
  instead leaves the drop stone empty for the first time in two
  seasons, ringing the market's edge with hidden soldiers under Chidebe
  and Osadebe, betting Mfoniso will come herself to learn why. The
  household spends the tense hours preparing; Kene unconsciously traces
  another spiral in the dirt, unsettling Zara, and Adaugo and Elder
  Maka discuss what comes next if the ambush succeeds. The episode
  closes on Mfoniso's own side: her informant's first-ever missed
  contact reads to her not as chance but as proof of compromise, and
  recalling her teacher's warning about a guardian old enough to
  remember being hunted, she rejects investigating the drop point
  entirely and instead decides to strike the family directly that same
  night, bypassing the ambush laid for her completely, patience finally
  spent.
- **Episode 90 — "The Confrontation" (2026-10-05):** With most soldiers
  deployed to the market ambush, Mfoniso breaches the thinly guarded
  compound directly and seizes Adaugo by the anchor thread. Elder Maka
  places herself unarmed between them; Emenike, freed to act for the
  first time since his exposure, throws himself into Mfoniso's path
  with a soldier's spear and is struck down, buying the household
  perhaps three seconds at the cost of a deep wound to his side.
  Chibundu, feeling the household's terror through their connection,
  tells the entity "now, whatever it costs," and it breaks three
  centuries of pure restraint to reach directly at Mfoniso for the
  first time in the story rather than merely advise. Mfoniso releases
  Adaugo and flees, wounded and shaken to have finally met a guardian
  old enough to remember being hunted meeting her in the open, exactly
  as her teacher once warned would happen eventually. The episode
  closes on Amara pressing both hands against Emenike's spreading wound
  in the compound dirt while, in Oso, the entity's reach snaps back
  into total silence, leaving Chibundu unable to tell whether it will
  answer him again.
- **Episode 91 — "What the Confrontation Cost" (2026-10-06):** Zara
  fights through the night to keep Emenike alive while Amara stays at
  his side, forgiving his betrayal fully once she understands what his
  sacrifice meant. Ozoemena and Adaugo each sit with him in turn;
  Chidebe and Osadebe reconstruct the failed ambush, naming plainly
  that pulling every soldier to the market was the very choice that
  left the compound open. In Oso, Chibundu keeps vigil through hours of
  total silence until the entity finally answers near dawn, badly
  weakened, admitting it does not know if it could reach that far again
  or what the act cost Oso itself, and conceding it has called its own
  restraint wisdom for three centuries without ever being tested
  closely enough to know if that was true. Chibundu orders it to rest,
  the first time he has ever spoken to it that way. The episode closes
  on Emenike's fever breaking toward survival and on Amara's unresolved
  fear that the household bought this single dawn with a debt whose
  size, and whose cost to people who never asked to stand in Mfoniso's
  way, none of them yet understand.
- **Episode 92 — "The Reckoning" (2026-10-07):** Elder Maka examines
  Adaugo's anchor thread in daylight and finds it gone quiet, likely
  overloaded past repair by the entity's direct intervention — a hard
  won relief confirmed to Obi, Zara, and Kene. The full council hears
  Emenike's case with him present; Amara argues justice and mercy ask
  the same thing here, Ozoemena seconds her, and Chidebe takes personal
  responsibility for not seeing the coercion sooner, which Emenike
  refuses to let him share. The council reinstates Emenike as a soldier
  under a season of supervised trust, with household resources
  committed to finding Ijeoma once he recovers; Osadebe sends Udo the
  most urgent report of his career, disclosing plainly that Oso's
  guardian has now acted directly for the first time in three
  centuries. The episode closes on Mfoniso, tending her wounds beyond
  Idoro's boundary, deciding this setback cannot be explained in a
  message left under a stone and setting out for the first time in her
  career to deliver her account to the Warden in person.
- **Episode 93 — "What the Concern Decides" (2026-10-08):** Mfoniso
  delivers her account in person at the Ijoma Concern's disguised
  headquarters. The Warden, visibly shaken by the description of the
  entity meeting Mfoniso directly, reveals the guardian ground debt has
  passed through four keepers before her rather than being her own
  personal grievance. The Factor, present for the account, makes his
  sharpest objection yet, arguing the House cannot keep spending lives
  on an inherited grudge; the Warden overrules him a third time and
  permanently relieves him of any further say in the operation,
  committing resources beyond anything spent on the hunt so far. Led
  out through the compound's inner grounds, Mfoniso glimpses a young
  woman in a heavily guarded courtyard whose watchfulness matches every
  detail she has absorbed of Emenike's sister without ever seeing her
  face, confirming that Ijeoma is held at this same headquarters. The
  episode closes on Mfoniso saying nothing of the discovery to anyone,
  filing it away as leverage she has not yet decided how to spend.
- **Episode 94 — "The Crown's Reckoning" (2026-10-09):** Osadebe's
  report reaches Udo and Eze Amadi's council convenes within the hour.
  Nkiruka confirms Oso's guardian has never before acted rather than
  warned in three centuries of records; Ejikeme, humbled since Episode
  65, asks a third time for a survey of Idoro's land, this time as
  protective obligation rather than trade interest, and Eze Amadi
  grants it alongside a formal crown investigation into which trading
  House sponsored the informant's coercion and a doubling of Idoro's
  permanent garrison. Nkiruka warns that moving against the sponsoring
  House risks provoking Mfoniso into striking again before she is
  ready; Eze Amadi accepts the risk as smaller than standing still. The
  episode closes on Nkiruka alone in the archive, finding a centuries
  old record of a border village that once discovered a coerced
  informant exactly as Idoro did — whose account simply stops mid
  record, unresolved, pages lost or removed, leaving her with a private,
  unshared fear that Idoro's own story might be heading toward the same
  silence.
- **Episode 95 — "What the Quiet Held" (2026-10-10):** The informant
  and confrontation arc closes on a quieter note of recovery. Emenike
  walks unassisted for the first time and declines an early end to his
  supervised season, preferring trust earned slowly; Elder Maka
  advances Adaugo to her next rite. Kene's unbidden spiral has gone
  still rather than resolved, and Zara feels the first faint,
  untrusted flicker of her muffled gift returning; Elder Maka calls
  both "not the same as gone." The entity speaks daily again, thin but
  present, mending slowly since Episode 90. The episode closes on the
  crown survey party's measuring lines creeping toward Oso's tree line
  for the first time in three centuries of outside eyes never reaching
  that close; the entity, alert but uncertain, tells Chibundu it does
  not yet know whether a secret kept this long should fear its first
  honest look from the one power capable of someday deciding not to
  keep it — a quiet dread opening the next arc rather than closing this
  one.
- **Episode 96 — "What the Surveyors Saw" (2026-10-11):** The crown
  survey's lead surveyor, Ubani, notices Oso's tree line behaves
  unnaturally — birdsong stopping at an exact, repeated point, canopy
  moving in wind the undergrowth never feels — and records it privately
  rather than officially. Chidebe and Amara each try, without lying
  outright, to steer him away from the ground; his second, Ude, warns
  him gently it is tied to old grief rather than mere superstition.
  Ubani respects all of it and remains unmoved. In Oso, the entity
  warns Chibundu that an honest man is harder to deceive than a
  dishonest one, while the presence notes the truer danger is not
  whether Ubani sees something but what he does afterward. The episode
  closes on Ubani informing Chidebe, gently but immovably, that he will
  walk Oso's boundary himself at first light to complete an honest map,
  leaving the household with no way to stop him without confirming the
  very secret they are trying to protect.
- **Episode 97 — "The Line He Crossed" (2026-10-12):** Ubani walks into
  Oso alone at first light while Chidebe and Ude wait at the boundary.
  The entity, too weak for direct confrontation and unwilling to spend
  strength on a man who means no harm, chooses not to manifest at all,
  instead letting Oso's undisguised ancient stillness reach him so his
  own fear does the rest; the presence cautions it to be sure this
  restraint is wisdom and not merely the shape of low strength. Ubani
  experiences a formless, escalating dread with no monster or voice to
  name, loses count of his own steps, and retreats badly shaken but
  unharmed, apologizing to Chidebe for calling the village's fear mere
  superstition. Amara's comment that "it let you leave" tips him off
  that she knew something in advance, which she neither confirms nor
  denies. The episode closes on Ubani, walked back to the market by
  Ude, still undecided what shape the truth of what he felt should take
  once it reaches the crown's own hands.
- **Episode 98 — "What They Chose to Tell Him" (2026-10-13):** Amara
  and Elder Maka decide to give Ubani a true but incomplete account
  rather than continued silence: the old law's abandonment ground and
  the three centuries of real grief soaked into it, without ever naming
  what lives beneath that grief. Ubani accepts it readily since it
  matches what he felt closely enough, and marks Oso in his official
  crown report as consecrated grief ground excluded from development,
  protecting the household's deeper secret without ever being told it.
  The entity, watching from Oso, expresses something like admiration
  that the family solved this danger with careful honesty rather than
  force or sacrifice. The survey departs with its work genuinely
  finished. The episode closes on an interlude with Mfoniso, fully
  healed and newly resourced by the Warden, resuming her surveillance
  of Idoro from a distance and finding it transformed — a far larger
  garrison, staggered patrols, and crown surveyors — forcing her to
  rebuild her understanding of the village from the ground up before
  deciding what her new resources actually let her attempt.
- **Episode 99 — "The Search They Owed Him" (2026-10-14):** Emenike
  finally asks the household when it will search for Ijeoma, and Amara
  admits crisis after crisis has delayed a promise that was never fair
  to delay; Ozoemena holds the household to it. Osadebe secures formal
  crown support under the Ep94 investigation's authority, and Ubani's
  survey maps give the search its first honest picture of the western
  ground beyond guesswork. Chidebe's objection that Emenike isn't yet
  strong enough is overruled by Emenike's flat refusal to be protected
  from the one thing he still has a right to insist on. A party forms —
  Osadebe, Emenike, soldiers Ifeanyi and Okonjo — to depart within the
  week. Amara raises the possibility the search finds the Ijoma
  Concern's true headquarters rather than Ijeoma alone. The episode
  closes on Elder Maka carrying the household's request for aid to Oso:
  the entity offers little, but the presence goes very still at the
  bearing (west, slightly south), admitting it recognizes the direction
  — not a place, a direction it has not let itself think about in three
  centuries — and asks only to be told what ground the search party
  finally reaches, the first visible sign of hope Chibundu has ever
  sensed in it.
- **Episode 100 — "West of Everything Known" (2026-10-15) [MILESTONE]:**
  The search party departs Idoro at dawn; Amara and Elder Maka each
  send Emenike off with a plea and a blessing, and Zara walks the first
  stretch of road with them, her flickering gift finding nothing to
  warn of before she turns back at the old boundary stone. Three days
  west, past the edge of Ubani's survey maps, the land itself grows
  strange — Ifeanyi notices ground that feels "walked around" rather
  than merely empty — and Osadebe deliberately takes on part of
  Emenike's emotional burden so he can finally sleep. In Oso, Chibundu
  presses the presence to stop protecting him from the truth, and it
  finally names its three century old loss plainly for the first time
  ever, including to the entity: its own guardian ground lay exactly
  along the bearing the search now travels, and it has never learned
  what became of that ground or the people it once protected there. The
  entity tells the presence it has never heard it speak this openly of
  its grief in their entire acquaintance. The episode closes on the
  search party making camp at the edge of unnamed country, unaware they
  may be walking toward two answers at once — Ijeoma's fate, and the
  presence's oldest unhealed wound.
- **Continuity & audio-clarity maintenance pass (2026-07-16):** Global
  rename of the boundary tree: "ak-pu" → **"iroko"** across all one hundred
  episode files (eighty occurrences in fifty one files), all build scripts,
  ARCHIVE.md, and this file — the old spelling was hyphenated (violating
  Section 3.4) and unreliable in TTS narration. Added Section 5.1
  (audio confusable-name rules: "the Concern" in narration, never bare
  "Amadi" near Amara, Chibundu/Chidebe role tags, Adaeku retired) and
  Section 5.2 (who-knows-what dramatic irony ledger). Corrected stale
  bookkeeping: archive-split note now says registry history through
  Episode 78 and changelog through Episode 83 (was "63/63");
  ARCHIVE.md's changelog header corrected from "1–63" to "1–83" and its
  tail note de-staled; registry column header updated to "as of Episode
  100"; Section 8's "Ohia Nso" corrected to "Oso"; Section 12's push
  target corrected from "main" to "master" (the actual branch);
  changelog dates labeled as scheduled release dates; Episode 87's entry
  corrected to reflect that the household never hears the captor House's
  name on the page. No story content changed beyond the tree's name.
- **Episode 1 TTS pacing restructure (2026-07-17):** Rebuilt Episode 1 to
  eliminate unnecessary narration pauses reported in the audio: merged
  single-sentence paragraphs into full beat paragraphs (one hundred twenty
  two body paragraphs down to eighty one, standalone lines now reserved for
  dramatic peaks), replaced the thirteen empty spacer paragraphs with
  spacing-before scene breaks (zero empty paragraphs in the docx), removed
  all em dashes, and added a tone cue to every dialogue line so the AI
  voice matches each speaker's emotion. Word count two thousand one
  hundred forty six, in range. Codified as Section 3.10; roll out to other
  episodes after the Episode 1 listen test confirms the improvement. No
  story content changed.
- **Episode 101 — "What She Is Worth" (2026-10-16):** The hostage clock
  starts. At the House's headquarters, the Warden cancels the bracelet
  proof runs — with Emenike discovered, proof of Ijeoma's life persuades
  no one — takes the guest's ledger line from the Factor, and leaves
  Ijeoma's fate explicitly undecided: the House keeps what it might
  still spend, not what it can only feed. The Factor, arguing in pure
  cost terms that bodies open accounts rather than close them, passes
  the guarded courtyard for the first time and recognizes he has signed
  two seasons of her keeping without ever reading the line as a person.
  Ijeoma, in her own viewpoint for the first time — nineteen, a cloth
  trader's daughter who counts everything — deduces from the overdue
  fifth taking exactly what it means, concludes nobody feeds a witness
  forever, and quietly begins studying guards, watches, and the wall's
  one bad corner: done waiting. Four days west, the search party finds
  a centuries old boundary stone laid deliberately face down, a spiral
  cut into its buried face; that night Chibundu dreams the stone
  standing before living ground, and the presence confirms its people
  cut it — hunters lay a taken ground's marks face down so the land
  forgets its own name — and that the lost ground lies two days ahead
  of the search. The episode closes cold on the Warden's ciphered
  question traveling toward Mfoniso: does the hunt still require the
  guest kept breathing, or may the House close the account.

---

## 12. GIT / GITHUB WORKFLOW

At the end of every episode:
```
git add -A
git commit -m "Episode ##: [short title] — [one-line summary]"
git push origin master
```
Never batch multiple episodes into one commit. Never push without first
completing the Section 10 checklist. If a push fails (auth/remote issue),
stop and flag it — don't silently skip it.
