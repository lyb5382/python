# Comprehension : 특히 리스트에서 많이 사용(list conprehension)
# for문이나 if문을 한줄로 작성
r = [0 for _ in range(100)]
print(r)
r = [10 for _ in range(100)]
print(r)
r = [i + 1 for i in range(100)]
print(r)
r = ["a" for _ in range(100)]
print(r)
d = [3, 5, 7, 9]
r = [d[i] ** 2 for i in range(len(d))]
# r = [i**2 for i in range(d)]
print(r)
# d = [int(input("정수 입력: ")) for _ in range(5)]
# print(sum(d))

# if와 for 혼합시 우선순위 for > if
# <explression> for 변수 in <interable>
r = []
for i in range(1, 5):
    if i % 2 == 0:
        r.append(i * 3)
r = [i * 3 for i in range(1, 20) if i % 2 == 0]
print(r)
r = ["짝수" if i % 2 == 0 else "홀수" for i in range(1, 6)]
print(r)

r = [(i, j) for i in [1, 2, 3] for j in [10, 20]]
print(r)

r = [(i, j) for i in range(1, 4) for j in range(1, 4) if (i + j) % 2 == 0]
print(r)

r = [(i, j) if (i + j) % 2 == 0 else (0, 0) for i in range(1, 4) for j in range(1, 4)]
print(r)

# unpacking
l = [(1, 11), (2, 21), (3, 31)]
for a, b in l:
    print(a + b)
print(*(a + b for (a, b) in l))
print([a + b for (a, b) in l])

# enumerate() : 인덱스 번호&데이터를 tuple로 반환
t = [1, 2, 3, 4, 5]
for i in enumerate(t):
    print(i)
for i, j in enumerate(t):
    print(f"{i} & {j}")

# zip() : 리스트 2개의 같은 인덱스끼리 묶어서 tuple로 반환 / 길이가 다르면 짧은거로 묶음
l1 = [10, 20, 30]
l2 = [100, 200, 300]
for i in zip(l1, l2):
    print(i)
for a, b in zip(l1, l2):
    print(a + b)