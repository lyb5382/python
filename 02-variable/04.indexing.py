# index번호가 -면 뒤에서부터 시작 단 -0 없음 당연함 
a='abcdefghijk'
print(a[0])
print(a[3])
print(a[5])
print()
print(a[-1])
print(a[-3])
print(a[-5])
print()

# 슬라이싱
# [시작:끝:step] -> 생략하면 1씩
print(a[1:3])
print(a[:3]) # 0부터 시작
print(a[1:]) # 끝까지
print(a[:]) # 전부다 (근데 왜 씀?)
print(a[0:9:2])
print(a[1:9:2])
print(a[::-1]) # 역순 (문자열 뒤집기)
print(a[5:1:-2]) # 3번째 자리 양수면 오류
print(a[-1:-8:-1])
print()

# 문자열 연결
b1='ab'
b2=a+b1
print(b2)

# 문자열 반복
c = b1 * 3
print(c)
print()

# 문자열 문자수 확인
print(len(a))

# indexing에서는 문자 변경 못 함
# a[0]='z' 오류
a='z'+a[1:]
print(a)
print()

a=a[:2]+'아'+a[4:]
print(a)