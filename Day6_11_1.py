class Student(object):

    def __init__(self, name):
        self.name = name
        print("init complete")

    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return object.__new__(cls)


p = Student("Alex")
