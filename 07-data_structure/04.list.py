sl = ["ko", "en", "ma", "his", "co"]
print(sl.index("en"))

a = "py"
if a in sl:
    print(sl.index(a))
else:
    print("X")

# 리스트 맨 뒤에 추가
sl.append("py")
print(sl)

# 리스트 중간에 삽입
sl.insert(1, "ai")
print(sl)

# 데이터 정렬 sort / sorted
print(sorted(sl))
print(sorted(sl, reverse=True))

sl.sort(reverse=True)
print(sl)

# 데이터 삭제
if a in sl:
    sl.remove(a)
    print(sl)
else:
    print("X")

# 모든 데이터 삭제
sl.clear()
print(sl)