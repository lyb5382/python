import random

x = random.random()
i = random.randint(1, 3)
print(x, i)

s = 0
while True:
    a, b, c = (random.randint(1, 6) for _ in range(3))
    print(a, b, c)
    if a == b == c:
        break
    s += 1
print(s)

a = random.randint(1, 6)
s = 0
while True:
    b = int(input("주사위의 숫자는? "))
    s += 1
    if a == b:
        break
    else:
        print("틀림. 다시!")
print(s, "회 만에 정답")