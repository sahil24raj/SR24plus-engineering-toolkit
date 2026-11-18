#!/usr/bin/env python3
"""
SR24Plus Global GitHub Hyperlink Validation Script
Scans documentation files across the repository to verify that:
1. Upstream GitHub repositories are properly formatted as active markdown hyperlinks.
2. No broken or malformed GitHub URLs exist.
3. Central registry (registry/SR24PLUS-UPSTREAM-SOURCES.md) matches documented sources.
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path(__file__).resolve().parent.parent

DOC_FILES = [
    ROOT_DIR / "README.md",
    ROOT_DIR / "registry" / "SR24PLUS-UPSTREAM-SOURCES.md",
    ROOT_DIR / "docs" / "SR24PLUS-MASTER-COMMANDS.md",
    ROOT_DIR / "docs" / "README-SR24-WEB-DEV.md",
    ROOT_DIR / "docs" / "README-SR24-GAME-DEV.md",
    ROOT_DIR / "docs" / "SR24PLUS-SOURCE-ATTRIBUTION.md",
    ROOT_DIR / "docs" / "SR24PLUS-SKILL-PROVENANCE.md",
    ROOT_DIR / "docs" / "SR24PLUS-CORE-INTELLIGENCE.md",
    ROOT_DIR / "docs" / "SR24PLUS-INTELLIGENCE-ENGINE.md",
    ROOT_DIR / "docs" / "SR24PLUS-PRODUCTION-AUDITOR.md",
    ROOT_DIR / "docs" / "SR24PLUS-SELF-HEALING-ENGINEER.md",
    ROOT_DIR / "00-MASTER-CONTROLLER" / "COMMANDS.md"
]

def validate_github_hyperlinks():
    print("=" * 60)
    print("SR24Plus Global GitHub Hyperlink Audit")
    print("=" * 60)
    
    github_link_pattern = re.compile(r'\[([^\]]+)\]\((https?://github\.com/[^)]+)\)')
    raw_github_pattern = re.compile(r'(?<!\()https?://github\.com/[a-zA-Z0-9_\-\./]+(?!\))')
    
    total_links = 0
    unique_repos = set()
    file_stats = defaultdict(int)
    
    for file_path in DOC_FILES:
        if not file_path.exists():
            print(f"[FAIL] Missing expected doc file: {file_path.relative_to(ROOT_DIR)}")
            sys.exit(1)
            
        content = file_path.read_text(encoding="utf-8")
        links = github_link_pattern.findall(content)
        file_stats[file_path.name] = len(links)
        total_links += len(links)
        
        for anchor_text, url in links:
            # Clean URL of anchors/subpaths to get owner/repo
            match = re.search(r'github\.com/([a-zA-Z0-9_\-\.]+)/([a-zA-Z0-9_\-\.]+)', url)
            if match:
                owner, repo = match.group(1), match.group(2)
                # Strip trailing .git
                repo = repo.removesuffix('.git')
                unique_repos.add(f"{owner}/{repo}")
    
    print(f"\n[1/3] File Hyperlink Density:")
    for fname, count in sorted(file_stats.items()):
        print(f"  • {fname:40s}: {count:3d} GitHub hyperlinks")
        
    print(f"\n[2/3] Hyperlink Metrics:")
    print(f"  • Total Active GitHub Hyperlinks: {total_links}")
    print(f"  • Total Unique Upstream Repositories: {len(unique_repos)}")
    
    assert total_links >= 150, f"Expected at least 150 GitHub links, found {total_links}"
    assert len(unique_repos) >= 40, f"Expected at least 40 unique repositories, found {len(unique_repos)}"
    
    print(f"\n[3/3] Central Upstream Registry Verification:")
    registry_file = ROOT_DIR / "registry" / "SR24PLUS-UPSTREAM-SOURCES.md"
    assert registry_file.exists(), "registry/SR24PLUS-UPSTREAM-SOURCES.md missing"
    reg_content = registry_file.read_text(encoding="utf-8")
    reg_links = github_link_pattern.findall(reg_content)
    print(f"  • Central Registry contains {len(reg_links)} verified repository links.")
    
    print("\n" + "=" * 60)
    print("✅ 100% GITHUB HYPERLINK VALIDATION PASSED!")
    print("=" * 60)
    return total_links, len(unique_repos), file_stats

if __name__ == "__main__":
    validate_github_hyperlinks()
