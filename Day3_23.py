def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        # print(a)
        yield a  # 暂停
        temp = a  # 给新的a赋值前先把旧的值存下来
        a = b
        b = temp + b
        count += 1


f = fib(20)
print(next(f))
print(list(f))
print(f)
