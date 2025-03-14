class Example:
    class_var = "I am a class variable" #Class variables are shared among all instances

    def  __init__(self, val):
        self.instance_val = val   # Instance variable , Instance variables are unique to each object.

ob1 = Example(10) # Instance 1
ob2 = Example(20) # Instance 2

print(f"ob1: {ob1.instance_val}")
print(f"ob2: {ob2.instance_val}")

print(f"Example.class_var: {Example.class_var}")
print(f"ob1.class_var: {ob1.class_var}")
Example.class_var = "I am modified"
print(f"ob2.class_var: {ob2.class_var}")  # modified for ob2


ob1.class_var = "Modified for ob1"  # only get modified ofr ob1 not for ob2 or Example class
print(f"ob1.class_var: {ob1.class_var}")
print(f"ob2.class_var: {ob2.class_var}")
print(f"Example.class_var: {Example.class_var}")

