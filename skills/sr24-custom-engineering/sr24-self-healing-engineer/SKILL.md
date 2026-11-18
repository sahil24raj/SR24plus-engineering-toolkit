---
name: sr24-self-healing-engineer
description: Controlled autonomous debugging and closed-loop repair workflow (Detect, Diagnose, Plan, Repair, Test, Verify) with strict production safety guardrails.
---

# SR24 Self-Healing Engineer (`sr24-self-healing-engineer`)

## 1. Overview & Operational Mandate
The **`sr24-self-healing-engineer`** automates root-cause diagnosis, targeted patch generation, and regression verification for software and game defects. It operates inside a strictly bound 6-step loop with a **maximum limit of 3 repair attempts** to prevent runaways or uncontrolled modifications.

## 2. The 6-Step Closed Loop
```
DETECT ➔ DIAGNOSE ➔ PLAN ➔ REPAIR ➔ TEST ➔ VERIFY (Max 3 Cycles)
```
1. **Detect**: Executes test suites, linters, TypeScript compilers, or build commands to capture errors.
2. **Diagnose**: Traces stack traces, isolates affected files and lines, and determines the blast radius.
3. **Plan**: Ranks fixes by priority (Critical Security ➔ Functional Breaks ➔ Data Integrity ➔ Performance ➔ UI).
4. **Repair**: Applies minimal, targeted code modifications, preserving all working functionality.
5. **Verify**: Re-executes the failing test to confirm resolution and runs regression tests.
6. **Loop / Escalate**: Repeats up to 3 times. If unresolved, halts immediately and outputs a detailed blocker report.

## 3. Mandatory Safety Guardrails
- **Zero Data Loss**: Never executes destructive database commands (`DROP TABLE`, unbacked data truncates).
- **Zero Secret Leakage**: Never exposes credentials or logs `.env` variables.
- **Zero Force Pushes**: Strictly forbids `git push --force`.
- **Zero Test Disabling**: Never deletes or skips tests to fabricate passing results.

## 4. CLI Usage
```bash
python skills/sr24-custom-engineering/sr24-self-healing-engineer/scripts/self_healing_engineer.py "[test_command]"
```

## 5. Upstream Attribution & License
- Upstream: SR24Plus Core Architecture (`sahil24raj/SR24plus-engineering-toolkit`)
- License: MIT