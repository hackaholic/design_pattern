class Animal:
    def speak(self):
        print("Animal Speaks")

# Overriding happens when a child class redefines a parent class method.
class Cat(Animal):
    def speak(self): # Method overriding
        print("Meow meow!!!")

animal = Animal()
animal.speak()

cat = Cat()
cat.speak()

