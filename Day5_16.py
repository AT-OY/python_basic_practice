class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100  # 私有变量

    def get_life_val(self):
        print("生命值还有：" + str(self.__life_val))
        return self.__life_val

    def got_attack(self):
        self.__life_val -= 20
        print("被击中了，生命值减20")
        return self.__life_val


a = Person("Alex", 22)
a.get_life_val()
a.got_attack()
a.get_life_val()