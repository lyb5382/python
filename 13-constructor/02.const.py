class Car:
    def __init__(self, speed='속도', color="색상", model="모델"):
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print(self.model, self.color, self.speed, sep=" / ")
        
mc = Car()
mc.output()