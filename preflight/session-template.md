# session.md rules

- One `session.md` per project, in the project root. Create it if missing.
- Local only: add `session.md` to `.gitignore` unless the user asks to commit it. Never delete it.
- Update it at the end of each piece of work, not after every step.
- The top part is the current truth: rewrite it so it stays correct. The Log is history: add to it, newest at the bottom, dated.
- "Start here" must be enough for a fresh session to pick up the work without reading the whole log.
- Plain words. Dates as YYYY-MM-DD (add a time if useful).
- No passwords, keys or tokens in it.
- Each log entry ends with a "Snags → lessons" line, so snags feed the lessons files (SKILL.md step 3).

# Template

```markdown
# session.md — <Project name>

## Start here
_Last updated: <YYYY-MM-DD>_

**What this is:** <one or two lines: what it does, the stack, repo link>

**Current state:**
- <version / what's released>
- <what works, what's not tested yet>

**Key decisions and why:**
- <decision>: <why> (<date>)

**Open / next:**
- <next step>

**Useful commands:**
- Build / test: `...`
- Run / install: `...`
- Release: `...`

---

## Log (newest at the bottom)

### <YYYY-MM-DD>: <short title>
- Done: <what changed>
- Found: <anything learned about the code, device or tools>
- Snags → lessons: <snag> → <saved to lessons/<file>.md, or "nothing to save">
```
