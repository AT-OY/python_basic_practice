class User(object):

    @staticmethod
    def login():
        print("欢迎来到登录页面")

    @staticmethod
    def register():
        print("欢迎来到注册页面")

    @staticmethod
    def save():
        print("欢迎来到存储页面")


u = User()
while True:
    user_cmd = input(">>:").strip()
    if hasattr(u, user_cmd):
        func = getattr(u, user_cmd)
        func()
