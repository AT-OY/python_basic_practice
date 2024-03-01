level = "L0"
n = 22


def func():
    level = "L1"
    n = 33
    print(locals())

    def outer():
        level = "L2"
        n = 44
        print("outer:", locals(), n)

        def inner():
            level = "L3"
            print("inner:", locals(), n)

        inner()
    outer()


func()
