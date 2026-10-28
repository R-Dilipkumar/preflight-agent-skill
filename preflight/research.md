# Research routine (before using something)

Use this before choosing any library, SDK or API, AI model, cloud service, payment method, or platform feature, and whenever my knowledge may be out of date. Keep it quick: a few minutes and a few searches. Small, well-known choices need no research.

## Steps

1. **Check the lessons first.** Read the matching `lessons/` file. If it already answers the question (and the fact isn't older than 6 months), use it and stop.
2. **Go to the official source first:** the docs, release notes or changelog, GitHub releases and open issues, the model card. Blogs and forum answers come second and are often out of date.
3. **Answer these for each option:**
   - What is the current stable version, and when was it last updated?
   - Is it deprecated, retired, or scheduled to shut down? (Hosted AI models retire often.)
   - Does it work on our minimum platform version and our real device (Android version, GPU, chip, OEM skin, browser)?
   - Is it a public API, or hidden/internal?
   - Is the licence OK for how it will be used (personal, open source, selling)?
   - Does it work with the versions of the other pieces we use?
   - Are there known open issues that hit our use case?
   - For models: exact variant (what it was fine-tuned on), languages, size, and speed on our device.
4. **Compare 2–3 options** when there's a real choice. Pick one and give a one-line reason.
5. **Write it down.** Put the choice, the reason and the date in the project's session.md under "Key decisions".
6. **If still unsure, build a tiny test first:** the smallest code that proves it works on the real target (one shader, one model run on a 1-minute clip, one API call), before building UI or features on top.

## When the first attempt fails

- Stop. Read the actual error and find out *why* it failed before trying the next option.
- Don't cycle through search results hoping one works. Each switch without knowing the cause wastes a full build-and-test round.
- Once the cause is known, save it as a lesson (SKILL.md step 3).
