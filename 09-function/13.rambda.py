# 함수 줄여쓰기: 함수명=lambda 매개변수:수행코드(한줄만 가능)


def fun(a):
    return a**2


fun = lambda a: a**2

funn = lambda a: print(a)

funn(10)

print((lambda a: a)(5))
(lambda: print("hi"))()  # 이름 없어도 실행되게 하는 것(맨 뒤 괄호가 함수 실행 요소)
(lambda a: print(a * 2))(10)  # 함수 호출&실행시 fun() <- 같은 개념

li = [(lambda a: a**2)(i) for i in range(1, 10)]
print(li)