import requests
res=requests.get("http://naver.com")
res.raise_for_status() #올바른 문서 가져왔으면 문제가 없고 에러가 있으면 바로 오류 내뱉고 프로그램 끝낸다.
if res.status_code == 200:
    print(res)
    
    
print(len(res.text))

with open("naver.html", "w", encoding="utf8") as f:  #f라 이름짓고
    f.write(res.text)  # res.text 를 naver.html 파일로 만들어줌