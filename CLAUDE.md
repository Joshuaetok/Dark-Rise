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
Episode 63 (registry) and Episode 63 (changelog) now lives in `ARCHIVE.md` in
this same repo. This file keeps only what's needed to write the next episode
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
history.** Full episode-by-episode detail through Episode 73 lives in
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

| Name | Role | Current status (as of Episode 78) |
|---|---|---|
| Amara | Mother of the twins | Alive, Idoro, full council seat. Knows the entity, the presence, Chibundu's identity, and Elder Maka's condition — no secrets left within the household. Current thread: stayed at Emenike's side through the night as Zara fought to save him, forgave his betrayal completely once he woke briefly asking after Ijeoma; carries an unresolved fear over the unknown size of the debt the entity's rescue may have opened (Ep91). |
| Obi | Father of the twins | Alive, Idoro. Fully present and active partner to Amara in every crisis since Episode 6. Current thread: named plainly, in the attack's aftermath, that the household chose wrong by pulling its soldiers to the market ambush rather than carelessly or maliciously — a costly but honest lesson (Ep91). |
| Zara | Village midwife | Alive, living mostly at Amara's compound. Delivered both twins; carries a dormant blood thread the presence (not the entity) has used to reach her since her Episode 42 return. Her borrowed sense of danger has been the family's best early warning system since Episode 69, though still muffled by Mfoniso's working since Ep77-78. Told Adaugo plainly, for the first time, that she considers her family (Ep82). Current thread: fought through the night to save Emenike's life with her own hands after her muffled gift failed to warn the household of Mfoniso's attack (Ep90); confirmed by dawn that he will live (Ep91). |
| Adaugo | Elder Maka's surviving daughter | Alive, Idoro, still carrying an active foreign working. Fully reconciled with her mother since Episode 66; learning the old rites. Current thread: reported the anchor thread "truly woke" rather than merely waited when Mfoniso gripped it directly (Ep90); Elder Maka has not yet re-examined it properly. Sat quietly beside the sleeping, wounded Emenike before dawn, thanking him for a debt he had already begun repaying before he nearly died proving it (Ep91). |
| Elder Maka | Elder priestess | Alive, Idoro, restored to a respected advisory council seat (not sole authority over the old law, stripped Ep19). Secretly carries her own thin thread to the entity since the Episode 12 binding rite (now openly known to the household and village). Current thread: promised Adaugo a proper examination of the anchor thread's changed state once daylight and steadier hands allow it (Ep91); has not yet performed it. |
| Ozoemena | Mid ranking Idoro elder | Alive, Idoro. Humbled, trusted council member who serves through labor since his own disastrous rite killed the dibia (Ep26). Current thread: knelt beside the wounded Emenike the night of the attack, telling him he had shown the household his best hour after asking it to judge him beyond his worst (Ep91). |
| Kene | Surviving firstborn twin | Alive, toddler, Idoro. Original twin thread to the entity severed (Ep12); knows he has a brother (told Ep66); survived Mfoniso's first abduction attempt (Ep70), saved when the presence reached beyond Oso's ground for the first time. Current thread: began tracing an unbidden spiral in the dirt (Ep76) — the same shape both old powers have used on Zara — raising fear the presence's rescue left a second, uncut thread in him. Family is watching, not attempting another hasty severing rite. |
| Chibundu | Abandoned secondborn twin / protagonist ("the one whom the presence carries") | Alive, Oso. Named by the presence through Zara (Ep47); reunited with Amara (Ep50); survived a trading House ambush at that reunion; has twice refused the trading House's partnership offer (once in his own voice, once when the presence seized his voice to refuse it for him, Ep60-61) and extracted a narrower promise from the presence (it will not take his voice again except to save his life). Current thread: kept vigil through the night in Oso's cold place until the entity finally answered near dawn, weaker than he has ever felt it; told it plainly to rest, the first time he has ever given it an order rather than a request (Ep91). |
| Eze Amadi | King, Kingdom of Ijendu, throned at Udo | Alive, Udo. Aware of the entity and, since Ep65, the presence as a second distinct power. Has permanently assigned Osadebe to Idoro, stationed Chidebe's garrison there, and twice refused Ejikeme's push for a crown survey of Idoro's land. Currently absorbing Nkiruka's revised reading of the crown's historical archive (two powers across three centuries, not one). |
| Nduka | Crown river-road intelligence agent | Alive. Minor, not currently active — carried the first report of Idoro's unraveling to Udo (Ep24). |
| Nkiruka | Keeper of the crown's old rites and records, Udo | Alive. Holds the crown's only historical archive on prior encounters with old powers. Revised her reading (Ep65) to recognize two separate powers rather than one growing bolder. Active advisor to Eze Amadi. |
| Ejikeme | Overseer of the crown's delta trade concessions, Udo | Alive. Has twice failed to win authorization for a crown survey of Idoro's land. Increasingly humbled by the scale of what the crown faces (admitted as much to Nkiruka, Ep65). |
| Osadebe | Captain of Eze Amadi's personal service, permanently assigned to Idoro | Alive. The crown's primary eyewitness and liaison to Idoro. Recently returned from a full moon in Udo (Ep73), openly frustrated at how slow crown caution is. Current thread: reconstructed the attack with Chidebe at dawn, warning Amara that whatever met Mfoniso in the compound has changed how she sees the household in ways not yet predictable (Ep91). |
| Chidebe | Captain, commands the crown garrison at Idoro | Alive. Disciplined, trusted by Osadebe. Has doubled the night watch three times in episodes 77-78 as warnings escalate. Current thread: named the tactical lesson of the failed ambush plainly to Osadebe — they built Mfoniso a door and called it a trap (Ep91). |
| Ikwuano | Keeper of the crown's scattered intelligence reports, Udo | Alive. Traced the trading House's court sponsor and confirmed its interest in Idoro predates its public approach by years. Not currently central to the active plot thread. |
| *(unnamed dibia)* | Village diviner/healer; carried the secondborn to Oso | **Deceased (Episode 26).** Was the entity's first mouthpiece; killed when Ozoemena's borrowed rite against him failed and the entity struck him down mid final message. |
| *(unnamed entity)* | Ancient presence beneath Oso, bonded to Chibundu | Active, badly weakened. Three centuries old, patient and transactional; broke three centuries of pure restraint to act directly against Mfoniso (Ep90). Current thread: answered Chibundu near dawn after a full night of silence, thinner and further away than he has ever felt it; admitted it does not know if it could reach that far again or what the act cost Oso itself, and conceded to Chibundu that it has called its own restraint "wisdom" for three centuries without ever being tested closely enough to know if that was true (Ep91). Resting at Chibundu's insistence. |
| *(unnamed presence)* | Older power beyond Oso's outer borders, reaches Chibundu through dreams and has spoken through Zara | Active. Named Chibundu (Ep47). Once lost a guardian ground centuries ago to a hunter using the exact tactic Mfoniso now uses (take the people the guardian loves, wait, strike slowly) — revealed Ep67. Broke its three century habit of never overspending its strength to save Kene directly (Ep70), at a cost it still hadn't finished paying as of Ep72-73; further spent by tearing itself out of Zara in Ep82. Current thread: still weakened, watched rather than actively reached during Elder Maka's Episode 83 trace, cautioning that a thread held open on purpose would show only what it chose to reveal. |
| Uduak | Market trader, former trading House informant | Alive, held pending Udo's judgment since his confession (Ep53). Not currently active in the plot. |
| the Warden | Ijoma Concern's keeper of old and dangerous knowledge | Active but offstage. Authorized Mfoniso's second attempt, against Zara directly (Ep74), overruling the Factor's objection. |
| Mfoniso | Ijoma Concern's retained guardian hunter | Active — the story's current antagonist. Failed to abduct Kene (Ep70) when the presence intervened directly; pivoted to a slow, undetectable working against Zara's borrowed senses instead, confirmed succeeding by Ep77-78. Confirmed as trained in or descended from the same hunting lineage that took the presence's guardian ground three centuries ago (Ep82); revealed to be carrying her own second thread to whoever trained her (Ep83). Breached Idoro's compound directly, seized Adaugo, and struck down Emenike, then fled wounded and shaken when the entity met her in the open for the first time in her career (Ep90). Current thread: wounded but alive beyond Idoro's boundary, deciding how to respond to a household now confirmed to carry a guardian willing to act directly rather than only defend (Ep91, ongoing). |
| Chiazor | Trading House's formal sponsor at Udo | Alive. Revealed a senior House figure was already traveling toward Idoro before the ambush. Not currently central to the active plot. |
| the Factor | Senior trading House figure, Ebiere's direct superior | Active but offstage since Ep61. Objected twice (Ep64, Ep74) to the Warden's authorization of lethal action against the old powers/Zara, both times overruled. |
| Ebiere | Trading House field agent who orchestrated the boundary ambush | Whereabouts unknown since Ep53; publicly disowned by the Factor as a rogue agent. |
| Effiong | Young crown soldier who sold patrol schedules for coin, enabling the ambush | Confessed (Ep52). Not currently active in the plot. |
| *(unnamed)* | Elder Maka's returned son | Deceased. Her own abandoned twin, returned wrong at age eight, killed three people including her husband; she killed him herself. Origin of her severity toward the old law. |
| Emenike | Soldier in Chidebe's garrison at Idoro | Alive, gravely wounded but confirmed by Zara to survive. Served under Chidebe since before the boundary ambush (Ep51); confirmed as Mfoniso's informant (Ep87), coerced for two seasons by threats against his sister, Ijeoma, taken from a river town while trading cloth. Threw himself between Mfoniso and Adaugo during her direct attack on the compound, taking a deep wound to the side that bought the household perhaps three seconds (Ep90). Current thread: fever broke near dawn; woke briefly to ask whether he had lost Ijeoma too, and was promised the household's search for her continues regardless (Ep91). Fully forgiven by Amara. |
| Ijeoma | Emenike's younger sister | Alive (proof of life confirmed twice a season via a blue thread bracelet). Taken from a river town by Ijoma Concern agents two seasons ago while trading cloth for their mother; held as leverage to coerce Emenike's cooperation as an informant. Location unconfirmed but her captors' bearing from Idoro (west, slightly south) may match the unknown point tied to Mfoniso's own second thread (Ep88). |
| Adaeku | Soldier in Chidebe's garrison at Idoro, quietest of the six informant suspects | Alive. Cleared in practice, if not yet formally: paired with Emenike on the same false route, but his own night proved ordinary — a plain meal alone and sleep, watched the whole while by Osadebe (Ep86). |

### Places
| Name | What it is |
|---|---|
| Kingdom of Ijendu | The nation; ruled by an Eze from the capital |
| Udo | Capital city, seat of the throne |
| Oji Delta | Oil-rich, foreign-exploited delta region |
| Idoro | Village where the story begins, in the Oji Delta |
| Oso | The "forbidden bush" where cursed children are abandoned |
| ak-pu tree | Ancient tree at the boundary of Oso; where abandoned children are laid |
| the Ijoma Concern | Foreign trading House operating through Ebiere, the Factor, and Chiazor; true headquarters revealed in Episode 64 as a disguised trading post several days downriver, kept off the crown's tax records |

### Titles / Concepts
| Term | Meaning in-story |
|---|---|
| Eze | King/ruler |
| Abiku | A child believed to be a spirit that dies and returns to torment its family — the in-world explanation for what the protagonist is believed to be |
| Dibia | Traditional healer/diviner who communes with spirits |

**Rule:** any new named character, village, or title must be added to this
table before or immediately after the episode that introduces them.

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

- **Things Fall Apart**: the Evil Forest / twin-abandonment custom (our Ohia
  Nso), the concept of *chi* (personal guardian spirit/fate — useful
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
active arc — roughly the most recent 15-20 episodes.** Episodes 1-73 are
archived verbatim in `ARCHIVE.md` under "ARCHIVED CHANGELOG"; when this
section grows past ~20 entries, move the oldest ones there following the
same pattern (see Section 10, step 5).

- **CLAUDE.md archive split (2026-07-13):** CLAUDE.md exceeded the
  150,000 character working-memory limit at Episode 78. Split the Living
  Name Registry and Changelog's older history out into `ARCHIVE.md`
  (lossless, verbatim). Section 5 now holds current-status-only entries per
  character with a maintenance rule against re-appending history; Section 11
  now holds only the active arc (Episodes 64-78 onward). Nothing was
  deleted — see `ARCHIVE.md` for the full Episode 1-63 record.
- **Episode 74 — "What Mfoniso Reports" (2026-09-19):** Rather than
  travel home, Mfoniso holes up in a river town two days from Idoro
  and writes the Warden an unflattering, honest account: the
  guardian's reach was badly underestimated, and the true reason she
  was caught was not either old power but Zara's borrowed senses. The
  Warden, revealing the House's guilt over its old lost ground is an
  inherited debt passed down through generations of keepers rather
  than something she witnessed herself, overrules the Factor's renewed
  objection and authorizes Mfoniso to move against Zara directly,
  writing back a single word: proceed. The episode closes on the
  Warden's private unease, quickly folded away with the rest of her
  dangerous archive.
- **Episode 75 — "What Zara's Gift Costs" (2026-09-20):** Zara's
  exhaustion since Episode 70 has only deepened; Amara, Elder Maka,
  Obi, and the council raise gently whether she should step back and
  rest. She refuses to stop listening entirely, agreeing only to
  smaller mercies — fewer duties, Adaugo assigned to sit with her
  through the worst evenings. Chibundu presses the entity on whether
  the cost is dangerous to her; it admits it does not know how to ease
  a burden it did not cause. The episode closes on Mfoniso, watching
  from a careful distance exactly as authorized, noting Zara's
  visible exhaustion as a measurable vulnerability and beginning to
  catalogue Adaugo as another piece worth tracking.
- **Episode 76 — "What the Presence Left in Him" (2026-09-21):** Amara
  finds Kene tracing an unbidden spiral in the compound dirt, the same
  shape Zara once traced under both old powers' touch, and he describes
  the feeling in his hand as a cold like morning water. Chibundu carries
  the discovery straight to the presence, which admits honestly it does
  not know whether its unprecedented reach to save Kene in Episode 70
  left something behind, only that it was rougher and less careful than
  anything it has done before. The entity, weighing the unknown thread
  against the cost Elder Maka's own rite once exacted, counsels watching
  over another hasty severing. Amara brings the discovery to Elder Maka
  rather than sit with it alone; Elder Maka admits she has never
  attempted to cut a thread this new or uncertain and is not confident
  her hands still remember how to do it safely, and instead teaches
  Amara what to watch for — his sleep, his unconscious hand movements,
  whether the cold sharpens or fades. Chibundu tells the presence
  plainly he does not want his brother raised the hard way he himself
  was raised. The episode closes on Amara sitting with a sleeping Kene,
  watching his curled hand for a shape she hopes never to see again.
- **Episode 77 — "The Quiet She Mistook for Peace" (2026-09-22):** Zara
  tells Adaugo she has felt no cold touch in three days and calls it
  earned peace. In Oso, the entity, checking its threads out of old
  habit, finds Zara's grown strangely muffled rather than gone, cannot
  tell whether the cause is her own exhaustion or something acting on
  her too slowly to notice, and tells Chibundu at once rather than
  wait for certainty, naming the possibility that Mfoniso has traded a
  sudden strike for a slow, patient one. Chibundu carries the warning
  to Amara that same night; Zara realizes the quiet she trusted may be
  the loss of the one gift this family has leaned on, and lets Adaugo
  comfort her rather than face it alone. Amara has Chidebe double the
  watch again. The episode closes on Mfoniso's own point of view,
  confirming in the field that her working has already succeeded well
  enough to let her walk closer to Idoro's boundary than she has dared
  since the night she lost Kene, undetected.
- **Episode 78 — "The Stranger at the Grinding Stone" (2026-09-23):**
  Zara tests what remains of her senses alone at the tree line and
  feels nothing answer her. Elder Maka examines her and diagnoses a
  deliberate working rather than exhaustion, recalling her
  grandmother's stories of houses that blind a guardian's watchers
  before striking the guardian itself, and warns that such workings
  require the attacker to have come physically close, repeatedly,
  undetected. Osadebe finds Mfoniso's old footprints on the high
  ground above the compound, confirming it; Chidebe doubles the watch
  a third time. The entity admits to Chibundu it cannot feel Mfoniso
  even knowing what to look for, and the two conclude together that
  she will target whoever stands closest to Zara next. The episode
  closes on Mfoniso herself, disguised as a traveler, gently drawing
  Adaugo's exact routine out of her at the market grinding stone,
  confirming the family's fear one step too late.
- **Episode 79 — "The Third Bend in the River" (2026-09-24):** Adaugo
  mentions to Elder Maka, almost in passing during a rite lesson, the
  friendly traveler who questioned her closely at the grinding stone;
  Elder Maka recognizes the pattern instantly and realizes Adaugo has
  already given away her exact path, hour, and habits. Adaugo leaves
  for Zara's before the warning can reach her, forcing Elder Maka,
  Amara, Obi, Chidebe, and Osadebe into a desperate race for the
  river's third bend. Zara, her senses still muffled, cannot confirm
  danger but trusts the instinct anyway and runs. In Oso, the entity
  feels Idoro's dread spike and, cut off by distance exactly as it was
  the night it could not reach Kene in time, can only warn Chibundu
  that something fast and close to Zara is already happening. The
  episode closes on Mfoniso herself, standing in the center of the
  path in the failing light, telling Adaugo plainly that she has not
  yet decided what she needs from her, and that the choice now belongs
  to whoever is running toward them and what they are willing to
  trade.
- **Episode 80 — "What Adaugo Carried Home" (2026-09-25):** Osadebe
  reaches the third bend in time to force Mfoniso to release Adaugo,
  but not before she grips her wrist, murmurs a few unheard words, and
  vanishes into the reeds leaving no trail at all, a new and uncanny
  capability that unsettles Osadebe more than a clean escape would
  have. Chidebe's search finds nothing; the family reaches Adaugo
  physically unharmed and allows itself real relief, Elder Maka
  declaring her whole after finding no mark. In Oso, the entity reads
  Mfoniso's willingness to be seen and caught as proof she was not
  chased off but finished, telling Chibundu a hunter who needs only
  kindness rather than force is limited by nothing at all. The episode
  closes on Zara, embracing Adaugo in relief on the walk home, feeling
  a cold thread still active on Adaugo's wrist exactly where Mfoniso
  held her, answering her reach the way her own borrowed gift used to
  before it was muffled, proof the danger did not pass. It simply
  changed hands.
- **Episode 81 — "The Thread That Answered Back" (2026-09-26):** Elder
  Maka confirms Zara's discovery herself, barely, before it retreats
  past finding again, and refuses to cut it blind given her own
  uncertain hands and the risk of alerting Mfoniso. Zara offers to be
  a conduit for the presence rather than wait for a slow overland
  consultation, over Amara's objection about the cost to her already
  deep exhaustion. In Oso, the entity tells Chibundu the presence,
  still not recovered from Episode 70's cost, is reaching through Zara
  regardless, and that neither of them has ever successfully stopped
  it when a child of this family is in danger. Reading through Zara,
  the presence identifies the working on Adaugo's wrist as an anchor
  rather than a blindfold, built to always reveal where she stands
  rather than to blind anyone watching over her, meaning Mfoniso no
  longer needs to stand inside Idoro to know what the household is
  doing. The episode closes mid reading as the thread reacts to being
  examined, Zara going rigid and voiceless as something reaches back
  through the open door, the family moving to break the bridge before
  they can learn what noticed them looking.
- **Episode 82 — "The Same Hand" (2026-09-27):** Amara breaks the
  bridge by force and the presence tears itself free of Zara, leaving
  her shaken but alive; Adaugo and Zara name each other family for the
  first time. In Oso, the presence tells Chibundu it recognizes the
  exact craft behind Adaugo's anchor thread as the same technique used
  by the hunter who took its guardian ground three centuries ago,
  meaning Mfoniso inherited her method rather than invented it. Elder
  Maka calls off any further reading or severing until dawn; the
  compound holds its heaviest watch yet, with Osadebe refusing rest at
  the gate. The episode closes on Mfoniso herself, unsettled to have
  felt a guardian reach back along her own working for the first time
  in her career, an experience her teacher once warned meant facing a
  guardian old enough to remember being hunted before, and deciding to
  abandon her patient timeline and move against the family sooner than
  planned.
- **Episode 83 — "A Second Thread" (2026-09-28):** At dawn, Elder Maka
  puts the household's choice to the whole family rather than deciding
  alone: sever Adaugo's still active anchor thread now, losing their
  only lead on Mfoniso, or leave it open and use it, carefully, to
  trace her back. After hearing Obi name the true cost, Adaugo consent
  knowingly, and Osadebe argue a hunter forced to move fast makes
  mistakes, the household chooses to trace. Elder Maka carries the
  reading herself in daylight, with the entity lending support and the
  still weakened presence cautioning restraint, sparing Zara further
  cost. The reading finds Mfoniso's rough distance and direction, then
  something unexpected: a second, thinner thread running from Mfoniso
  herself toward an unknown third point, meaning she is not acting
  entirely alone or entirely by her own will. Mfoniso feels the trace
  find her and severs it before Elder Maka can see who holds the other
  end, then pushes toward Idoro faster than she has allowed herself to
  move in weeks, unsettled that the tie to her own teacher's lineage
  was found rather than kept hidden.
- **Episode 84 — "The Path No One Watched" (2026-09-29):** Chidebe and
  Osadebe convert Elder Maka's rough trace direction into staggered,
  unpredictable patrols. Over three days, reports come back of fresh
  signs of passage always in the one stretch of ground a patrol had
  just left, too precise to be luck. When a route changed inside a
  closed four person meeting is compromised before it even takes
  effect, Osadebe brings the conclusion to Amara directly: someone
  inside Idoro is feeding Mfoniso their movements. In Oso, the entity
  tells Chibundu it would not be surprised if Mfoniso bought eyes
  inside the household rather than out thinking the garrison from
  outside it, warning that a house doubting its own hands does half a
  hunter's work for her. Elder Maka cautions against naming a suspect
  without proof. The episode closes on Mfoniso's own side, confirming
  she receives Idoro's patrol movements through an anonymous bark
  cloth drop point near the market, twice weekly — she does not know
  her informant's face, only that someone inside that grieving,
  guarded household wants her to succeed badly enough to risk
  everything for it.
- **Episode 85 — "Who Among Us" (2026-09-30):** Suspicion spreads
  quietly through Idoro; Amara admits to Obi the shame of watching
  trusted faces differently, and Ozoemena feels doubt land on him
  first, unspoken, because of his own history with the dibia's death.
  Chidebe privately narrows a shortlist of six names against duty
  rosters, finding one, the long trusted soldier Emenike, present at
  every compromised route change, though presence alone proves
  nothing. Elder Maka's warning proves true when two soldiers come to
  blows over unproven suspicion at the well; Chidebe breaks it up and
  bars further accusations without proof brought to him or Osadebe
  first. Osadebe proposes testing the shortlist with deliberately
  false patrol details rather than confronting anyone outright. The
  episode closes on Mfoniso, camped closer to Idoro than she has dared
  since losing Kene, trusting her informant's unbroken reliability
  completely, unaware the household has finally turned its attention
  inward and is about to test that reliability with a lie built to
  catch her listening.
- **Episode 86 — "The False Patrol" (2026-10-01):** Chidebe splits the
  six-name informant shortlist into isolated pairs, each given a
  different fabricated patrol detail, pairing Emenike with the quiet
  soldier Adaeku on a route along the old grain path. Amara presses him
  on the ethics of lying to his own men before making him promise it
  will not become how the household operates. After two tense days,
  only the Emenike-Adaeku route draws fresh signs of Mfoniso's passage.
  That night Osadebe trails Adaeku, whose evening proves ordinary,
  while Chidebe follows Emenike himself and watches him break from his
  usual path after watch, moving in secret toward the market's edge.
  The episode closes mid pursuit, with Chidebe closing the last
  distance behind Emenike toward what can only be the drop point,
  forcing himself forward even as he wishes he had never built the
  test at all.
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
  down and confesses the Ijoma Concern has held his sister captive for
  two seasons, forcing his cooperation from the very first message. The
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

---

## 12. GIT / GITHUB WORKFLOW

At the end of every episode:
```
git add -A
git commit -m "Episode ##: [short title] — [one-line summary]"
git push origin main
```
Never batch multiple episodes into one commit. Never push without first
completing the Section 10 checklist. If a push fails (auth/remote issue),
stop and flag it — don't silently skip it.
