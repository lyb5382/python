# 기본환경: 모든 개발환경에 공통적으로 설치됨
# 가상환경: 특정 프로젝트에서만 사용하는 패키지 설치
# 가상환경 생성: 터미널에서 python -m venv 가상환경이름
# 활성화 명령어(cmd 기준): 이름\Scripts\activate
# 종료: deactivate
# requests: 외부 웹페이지에 접근하는 http 통신 라이브러리
import requests

def reget():
    a=requests.get('https://google.com')
    print(a.status_code, a.text)
    
if __name__ == '__main__':
    reget()