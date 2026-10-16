# 클래스 변수: 모든 객체가 변수를 공유, class 바로 밑에 선언, Class.varname
# 인스턴스 변수: 자기자신 객체에서만 사용, 함수 안에 선언, self.varname


class Car:
    maker = "벤츠"

    def car(self):
        self.model = "스포츠"
        self.color = "무광"
        self.speed = 10

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def output(self):
        print(self.model, self.color, self.speed)


print(Car.maker)

mc = Car()
mc.car()
mc.output()

mc1 = Car()
mc1.car()
mc1.speedUp()
mc1.output()

mc.speedDown()
mc1.speedUp()
mc.output()
mc1.output()

print(Car.maker)
Car.maker = "아우디"
print(Car.maker)
print(mc.maker, mc1.maker)