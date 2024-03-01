class Dog:
    d_type = "京巴"  # 属性，类属性，类变量
    sss = "sss"  # 属性，类属性，类变量

    def __init__(self, name, age):  # 初始化方法，构造方法，构造函数，实例化是会自动执行，进行一些初始化工作
        print("hahaha", name, age)
        # 要想把name，age这2个值真正存到实例里，就要把这2个值跟实例绑定
        self.name = name  # 绑定参数值到实例
        self.age = age

    def sayhi(self):  # 方法，第一个参数必须是self，self代表实例本身
        print("Hello, I am a dog, my type is", self.d_type, self.name)


d = Dog("mjj", 3)  # 生成了一个实例
d2 = Dog("毛蛋", 2)  # 生成了一个实例

d.sayhi()  # 实例.方法
d2.sayhi()

d.sex = "M"
print(d.sex)

print(d.d_type, d.sss)  # 实例.属性
