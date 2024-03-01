class Student(object):
    def __init__(self, name):
        self.name = name

    @property
    def fly(self):
        print(self.name, "is flying")


s = Student("Jack")
s.fly
