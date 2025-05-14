# 1.1. Create a class with a constructor and a method
class ClassOne:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from ClassOne, {self.name}!"
