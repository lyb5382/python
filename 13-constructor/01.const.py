# 생성자


class Car:
    def __init__(self, model, color, speed):
        print("생성자 호출")
        self.model = model
        self.color = color
        self.speed = speed

    def output(self):
        print(self.model, self.color, self.speed, sep=" / ")


mc = Car("모델", "색상", "속도")
mc.output()
mc2=Car('야발','개','졸려')
mc2.output()