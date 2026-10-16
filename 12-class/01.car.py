# pass: 클래스 내부를 빈 상태로 만들때 사용
# 매개변수 self: 자기자신의 객체를 의미, 클래스 안에서 함수를 호출할 때


class Car:
    def car(s):
        s.model = "벤츠"
        s.color = "무광"
        s.speed = 10

    def speedUp(s):
        s.speed = 20

    def output(s):
        print("모델:", s.model)
        print("색상:", s.color)
        print("속력:", s.speed)


myCar = Car()
myCar.car() # 메소드를 호출 하며 변수 생성&초기화
myCar.output()
myCar.speedUp()
myCar.output()
print(myCar.model, myCar.color, myCar.speed)