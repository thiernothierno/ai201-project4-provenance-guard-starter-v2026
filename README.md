# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:   
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **`POST /submit` in `app.py`**: receives the request from the writer.
   **Adds:** the `text` and `creator_id`, now inside the service.
2. **Input check inside `submit()`**: rejects text that is missing, empty, or
   longer than ___ characters, returning an error message instead of crashing.
   **Adds:** a guarantee that the text is usable by every step after it.
3. **Signal one, `detector.py → model_signal`**: a local language model (gpt2)
   measures how predictable the text is (perplexity).
   **Adds:** `model_score`, 0–1, higher = more likely AI.
4. **Signal two, `stylometry.py → style_signal`**: measures the shape of the
   text: sentence-length spread, vocabulary variety (type-token ratio), and
   punctuation density, each capped at 1, flipped so higher = more AI, then
   averaged.
   **Adds:** `style_score`, 0–1, higher = more likely AI.
5. **`scoring.py → combine_signals`**: blends the two scores into one.
   **Adds:** a single combined score, 0–1, returned as `confidence`.
6. **`scoring.py → score_to_label`**: compares the score to the thresholds.
   **Adds:** a short `guess` ("human" / "unsure" / "ai") and the `label`
   sentence the reader sees.
7. **`audit.py → log_decision` + the JSON response**: saves the decision with a
   new `content_id`, both signal scores, and the label, then answers the writer.
   **Adds:** a record that `/appeal` can find later, and a response containing
   `content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a language model (gpt2),
measured as perplexity: low perplexity means the model could have guessed the
next word. It is converted to a 0–1 score where higher means more likely AI.

**Why that might differ between human and AI writing:** A language model writes
by repeatedly choosing a likely next word, so AI-generated text tends to be easy
for a model to predict. Human writing wanders more: unusual word choices, abrupt
turns, specific details instead of typical ones.

**What it can't see:** Predictability is not authorship. Plain human writing
(common words in short, ordinary sentences) looks just as predictable as AI
text. That includes people writing in a second language, younger writers, and
anyone writing simply on purpose. The reverse also happens: dense prose full of
rare words can score as human even if a model wrote it. The writers this signal
is most likely to wrongly accuse are the ones with the least room to argue back.

### Signal two — the style signal

**What it measures:** The shape of the text, without reading its meaning. Three
measures, each turned into a 0–1 "AI-likeness" score and averaged:
- **Sentence-length spread:** how much sentence lengths (in words) vary
  (standard deviation ÷ mean). Low spread → more AI-like.
- **Type-token ratio:** distinct words ÷ total words. Repetitive vocabulary →
  more AI-like.
- **Punctuation density:** punctuation marks per word. Little punctuation → more
  AI-like.

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences and a narrower, "safe" vocabulary, because
that's what choosing the most likely next word produces on average. Human writing
is lumpier: a three-word sentence next to a forty-word one, asides in dashes or
parentheses, odd word choices.

**What it can't see:** It cannot read. Anything that changes the shape without
changing the content moves the score: adding typos, splitting or joining
sentences, sprinkling in punctuation, or pasting in a quotation. These are cheap,
deliberate edits. It also can't tell plain human writing from AI: in my tests, a
plain human paragraph had a punctuation density of 0.125, almost the same as AI
samples (0.106–0.136). Very short texts are also unreliable: a single sentence has
no spread at all, and text with no words returns 0 for every measure.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** <!-- TODO (Milestone 4): write your rule in words once you've
built combine_signals. Starting point in config.py: a 50/50 weighted average. -->

**The numbers:** <!-- TODO: e.g. "0.5 × model_score + 0.5 × style_score" —
must match scoring.py. -->

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
<!-- TODO (Milestone 4): run detector.py and stylometry.py on the same text,
     find one where the scores disagree, paste both numbers here. -->



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | <!-- TODO (Milestone 5) --> |
| unsure | 0.35 – 0.65 | <!-- TODO (Milestone 5) --> |
| high-confidence AI | 0.65 – 1.00 | <!-- TODO (Milestone 5) --> |

<!-- Ranges above are the current config.py placeholders (HUMAN_THRESHOLD = 0.35,
     AI_THRESHOLD = 0.65). Update them if you change config.py. -->


**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
