def fun1(a, b):
    s = 0
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        s += i
    return s


def star1(a):
    for i in range(a):
        for j in range(i + 1):
            print("*", end="")
        print()


def star2(a):
    for i in range(a):
        print(("*" * (2 * i + 1)).center(2 * a - 1))


print(fun1(10, 2))
star1(10)
star2(10)