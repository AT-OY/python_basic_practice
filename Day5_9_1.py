class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self, person):
        person.life_val -= self.attack_val
        print("狗[%s]咬了人[%s]一口，人掉血[%s]，还有血量[%s]..." %
              (self.name, person.name, self.attack_val, person.life_val))


class Person:
    role = "person"

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s]一棒，狗掉血[%s]，还有血量[%s]..." %
              (self.name, dog.name, self.attack_val, dog.life_val))


d1 = Dog("Mjj", "二哈", 30)
d2 = Dog("MJM", "金毛", 40)
p1 = Person("Alex", "M", 50)

p1.attack(d1)
d1.bite(p1)
