import math

def add(x,y):
    '''
    This function adds two passed arguments and returns them as a string
    '''
    sum = x+y # Adds the two passed arguments
    return str(x) + " + " + str(y) + " = " + str(sum) # Casts x, y and the sum variable to a string and returns them

def subtract(x,y):
    '''
    This function subtracts two passed arguments and returns them as a string
    '''
    difference = x-y # Subtracts the two passed arguments
    return str(x) + " - " + str(y) + " = " + str(difference) # Casts x, y and the difference variable to a string and returns them

def multiply(x,y):
    '''
    This function multiplies two passed arguments and returns them as a string
    '''
    product = x*y # Multiplies the two passed arguments
    return str(x) + " * " + str(y) + " = " + str(product) # Casts x, y and the product variable to a string and returns them

def divide(x,y):
    '''
    This function divides two passed arguments and returns them as a string
    '''
    if y == 0:
        return str(x) + " / " + str(y) + " = " + "NaN" # If the denominator is 0, it will return a string with NaN
    quotient = x/y # Divides the two passed arguments
    return str(x) + " / " + str(y) + " = " + str(quotient) # Casts x, y and the quotient variable to a string and returns them

def exponent(x,y):
    '''
    This function exponentizes two passed arguments and returns them as a string
    '''
    power = math.pow(x, y) # Raises x to the power of y
    return str(x) + "^" + str(y) + " = " + str(power) # Casts x, y and the power variable to a string and returns them

def main():
    '''
    The main function of this program, prompts the user to enter two numbers and prints out the results of each function called
    '''
    # Prompt user to enter two integer values x and y
    num_x = int(input("enter x: ")) # Casts the first num input to an integer value
    num_y = int(input("enter y: ")) # Casts the second num input to an integer value

    print(add(num_x, num_y)) # Calls add function and prints to the output
    print(subtract(num_x, num_y)) # Calls subtract function and prints to the output
    print(multiply(num_x, num_y)) # Calls multiply function and prints to the output
    print(divide(num_x, num_y)) # Calls divide function and prints to the output
    print(exponent(num_x,num_y)) # Calls exponent function and prints to the output

if __name__ == "__main__":
    main()