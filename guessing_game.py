import random

MINIMUM = 1
MAXIMUM = 100

CORRECT = "Correct"
TOO_HIGH = "Too High"
TOO_LOW = "Too Low"

def secret_number():
    '''
    This function generates a random secret number and returns it
    '''
    return random.randint(MINIMUM,MAXIMUM)

def check_guess(number, guess):
    '''
    This function compares a number to player's guessed number
    '''
    if guess == number:
        return CORRECT # Returns correct if number matches
    
    if guess > number:
        return TOO_HIGH # Returns too high if guessed number is too high
    
    if guess < number:
        return TOO_LOW # Returns too low if guessed number is too low