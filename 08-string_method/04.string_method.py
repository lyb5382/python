s1 = "Hi Im Yebin, and Im girl, Bye"

# 분리 (기본값 ' '), 리스트로 반환
print(s1.split())
print(s1.split(", "))  # 해당 문자열은 포함 x
# print(s1.split(2)) --- x
print(s1.split(maxsplit=2))

print(" ".join(s1.split()))