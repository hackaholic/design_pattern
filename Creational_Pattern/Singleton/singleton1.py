class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, *kwargs)
        return cls._instance

# class Singleton(object):  # Explicitly inheriting from `object`
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super().__new__(cls, *args, *kwargs)
#         return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(f"obj1 == obj2: {obj1 == obj2}")
print(f"obj1 id: {id(obj1)}")
print(f"obj2 id: {id(obj2)}")