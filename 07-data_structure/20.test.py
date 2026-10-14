import random

n = int(input("몇 회?"))
for i in range(n):
    a = set()
    while len(a) < 6:
        a.add(random.randint(1, 45))
    print(*sorted(a))