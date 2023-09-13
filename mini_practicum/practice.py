def convert_height():
    '''
    This function prompts the user to enter their height in inches and will print out their height in feet
    '''
    height_inches = int(input("Enter your height in inches: ")) # Prompts the user to enter their height in inches and castes it to integer
    height_in_feet = height_inches//12 # Converts inches to feet
    height_remainder = height_inches - height_in_feet*12 # Gets the remainder of the height in inches after feet
    print("You are ", height_in_feet, "\' ", height_remainder, "\" ", "tall", sep="") # Prints out to the console

def before(letter):
    '''
    This function takes in a letter and will print the original letter and the 3 preceeding alphabet letters
    '''
    letter_ascii_value = ord(letter) # Converts passed letter argument to ASCII value
    letter_1 = letter_ascii_value+1 # Adds one integer value to letter ascii value (next letter)
    letter_2 = letter_ascii_value+2 # Adds two integer value to letter ascii value (next 2 letters)
    letter_3 = letter_ascii_value+3 # Adds three integer value to letter ascii value (next 3 letters)
    print(chr(letter_ascii_value),chr(letter_1),chr(letter_2),chr(letter_3),sep="\n") # Converts all back to chr (the actual ascii key of the given value) and prints to the console


def main():
    '''
    The main function that runs this program
    '''
    convert_height() # Calls convert_height function
    before("a") # Calls before function

main()