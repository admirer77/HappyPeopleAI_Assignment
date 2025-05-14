# 1. Class with a default constructor
class A:
    def __init__(self):
        self.name = "Nehanth"

    def print_A(self):
        print("Class A Name:", self.name)

# Creating object and calling method
obj_a = A()
obj_a.print_A()


# 2. Child class calling its own constructor
class B(A):
    def __init__(self):
        super().__init__()  # Optional: call parent constructor
        self.name = "Gaddam"

    def print_B(self):
        print("Class B Name:", self.name)

obj_b = B()
obj_b.print_B()


# 3. Class with public, protected, and private attributes
class C:
    def __init__(self, name, roll, branch):
        self.name = name          # public
        self._roll = roll         # protected
        self.__branch = branch    # private

    def show_name(self):
        print("Name:", self.name)

    def _show_roll(self):
        print("Roll:", self._roll)

    def __show_branch(self):
        print("Branch:", self.__branch)

    def access_private(self):
        self.__show_branch()


# 4. Child class accessing protected and public members
class D(C):
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)

    def access_protected(self):
        self._show_roll()

# Creating object of child class
obj_d = D("NEHANTH", 7, "CSD")
obj_d.show_name()
obj_d.access_protected()
obj_d.access_private()
