class TestCl:
    def area(self, h, b):
        return b * h / 2

    def inputM(self):
        self.n = input("이름 입력: ")
        self.p = int(input("파이썬 점수: "))
        self.a = int(input("AI 점수: "))

    def priM(self):
        print("이름:", self.n)
        print("파이썬:", self.p)
        print("AI:", self.a)
        print("합계:", self.p + self.a)
        print(f"평균: {(self.p + self.a) / 2:.1f}")