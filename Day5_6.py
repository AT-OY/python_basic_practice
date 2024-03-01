class Dog:
    d_type = "京巴"  # 属性，类属性，类变量
    sss = "sss"  # 属性，类属性，类变量

    def sayhi(self):  # 方法，第一个参数必须是self，self代表实例本身
        print("Hello, I am a dog, my type is ", self.d_type)


d = Dog()  # 生成了一个实例
d2 = Dog()  # 生成了一个实例

d.sayhi()  # 实例.方法
d2.sayhi()

print(d.d_type, d.sss)  # 实例.属性
