from abc import ABC, abstractmethod

# 1. Abstract class with abstract and non-abstract methods
class Animal(ABC):  # Abstract base class

    def sound(self):  # Non-abstract method
        print("Animals make sounds")

    @abstractmethod
    def type(self):  # Abstract method
        pass

# 2. Subclass for abstract class
class Dog(Animal):

    def type(self):  # Implementing abstract method
        print("Dog: I am a domestic animal")

    def call_non_abstract(self):
        # 4. Call non-abstract method from child class
        self.sound()

    def call_abstract(self):
        # 3. Call abstract method from child class
        self.type()

# Driver code

# Creating object of child class
d = Dog()

# Accessing non-abstract method from abstract class
d.sound()

# Accessing abstract method implemented in child class
d.type()

# Calling abstract and non-abstract methods from within child class
d.call_abstract()
d.call_non_abstract()
