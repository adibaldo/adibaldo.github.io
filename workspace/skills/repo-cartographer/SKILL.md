# SKILL.md - OpenClaw Repository Cartographer

This skill provides precise guidance on the standard OpenClaw workspace file layout and where specific types of files should be stored according to official documentation. Use this to ensure the repository remains organized, compliant, and "sparking joy" (KonMari style).

## Standard Workspace Layout

According to OpenClaw concepts, the following files have specific meanings within the workspace:

| File/Folder | Purpose | Lifecycle |
| :--- | :--- | :--- |
| `AGENTS.md` | Operating instructions, rules, and memory usage details. | Loaded every session. |
| `SOUL.md` | Persona, tone, boundaries, and character rules. | Loaded every session. |
| `USER.md` | Profile of the human being helped (Adi Baldo). | Loaded every session. |
| `IDENTITY.md` | Agent's name (Aparício Funes), vibe, and emoji signature. | Set during bootstrap. |
| `TOOLS.md` | Local tool notes, conventions, and environment specifics. | Reference only. |
| `HEARTBEAT.md` | Checklist for periodic automated checks (keep it short). | Loaded during heartbeats. |
| `BOOT.md` | Startup checklist executed on gateway restart. | Execution only. |
| `BOOTSTRAP.md` | First-run ritual instructions. | Delete after setup. |
| `MEMORY.md` | Curated long-term memory (distilled wisdom). | Main session only. |
| `memory/*.md` | Raw daily logs (YYYY-MM-DD.md). | Created daily. |
| `skills/` | Workspace-specific skills (overrides managed ones). | Persistent. |
| `assets/` | Multimedia assets (audio, images, screenshots). | Persistent. |
| `scripts/` | Custom automation scripts (Python, Bash, etc.). | Persistent. |

## Specialized Storage (Custom Patterns)

For the Aparício-Funes ecosystem, we follow these extended organization rules:

### 1. Audio & Transcripts (`assets/audio/`)
- **Active Audios:** Store standard naming convention files here: `{timestamp}_{sessionID}_{slug}.wav`.
- **Transcripts:** Matching Markdown files go in `assets/audio/transcripts/{filename}.md`.
- **Archive:** Move non-standard or old testing audios to `assets/audio/archive/`.

### 2. Visual Assets (`assets/screenshots/` & `assets/images/`)
- **Screenshots:** All PNG/JPG captures of the blog or UI tests go in `assets/screenshots/`.
- **Illustrations:** Cover images or blog assets go in `assets/images/` (or `archive/` if old).

### 3. Sub-Agent Definitions (`jules-agents/`)
- Store Jules agent personas and prompts in their respective subfolders (e.g., `jules-agents/vitrine/SOUL.md`).

## What stays OUTSIDE the workspace
These live in `~/.openclaw/` but **NEVER** in the git-tracked workspace:
- `openclaw.json` (System config)
- `credentials/` (OAuth tokens, API keys)
- `sessions/` (Raw conversation transcripts)
- `agent/` (Auth profiles and system state)

## Skill Commands
- **Check health:** `ls -la` on the root to spot files out of place.
- **Enforce order:** Move any misplaced file to its designated home above.
- **Gratitude:** (KonMari) Thank the file before moving or deleting it.
