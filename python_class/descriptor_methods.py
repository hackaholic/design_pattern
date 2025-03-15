"""
The term "descriptor" in Python refers to objects that define how attributes are accessed and manipulated

Attribute Access and Descriptor Methods

__getattr__(self, name), __setattr__(self, name, value), and __delattr__(self, name): Customize attribute access.
__getattribute__(self, name): Called unconditionally to implement attribute access.
__get__(self, instance, owner), __set__(self, instance, value), __delete__(self, instance): Implement descriptor protocol.

"""

class ProtectedAttributes:
    def __init__(self):
        self._protected = "This is Protected"
    
    def __getattr__(self, name):
        if name == "secret":
            raise AttributeError("Access denied")
        return self.__dict__.get(name, f"{name} not found")
    
    def __setattr__(self, name, value):
        if name == "secret":
            raise AttributeError("Cannot Modity Secret")
        self.__dict__[name] = value
    
    def __delattr__(self, name):
        if name == "secret":
            raise AttributeError("Cannot delete secret")
        del self.__dict__[name]

proc1 = ProtectedAttributes()
print(proc1._protected)
print(proc1.name)


class Demo:
    def __init__(self):
        self.existing = "I exist"

    def __getattribute__(self, attr):
        print(f"Intercepting {attr}")  # Runs for all attributes
        return super().__getattribute__(attr)

    def __getattr__(self, attr):
        return f"{attr} not found (fallback)"  # Runs only if attribute is missing

obj = Demo()
print(obj.existing)  # 🔍 "Intercepting existing" -> "I exist"
print(obj.missing)   # 🔍 "Intercepting missing" -> ❌ Calls __getattr__ -> "missing not found"


"""
When you access obj.missing, both __getattribute__ and __getattr__ are called, but in sequence:

    __getattribute__ is always called first for every attribute access.
        It prints "Intercepting missing".
        It then tries to retrieve self.missing using super().__getattribute__("missing").

    Since missing does not exist, super().__getattribute__("missing") raises an AttributeError.
        Python then automatically calls __getattr__("missing") as a fallback.
        __getattr__ returns "missing not found (fallback)".
"""