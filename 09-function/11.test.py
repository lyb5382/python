def caf(menu, size="small"):
    print(f"메뉴: {menu}, 사이즈: {size}")


def deli(name, addr, num):
    print(name, addr, num)


def pay(*args):
    s = 0
    for i in args:
        s += i
    return s


def user(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}: {j}")


caf("아샷추")
deli(addr="강남", name="뉸늉", num="1234")
print(pay(1000, 1500, 3500))
a = {"name": "이름", "pwd": "비밀번호", "email": "abc@gmail.com"}
b = {"name": "하이", "pwd": "123qwe"}
user(**a)
user(**b)