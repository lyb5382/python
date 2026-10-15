with open("11-file/test.txt", "r", encoding="utf-8") as f:
    a = f.read()  # 전체내용 읽음
    print(a)
    b = a.split("\n")
    print(b)

with open("11-file/test1.txt", "r", encoding="utf-8") as f:
    print(f.readline())  # 한줄만 읽음

with open("11-file/test1.txt", "r", encoding="utf-8") as f:
    print(f.readlines())  # 한줄씩 리스트로 저장 후 반환
    print(f.read().splitlines())