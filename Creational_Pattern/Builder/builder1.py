# Step 1: Define the Complex Object (Product)
class Car:
    def __init__(self, brand="Unknown", engine="Petrol", airbags=0):
        self.brand = brand
        self.engine = engine
        self.airbags = airbags
    

    def __str__(self):
        return f"Car(Brand: {self.brand}, Engine: {self.engine}, Airbags: {self.airbags})"

# Step 2: Create the Builder Class
class CarBuilder:
    def __init__(self):
        self.brand = None
        self.engine = None
        self.airbags = None    # Keep it None to detect missing values
    
    def set_brand(self, brand):
        self.brand = brand
        return self             # Returning self allows method chaining
    
    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_airbags(self, airbags):
        self.airbags = airbags
        return self

    def build(self):
        """Fills missing fields with default values"""
        return Car(
            brand=self.brand if self.brand is not None else "Unknown",
            engine=self.engine if self.engine is not None else "Petrol",
            airbags=self.airbags if self.airbags is not None else 0
        )

car1 = CarBuilder().set_brand("Tesla").build()
print(car1)

car2 = CarBuilder().set_brand("BMW").set_engine("Diesel").build()
print(car2)