# set: 중복 불가, 순서(index)없음, {}사용, 빈 세트 만드려면 set()이렇게 생성해야 함({}는 딕셔너리)
a = {1, 2, 3, 1, 2, 3}
print(a, len(a))
b = {"a", 3, 5.5, True, (1, 2, 3)}
print(b)
c = set()
print(c, type(c))