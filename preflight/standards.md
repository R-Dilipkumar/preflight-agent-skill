# Coding standards

Short on purpose: only rules that change how code gets written. Generic advice ("write clean code") is left out.

1. **Build only what was asked.** No extra features, settings or options "just in case". Add them when there's a real need.
2. **Simple first.** Write the obvious version. Optimise only after measuring a real problem.
3. **Fail loudly, never silently.** A failed check must block or show a clear error, never pass as "OK". Log errors with context (what failed, with which input). Never swallow exceptions.
   *Why:* when a retired API returns an error and the check "passes" anyway, bad data gets through unnoticed.
4. **Copy twice, share on the third.** Make shared code only when the same logic shows up a third time. If a shared helper keeps growing flags and if-branches for each caller, undo it and go back to copies.
5. **Delete only what's confirmed unused.** Before deleting, search every caller, including ones code search misses: JNI/native code, reflection, XML/manifest, saved setting keys, file names.
   *Why:* fields read only by native code, or names used as saved setting values, look unused to a text search.
6. **Names say the meaning and the unit.** `timeoutMs`, `maxPieceSec`, not `t` or `max`. Follow the project's existing naming style; use one word per idea (don't mix "login" and "sign in").
7. **Small steps, real target early.** Run each step on the real device or browser before building the next one, so a wrong guess costs one step, not a whole feature.
8. **Verify before trusting.** Specs, outside audits, research docs, search results and my own memory can all be wrong. Check each claim against the code or the official docs before acting on it.
   *Why:* outside specs and audits are often partly wrong: code that doesn't compile, outdated library picks, bugs that aren't there.
