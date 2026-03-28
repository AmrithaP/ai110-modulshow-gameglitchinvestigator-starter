from logic_utils import check_guess

# --- Starter tests (fixed to unpack tuple correctly) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be Too High
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be Too Low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- New tests for Bug 1 fix ---

def test_hint_message_too_high():
    # Hint should say Go LOWER when guess is too high
    outcome, message = check_guess(80, 50)
    assert "LOWER" in message

def test_hint_message_too_low():
    # Hint should say Go HIGHER when guess is too low
    outcome, message = check_guess(20, 50)
    assert "HIGHER" in message

def test_no_string_conversion():
    # Secret should always be compared as int, never converted to string
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"