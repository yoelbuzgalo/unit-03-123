def squared(x):
    value = x*x
    return value

def cubed(x):
    value = x**3
    return value

def main():
    x = int(input("Enter a number: "))
    square = squared(x)
    cube = cubed(x)
    print(x, "^2 =", square)
    print(x, "^3 =", cube)

main()