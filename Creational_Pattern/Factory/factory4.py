from abc import ABC, abstractmethod

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
