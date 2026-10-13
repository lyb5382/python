work = 4, 5, 3, 4
s = sum(work)
sun = work[2], work[3]
lwork = 5, *work[1:]
print(s, sun, lwork)