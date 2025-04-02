class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)   # invoking object.__new__(cls)
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


"""
Solid Principles
Singleton → Violates SRP, OCP, and DIP
⚠️ Singleton is often considered an anti-pattern because it introduces global state, which can lead to hidden dependencies and tight coupling.
❌ Violates SRP because it controls both its logic and its lifecycle (instantiation management).
❌ Violates OCP since modifying the Singleton’s creation logic can break its global instance.
❌ Violates DIP because it enforces direct dependency on a concrete class instead of using abstractions.
"""