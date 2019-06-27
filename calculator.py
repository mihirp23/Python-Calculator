# Name : Mihir Patel
# Date : 6/27/19
# File : calculator.py
# Interactive Calculator that allows user to perform
# mathematical operations on either one or two operands.

import math

############################################################
def get_numeric_input(prompt_str):
############################################################
# Purpose of this function is to prompt the user the
# provided string and retrieve a numeric input.
    while True:
        try:
            num = float(input(prompt_str))
        except ValueError:
            print("please enter a numeric value")
            continue
        else:
            break

    return num

# get_numeric_input()

############################################################
def calculate(operator, operand1, operand2=None):
############################################################
# purpose of this function is to calculate the result
# value based on provided operand(s) and operator.
# Some operators are only on single value, therefore
# the second operand is an optional argument.

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            # prevent dividing by zero
            result = "Undefined"
        else:
            result = operand1 / operand2
    elif operator == "^":
        result = math.pow(operand1, operand2)
    elif operator == "factorial":
        try:
            result = math.factorial(operand1)
        except ValueError:
            result = None
    elif operator == "sqrt":
        try:
            result = math.sqrt(operand1)
        except ValueError:
            result = None
    elif operator == "gcd":
        try:
            result = math.gcd(int(operand1), int(operand2))
        except ValueError:
            result = None
    else:
        result = None

    return result
# calculate()


############################################################
def main():
############################################################

    # initialize constant variables
    SINGLE_VALUE_OPERATIONS = ['factorial', 'sqrt']
    MULTIPLE_VALUE_OPERATIONS = ['+', '-', '*', '/', '^', 'gcd']
    OPERATIONS = SINGLE_VALUE_OPERATIONS + MULTIPLE_VALUE_OPERATIONS

    # display a welcome message to user
    print("Welcome to the CLI Calculator")
    print("The following operations are available : ")
    print(*OPERATIONS, sep=", ")


    # allow user to use the calculator interactively
    while True:
        op = input("What operation would you like to perform? ")
        if op not in OPERATIONS:
            print("This operation is not recognized by the calculator. Pleas try again.")
            continue
        else:
            if op in SINGLE_VALUE_OPERATIONS:
                number1 = get_numeric_input("enter an integer value: ")
                result = calculate(op, number1)
            else:
                number1 = get_numeric_input("enter the first number: ")
                number2 = get_numeric_input("enter the second number: ")
                result = calculate(op, number1, number2)
            print(result)
# main()

    
############################################################
if __name__ == "__main__":
############################################################
    main()

