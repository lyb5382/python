from datetime import datetime

print(datetime.now())

a = datetime(2026, 10, 8, 10, 0)
print(a)

print(f"{a:%y.%m.%d}")
print(f"{a.hour}.{a.minute}.{a.second}")
print(f"{a:%H.%M.%S}")

# H: 24시간 / I: 12시간 / p: AM, PM
print(f"{a:%I%p}")

# 일 수 계산
b = datetime(2026, 10, 1)
print(datetime.now() - b)
print((datetime.now() - b).days)