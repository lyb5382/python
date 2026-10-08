# 사용자에게 입력받기
a = input("입력: ")
print(a)

# a1 = input("점수1: ")
# a2 = input("점수2: ")
# print(int(a1 + a2))
# print(int(a1) + int(a2))
# print("%s+%s=%d" % (a1, a2, int(a1) + int(a2)))

a1 = int(input("점수1: "))
a2 = int(input("점수2: "))
print(a1 + a2)
print("%s+%s=%d" % (a1, a2, a1 + a2))
print("%s+%s=%s" % (a1, a2, a1 + a2))
print(f'{a1}+{a2}={a1+a2}')