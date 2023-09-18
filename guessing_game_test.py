import guessing_game
import random

def test_secret_number():
    # Setup
    random.seed(1)
    expected = 18
    
    # Invoke
    result = guessing_game.secret_number()

    # Analyze
    assert result == expected

def test_check_number_correct():
    # Setup
    random.seed(1)
    expected = guessing_game.CORRECT
    secret_num = guessing_game.secret_number()
    guessed_num = 18

    # Invoke
    result = guessing_game.check_guess(secret_num, guessed_num)

    # Analyze
    assert result == expected

def test_check_number_low():
    # Setup
    random.seed(1)
    expected = guessing_game.TOO_LOW
    secret_num = guessing_game.secret_number()
    guessed_num = 15

    # Invoke
    result = guessing_game.check_guess(secret_num, guessed_num)

    # Analyze
    assert result == expected

def test_check_number_high():
    # Setup
    random.seed(1)
    expected = guessing_game.TOO_HIGH
    secret_num = guessing_game.secret_number()
    guessed_num = 23

    # Invoke
    result = guessing_game.check_guess(secret_num, guessed_num)

    # Analyze
    assert result == expected