s1 = "12345"
s2 = "python"
s3 = "p y t h o n"
s4 = "파이썬"
s5 = "123qwe"
s6 = "  "

# 숫자만으로 구성되어 있는지 검사
print(s1.isdigit(), s5.isdigit())
# 문자로만 검사
print(s2.isalpha(), s3.isalpha(), s5.isalpha())  # 공백도 미포함
# 문자|숫자 검사
print(s1.isalnum(), s2.isalnum(), s3.isalnum(), s4.isalnum(), s5.isalnum())
# 소문자 검사
print(s1.islower(), s2.islower(), s3.islower(), s5.islower(), s6.islower())
# 대문자 검사
s2 = s2.upper()
s3 = s3.upper()
s5 = s5.upper()
print(
    s1.isupper(), s2.isupper(), s3.isupper(), s4.isupper(), s5.isupper(), s6.isupper()
)
# 문자+숫자면 숫자는 무조건 True 되네? 한글도 True? 공백포함도?

# 문자열이 공백문자인지 검사
print(s3.isspace(), s6.isspace())

# 각 단어의 첫글자만 대문자?
s3 = "Python Ai"
print(s2.istitle(), s3.istitle())

# 빈자리 0으로 채우기
print(s1.zfill(20))