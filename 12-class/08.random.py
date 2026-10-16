# import 모듈명: 모듈명.명령어
# from 모듈명 import 함수|클래스명
import random

print(random.__file__)

from random import random
from random import randint
from random import randrange
from random import sample

print(random(), randint(0, 9), randrange(5, 10, 2), sep=" / ")
print(sample([1, 2, 3, 4, 5], 2))  # 정해진 샘플 중 몇개 뽑는거
print(chr(randint(65, 122)))  # 아스키코드 숫자->문자 변환