import math
import random

def squared(x):
    value = math.pow(x, 2)
    return value

def cubed(x):
    value = math.pow(x, 3)
    return value

def even_or_odd(n):
    if(n%2 == 0):
        return "even"
    return "false"

def coin_toss():
    randomizer = random.randrange(1,3)
    if randomizer == 1:
        return "heads"
    if randomizer == 2:
        return "tails"

def main():
    # x = int(input("Enter a number: "))
    # square = squared(x)
    # cube = cubed(x)
    # print(x, "^2 =", square)
    # print(x, "^3 =", cube)
    # print(even_or_odd(2))
    # print(coin_toss())
    # print(coin_toss())
    # print(coin_toss())
    # print(coin_toss())
    # print(coin_toss())
    random.seed(100)
    print(random.randrange(1,100))
    print(random.randint(1, 100))
    print(random.random())

if __name__ == "__main__":
    main()

'''
Answers for Activity 3.3:
not d: False
not e: True
d or e: True
d or f: True
e or g: False
d and e: False
d and f: True
d ^ f: False
d ^ e: True
not d and f: False
'''

'''
Answers for Activity: 3.4:
a == b: False
a != b: True
a == (b-5): True
c == d: False
a == c: False
a < b:  True
a <= b: True
a > 5: False
a >= 5: True
c > d: False
c <= d: True
b < c: TypeError
'''


'''
Activity 3.16 Answers:
1. The most common errors I get is "SyntaxError" which is pretty obvious by its name, it specifies what it expects and what is missing (for example missing closing paranthesis)
2. Yes, I usually just look at what line and the expected statement and add in the code itself.
3. Only the PyTest I found a bit confusing because when I first ran it without specifying the file, it tells me all kinds of 'fails' when it actually just ran different files for tests and not the one I wanted.
4. So far most of the errors I get are typically easy to fix, like the SyntaxError or TypeError where I just go back and fix. I did not have anything major error yet.
'''