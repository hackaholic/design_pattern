class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def display(self):
        print(f"x: {self.x}, y: {self.y}")

v1 = Vector(2, 3)
v2 = Vector(5, 6)
v3 = v1 + v2
v3.display()