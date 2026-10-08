# identity 연산자 : is(변수의 주소값이 같은지 검사) / is not(주소 다른지 검사) / id()(주소값 확인)

a=1
b=2
print(f'주소: {id(a)}')
print(f'주소: {id(b)}')
print(a is b)
print()
c=1
print(f'주소: {id(c)}')
print(a is c)

print(id(a))
print(id(c))