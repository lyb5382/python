# {key:value} : key는 프라이머리

d1 = {"a": 1, "b": 1.2345, "c": "hi", "d": "py"}
print(d1["a"])
d1["e"] = "hihi"
print(d1)
d1["a"] = "hihi"
del d1["e"]
print(d1)
d1.clear()