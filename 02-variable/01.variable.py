# 변수 : 자료형 안 씀 개꿀
a = '안녕'
print(a)
print(id(a))

a=100
print(a)
print(id(a))
# 변수명 : 예약어 불가, 당연함.
# 변수가 무엇인지 알 수 있게 이름 정하기
# python의 자료 크기는 상관 없음(정하지 않아도 됨) 유동적 개편함
a = '집'
b = 'home'
c = True
print(type(a))
print(f'자료형 = {type(a)}')
print(type(b))
print(type(c))

# int a=1, b=2, c=3
d, e, f = 9, 8, 7
print(d, e, f)

g, h, i = '집', '가고', '싶다'
print(g, h, i)