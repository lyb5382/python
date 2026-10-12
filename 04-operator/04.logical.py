# 논리연산자 : and or not xor(^/!=)

n1 = 100
n2 = 200
x = 7
y = 3
fr = n1 >= n2
tr = x >= y
print(f"False={fr}, True={tr}")

ar = fr and tr
print(ar)

orR = fr or tr
print(orR)

nr1 = not fr
print(nr1)

nr2 = not tr
print(nr2)

xr1 = fr ^ tr # 두 값이 다르면 True
xr2 = fr ^ fr
print(xr1, xr2)