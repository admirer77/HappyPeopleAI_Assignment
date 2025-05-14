# 1. Write two methods with the same name but different number of parameters of same type
class Example1:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two parameters: a = {a}, b = {b}")
        elif a is not None:
            print(f"One parameter: a = {a}")
        else:
            print("No parameters")

# Driver code for Example 1
print("Example 1:")
obj1 = Example1()
obj1.display()
obj1.display(10)
obj1.display(10, 20)


# 2. Write two methods with the same name but different number of parameters of different data type
class Example2:
    def display(self, a=None, b=None):
        if isinstance(a, int) and isinstance(b, int):
            print(f"Two integer parameters: a = {a}, b = {b}")
        elif isinstance(a, str) and isinstance(b, str):
            print(f"Two string parameters: a = {a}, b = {b}")
        elif isinstance(a, int):
            print(f"One integer parameter: a = {a}")
        elif isinstance(a, str):
            print(f"One string parameter: a = {a}")
        else:
            print("No parameters")

# Driver code for Example 2
print("\nExample 2:")
obj2 = Example2()
obj2.display()
obj2.display(10)
obj2.display("Hello")
obj2.display(10, 20)
obj2.display("Hello", "World")


# 3. Write two methods with the same name and same number of parameters of same type
class Example3:
    def display(self, a, b):
        print(f"Parameters: a = {a}, b = {b}")

# Driver code for Example 3
print("\nExample 3:")
obj3 = Example3()
obj3.display(10, 20)
obj3.display("Hello", "World")

