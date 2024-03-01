class Dog(object):
    name = "stupid dog"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(cls):
        print(cls)
        print("Dog %s is eating..." % cls.name)


d = Dog("Mjj")
d.eat()
