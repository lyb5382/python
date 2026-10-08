# str() 함수 : 데이터를 문자열로 변환

a = 5
b = 1.2
c = True
print(a, b, c, sep='\n')

# print('a'+a) 오류남
print('a='+str(a))
print(f'a={a}')

# 연산 우선순위 당연히 수학이랑 같음
y=2.5*2**2+3.3*2+6
print(y)