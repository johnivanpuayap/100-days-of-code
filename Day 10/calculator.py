# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def modulo(n1, n2):
    return n1 % n2

operations = {'+': add, 
              '-': subtract, 
              '*': multiply, 
              '/': divide,
              '%': modulo}

def calculator():

    num1 = int(input("What's the first number?: "))

    again = True

    while again:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the second number?: "))

        function = operations[operation_symbol]
        result = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        todo = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or any other character to exit: ")

        if todo == 'y':
            num1 = result
        elif todo == 'n':
            again = False
            calculator()
        else:
            break
        
calculator()