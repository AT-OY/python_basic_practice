import sys

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, "is walking")


p = Person("Alex", 22)
if hasattr(p, "name"):
    print("L...")


mod = sys.modules[__name__]
print(hasattr(mod, "p"))
