# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").


When I first ran the game, it launched in Streamlit and appeared to work 
on the surface — but several bugs became clear after playing it a couple 
of times.

**Bug 1: Hints are reversed/lying**
Expected: If my guess was too low, the hint should say "go higher."
Actual: The hints pointed me in the wrong direction, guiding me away 
from the secret number instead of toward it. I never found the number 
despite following the hints.

**Bug 2: New Game button does nothing**
Expected: Clicking "New Game" should reset the game and start fresh 
with a new secret number.
Actual: Clicking the button had no effect — the game stayed in its 
current state with no reset.

**Bug 3: Duplicate guesses are silently ignored**
Expected: If I submit the same number twice, the game should either 
warn me ("You already guessed that!") or count it as a wasted attempt.
Actual: The game accepted the duplicate without any message, didn't 
count it as an attempt, but still registered the value — inconsistent 
and confusing behavior.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code (Anthropic) as my primary AI tool throughout this project. 
It was accessible directly inside VS Code and could read and edit multiple 
files at once, similar to Copilot Agent Mode.

**Example of a correct AI suggestion:**
I asked Claude Code to move the `check_guess` function from `app.py` into 
`logic_utils.py` and fix the bug where the secret number was being converted 
to a string on even attempts. Claude Code correctly removed the broken 
`if st.session_state.attempts % 2 == 0` block, moved the function to 
`logic_utils.py`, and updated the import in `app.py` automatically. I verified 
this was correct by running the app and confirming hints were no longer lying, 
and by running `pytest tests/ -v` which showed 6/6 tests passing.

**Example of an incorrect/misleading AI suggestion:**
While Claude Code fixed the string conversion bug, it made two mistakes I had 
to catch myself. First, it kept the hint messages backwards — when a guess was 
too high it said "Go HIGHER!" instead of "Go LOWER!". Second, the emojis were 
corrupted during the move, appearing as `ð` instead of 🎉 📈 📉. The AI did 
not flag either issue. I caught them by carefully reviewing the diff before 
accepting, and fixed both manually in `logic_utils.py`. This taught me that 
AI suggestions always need human review — even when the main task looks correct.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
