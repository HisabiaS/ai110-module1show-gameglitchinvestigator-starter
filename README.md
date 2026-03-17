# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:**
A number-guessing game built with Streamlit. The player picks a difficulty, gets a limited number of attempts, and receives higher/lower hints after each guess. A score is tracked based on how quickly they find the secret number.

**Bugs found:**

| # | Bug | Location |
|---|-----|----------|
| 1 | New Game button did nothing after a win or loss — game stayed frozen | `app.py` New Game handler |
| 2 | Hints were reversed — "Go HIGHER!" when guess was too high, "Go LOWER!" when too low | `check_guess` in `app.py` |
| 3 | New Game always picked a secret from 1–100, ignoring the selected difficulty range | `app.py` line 136 |

**Fixes applied:**

- **Bug 1:** Added `st.session_state.status = "playing"` and `st.session_state.history = []` to the New Game handler so the game fully resets on rerun.
- **Bug 2:** Swapped the hint messages in `check_guess` — `guess > secret` now correctly returns "Go LOWER!" and `guess < secret` returns "Go HIGHER!".
- **Bug 3:** Changed `random.randint(1, 100)` to `random.randint(low, high)` in the New Game handler so it respects the difficulty range.
- **Refactor:** Moved all four logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) from `app.py` into `logic_utils.py` and updated `app.py` to import them.
- **Tests:** Fixed the broken starter tests and added 8 new pytest cases targeting each bug.

## 📸 Demo

- <img width="1874" height="912" alt="image" src="https://github.com/user-attachments/assets/4804bb09-0d25-4945-b992-93a7b455b856" />


