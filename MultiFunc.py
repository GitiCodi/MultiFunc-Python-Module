import math, random

def len_analyze(variable_or_string):
    length = len(variable_or_string)
    print(f"string length: {length}")

def RamdomNum(between1, between2):
    if not isinstance(between1, int):
        print("Type Error: between1 should be an integer")
    elif not isinstance(between2, int):
        print("Type Error: between1 should be an integer")
    else:
        print(random.randint(between1, between2))

def Addition(num1, num2):
    if not isinstance(num1, int):
        print("TypeError: num1 should be an integer")
    elif not isinstance(num2, int):
        print("TypeError: num2 should be an integer")
    else:
        print(num1 + num2)

def Subtraction(num1, num2):
    if not isinstance(num1, int):
        print("TypeError: num1 should be an integer")
    elif not isinstance(num2, int):
        print("TypeError: num2 should be an integer")
    else:
        print(num1 - num2)

def Multiplication(num1, num2):
    if not isinstance(num1, int):
        print("TypeError: num1 should be an integer")
    elif not isinstance(num2, int):
        print("TypeError: num2 should be an integer")
    else:
        print(num1 * num2)

def Dividition(num1, num2):
    if not isinstance(num1, int):
        print("TypeError: num1 should be an integer")
    elif not isinstance(num2, int):
        print("TypeError: num2 should be an integer")
    else:
        print(num1 / num2)

