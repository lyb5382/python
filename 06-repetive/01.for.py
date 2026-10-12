for x in "abcdefg":
    print(x)

a = [1, 2, 3, 4]
for i in a:
    print(i)

print()

# range(시작값,종료값,step) -> 시작값 생략시=0, step 생략시=1
for i in range(5):
    print(i)

print()

for i in range(3, 10):
    print(i)

print()

for i in range(1, 10, 3):
    print(i)

print()

for i in range(1, 20, 2):
    print(i, end=", " if i != 19 else "")