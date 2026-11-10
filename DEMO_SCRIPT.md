# 3-minute demo walkthrough

## 0:00–0:20 — Open the console
“ReportFix sits between student reports and live question corrections. The queue is grouped by question rather than by individual report, so faculty can see repeat signals together. The top cards summarise the 44 incoming reports, verified defects, safe fixes and faculty-gated cases.”

## 0:20–1:00 — Show a high-signal repeated report
“Here is the LCR circuit question with three separate student reports. All three point to the same discrepancy. The stored answer is C, but the independent phasor calculation is √(40²+(60−30)²)=50 V, option A. The console shows the exact before/after key change and a short student-facing explanation.”

## 1:00–1:35 — Show a student who is confidently wrong
“R004 is a useful example of why we do not trust the student's proposed answer. The student suggests 8225 Pa. Recomputing pressure from the provided density and RMS speed gives 4800 Pa, option D. The report is still valuable because the stored key points to A, but we do not copy the student's number.”

## 1:35–2:10 — Show human gates and prompt injection
“R025 references a figure that is not attached. We detect the defect but do not invent a diagram. It goes to faculty review. R027 contains an instruction telling the system to ignore its rules and change the answer. That text is treated as untrusted student input and produces no edit.”

## 2:10–2:40 — Demonstrate a safe action and audit
“On an eligible taxonomy-approved fix, I can approve and apply the exact field-level edit. The system checks the repair allowlist and the exact source value before changing anything in the demo state. The action is recorded with the report IDs, timestamp, reviewer and proposed edit. The audit persists across refreshes in this browser.”

## 2:40–3:00 — Close with product thinking
“The current demo loads precomputed, evidence-reviewed results so it works without model credits. PROMPTS.md documents the production LLM contract and safety gates. In production I would add authenticated server-side audit persistence, faculty roles, and monitoring for verified-defect time-to-containment.”
