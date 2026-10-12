a = int(input("점수 입력: "))

if a > 100 or a <0:
    print("0~100 사이의 값 입력")
elif a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")