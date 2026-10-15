with open('11-file/test1.txt','a', encoding="utf-8") as f:
    f.write('덮어쓰기 안 하고 쓰기')
    
with open('11-file/test2.txt','x', encoding="utf-8") as f:
    f.write('덮어쓰기 막기, 같은 파일이 존재하지 않을때만 가능')