class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("%s is eating..." % self.name)


class Person(Animal):
    a_type = "哺乳高等动物"

    def talk(self):
        print("Person %s is talking..." % self.name)

    def eat(self):
        print("人在优雅的吃...")


class Dog(Animal):
    def chase_rabbit(self):
        print("Dog %s is chasing rabbit..." % self.name)


p = Person("Alex", 22, "M")
p.eat()
p.talk()
print(p.a_type)

d = Dog("Mjj", 3, "F")
d.eat()
d.chase_rabbit()
print(d.a_type)
