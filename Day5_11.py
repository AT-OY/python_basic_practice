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

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        # self.attack_val = attack_val
        self.life_val = 100
        self.weapon = Weapon(name)  # 直接实例化


class Weapon:
    def __init__(self, user):
        self.user = user
        self.name = None
        self.attack_val = None

    def dog_stick(self, obj):
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        self.name = "屠龙刀"
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        self.name = "AK47"
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("[%s]被[%s]的[%s]攻击了，掉血[%s]，还有血量[%s]..." %
              (obj.name, self.user, self.name, self.attack_val, obj.life_val))


d = Dog("Mjj", "二哈", 30)
p = Person("Alex", "M")

d.bite(p)
p.weapon.gun(d)
