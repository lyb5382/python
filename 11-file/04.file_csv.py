li = []
with open("11-file/test.csv", "r", encoding="utf-8") as f:
    # a = f.read().splitlines()
    # print(a)
    li.extend(i.strip().split(",") for i in f.readlines())

print(li)

for i in li:
    name, ko, en, ma = i
    a = int(ko) + int(en) + int(ma)
    avg = a / 3
    print(f"이름: {name}, 국어: {ko}, 영어: {en}, 수학: {ma}, 총점: {a}, 평균: {avg:.2f}")
    with open("11-file/rt.txt", "a", encoding="utf-8") as f:
        f.write(f"이름: {name}, 국어: {ko}, 영어: {en}, 수학: {ma}, 총점: {a}, 평균: {avg:.2f}\n")
