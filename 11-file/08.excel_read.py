# pandas API : 데이터 분석 및 조작을 위한 라이브러리 / csv,excel,json,sql등 데이터 쉽게 읽어올 수 있음
# 결측지(빈 데이터) 채우기/삭제, 중복 데이터 제거, 타입 변환 등 전처리에 용이
# 대용량 데이터도 빠름

import pandas as pd

fn = "11-file/data/"
# 엑셀
ex = pd.read_excel(f"{fn}students.xlsx")
# ex=pd.read_excel('11-file/data/students.xlsx',sheet_name='시트 이름') / 시트 여러개일 경우
print(ex)
print(ex.head())  # 상위 5개만 불러옴

# json
ex = pd.read_json(f"{fn}data.json")
print(ex)

# 리스트로 된 json
ex = pd.read_json(f"{fn}data_list.json")
print(ex)
ex = pd.read_json(f"{fn}data_list2.json")
print(ex)

# 일반 json 모듈로 파일 내용을 딕셔너리로 가져오기
import json

with open(f"{fn}data.json", "r", encoding="utf-8") as f:
    dt = json.load(f)
df = pd.DataFrame([dt])
print(df)