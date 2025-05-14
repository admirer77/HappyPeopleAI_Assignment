# Superclass A
class A:
    def method1(self):
        print("Method1 in class A")

    def method2(self):
        print("Method2 in class A")

    def show(self):
        print("Show in class A")

# Subclass B inherits A
class B(A):
    def method3(self):
        print("Method3 in class B")

    def method4(self):
        print("Method4 in class B")

    def show(self):
        print("Show in class B")

# Subclass C inherits B
class C(B):
    def method5(self):
        print("Method5 in class C")

    def method6(self):
        print("Method6 in class C")

    def show(self):
        print("Show in class C")

# Main class to test
class Main:
    # Main method
    def run(self):
        
        a = A()
        a.method1()
        a.method2()
        a.show()

        print()

        b = B()
        b.method1()
        b.method2()
        b.method3()
        b.method4()
        b.show()

        print()

        c = C()
        c.method1()
        c.method2()
        c.method3()
        c.method4()
        c.method5()
        c.method6()
        c.show()

        print()

        a_ref = B()
        a_ref.show()  # Calls B's show()

        a_ref = C()
        a_ref.show()  # Calls C's show()

        print()

        
        class A2:
            x = "Data in A"

        class B2(A2):
            x = "Data in B"

        class C2(B2):
            x = "Data in C"

        a2 = A2()
        b2 = B2()
        c2 = C2()

        print(a2.x)  # Data in A
        print(b2.x)  # Data in B
        print(c2.x)  # Data in C

        # Superclass reference
        ref = B2()
        print(ref.x)  # Data in B

        ref = C2()
        print(ref.x)  # Data in C

# Run the main method
main = Main()
main.run()
