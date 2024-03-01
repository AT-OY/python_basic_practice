def g_test():
    while True:
        n = yield  # 收到的值赋给n
        print("Receive from outside:", n)


g = g_test()
next(g)  # 调用生成器，同时发送None到yield

for i in range(10):
    g.send(i)
