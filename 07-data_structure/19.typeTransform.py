a = [1, 2, 3, 4, 5]
b = (6, 7, 8, 9, 10)
c = {11, 12, 13, 14, 15}
# list -> tuple | set
s1 = set(a)
t1 = tuple(a)
# tuple -> list | set
l1 = list(b)
s2 = set(b)
# set -> list | tuple
l2 = list(c)
t2 = tuple(c)
print(type(s1), type(t1), type(l1), type(s2), type(l2), type(t2))