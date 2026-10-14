# return값이 2개 이상 시 tuple로 반환
def abc():
    a = 1 + 2
    b = 2 * 3
    return (a, b)


a = abc()
print(a[0], a[1])
a, b = abc()
print(a, b)