class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"


# Instead of if-else, we use a dictionary to store classes.

class AnimalFactory:
    _animals = {}

    @classmethod
    def register_animal(cls, animal_type, animal_class):
        cls._animals[animal_type] = animal_class 

    @classmethod
    def get_animal(cls, animal_type):
        if animal_type in cls._animals:
            return cls._animals[animal_type]()
        else:
            raise ValueError("Unknow animal type")

AnimalFactory.register_animal("dog", Dog)
AnimalFactory.register_animal("cat", Cat)

dog = AnimalFactory.get_animal("dog")
cat = AnimalFactory.get_animal("cat")

print(dog.speak())
print(cat.speak())

"""
✅ More scalable
✅ No need to modify existing code for new animals
"""