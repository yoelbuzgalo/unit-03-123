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
    
def get_guess(secret_num):
    guessed_num = int(input("Enter your guess: "))
    result = check_guess(secret_num, guessed_num)
    print(result)
    return result

def start_game():
    secret_num = secret_number()
    if get_guess(secret_num) == CORRECT:
        print("You win!")
    if get_guess(secret_num) == CORRECT:
        print("You win!")
    if get_guess(secret_num) == CORRECT:
        print("You win!")
    if get_guess(secret_num) == CORRECT:
        print("You win!")
    if get_guess(secret_num) == CORRECT:
        print("You win!")
    print("You ran out of guesses!")



def main():
    start_game()


if __name__ == "__main__":
    main()