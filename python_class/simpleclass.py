class Car:
    #__init__: Constructor initializes the object.
    def  __init__(self, brand, model):     
        self.brand = brand  # Instance varibale
        self.model = model
    
    def display(self):
        print(f"{self.brand}, {self.model}")
    
    def __del__(self):
        print("I am destroyed ....")


# # Creating an instance (object)
car1 = Car("Tata", "Safari")   
car1.display()
del car1



"""
When is __del__ Called?

    When an object goes out of scope.
    When del obj is explicitly used.
    When Python Garbage Collector removes unused objects.

⚠ __del__ is Not Always Reliable

    Python automatically handles memory cleanup.
    If an object has circular references, __del__ might not be called immediately.

✅ Better Alternative?
Use context managers (with statement) for cleanup instead of relying on __del__.


"""