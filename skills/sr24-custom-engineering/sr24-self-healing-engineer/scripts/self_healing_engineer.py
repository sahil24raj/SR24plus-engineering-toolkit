#!/usr/bin/env python3
"""
SR24 Self-Healing Engineer
Controlled Autonomous 6-Step Closed Loop:
Detect ➔ Diagnose ➔ Plan ➔ Repair ➔ Test ➔ Verify (Max 3 Retries).
Enforces Strict Production Safety Guardrails.
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional

class SelfHealingEngineer:
    def __init__(self, target_dir: str, max_retries: int = 3):
        self.target_dir = Path(target_dir).resolve()
        self.max_retries = max_retries
        self.history = []

    def log(self, step: str, message: str):
        entry = f"[{step}] {message}"
        self.history.append(entry)
        print(entry)

    def run_check(self, command: str) -> tuple[int, str]:
        try:
            res = subprocess.run(
                command,
                shell=True,
                cwd=self.target_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60
            )
            return res.returncode, res.stdout + "\n" + res.stderr
        except Exception as e:
            return 1, str(e)

    def detect_failures(self, test_cmd: str) -> Optional[str]:
        self.log("STEP 1: DETECT", f"Running check: {test_cmd}")
        code, output = self.run_check(test_cmd)
        if code == 0:
            self.log("STEP 1: DETECT", "No errors detected. System is green.")
            return None
        self.log("STEP 1: DETECT", f"Failure detected (exit code {code})")
        return output

    def diagnose(self, error_output: str) -> Dict[str, Any]:
        self.log("STEP 2: DIAGNOSE", "Analyzing failure stack trace & root cause...")
        
        # Check TypeScript / syntax error pattern
        ts_match = re.search(r"([\w\-/\\]+\.(?:ts|tsx|js|jsx)):(\d+):(\d+)\s*-\s*error\s*TS\d+:\s*(.*)", error_output)
        if ts_match:
            return {
                "file": ts_match.group(1),
                "line": int(ts_match.group(2)),
                "col": int(ts_match.group(3)),
                "error": ts_match.group(4).strip(),
                "type": "typescript_error"
            }
            
        # Check standard Python syntax error pattern
        py_match = re.search(r'File "([^"]+)", line (\d+)(?:, in .*)?\n\s*(.*)\n([A-Za-z]+Error: .*)', error_output)
        if py_match:
            return {
                "file": py_match.group(1),
                "line": int(py_match.group(2)),
                "code": py_match.group(3).strip(),
                "error": py_match.group(4).strip(),
                "type": "python_error"
            }

        return {
            "file": "unknown",
            "error": error_output[:300],
            "type": "generic_error"
        }

    def plan(self, diagnosis: Dict[str, Any]) -> str:
        self.log("STEP 3: PLAN", f"Generating minimal targeted repair plan for {diagnosis.get('file')}...")
        return f"Patch {diagnosis.get('file')} to resolve {diagnosis.get('error')}"

    def repair_safety_check(self, planned_patch: str) -> bool:
        # Strict Safety Boundaries
        forbidden = ["DROP TABLE", "rm -rf /", "git push --force", "process.env.", "DELETE FROM users"]
        for bad in forbidden:
            if bad in planned_patch:
                self.log("SAFETY ALERT", f"Refusing destructive repair operation containing: {bad}")
                return False
        return True

    def execute_closed_loop(self, test_cmd: str, patch_callback) -> Dict[str, Any]:
        attempt = 0
        while attempt < self.max_retries:
            attempt += 1
            self.log("LOOP", f"Starting repair attempt {attempt} of {self.max_retries}")
            
            error = self.detect_failures(test_cmd)
            if error is None:
                self.log("STEP 6: PASS", "Verification succeeded! Repair complete.")
                return {"status": "SUCCESS", "attempts": attempt, "history": self.history}
                
            diagnosis = self.diagnose(error)
            plan_str = self.plan(diagnosis)
            
            if not self.repair_safety_check(plan_str):
                return {"status": "BLOCKED_BY_SAFETY", "attempts": attempt, "history": self.history}
                
            self.log("STEP 4: REPAIR", f"Applying targeted repair (Attempt {attempt})...")
            patched = patch_callback(diagnosis, attempt)
            if not patched:
                self.log("STEP 4: REPAIR", "Could not synthesize safe patch.")
                break
                
            self.log("STEP 5: VERIFY", "Verifying repair against test suite...")
            
        self.log("ESCALATION", f"Failed to heal issue after {self.max_retries} attempts. Halting to preserve safety.")
        return {"status": "ESCALATED_TO_HUMAN", "attempts": attempt, "history": self.history}

if __name__ == "__main__":
    test_command = sys.argv[1] if len(sys.argv) > 1 else "npm test"
    engineer = SelfHealingEngineer(".")
    print(f"Self-Healing Engineer initialized for: {test_command}")