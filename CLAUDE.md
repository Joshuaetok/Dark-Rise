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
| Chibundu | Abandoned secondborn twin / protagonist ("the one whom the presence carries") | Alive, Oso. Named by the presence through Zara (Ep47); reunited with Amara (Ep50); survived a trading House ambush at that reunion; has twice refused the trading House's partnership offer (once in his own voice, once when the presence seized his voice to refuse it for him, Ep60-61) and extracted a narrower promise from the presence (it will not take his voice again except to save his life). Current thread: served as the unwilling conduit for the presence's first returned fragment of old strength, flooded with three centuries of raw grief and a single unexplained name; chose not to press the presence for who she was, and is left privately wanting to know more about her than the presence has yet been willing to give (Ep115). |
| Eze Amadi | King, Kingdom of Ijendu, throned at Udo | Alive, Udo. Aware of the entity and, since Ep65, the presence as a second distinct power. Has permanently assigned Osadebe to Idoro and stationed Chidebe's garrison there. Current thread: ruled out sending an open crown army after the search party (too visible a declaration against a foreign House whose court sponsor remains unidentified) and instead authorized a small, deniable detachment, ordering Chidebe at Idoro to choose and dispatch the men himself (Ep118). |
| Nduka | Crown river-road intelligence agent | Alive. Minor, not currently active — carried the first report of Idoro's unraveling to Udo (Ep24). |
| Nkiruka | Keeper of the crown's old rites and records, Udo | Alive. Holds the crown's only historical archive on prior encounters with old powers. Revised her reading (Ep65) to recognize two separate powers rather than one growing bolder. Found a centuries old record of a border village that discovered a coerced informant exactly as Idoro did, whose account then stops mid record with no resolution, marked with a spiral matching the search party's own find (Ep94, Ep103). Current thread: told Eze Amadi the full truth of the record the same night Idoro's rider confirmed the search and the Ijeoma hunt are one lineage's work; making a second copy to ride west with the crown's fastest available rider as a warning, though she privately doubts it can outrun ground the search party is already walking (Ep112). |
| Ejikeme | Overseer of the crown's delta trade concessions, Udo | Alive. Won authorization for the crown survey of Idoro's land he had twice been refused (Ep94), granted as crown protective obligation rather than a trade measure, though he could not promise Nkiruka the crown would keep that distinction once exploitable ground was found. Current thread: pushed hardest in council for sending real help to the search party, prevailing on shape (a deniable detachment) if not scale; privately still uneasy that even quiet help moving on the right bearing might eventually be noticed by whoever truly sponsors the Concern at court (Ep118). |
| Osadebe | Captain of Eze Amadi's personal service, permanently assigned to Idoro | Alive. The crown's primary eyewitness and liaison to Idoro. Leads the Ijeoma search party (himself, Emenike, Ifeanyi, Okonjo), sketching fresh maps each evening past the edge of Ubani's survey. Current thread: weighed retreat, waiting for Adaeku's detachment, or pushing closer against the compound; sided with Emenike's case that a House that lost men will move fast rather than wait, and committed the party to closing the distance carefully rather than storming anything, with an explicit standing order that any man may call the risk too high at any time (Ep123). |
| Chidebe | Captain, commands the crown garrison at Idoro | Alive. Disciplined, trusted by Osadebe. Argued Emenike was not yet strong enough for the Ijeoma search and was overruled by Emenike's own flat refusal to be protected (Ep99). Current thread: received the crown's order authorizing a deniable detachment, chose Adaeku to lead it without hesitation, and told Amara honestly that three men are enough to find and stand beside the search party but not enough to take the compound's wall by force (Ep118). |
| Adaeku | Soldier in Chidebe's garrison at Idoro, quietest of the six informant suspects | Alive. Cleared in practice, if not yet formally, of the informant search (Ep86). Current thread: chosen by Chidebe to lead the crown's deniable three man detachment following the search party's bearing, carrying no crown marking and no name traceable to the garrison; departed before dawn with two trusted, lesser known soldiers, promising Amara only what three careful men can honestly deliver (Ep118). |
| Ikwuano | Keeper of the crown's scattered intelligence reports, Udo | Alive. Traced the trading House's court sponsor and confirmed its interest in Idoro predates its public approach by years. Current thread: reported to the council that his tracing has found no confirmed sign the sponsor knows more than an ordinary sponsor should, but urged the crown to act as though it might anyway (Ep118). |
| *(unnamed dibia)* | Village diviner/healer; carried the secondborn to Oso | **Deceased (Episode 26).** Was the entity's first mouthpiece; killed when Ozoemena's borrowed rite against him failed and the entity struck him down mid final message. |
| *(unnamed entity)* | Ancient presence beneath Oso, bonded to Chibundu | Active, still badly weakened but mending. Three centuries old, patient and transactional; broke three centuries of pure restraint to act directly against Mfoniso (Ep90). Current thread: watched the presence receive its first returned fragment of old strength through Chibundu and asked, plainly, what the gain had cost; noted afterward that it had never once heard the presence speak this openly of its grief before this stretch of episodes (Ep115). |
| *(unnamed presence)* | Older power beyond Oso's outer borders, reaches Chibundu through dreams and has spoken through Zara | Active. Named Chibundu (Ep47). Once lost a guardian ground centuries ago to a hunter using the exact tactic Mfoniso now uses (take the people the guardian loves, wait, strike slowly) — revealed Ep67. Broke its three century habit of never overspending its strength to save Kene directly (Ep70), at a cost it still hadn't finished paying as of Ep72-73; further spent by tearing itself out of Zara in Ep82. **Major reveal (Ep100):** confirmed under Chibundu's direct pressure that its own lost guardian ground lay exactly along the bearing west and slightly south of Oso. Learned through the search party's find that its people were taken and moved rather than slaughtered where they stood, breaking three centuries of mourning a false, finished story (Ep105). Current thread: received, unbidden and through Chibundu, the first fragment of its own old strength to return since the taking, sealed away inside the false grief and freed now that the true, unfinished grief has replaced it. Cost both of them a flood of raw memory (including a woman's name it let slip and will not yet explain) but yielded a small, real, tested gain: it can now reach a short true distance past Oso's border for the first time since Ep70, and privately admits it would pay the same cost again gladly (Ep115). |
| Uduak | Market trader, former trading House informant | Alive, held pending Udo's judgment since his confession (Ep53). Not currently active in the plot. |
| the Warden | Ijoma Concern's keeper of old and dangerous knowledge | Active. Authorized Mfoniso's second attempt, against Zara directly (Ep74), overruling the Factor's objection. Revealed the guardian ground debt is inherited across four keepers before her rather than her own personal grievance; permanently relieved the Factor of any further say in the operation and committed resources beyond anything spent on the hunt so far (Ep93). Current thread: when Mfoniso's three day deadline arrived, received an outright refusal, both to recommend closing Ijeoma's account and to personally carry out a kill order, the first order Mfoniso has ever refused (Ep124). Concluded Mfoniso's own lineage tie to the guardian had compromised her judgment, and summoned Ebiere, quietly kept in reserve since her public disowning after the boundary ambush, to close Ijeoma's account cleanly instead; withheld both Mfoniso's guardian theory and the full shape of the recent strangers found on the property, judging a colder hand works best unburdened by complications (Ep125). Does not yet know a Concern patrol clashed with armed strangers on the property this same stretch of days. |
| Mfoniso | Ijoma Concern's retained guardian hunter | Formerly active as the story's chief antagonist — **broke from the House (Ep124)**, its most consequential status change since her introduction. Failed to abduct Kene (Ep70) when the presence intervened directly; pivoted to a slow, undetectable working against Zara's borrowed senses instead, confirmed succeeding by Ep77-78. Confirmed as trained in or descended from the same hunting lineage that took the presence's guardian ground three centuries ago (Ep82); revealed to be carrying her own second thread to whoever trained her, gone silent since Ep108 and never restored. Breached Idoro's compound directly, seized Adaugo, and struck down Emenike, then fled wounded and shaken when the entity met her in the open for the first time (Ep90). Learned her own teacher stands only two apprenticeships from the original hunter (Ep113). Current thread: when her final three day deadline arrived, refused outright to recommend closing Ijeoma's account and refused, in the same breath, to carry out a kill order personally, the first order she has ever refused in her career. Cited her growing conviction that the guardian at Idoro is the same one her teacher's unfinished training story always protected, and that continuing the hunt would mean knowingly finishing an unpaid debt she no longer believes her lineage had any right to collect. Relieved of every operation and told to remain findable, her fate undecided. Does not yet know a Concern patrol clashed with armed strangers on the property this same stretch of days. |
| Chiazor | Trading House's formal sponsor at Udo | Alive. Revealed a senior House figure was already traveling toward Idoro before the ambush. Not currently central to the active plot. |
| the Factor | Senior trading House figure, Ebiere's direct superior | Alive, permanently removed from any further say in the Mfoniso operation. Objected three times now (Ep64, Ep74, Ep93) to escalating the hunt against Oso's guardian, each time overruled; his final, sharpest objection after learning of the entity's direct intervention led the Warden to relieve him of authority over the operation entirely (Ep93). Split the eastern gate's morning post into two shorter watches during a routine staffing review (Ep114); recognized Ijeoma's family trade knot during a dock inspection and let it pass (Ep117). Current thread: used a pretext security review, prompted by the compound wide alert after the courier ambush, to speak to Ijeoma directly for the first time, an oblique but real warning that the House's tightened fear will not make it more patient with her. His most dangerous act of quiet treason yet, deliberate rather than deniable (Ep121). |
| Ebiere | Trading House field agent who orchestrated the boundary ambush | Alive. **Reveal (Ep125):** never actually cut loose — quietly reassigned to a small downriver holding two seasons ago while publicly disowned as a rogue agent, kept in reserve for exactly the kind of task the House could not afford to be seen requesting directly. Current thread: summoned by the Warden to take over Ijeoma's account from Mfoniso, precisely because she carries no lineage tie to the guardian and no capacity the Warden has yet seen for doubt. Accepted the assignment as her chance to erase the stain of a fall she has always privately believed was undeserved; traveling to the main compound (Ep125). |
| Effiong | Young crown soldier who sold patrol schedules for coin, enabling the ambush | Confessed (Ep52). Not currently active in the plot. |
| *(unnamed)* | Elder Maka's returned son | Deceased. Her own abandoned twin, returned wrong at age eight, killed three people including her husband; she killed him herself. Origin of her severity toward the old law. |
| Emenike | Soldier in Chidebe's garrison at Idoro | Alive, on the road with the Ijeoma search party, well past the lost ground. Served under Chidebe since before the boundary ambush (Ep51); confirmed as Mfoniso's informant (Ep87), coerced for two seasons by threats against his sister, Ijeoma. Threw himself between Mfoniso and Adaugo during her direct attack on the compound (Ep90). Carries Elder Maka's protective cord and Amara's plea to come home either way. Current thread: made the case that carried the party's aftermath debate, that a House which lost men in the clash will move fast against its liabilities rather than wait, and won Osadebe's agreement to push closer rather than retreat or simply hide. Took the dawn watch alone, still uncertain whether the choice leads to his sister or to all four of their deaths (Ep123). Does not know Mfoniso confirmed Ijeoma's location (Ep93), that the Warden has stopped the bracelet proof runs, nor that the Warden's fourteen day deadline for Ijeoma's fate is already running. |
| Ijeoma | Emenike's younger sister | Alive, confirmed held at the Ijoma Concern's disguised headquarters downriver, seen briefly by Mfoniso in a heavily guarded inner courtyard (Ep93), confirming the bearing (west, slightly south) reported in Ep88. Taken from a river town by the Concern's agents two seasons ago while trading cloth for their mother; held as leverage to coerce Emenike's cooperation as an informant. Introduced in her own viewpoint for the first time (Ep101): nineteen, a cloth trader's daughter who counts everything, watchful and deliberate. Current thread: finished mapping the compound's full guard rotation (old and new eastern gate gaps, a thin dock handoff gap) and requested dock duty as cover. Tied her family's private trade signature knot into an outgoing cloth bundle's corner as a signal to any river trader who might someday recognize it, the closest call yet when the Factor's thumb passed directly over the knot during his own inspection and he let it go with a flat "count is correct" (Ep117). Does not know whether his response was genuine or deliberate. Does not know a search party has sighted her House's headquarters and, through a captured courier, confirmed her name and general condition (Ep120), nor that the Warden has given Mfoniso a fourteen day deadline on her own fate. Current thread: made her second real escape attempt during the compound's three day alert, using a rope stolen a hand span at a time and a submerged rock spit her dock counting identified to finally cross the water that stopped her the first time. Cleared the wall itself for the first time, but was spotted by an unscheduled patrol in the open ground beyond it and is being run down at a dead sprint, a hand just closing on her arm as the episode ends (Ep126, cliffhanger, outcome unresolved). Does not know about Ebiere. Idoro's household does not yet know her exact location has been confirmed. |
| the guard | Unnamed soldier posted at the Concern headquarters' eastern gate | Alive. His habitual, unpunished gap in the gate watch is the timing Ijeoma has built her escape planning around since Ep102. Caught Ijeoma returning from her failed climb at dawn and chose not to report her (Ep109); a household wide security tightening ordered days later for unrelated reasons left his own post untouched, and he has kept his same careless habit since, unaware Ijeoma now reads that consistency as deliberate confirmation and is watching him deliberately in turn (Ep110). Still rattled by the compound's three day alert, left his post in a ragged version of his usual gap, unknowingly giving Ijeoma her second real chance (Ep126). First thread of a possible inside ally; his own motive (an unfinished thought about a sister of his own) remains unconfirmed even to the audience. |
| Ubani | Lead surveyor, crown survey party at Idoro (Ep94's authorized survey) | Alive, survey work concluded. Careful, observant, professionally honest; fifteen years' experience surveying disputed and unusual ground. Walked Oso's boundary alone (Ep97) and encountered an overwhelming, formless dread with no concrete cause he could name. Current thread: accepted Elder Maka's true but incomplete account of Oso as the old law's abandonment ground and grief-soaked site; marked it consecrated ground excluded from crown development in his official report, protecting the household's deeper secret without ever being told it, and departed Idoro with genuine respect for what he chose not to dig further into (Ep98). |
| Ude | Ubani's second on the crown survey, carries the measuring chain | Alive. Grew up two villages from Idoro; knows Oso's reputation but is cautious about saying so to a crown official. Warned Ubani gently that the ground is tied to old grief, not merely superstition (Ep96), which helped prepare him to accept Elder Maka's account without much resistance (Ep98). |
| Ifeanyi | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Grew up hunting; first to read the land's wrongness — game trails bending in wide curves around nothing (Ep101). Current thread: argued for retreat during the aftermath debate, unconvinced by Emenike's reasoning but following Osadebe's decision to push closer regardless (Ep123). |
| Okonjo | Soldier, Chidebe's garrison at Idoro | Alive, with the search party. Found the toppled spiral boundary stone an hour before dusk on the fourth day west (Ep101). Current thread: shaken by his own near death in the patrol clash, admitted he trusts Osadebe's judgment over his own right now and deferred entirely on the party's next move (Ep123). |

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

### 5.2 WHO KNOWS WHAT — dramatic irony ledger (as of Episode 126)

Update this table whenever knowledge changes hands. It protects continuity
(no character may act on a fact this table says they lack) and marks where
the suspense lives.

| Fact | Who knows | Who does NOT know |
|---|---|---|
| The captor House's name ("the Ijoma Concern") | The Concern's own people; the narration (Eps 64, 68, 74 only) | **The household and the crown have never heard the name.** They say "the trading House" / "the House." The crown's Ep94 investigation into which House sponsored the coercion is still unresolved. |
| Ijeoma's exact location (the Concern's headquarters, confirmed Ep93) | Mfoniso only — she told no one, holding it as leverage | The Warden, the household, the crown, and **Emenike**, who searches on a bearing alone |
| The presence's lost guardian ground lies along the search bearing (Ep100), two days ahead of the party (Ep101) | The presence, the entity, Chibundu | Everyone else — the search party found the ground's boundary stone (Ep101) but has no idea what it marks or that Oso knows |
| The bracelet proof runs are canceled (Ep101) | The Warden, the Factor; Ijeoma has independently deduced it from the overdue taking | The household, the crown, and Emenike, who does not know his sister's proof of life has stopped mattering to the House |
| The Warden's ciphered question — does the hunt still need Ijeoma alive, or may the House close the account (Ep101) — reached Mfoniso in Ep108, who chose to carry her answer south in person rather than reply by courier | The Warden and Mfoniso | The Warden does not know her question was received at all; reads Mfoniso's silence as an alarming, unexplained delay and is hardening toward closing the account because of it (Ep110). Idoro, Udo, and Ijeoma remain unaware a clock is running on Ijeoma's life |
| Ijeoma made a real escape attempt and reached the top of the eastern wall before retreating rather than drop blind into unreadable water (Ep109); she has since confirmed the guard's continued silence and begun deliberately banking it as usable intelligence (Ep110) | Ijeoma, the eastern gate guard (saw her return), the Factor (found and hid the physical evidence) | The Warden, Mfoniso, the household, and the search party coming for her |
| The eastern gate guard saw Ijeoma return from her climb and chose not to report her; the Factor found the disturbed ground the next morning and scuffed it smooth rather than report it either (Ep109) | The guard and the Factor, each unaware of the other's silence | Everyone else, including each other — neither man knows the other also chose not to report it |
| The household's doubled guest watch (Ep110) is the Warden's own reaction to Mfoniso's unexplained delay, not a response to Ijeoma's escape attempt | The Warden (and the audience) | Ijeoma spent the day certain she had been caught before reasoning her way to the correct, if unproven, conclusion by nightfall |
| Fresh, carelessly left multi day footprints cross the search party's path west of the lost ground, moving the same direction, with a fainter set weeks older beneath them suggesting the ground is regularly walked (Ep111) | The search party (Osadebe has not yet shared the older set's age with the other three) | Everyone else — the Concern does not yet know it is being tracked, and the search party does not yet know whether these are Concern scouts, ordinary travelers, or something else |
| The Factor's loyalty has begun to crack (Ep101) | The Factor only (and the audience) | The Warden believes his objections are still merely professional |
| Mfoniso's lineage tie to the hunter who took the presence's ground (Ep82) and her second thread to her teacher (Ep83) | The household and both powers | Mfoniso does not know they know |
| Mfoniso's private suspicion that the one guardian her teacher's training story always broke off at, the single lineage conquest ever refused, is the same guardian that met her at Idoro's wall (Ep108); deepened by learning her own teacher stands only two apprenticeships removed from the original hunter (Ep113) | Mfoniso only | The household, both powers, the Warden, and the search party have no idea she has begun drawing this connection |
| Mfoniso has refused the Warden's order outright, both the recommendation and any personal role in closing Ijeoma's account, and been relieved of every operation (Ep124) | The Warden, Mfoniso, and (by rumor already spreading) the wider compound staff | Ijeoma, the household in Idoro, the search party, and the Factor (who passed Mfoniso in a corridor but does not know why the mood around her has shifted) |
| Ebiere was never actually cut loose after the boundary ambush, only quietly reassigned; the Warden has now summoned her to close Ijeoma's account in Mfoniso's place, and she is traveling to the main compound (Ep125) | The Warden and Ebiere | Ijeoma, Mfoniso, the Factor, the household in Idoro, and the search party all have no idea a second, colder threat is now converging |
| Ijeoma cleared the eastern wall itself for the first time in her second escape attempt, using a stolen rope and a submerged rock crossing, but was spotted in the open ground beyond it by an unscheduled patrol and is being chased down as of the last page (Ep126, unresolved) | Whoever is present at the chase | Everyone else in the story, including the reader's next confirmed fact — outcome deliberately left open |
| The Warden has privately begun to doubt whether Mfoniso's legendary reliability has ever been tested by anything that mattered to her personally rather than only to the House (Ep119) | The Warden only | Mfoniso does not know the Warden's trust in her has quietly started to shift |
| The Factor split the eastern gate's morning post into two shorter watches, folding a second official, unquestionable gap into the handoff between them (Ep114) | The Factor only; Ijeoma has noticed the new pattern but not yet its cause or usefulness | The guard himself does not know why his post changed; the Warden, Mfoniso, and the household have no idea it happened |
| The presence received a fragment of its own old strength back through Chibundu, including the name of a woman it has not yet explained, and can now reach a short true distance past Oso's border for the first time since Ep70 (Ep115) | The household inside Oso only (Chibundu, the entity, the presence) | The search party, Mfoniso, both Houses, and everyone in Idoro's wider world; the fragment's cause (the search party disproving the old "slaughter" story) is unknown to the party itself |
| The search party has confirmed, through a captured courier, that Ijeoma is held in the compound's inner courtyard, alive and apparently unharmed (Ep120) | The search party only | Ijeoma does not know she has been found; the Warden, Mfoniso, and the household in Idoro have no idea the party has confirmed anything |
| A Concern tracking patrol found and clashed openly with the search party; several trackers were wounded or killed and the party broke contact down a ravine, losing all remaining stealth (Ep122) | The search party and the surviving trackers who reported back (implied, not yet shown on page) | The Warden, still consumed by her own deadline decision with Mfoniso, does not yet know the clash happened; two clocks (her three day deadline and the compound's now certain knowledge of armed strangers) are running in parallel, unknown to each other |
| The search party has committed to pushing closer to the compound rather than retreating or waiting for Adaeku's detachment, on Emenike's judgment that a House which lost men will act fast (Ep123) | The search party only | The compound, the Warden, Mfoniso, Ijeoma, and Adaeku's own detachment (whose distance behind the party remains unknown to both sides) |
| The Factor spoke to Ijeoma directly for the first time, warning her obliquely that the compound's new fear will not make it kinder to her (Ep121) | The Factor and Ijeoma | The Warden, the guard at the door (who heard nothing incriminating), and everyone else in the compound |
| Ijeoma hid her family's private trade knot in an outgoing cloth bundle as a signal to any river trader who might recognize it (Ep117); the Factor recognized it during inspection and deliberately let it pass | Ijeoma and the Factor, each unaware of what the other actually knows about the other's awareness | Everyone else; the boat's eventual destination and whether anyone will ever notice the knot is unknown even to the narration |
| Udo has dispatched a small, deniable three man detachment (Adaeku and two others, no crown markings) to find and reinforce the search party (Ep118) | Eze Amadi, Nkiruka, Ejikeme, Ikwuano, Chidebe, Amara, and the three men themselves | The search party, who do not know help is coming at all; the Concern and the Warden, who have no idea any crown activity is moving on this bearing |
| A tension along Mfoniso's second thread to her teacher went slack for the first time in her memory, the night she made camp south on the river road (Ep108); cause unrevealed | No one, including the narration | Mfoniso only knows something moved; she has no name or direction for it |
| The House holding Ijeoma is the same lineage that emptied the presence's lost ground three centuries ago, confirmed by a matching maker's mark (Ep106) | The search party | The household, the crown, Oso, the Warden, and Mfoniso (who already knows the lineage tie from her own training but does not know the search party has made this connection) |
| The search party's true purpose and departure (Ep99-100) | The household, the crown | Mfoniso saw a small four man band leave Idoro at a distance (Ep102) but filed it as routine patrol rotation — she does not know it was the search party, or what it is for |
| Nkiruka's archive record that stops mid-page (Ep94), understood as a deliberate warning marked with the same spiral the search party found (Ep103); told to Eze Amadi in full and now being copied to ride west as a warning (Ep112) | Nkiruka, Eze Amadi, and (secondhand) Ejikeme, who was present when Idoro's rider reported | The search party, still walking the same ground unwarned; the copy has not yet left Udo |
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
header for its current range, Episodes 1-108 as of this writing); when this
section grows past ~20 entries, move the oldest ones there following the
same pattern (see Section 10, step 5).

**Note on dates:** the parenthetical dates on episode entries are the
scheduled Pocket FM release dates (per Section 4's schedule-ahead cadence),
not writing dates. Writing/commit dates live in git history and are weeks
to months earlier.

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
- **Episode 110 — "The Wrong Reason to Be Afraid" (2026-10-25):** The
  Warden, unsettled by Mfoniso's overdue answer, orders the guest's
  household watch doubled for reasons that have nothing to do with
  Episode 109's failed climb; privately, the delay is tipping her own
  ledger further toward closing the account. Ijeoma wakes to a
  visibly tightened compound and spends the day certain she has been
  caught, working through the fear with the same counting patience
  that has kept her alive this long. By nightfall, reasoning from the
  eastern gate guard's unchanged habits rather than any proof, she
  concludes the tightening is not about her, and reclassifies his
  continued silence from one time luck to intelligence worth banking.
  Closes on the dramatic irony made explicit to the audience alone:
  the net closing around the compound is the Warden's, not Ijeoma's,
  and if Mfoniso's answer does not arrive soon it will not need
  Ijeoma's own secret to justify what comes next.
- **Episode 111 — "The Weight He Could Finally Carry" (2026-10-26):**
  Five days past the lost ground, on country no crown map has ever
  touched, a rain rotted footbridge gives way under Okonjo crossing a
  swollen ravine. Emenike, once doubted as too fragile for this
  search, holds him from the current at the cost of a deep arm
  bruise, and Osadebe tells him plainly, in front of the other two,
  that Chidebe's Episode 99 doubt was wrong. The near miss deepens
  trust among the four men under real strain rather than simply
  costing them a day. Closes on Ifeanyi finding fresh, carelessly
  left footprints crossing their own trail, moving the same
  direction, with a fainter set weeks older beneath them, proof this
  forgotten ground is walked regularly by someone who has never once
  worried about being followed on it.
- **Episode 112 — "What the Record Was Trying to Say" (2026-10-27):**
  Idoro's rider reaches Udo after nine hard days, confirming the
  search for Ijeoma and the search for the presence's lost people are
  one lineage's work. Nkiruka, hearing it land beside the archive
  record she has privately sat on since Episode 94, a border village's
  coerced informant account that stops mid page, marked with the same
  spiral the search party found, finally understands it as a pattern
  rather than an isolated mystery and confesses the full truth to Eze
  Amadi that same night. He orders it copied and sent west as a
  warning. Closes on Nkiruka's unspoken fear that no courier, however
  fast, can outrun ground the search party is already walking, and
  that the record's warning may reach them only after they have found
  its meaning for themselves.
- **Episode 113 — "Closer Than the Story Let Her Believe" (2026-10-28):**
  Mfoniso reaches the Concern's headquarters and insists on asking the
  Warden her own question first: what became of the guardian ground's
  resettled people, and does the House still keep record of where.
  The Warden answers plainly, then names the debt's four keeper chain
  almost as an aside, letting Mfoniso work out for herself that her
  own teacher stands only two apprenticeships removed from the
  original hunter, collapsing the "one guardian who ever refused to
  run" story from distant legend to something close enough to touch.
  Mfoniso recommends caution rather than closing Ijeoma's account; the
  Warden agrees to wait, but warns it will not be forever. Closes on
  Mfoniso's private, unspoken realization that she may have spent her
  entire career unknowingly finishing a story her own teacher never
  let her hear the end of.
- **Episode 114 — "The Kindness No One Will Trace" (2026-10-29) [Act 2
  hook]:** The Factor, left with only the household's quarterly
  staffing review as authority, splits the eastern gate's morning
  post into two shorter watches, folding a second official, logged,
  unquestionable gap into the handoff between them inside an
  otherwise ordinary security improvement, untraceable to himself and
  motivated by the shame of Episode 101's realization that he had
  never once read Ijeoma as a person. Ijeoma notices the new pattern
  without yet understanding its cause. The Warden, unmoved by
  Mfoniso's call for more time, sets a firm ten day deadline for a
  final recommendation on Ijeoma's fate, closed account or continued
  asset, and warns she will decide herself, unsentimentally, if the
  ten days pass unanswered. Closes on the number sitting unseen over
  the compound: unknown to Ijeoma, unknown to the search party still
  days out, unknown to the guard now working a schedule reshaped by a
  man who wants nothing from this House but its own overdue
  conscience.
- **Episode 115 — "A Fragment of What Was Lost" (2026-10-30):** Days
  after the search party disproved the presence's three century
  "slaughter" story, a fragment of its own old strength finally finds
  its way home through Chibundu, unbidden, flooding him with raw
  memory including a woman's name the presence lets slip and will not
  yet explain. The gain is real: tested carefully afterward, the
  presence can now reach a short true distance past Oso's border for
  the first time since it tore itself loose from Zara to save Kene.
  The entity notes it has never heard the presence speak this openly
  of its grief before. Closes on the presence's quiet admission that
  it would pay the same cost again gladly, and does not yet know what
  receiving the whole, rather than a fragment, would actually demand.
- **Episode 116 — "A Fortress Wearing a Market's Face" (2026-10-31):**
  The search party sights the Concern's disguised headquarters from a
  wooded ridge: a proper defensive wall, disciplined guard rotations,
  and a second inner wall hinting at something the House values more
  than its warehouses, far larger and better guarded than four crown
  soldiers prepared for. Emenike, sighting the wall his sister may be
  held behind for the first time, argues to keep moving rather than
  wait for help; Osadebe holds the line at watch and learn rather than
  attempt entry, privately doing the grim arithmetic of how many days
  any crown help would need to reach this ground and return. Closes
  cold on four men lying within sight of a wall that gives away
  nothing about what it actually keeps behind it.
- **Episode 117 — "A Knot Her Mother Taught Her" (2026-11-01):** Ijeoma
  finishes mapping the compound's full guard rotation and requests
  dock duty as cover, then ties her family's private cloth trade
  signature into an outgoing shipment's corner selvedge, a signal
  legible only to a stranger from her own home market. The Factor's
  own dock inspection brings his thumb directly over the knot, the
  closest near miss yet; he declares the count correct and lets it
  pass, privately feeling relief rather than fear at how close he
  came to exposing his own quiet treason. Closes on Ijeoma alone that
  night, unable to tell whether his response was genuine or
  deliberate, having reached, for the first time, beyond the
  compound's walls toward a world that still does not know to look
  for her.
- **Episode 118 — "Quiet Enough to Deny" (2026-11-02):** Eze Amadi,
  Nkiruka, and Ejikeme weigh the crown's options for a search party
  standing outside crown jurisdiction against a House whose court
  sponsor Ikwuano still cannot rule out. An open army risks a
  declaration against an unknown enemy; Eze Amadi authorizes a small,
  deniable detachment instead, ordering Chidebe at Idoro to choose the
  men himself. Chidebe hands the mission to Adaeku, the quietest
  soldier in his garrison, who departs before dawn with two trusted
  companions carrying no crown marking, promising Amara only what
  three careful men can honestly deliver. Closes on Ejikeme's private
  unease that even deniable help moving on the right bearing might
  eventually be noticed by whoever truly sponsors the Concern at
  court.
- **Episode 119 — "The First Crack in Her" (2026-11-03):** Six days
  into her ten day allowance, Mfoniso has spent her spare hours
  reaching for her silent teacher rather than building a
  recommendation on Ijeoma's fate. Pressed by the Warden for progress,
  she admits, for the first time in ten years of service, that she
  cannot reach her teacher and does not know why, an unrehearsed
  apology that cracks a composure the Warden had always trusted
  completely. The Warden extends the deadline to fourteen days rather
  than replace her, but closes privately turning over a harder
  question: whether her most reliable instrument has ever actually
  been tested by anything that mattered to Mfoniso personally, rather
  than only to the House's own careful ledgers.
- **Episode 120 — "A Name From a Stranger's Mouth" (2026-11-04):** The
  search party ambushes two couriers on a rear gate supply trail.
  Osadebe captures and questions one, confirming a closely watched
  "guest" in the inner courtyard matches Ijeoma exactly, her name
  spoken aloud by a stranger for the first time; Emenike, present
  against his own better judgment, asks whether she seems well and
  receives a cautious but genuinely hopeful answer. The second courier
  breaks free wounded and flees back to the compound, costing the
  party its invisibility. Osadebe binds the captive rather than kill
  or free him and moves the party to a new hidden position. Closes on
  the party's grim recalculation: they have confirmation, but no
  longer the luxury of being unseen while they decide what to do with
  it.
- **Episode 121 — "The Warning He Could Not Take Back" (2026-11-05):**
  The compound doubles every watch after the wounded courier's report.
  Fearing a frightened House grows harsher rather than kinder toward
  its uncertain liabilities, the Factor uses a pretext security review
  to speak to Ijeoma directly for the first time, warning her obliquely
  that her window is closing faster than she may realize. It is his
  most dangerous act of quiet treason yet, deliberate rather than
  deniable. Closes on Ijeoma, unable to confirm his motive or trust
  him fully, choosing to trust the urgency anyway and beginning to
  weigh how to act faster than her old patient counting would
  normally allow.
- **Episode 122 — "The Quiet Finally Breaks" (2026-11-06) [Act 3
  close, MIDPOINT]:** A six man Concern tracking patrol, following the
  wounded courier's blood trail, finds the search party's relocated
  position and forces an open clash. Emenike wounds a man for the
  first time and finds the fear of it matches the fear he has carried
  since the Idoro ambush; Okonjo's weak ankle nearly costs him his
  life before Ifeanyi intervenes. The party breaks contact down a
  ravine slope, stealth gone for good. In the same stretch of days,
  the Warden, unsettled by sleepless nights and a compound that no
  longer feels safe, collapses Mfoniso's fourteen day allowance to a
  hard, non negotiable three, admitting plainly it is fear rather than
  doubt in her judgment. Act Three closes on two clocks now running
  in parallel, neither the Warden nor Mfoniso aware the patrol clash
  has already happened.
- **Episode 123 — "Whatever It Costs Us Now" (2026-11-07):** With
  stealth gone, the search party debates retreat, waiting for
  Adaeku's detachment, or pushing closer. Emenike argues a House that
  lost men in the clash will move fast against its liabilities rather
  than wait, not slow down; Osadebe, weighing the debt he has owed
  Emenike's judgment since the ravine, commits the party to closing
  the distance carefully rather than storming anything, with a
  standing order that any man may call the risk too high at any time.
  Closes on Emenike taking the dawn watch alone, uncertain whether
  tonight's decision leads to his sister or to all four of their
  deaths.
- **Episode 124 — "The First Order She Ever Refused" (2026-11-08):**
  Mfoniso's three day deadline arrives. Rather than delay or offer a
  comfortable answer, she refuses outright to recommend closing
  Ijeoma's account and refuses, in the same breath, to be the hand
  that closes it herself, the first order she has ever refused in her
  career. She cites her growing conviction that the guardian at Idoro
  is the same one her teacher's unfinished training story always
  protected, and that continuing the hunt means knowingly finishing a
  debt she no longer believes her lineage had any right to collect.
  The Warden, more frightened than angry, relieves her of every
  operation and orders her to remain findable rather than punishing
  her immediately. Closes on Mfoniso walking a compound that already
  feels different beneath her, feeling clarity rather than fear for
  the first time in weeks.
- **Episode 125 — "A Colder Hand to Finish It" (2026-11-09):** The
  Warden concludes Mfoniso's own lineage tie to the guardian has
  compromised her judgment, and summons Ebiere, reveal: never actually
  cut loose after the boundary ambush, only quietly reassigned to a
  downriver holding two seasons ago and kept in reserve for exactly
  this kind of task. Ebiere accepts the assignment to close Ijeoma's
  account as her chance to erase the stain of a fall she has always
  believed was undeserved, carrying none of Mfoniso's doubt. The
  Warden withholds both Mfoniso's guardian theory and the full shape
  of the recent strangers found on the property, judging a colder
  hand works best unburdened. Closes on Ebiere traveling toward the
  compound, a second, colder threat now converging on a young woman
  who has no idea her account has just changed hands.
- **Episode 126 — "The Water She Finally Crossed" (2026-11-10)
  [cliffhanger]:** Reading the compound's three day alert as her last
  real window rather than new danger, Ijeoma makes her second escape
  attempt, using a rope stolen a hand span at a time and a submerged
  rock crossing her dock counting identified to finally solve the
  water that stopped her the first time. She clears the wall itself
  for the first time, only to be spotted by an unscheduled patrol in
  the open ground beyond it, the same scrambled watch that gave her
  the opening now working against her. Closes mid chase, a hand
  closing on her arm, outcome deliberately unresolved.

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
