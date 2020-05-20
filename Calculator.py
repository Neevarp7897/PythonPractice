import re

print('Welcome to the Magical Calculator')
print('\nType "QUIT" to exit this calculator\n')
previous = 0  # Previous is used to store the previously calculated value.
run = True  # Run is used for executing the calculation until the user quit.


def perform_math():  # Function for performing the mathematical operations
    global run  # Global keyword is used for accessing the Global variables.
    global previous
    expression = ''  # Expression is used to store the user input
    if previous == 0:
        expression = input('Enter the equation: ')
    else:
        expression=input(str(previous))

    if expression == 'QUIT':
        print('\nGoodbye.')
        run = False  # Exit from the calculation
    else:
        expression = re.sub('[a-zA-Z,.' ']', '', expression)  # Removes the values other than integer
        if previous == 0:
            previous = eval(expression)  # Performs calculation
        else:
            previous = eval(str(previous)+expression)  # Performs calculation along with the previous output.


while run:  # Loop to execute the calculation multiple times.
    perform_math()  # Calling Function
