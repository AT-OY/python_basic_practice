class School(object):

    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self. type = type

    def __repr__(self):
        return "School(%s, %s)" % (self.name, self.addr)

    def __str__(self):
        return "(%s, %s)" % (self.name, self.addr)

    def __del__(self):
        print("对象被释放了")


s1 = School("XYQ", "北京", "私立")
print("from repr:", repr(s1))
print("from str:", str(s1))
print(s1)
del s1
print(s1)
