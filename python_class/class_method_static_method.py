class MathOperations:
    class_var = 10

    @classmethod    # @classmethod modifies class-level data.
    def class_method(cls) -> int:
        return cls.class_var

    @staticmethod  #@staticmethod is independent of instance/class.
    def static_method(x: int, y: int) -> int:
        return x + y


print(f"MathOperations.class_var: {MathOperations.class_var}")
print(f"MathOperations.static_method(2, 3): {MathOperations.static_method(2, 3)}")

"""
cls in class methods is a reference to the class (not an instance), and you can use it to access or modify class-level attributes and methods.

Class Method (class_method):

    The method is marked with @classmethod, which means it's bound to the class, not the instance.
    The first parameter is cls, which refers to the class MathOperations.
    cls.class_var accesses the class variable class_var.

Static Method (static_method):

    The method is marked with @staticmethod, so it doesn't receive the cls or self parameter.
    It behaves like a regular function but is scoped inside the class.

"""




"""
Why use class methods if class variables are accessible directly?

    Encapsulation and Abstraction:
        Class methods provide an additional layer of abstraction and encapsulation. Instead of directly modifying class variables, you can wrap that logic in a method that performs checks, validation, or additional logic.

    Control over class-level operations:
        You might want to control how the class variable is accessed or modified. For example, you may want to log every time a class variable changes, or restrict the modification to certain conditions.

    Inheritance and Polymorphism:
        When using inheritance, a class method can be called on the derived class, and it will still refer to the derived class (thanks to the cls parameter). This is polymorphism in action.
        If you change the class variable directly, you may lose the ability to take advantage of this polymorphic behavior.

Even though class methods can provide validation and encapsulation, the class variable can still be modified directly from outside the class, potentially leading to buggy or inconsistent behavior.

Explore: property() function to achieve getters and setters behaviour
"""
