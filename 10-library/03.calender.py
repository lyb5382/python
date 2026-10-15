import calendar

print(calendar.calendar(2003))
print(calendar.month(2003, 2))

# 윤년 계산
print(calendar.isleap(2003), calendar.isleap(2024))