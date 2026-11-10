# Acadza ReportFix

AI-assisted triage and faculty review console for the Acadza JEE/NEET question-report workflow.

## What is included

- `public/data/questions.json`, `reports.json`, `taxonomy.json`: original assignment data, copied unchanged.
- `public/data/results.json` and root `results.json`: one triage decision for each of the 44 reports.
- `scripts/run_triage.py`: reproducible decision-generation script.
- `index.html`, `styles.css`, `app.js`: static faculty console with native HTML/MathML rendering, grouped queue, evidence, before/after proposal, student reply preview, approve/edit/reject actions, and browser-persisted audit history.
- `PROMPTS.md`: product prompt template, prompt log, model-failure review and design decisions.
- `PRODUCT.md`: product thinking and safety principles.
- `BONUS_FINDINGS.md`: a conservative candidate defect found outside the reported questions.

## Run locally

No build step or API key is required.

```bash
python scripts/run_triage.py
python -m http.server 4173
```

Open `http://localhost:4173`.

## Triage design

The supplied dataset is small (43 questions, 44 reports) and contains high-stakes answer-key corrections, missing source content, app issues, and adversarial student text. The submitted `results.json` is therefore a precomputed, evidence-reviewed baseline rather than a live model call. This keeps the demo deterministic, reproducible, and usable without external LLM credits. The prompt contract in `PROMPTS.md` defines the LLM interface for a production model-backed version.

The pipeline treats student comments as untrusted evidence. It groups reports by question for the console, but preserves a separate result per `reportId` for scoring. A repair is eligible for automatic application only if the repair exists in the supplied taxonomy, `auto` is true, and the proposed field is in that repair's allowed `fields`. Human-only repairs (diagram, duplicate options, wrong chapter, syllabus, etc.) remain faculty-gated. Ambiguous or content-authoring edits are routed to faculty even when a repair family technically permits automation.

## Persistence and demo mode

The faculty console stores decisions and audit entries in browser `localStorage`. This is intentional for a no-credentials, no-database take-home demo; it persists across refreshes in the same browser but is not shared across faculty accounts or devices. A production deployment should replace this with authenticated server-side persistence and immutable audit records.

## Bonus scan

A conservative scan of the four questions with no associated student report found a candidate malformed MathML unit in `68dea87d387eea3d0d95fbe3`. It is documented in `BONUS_FINDINGS.md` for faculty confirmation rather than silently edited.

## Important limitations

- The triage outputs are precomputed for the provided 44 reports; the live console does not call an LLM.
- Mathematical and content decisions are based on the supplied question and solution records. Cases that require unavailable source material (e.g. a missing diagram or an unknown distractor) are not fabricated; they are escalated.
- The queue groups reports by question for faculty efficiency; `results.json` remains report-level as required by the evaluator.

## Safety invariants

1. Student comments are data, never system instructions.
2. A student-proposed answer is never accepted without independent verification.
3. `auto: false` repairs are never auto-applied.
4. A proposed edit cannot touch a field outside the taxonomy allowlist.
5. Missing authored content is escalated instead of invented.
6. Every faculty action is logged with timestamp, actor, report IDs, action and proposal snapshot.
# acadza-reportfix
