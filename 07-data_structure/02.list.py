import random

a = [1, 2, 3]
a[1] = ["a", "b", "c"]
print(a)
print(a[1][0])
b = [1, 2, 3, 4, 5]
b[1:3] = [1000]
print(b)
b[1:2] = [2, 3]
print(b)

a = [
    "명언1",
    "명언2",
    "명언3",
    "명언4",
    "명언5",
    "명언6",
    "명언7",
    "명언8",
    "명언9",
    "명언10",
]
print(random.choice(a))