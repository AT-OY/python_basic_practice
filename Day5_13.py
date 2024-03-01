class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("父类构造方法".center(20, "-"))

    def eat(self):
        print("%s is eating..." % self.name)


class Person(Animal):
    a_type = "哺乳高等动物"

    def __init__(self, name, age, sex, hobby):
        # Animal.__init__(self, name, age, sex)
        # super(Person, self).__init__(name, age, sex)
        super().__init__(name, age, sex)
        self.hobby = hobby
        print("子类构造方法".center(20, "-"))

    def talk(self):
        print("Person %s is talking..." % self.name)

    def eat(self):
        # Animal.eat(self)
        super().eat()
        print("人在优雅的吃...")


class Dog(Animal):
    def chase_rabbit(self):
        print("Dog %s is chasing rabbit..." % self.name)


p = Person("Alex", 22, "M", "女")
p.eat()
p.talk()
print(p.a_type)

d = Dog("Mjj", 3, "F")
d.eat()
d.chase_rabbit()
print(d.a_type)
