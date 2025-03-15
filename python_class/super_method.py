""""
1. Basic Concept of super()

The primary use of super() is to call methods from the parent class (also known as the base class) within the child class (also called the subclass).
Syntax:

super().method_name()

2. Why Use super()?

super() is useful in the following cases:

    Calling parent class methods in the child class to avoid code duplication.
    Method overriding: when you override a method in the subclass, but still want to invoke the parent class method.

3. super() with Arguments

You can pass arguments to super() if you need to specify which class to start the method lookup from. This is especially useful in more complex inheritance chains.
Syntax:

super(current_class, instance).method_name()

    current_class: The class where the method call is happening.
    instance: The instance of the class (typically self).
"""

class Parent:
    def greet(self):
        print("Greeting from Parent")

class Child(Parent):
    def greet(self):
        super().greet()    # When we use super(), it's typically used without arguments inside a class method. In that case, Python automatically determines the current class and instance
        print("Geting from Child")

obj = Child()
obj.greet()



class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super(B, self)