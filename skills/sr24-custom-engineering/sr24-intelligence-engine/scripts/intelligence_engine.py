#!/usr/bin/env python3
"""
SR24 Intelligence Engine
Autonomous Project Understanding, Stack Detection, Archetype Classification,
and Priority-Scored Skill Activation Planner.
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Any

ARCHETYPES = {
    "browser_game": {
        "title": "Browser Game / Esports Platform",
        "markers": ["canvas", "three", "phaser", "pixi", "matter-js", "rapier", "colyseus", "howler"],
        "recommended_skills": [
            "browser-game-architect", "threejs-game-engine", "react-three-fiber",
            "rapier-physics", "matter-js-physics", "colyseus-multiplayer",
            "socketio-realtime", "threejs-ui-hud", "howler-js-audio",
            "threejs-optimization-profiling", "gameplay-regression-testing"
        ]
    },
    "unity_game": {
        "title": "Unity 3D / Native Action Title",
        "markers": ["Assets", "ProjectSettings", "Assembly-CSharp", ".unity", ".prefab"],
        "recommended_skills": [
            "new-unity-project", "unity-entities-ecs", "truck-physics-engineer",
            "realistic-car-controller-engineer", "racing-track-design-engineer",
            "urp-postprocessing", "unity-cli", "optimize-web", "game-build-and-release"
        ]
    },
    "fullstack_saas": {
        "title": "Full Stack SaaS Platform",
        "markers": ["prisma", "drizzle", "supabase", "stripe", "razorpay", "bullmq", "redis", "next", "auth"],
        "recommended_skills": [
            "bulletproof-react", "supabase-engineering", "prisma-orm", "drizzle-orm",
            "dbml-schema-design", "lago-billing", "node-best-practices",
            "growthbook-experimentation", "sentry-monitoring", "posthog-analytics"
        ]
    },
    "ecommerce": {
        "title": "E-Commerce / Retail Engine",
        "markers": ["cart", "checkout", "vendure", "shopify", "medusa", "stripe", "catalog"],
        "recommended_skills": [
            "vendure-ecommerce", "dbml-schema-design", "drizzle-orm",
            "zod-schema-validation", "axe-core-accessibility", "posthog-analytics"
        ]
    },
    "ai_agent": {
        "title": "AI Agent & Workflow System",
        "markers": ["langchain", "openai", "anthropic", "mcp", "llama", "fastapi", "rag"],
        "recommended_skills": [
            "tavily-search-intelligence", "firecrawl-scraper", "zod-schema-validation",
            "node-best-practices", "docker-containerization", "sentry-monitoring"
        ]
    },
    "developer_tools": {
        "title": "Developer Tooling / CLI / SDK",
        "markers": ["commander", "yargs", "bin", "cli", "oclif", "ink"],
        "recommended_skills": [
            "typescript-eslint", "react-testing-library", "playwright-testing",
            "bruno-api-testing", "github-actions-ci"
        ]
    }
}

class ProjectIntelligenceEngine:
    def __init__(self, target_dir: str):
        self.target_dir = Path(target_dir).resolve()
        self.stack = {}
        self.archetypes = []
        self.matched_skills = []

    def scan_files(self) -> Dict[str, Any]:
        detected_files = []
        deps = set()
        dev_deps = set()
        
        # Check package.json
        pkg_json = self.target_dir / "package.json"
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text(encoding="utf-8"))
                for k in data.get("dependencies", {}).keys():
                    deps.add(k.lower())
                for k in data.get("devDependencies", {}).keys():
                    dev_deps.add(k.lower())
            except Exception:
                pass

        # Check Unity
        is_unity = (self.target_dir / "ProjectSettings").exists() or (self.target_dir / "Assets").exists()

        # Check Python
        is_python = (self.target_dir / "requirements.txt").exists() or (self.target_dir / "pyproject.toml").exists()

        return {
            "dependencies": sorted(list(deps)),
            "devDependencies": sorted(list(dev_deps)),
            "is_unity": is_unity,
            "is_python": is_python
        }

    def infer_archetype(self, scan_result: Dict[str, Any]) -> List[str]:
        all_deps = set(scan_result["dependencies"] + scan_result["devDependencies"])
        detected = []

        if scan_result["is_unity"]:
            detected.append("unity_game")

        # Check browser gaming markers
        game_libs = {"three", "@react-three/fiber", "phaser", "pixi.js", "matter-js", "@dimforge/rapier2d", "@dimforge/rapier3d", "colyseus.js", "socket.io-client", "howler"}
        if any(lib in all_deps for lib in game_libs):
            detected.append("browser_game")

        # Check SaaS markers
        saas_libs = {"@prisma/client", "drizzle-orm", "@supabase/supabase-js", "stripe", "razorpay", "bullmq", "next-auth", "@clerk/nextjs"}
        if any(lib in all_deps for lib in saas_libs):
            detected.append("fullstack_saas")

        # Check E-commerce markers
        ecom_libs = {"@vendure/core", "@medusajs/medusa", "commerce"}
        if any(lib in all_deps for lib in ecom_libs):
            detected.append("ecommerce")

        # Fallback to web app if next/react detected
        if not detected and any(f in all_deps for f in ["next", "react", "vue", "svelte"]):
            detected.append("fullstack_saas")

        return detected or ["fullstack_saas"]

    def plan_skills(self, detected_archetypes: List[str]) -> List[Dict[str, Any]]:
        planned = []
        seen = set()

        # Always include foundational quality skills
        base_skills = [
            ("anti-slop", 100, "Core AI quality & clean implementation guardrail"),
            ("zod-schema-validation", 95, "Strict runtime schema & contract safety"),
            ("typescript-eslint", 90, "Type integrity and static code analysis"),
            ("playwright-testing", 88, "Automated E2E and visual regression verification")
        ]
        for name, score, reason in base_skills:
            seen.add(name)
            planned.append({"skill": name, "relevance_score": score, "reason": reason})

        for arch_key in detected_archetypes:
            arch = ARCHETYPES.get(arch_key)
            if not arch:
                continue
            for sk in arch["recommended_skills"]:
                if sk not in seen:
                    seen.add(sk)
                    planned.append({
                        "skill": sk,
                        "relevance_score": 85,
                        "reason": f"Required for {arch['title']} implementation"
                    })

        planned.sort(key=lambda x: x["relevance_score"], reverse=True)
        return planned

    def run(self) -> Dict[str, Any]:
        scan = self.scan_files()
        archetypes = self.infer_archetype(scan)
        skills = self.plan_skills(archetypes)
        
        return {
            "target_directory": str(self.target_dir),
            "detected_stack": {
                "is_unity": scan["is_unity"],
                "is_python": scan["is_python"],
                "dependencies_count": len(scan["dependencies"]),
                "key_libraries": scan["dependencies"][:15]
            },
            "classified_archetypes": [ARCHETYPES[k]["title"] for k in archetypes if k in ARCHETYPES],
            "activated_skills_plan": skills
        }

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    engine = ProjectIntelligenceEngine(target)
    result = engine.run()
    print(json.dumps(result, indent=2))