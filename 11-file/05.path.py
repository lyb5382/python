# mkdir
from pathlib import Path

# 경로 저장?
a = Path("11-file/output/test.txt")
# output 폴더 없어도 만들어주기?
a.parent.mkdir(parents=True, exist_ok=True)
with open(a, "w") as f:
    f.write("hi")

with open("11-file/test3.txt", "w", encoding="utf-8") as f:
    f.write("땅끝 땅끝도\n별끝 별끝도\n너를 따라갈 준비 돼있어")
with open("11-file/test3.txt", "r", encoding="utf-8") as f:
    print(f.read())