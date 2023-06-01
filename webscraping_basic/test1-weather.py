##
from bs4 import BeautifulSoup
import requests
url ="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=iZcYqdp0JywssEqrzuGssssssU4-064836"
headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

res=requests.get(url , headers=headers)
soup = BeautifulSoup(res.text,'html.parser') 


datas = soup.find_all("section",attrs={"class":"sc_new cs_weather_new _cs_weather"})
print("[오늘의 날씨]")
for data in datas:
    temp = data.find("p").get_text().split()
    now = data.find(attrs={"class":"temperature_text"}).get_text().split()
    humid = data.find("dl").get_text().split()
    dust = data.find(attrs={"class":"today_chart_list"}).get_text().split()
    
    
    print(temp[3]+","+' '.join(temp[:3]))
    print(''.join(now))
    print(','.join(humid)) #['체감', '22.0°', '습도', '40%', '남서풍', '2.1m/s']
    print(dust[0]+"-"+dust[1]+","+dust[2]+"-"+dust[3])  #['미세먼지', '보통', '초미세먼지', '좋음', '자외선', '좋음', '일몰', '19:12']
    
# print(datas)


# 흐림 / 어제보다 ㅇㅇ도 높아요
# 현재 ㅇ도 / 최저 ㅇㅇ도 / 최고 ㅇㅇ도