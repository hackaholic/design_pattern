from abc import ABC, abstractmethod

# Step 1: Define Delivery Method (Implementation)
class DeliveryMethod:
    @abstractmethod
    def deliver(self, order):
        pass

# Concrete Delivery Implementations
class BikeDelivery:
    def deliver(self, order) -> str:
        return f"Delivering {order} by bike"
    
class CarDelivery:
    def deliver(self, order) -> str:
        return f"Delivering {order} by Car"

class DronDelivery:
    def deliver(self, order) -> str:
        return f"Delivering {order} by drone"

# Delivery Service (Handles Delivery Separately)
class DeliveryService:
    def __init__(self , delivery_method):
        self.delivery_method = delivery_method
    
    def deliver(self, order):
        return self.delivery_method.deliver(order)

# Restaurant (Only Prepares Food)
class Restaurant:
    def __init__(self, name):
        self.name = name
    
    def prepare_food(self, food_name):
        return f"{self.name} prepared {food_name}"


pizza_hut = Restaurant("Pizza Hut")
bike_delivery_service = DeliveryService(BikeDelivery())

food = pizza_hut.prepare_food("Margarita Pizza")
print(food)

print(bike_delivery_service.deliver("Margarita Pizza"))