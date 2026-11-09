# SR24PLUS SKILL COMPATIBILITY MATRIX

This document details the environment compatibility, language runtimes, host platform support, and Antigravity execution modes for all skill suites in the SR24Plus Engineering Toolkit.

---

## 1. Environment & Runtime Compatibility Table

| Suite Name | Target Runtimes | Antigravity Native Mode | CLI Dependencies | Primary Output Formats |
|---|---|:---:|---|---|
| **`sr24-custom-engineering`** | Node.js (v18+), TypeScript, Unity C#, Python 3.10+ | Full Reasoning Context & Dynamic Load | None (Pure code/architecture) | TypeScript, C#, SQL, JSON-LD, Markdown Runbooks |
| **`agency-agents`** | Node.js, Python 3.9+, Docker | Full Reasoning Context & Dynamic Load | Optional: Docker, Git, CLI tools | PRD, Architecture Specs, Microservices Code, Threat Models |
| **`unity-skills`** | Unity 2022.3 LTS, Unity 6, C# | Full Reasoning Context & Dynamic Load | Unity Hub, Unity CLI, dotnet SDK | C# Monobehaviours, ScriptableObjects, Shader Graph, HLSL |
| **`addyosmani-agent-skills`**| Node.js, Chrome DevTools | Full Reasoning Context & Dynamic Load | Node, npm, Playwright | Test Suites, CI/CD YAML, ADRs, Refactored Code |
| **`ui-design-suite`** | React, Tailwind CSS, Three.js, CSS3 | Full Reasoning Context & Dynamic Load | Vite, npm, Tailwind | JSX/TSX Components, USS/UXML, CSS Tokens, Diffs |
| **`vercel-skills`** | Next.js (v14/15), Node.js | Full Reasoning Context & Dynamic Load | Vercel CLI, npm | Next.js Routes, Middleware, Server Actions, Configs |
| **`android-mobile`** | Android SDK, Java/Kotlin, ADB | Full Reasoning Context & Dynamic Load | adb, Android SDK build-tools | Gradle configs, Android Manifests, ADB scripts |
| **`antigravity-core`** | Antigravity Runtime | Native Built-in Tools | Antigravity CLI / Extension | MCP Servers, Custom Rules, Tool Schemas |

---

## 2. Antigravity Native Tool Integration Mapping

| Capability Required | Supported Native Mechanism | Fallback Mechanism |
|---|---|---|
| **Multi-Agent Delegation** | `invoke_subagent` (built-in types: `research`, `code-reviewer`, `security-auditor`, `test-engineer`, `web-performance-auditor`) | Sequential phase execution with single source of truth |
| **Custom Dynamic Subagents** | `define_subagent` (Registers runtime agents with dedicated system prompts and tools) | In-context persona switching guided by `SKILL.md` |
| **Skill Instruction Loading** | Native skill context auto-detection + `read_file` of target `SKILL.md` | Direct prompt injection of skill operational instructions |
| **Command Interception** | Master Router prompt interception (`/sr24-*` commands parsed in chat) | Natural language trigger phrases (`"Activate SaaS Toolkit"`) |
| **Verification & Testing** | `run_command` (`npm test`, `pytest`, `npm run build`, `git status`) | Dry-run code review with explicit diff inspection |

---

## 3. Platform & OS Support
- **Windows 10/11**: Fully tested and verified (PowerShell 5.1/7+, Windows paths with backslash normalization).
- **macOS / Linux**: 100% compatible (POSIX compliant paths, standard Bash/Zsh commands).
- **Cloud Containers**: Fully compatible with Linux Docker containers (`node:20-alpine`, `python:3.11-slim`).
