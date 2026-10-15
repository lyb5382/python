# 가변 위치 인자(*args) : 매개변수 개수가 정해져있지 않을 때 사용, 튜플로 전달


def fun(*args):
    print(type(args), args)
    s = 0
    for i in args:
        s += i
    return s


# 매개변수가 여러개일 경우(가변위치인자는 맨 뒤에)
def ffun(a, *args):
    if a == "+":
        r = 0
        for i in args:
            r += i
    if a == "-":
        r = 0
        for i in args:
            r -= i
    return r


print(fun(1, 2, 3, 4, 5, 6))
print(fun())
print(ffun("+", 1, 2, 3, 4, 5, 6))


def ffuun(a, *args, b):
    print(a, args, b)


ffuun("a", 1, 2, 3, 4, b="b")  # 이 경우는 가능