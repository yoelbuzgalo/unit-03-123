def add(x,y):
    '''
    This function adds two passed arguments and returns a string of the addition
    '''
    sum = x+y # Adds the two passed arguments
    return str(x) + " + " + str(y) + " = " + str(sum) # Casts x, y and the product variables to a string and returns them as a string

def subtract(x,y):
    '''
    This function subtracts two passed arguments and returns a string of the subtraction
    '''
    differences = x-y # Subtracts the two passed arguments
    return str(x) + " - " + str(y) + " = " + str(differences) # Casts x, y and the product variables to a string and returns them as a string

def multiply(x,y):
    '''
    This function multiplies two passed arguments and returns a string of the multiplication
    '''
    product = x*y # Multiplies the two passed arguments
    return str(x) + " * " + str(y) + " = " + str(product) # Casts x, y and the product variables to a string and returns them as a string
