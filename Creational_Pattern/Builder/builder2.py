# Step 1: Define the Complex Object
class Car:
    def __init__(self, brand, engine, airbags):
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
        self.airbags = 0  # Default value

    def set_brand(self, brand):
        self.brand = brand
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_airbags(self, airbags):
        self.airbags = airbags
        return self

    def build(self):
        return Car(self.brand, self.engine, self.airbags)

# Step 3: Create a Director Class
class CarDirector:
    """Defines predefined car models using the builder."""
    
    @staticmethod
    def build_sports_car():
        return CarBuilder().set_brand("Ferrari").set_engine("V8 Turbo").set_airbags(2).build()

    @staticmethod
    def build_suv():
        return CarBuilder().set_brand("Toyota").set_engine("Hybrid").set_airbags(6).build()

# Step 4: Client Uses the Director
if __name__ == "__main__":
    sports_car = CarDirector.build_sports_car()
    suv = CarDirector.build_suv()

    print(sports_car)  # Output: Car(Brand: Ferrari, Engine: V8 Turbo, Airbags: 2)
    print(suv)         # Output: Car(Brand: Toyota, Engine: Hybrid, Airbags: 6)
