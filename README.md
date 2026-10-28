# Preflight Agent Skill

An agent skill for AI coding tools (Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor and more) that checks before it builds, and learns from every bug so the same mistake doesn't happen twice, across all your projects.

[![Release](https://img.shields.io/github/v/release/R-Dilipkumar/preflight-agent-skill)](https://github.com/R-Dilipkumar/preflight-agent-skill/releases/latest)
[![License: MIT](https://img.shields.io/github/license/R-Dilipkumar/preflight-agent-skill)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills%20(SKILL.md)-blue)](https://agentskills.io)

## Why

A lot of time in AI-assisted coding goes on the same loop: build something, find out it's deprecated or doesn't work on the real device, search, try the first answer, it fails, try the next one. This skill moves that research to the start, and turns every snag into a short "before doing X, check Y" lesson that your AI agent reads on the next project.

## Features

- **Check before building:** before using any library, API, SDK version, AI model or cloud service, the agent checks the official docs for deprecation, platform support, licence and known issues, and compares 2–3 options.
- **Lessons that grow:** after a bug is fixed, the agent asks "what check would have avoided this?" and saves one line: a general **rule**, or a specific **fact** with a date.
- **Stays small:** repeats get merged into one rule, each file stays under about 60 lines, and facts older than 6 months get re-checked.
- **Coding standards:** a short list that changes how code gets written (build only what's asked, fail loudly, copy twice before sharing code, delete only what's confirmed unused, and more).
- **session.md per project:** a local notes file with a "Start here" summary, key decisions and a dated log, so any new session can pick up the work. Each log entry feeds snags back into the lessons.
- **Works across tools:** plain Markdown in the open Agent Skills format (`SKILL.md`). Nothing tool-specific inside.
- **Starts empty:** your lessons come from your own projects.

## Install

Download `preflight.skill` from the [latest release](https://github.com/R-Dilipkumar/preflight-agent-skill/releases/latest) (it's a zip file) and unzip it into your tool's skills folder, or clone the repo:

```bash
git clone https://github.com/R-Dilipkumar/preflight-agent-skill.git
```

Then copy the `preflight` folder into the skills folder for your tool:

| Tool | Skills folder (all projects) |
|---|---|
| Claude Code | `~/.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| GitHub Copilot | `~/.copilot/skills/` |
| Cursor | `~/.cursor/skills/` (also reads `~/.claude/skills/` and `~/.codex/skills/`) |

For example, for Claude Code:

```bash
cp -r preflight-agent-skill/preflight ~/.claude/skills/
```

Folder names change as tools update, so check your tool's skills docs if it doesn't pick the skill up.

**Using more than one tool?** Keep one real copy (for example in `~/.agents/skills/preflight`) and link the other tools' folders to it, so every tool reads and writes the same lessons instead of each learning alone.

**Tool without skill support?** Put the `preflight` folder anywhere and add this line to the tool's instructions file:

```markdown
Before planning or building, after fixing any bug, and at the end of each piece of work, read /path/to/preflight/SKILL.md and follow it.
```

**Chat apps (claude.ai etc.):** you can upload `preflight.skill` where the app lets you add skills. There, the agent can read the skill but usually can't save new lessons into it.

## Setup

Skills load when a request looks like a match. To make sure it runs on every project, add this line to your tool's global instructions file (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Copilot instructions or Cursor rules):

```markdown
Use the preflight skill before planning or building, after fixing any bug or snag, and at the end of each piece of work.
```

## How it works

| When | What the agent does |
|---|---|
| Before planning | Reads the project's `session.md` and the matching lessons, then researches anything risky in the plan |
| While building | Follows `standards.md`, works in small steps, tests on the real target early, and finds the cause of a failure before trying another fix |
| After a snag is fixed | Saves one lesson (rule or fact) and tells you in one line |
| End of each piece of work | Updates `session.md` and saves any snag it missed |

Files in `preflight/`:

- `SKILL.md`: when and how to use everything below
- `standards.md`: coding rules
- `research.md`: the check-before-using routine
- `session-template.md`: session.md rules and layout
- `lessons/`: `general.md` plus topic files (Android, web, ...) that the agent creates as lessons come in

## Good to know

- The self-updating part needs a tool that can edit files on your computer (a coding agent, not a plain chat).
- It only learns from snags the agent notices. If you fix something yourself, tell it so it can save the lesson.
- Lessons are plain Markdown, so you can read, edit or delete them any time.
- `session.md` is meant to stay local: the agent adds it to each project's `.gitignore` unless you ask otherwise.
- Don't put secrets in lessons. The skill tells the agent not to store keys, passwords, emails or device IDs.
- Want to share your lessons? Copy your `lessons/` folder, but read it first: it describes your own projects.

## Build from source

Package the skill folder as a `.skill` file (a zip):

```bash
cd preflight-agent-skill && zip -r preflight.skill preflight
```

## License

[MIT](LICENSE) © 2026 Dilipkumar R
