class MathOperations:
    class_var = 10

    """
    cls is just a convention—you can use any name you like for that first parameter. However, 
    cls is the widely accepted convention in Python for referring to the class in class methods, 
    similar to how self is the convention for referring to the instance in instance methods.
    """
    @classmethod    # @classmethod modifies class-level data.
    def class_method(cls) -> int:   
        return cls.class_var

    @staticmethod  #@staticmethod is independent of instance/class.
    def static_method(x: int, y: int) -> int:
        return x + y


print(f"MathOperations.class_var: {MathOperations.class_var}")
print(f"MathOperations.static_method(2, 3): {MathOperations.static_method(2, 3)}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    """
    # @staticmethod is fixed to Circle, @classmethod is dynamic:
    @staticmethod
    def from_diameter(diameter):              
        return Circle(diameter / 2)

    
    class Sphere(Circle):
        pass


    s = Sphere.from_diameter(10)
    print(type(s))  # Output: <class '__main__.Circle'> (not Sphere!)
    Even though from_diameter is called on Sphere, it still creates a Circle instance.
    """


c1 = Circle(10)  # Normal constructor
c2 = Circle.from_diameter(20)  # Using class method as an alternate constructor

print(f"c1 radius: {c1.radius}")  
print(f"c2 radius (from diameter): {c2.radius}")  



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
