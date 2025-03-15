"""
@property decorator allows you to define getter, setter, and deleter methods while treating them like attributes

Always store the actual value in a different attribute (_name instead of name).
A getter-only property (@property) makes the attribute read-only.
To allow modification, add a setter (@name.setter).
Infinite recursion happens when a property calls itself directly (self.name inside name()).

"""


class Cat:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self): # this will act as getter
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name)<=2:
            raise ValueError("Nmae must be string")   
        self._name = name
    
    @name.deleter
    def name(self):
        print("name delete")
        del self._name

coco = Cat('Coco')
print(f"using coco.name: {coco.name}")
coco.name = "Mini"

print(f"using coco.name: {coco.name}")

del coco.name
coco.name = "hello"
print(f"using coco.name: {coco.name}")