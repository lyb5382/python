# 클래스 메소드


class Calc:
    @staticmethod  # self 필수 포함 X, 첫번째 변수 자리에 self를 넣지 않음
    def plus(x, y):
        print("스테이틱 메소드")
        return x + y

    def plu(s, x, y):
        print("인스턴스 메소드")
        return x + y

    def res(s, x, y):
        r1 = Calc.plu(x, y)
        r2 = s.plus(x, y)
        return r1 + r2


print(Calc.plus(10, 20))
c1 = Calc()
print(c1.plus(20, 20))
print(c1.plu(30, 20))