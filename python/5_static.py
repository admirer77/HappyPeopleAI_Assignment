# 1. Define a static variable and access that through a class
class Example1:
    static_var = "Accessed via class"

print("1. Accessing static variable through class:")
print(Example1.static_var)  # Output: Accessed via class

print()

# 2. Define a static variable and access that through an instance
class Example2:
    static_var = "Accessed via instance"

instance2 = Example2()
print("2. Accessing static variable through instance:")
print(instance2.static_var)  # Output: Accessed via instance

print()

# 3. Define a static variable and change within the instance
class Example3:
    static_var = "Original value"

instance3 = Example3()
instance3.static_var = "Changed via instance"  # This creates an instance variable, doesn't change class variable

print("3. Changing static variable via instance:")
print("Instance variable:", instance3.static_var)  # Output: Changed via instance
print("Class variable remains:", Example3.static_var)  # Output: Original value

print()

# 4. Define a static variable and change within the class
class Example4:
    static_var = "Initial value"

# Changing the static variable directly through the class
Example4.static_var = "Changed via class"

print("4. Changing static variable via class:")
print("Class variable:", Example4.static_var)  # Output: Changed via class

# Also check through an instance
instance4 = Example4()
print("Access through instance:", instance4.static_var)  # Output: Changed via class
