import random


def cur(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    else:
        return '오류'

def scr(a, b):
    return (a + b) / 2


def rot(a):
    for _ in range(a):
        k = set()
        while len(k) < 6:
            k.add(random.randint(1, 45))
        print(*k)


def pas():
    while True:
        a = input("비밀번호 생성(8글자 이상, 문자&숫자만 허용): ")
        if len(a) >= 8 and a.isalnum():
            print("비밀번호가 생성되었습니다.", a)
            break
        else:
            print("오류. 비밀번호가 규칙에 맞지 않습니다.")


a = int(input("정수 입력: "))
b = int(input("정수 입력: "))
c = input("기호 입력(+, -, *): ")
print(cur(a, b, c))
ko = int(input("국어 점수: "))
en = int(input("영어 점수: "))
print(f"{scr(ko, en):.2f}")
rot(int(input("로또 횟수: ")))
pas()