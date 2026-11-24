import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AUDIT_OUT = BASE / "audit-logs" / "phase0-14-preflight-audit.json"
AUDIT_OUT.parent.mkdir(parents=True, exist_ok=True)

STEPS = [
    ("stage_kaggle_packages", [sys.executable, "scripts/stage_kaggle_packages.py"]),
    ("validate_dsppo_datasets", [sys.executable, "scripts/validate_dsppo_datasets.py"]),
    ("test_pipeline", [sys.executable, "scripts/test_pipeline.py", "-v"]),
    ("verify_phase6_9_outputs", [sys.executable, "scripts/verify_phase6_9_outputs.py"]),
]

results = {}
all_passed = True
for name, cmd in STEPS:
    proc = subprocess.run(cmd, cwd=str(BASE), capture_output=True, text=True)
    passed = proc.returncode == 0
    all_passed = all_passed and passed
    results[name] = {"passed": passed, "returncode": proc.returncode, "output": (proc.stdout + proc.stderr).strip()}

report = {
    "observatory": "DSPPO v1.1",
    "phases_completed": "Phase 0-14",
    "all_passed": all_passed,
    "checks": results,
    "publication_gate": "REQUIRES_HUMAN_APPROVAL",
}
AUDIT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({"all_passed": all_passed, "audit_log": str(AUDIT_OUT.relative_to(BASE))}, indent=2))
if not all_passed:
    raise SystemExit(1)
