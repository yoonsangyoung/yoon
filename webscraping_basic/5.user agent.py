import requests
headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"}
res=requests.get("http://naver.com",headers=headers)
res.raise_for_status()

with open("naver.html", "w", encoding="utf8") as f:  #f라 이름짓고
    f.write(res.text)  # res.text 를 naver.html 파일로 만들어줌