import math

def fact(num):
    '''
    This function calls factorial function if the num is positive
    '''
    if num > 0:
        return math.factorial(num) # Calls the factorial function from math library and returns the result
    return 0

def root(num):
    '''
    This function calls sqrt function if the num is positive
    '''
    if num > 0:
        return math.sqrt(num) # Calls the sqrt function from math library and returns the result
    return 0

def trunk(num):
    '''
    This function calls trunc function for given int/float number
    '''
    return math.trunc(num) # Calls trunc function from math library and returns the result

def main():
    input_number = input("Enter a number: ") # Prompts the user to enter a number
    print(fact(int(input_number))) # Converts input number to int and calls factorial function and prints out the result
    print(root(float(input_number))) # Converts input number to float and calls root function and prints out the result
    print(trunk(float(input_number))) # Calls trunk function and prints out the result

if __name__ == "__main__":
    main()