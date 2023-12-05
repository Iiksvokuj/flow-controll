# interactive calculator
from os import system
# CLI - textual terminal

# input values
# *operations: +, -, /, *
# show result
# * interactive menu

# + print formatting

# a + b
while True:
    operand_1 = int(input('> '))
    operation = input('> ')
    operand_2 = int(input('> '))

    system('cls')

    result = 0
    if operation == '+':
        result = operand_1 + operand_2
    if operation == '-':
        result = operand_1 - operand_2
    if operation == '*':
        result = operand_1 * operand_2
    if operation == '/':
        result = operand_1 / operand_2



    print(f"{operand_1:20}\n{operation:>20}\n{operand_2:20}\n--------------------\n{result:20}")

