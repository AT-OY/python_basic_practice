account = {
    "is_authenticated": False,
    "username": "D",
    "password": "123"
}


def login(func):
    def inner():
        if account["is_authenticated"] is False:
            username = input("User:")
            password = input("Password:")
            if username == account["username"] and password == account["password"]:
                print("welcome login...")
                account["is_authenticated"] = True
                func()  # 认证成功，执行功能函数
            else:
                print("Wrong username or password!")
        else:
            print("用户已登录，验证通过...")
            func()  # 认证成功，执行功能函数

    return inner


def home():
    print("HOME".center(10, "-"))


@login
def america():
    print("US".center(10, "-"))


def japan():
    print("JP".center(10, "-"))


@login
def china():
    print("CN".center(10, "-"))


# america = login(america)  # inner的内存地址
# china = login(china)

print(america)
print(china)

home()
america()  # inner()
china()
