# 1. PRIVATE fields and methods

class PrivateExample:
    def __init__(self):
        self.__private_field1 = "Private Field 1"
        self.__private_field2 = "Private Field 2"

    def __private_method(self):
        print("Private Method Called")

    def main(self):
        print(self.__private_field1)
        print(self.__private_field2)
        self.__private_method()

# Subclass trying to access private members
class SubPrivate(PrivateExample):
    def access_private(self):
        # The following lines will raise AttributeError if uncommented
        # print(self.__private_field1)
        # self.__private_method()
        print("Cannot access private members directly from subclass")

p = PrivateExample()
p.main()

sp = SubPrivate()
sp.access_private()

print()

# 2. PROTECTED fields and methods

class ProtectedExample:
    def __init__(self):
        self._protected_field1 = "Protected Field 1"
        self._protected_field2 = "Protected Field 2"

    def _protected_method(self):
        print("Protected Method Called")

# Same package access
class SamePackageAccess:
    def access(self):
        obj = ProtectedExample()
        print(obj._protected_field1)
        print(obj._protected_field2)
        obj._protected_method()

# Different package simulation (Python doesn't enforce packages like Java)
class SubProtected(ProtectedExample):
    def access(self):
        print(self._protected_field1)
        print(self._protected_field2)
        self._protected_method()

spa = SamePackageAccess()
spa.access()

dp = SubProtected()
dp.access()

print()

# 3. PUBLIC fields and methods

class PublicExample:
    def __init__(self):
        self.public_field1 = "Public Field 1"
        self.public_field2 = "Public Field 2"

    def public_method(self):
        print("Public Method Called")

# Access from same or different class
class AccessPublic:
    def access(self):
        obj = PublicExample()
        print(obj.public_field1)
        print(obj.public_field2)
        obj.public_method()

ap = AccessPublic()
ap.access()
