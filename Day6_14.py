while True:
    try:
        num1 = int(input("num1:"))
        num2 = int(input("num2:"))
        res = num1 + num2
        print(res)
        print(res, name)

    except NameError as err:
        print(err)
    except ValueError as err:
        print("输入的值不合法，必须是数字")
    # except Exception as err:
    #     print("出现异常，信息如下：")
    #     print(err)
