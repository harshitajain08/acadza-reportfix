# Bonus scan — unreported content candidates

The supplied 44 reports cover 39 unique question IDs? (The console groups by question; the remaining records were scanned separately.) The following candidate was found in a question with no matching student report.

## Candidate: `68dea87d387eea3d0d95fbe3` — Physics / Electrostatics

The question's unit for α is represented as `volt` followed by MathML `<msup><mi></mi>…−1</msup>`. The superscript has an empty base element. The intended unit appears to be V⁻¹, but the MathML node is malformed and may render as a detached superscript. Suggested repair: correct the MathML to represent `V^{-1}` explicitly. This is a notation/markup-quality finding, not an answer-key defect; the supplied solution gives V=5 V (option A) consistently.

This is recorded as a candidate for content QA rather than silently modifying an unreported question. Faculty should confirm the intended unit notation against the source.
