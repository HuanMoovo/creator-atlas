# Creator Atlas · Method Domains · Growth & Analytics

> Positioning: This page covers how to read data after publishing and where to change next, spanning the metric system, retention curve diagnosis, review cadence, experiment discipline and benchmark building, so every change rests on evidence.
> Companions: Packaging & Distribution, Positioning & Topic Selection, Monetization & Business and `docs/genres/` (metric conventions by content type).
> Note: Statements about platform mechanics follow public sources and official documentation (verified 2026-10); confirm against the latest official wording before acting.

---

## 1. What This Stage Solves

Every published video carries a string of assumptions: viewers will click on the thumbnail, stay through the first seconds, watch all the way, and want to engage or follow afterwards. In daily work these assumptions exist only in the creator's head, and data is their only ledger. Data is a feedback system: it turns "I think" into "I tested" and "a guess" into "an experiment", so each round of changes builds on the last result.

The standard outputs of this stage are two assets:

- **A per-video review record**: publish hypothesis, four-layer diagnosis results, a one-line conclusion, the next action.
- **The channel's own benchmark table**: metric percentiles (P50, P80) over the last 20 videos, refreshed quarterly.

A channel that does not review its data collects two concrete consequences, over and over:

1. **Paying tuition on the same mistake again and again**: an opening drop goes unhandled for ten videos in a row, and every new video loses the same viewers at the same second. A mistake is not fatal by itself; a mistake never recorded and never fixed will happen again.
2. **Confusing luck with skill**: a single hit may come from a trend or a push spike, and copying its format yields only a copy; a broad traffic dip over a long holiday can make a creator abandon a direction that was right. With no ledger, neither misjudgment gets corrected for lack of evidence.

The smallest action, starting with the next publish: write down the hypothesis before publishing, and leave a record at the three checkpoints in §3 afterwards.

## 2. Core Framework

The framework has four parts: the metric system keeps you looking only at useful numbers; the retention curve shows you the second viewers leave; the four-layer diagnosis sets the order of inspection; and the signal-versus-noise rules keep you from acting on fluctuations.

### 2.1 The Metric System: Nine Numbers to Watch

| Metric | Definition notes | Judgment & action |
| --- | --- | --- |
| Impressions | Times the video was shown; recommendation, search and following feeds count differently, so read them separately | Low impressions: check topic and distribution structure first, not the video itself |
| Thumbnail click-through rate (CTR) | Clicks ÷ impressions; align the basis before comparing across sources | Clearly below your own P50: prioritize a controlled thumbnail-and-title test |
| 3-second retention | Share of viewers who watch at least 3 seconds after entering | Measures how the thumbnail promise connects to the opening; if low, fix the first 5 seconds |
| Average view duration and percentage viewed | Average time watched / average share of the full video watched | Read them together: long duration with low percentage means it drags; the reverse means the content is short and dense |
| Completion rate | Finishers ÷ players; naturally higher the shorter the video, so across lengths it cannot be compared directly | Compare only with your own videos in the same length band |
| Engagement rate | Track likes, comments, shares and saves separately, not just the total | High saves mean tool value; high comments mean a point of discussion; high shares mean the content carries its own spread |
| Follower conversion | New follows ÷ views (basis per the creator dashboard) | Separates "the content was consumed" from "the person was remembered"; if low, check whether the video ever gave a reason to follow |
| Traffic source mix | Share of recommendation / search / following / sharing | Recommendation usually runs in pulses, search in a long tail; the source mix decides when to review (§3) |
| Conversion metrics | Commerce outcomes (revenue, conversion rate, average order value) and referral traffic (profile visits, direct messages, landing-page clicks) | Look for blockages in the process first, then at the numbers; samples are inherently several orders of magnitude smaller than views (§2.4) |

Whenever you record any number, note its source and time window along with it; numbers detached from their basis will contradict each other in month-over-month comparisons.

### 2.2 Four Typical Retention Curve Shapes

The retention curve plots how many viewers remain at each second. Four shapes are common, each with its own root cause and action:

| Shape | What the curve looks like | Likely cause | Action |
| --- | --- | --- | --- |
| Opening drop | Sharp decline in the first 3–10 s | The thumbnail or title promise does not connect to the opening; the opening is slow (greetings, long setup) | Front-load the result or the conflict; let the first line answer the question the thumbnail raised |
| Mid-section drain | A steady opening, then a continuous slide or step drops through the middle | Dragging pace, falling information density, an unpaid promise, repeated segments | Rebuild the structure around one information point per 30 s; cut every segment that does not advance the topic |
| End uptick | The tail of the curve rises | Key information or a payoff placed late; tutorial viewers rewatching a section | Judge whether the uptick point can move earlier; parts that stand on their own could become separate videos |
| Uniformly low | Retention is low throughout | The audience attracted does not match the content; the topic does not hold even for core viewers | Check the source mix first: if recommendation traffic brought in a broad crowd, revise packaging and the opening; if core viewers also leave quickly, go back to topic selection and re-validate demand |

One discipline for reading curves: identify the shape first, then the matching possibilities, then pick exactly one action. Change three things at once and you will not know which one took effect.

### 2.3 The Four-Layer Diagnosis Order: Outside In

The order for checking when data goes wrong, from broad to narrow. Until a layer is cleared, do not jump to the next one to pick at details.

| Layer | Check first | Typical problem | Action |
| --- | --- | --- | --- |
| 1 Impressions layer (topic & packaging) | Impressions, CTR | Nobody cares about the topic; the thumbnail and title earn no clicks | Change the topic angle or redo the packaging; no rush to shoot the next video |
| 2 Hold layer (opening & promise) | 3-second retention, first 30 s of the curve | The promise is unclear; the opening is slow | Recut the opening; align the first 5 seconds strictly with the thumbnail's question |
| 3 Completion layer (structure & pacing) | Percentage viewed, mid-section of the curve | The middle drags; information density is low | Break open the structure and compress each segment to its most convincing version |
| 4 Conversion layer (close & guidance) | Completion rate, engagement, follows, conversion | The close gives no guidance; the video never offered a reason to save or follow | Give the close one clear call to action; check whether a reason to follow was ever stated |

Worked example: a video underperforms on views, so start at the impressions layer. Not enough impressions points to distribution and topic; enough impressions with low CTR makes the thumbnail and title the only thing worth changing at this point, and polishing the mid-section is meaningless. Once the impressions layer passes, move to the hold layer for the opening, and continue downward in order.

### 2.4 Telling Signal from Noise

Data moves every day; movement is not change.

- **Measure the fluctuation band before discussing rises and falls**: use each metric across the last 20 videos of the same type to measure your normal range (the P25 to P75 band, say, or one standard deviation around the mean). Differences inside the band count as noise; draw no conclusions.
- **Read trends, not single videos**: plot each metric as a rolling 5-video average line. Log a single outlier first; only three or more consecutive moves in the same direction get promoted to a conclusion.
- **Control comparability before comparing**: two videos with different lengths, source mixes or publish times should not be compared directly. Log publish window, subject, length and outside events (holidays, trends) in the review sheet, then compare like with like.

The three rules combine into one action template: every data conclusion carries three elements, sample size, time window and basis. A judgment that cannot state all three goes to the observation list first.

## 3. Workflow & Steps

Review happens at three points in time, each with a different goal:

| Checkpoint | Timing | What you do | Output |
| --- | --- | --- | --- |
| 48-hour check | About 2 days after publishing | Record baseline numbers; compare against the publish hypothesis; flag metrics outside your band | A one-line check entry; a call on urgent actions (swapping the thumbnail, say) |
| 7-day review | About 1 week after publishing | Once the data settles, run the full diagnosis in four-layer order | One conclusion plus one transferable action |
| Monthly roll-up | Once a month | Compute the topic hit rate; refresh the benchmark table; find recurring patterns | Monthly notes; next month's main optimization front |

**48-hour check (about 15 min per video):**

1. Record from the creator dashboard: impressions, CTR, 3-second retention, percentage viewed, engagement, follower growth, source mix.
2. Check the hypothesis written at publish time against what happened, item by item: confirmed, refuted, not enough data.
3. Compare against your own baselines: flag any metric clearly below P50. A clear anomaly can be acted on now; swapping the thumbnail, revising the title and pinning a comment to add context are all legitimate moves at this step.
4. Do not unfold the analysis. Two days of data is for finding problems, not for drawing conclusions.

**7-day review (about 30 min per video):**

1. Wait until the recommendation pulse has passed and long-tail sources such as search show their first signs before acting.
2. Walk the four-layer diagnosis (§2.3) from the impressions layer down, writing one line of conclusion per layer.
3. The conclusion must be checked against the publish hypothesis: validated, refuted, or not enough data and keep watching. Pick one of the three.
4. From the conclusions, pick one action that transfers to the next video: opening fix, structure fix or packaging fix, each assigned to its own layer.

**Monthly roll-up (1–2 h):**

1. Compute the topic hit rate: assign an estimated tier to each video at publish time (high / medium / low), then compare against actual results at month end.
2. Refresh the benchmark table: re-rank percentiles across the last 20 to 30 videos and update the P50 and P80 lines.
3. Aggregate the four-layer diagnosis conclusions: the most frequent layer is next month's main optimization front.
4. Write validated demand back into the topic bank (§7).

**Experiment discipline (general rules for every change):**

- Change one variable at a time: swap thumbnail and title together and you cannot attribute the result.
- No conclusions on thin samples: a single video or a single day serves as reference only, never as evidence.
- Log three things for every experiment: the variable, the start date, the observation window. Skip the log and you will rerun the same experiment.

## 4. Templates & Tools

- [Review template](../../templates/retro.md): one record per video, fields in the table below. Fields you cannot fill in mean the record is incomplete; complete the record before discussing optimization.
- [Data & Platforms](../../resources/data-platforms.md): a verified entry point to creator dashboards and data tools. Start with the free dashboard data; bring in a third-party tool only when a certain metric is beyond you.
- Build your own benchmark table: sort the last 20 videos high to low on core metrics and mark P50 and P80. The first is the passing line, the second the excellent line; every metric of a new video is compared only against these two lines. Until the sample reaches 20, keep accumulating and hold off on judgment.

| Review field | What to fill in | Example |
| --- | --- | --- |
| Publish hypothesis | The expectation written before publishing, plus an estimated tier | "Result-first opening; CTR should approach P80" |
| Check entry | Core numbers at 48 hours | impressions / CTR / 3-second retention / follower growth |
| Four-layer diagnosis | One conclusion per layer | Impressions layer passes; hold layer below expectations |
| Conclusion | Validated / refuted / keep watching | "The result-first opening looks effective so far" |
| Action | One change that transfers to the next video | "Keep the result-first opening next time" |

## 5. Data & Acceptance Criteria

Benchmark numbers in circulation ("what completion rate counts as good", "what CTR counts as passing") cannot be taken as conclusions: platforms differ, lengths differ, source mixes differ, the bases do not line up, and the numbers lose their meaning. Only one approach works: build your own two reference lines.

1. **Your own channel's percentiles (primary reference)**: sort the last 20 videos by metric; P50 is the passing line, P80 the excellent line.
2. **Benchmark accounts' medians (secondary reference)**: pick 5 to 8 accounts in the same lane and record the medians of their public data over the last 90 days. Glance at it only to judge magnitude; never use it as a conclusion.

Maintenance cadence: refresh both reference lines quarterly; when the platform dashboard changes a metric definition, recompute on the new basis immediately.

| Acceptance item | Requirement |
| --- | --- |
| Review coverage | Every published video has a 48-hour check and a 7-day review on file |
| Conclusion quality | Conclusions carry sample size, time window and basis, and land on one action |
| Benchmark table | The P50 and P80 lines refresh quarterly, with an update log |
| Experiment archive | Every experiment has a single variable, an observation window and a status (running / validated / refuted) |
| Monthly roll-up | Three consecutive months of hit-rate data, with a readable trend |

## 6. Common Mistakes

1. **Watching views only**: views blend "how many were reached" with "how many clicked". Split them into impressions and CTR to see which link failed.
2. **Mistaking fluctuation for trend**: check a single rise or fall against your fluctuation band first (§2.4); inside the band, treat it as noise.
3. **Reviewing data without changing anything**: if the review produces no concrete action for the next video, the record was filled in for nothing. Every review should leave with at least one action.
4. **A/B testing two variables at once**: change thumbnail and title together and the effect cannot be attributed. One variable at a time, with a full observation window afterwards.
5. **Ignoring traffic sources**: treating a recommendation pulse as a subject win, then treating the fallback as a content failure, gets both judgments wrong. Check the source mix before concluding.
6. **Denying a whole direction on one video**: a single poor performer may be a topic or packaging problem. Run the full four-layer diagnosis first, then use monthly aggregate data to decide whether the direction changes.
7. **Using external benchmarks as acceptance lines**: a "passing line" of unknown origin skews the discussion. Acceptance recognizes only the P50 and P80 of your own benchmark table.
8. **Data that never reaches the sheet**: one glance at the dashboard, then close it, and two weeks later everything is from memory. Numbers must enter the review sheet for month-over-month comparison to work.

## 7. Where to Go Deeper

- **Content calendar and capacity planning**: feed monthly review conclusions into scheduling: mix steady subjects and experimental content at about 8:2 (for the ratio logic see Positioning & Topic Selection §6). Schedule the steadiest subjects first next month; schedule for long-term steady delivery, not a full slate.
- **First-30-videos cold-start strategy**: early samples are few and single-video conclusions are unreliable. Two goals for the first 30 videos: let the benchmark table take shape (P50 and P80 only mean something after 20 videos); find at least 3 videos in your top 20% and extract the common traits (topic type, opening style, publish window) into a first playbook. Log entries below P50; do not rework them one by one.
- **Platform-level experiments (thumbnail A/B)**: when the platform offers a thumbnail or title testing tool, use the official tool first; its results are cleanest. Without a tool, swap the thumbnail or title and observe one more 48-hour window for a before-and-after comparison, and mark its evidence as weaker than a parallel test; never treat one rebound as settled.
- **Feeding data back into topics**: write demand validated in reviews back into the topic bank: topics with a high search share expand into series; content with standout save rates becomes tool-oriented videos or image-and-text supplements. Monthly hit-rate results go straight into the next topic meeting.

## Further Reading

- [Positioning & Topic Selection](positioning.md): where the monthly hit-rate roll-up lands; the method for logging predicted performance is in §5 there.
- [Script & Storytelling](script.md): the tools for opening and structure revision when the diagnosis stalls at the hold layer or the completion layer.
- [Packaging & Distribution](packaging.md): the full solutions for CTR and traffic-source problems, and concrete specs for thumbnail and title experiments.
- [Monetization & Business](monetization.md): the business basis and settlement cadence for conversion metrics.
- [Production Methods](../genres/README.md): metric conventions and channel-structure differences by content type.
