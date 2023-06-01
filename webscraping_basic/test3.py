import csv
from openpyxl import workbook
import requests
from bs4 import BeautifulSoup


url ="https://www.mediajob.co.kr/recruit/recruit.htm?ctg=jikjong&jikjong=04000"
headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# datas = soup.find("ul",attrs={"class":"list list_vvip cols3"}).find_all("li")

# for data in datas:
#     company = data.find(attrs={"class":"wrap_rec wrap_rec_company"}).get_text().split()
#     subject = data.find(attrs={"class":"subject"}).get_text()
#     print(company)
#     print(subject)
    
# basic_datas = soup.find_all("table")
# for data in basic_datas:
#     subject = data.find("tr").find("td",attrs={"class":"company_name"})
#     print(subject)

basic_datas = soup.find_all("tr",attrs={"class":"in_recruit_list"})
for data in basic_datas:
    name = data.find(attrs={"class":"company_name"})
    content = data.a
    print(name.get_text())
    print(content.get_text())