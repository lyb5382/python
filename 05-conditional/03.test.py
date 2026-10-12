a = int(input("정수 입력: "))

if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

x, y = map(int, input('정수 2개 입력(띄어쓰기로 구분): ').split())

if x > y:
    print(f'{x}이/가 더 크다')
elif y > x:
    print(f'{y}이/가 더 크다')
else:
    print(f'똑같잖아')

if y > x:
    x, y = y, x #자리 바꿈
print(f'{x}이/가 {y}보다 더 크다')