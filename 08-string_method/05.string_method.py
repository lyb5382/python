s1 = "Hi Im Yebin, and Im girl, Bye"

# 가운데 정렬
print("|" + s1.center(50) + "|")
print(s1.center(50, "|"))
# 오른쪽/왼쪽 정렬
print(s1.rjust(50))
print(s1.ljust(50) + "|")

s = "1\t2\n\t3"
print(s)
print(s.expandtabs()) # tap 대신 공백 숫자 만큼, 기본값 8개
print(repr(s))
print(repr(s.expandtabs()))
print(len(s))
print(len(s.expandtabs()))