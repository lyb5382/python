def fun(a, b, c):
    print(a, b, c)

def fun1(a, b, c='c'): # default 값이 있으면 반드시 뒤에 위치
    print(a, b, c)

fun("a", "b", "c")

fun1(b="a", a="b")