students = [[] for _ in range(3)]
students[0] = ["홍길동", 89, 100, 78, 76]
students[1] = ["아무개", 89, 100, 78, 76]
students[2] = ["이순신", 89, 100, 78, 76]

for i in range(len(students)):
    students[i].extend(
        [sum(students[i][1:]), sum(students[i][1:]) / (len(students[i]) - 1)]
    )

s = []
avg = []
for a in range(1, len(students[0]) - 2):
    total = sum(students[b][a] for b in range(len(students)))
    s.append(total)
    avg.append(total / len(students))

students.extend([["과목 합계"] + s, ["과목 평균"] + avg])
print(*students, sep="\n")

# for row in students:
#     name = row[0]
#     score = row[1:]
#     for i in range(4):
#         과목합계[i] += score[i]
#     h = sum(score)
#     avg = sum(score) / len(score)
# 과목평균 = [a / len(students) for a in 과목합계]