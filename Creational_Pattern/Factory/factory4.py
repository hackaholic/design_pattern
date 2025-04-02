import inspect
from abc import ABC, abstractmethod

"""
1️⃣ Abstract Methods Cannot Have an Implementation (Normally)
By default, abstract methods should not have an implementation. However, you can provide a default implementation in the base class if needed.

2️⃣ Abstract Classes Cannot Be Instantiated

"""
class Coffee(ABC):
    @abstractmethod
    def serve(self):
        """Every coffee must implement serve()"""
        pass

class Espresso(Coffee):
    def serve(self):
        return "Espresso ☕"

class Latte(Coffee):
    def serve(self):
        return "Latte ☕🥛"
    
class Cappuccino(Coffee):  # ❌ If we forget serve(), Python will throw an error
    pass  

class CoffeeFactory:
    @staticmethod
    def get_coffee(coffee_type):
        if coffee_type == "espresso":
            return Espresso()
        elif coffee_type == "latte":
            return Latte()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Unknow coffee type")

coffee = CoffeeFactory.get_coffee("latte")
print(coffee.serve())

# coffee1 = CoffeeFactory.get_coffee("cappuccino")
try:
    c = Coffee()  # TypeError: Can't instantiate abstract class Coffee
except TypeError as e:
    print(e)
finally:
    print("Told you  Can't instantiate abstract class Coffee")


# check if a class is abstract Class
assert(inspect.isabstract(Coffee) == True)
print("Yes Coffee is abstract class")