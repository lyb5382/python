# 파일 열기
f = open("test.txt", "w", encoding="utf-8")  # w=쓰기모드라는 뜻
# 파일 쓰기
# f.write('home\nsweet\nhome')  # 덮어쓰기 됨

for i in range(1, 11):
    f.write(f"{i}: 집 보내줘 힝\n")
f.close()

with open("test1.txt", "w") as f:  # 알아서 파일 닫힘
    for i in range(1, 6):
        f.write("home sweet home\n")