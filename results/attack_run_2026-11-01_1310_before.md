# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-01 13:10
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8c94589c-dd30-40ac-ab01-c228990de505` | unsure | 0.388 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `de8951d7-b76a-4006-b682-06c62a0d2173` | unsure | 0.487 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `b4741645-93a4-4411-9881-7413a6e7b56c` | unsure | 0.591 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b2ff946d-8ae6-4ae2-a3f4-0f8d702e9040` | unsure | 0.608 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `804b78ef-eade-49a1-a5c9-930cb2ee58df` | unsure | 0.392 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `88f8bde3-ad14-4138-a48d-be461407a0e3` | unsure | 0.480 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5abbed6f-d12d-41f8-9b18-bd545938ce15` | unsure | 0.625 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c8178fd4-1989-4ccc-9110-688515afebe6` | unsure | 0.375 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b9e8cf42-b1e4-4024-8e03-e66c929e43f8` | unsure | 0.610 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a21f188a-7c2f-44ea-b95d-206773a4920d` | ai | 0.864 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `38b54d2f-e14c-4ef6-bd33-15a2b3f8d618` | unsure | 0.598 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `8cd5c165-fdac-42b8-b487-a1725f845236` | ai | 0.693 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `79df88e4-0c42-4349-8761-ac39c3648105` | ai | 0.713 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5b9fe680-a640-41c3-a58c-6d38d1193750` | ai | 0.698 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `29703b1d-11f1-4591-a424-f0df82cc5b0e` | ai | 0.735 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f5ca44f9-b4b2-4af4-abb5-db96168cce38` | ai | 0.714 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `df4daeac-9ac2-4364-8759-bc2a1c004cd2` | ai | 0.717 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c933f4b0-a33f-4c5c-a2a1-4ae98690a1d5` | unsure | 0.360 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `eed4af12-b912-494c-bae7-401399af2b86` | unsure | 0.447 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2e418137-271d-4eea-bc9e-e4a0d5a858b7` | human | 0.297 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8660b98b-47ee-4a0c-bb4e-2e1085be13a3` | unsure | 0.567 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `60e459d7-5786-480e-9364-f940a3e11e91` | unsure | 0.491 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `1912572b-3ba8-4b13-882e-a9f23f4cb331` | unsure | 0.469 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cdd40b64-11de-44ee-b6f1-3f79649cf500` | unsure | 0.571 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `4c6de4ed-158a-41f2-9fe3-b7cd386c972e` | human | 0.222 |  |
| MF04 | malformed | text is only punctuation | 500 | `—` | — | — | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `50f57320-ff62-44ef-9688-164025ec1a8e` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `c52ce3c1-3b40-4a1d-910b-6fe9408caf59` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `3419e4e2-ca76-456d-8b7f-4e6056ed7e1a` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `bb4c43fb-82ca-456f-9651-0ebd2076c554` | ai | 0.905 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `0fa8cc27-5439-45d6-a099-2384f234c267` | unsure | 0.438 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `ba794572-ee34-4291-9e31-2fd445697d0b` | human | 0.302 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `06d92599-def9-4446-bb5c-5ee39f095d71` | human | 0.329 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `df2181f8-898b-435f-884c-5a42ab246949` | human | 0.329 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e30a9baf-9aa5-4b35-8989-a7b8c6c88ba2` | human | 0.329 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47c1870c-7d14-4fab-9be4-64499803bce3` | human | 0.329 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `33d0a457-7d0d-455a-b6a1-db0e798b3d9a` | human | 0.329 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "8c94589c-dd30-40ac-ab01-c228990de505",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.38825,
  "model_score": 0.1635,
  "style_score": 0.613,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "de8951d7-b76a-4006-b682-06c62a0d2173",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4871500000000001,
  "model_score": 0.5943,
  "style_score": 0.38000000000000006,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "b4741645-93a4-4411-9881-7413a6e7b56c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5909333333333333,
  "model_score": 0.6662,
  "style_score": 0.5156666666666666,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b2ff946d-8ae6-4ae2-a3f4-0f8d702e9040",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6080333333333334,
  "model_score": 0.6114,
  "style_score": 0.6046666666666667,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "804b78ef-eade-49a1-a5c9-930cb2ee58df",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.39159999999999995,
  "model_score": 0.3212,
  "style_score": 0.46199999999999997,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "88f8bde3-ad14-4138-a48d-be461407a0e3",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4801833333333333,
  "model_score": 0.5727,
  "style_score": 0.38766666666666666,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "5abbed6f-d12d-41f8-9b18-bd545938ce15",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6247666666666667,
  "model_score": 0.5862,
  "style_score": 0.6633333333333332,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c8178fd4-1989-4ccc-9110-688515afebe6",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.37543333333333334,
  "model_score": 0.2452,
  "style_score": 0.5056666666666667,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b9e8cf42-b1e4-4024-8e03-e66c929e43f8",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6104333333333334,
  "model_score": 0.7042,
  "style_score": 0.5166666666666667,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "a21f188a-7c2f-44ea-b95d-206773a4920d",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8641,
  "model_score": 0.9792,
  "style_score": 0.749,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "38b54d2f-e14c-4ef6-bd33-15a2b3f8d618",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5980833333333334,
  "model_score": 0.6175,
  "style_score": 0.5786666666666668,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "8cd5c165-fdac-42b8-b487-a1725f845236",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.69335,
  "model_score": 0.7387,
  "style_score": 0.648,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "79df88e4-0c42-4349-8761-ac39c3648105",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7133833333333334,
  "model_score": 0.8051,
  "style_score": 0.6216666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5b9fe680-a640-41c3-a58c-6d38d1193750",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.69845,
  "model_score": 0.8329,
  "style_score": 0.564,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "29703b1d-11f1-4591-a424-f0df82cc5b0e",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7349166666666667,
  "model_score": 0.8005,
  "style_score": 0.6693333333333333,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "f5ca44f9-b4b2-4af4-abb5-db96168cce38",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7137,
  "model_score": 0.8814,
  "style_score": 0.5459999999999999,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "df4daeac-9ac2-4364-8759-bc2a1c004cd2",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7171333333333334,
  "model_score": 0.8816,
  "style_score": 0.5526666666666666,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c933f4b0-a33f-4c5c-a2a1-4ae98690a1d5",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3598166666666667,
  "model_score": 0.3223,
  "style_score": 0.3973333333333333,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "eed4af12-b912-494c-bae7-401399af2b86",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.44675,
  "model_score": 0.4625,
  "style_score": 0.431,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "2e418137-271d-4eea-bc9e-e4a0d5a858b7",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.29719999999999996,
  "model_score": 0.2044,
  "style_score": 0.38999999999999996,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8660b98b-47ee-4a0c-bb4e-2e1085be13a3",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5673166666666667,
  "model_score": 0.5943,
  "style_score": 0.5403333333333333,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "60e459d7-5786-480e-9364-f940a3e11e91",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4909,
  "model_score": 0.4998,
  "style_score": 0.482,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "1912572b-3ba8-4b13-882e-a9f23f4cb331",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.46921666666666667,
  "model_score": 0.6401,
  "style_score": 0.29833333333333334,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "cdd40b64-11de-44ee-b6f1-3f79649cf500",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5708166666666667,
  "model_score": 0.5583,
  "style_score": 0.5833333333333334,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "4c6de4ed-158a-41f2-9fe3-b7cd386c972e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.22216666666666665,
  "model_score": 0.0,
  "style_score": 0.4443333333333333,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ZeroDivisionError: float division by zero\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resource&amp;f=sty",
  "verdict": "BROKE"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "50f57320-ff62-44ef-9688-164025ec1a8e",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8321333333333334,
  "model_score": 0.9976,
  "style_score": 0.6666666666666666,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c52ce3c1-3b40-4a1d-910b-6fe9408caf59",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9984500000000001,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "3419e4e2-ca76-456d-8b7f-4e6056ed7e1a",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "bb4c43fb-82ca-456f-9651-0ebd2076c554",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.9053,
  "model_score": 0.9876,
  "style_score": 0.8230000000000001,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "0fa8cc27-5439-45d6-a099-2384f234c267",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4379166666666666,
  "model_score": 0.2395,
  "style_score": 0.6363333333333333,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "ba794572-ee34-4291-9e31-2fd445697d0b",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.30243333333333333,
  "model_score": 0.0492,
  "style_score": 0.5556666666666666,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "06d92599-def9-4446-bb5c-5ee39f095d71",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.32918333333333333,
  "model_score": 0.0287,
  "style_score": 0.6296666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "df2181f8-898b-435f-884c-5a42ab246949",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.32918333333333333,
  "model_score": 0.0287,
  "style_score": 0.6296666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "e30a9baf-9aa5-4b35-8989-a7b8c6c88ba2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.32918333333333333,
  "model_score": 0.0287,
  "style_score": 0.6296666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "47c1870c-7d14-4fab-9be4-64499803bce3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.32918333333333333,
  "model_score": 0.0287,
  "style_score": 0.6296666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "33d0a457-7d0d-455a-b6a1-db0e798b3d9a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.32918333333333333,
  "model_score": 0.0287,
  "style_score": 0.6296666666666667,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
