import csv
import requests
from bs4 import BeautifulSoup

def generate_csv_data():
    url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
    filename = "amount list.csv"
    f = open(filename, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
    writer.writerow(title)

    for i in range(1,2):
        res = requests.get(url+str(i))
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        
        data_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
        for rows in data_rows:
            columns=rows.find_all("td")
            if len(columns)<=1:
                continue
            data=[column.get_text().strip() for column in columns]
            writer.writerow(data) 
            # print("*"*100)
            # print(data)
        
        # print(str(i)+"페이지")
        # print(soup.td)