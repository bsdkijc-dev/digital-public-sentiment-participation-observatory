import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

REQUIRED_PHASE6_9 = [
    "validated-evidence/evidence-triangulation-protocol.md",
    "consultation-framework/consultation-questionnaire-perma-1-2016.md",
    "reports/pilot-1-perma-1-2016-comprehensive-report.md",
    "ex-post-ria/ijrio-handoff-package.json",
    "policy-briefs/perma-1-2016-pilot-policy-brief.md",
]

for rel in REQUIRED_PHASE6_9:
    p = BASE / rel
    assert p.exists() and p.stat().st_size > 0, f"Missing or empty Phase 6-9 file: {rel}"

handoff = json.loads((BASE / "ex-post-ria/ijrio-handoff-package.json").read_text(encoding="utf-8"))
assert handoff["pilot_perma_id"] == "PERMA-2016-01"
assert len(handoff["traceability_chain"]) == 7

print(f"PHASE 6-9 VERIFICATION PASSED: {len(REQUIRED_PHASE6_9)}/5 deliverables verified.")
