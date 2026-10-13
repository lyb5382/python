a = ["n", "a", "m", "e"]
b = [[] for _ in range(len(a))]
b[0].append(100)
b[0].append(90)
b[0].append(80)
b[1].append(70)
b[1].append(60)
b[1].append(50)
b[2].append(40)
b[2].append(30)
b[2].append(20)
b[3].append(10)
b[3].append(20)
b[3].append(30)

print(*((sum(b[i]), sum(b[i]) / len(b[i])) for i in range(len(b))))