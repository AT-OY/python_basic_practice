class ShenXianBase:
    def fight(self):
        print("神仙始祖们在天地边界打架")


class ShenXian(ShenXianBase ):
    def fly(self):
        print("神仙都会飞...")

    def fight(self):
        print("神仙在打架")


class Monkeybase:
    def fight(self):
        print("猿猴在打架")


class Monkey(Monkeybase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    # def fight(self):
    #     print("猴子在打架")


class MonkeyKing(Monkey, ShenXian):
    def play_golden_stick(self):
        print("孙悟空玩金箍棒...")


m = MonkeyKing()
m.play_golden_stick()
m.fly()
m.play_golden_stick()
m.fight()