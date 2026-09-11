#!/usr/bin/env python3
"""Regression tests for the quality gates. Stdlib unittest; each test names its bug."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script)], capture_output=True, text=True)


class TestGates(unittest.TestCase):
    def test_catalog_validates(self):
        """Bug guarded: a malformed record shipping in a release because nobody ran the validator."""
        r = run("validate_catalog.py")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_no_dashes(self):
        """Bug guarded: SPYGLASS ADR-004 class regression where dashes survived in raw bytes despite a parsed-value sweep."""
        r = run("dash_gate.py")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_no_drift(self):
        """Bug guarded: hand-edited derived CSVs silently diverging from the canonical JSON."""
        r = run("drift_gate.py")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_stated_quarantine_present(self):
        """Bug guarded: vendor self-reports upgraded to VERIFIED or CORROBORATED during a metric refresh."""
        doc = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
        duo = next(a for a in doc["assets"] if a["asset_id"] == "vault:conlang-b01")
        learner_metrics = [m for m in duo["metrics"] if "learners" in m["name"]]
        self.assertTrue(learner_metrics)
        for m in learner_metrics:
            self.assertEqual(m["evidence_tier"], "S", f"{m['name']} escaped the STATED quarantine")


if __name__ == "__main__":
    unittest.main()
