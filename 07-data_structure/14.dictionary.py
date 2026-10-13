d1 = {"a": 1, "b": 1.2345, "c": "hi", "d": "py"}

if "c" in d1:
    print(d1["c"])
else:
    d1["c"] = "hihihi"

# items(): 딕셔너리의 키와 값 묶어서 가져오는 함수
for key, value in d1.items():
    print(key, value)
print()
for key in sorted(d1.keys(), reverse=True):
    print(key, d1[key])

d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
for v in sorted(d1.values()):
    print(v)

d2 = {"e": 5, "f": 6}
# d1['g']=d2
d1.update(d2)
print(d1)