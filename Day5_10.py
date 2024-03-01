class RealtionShip:
    def __init__(self):
        self.couple = []

    def make_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]
        print("[%s]和[%s]确定了关系" % (obj1.name, obj2.name))

    def get_my_partner(self, obj):
        print("找[%s]的对象" % obj.name)
        for i in self.couple:
            if i != obj:
                return i
        else:
            print("你没有对象")

    def break_up(self):
        print("[%s]和[%s]分手了" % (self.couple[0].name, self.couple[0].name))
        self.couple.clear()


class Person:
    def __init__(self, name, age, sex, relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation
        # self.partner = None  # 应该是一个对象，代表另一半

    def do_stuff(self):
        pass


relation_obj = RealtionShip()
p1 = Person("Mjj", 24, "M", relation_obj)
p2 = Person("Lyy", 22, "F", relation_obj)

relation_obj.make_couple(p1, p2)
print(p1.relation.couple)

print(p1.relation.get_my_partner(p1).name)

p1.relation.break_up()
p2.relation.get_my_partner(p2)