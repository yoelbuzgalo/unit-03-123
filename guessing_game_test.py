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