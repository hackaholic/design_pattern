import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)  # create the deep copy of the object


class Coffee(Prototype):
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type
        self.size = size

    def __str__(self):
        return f"{self.size} {self.coffee_type} ☕"

cof1 = Coffee("Lattee", "Regular")

cof2 = cof1.clone()

cof2.size = "Medium"

print(cof1)
print(cof2)

"""
Prototype Pattern and SOLID Principles
Single Responsibility Principle (SRP)	✅ The cloning logic is separated from the object's business logic.
Open-Closed Principle (OCP)	            ✅ Extending the class does not require modifying existing code.
Liskov Substitution Principle (LSP)	    ✅ Cloned objects should behave the same as originals, ensuring LSP compliance.
Interface Segregation Principle (ISP)	✅ No unnecessary methods are forced on subclasses.
Dependency Inversion Principle (DIP)	✅ Cloning works with abstractions rather than direct dependencies."
"""