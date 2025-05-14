#basics

# 1. Write a program to print your name
print("Nehanth \n")

# 2. Write a program for a Single line comment and multi-line comments

    # This is a single-line comment in Python.
    # It starts with a '#' symbol.
    # Single-line comments are used to explain a single line of code.

print("Print comment line \n")  # This comment explains the print statement.

"""
This is a multi-line comment in Python.
It is also called a docstring (documentation string).
Multi-line comments are enclosed in triple quotes (either single or double).
They are used to explain a block of code or a function.
"""

'''
This is another way to write a multi-line comment in Python,
using triple single quotes.  It's also a docstring.
'''

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

INT = 7
print(f"{INT} is {type(INT)}")
BOOL = True
print(f"{BOOL} is {type(BOOL)}")
FLOAT = 6.1
print(f"{FLOAT} is {type(FLOAT)}")
STR = "QW%^67"
print(f"{STR} is {type(STR)}")


# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

global_var = 5
# Uses global because there is no local variable with the same name
def print_global_value():
    print('Inside print_global_value() : ', global_var)
# Variable 'global_var' is redefined as a local variable
def create_local_variable():
    global_var = 2
    print('Inside create_local_variable() : ', global_var)
# Uses global keyword to modify the global variable 'global_var'
def modify_global_variable():
    global global_var
    global_var = 4       # Value of 'global_var' is modified
    print('Inside modify_global_variable() : ', global_var)
# Global scope
print('global : ', global_var)
print_global_value()
print('global : ', global_var)
create_local_variable()
print('global : ', global_var)
modify_global_variable()
print('global : ', global_var)