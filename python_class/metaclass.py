"""
 Metaclasses are a way to control the behavior of class creation. They define how classes behave, 
 just like classes define how objects behave.
"""

# Normal way of defining a class
class Myclass:
    pass

# Equivalent to:
Myclass = type("Myclass", (), {})   #type() dynamically creates a class named MyClass.

# type(name, bases, dict)  or type(object)
"""
name (str) → Name of the new class ("MyClass").
bases (tuple) → The base classes the new class should inherit from.
dict (dict) → A dictionary containing attributes and methods for the class.
"""

class Parent:
    pass

Childclass = type("ChildCLass", (Parent,), {"x":10, "greet": lambda self: "Hello!"})

obj = Childclass()
print(obj.greet())
print(f"x: {obj.x}")


def dynamic_method(self):
    return "I'm dynamic!"

DynamicClass = type("DynamicClass", (), {"say_hello": dynamic_method})

obj = DynamicClass()
print(obj.say_hello())  # Output: I'm dynamic!


"""
Creating a Custom Metaclass
"""

class MyMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class {name}")
        class_dict["new_attr"] = "Added by Metaclass"
        return super().__new__(cls, name, bases, class_dict)
    
    def __init__(cls, name, bases, class_dict):
        print(f"Running __init__ for {name}")
        super().__init__(name, bases, class_dict)

    def __call__(cls, *args, **kwargs):
        print(f"Creating an instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)  # Call default instance creation

class Myclass(metaclass=MyMeta):
    pass


print(f"New attribute: {Myclass.new_attr}")

obj = Myclass()

