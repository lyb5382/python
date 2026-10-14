s1 = "hi Im Yebin, and Im girl, Bye"

# 문자열에서 특정 문자(열) 개수
print(s1.lower().count("im"))

# 문자열 검색(왼쪽 시작) : 문자열 첫 시작의 인덱스 번호
print(s1.lower().find("im"))
print(s1.lower().find("he"))  # 없는거 : -1
# 오른쪽에서 검색
print(s1.lower().rfind("im"))
print(s1.lower().rfind("im", 0, 18))  # 찾을거, 시작 인덱스, 끝 인덱스(끝 번호 포함 안함)
# index(): fine와 같음 but 값 없으면 예외 발생
# print(s1.lower().index('boy'))
print(s1.lower().index("im"))

# 시작 단어 검사
print(s1.lower().startswith("im"))
print(s1.lower().startswith("im", 3))
# 끝 단어 검사
print(s1.lower().endswith("im"))
print(s1.lower().endswith("im", 0, 19))