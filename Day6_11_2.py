class Printer(object):
    tasks = []
    instance = None  # 存放第一个实例对象

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 只有第一次实例化时正常进行，后面每次实例化并不真正创建一个新实例
        if cls.instance is None:
            # 进行正常实例化，并把实例化后的对象存在cls.instance里
            obj = object.__new__(cls)  # 实例化过程
            print("Obj:", obj)
            cls.instance = obj
        return cls.instance  # 以后的每次实例化， 直接返回第一次存的对象
        # 在上一次对象的基础上，再执行__init__, 只保留最后的__init__

    def add_task(self, job):
        self.tasks.append(job)
        print("[%s]添加任务[%s]到打印机，总任务%s" % (self.name, job, self.tasks))


p1 = Printer("Word APP")
p2 = Printer("pdf APP")
p3 = Printer("excel APP")

p1.add_task("word")
p2.add_task("pdf")
p3.add_task("excel")

print(p1)
print(p2)
print(p3)