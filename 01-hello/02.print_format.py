print(1, "&", 3)
print("집", "\n가고", "싶다")
print("-" * 15)
print("집" + "갈래")
print(1, "home")
# print(1+'home') X 타입이 맞아야 함
print(str(1) + "a")
print("-" * 15)
# 서식 : %d(정수), %f(실수), %s(문자열)
print("정수 : %d\n실수 : %f\n문자열 : %s" % (5, 1.2, "초코우유"))
print("-" * 15)
# 자리지정 : %자리수d(정수), %자리수f(실수), %자리수s(문자열)
print("정수 : %3d\n실수 : %1.3f\n문자열 : %4s" % (5, 1.23, "배고파"))
print("소수점 둘째자리까지 : %.2f, %.2f, %.2f" % (9.87, 10.01, 345352.48599))
# sep 속성
# : 분리 문자 설정 - 기본값은 공백 문자 하나
print(5, 1.2, "a", False)
print(5, 1.2, "a", False, sep=" / ")  # 공백문자 대신 넣은 것 사용
print(5, 1.2, "a", False, sep=", ")
print("-" * 15)
print("오늘은 목요일 입니다.\n\t내일은 공휴일 개꿀")
# end 속성 : 마지막 문자 설정
print("hihihi", end="\n")
print("hihihi", end="")
print("hihihi", end="\t")
print("hihihi")
print("-" * 15)
# format
print("{},{},{}".format(100, "a", 12.3))
print("{1},{0},{2}".format(100, "a", 12.3))
print("이름 : {}, 나이 : {}, data={}".format("이예빈", 24, 1.234))
print("이름 : {1}, 나이 : {0}, data={2}".format(24, "이예빈", 1.234))
print(format(1.23))
print(format(1.23456,'.2f'))
print('원주율 =', format(3.14))
print('원주율 = {}'.format(3.14))
print('원주율 = {}'.format(3.14))
print('원주율 =', format(3.1415, '.2f'))
print('정수 =', format(30000,'7d'))
print('정수 =', format(300,'7d'))
print('정수 =', format(30000,'3,d'))

# f-string
# 문자열을 만드는 따옴표(' ")앞에 알파벳 f(F)를 붙여줌
# 문자열 내부에 변수를 넣고 싶은 자리에 {변수명}을 적음
print('합은',3+5,'이다')
print('합은 '+str(3+5)+' 이다')
print('합은 %d 이다'%(3+5))
print(f'합은 {3+5} 이다')