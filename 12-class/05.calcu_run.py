# 다른 클래스 불러오기
# import calculator  전체 불러오기?
# from calculator import Cal  특정 클래스만 불러오기?

import calculator
c=calculator.Cal()
print(c.plus(10,10))

from calculator import Cal
c=Cal()
print(c.plus(10,10))

import calculator as cal
from calculator import Cal as cal
c=cal()
print(c.plus(10,10))