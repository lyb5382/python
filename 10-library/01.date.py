from datetime import date

print(date.today())

birth = date(2003, 2, 27)
print(birth.strftime("%A"))
print(f"{birth:%Y.%m.%d}")
print(f"{birth:%y.%m.%d}")