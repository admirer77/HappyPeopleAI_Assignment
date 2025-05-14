# 1. Write a function for arithmetic operators(+,-,*,/)

def perform_arithmetic(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None  # Handle division by zero
        else:
            return num1 / num2
    else:
        print("Error: Invalid operator. Please use '+', '-', '*', or '/'.")
        return None  # Handle invalid operator

# Driver code
number1 = 100
number2 = 500

addition_result = perform_arithmetic(number1, number2, '+')
print(f"{number1} + {number2} = {addition_result}")

subtraction_result = perform_arithmetic(number1, number2, '-')
print(f"{number1} - {number2} = {subtraction_result}")

multiplication_result = perform_arithmetic(number1, number2, '*')
print(f"{number1} * {number2} = {multiplication_result}")

division_result = perform_arithmetic(number1, number2, '/')
print(f"{number1} / {number2} = {division_result} \n")


# 2. Write a method for increment and decrement operators(++, --)

def increment(number):
    return number + 1

def decrement(number):
    return number - 1

# Driver code
num = 10

# Increment
num = increment(num)  # Equivalent to num++ in other languages
print("Incremented value:", num)  # Output: 11

# Decrement
num = decrement(num)  # Equivalent to num-- in other languages
print("Decremented value:", num)  # Output: 10

print()
# 3. Write a program to find the two numbers equal or not.

def eq(num1, num2):
    if num1 == num2:
        print(f"{num1} and {num2} are equal \n")
    else:
        print(f"{num1} and {num2} are not equal \n")

eq(0,0)
eq(1,2)

# 4. Program for relational operators (<,<==, >, >==)

def relational_operators_example(a, b):
    
    # Less than operator (<)
    print(f"a < b: {a < b}")

    # Less than or equal to operator (<=)
    print(f"a <= b: {a <= b}")

    # Greater than operator (>)
    print(f"a > b: {a > b}")

    # Greater than or equal to operator (>=)
    print(f"a >= b: {a >= b}")

    # Equal to operator (==)
    print(f"a == b: {a == b}")

    # Not equal to operator (!=)
    print(f"a != b: {a != b} \n")

# Driver code

relational_operators_example(7, -7)

# 5. Print the smaller and larger number

a = 2
b = 3

if a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{b} is smaller than {a}")
