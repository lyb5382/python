class Account:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    def getMoney(self):
        return self.__money

    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            print(self.name, self.__money, sep=': ')
        else:
            print("금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__money >= amount:
                self.__money -= amount
                print(self.name, self.__money, sep=': ')
            else:
                print("잔액이 부족합니다.")
        else:
            print("금액은 0보다 커야 합니다.")


ma = Account(input("이름 입력: "), int(input("예금액: ")))
ma.deposit(int(input("입금: ")))
ma.withdraw(int(input("출금: ")))