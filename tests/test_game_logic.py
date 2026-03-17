from logic_utils import check_guess, get_range_for_difficulty, parse_guess


# --- Existing starter tests (fixed: check_guess returns a tuple) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 2 fix: hint messages must NOT be reversed ---

def test_too_high_message_says_lower():
    # Guess is above secret, so the message must tell the player to go LOWER
    _, message = check_guess(60, 50)
    assert "LOWER" in message.upper()

def test_too_low_message_says_higher():
    # Guess is below secret, so the message must tell the player to go HIGHER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message.upper()


# --- Bug 3 fix: difficulty ranges must be respected ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


# --- parse_guess edge cases ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
