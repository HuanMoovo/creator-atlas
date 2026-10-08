# Creator Atlas · Method Domains · Editing & Post-Production

> Positioning: This page covers how footage becomes a finished cut an audience will stay with, across the whole chain from footage organization, rough cut, fine cut, sound, subtitles and packaging to export and delivery.
> Companions: Script & Storytelling, Production & Shooting, Growth & Analytics and `docs/genres/` (editing conventions by content type).
> Note: Statements about platform mechanics follow public sources and official documentation (verified 2026-10); confirm against the latest official wording before acting.

---

## 1. What This Stage Solves

Editing is the second screenwriting pass: structure, pacing and emotion take their final shape here, and whether the audience keeps watching is decided mostly at the editing table. Footage that was not shot well can be rescued to a passing grade at best; footage that was shot well still needs editing to become genuinely good.

The four problem types this stage solves:

1. **Structure**: piles of footage, no storyline. The shooting order is not the telling order; most obvious when you shoot first and cut later.
2. **Pacing**: the structure is right, but it still drags. When viewers are choosing between faster playback and swiping away, information density is usually too low.
3. **Sound**: the picture is fine but the audio is not: levels swing up and down and music covers the voice, most obvious on a phone speaker.
4. **Delivery**: typos in subtitles, corner logos covering content, export specs that miss platform requirements. The content is not bad; it dies in the final 10%.

This page covers the full post-production chain from footage organization to the exported cut: media management, rough cut, fine cut, sound, subtitles, packaging, export and self-check. On-set execution details are in Production & Shooting, titles and thumbnails in Packaging & Distribution, and post-publish data reading in Growth & Analytics.

## 2. Core Framework

### 2.1 Seven Stages, One Problem Type Each

Most editing rework traces to the same root cause: stages mixed together. Give each stage a defined responsibility, and move on only after its pass criteria are met:

| Stage | Owns | Key Actions | Pass Criteria |
| --- | --- | --- | --- |
| Footage organization | Findability | Back up, import, partition by camera and scene, tag usable takes | Any clip can be found within 10 s |
| Rough cut | Structure | Build the spine from the script, ignore the details | The storyline reads even with the sound off |
| Fine cut | Pacing | Trim section by section, cut redundancy, work the joins | At normal speed, nothing drags |
| Sound | Listening | Dialogue cleanup, music, sound effects, loudness normalization | Every word is clear on a phone speaker |
| Subtitles & packaging | Readability | Subtitles, corner logo, progress bar, motion graphics | No typos; packaging does not steal the scene |
| Export | Delivery | Output to platform specs | Parameters match the spec table in §5 |
| Self-check | Final gate | Run the full checklist in §5 | Publish only when the checklist fully passes |

One discipline: return to an earlier stage only when the current stage's criteria fail. The rough cut touches no transitions and no color grading: change the structure and all of that work is redone.

### 2.2 Pacing Principles

The standard for pacing is simple: waste none of the viewer's time. Put the principle into concrete moves:

**Cut.** Ask every section the same question: if it were removed, would understanding suffer? If not, cut it. Opening setup, repeated explanations and slow passages are the first candidates. Adding back after cutting too much is easier than patching clutter later.

**Information density.** Use the retell test: after a minute of watching, can the viewer recount 2–3 key points? If not, some section carried no new information. Write a one-line purpose for every section; one that cannot get a purpose is cut or merged into its neighbor.

**Joins.** The J-cut and the L-cut are the two basic moves that smooth a shot change; transitions and pauses work the same way, all used with restraint:

| Move | Effect | Typical Use | Restraint |
| --- | --- | --- | --- |
| J-cut (sound first) | The next section's audio arrives early, previewing information or emotion | Scene changes; interviews cutting to B-roll | Lead time commonly 0.5–1.5 s, tuned to the speech rate |
| L-cut (picture first) | The picture cuts away while the previous section's audio continues | Dialogue joins, flashbacks and memories | Same basis as J-cuts; every use has a purpose you can state |
| Jump cut | Compresses time by dropping the middle | Cutting sections from a monologue; cutting waits from a tutorial | Keep camera and shot size steady within a section; place cuts at semantic pauses |
| Hard cut | The default join | Between the vast majority of shots | No jump in time or place, no transition added |
| Time-space transition | Marks a change of time or place | Chapter changes; outdoor location jumps | Keep to 2–3 styles per video; one meaning, one style |
| Pause | Lets information settle and leaves room for emotion | After key conclusions; before emotional turns | Hold 0.5–1 s after key lines; never cut it out entirely |

**Restraint with jump cuts, transitions and pauses.** A transition is punctuation, its only job to flag a change of time or place. The jump cut is the cheapest way to compress time; too dense and it reads as cheap, and several jumps in a row make the audience notice the jumping itself. Pauses are the opposite: hold the 0.5–1 s after a key line so the information is absorbed. Self-check with net speaking time: after 30–40 s of unbroken dense delivery, schedule a picture change or a stretch of buffer footage (Basis: common practice for knowledge monologues; interviews and documentaries can relax it).

### 2.3 Sound Design

Audio priority runs high to low: **dialogue > music > sound effects**. Make the voice intelligible first, pleasant second; clean the dialogue with noise reduction, de-plosive and level alignment, and handle loudness uniformly before export. Mixing layers and their level basis:

| Layer | Content | Level Basis (vs. Dialogue) | Check |
| --- | --- | --- | --- |
| 1 | Dialogue and voice | The reference layer, consistent across the video | Every line clear on a phone speaker |
| 2 | Music | Pulled down 6–12 dB under dialogue | Eyes closed, no word sounds covered |
| 3 | Sound effects | Never above dialogue; accent hits may briefly approach it | Ask: would removing it hurt understanding? |
| 4 | Ambience and room tone | The bottom bed, competing with nothing | Any hum or noise in quiet passages? |

**The three-part music method.** Treat music as a structural tool, not as background filler:

- **Entry**: set the tone in the opening seconds with the level low so the first line is clear (Basis: with voice in the opening, music stays ambient only).
- **Emotional anchor**: lift it at a section turn or where the argument advances; 1–2 places per video is enough. One intensity from start to finish means no contrast at all.
- **Close**: settle back to calm at the end, give the audience a sense of closure, and avoid cutting off mid-crescendo.

**Ducking.** Music drops when dialogue appears and recovers after it ends; side-chain compression is the standard approach, commonly pulling 6–12 dB. Hand-drawing volume automation also works: more control, more time. Acceptance test: listen once with eyes closed; no line may be covered.

**Sound-effect accents.** Transition stings, action sounds (typing, page turns, clicks), accent hits. Sound effects serve understanding and a sense of space; as a density guide, no more than one accent per 10–20 s. Fix one sound pack to keep a series consistent (Basis: tutorials can run denser; interviews mostly add none).

**Loudness and real-world tests.** Mainstream streaming platforms reference loudness around -14 LUFS (integrated), and they normalize material that strays far from it; keep true peak within -1 dBTP (Basis: algorithms and thresholds differ by platform; check official documentation and your own tests before publishing). Before export, always run the **phone-speaker test**: listen once on the phone and once on headphones, confirming every line of dialogue is clear.

### 2.4 Subtitles and Readability

Subtitles have exactly one goal: let viewers keep up without effort. The standing specs, in numbers (Basis: set against the two mainstream aspect ratios; verify with a phone preview before publishing):

| Item | Landscape (1920×1080 baseline) | Vertical (1080×1920 baseline) | Notes |
| --- | --- | --- | --- |
| Type size | Glyph height about 3%–5% of frame height | 4%–6% | Err large rather than small; check the phone preview first |
| Characters per line | 15–20 | 8–12 | Wrap when exceeded |
| Lines per screen | 2 max | 2 max | Three or more and viewers cannot finish reading |
| On-screen hold | Follows the voice, never under 1 s | Same as landscape | Split the screen if it does not fit; do not stretch the hold |
| Safe zone | Avoid platform UI overlays | Keep key information out of the bottom 15%–20% of height | Verify with the platform preview before publishing |

**Line-break discipline.** Break at complete meaning units and at speech pauses; never split a phrase, never separate a number from its unit. Read the subtitles aloud once: if it does not flow, the breaks are wrong.

**Full proofread discipline for auto-captions.** After automatic recognition, go through the whole text word by word against the audio, focusing on proper nouns, names, numbers, industry terms, verbal tics and repeated words. Proofread once from the subtitle file alone, without the picture: that pass catches errors the eye skips while watching. Subtitle text gets searched and reused, so hold it to the standard of a formal document.

### 2.5 Packaging

Packaging is signage: it helps viewers orient themselves, and it is wrong the moment it steals the scene. The elements and their restraint:

- **Corner logo and credits**: fixed position, fixed size, covering no key information; always on through the video, or only at the head and tail. Pick one and keep it consistent.
- **Progress bar and chapters**: for content over 10 min, add chapters or a progress bar; it makes rewatching easier and helps completion.
- **Motion graphics**: keep two uses only: emphasizing key information and marking changes of time or place. An effect on every point turns attention from the content to the effects.
- **Brand consistency**: fonts (1–2), main colors (2–3), subtitle style, sound pack and logo position fixed as one set, unchanged within a series.
- **Intro**: keep it within 5 s or skip it; the rule of experience is that the longer the intro, the faster viewers leave.

## 3. Workflow & Steps

Turn the framework into a repeatable process. Solo creators run it per project; teams write the same standards into their working agreements.

**A. Footage organization (done on shoot day or the next day)**

1. Backup: keep two copies of the footage (local drive plus a second drive or the cloud); keep the memory cards until after the finished video is published.
2. Set up the project: copy the project folder from a fixed template (structure at the end of this section).
3. Import and partition: create bins by camera or scene; delete obvious rejects and tag the usable takes.
4. Generate proxies: for footage above 4K or at high bitrate, make 1080p proxies for the edit, then relink the originals before export.

**B. Rough cut (owns structure)**

1. Listen through the recordings or skim the footage, and pick the good takes (selects); this step is selection only, no polishing.
2. Build the spine from the script: first the who, what happens and the conclusion; log missing shots on a pickup list.
3. Play it back muted: wherever it stops making sense is a structural gap; go back and add footage or a bridge.

**C. Fine cut (owns pacing)**

1. Trim section by section: cut pauses, cut repeats, work the jump-cut points.
2. Add joins: J-cut / L-cut, B-roll coverage, key-point text cards.
3. Watch it twice: once at normal speed for pacing, once at 1.25x to catch drag.

**D. Sound**

1. Clean the dialogue: noise reduction, de-plosive, fix level jumps.
2. Lay the music: arrange by the three-part method and duck it.
3. Add sound effects: only those that serve understanding.
4. Normalize loudness: hit the platform reference level, then test on speaker and headphones.

**E. Subtitles and packaging**

1. After auto-captioning, complete the full proofread (discipline in §2.4).
2. Unify line breaks and styles; add the corner logo, progress bar and motion graphics.

**F. Export and self-check**

1. Export to the spec table in §5.
2. Run the §5 self-check list in full; failed items go back to their stage for a fix, and publish only after a full pass.

**Project standards**

Folder structure (save it as a template and copy it for every new project):

```text
project-name_date/
├── 00_materials/   # Scripts, storyboards, references
├── 01_footage/     # Partitioned by camera or scene
├── 02_project/     # Edit project and autosaves
├── 03_audio/       # Recordings, music, sound effects
├── 04_subtitles/   # Subtitle projects and exported files
├── 05_exports/     # Finished cuts and platform versions
└── 06_publish/     # Thumbnails, titles, descriptions
```

Naming rules:

| Object | Format | Example |
| --- | --- | --- |
| Footage | date_camera_scene_index | 20261005_A_Opening_001 |
| Project | project-name_vMajor | my-video_v03 |
| Export | project-name_platform_aspect_vVersion | my-video_bilibili_landscape_v3 |
| Subtitles | project-name_language_status | my-video_zh_proofread |

Versions and autosave:

- Set autosave every 5–10 min; before any major change, manually save a new version number.
- Export file names carry the version number and map one-to-one to the publishing assets; clear out old versions only after delivery and footage archiving are done.
- Regularly package and archive the project, subtitles and exports together; before deleting any footage, confirm the finished video can be rebuilt.

Proxy editing basis: switch to proxies only after confirming playback really stutters on your machine. When footage resolution or bitrate exceeds what the edit machine handles smoothly, transcode to a 1080p intermediate format (ProRes Proxy or similar) for editing; relink the originals before export, and spot-check 2–3 points in the output for frame alignment.

## 4. Templates & Tools

Tools are chosen by stage: light pipelines run from start to finish in one all-in-one tool; long videos and teams split by stage. Common options:

| Tool | Role | Best Stage | Cost Basis | Notes |
| --- | --- | --- | --- | --- |
| Jianying / CapCut | All-in-one: editing, auto-captions, templates and a sound library | Full pipeline for talking-head and short video | Free tier works; membership unlocks some assets and features | Auto-captions are a starting point; still proofread in full |
| Premiere Pro | Professional editing; mature plugin and collaboration ecosystem | Full pipeline for mid-length and long video | Subscription | Integrates easily with other Adobe apps |
| Final Cut Pro | Professional editing on the Mac | Full pipeline for mid-length and long video | One-time purchase | Magnetic timeline; efficient for solo work |
| DaVinci Resolve | Editing, color grading and audio in one | Full pipeline, especially color and sound | Full-featured free tier | The free tier covers most solo needs |
| Text-based and AI-assisted tools | Edit from a transcript, strip silences and filler words, search footage by description | Footage organization and rough cut | Mostly subscription or usage-based | Output must pass human review before use |

- Entry points and templates: [Software & Tools](../../resources/software.md) (software list) and [Checklists & Templates](../../templates/README.md) (publishing checklists and other templates).
- Project template: save the folder structure, naming rules, track layout, subtitle style and export presets into one empty project; copy it for each episode instead of rebuilding, and setup time halves.

## 5. Data & Acceptance Criteria

After exporting the cut and before publishing, run the list below in full. It corresponds to the self-check stage in §2.1 and is this stage's passing line:

| Check | Action | Pass Criteria |
| --- | --- | --- |
| First 3 seconds | Watch the first three seconds on their own | Someone with no background still gets what this is about and why to keep watching |
| A/V sync | Spot-check 3–5 points of lip and voice | No perceptible offset (Basis: no audible anomaly on normal playback is enough) |
| Pacing scan | One full pass at 1.25x | Nothing rushed or jumpy; you can still name the sections that drag |
| Speaker check | One pass on phone speaker, one on headphones | Every line clear; no clipping, no level jumps |
| Full subtitle check | Word-by-word pass against the audio | Zero typos; breaks split no phrases and no sentences across screens |
| Packaging check | Inspect the positions of corner logo, subtitles and motion graphics | Nothing covers key information or crosses the safe zone |
| Export specs | Verify resolution, frame rate, bitrate and file name | Matches the spec table below; the platform preview looks normal |
| Post-upload review | Preview once after the platform finishes transcoding | Picture and sound normal; subtitles aligned |

Platform export specs (common basis; re-check each platform's official documentation before publishing):

| Class | Resolution | Frame Rate | Bitrate Guide | Format & Audio |
| --- | --- | --- | --- | --- |
| Landscape 1080p | 1920×1080 | 24 / 25 / 30, matching the shoot | H.264 around 8–16 Mbps | MP4, H.264 + AAC 192–320 kbps |
| Landscape 4K | 3840×2160 | Matching the shoot; 60 for sports and games | H.264 around 35–68 Mbps, upper end for high frame rates | MP4; H.265 can lower the bitrate by about half |
| Vertical 1080p | 1080×1920 | 30 or 60 | H.264 around 6–12 Mbps | MP4, H.264 + AAC |
| Vertical 4K | 2160×3840 | 30 or 60 | Follow the platform's upload guidance | Most vertical platforms still treat 1080p as the safe tier |

Basis notes:

- The bitrate figures are common ranges: above the platform's transcode tier it recompresses anyway, far below and the picture goes soft. Keep one frame rate across the video; conform mixed-frame-rate footage to the main timeline before the output.
- Output color to standard platform requirements (Rec.709 for SDR); confirm platform support before running an HDR workflow. Export file names carry the project name, platform and version number, mapping one-to-one to the publishing assets.

Post-publish calibration (ties into Growth & Analytics):

- Review the retention curve 24–48 h after publishing: drop-off in the first 30 s points to the opening and hook edit; unusual mid-video drop-off points to pacing and sound.
- Compare against the median of the last 10 videos of the same type and length band; adjust the editing approach only when clearly below the baseline, and never treat a single video's swing as a decision basis.

## 6. Common Mistakes

1. **Straight to the timeline without organizing footage**: shots go missing mid-edit and takes cannot be found; rework doubles.
2. **Doing fine-cut work during the rough cut**: the structure changes and every transition and grade is thrown away.
3. **Unwilling to cut**: three hours shot means three hours shipped. Cutting is the main work of editing.
4. **Transition abuse**: a new transition every section looks amateur; fix one style per meaning and stay within 2–3 for the whole video.
5. **Music over the voice**: the song was picked before the listening test, forgetting the audience came for the voice; dialogue first, music second, always.
6. **No level matching**: levels jump between sections and viewers keep adjusting the volume; normalize loudness and test on a speaker before export.
7. **Auto-captions with no proofread**: wrong names and numbers ship in the cut and professionalism drops to zero.
8. **Subtitles packing the screen**: three-plus lines and edge-to-edge type leave viewers reading text and missing the picture.
9. **Piling on motion graphics**: an effect on every point turns attention from content to effects.
10. **Guessing at export specs**: too-low bitrate and mixed frame rates get recompressed by the platform and the picture collapses.

## 7. Where to Go Deeper

- **Motion graphics and shapes**: visualizing key information (data, processes, comparisons), subtitle animation, simple animation. Priority order: what improves understanding comes first, pure decoration later; the built-in graphics modules of your editing software cover most needs, and only complex work justifies dedicated software.
- **Color grading basics**: finish primary correction first: matching exposure and white balance across cameras, fixing color casts and matching shots; then move to a stylistic grade. Series content fixes one color base; a LUT is the starting point of the process, and you still fine-tune it to the footage.
- **Templates and batch production**: fix the intro, subtitle style, corner logo, transition sounds and export presets into templates; start each series episode from the same project and the repeated decisions drop to zero.
- **Templated projects and collaboration**: write the folder structure and naming rules from §3 into team agreements; multi-person work uses one project template and version naming, and the handoff basis is stated once.
- **An editing review habit**: every 10 episodes, rewatch your own cuts, list the recurring problems and fix them in the next batch; editing skill comes mostly from this loop (for the data comparison routine, see Growth & Analytics).

## Further Reading

- [Script & Storytelling](script.md): the script sets the structural skeleton; editing runs the final checks against it (§2, §3).
- [Production & Shooting](production.md): footage quality and backup discipline start here and set the ceiling for editing.
- [Growth & Analytics](growth.md): how to read retention curves and completion data, and how to trace them back to editing problems (§2, §4).
- [Production Methods](../genres/README.md): the concrete editing conventions and time structures by content type.
- [Resources & Tools](../../resources/README.md): entry points for editing software, footage and audio resources.
