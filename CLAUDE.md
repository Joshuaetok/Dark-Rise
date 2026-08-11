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

### 3.10 Paragraph Pacing and Dialogue Tone (added 2026-07-17; applied to all episodes, 1-101)
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
| Amara | Mother of the twins | Alive, Idoro, full council seat. Knows the entity, the presence, Chibundu's identity, and Elder Maka's condition — no secrets left within the household. Current thread: read Osadebe's courier report to the full council and ordered word sent to Udo by the fastest rider available, unwilling to let the crown learn only half of what the search party now knows (Ep107). |
| Obi | Father of the twins | Alive, Idoro. Fully present and active partner to Amara in every crisis since Episode 6. Current thread: sat quietly with the recovering Emenike, who declined an early end to his season of watching, preferring trust earned slowly to trust granted out of pity (Ep95). |
| Zara | Village midwife | Alive, living mostly at Amara's compound. Delivered both twins; carries a dormant blood thread the presence (not the entity) has used to reach her since her Episode 42 return. Her borrowed sense of danger has been the family's best early warning system since Episode 69. Current thread: walked the first stretch of road with the search party as promised, her flickering gift finding nothing to warn of; turned back at the old boundary stone (Ep100). |
| Adaugo | Elder Maka's surviving daughter | Alive, Idoro. Fully reconciled with her mother since Episode 66. The anchor thread Mfoniso planted on her wrist (Ep80) appears permanently inert since Ep90. Current thread: named the council's unspoken stakes aloud, that the household now fights on behalf of every name the hillside holding room ever contained, drawing directly on her own memory of what it felt like to belong to Mfoniso's ledger for a moment (Ep107). |
| Elder Maka | Elder priestess | Alive, Idoro, restored to a respected advisory council seat (not sole authority over the old law, stripped Ep19). Secretly carries her own thin thread to the entity since the Episode 12 binding rite (now openly known to the household and village). Current thread: blessed the search party's departure with an old protective rite and gave Emenike a plaited cord to carry (Ep100). |
| Ozoemena | Mid ranking Idoro elder | Alive, Idoro. Humbled, trusted council member who serves through labor since his own disastrous rite killed the dibia (Ep26). Current thread: held the household to its promise to search for Ijeoma, arguing a harder promise kept only when convenient has not truly been kept at all (Ep99). |
| Kene | Surviving firstborn twin | Alive, toddler, Idoro. Original twin thread to the entity severed (Ep12); knows he has a brother (told Ep66); survived Mfoniso's first abduction attempt (Ep70), saved when the presence reached beyond Oso's ground for the first time. Began tracing an unbidden spiral in the dirt (Ep76) — the same shape both old powers have used on Zara — raising fear the presence's rescue left a second, uncut thread in him. Current thread: the spiral tracing has gone still rather than resolved; Kene reports it "does not feel like it wants me to" today, unresolved per Elder Maka's assessment (Ep95). Family continues watching rather than attempting a severing rite. |
| Chibundu | Abandoned secondborn twin / protagonist ("the one whom the presence carries") | Alive, Oso. Named by the presence through Zara (Ep47); reunited with Amara (Ep50); survived a trading House ambush at that reunion; has twice refused the trading House's partnership offer (once in his own voice, once when the presence seized his voice to refuse it for him, Ep60-61) and extracted a narrower promise from the presence (it will not take his voice again except to save his life). Current thread: dreamed the toppled boundary stone as it stood three centuries ago — upright, ochre filled, living ground beyond it — the same night the search party found it; woke to the presence's confirmation and now knows the party is two days from the lost ground. Deliberately did not promise the presence the answer would be bearable, honoring its request to stop being protected from the truth (Ep101). |
| Eze Amadi | King, Kingdom of Ijendu, throned at Udo | Alive, Udo. Aware of the entity and, since Ep65, the presence as a second distinct power. Has permanently assigned Osadebe to Idoro and stationed Chidebe's garrison there. Current thread: absorbed Osadebe's report of the entity's direct action and the coerced informant, and authorized a formal crown investigation into trading House sabotage, a doubled permanent garrison for Idoro, and Ejikeme's long refused land survey, reframed as crown obligation rather than trade measure (Ep94). |
| Nduka | Crown river-road intelligence agent | Alive. Minor, not currently active — carried the first report of Idoro's unraveling to Udo (Ep24). |
| Nkiruka | Keeper of the crown's old rites and records, Udo | Alive. Holds the crown's only historical archive on prior encounters with old powers. Revised her reading (Ep65) to recognize two separate powers rather than one growing bolder. Found a centuries old record of a border village that discovered a coerced informant exactly as Idoro did, whose account then stops mid record with no resolution (Ep94); still kept private from Eze Amadi. Current thread: found a small spiral mark cut into the record's gutter, matching the mark from Osadebe's own report, and now reads the record's unfinished ending as a deliberate warning rather than lost pages; copied it in full and is undecided whether to send it west to the search party (Ep103). |
| Ejikeme | Overseer of the crown's delta trade concessions, Udo | Alive. Won authorization for the crown survey of Idoro's land he had twice been refused (Ep94), granted as crown protective obligation rather than a trade measure, though he could not promise Nkiruka the crown would keep that distinction once exploitable ground was found. Dispatched to begin survey preparations within the week. |
| Osadebe | Captain of Eze Amadi's personal service, permanently assigned to Idoro | Alive. The crown's primary eyewitness and liaison to Idoro. Leads the Ijeoma search party (himself, Emenike, Ifeanyi, Okonjo), sketching fresh maps each evening past the edge of Ubani's survey. Current thread: found a House maker's mark burned into the hillside chamber's binding cloth, identical to the seal Emenike recognizes from the Concern's drop point messages, confirming the search for the presence's lost people and the search for Ijeoma are one mission. Pressing on west past the lost ground for the first time (Ep106). |
| Chidebe | Captain, commands the crown garrison at Idoro | Alive. Disciplined, trusted by Osadebe. Current thread: argued Emenike was not yet strong enough for the Ijeoma search and was overruled by Emenike's own flat refusal to be protected from the one thing he still has a right to insist on (Ep99). |
| Ikwuano | Keeper of the crown's scattered intelligence reports, Udo | Alive. Traced the trading House's court sponsor and confirmed its interest in Idoro predates its public approach by years. Not currently central to the active plot thread. |
| *(unnamed dibia)* | Village diviner/healer; carried the secondborn to Oso | **Deceased (Episode 26).** Was the entity's first mouthpiece; killed when Ozoemena's borrowed rite against him failed and the entity struck him down mid final message. |
| *(unnamed entity)* | Ancient presence beneath Oso, bonded to Chibundu | Active, still badly weakened but mending. Three centuries old, patient and transactional; broke three centuries of pure restraint to act directly against Mfoniso (Ep90). Current thread: gently turned Chibundu's own argument for the presence's limits back around, telling the presence it could not have walked a bearing it can barely reach past Oso's borders even now (Ep105). |
| *(unnamed presence)* | Older power beyond Oso's outer borders, reaches Chibundu through dreams and has spoken through Zara | Active. Named Chibundu (Ep47). Once lost a guardian ground centuries ago to a hunter using the exact tactic Mfoniso now uses (take the people the guardian loves, wait, strike slowly) — revealed Ep67. Broke its three century habit of never overspending its strength to save Kene directly (Ep70), at a cost it still hadn't finished paying as of Ep72-73; further spent by tearing itself out of Zara in Ep82. **Major reveal (Ep100):** confirmed under Chibundu's direct pressure that its own lost guardian ground lay exactly along the bearing west and slightly south of Oso. Current thread: learned through the search party's find that its people were taken and moved rather than slaughtered where they stood; has spent three centuries mourning the wrong story, and now does not know where they were taken to, by whom, or whether any survived to be found (Ep105). |
| Uduak | Market trader, former trading House informant | Alive, held pending Udo's judgment since his confession (Ep53). Not currently active in the plot. |
| the Warden | Ijoma Concern's keeper of old and dangerous knowledge | Active. Authorized Mfoniso's second attempt, against Zara directly (Ep74), overruling the Factor's objection. Revealed the guardian ground debt is inherited across four keepers before her rather than her own personal grievance; permanently relieved the Factor of any further say in the operation and committed resources beyond anything spent on the hunt so far (Ep93). Current thread: canceled the bracelet proof runs outright (no one left to persuade), took the guest's ledger line from the Factor, left Ijeoma's fate explicitly undecided between asset and expense, and sent a ciphered query to Mfoniso asking whether the hunt still requires the guest kept breathing or the House may close the account, now one day from delivery (Ep101-102). |
| Mfoniso | Ijoma Concern's retained guardian hunter | Active — the story's current antagonist. Failed to abduct Kene (Ep70) when the presence intervened directly; pivoted to a slow, undetectable working against Zara's borrowed senses instead, confirmed succeeding by Ep77-78. Confirmed as trained in or descended from the same hunting lineage that took the presence's guardian ground three centuries ago (Ep82); revealed to be carrying her own second thread to whoever trained her (Ep83). Breached Idoro's compound directly, seized Adaugo, and struck down Emenike, then fled wounded and shaken when the entity met her in the open for the first time (Ep90). Delivered her account to the Warden in person and received resources beyond anything committed so far, plus confirmation of Ijeoma's location at the Concern's headquarters (Ep93). Current thread: walking the river road south, recalled two old training lessons from her teacher, that the lineage's taken guardian grounds were "resettled" rather than the people left dead, and that only one guardian in the lineage's history ever refused to run from the tactic, a story her teacher always broke off at that word. That night felt a held tension go slack somewhere along her second thread to her teacher, a sensation she has never felt before, and now privately suspects the unnamed guardian was the same one that met her at Idoro; resolved to ask the Warden what became of the resettled people before she answers the Warden's own question (Ep108). |
| Chiazor | Trading House's formal sponsor at Udo | Alive. Revealed a senior House figure was already traveling toward Idoro before the ambush. Not currently central to the active plot. |
| the Factor | Senior trading House figure, Ebiere's direct superior | Alive, permanently removed from any further say in the Mfoniso operation. Objected three times now (Ep64, Ep74, Ep93) to escalating the hunt against Oso's guardian, each time overruled; his final, sharpest objection after learning of the entity's direct intervention led the Warden to relieve him of authority over the operation entirely (Ep93). Current thread: found the mud and disturbed ground at the wall's weak corner the morning after Ijeoma's failed escape attempt, read it correctly, and quietly scuffed it smooth rather than report it, his second small act of withheld loyalty since Ep101 (Ep109). |
| Ebiere | Trading House field agent who orchestrated the boundary ambush | Whereabouts unknown since Ep53; publicly disowned by the Factor as a rogue agent. |
| Effiong | Young crown soldier who sold patrol schedules for coin, enabling the ambush | Confessed (Ep52). Not currently active in the plot. |
| *(unnamed)* | Elder Maka's returned son | Deceased. Her own abandoned twin, returned wrong at age eight, killed three people including her husband; she killed him herself. Origin of her severity toward the old law. |
| Emenike | Soldier in Chidebe's garrison at Idoro | Alive, on the road with the Ijeoma search party, three days west of Idoro. Served under Chidebe since before the boundary ambush (Ep51); confirmed as Mfoniso's informant (Ep87), coerced for two seasons by threats against his sister, Ijeoma. Threw himself between Mfoniso and Adaugo during her direct attack on the compound (Ep90). Carries Elder Maka's protective cord and Amara's plea to come home either way. Current thread: recognized the branded mark on the hillside chamber's cloth as the same seal used on messages left for him at the drop stone, confirming the House holding Ijeoma is the same lineage that emptied the lost ground. States plainly the road is longer than he thought but he is not walking any less for knowing it (Ep106). Does not know Mfoniso confirmed Ijeoma's location (Ep93), that the Warden has stopped the bracelet proof runs and is asking Mfoniso whether Ijeoma still needs keeping alive, nor that the Warden's ciphered question is now within a day of reaching Mfoniso's hand. |
| Ijeoma | Emenike's younger sister | Alive, confirmed held at the Ijoma Concern's disguised headquarters downriver, seen briefly by Mfoniso in a heavily guarded inner courtyard (Ep93), confirming the bearing (west, slightly south) reported in Ep88. Taken from a river town by the Concern's agents two seasons ago while trading cloth for their mother; held as leverage to coerce Emenike's cooperation as an informant. Introduced in her own viewpoint for the first time (Ep101): nineteen, a cloth trader's daughter who counts everything, watchful and deliberate. Current thread: made her first real escape attempt, using her now approved laundry duty and the eastern gate guard's habitual gap to climb the wall's weak corner alone at night. Reached the top and found the far side is unreadable black water rather than open ground, and chose a controlled retreat over a blind drop. The guard returned to his post in time to see her walk back and has said nothing so far (Ep109). Does not know a search party is now on her House's own trail west, nor that the Warden has asked Mfoniso whether she still needs keeping alive. Idoro's household does not yet know her exact location has been confirmed. |
| the guard | Unnamed soldier posted at the Concern headquarters' eastern gate | Alive. His habitual, unpunished gap in the gate watch is the timing Ijeoma has built her escape planning around since Ep102. Current thread: caught Ijeoma returning from her failed climb at dawn and chose not to report her, telling himself it was too small a thing to matter; privately, an unfinished thought about a sister of his own, sold before he ever wore House colors, surfaces and is left deliberately unexamined (Ep109). First thread of a possible inside ally; motive not yet confirmed even to the audience. |
| Adaeku | Soldier in Chidebe's garrison at Idoro, quietest of the six informant suspects | Alive. Cleared in practice, if not yet formally: paired with Emenike on the same false route, but his own night proved ordinary — a plain meal alone and sleep, watched the whole while by Osadebe (Ep86). |
| Ubani | Lead surveyor, crown survey party at Idoro (Ep94's authorized survey) | Alive, survey work concluded. Careful, observant, professionally honest; fifteen years' experience surveying disputed and unusual ground. Walked Oso's boundary alone (Ep97) and encountered an overwhelming, formless dread with no concrete cause he could name. Current thread: accepted Elder Maka's true but incomplete account of Oso as the old law's abandonment ground and grief-soaked site; marked it consecrated ground excluded from crown development in his official report, protecting the household's deeper secret without ever being told it, and departed Idoro with genuine respect for what he chose not to dig further into (Ep98). |
| Ude | Ubani's second on the crown survey, carries the measuring chain | Alive. Grew up two villages from Idoro; knows Oso's reputation but is cautious about saying so to a crown official. Warned Ubani gently that the ground is tied to old grief, not merely superstition (Ep96), which helped prepare him to accept Elder Maka's account without much resistance (Ep98). |
| Ifeanyi | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Grew up hunting; first to read the land's wrongness — game trails bending in wide curves around nothing (Ep101). Current thread: identified restraints and handling tools among the hillside chamber's stores, and noted the shelf dust was too thin for three centuries, proof the room is still kept ready (Ep105). |
| Okonjo | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Found the toppled spiral boundary stone an hour before dusk on the fourth day west (Ep101). Current thread: found the hillside's concealed door half hidden under deliberately grown vine, and was visibly troubled by how close the chamber sits to the ruined square below (Ep105). |

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

### 5.2 WHO KNOWS WHAT — dramatic irony ledger (as of Episode 109)

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
| Ijeoma made a real escape attempt and reached the top of the eastern wall before retreating rather than drop blind into unreadable water (Ep109) | Ijeoma, the eastern gate guard (saw her return), the Factor (found and hid the physical evidence) | The Warden, Mfoniso, the household, and the search party coming for her |
| The eastern gate guard saw Ijeoma return from her climb and chose not to report her; the Factor found the disturbed ground the next morning and scuffed it smooth rather than report it either (Ep109) | The guard and the Factor, each unaware of the other's silence | Everyone else, including each other — neither man knows the other also chose not to report it |
| The Factor's loyalty has begun to crack (Ep101) | The Factor only (and the audience) | The Warden believes his objections are still merely professional |
| Mfoniso's lineage tie to the hunter who took the presence's ground (Ep82) and her second thread to her teacher (Ep83) | The household and both powers | Mfoniso does not know they know |
| Mfoniso's private suspicion that the one guardian her teacher's training story always broke off at, the single lineage conquest ever refused, is the same guardian that met her at Idoro's wall (Ep108) | Mfoniso only | The household, both powers, the Warden, and the search party have no idea she has begun drawing this connection |
| A tension along Mfoniso's second thread to her teacher went slack for the first time in her memory, the night she made camp south on the river road (Ep108); cause unrevealed | No one, including the narration | Mfoniso only knows something moved; she has no name or direction for it |
| The House holding Ijeoma is the same lineage that emptied the presence's lost ground three centuries ago, confirmed by a matching maker's mark (Ep106) | The search party | The household, the crown, Oso, the Warden, and Mfoniso (who already knows the lineage tie from her own training but does not know the search party has made this connection) |
| The search party's true purpose and departure (Ep99-100) | The household, the crown | Mfoniso saw a small four man band leave Idoro at a distance (Ep102) but filed it as routine patrol rotation — she does not know it was the search party, or what it is for |
| Nkiruka's archive record that stops mid-page (Ep94), now understood as a deliberate warning marked with the same spiral the search party found (Ep103) | Nkiruka only | Eze Amadi, the search party, and everyone else; she has copied it but not yet decided whether to send it west |
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
header for its current range, Episodes 1-100 as of this writing); when this
section grows past ~20 entries, move the oldest ones there following the
same pattern (see Section 10, step 5).

**Note on dates:** the parenthetical dates on episode entries are the
scheduled Pocket FM release dates (per Section 4's schedule-ahead cadence),
not writing dates. Writing/commit dates live in git history and are weeks
to months earlier.

- **Episode 1 TTS pacing restructure (2026-07-17):** Rebuilt Episode 1 to
  eliminate unnecessary narration pauses reported in the audio: merged
  single-sentence paragraphs into full beat paragraphs (one hundred twenty
  two body paragraphs down to eighty one, standalone lines now reserved for
  dramatic peaks), replaced the thirteen empty spacer paragraphs with
  spacing-before scene breaks (zero empty paragraphs in the docx), removed
  all em dashes, and added a tone cue to every dialogue line so the AI
  voice matches each speaker's emotion. Word count two thousand one
  hundred forty six, in range. Codified as Section 3.10. No story content
  changed. The Episode 1 listen test confirmed the improvement.
- **Episodes 2-10 TTS pacing pass (2026-07-17):** Rolled the Section 3.10
  fixes out to the next nine episodes after the Episode 1 listen test
  succeeded. All build scripts now use scene break spacing instead of
  empty spacer paragraphs (about one hundred spacer paragraphs removed
  across the nine files; every built docx verified to contain zero empty
  paragraphs) and lint for dashes, double spaces, and hyphenated words.
  Roughly fifty em and en dashes rewritten as periods or commas, with
  dialogue interruptions becoming single ellipses. Every bare quote
  gained a tone cue; Episode 3's rapid interrogation exchange and Episode
  9's confession exchange got per speaker attributions. All system status
  lines converted from typed all caps to sentence case (the caps run
  property keeps the page look) and given a one line herald in the
  entity's ledger voice, matching Episode 1. Episodes 2 and 3
  additionally had one liner paragraph runs merged into beat paragraphs.
  All nine word counts remain in range. No story content changed.
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
- **Episodes 11-101 TTS pacing pass (2026-07-17):** Completed the Section
  3.10 rollout across the remaining ninety one episodes, finishing the
  series-wide audit begun with Episode 1. All build scripts now use scene
  break spacing instead of empty spacer paragraphs (three hundred ninety
  four spacers removed; every built docx verified to contain zero empty
  paragraphs) and lint for dashes, double spaces, and hyphenated words.
  All forty four system status lines were converted from typed all caps
  to sentence case (the caps run property keeps the page look) and given
  a one line herald in the entity's ledger voice, matching Episode 1;
  the fifteen status lines in Episodes 35-50 that had been typed as
  plain body paragraphs were also restored to true system formatting.
  Six em dashes rewritten (dialogue interruptions became single
  ellipses, per the Episodes 2-10 pattern); one bare quote in Episode 77
  gained a tone cue; Episode 101, built with no scene breaks at all,
  gained four. Three spoken episode number references — Section 3.5
  violations the AI voice would have read aloud ("since Episode eighty
  two" in Episode 84's narration, "Episode ninety four's reckoning" in
  Episode 99's, "predates episode thirty six contact" in Episode 37's
  status line) — were rewritten in world. No story content changed.
  Known pre existing issue, deliberately not addressed in this pass:
  eighteen episodes (45, 48, 49, 64, 68, 71, 73, 74, 76, 86, 87, 89,
  90, 94, 96, 97, 98, 99) sit one to fifteen words under the 1,550
  word minimum and did so before this pass; fixing them means adding
  story content and should be its own deliberate pass. (Resolved by
  the padding pass in the next entry, same day.)
- **Word count padding pass (2026-07-17):** Resolved the shortfall
  flagged in the previous entry. Each of the eighteen episodes that had
  shipped one to fifteen words under the 1,550 word minimum gained one
  or two added sentences (thirteen to thirty three words each) inside
  an existing mid episode paragraph — atmosphere, sensory texture, or a
  small emotional beat in the episode's own voice. No closing hooks
  were touched, no new plot facts were introduced, and every addition
  follows the Section 3 audio rules. All eighteen now land between one
  thousand five hundred sixty two and one thousand five hundred
  seventy five words; the full series (Episodes 1 through 101) is now
  verified in the 1,550-2,150 range, lint clean, with zero empty
  paragraphs in every built docx.
- **Shared build module extracted (2026-08-06):** Ahead of the Episodes
  102-140 arc, pulled the ~350 lines of OOXML/docx helper code
  duplicated in every Episode 1-101 build script into a single
  `scripts/dr_build.py` module (`make_run`, `make_paragraph`,
  `build_docx`, `count_words`, `lint_content`, `build_episode`).
  Existing Episode 1-101 scripts are untouched. New episode scripts
  import the shared module and define only their content list, episode
  number, and title. See `docs/superpowers/specs/2026-08-06-episodes-102-140-arc-design.md`
  for the full arc design (Ijeoma captivity arc and the presence's lost
  guardian ground resolve as one converging thread across Episodes
  102-140; no new Section 7 skeleton arc introduced this block).
- **Episode 102 — "The Shape of Waiting" (2026-10-17):** Opens the
  Episodes 102-140 arc with three parallel watching threads. The
  search party, one day into the two the presence promised, finds an
  old path that stopped being walked all at once and a second,
  unexplored branch they choose to leave for now. Ijeoma studies the
  eastern gate's guard rotation with intent for the first time and
  finds a habitual gap in it, a possible door she has not yet decided
  how to use. Mfoniso, still rebuilding her read of a transformed
  Idoro from her western ridge, is unsettled by her own teacher's
  unexplained silence since the Episode 90 confrontation; this episode
  deliberately resolves the open Section 5.2 question of whether she
  saw the search party leave, she did, four days ago, and dismissed
  the four man band as routine patrol rotation, not the search. The
  episode closes cold: the Warden's ciphered question is one day from
  reaching Mfoniso's hand, and she still has no idea it is coming.
- **Episode 103 — "Ground That Remembers Feet" (2026-10-18):** Okonjo
  finds the first worked stone of a buried settlement wall; the search
  party spends the day uncovering a vanished town of hundreds and
  camps one day short of it, unsettled that its story seems to have
  been buried along with it. In Oso, the presence shows Chibundu a
  remembered evening from its lost street for the first time in three
  centuries, an ordinary night of firelight and a laughing child, and
  admits it no longer remembers all of its people's names. The entity
  reads the gesture as the presence taking Chibundu at his word about
  not wanting to be protected from the truth. In Udo, Nkiruka reopens
  her Episode 94 archive record and finds a spiral mark hidden in its
  gutter, matching the search party's own find, recontextualizing the
  record's unfinished ending as a deliberate warning rather than lost
  pages. She copies it in full, undecided whether to send it west.
- **Episode 104 — "What Grief Left Standing" (2026-10-19):** The
  search party reaches the presence's lost ground: a settlement
  preserved unnaturally intact, bowls still set in place, grass that
  will not cross a doorway. At its ruined square's heart they find a
  standing stone cut with a spiral far fresher than three centuries
  old, proof someone still tends it, and Osadebe orders camp made
  outside the clearing rather than within it. In Oso, Chibundu feels
  the presence's grief directly for the first time as the party enters
  its square; the presence admits it does not know whether it has been
  waiting for this moment or dreading it, and confirms, for the first
  time, that it was drawn away from its own ground before the strike
  centuries ago, the same tactic Mfoniso later used against Kene. The
  entity, in turn, offers the presence something close to comfort for
  the first time in their long acquaintance.
- **Episode 105 — "Not a Grave" (2026-10-20):** Working the clearing's
  edges rather than its dangerous heart, the search party finds a
  concealed chamber built into the hillside, still oiled and dusted,
  stocked with restraints and handling tools rather than bones.
  Emenike names it plainly, a holding room, not a grave, and draws the
  line to his sister's own captivity aloud. Osadebe privately suspects
  this bearing has been used for exactly this purpose more than once
  across three centuries. In Oso, the presence learns its people were
  taken and moved rather than killed where they stood, and must
  relearn, after three hundred years of mourning the wrong story,
  that the real question was always where they were taken and by
  whom.
- **Episode 106 — "One Mission Now" (2026-10-21) [Act 1 close]:**
  Osadebe returns to the hillside chamber alone at dawn and finds a
  House maker's mark burned into the binding cloth. Emenike recognizes
  it instantly, the same seal used on messages left for him at the
  drop stone. The search for the presence's lost people and the
  search for Ijeoma are, from this point, confirmed as one mission
  against one House lineage rather than two separate mysteries sharing
  a bearing. The party presses on west past the lost ground for the
  first time. Downriver, Ijeoma secures a plausible reason to be at
  the eastern wall during the guard's gap, laundry duty, after a
  servant girl offers to arrange it, and deliberately keeps the word
  escape out of her own planning, superstitious about naming a thing
  too early.
- **Episode 107 — "The Question She Will Not Answer by Courier"
  (2026-10-22) [Act 1 close]:** Osadebe's courier report reaches Idoro.
  The council absorbs the full weight of Episode 106's discovery;
  Adaugo names what it means for the household to now be fighting on
  behalf of every name the hillside chamber ever held, and Amara
  orders word sent to Udo by the fastest rider available rather than
  let the crown learn only half the picture. Downriver, the Warden's
  ciphered question finally reaches Mfoniso. Rather than answer by
  return courier, she decides, for reasons she is not yet ready to
  examine closely, to carry her answer to the headquarters in person,
  breaking off her surveillance of Idoro and turning south.
- **Episode 108 — "What Her Teacher Never Finished Telling Her"
  (2026-10-23):** On the river road south, Mfoniso's
  mind drifts to two old training memories: her teacher's account of
  the lineage's first guardian ground conquest, whose taken people
  were only ever called "resettled," and a later lesson in the tactic
  itself, taught with the flat admission that exactly one guardian in
  the lineage's history ever refused to run for it, a story her
  teacher always broke off at that word and never finished. That
  night, camped off the road, Mfoniso feels a tension along her second
  thread to her teacher go slack for the first time in her memory, an
  unnamed, undirected wrongness that leaves her unable to sleep. By
  morning she has privately begun to suspect the nameless guardian of
  her teacher's unfinished story and the one that met her at Idoro's
  wall are the same, and resolves not to answer the Warden's Episode
  107 question until she has asked one of her own first: what actually
  became of the people her lineage once resettled, and whether the
  House still keeps any record of where.
- **Episode 109 — "The Wall She Almost Cleared" (2026-10-24):** Ijeoma
  makes her first real escape attempt, using her newly granted laundry
  duty and the eastern gate guard's habitual gap to slip out of her
  holding room and climb the compound's weak wall corner alone in the
  dark. She reaches the top only to find the far side is unreadable
  black water rather than open ground, and makes the deliberate,
  characteristic choice to retreat rather than drop in blind. The
  guard returns to his post in time to see her walk back and says
  nothing, an unfinished thought about a sister of his own surfacing
  and going deliberately unexamined. At dawn the Factor finds the
  disturbed ground at the wall's corner, reads it correctly, and
  quietly scuffs it smooth rather than report it, his second small
  act of withheld loyalty since Episode 101. Neither man yet knows the
  other also chose silence. Closes on the shape of the secret itself:
  a girl who counts everything now knows the wall, and the man who
  guards it, can both be climbed.

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
