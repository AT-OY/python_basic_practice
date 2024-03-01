class School(object):

    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)


s = School("Apeland", "Beijing", "Master")
s(123)
