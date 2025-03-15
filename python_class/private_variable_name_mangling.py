"""
Private Variables in Python

In Python, there is no true "private" variable like in languages such as C++ or Java. However, 
Python provides mechanisms to indicate that a variable should be treated as private (by convention), 
and it allows you to define how variables should be accessed and modified.
1. By Convention: Single Leading Underscore (_)

    The single leading underscore (_) is a convention used to indicate that a variable is intended for internal use by the class or module. 
    It is not enforced by Python, and external code can still access it.

    Here, _private_var is intended to be private, but Python doesn't enforce this. It's simply a signal to other developers that the variable is meant for internal use only.

2. Strongly Indicating Private: Double Leading Underscore (__)

    When a variable has double leading underscores (e.g., __private_var), Python performs name mangling to "hide" the variable in a way that makes it less likely to be accidentally accessed from outside the class.

Name Mangling

Name mangling is a mechanism Python uses when variables are prefixed with double underscores (__) in class definitions. Python changes the name of the variable in a way that makes it difficult (but not impossible) to accidentally overwrite or access it from outside the class.
How Name Mangling Works:

When you declare a variable like __private_var in a class, Python "mangles" the name by adding the class name as a prefix to the variable name.
"""

class Myclass:
    def __init__(self):
        self._private_var = 42 # single _ Convention for internal use

obj = Myclass()
print(f"obj._private_val: {obj._private_var}")    ## It's allowed, but shouldn't be accessed outside the class


class Myclass:
    __private_var = 29

    def __private_method(self):
        print(" I am Private Method")    # # Can only be called using name mangling or internally

try:
    obj = Myclass()
    print(obj.__private_var)
except Exception as e:
    print(e)

print("Using Name Mangling")
print(f"obj._Myclass__private_var: {obj._Myclass__private_var}")