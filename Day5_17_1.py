class Dog(object):
    def sound(self):
        print("汪汪汪...")


class Cat(object):
    def sound(self):
        print("喵喵喵...")


def make_sound(animal_obj):
    # 统一调用接口
    animal_obj.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)