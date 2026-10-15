p = [1000, 2000, 3000, 4000, 5000]
li = [(lambda a: a - a * 0.2)(i) for i in p]
print(li)