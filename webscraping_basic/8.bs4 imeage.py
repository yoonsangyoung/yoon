import csv
import requests
from bs4 import BeautifulSoup


headers ={"User-Agent":"ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}


for year in range(2018,2023):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res=requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    imeages = soup.find_all("img",attrs={"class":"thumb_img"})

    for idx,imeage in enumerate(imeages):
        if idx <=4:
            img_data = requests.get(imeage["src"]).content
            with open("movie{}.{}.jpg".format(year,idx+1), "wb") as f:
                f.write(img_data)
                
            # f = open(filename, "w", encoding="utf-8-sig", newline="")
            # writer = csv.writer(f)