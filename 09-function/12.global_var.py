def fun():
    a = 10  # 지역변수
    print(a, " / ", globals()["a"])


def fun1():
    print(a)


def fun2():
    global a
    a = 0
    print(a)


def fun3():
    print(a)


def fun4(r):
    global x
    x = 3.14 * r**2
    return x


a = 20  # 전역변수, 함수 호출 전에 선언 필요
fun()
fun1()
fun2()
fun3()
print(fun4(5))
print(x)