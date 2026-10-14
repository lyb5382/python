s1 = " ~ hi Im Yebin, and Im girl, Bye ~ "

# 앞뒤 공백 제거
print(s1.strip())
# 오른쪽 공백 제거
print(s1.rstrip())
# 왼쪽
print(s1.lstrip())

# 문자열 바꾸기
print(s1.replace("Im", "im"))
print(s1.replace("Im", "im", 1))
print(s1.replace(" ", "", 5))