def square():
    n = float(input("Enter a number:"))
    print(n*n)

def rectangle():
    n = float(input("Enter a number:"))
    m = float(input("Enter second number:"))
    print(n*m)

def triangle():
    n = float(input("Enter a number:"))
    m = float(input("Enter second numbe:"))
    print((n*m)/2)

x = int(input("Enter a number:"))
if x == 1:
    square()
if x == 2:
    rectangle()
if x == 3:
    triangle()
