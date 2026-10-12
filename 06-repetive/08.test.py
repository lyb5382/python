while True:
    a = int(input("단 입력: "))
    for i in range(1, 10):
        print(f"{a} * {i} = {a*i}")
    b = input("계속 출력하려면 y 입력: ")
    if b.lower() == "y":
        continue
    else:
        break