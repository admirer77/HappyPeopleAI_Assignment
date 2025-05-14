# 1. Write a program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

print() 

# 2. Write a program to print 1 to 20 numbers using the while loop
i = 1
while i <= 20:
    print(i)
    i += 1

print() 

# 3. Program to equal operator and not equal operators
a = 5
b = 10
print(a == b)  # Equal operator
print(a != b)  # Not Equal operator

print() 

# 4. Write a program to print the odd and even numbers
numbers = list(range(1, 11))
print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd Numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")
print()


# 5. Write a program to print largest number among three numbers
a, b, c = 40, 50, 90
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number is:", largest)

print() 

# 6. Write a program to print even number between 10 and 20 using while
i = 10
print("Even numbers between 10 and 20:")
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()


# 7. Write a program to print 1 to 10 using the do-while loop statement
i = 1
print("Numbers from 1 to 10:")
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break
print()

# 8. Write a program to find Armstrong number or not
def is_armstrong_number(number):
    s = str(number)
    n_digits = len(s)
    sum_of_powers = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n_digits
        temp //= 10

    if number == sum_of_powers:
        return True
    else:
        return False

# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print() 

# 9. Write a program to find the prime or not
def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
number = 11
if is_prime_number(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

print() 

# 10. Write a program to palindrome or not
def is_palindrome(data):
    s = str(data).lower()
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False

# Example usage
data = "madam"
if is_palindrome(data):
    print(f"'{data}' is a palindrome.")
else:
    print(f"'{data}' is not a palindrome.")

print() 

# 11. Program to check whether a number is EVEN or ODD using switch
def check_even_odd_switch_simulation(number):
    if number % 2 == 0:
        result = "EVEN"
    else:
        result = "ODD"
    print(f"Using if-else: {number} is {result}.")

# Example usage
check_even_odd_switch_simulation(7)

print() 

# 12. Print gender (Male/Female) program according to given M/F using switch
def print_gender_switch_simulation(gender_char):
    gender_char_upper = gender_char.upper()
    if gender_char_upper == 'M':
        full_gender = "Male"
    elif gender_char_upper == 'F':
        full_gender = "Female"
    else:
        full_gender = "Unknown"
    print(f"The gender for '{gender_char}' is {full_gender}.")

# Example usage
print_gender_switch_simulation('f')


