# Question 1: Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    "S101": "Amit",
    "S102": "Priya",
    "S103": "Rahul",
    "S104": "Sneha",
    "S105": "Vikram"
}
print("Initial Dictionary:", students)

# Question 1.1: Adding values in dictionary
students["S106"] = "Neha"
print("\nAfter Adding S106:", students)

# Question 1.2: Updating values in dictionary
students["S103"] = "Rohan"
print("\nAfter Updating S103:", students)

# Question 1.3: Accessing the value in dictionary
print("\nAccessing S104:", students["S104"])

# Question 1.4: Create a nested loop dictionary
nested_students = {
    "S101": {"name": "Amit", "age": 20, "grade": "A"},
    "S102": {"name": "Priya", "age": 21, "grade": "B"},
    "S103": {"name": "Rohan", "age": 22, "grade": "A"},
}
print("\nNested Dictionary:", nested_students)

# Question 1.5: Access the values of nested loop dictionary
print("\nAccessing S102's Grade:", nested_students["S102"]["grade"])

# Question 1.6: Print the keys present in a particular dictionary
print("\nKeys in students dictionary:", students.keys())

# Question 1.7: Delete a value from a dictionary
del students["S105"]
print("\nAfter Deleting S105:", students)
