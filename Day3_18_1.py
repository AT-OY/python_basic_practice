account = {
    "is_authenticated": False,
    "username": "D",
    "password": "123"
}


def login():
    if account["is_authenticated"] is False:
        username = input("User:")
        password = input("Password:")
        if username == account["username"] and password == account["password"]:
            print("welcome login...")
            account["is_authenticated"] = True
        else:
            print("Wrong username or password!")
    else:
        print("用户已登录，验证通过...")


def home():
    print("HOME".center(10, "-"))


def america():
    login()
    print("US".center(10, "-"))


def japan():
    print("JP".center(10, "-"))


def china():
    login()
    print("CN".center(10, "-"))


home()
america()
china()
