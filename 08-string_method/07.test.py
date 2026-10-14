pn = input("번호 입력(000-0000-0000): ")
pn = pn.replace("-", "")
print(pn.isdigit())
print(pn.count("0"))