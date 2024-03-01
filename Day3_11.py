def calc(x):
    return x**2


res = map(calc, [1, 5, 7, 4, 8])
print(list(res))

res = map(lambda x: x**2 if x > 5 else x**3, [1, 5, 7, 4, 8])
print(list(res))
