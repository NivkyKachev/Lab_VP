def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def mult(a, b):
    return a * b

def devision(a, b):
    return a / b


operation = input("Enter operator: +, -, *, / ")

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))

if operation == "+":
    print(sum(a, b))
    
elif operation == "-":
    print(subtraction(a, b))
    
elif operation == "*":
    print(mult(a, b))
    
elif operation == "/":
    print(devision(a, b))
