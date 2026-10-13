l1 = []
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
print(l1)

l2 = [1, 2, 3]
l2.append(4)
l2.append(5)
print(l2)

l3 = [1, 2, 3]
l3.append([4, 5])
print(l3)

l4 = [1, 2, 3]
l4.extend([4, 5])
print(l4)

l5 = []
for i in range(1, 1001):
    l5.append(i)
print(l5)