# 1. Write a function to add integer values of an array
def add_integers(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Driver code
array1 = [1, 2, 3, 4, 5]
print("Sum of array:", add_integers(array1))

# 2. Write a function to calculate the average value of an array of integers
def average_value(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

# Driver code
array2 = [10, 20, 30, 40, 50]
print("Average of array:", average_value(array2))

# 3. Write a program to find the index of an array element
def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

# Driver code
array3 = [5, 10, 15, 20, 25]
value_to_find = 15
print(f"Index of {value_to_find}:", find_index(array3, value_to_find))

# 4. Write a function to test if array contains a specific value
def contains_value(arr, value):
    for num in arr:
        if num == value:
            return True
    return False

# Driver code
array4 = [3, 6, 9, 12, 15]
value_to_test = 9
print(f"Array contains {value_to_test}:", contains_value(array4, value_to_test))

# 5. Write a function to remove a specific element from an array
def remove_element(arr, value):
    new_arr = []
    for num in arr:
        if num != value:
            new_arr.append(num)
    return new_arr

# Driver code
array5 = [7, 14, 21, 28, 35]
value_to_remove = 21
print(f"Array after removing {value_to_remove}:", remove_element(array5, value_to_remove))

# 6. Write a function to copy an array to another array
def copy_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr

# Driver code
array6 = [2, 4, 6, 8, 10]
print("Copied array:", copy_array(array6))

# 7. Write a function to insert an element at a specific position in the array
def insert_element(arr, value, position):
    new_arr = []
    for i in range(len(arr)):
        if i == position:
            new_arr.append(value)
        new_arr.append(arr[i])
    if position >= len(arr):
        new_arr.append(value)
    return new_arr

# Driver code
array7 = [1, 3, 5, 7, 9]
value_to_insert = 4
position_to_insert = 2
print(f"Array after inserting {value_to_insert} at position {position_to_insert}:", insert_element(array7, value_to_insert, position_to_insert))

# 8. Write a function to find the minimum and maximum value of an array
def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

# Driver code
array8 = [11, 22, 33, 44, 55]
min_val, max_val = find_min_max(array8)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")

# 9. Write a function to reverse an array of integer values
def reverse_array(arr):
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append(arr[i])
    return new_arr

# Driver code
array9 = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(array9))

# 10. Write a function to find the duplicate values of an array
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Driver code
array10 = [1, 2, 3, 2, 4, 5, 1]
print("Duplicate values:", find_duplicates(array10))

# 11. Write a program to find the common values between two arrays
def find_common_values(arr1, arr2):
    common_values = []
    for num in arr1:
        if num in arr2 and num not in common_values:
            common_values.append(num)
    return common_values

# Driver code
array11_1 = [1, 2, 3, 4, 5]
array11_2 = [4, 5, 6, 7, 8]
print("Common values:", find_common_values(array11_1, array11_2))

# 12. Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr

# Driver code
array12 = [1, 2, 3, 2, 4, 5, 1]
print("Array after removing duplicates:", remove_duplicates(array12))

# 13. Write a method to find the second largest number in an array
def find_second_largest(arr):
    largest = arr[0]
    second_largest = None
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest

# Driver code
array13 = [10, 20, 30, 40, 50]
print("Second largest number:", find_second_largest(array13))

# 14. Write a method to find the second smallest number in an array
def find_second_smallest(arr):
    smallest = arr[0]
    second_smallest = None
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest

# Driver code
array14 = [10, 20, 30, 40, 50]
print("Second smallest number:", find_second_smallest(array14))

# 15. Write a method to find number of even number and odd numbers in an array
def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Driver code
array15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(array15)
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")

# 16. Write a function to get the difference of largest and smallest value
def difference_largest_smallest(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

# Driver code
array16 = [10, 20, 30, 40, 50]
print("Difference between largest and smallest value:", difference_largest_smallest(array16))

# 17. Write a method to verify if the array contains two specified elements (12, 23)
def contains_two_elements(arr, elem1, elem2):
    found_elem1 = False
    found_elem2 = False
    for num in arr:
        if num == elem1:
            found_elem1 = True
        if num == elem2:
            found_elem2 = True
    return found_elem1 and found_elem2

# Driver code
array17 = [10, 12, 14, 16, 18, 23]
print("Array contains 12 and 23:", contains_two_elements(array17, 12, 23))

# 18. Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr

# Driver code
array18 = [1, 2, 3, 2, 4, 5, 1]
print("Array after removing duplicates:", remove_duplicates(array18))

