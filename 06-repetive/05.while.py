s = 0
i = 1
while i < 101:
    s += i
    i += 1
print(s)

s = 0
i = 1
while True:
    s += i
    i += 1
    if i > 100:
        break
print(s)