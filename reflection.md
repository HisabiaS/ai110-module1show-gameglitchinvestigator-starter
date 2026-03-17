# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Answer:

The first time I ran the game, it appeared to work but quickly showed problems during actual play. I identified three bugs:

1. **New Game button broken after game over** — After winning or losing, clicking "New Game" did nothing. The game stayed frozen on the win/loss screen. I expected it to reset everything and start fresh.
2. **Hints are reversed** — When my guess was too high, the game said "Go HIGHER!" and when it was too low, it said "Go LOWER!" — the exact opposite of what it should say.
3. **New Game ignores difficulty range** — Even on Easy mode (range 1–20), starting a new game would pick a secret number from 1–100 because the code used `random.randint(1, 100)` hardcoded instead of using the difficulty range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Answer:

I used Claude Code (Claude Sonnet) as my AI assistant throughout this project.

**Correct suggestion — Bug 1 fix:** The AI correctly identified that the New Game handler was missing `st.session_state.status = "playing"`. When New Game was clicked, it reset attempts and generated a new secret, but left the status as `"won"` or `"lost"`. On the next rerun, the status check at line 142 would immediately call `st.stop()`, freezing the game. I verified this by clicking New Game after winning — the game successfully reset and I could play again.

**Incorrect/misleading suggestion — existing tests:** The AI initially did not flag that the starter tests in `test_game_logic.py` were already broken. The tests compared `check_guess(60, 50)` directly to the string `"Too High"`, but `check_guess` returns a tuple `(outcome, message)`. That comparison would always fail. I caught this by running `pytest` and reading the actual failure output, then fixed the tests to unpack the tuple: `outcome, _ = check_guess(60, 50)`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Answer:

I used two layers of verification for each fix: automated pytest tests and manual testing in the live Streamlit app.

For Bug 2 (inverted hints), I added two targeted tests: `test_too_high_message_says_lower` checks that `check_guess(60, 50)` returns a message containing "LOWER", and `test_too_low_message_says_higher` checks that `check_guess(40, 50)` returns a message containing "HIGHER". Both passed after the fix. I also manually played the game, guessing a number I knew was too high, and confirmed the hint now correctly said "Go LOWER!".

The AI helped me structure the tests — it suggested checking only the relevant part of the return value (the message string) rather than matching the entire tuple, which made the tests cleaner and more focused on exactly what the bug was about.

Running `pytest -v` showed all 11 tests passing, including the 3 original starter tests (once fixed) and 8 new ones targeting the bugs.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Answer:

Streamlit reruns the entire Python script from top to bottom every time the user interacts with the app — clicking a button, typing in a box, or changing a sidebar setting all trigger a full rerun. Without session state, any variable you set (like a random secret number) gets thrown away and recreated on each rerun.

Think of it like a website that refreshes the whole page every time you click anything. If your secret number was just `secret = random.randint(1, 100)`, it would pick a brand new number every single click. Session state is like a sticky notepad that survives these refreshes — once you write something there, it stays until you explicitly change it.

The fix is the pattern on lines 92–93 of app.py: `if "secret" not in st.session_state: st.session_state.secret = random.randint(low, high)`. This only generates the secret once — on the very first run — and reuses the stored value on every subsequent rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Answer:

One habit I want to keep is always running existing tests before touching any code. When I ran `pytest` early on, it revealed the starter tests were already broken — the AI had written tests that compared a tuple to a string, which would always fail. Catching that first saved me from assuming my own fixes were the cause of failures.

Next time I work with AI on a debugging task, I would ask it to explicitly explain *why* the bug exists (the root cause) before jumping to a fix. In this project the AI sometimes gave the correct fix without making the underlying reason obvious, which made it harder to learn from.

This project shifted my view of AI-generated code from "probably correct, just check for typos" to "assume there are logic bugs and verify every behavior." The code looked reasonable on the surface — it ran, it had functions with sensible names — but the actual logic was wrong in multiple places that only showed up during real play.

