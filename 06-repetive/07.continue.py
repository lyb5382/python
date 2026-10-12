x = 1
while True:
    print(x)
    x += 1
    if x == 6:
        x += 2
        continue
    if x == 10:
        break

a = 0
for i in range(1, 101):
    if i % 4 == 0:
        continue
    a += i
print(a)