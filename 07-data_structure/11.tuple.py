a = ("ko", "py", "ai", "ma", "en")
print(a[2], a[::2], a[-1], a[::-1])
print(a.index("py"))

t1 = 1, 2, 3, 4, 5
print("%d, %d, %d, %d, %d" % (t1[0], t1[4], t1[2], t1[1], t1[3]))
print(f"{t1[0]} {t1[4]}")
print("{0}{3}{2}{1}".format(t1[0], t1[1], t1[2], t1[3]))

# unpacking: tuple(list 등)의 내용만 출력 / *변수명
print("{3}{0}{2}".format(*t1))
print("{}{}{}".format(*t1[2:5]))
print(*t1[:3])
print(t1[:3])

t2 = 12.3456, 1.2345, 23.4567, 1.23431
print("{:.2f}/{:.1f}/{:.3f}".format(*t2))

for i in range(len(t2)):
    if i < len(t2) - 1:
        print("{:.2f}".format(t2[i]), end=", ")
    else:
        print("{:.2f}".format(t2[i]))

# join(): 여러개의 문자열을 하나로 합칠때 사용하는 메소드 / '구분자'.join(문자열이 담긴 리스트나 튜플)
x = ["a", "b", "c"]
print("/".join(x))
print(" / ".join(f"{i:.2f}" for i in t2))

t3 = 10, 20, 30
a, b, c = t3
print(a, b, c)

a, b = t3[:2]
print(a, b)