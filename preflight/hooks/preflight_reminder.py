"""Stop hook: reminds the agent to run preflight's end-of-work steps.

Fires only when files were edited since the last reminder, and at most once
every 30 minutes per session, so it doesn't nag on every turn. Any error
means "do nothing": a broken reminder must never block the user's work.
"""
import json
import os
import re
import sys
import time

COOLDOWN_SEC = 30 * 60
EDIT_TOOL = re.compile(r'"type":\s*"tool_use",\s*"id":\s*"[^"]*",\s*"name":\s*"(Edit|Write|MultiEdit|NotebookEdit)"')
STATE_DIR = os.path.join(os.path.expanduser("~"), ".claude", "preflight-reminder")

REASON = (
    "Preflight end-of-work check (automatic, at most every 30 min, only after file edits). "
    "If a snag in this work cost a retry, save one lesson (preflight SKILL.md step 3; back up the lessons file first), "
    "and update the project's session.md if a piece of work just finished. "
    "If there was no snag and session.md is current, just finish without mentioning this check."
)


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        return
    session_id = data.get("session_id") or ""
    transcript = data.get("transcript_path") or ""
    if not session_id or not os.path.isfile(transcript):
        return

    with open(transcript, encoding="utf-8", errors="ignore") as f:
        edit_count = len(EDIT_TOOL.findall(f.read()))

    os.makedirs(STATE_DIR, exist_ok=True)
    state_file = os.path.join(STATE_DIR, re.sub(r"[^A-Za-z0-9_-]", "_", session_id) + ".json")
    state = {"edits": 0, "time": 0}
    if os.path.isfile(state_file):
        with open(state_file, encoding="utf-8") as f:
            state = json.load(f)

    now = time.time()
    if edit_count <= state["edits"] or now - state["time"] < COOLDOWN_SEC:
        return

    with open(state_file, "w", encoding="utf-8") as f:
        json.dump({"edits": edit_count, "time": now}, f)
    print(json.dumps({"decision": "block", "reason": REASON}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
