#!/usr/bin/env bash
set -euo pipefail

# GATE-04: Run only after explicit human approval to publish to GitHub.
python3 scripts/run_full_preflight.py
git status
echo "Ready to push to origin (git@github.com:bsdkijc-dev/digital-public-sentiment-participation-observatory.git)."
echo "Run manually after human approval: git push -u origin main"
