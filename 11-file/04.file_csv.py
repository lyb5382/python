li = []
with open("11-file/test.csv", "r", encoding="utf-8") as f:
    # a = f.read().splitlines()
    # print(a)
    b = f.readlines()
    li.extend(i.strip().split(",") for i in b)

print(li)