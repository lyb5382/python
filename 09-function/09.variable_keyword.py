# 가변 키워드 인자(**kwargs) : 딕셔너리가 전달됨
def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


fun(a="A")
fun(a=1, b=2, c=3)
dic = {"a": "abc", "b": "def"}
fun(**dic)  # unpacking(**)하지 않으면 type error: 객체 1개(딕셔너리)만 넘겨줘서