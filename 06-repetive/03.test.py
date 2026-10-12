# 식곤증 졸려

a, b, c = map(int, input("시작 값, 끝 값, 배수 입력, 띄어쓰기로 구분: ").split())
s = 0
count = 0
for i in range(a, b + 1):
    if i % c == 0:
        s += i
        count += 1
print(s, count)