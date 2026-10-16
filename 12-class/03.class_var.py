class Hi:
    msg = "hihi"  # 클래스 변수

    def eng(s):
        s.msg = "bye"  # 인스턴스 변수

    def kor(s):
        s.msg = "하이"

    def loc(s):
        msg = "whffu"  # 지역변수
        print(msg)

    def pri(s):
        print(Hi.msg, s.msg)
        
hi1=Hi()
hi1.pri()

hi1.eng()
hi1.pri()