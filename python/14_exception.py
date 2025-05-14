# 1. Write a program to generate Arithmetic Exception without exception handling
def generate_arithmetic_exception():
    result = 10 / 0

# Driver code for 1
print("1. Generating Arithmetic Exception without handling:")
# Uncomment the line below to see the exception
# generate_arithmetic_exception()


# 2. Handle the Arithmetic exception using try-except block
def handle_arithmetic_exception():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Arithmetic Exception handled: {e}")

# Driver code for 2
print("\n2. Handling Arithmetic Exception using try-except block:")
handle_arithmetic_exception()


# 3. Write a method which throws exception, Call that method in main class without try block
def method_throws_exception():
    raise Exception("This is an exception")

# Driver code for 3
print("\n3. Method throwing exception without try block:")
# Uncomment the line below to see the exception
# method_throws_exception()


# 4. Write a program with multiple catch blocks
def multiple_catch_blocks():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except Exception as e:
        print(f"Caught Exception: {e}")

# Driver code for 4
print("\n4. Multiple catch blocks:")
multiple_catch_blocks()


# 5. Write a program to throw exception with your own message
def throw_custom_exception():
    raise Exception("This is a custom exception message")

# Driver code for 5
print("\n5. Throwing exception with custom message:")
# Uncomment the line below to see the exception
# throw_custom_exception()


# 6. Write a program to create your own exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

def raise_custom_exception():
    raise MyCustomException("This is my custom exception")

# Driver code for 6
print("\n6. Creating and raising custom exception:")
# Uncomment the line below to see the exception
# raise_custom_exception()


# 7. Write a program with finally block
def program_with_finally():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Exception caught: {e}")
    finally:
        print("This is the finally block, executed regardless of exception")

# Driver code for 7
print("\n7. Program with finally block:")
program_with_finally()


# 8. Write a program to generate Arithmetic Exception
def generate_arithmetic_exception_again():
    result = 10 / 0

# Driver code for 8
print("\n8. Generating Arithmetic Exception:")
# Uncomment the line below to see the exception
# generate_arithmetic_exception_again()


# 9. Write a program to generate FileNotFoundException
def generate_file_not_found_exception():
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()

# Driver code for 9
print("\n9. Generating FileNotFoundException:")
# Uncomment the line below to see the exception
# generate_file_not_found_exception()


# 10. Write a program to generate ClassNotFoundException
def generate_class_not_found_exception():
    raise ImportError("Class not found")

# Driver code for 10
print("\n10. Generating ClassNotFoundException:")
# Uncomment the line below to see the exception
# generate_class_not_found_exception()


# 11. Write a program to generate IOException
def generate_io_exception():
    raise IOError("This is an IO exception")

# Driver code for 11
print("\n11. Generating IOException:")
# Uncomment the line below to see the exception
# generate_io_exception()


# 12. Write a program to generate NoSuchFieldException
def generate_no_such_field_exception():
    raise AttributeError("No such field found")

# Driver code for 12
print("\n12. Generating NoSuchFieldException:")
# Uncomment the line below to see the exception
# generate_no_such_field_exception()

