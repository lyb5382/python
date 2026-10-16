import json


def enco(a):
    ecs = ["utf-8", "euc-kr", "cp949"]
    for i in ecs:
        try:
            with open(a, "r", encoding=i) as f:
                return i
        except UnicodeDecodeError:
            continue


# 한개의 데이터(딕셔너리)만 있을 때
fs = "11-file/data/data.json"
with open(fs, "r", encoding=enco(fs)) as f:
    data = json.load(f)

print(data)
print(type(data))
print(data["name"], data["skills"])

# 여러개의 경우
fs = "11-file/data/data2.json"
ac = ""
pd = []
with open(fs, "r", encoding=enco(fs)) as f:
    for i in f:
        i = i.strip()
        ac += i
        if i == "}":
            pd_d = json.loads(ac)
            pd.append(pd_d)
            ac = ""
print(pd)
for i in pd:
    print(i["name"], i["age"], i["skills"])

# 데이터에 여러줄바꿈 있을때
fs = "11-file/data/data3.json"
ac = ""
pd = []
with open(fs, "r", encoding=enco(fs)) as f:
    for i in f:
        if not i:
            continue
        i = i.strip()
        ac += i
        if i == "}":
            pd_d = json.loads(ac)
            pd.append(pd_d)
            ac = ""
print(pd)
for i in pd:
    print(i["name"], i["age"], i["skills"])