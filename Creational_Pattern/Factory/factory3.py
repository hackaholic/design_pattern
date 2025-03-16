# Instead of functions, we make the factory itself callable.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def __init__(self):
        self._animal = {}
    
    def __call__(self, animla_type):
        if animla_type in self._animal:
            return self._animal[animla_type]()
        raise ValueError("Unknown Animal type")

    def register_animal(self, animal_type, animal_class):
        self._animal[animal_type] = animal_class

factory = AnimalFactory()

factory.register_animal("cat", Cat)
factory.register_animal("dog", Dog)

cat = factory("cat")
dog = factory("dog")

print(cat.speak())
print(dog.speak())

            