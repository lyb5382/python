s = {1, 2, 3, 1, 2, 3, 4, 5, 4, 5}
print(2 in s)
# 데이터 추가
s.add(6)
print(s)
# update
s.update({5, 7, 8, 9})
print(s)
# 개별 삭제
s.remove(2)
print(s)
# 전체 삭제
s.clear()