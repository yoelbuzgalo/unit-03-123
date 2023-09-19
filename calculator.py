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