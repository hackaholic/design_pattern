class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknow animal type")

animal1 = AnimalFactory.get_animal("Dog")
print(animal1.speak())

animal2 = AnimalFactory.get_animal("Cat")
print(animal2.speak())