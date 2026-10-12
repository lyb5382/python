s = 0
for i in range(1, 101):
    s += i
print(s)

s = 0
for i in range(1, 101, 5):
    if i % 5 == 0:
        s += i
print(s)

s = 0
for i in range(0, 101, 5):
    s += i
print(s)
