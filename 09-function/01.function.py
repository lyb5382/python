# 함수: 클래스 바깥에 독립적으로 존재, 이름으로 호출
# 메소드: 클래스 내부에 정의됨, 객체로 호출


def fun1():
    print("hi")
def fun2(a, b):
    return a+b

fun1()
print(fun2(1,2))