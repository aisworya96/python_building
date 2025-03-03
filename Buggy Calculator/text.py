def add (a, b):
    return a - b

def substract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / 0

def calculator():
    print("Simple Calculator")
    num1 = input("Enter first number: ")  # Bug: Should convert input to int or float
    num2 = input("Enter second number: ")



