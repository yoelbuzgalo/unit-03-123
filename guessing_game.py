import random

MINIMUM = 1
MAXIMUM = 100

def secret_number():
    '''
    This function generates a random secret number and returns it
    '''
    return random.randint(MINIMUM,MAXIMUM)