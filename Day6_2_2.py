class Student(object):
    __stu_num = 0

    def __init__(self, name):
        self.name = name
        # Student.stu_num += 1
        # print("生成了一个新学生", name, self.stu_num)
        self.add_stu(self)

    @classmethod
    def add_stu(cls, obj):
        if obj.name:
            cls.__stu_num += 1
            print("生成了一个新学生", cls.__stu_num)


s1 = Student("Mjj")
s2 = Student("Jack")
s3 = Student("Alex")

Student.add_stu()
