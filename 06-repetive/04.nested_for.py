for i in range(3):
    for j in range(2):
        print(i, j)
print()

for i in range(2, 10):
    print("{:^10}".format(f"{i}단"))
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
print()

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {i*j:2d}", end="   ")
    print()