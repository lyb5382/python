def fun(a):
    for i in a:
        a[i] = int(input("정수 입력: "))


n = [i for i in range(5)]
fun(n)
print(n)


def funn(a):
    for x, y in enumerate(a):
        print(a[x], end="")

funn(n)