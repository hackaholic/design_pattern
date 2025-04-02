
from abc import ABC, abstractmethod

# 1️⃣ Abstract Products:
# define the interfaces or abstract classes for both Chair and Sofa.
class Chair(ABC):
    @abstractmethod
    def create(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def create(self):
        pass

# 2️⃣ Concrete Products:
# implement concrete products for each of the variations in both categories

class ModernChair(Chair):
    def create(self):
        return "ModernChair Chair created"

class ClassicalChair(Chair):
    def create(self):
        return "Classical Chair created"

class ClassicalSofa(Sofa):
    def create(self):
        return "Classical Sofa created"

class ModernSofa(Sofa):
    def create(self):
        return "Modern Sofa created"

# 3️⃣ Abstract Factory:
# create an abstract factory that defines methods for creating both Chair and Sofa.

class FurnitureFactory:
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

# 4️⃣ Concrete Factories:
# implement concrete factories for each theme
class ModernFurniture(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    
    def create_sofa(self):
        return ModernSofa()

class ClassicFurniture(FurnitureFactory):
    def create_chair(self):
        return ClassicalChair()
    
    def create_sofa(self):
        return ClassicalSofa()


def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.create())
    print(sofa.create())


modern_factory = ModernFurniture()
claassic_factory = ClassicFurniture()

create_furniture(modern_factory)
create_furniture(claassic_factory)

"""
Solid Principle:
Abstract Factory → Dependency Inversion Principle (DIP)
✅ Clients depend on abstract interfaces rather than concrete classes, reducing coupling.
"""

