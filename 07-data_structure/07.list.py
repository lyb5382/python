a = [100, 98, 68]
b = [89, 67, 99]
c = []
s = [0, 0, 0]

# for i in a:
#     s[0] += i

for i in range(3):
    c.append(int(input("점수 입력: ")))

s[0] = sum(a)
s[1] = sum(b)
s[2] = sum(c)

print(s, f"{sum(s) / len(s):.2f}")