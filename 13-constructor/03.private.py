class Car:
    def __init__(self, m="모델", c="색상", s="속력", mk="메이커"):
        self.m = m
        self.c = c
        self.s = s
        self.__mk = mk

    def output(self):
        print(self.m, self.c, self.s, self.__mk, sep=" / ")

    def getMk(self):  # private를 읽을 수 있게 해줌
        return self.__mk

    def setMk(self, mk):
        self.__mk = mk


mc = Car()
mc.output()
# print(mc.__mk) 오류!
print(mc.getMk())
# mc.__mk='하이' 오류는 안 나지만 안 바뀜