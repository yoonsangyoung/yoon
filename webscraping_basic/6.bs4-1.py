import requests
from bs4 import BeautifulSoup
headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"}

url = "https://weather.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #가져온 html 문서를 lxml 통해서 뷰티플숲 객체로 만듬


print(soup.a) #첫번째로 발견 되는 a엘리먼트 반환
print(soup.a.attrs) # a엘리먼트의 속성정보
print(soup.find("a", attrs={"class":"nav"}))   # a태그에 해당하는 속성-클래스 찾는다.
print(soup.find(attrs={"class:GlobalNavigationBar__link--WMOzG"}))
print(soup.a["href"]) # a 대괄호 사이에 속성값 넣으면 a엘리먼트의 속성값 정보 출력할수 있다.

ex1 = soup.find("li", attrs={"class":"nav_item"})
ex2 = ex1.next_sibling.next_sibling.get_text()

times=soup.find_all("a",attrs={"class":"data top  _cnItemTime"})
# class 속성이 data top  _cnItemTim인 모든 "a" element 를 반환



# itemlists=soup.find_all("p",attrs={"class":"name"})
# for item in itemlists:
#     print(item.get_text())
    
# items=soup.find_all(attrs={"class":"item_inner"})
# print(items)