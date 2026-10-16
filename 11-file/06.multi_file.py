from pathlib import Path

# 읽어올 폴더 지정
dd = Path("11-file/output")
tf = dd.glob("*.txt")

for i in tf:
    print(i.name)
    with open(i, "r", encoding="utf-8") as f:
        fn = f.read()
        print(fn)