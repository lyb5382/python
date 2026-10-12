# 대입 연산자
a1 = 10
a1 = a1 + 10  # a1+=10
print(a1)
a1 -= 10
print(a1)
a1 *= 10
print(a1)
a1 /= 2
print(a1)
a1 %= 9
print(a1)
a1 //= 3
print(a1)
a1 = 10
a1 **= 3
print(a1)

a = int(input("파운드 입력: "))
a = a * 0.453592
print("%.2f" % a)
a = int(input("킬로그램 입력: "))
a = a * 2.204623
print("%.2f" % a)
print(f"{a:.2f}")
print("{:.2f}".format(a))
