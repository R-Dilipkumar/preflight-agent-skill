---
name: preflight
description: A "check before you build" routine plus a lessons memory that grows from real mistakes across all projects, and the rules for each project's session.md. Use at the START of planning or building any app, feature or project (before writing code or picking libraries, APIs, SDK versions, AI models, cloud services or payment methods); whenever choosing between tools or wondering if something is deprecated or works on a given Android version or device; right after a bug, crash, failed build or "works on the emulator but not the phone" snag is fixed, to save what check would have prevented it; and at the end of each piece of work, to update session.md. Use it even when the user doesn't mention it: any coding project counts.
---

# Preflight

A few minutes of checking before building saves hours of fixing after. Every snag we hit becomes one short rule or fact in this skill, so the next project starts smarter. The lessons are written as "before doing X, check Y", never as a bug diary.

All paths below are inside this skill's folder.

## Files

| File | Read it when |
|---|---|
| `standards.md` | Before writing code (once per session) |
| `research.md` | Before picking any library, API, SDK version, model, service or platform feature |
| `lessons/general.md` | Always, when planning |
| `lessons/<topic>.md` | When the project touches that topic (list below) |
| `session-template.md` | When creating or updating a project's session.md |
| `hooks/preflight_reminder.py` | Never needs reading: an optional Claude Code Stop hook that reminds you of steps 3–4 after file edits (at most every 30 min) |

Topics (keep this list in sync when you add a file):
- _None yet. Create a topic file (e.g. `android.md`, `web.md`, `ai-models.md`, `tools.md`) the first time a lesson doesn't fit `general.md`, and list it here with a one-line "covers"._

## 1. Before planning or building

1. Read the project's `session.md` if it exists ("Start here" and "Next").
2. Read `lessons/general.md` and every topic file that matches the project.
3. List the risky choices in the plan: anything new to us, tied to a version, tied to a device, or where training knowledge may be out of date (model names, deprecations, platform rules). Run `research.md` on each. Skip choices a lesson already settles.
4. Add a short "Checked before starting" part to the plan: what was checked and which lessons apply. A few lines, not an essay.

## 2. While building

- Follow `standards.md`.
- Build in small steps and run on the real target early: the real phone, a 375px browser width, the release (minified) build.
- When something fails, stop and find the cause before trying another fix. Don't jump to the next search result or the next library hoping it works.

## 3. After a snag is fixed: save the lesson

A snag is anything that cost a retry: a build or runtime failure, works on the emulator but not the phone, a deprecated or retired API, the wrong library or model version, a platform limit, a wrong assumption.

Ask: **"What check, done before starting, would have avoided this?"**
- No sensible check (a typo, a logic slip tests caught quickly, the user changed their mind): save nothing.
- A general habit: save a **rule**.
- A specific tech detail: save a **fact**, with the month it was checked.

Then:
1. Read the target lessons file. If a similar entry exists, sharpen it instead of adding a new one.
   Before changing it, back it up: copy it to `backups/<file name>-<YYYY-MM-DD>.md` (one copy per file per day is enough; keep the 5 newest per file and delete older ones). To undo a bad edit, copy a backup back. Do the same before editing any other file in this skill.
2. If this is the second fact of the same kind, merge them into one rule and keep the facts as short examples under it.
3. Write one line in the format below.
4. If no topic file fits and the topic will likely come up again, create a new file and add it to the Topics list above.
5. Tell the user in one line, e.g. "Lesson saved (lessons/android.md): check codec size limits before encoding."

Formats:
- Rule: `- **Before <action>:** <check>. *Why:* <what went wrong, short> (<project>, <YYYY-MM>)`
- Fact: `- <fact>. (checked <YYYY-MM>, <project>)`

Keeping it useful:
- Each lessons file stays under about 60 lines. When it grows past that, merge similar entries and drop ones that no longer matter.
- Facts older than 6 months: re-check before trusting; update the date or delete.
- Write lessons so they help on a different project, not only this one.
- Never store secrets, keys, passwords, emails, phone numbers or device IDs here.

## 4. End of each piece of work

1. Update the project's `session.md` (see `session-template.md`).
2. Look back: any snag this session not saved yet? Save it (step 3).
3. If any skill file changed, say so in one line in the wrap-up.
