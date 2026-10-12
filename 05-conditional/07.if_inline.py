# 삼항 연산자

n1 = 7
print("2 맞음") if n1 == 2 else print("2 아님")
print("2 맞음" if n1 == 2 else "2 아님")

s = 75
r = "합격" if s >= 60 else "불합격"
print(r)

a, b = 10, 100
r = a if a > b else b
print(r)

# 회문: 왼쪽에서 읽어도 오른쪽으로 읽었을 때 같은 문자열 (예: 토마토)
str = "abcba"

if str == str[::-1]:
    print("회문 맞음!")
else:
    print("회문 아님!")
print(str, "회문 맞음!" if str == str[::-1] else "회문 아님!")