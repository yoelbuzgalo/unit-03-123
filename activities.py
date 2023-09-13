import math

def squared(x):
    value = math.pow(x, 2)
    return value

def cubed(x):
    value = math.pow(x, 3)
    return value

def main():
    x = int(input("Enter a number: "))
    square = squared(x)
    cube = cubed(x)
    print(x, "^2 =", square)
    print(x, "^3 =", cube)

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