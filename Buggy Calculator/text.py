def add (a, b):
    return a - b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / 0

def calculator():
    print("Simple Calculator")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    print("Choose operation: +, -, *, /")
    operation = input("Enter operation: ")

    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")

calculator()




