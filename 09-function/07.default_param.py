def fun(a="", b=""):
    print(a, b)


fun("a", "b")
fun()


def funn(a, b, c="1", d="2"):
    print(a, b, c, d)


funn("a", "b")


# 가변객체 사용 불가
def aaa(a, b="hi", c=[]):
    c.append(1)
    print(a, b, c)


aaa("yo", "skrr")  # c 변수 전달시 오류


def aab(a, b="hi", c=None):
    if c == None:
        c=1
    print(a, b, c)


aab("yo", "skrr", 2)