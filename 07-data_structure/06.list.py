li = [int(input("정수 입력: ")) for _ in range(4)]

s = 0
for i in range(len(li)):
    s += li[i]
print(li, s)

# 빈 리스트는 값 바로 넣기 불가
li = []
for i in range(4):
    li.append(int(input("정수 입력: ")))
print(li, sum(li))