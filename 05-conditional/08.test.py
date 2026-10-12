a = int(input("정수1 입력: "))
b = int(input("정수2 입력: "))
c = input("연산자 입력(+,-,*,/,//,%,**): ")

if c == "+":
    print(a + b)
elif c == "-":
    if b > a:
        a, b = b, a
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b > a:
        a, b = b, a
    print(a / b)
elif c == "//":
    if b > a:
        a, b = b, a
    print(a // b)
elif c == "%":
    if b > a:
        a, b = b, a
    print(a % b)
elif c == "**":
    print(a**b)

a = int(input("정수 입력: "))

if a > 0:
    print("양수 & 짝수" if a % 2 == 0 else "양수 & 홀수")
elif a == 0:
    print("0입니다")
else:
    print("음수 & 짝수") if a % 2 == 0 else print("음수 & 홀수")