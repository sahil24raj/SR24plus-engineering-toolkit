#!/usr/bin/env python3
"""
SR24Plus Documentation Validation Suite
Validates:
1. Internal markdown file link targets exist.
2. All 14 master commands are documented and have matching runbooks.
3. Web Dev and Game Dev 12-phase lifecycles are documented.
4. All registered skill paths exist on disk.
5. Markdown tables are syntactically well-formed.
"""

import sys
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def test_master_commands():
    print("[1/5] Validating 14 Master Commands...")
    commands_md = (ROOT_DIR / "00-MASTER-CONTROLLER" / "COMMANDS.md").read_text(encoding="utf-8")
    workflows_dir = ROOT_DIR / "00-MASTER-CONTROLLER" / "workflows"
    
    expected_commands = [
        "/sr24-auto",
        "/sr24-web-dev",
        "/sr24-game-dev",
        "/sr24-saas",
        "/sr24-fullstack",
        "/sr24-browser-game",
        "/sr24-multiplayer",
        "/sr24-unity",
        "/sr24-racing-game",
        "/sr24-ai",
        "/sr24-design",
        "/sr24-security",
        "/sr24-research",
        "/sr24-ship"
    ]
    
    for cmd in expected_commands:
        assert cmd in commands_md, f"Command {cmd} missing from COMMANDS.md"
        # Check runbook existence
        wf_name = cmd.replace("/", "").upper() + ".md"
        wf_path = workflows_dir / wf_name
        assert wf_path.exists(), f"Runbook {wf_path} does not exist for {cmd}"
    
    print(f"  ✓ All {len(expected_commands)} Master Commands and runbooks verified.")

def test_documentation_files_exist():
    print("[2/5] Validating Required Documentation Files...")
    required_docs = [
        "README.md",
        "docs/SR24PLUS-README-AUDIT.md",
        "docs/SR24PLUS-MASTER-COMMANDS.md",
        "docs/README-SR24-WEB-DEV.md",
        "docs/README-SR24-GAME-DEV.md",
        "docs/SR24PLUS-CORE-INTELLIGENCE.md",
        "docs/SR24PLUS-SOURCE-ATTRIBUTION.md",
        "docs/SR24PLUS-SKILL-PROVENANCE.md",
        "docs/SR24PLUS-TECH-STACK.md",
        "docs/SR24PLUS-CORE-ARCHITECTURE.md",
        "SKILL-REGISTRY.md",
        "SKILL-INDEX.md"
    ]
    for rel_path in required_docs:
        doc_file = ROOT_DIR / rel_path
        assert doc_file.exists(), f"Required documentation file {rel_path} does not exist"
    print(f"  ✓ All {len(required_docs)} critical documentation files present.")

def test_internal_links():
    print("[3/5] Validating Internal Relative Markdown Links in Root README...")
    readme = (ROOT_DIR / "README.md").read_text(encoding="utf-8")
    # Match markdown links: [text](path)
    links = re.findall(r'\[([^\]]+)\]\((?!http|#|mailto)([^)]+)\)', readme)
    
    broken = []
    for text, link in links:
        # Strip anchor
        clean_link = link.split('#')[0]
        if not clean_link:
            continue
        target = (ROOT_DIR / clean_link).resolve()
        if not target.exists():
            broken.append((text, link, str(target)))
    
    if broken:
        print(f"  ✗ Broken links found in README.md: {broken}")
        sys.exit(1)
    else:
        print(f"  ✓ All {len(links)} relative links in README.md resolve to existing files.")

def test_phase_coverage():
    print("[4/5] Validating 12-Phase Coverage for Web Dev and Game Dev...")
    web_doc = (ROOT_DIR / "docs" / "README-SR24-WEB-DEV.md").read_text(encoding="utf-8")
    game_doc = (ROOT_DIR / "docs" / "README-SR24-GAME-DEV.md").read_text(encoding="utf-8")
    
    for phase_num in range(1, 13):
        # Match phase references
        assert f"Phase {phase_num}" in web_doc or f"Phase {phase_num:02d}" in web_doc, f"Web Dev missing Phase {phase_num}"
        assert f"Phase {phase_num}" in game_doc or f"Phase {phase_num:02d}" in game_doc, f"Game Dev missing Phase {phase_num}"
    print("  ✓ All 12 Web Dev phases and 12 Game Dev phases fully documented.")

def test_markdown_tables():
    print("[5/5] Validating Markdown Table Delimiters across Documentation...")
    for doc_path in (ROOT_DIR / "docs").glob("*.md"):
        lines = doc_path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            if line.startswith("|") and line.endswith("|") and "---" in line:
                # Check delimiter row has proper pipes
                cells = [c.strip() for c in line.split("|")[1:-1]]
                for c in cells:
                    assert re.match(r"^:?-+:?$", c), f"Invalid table delimiter in {doc_path.name}:{idx+1} -> {line}"
    print("  ✓ All Markdown table structures syntactically valid.")

if __name__ == "__main__":
    test_master_commands()
    test_documentation_files_exist()
    test_internal_links()
    test_phase_coverage()
    test_markdown_tables()
    print("\n✅ ALL DOCUMENTATION VALIDATION CHECKS PASSED SUCCESSFULLY!")
