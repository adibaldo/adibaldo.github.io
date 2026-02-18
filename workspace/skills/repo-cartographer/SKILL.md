# SKILL.md - OpenClaw Repository Cartographer (Aparício Funes Edition)

This skill provides precise guidance on the file layout for the Aparício Funes repository. Note that in this environment, the Git repository root is one level ABOVE the agent's working directory (`workspace/`).

## Repository Root Layout (/)
The Git repository (`franklinbaldo/aparicio-funes`) starts at `/home/franklinbaldo/.openclaw/agents/aparicio/`.

| File/Folder | Purpose |
| :--- | :--- |
| `SOUL.md`, `AGENTS.md`, `USER.md`, `IDENTITY.md` | Core agent personality and instructions. |
| `workspace/` | The active directory where the agent operates. |
| `jules-agents/` | Persona definitions for Jules sub-agents. |
| `assets/` | Multimedia storage (audio, transcripts, screenshots, images). |
| `memory/` | Raw daily memory logs (YYYY-MM-DD.md). |
| `scripts/` | Custom automation and utility scripts. |
| `skills/` | Agent skills (including this one). |
| `sessions/` | **UNTRACKED** - Raw conversation transcripts (not committed to Git). |
| `agent/` | **UNTRACKED** - Auth profiles and system state (not committed to Git). |

## Internal Workspace Layout (/workspace)
When operating inside `workspace/`, the agent sees a mirrored or symlinked set of core files to maintain compatibility with OpenClaw standards.

## Specialized Storage Rules

### 1. Audio & Transcripts (`/assets/audio/`)
- **Active Audios:** `{timestamp}_{sessionID}_{slug}.wav`
- **Transcripts:** `/assets/audio/transcripts/{filename}.md`
- **Archive:** `/assets/audio/archive/` (old or test files).

### 2. Visual Assets (`/assets/screenshots/` & `/assets/images/`)
- All captures go to `/assets/screenshots/`.
- Final blog assets go to `/assets/images/`.

## Enforcing Order
- **Git Root vs Workspace:** Always remember that the repo is the parent of the `workspace/` folder.
- **KonMari:** Thank every file before moving it to its correct home.
