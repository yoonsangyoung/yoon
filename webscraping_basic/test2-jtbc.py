import csv
import requests
from bs4 import BeautifulSoup


f = open("news_ranking.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
writer.writerow(['날짜', '순위', '기사 제목', '링크'])

# with open('jtbc_news.csv', mode='w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["날짜", "랭킹", "기사제목", "기사링크"])

for i in range(1,25):
    url ="https://news.jtbc.co.kr/ranking/ranking_news.aspx?pdate=202304{:02}&jt=NV&sc=00&sd=4".format(i)
    headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    datas = soup.find("ol").find_all("li")    
    

    for idx,data in enumerate(datas):
        subject = data.find("a",attrs={"class":"title_cr"})
        link = data.p.a["href"]
        
        print("4월"+str(i)+"일"+str(idx+1)+"번"+subject.get_text())
        print(link)
        row = ['4월'+str(i)+'일', idx+1, subject.get_text().strip(), link]
        writer.writerow(row)
