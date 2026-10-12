age = int(input("나이 입력: "))

if age <= 0:
    print("???")
elif age > 19:
    print("성인")
elif age >= 15:
    print("청소년")
else:
    print("어린이")

if age <= 19:
    if age >= 15:
        print("청소년")
    else:
        print("어린이")
else:
    print("성인")