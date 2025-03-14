
#  Python follows C3 Linearization (MRO) to resolve multiple inheritance conflicts.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.show()  # "Class B"

print(D.mro())  # Method Resolution Order (MRO)


# Uncomment to see error, TypeError: Cannot create a consistent method resolution order (MRO) for bases B, C
# class E(D, C, B):  # Multiple Inheritance
#     pass

# obj = E()
# obj.show()  # "Class C"

# print(E.mro())  # Method Resolution Order (MRO)


"""
This means that when you call obj.show(), Python will follow this order:

    Look in D (but D doesn’t have a show() method).
    Look in B (finds show() in B, so it calls B.show()).
    If it didn’t find show() in B, it would continue to look in C and then A, but it found the method in B, so it calls B.show().

"""


